import type { AutoGrader } from './graders';

export const CORE_CONCEPT_EXPANSION_GRADERS: Record<number, AutoGrader> = {
  "6608": {
    "functionNames": [
      "default_if_none_1"
    ],
    "tests": [
      {
        "args": [
          null
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
          ""
        ],
        "expected": ""
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6609": {
    "functionNames": [
      "default_if_none_2"
    ],
    "tests": [
      {
        "args": [
          null
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
          ""
        ],
        "expected": ""
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6610": {
    "functionNames": [
      "default_if_none_3"
    ],
    "tests": [
      {
        "args": [
          null
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
          ""
        ],
        "expected": ""
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6611": {
    "functionNames": [
      "default_if_none_4"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6612": {
    "functionNames": [
      "default_if_none_5"
    ],
    "tests": [
      {
        "args": [
          null
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
          ""
        ],
        "expected": ""
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6613": {
    "functionNames": [
      "none_count_plus_1"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
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
            false,
            null
          ]
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6614": {
    "functionNames": [
      "none_count_plus_2"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
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
            false,
            null
          ]
        ],
        "expected": 3
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6615": {
    "functionNames": [
      "none_count_plus_3"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
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
            false,
            null
          ]
        ],
        "expected": 4
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6616": {
    "functionNames": [
      "none_count_plus_4"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
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
            false,
            null
          ]
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6617": {
    "functionNames": [
      "none_count_plus_5"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
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
            false,
            null
          ]
        ],
        "expected": 6
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6618": {
    "functionNames": [
      "truthy_count_plus_1"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            "x"
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
            false,
            [],
            3
          ]
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "bool",
        "minArgs": 0
      }
    ]
  },
  "6619": {
    "functionNames": [
      "truthy_count_plus_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            "x"
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
            false,
            [],
            3
          ]
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "bool",
        "minArgs": 0
      }
    ]
  },
  "6620": {
    "functionNames": [
      "truthy_count_plus_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            "x"
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
            false,
            [],
            3
          ]
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "bool",
        "minArgs": 0
      }
    ]
  },
  "6621": {
    "functionNames": [
      "truthy_count_plus_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            "x"
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
            false,
            [],
            3
          ]
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "bool",
        "minArgs": 0
      }
    ]
  },
  "6622": {
    "functionNames": [
      "truthy_count_plus_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            "x"
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
            false,
            [],
            3
          ]
        ],
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "bool",
        "minArgs": 0
      }
    ]
  },
  "6623": {
    "functionNames": [
      "first_truthy_or_1"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            "",
            7,
            8
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            0,
            false,
            ""
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            "x",
            2
          ]
        ],
        "expected": "x"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6624": {
    "functionNames": [
      "first_truthy_or_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            "",
            7,
            8
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            0,
            false,
            ""
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            "x",
            2
          ]
        ],
        "expected": "x"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6625": {
    "functionNames": [
      "first_truthy_or_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            "",
            7,
            8
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            0,
            false,
            ""
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            "x",
            2
          ]
        ],
        "expected": "x"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6626": {
    "functionNames": [
      "first_truthy_or_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            "",
            7,
            8
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            0,
            false,
            ""
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          [
            "x",
            2
          ]
        ],
        "expected": "x"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6627": {
    "functionNames": [
      "first_truthy_or_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            "",
            7,
            8
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            0,
            false,
            ""
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            "x",
            2
          ]
        ],
        "expected": "x"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6628": {
    "functionNames": [
      "replace_none_1"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            "",
            2
          ]
        ],
        "expected": [
          1,
          0,
          "",
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
            false,
            null
          ]
        ],
        "expected": [
          false,
          1
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6629": {
    "functionNames": [
      "replace_none_2"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            "",
            2
          ]
        ],
        "expected": [
          2,
          0,
          "",
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
            false,
            null
          ]
        ],
        "expected": [
          false,
          2
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6630": {
    "functionNames": [
      "replace_none_3"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            "",
            2
          ]
        ],
        "expected": [
          3,
          0,
          "",
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
            false,
            null
          ]
        ],
        "expected": [
          false,
          3
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6631": {
    "functionNames": [
      "replace_none_4"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            "",
            2
          ]
        ],
        "expected": [
          4,
          0,
          "",
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
            false,
            null
          ]
        ],
        "expected": [
          false,
          4
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6632": {
    "functionNames": [
      "replace_none_5"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            "",
            2
          ]
        ],
        "expected": [
          5,
          0,
          "",
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
            false,
            null
          ]
        ],
        "expected": [
          false,
          5
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6633": {
    "functionNames": [
      "truthy_with_marker_1"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            2
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
          []
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          [
            false,
            "ok"
          ]
        ],
        "expected": [
          "ok",
          1
        ]
      }
    ]
  },
  "6634": {
    "functionNames": [
      "truthy_with_marker_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            2
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
          []
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          [
            false,
            "ok"
          ]
        ],
        "expected": [
          "ok",
          2
        ]
      }
    ]
  },
  "6635": {
    "functionNames": [
      "truthy_with_marker_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
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
          []
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            false,
            "ok"
          ]
        ],
        "expected": [
          "ok",
          3
        ]
      }
    ]
  },
  "6636": {
    "functionNames": [
      "truthy_with_marker_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            2
          ]
        ],
        "expected": [
          1,
          2,
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
            false,
            "ok"
          ]
        ],
        "expected": [
          "ok",
          4
        ]
      }
    ]
  },
  "6637": {
    "functionNames": [
      "truthy_with_marker_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            "",
            2
          ]
        ],
        "expected": [
          1,
          2,
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
            false,
            "ok"
          ]
        ],
        "expected": [
          "ok",
          5
        ]
      }
    ]
  },
  "6638": {
    "functionNames": [
      "both_present_1"
    ],
    "tests": [
      {
        "args": [
          0,
          ""
        ],
        "expected": true
      },
      {
        "args": [
          null,
          1
        ],
        "expected": false
      },
      {
        "args": [
          2,
          null
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6639": {
    "functionNames": [
      "both_present_2"
    ],
    "tests": [
      {
        "args": [
          0,
          ""
        ],
        "expected": true
      },
      {
        "args": [
          null,
          1
        ],
        "expected": false
      },
      {
        "args": [
          2,
          null
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6640": {
    "functionNames": [
      "both_present_3"
    ],
    "tests": [
      {
        "args": [
          0,
          ""
        ],
        "expected": true
      },
      {
        "args": [
          null,
          1
        ],
        "expected": false
      },
      {
        "args": [
          2,
          null
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6641": {
    "functionNames": [
      "both_present_4"
    ],
    "tests": [
      {
        "args": [
          0,
          ""
        ],
        "expected": true
      },
      {
        "args": [
          null,
          1
        ],
        "expected": false
      },
      {
        "args": [
          2,
          null
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6642": {
    "functionNames": [
      "both_present_5"
    ],
    "tests": [
      {
        "args": [
          0,
          ""
        ],
        "expected": true
      },
      {
        "args": [
          null,
          1
        ],
        "expected": false
      },
      {
        "args": [
          2,
          null
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6643": {
    "functionNames": [
      "coalesce_1"
    ],
    "tests": [
      {
        "args": [
          null,
          8
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          9
        ],
        "expected": 0
      },
      {
        "args": [
          null,
          null
        ],
        "expected": 1
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6644": {
    "functionNames": [
      "coalesce_2"
    ],
    "tests": [
      {
        "args": [
          null,
          8
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          9
        ],
        "expected": 0
      },
      {
        "args": [
          null,
          null
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6645": {
    "functionNames": [
      "coalesce_3"
    ],
    "tests": [
      {
        "args": [
          null,
          8
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          9
        ],
        "expected": 0
      },
      {
        "args": [
          null,
          null
        ],
        "expected": 3
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6646": {
    "functionNames": [
      "coalesce_4"
    ],
    "tests": [
      {
        "args": [
          null,
          8
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          9
        ],
        "expected": 0
      },
      {
        "args": [
          null,
          null
        ],
        "expected": 4
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6647": {
    "functionNames": [
      "coalesce_5"
    ],
    "tests": [
      {
        "args": [
          null,
          8
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          9
        ],
        "expected": 0
      },
      {
        "args": [
          null,
          null
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6648": {
    "functionNames": [
      "none_indexes_from_1"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
          ]
        ],
        "expected": [
          1,
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
            1,
            null
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6649": {
    "functionNames": [
      "none_indexes_from_2"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
          ]
        ],
        "expected": [
          2,
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
            1,
            null
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6650": {
    "functionNames": [
      "none_indexes_from_3"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
          ]
        ],
        "expected": [
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
            1,
            null
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6651": {
    "functionNames": [
      "none_indexes_from_4"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
          ]
        ],
        "expected": [
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
            1,
            null
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6652": {
    "functionNames": [
      "none_indexes_from_5"
    ],
    "tests": [
      {
        "args": [
          [
            null,
            0,
            null
          ]
        ],
        "expected": [
          5,
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
            1,
            null
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6653": {
    "functionNames": [
      "truthy_keys_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 0
          }
        ],
        "expected": [
          "a",
          "marker_1"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "marker_1"
        ]
      },
      {
        "args": [
          {
            "x": "",
            "y": true
          }
        ],
        "expected": [
          "marker_1",
          "y"
        ]
      }
    ]
  },
  "6654": {
    "functionNames": [
      "truthy_keys_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 0
          }
        ],
        "expected": [
          "a",
          "marker_2"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "marker_2"
        ]
      },
      {
        "args": [
          {
            "x": "",
            "y": true
          }
        ],
        "expected": [
          "marker_2",
          "y"
        ]
      }
    ]
  },
  "6655": {
    "functionNames": [
      "truthy_keys_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 0
          }
        ],
        "expected": [
          "a",
          "marker_3"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "marker_3"
        ]
      },
      {
        "args": [
          {
            "x": "",
            "y": true
          }
        ],
        "expected": [
          "marker_3",
          "y"
        ]
      }
    ]
  },
  "6656": {
    "functionNames": [
      "truthy_keys_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 0
          }
        ],
        "expected": [
          "a",
          "marker_4"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "marker_4"
        ]
      },
      {
        "args": [
          {
            "x": "",
            "y": true
          }
        ],
        "expected": [
          "marker_4",
          "y"
        ]
      }
    ]
  },
  "6657": {
    "functionNames": [
      "truthy_keys_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 0
          }
        ],
        "expected": [
          "a",
          "marker_5"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "marker_5"
        ]
      },
      {
        "args": [
          {
            "x": "",
            "y": true
          }
        ],
        "expected": [
          "marker_5",
          "y"
        ]
      }
    ]
  },
  "6658": {
    "functionNames": [
      "is_none_check_1"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": true
      },
      {
        "args": [
          0
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
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6659": {
    "functionNames": [
      "is_none_check_2"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": true
      },
      {
        "args": [
          0
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
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6660": {
    "functionNames": [
      "is_none_check_3"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": true
      },
      {
        "args": [
          0
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
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6661": {
    "functionNames": [
      "is_none_check_4"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": true
      },
      {
        "args": [
          0
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
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6662": {
    "functionNames": [
      "is_none_check_5"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": true
      },
      {
        "args": [
          0
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
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6663": {
    "functionNames": [
      "is_not_none_check_1"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6664": {
    "functionNames": [
      "is_not_none_check_2"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6665": {
    "functionNames": [
      "is_not_none_check_3"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6666": {
    "functionNames": [
      "is_not_none_check_4"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6667": {
    "functionNames": [
      "is_not_none_check_5"
    ],
    "tests": [
      {
        "args": [
          null
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "IsNot"
    ]
  },
  "6668": {
    "functionNames": [
      "equal_after_offset_1"
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
          0,
          1
        ],
        "expected": true
      },
      {
        "args": [
          3,
          9
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6669": {
    "functionNames": [
      "equal_after_offset_2"
    ],
    "tests": [
      {
        "args": [
          2,
          4
        ],
        "expected": true
      },
      {
        "args": [
          0,
          2
        ],
        "expected": true
      },
      {
        "args": [
          3,
          9
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6670": {
    "functionNames": [
      "equal_after_offset_3"
    ],
    "tests": [
      {
        "args": [
          2,
          5
        ],
        "expected": true
      },
      {
        "args": [
          0,
          3
        ],
        "expected": true
      },
      {
        "args": [
          3,
          9
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6671": {
    "functionNames": [
      "equal_after_offset_4"
    ],
    "tests": [
      {
        "args": [
          2,
          6
        ],
        "expected": true
      },
      {
        "args": [
          0,
          4
        ],
        "expected": true
      },
      {
        "args": [
          3,
          9
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6672": {
    "functionNames": [
      "equal_after_offset_5"
    ],
    "tests": [
      {
        "args": [
          2,
          7
        ],
        "expected": true
      },
      {
        "args": [
          0,
          5
        ],
        "expected": true
      },
      {
        "args": [
          3,
          9
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6673": {
    "functionNames": [
      "same_type_and_value_1"
    ],
    "tests": [
      {
        "args": [
          1,
          1
        ],
        "expected": true
      },
      {
        "args": [
          1,
          true
        ],
        "expected": false
      },
      {
        "args": [
          "1",
          "1"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "type",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Is",
      "Eq"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6674": {
    "functionNames": [
      "same_type_and_value_2"
    ],
    "tests": [
      {
        "args": [
          1,
          1
        ],
        "expected": true
      },
      {
        "args": [
          1,
          true
        ],
        "expected": false
      },
      {
        "args": [
          "1",
          "1"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "type",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Is",
      "Eq"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6675": {
    "functionNames": [
      "same_type_and_value_3"
    ],
    "tests": [
      {
        "args": [
          1,
          1
        ],
        "expected": true
      },
      {
        "args": [
          1,
          true
        ],
        "expected": false
      },
      {
        "args": [
          "1",
          "1"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "type",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Is",
      "Eq"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6676": {
    "functionNames": [
      "same_type_and_value_4"
    ],
    "tests": [
      {
        "args": [
          1,
          1
        ],
        "expected": true
      },
      {
        "args": [
          1,
          true
        ],
        "expected": false
      },
      {
        "args": [
          "1",
          "1"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "type",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Is",
      "Eq"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6677": {
    "functionNames": [
      "same_type_and_value_5"
    ],
    "tests": [
      {
        "args": [
          1,
          1
        ],
        "expected": true
      },
      {
        "args": [
          1,
          true
        ],
        "expected": false
      },
      {
        "args": [
          "1",
          "1"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "type",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Is",
      "Eq"
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "6678": {
    "functionNames": [
      "normalized_text_equal_1"
    ],
    "tests": [
      {
        "args": [
          " Python ",
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
          "",
          " "
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6679": {
    "functionNames": [
      "normalized_text_equal_2"
    ],
    "tests": [
      {
        "args": [
          " Python ",
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
          "",
          " "
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6680": {
    "functionNames": [
      "normalized_text_equal_3"
    ],
    "tests": [
      {
        "args": [
          " Python ",
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
          "",
          " "
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6681": {
    "functionNames": [
      "normalized_text_equal_4"
    ],
    "tests": [
      {
        "args": [
          " Python ",
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
          "",
          " "
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6682": {
    "functionNames": [
      "normalized_text_equal_5"
    ],
    "tests": [
      {
        "args": [
          " Python ",
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
          "",
          " "
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6683": {
    "functionNames": [
      "same_sorted_values_1"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2
          ],
          [
            1,
            2,
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
            1,
            1
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
        "functionName": "sorted",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6684": {
    "functionNames": [
      "same_sorted_values_2"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2
          ],
          [
            1,
            2,
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
            1,
            1
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
        "functionName": "sorted",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6685": {
    "functionNames": [
      "same_sorted_values_3"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2
          ],
          [
            1,
            2,
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
            1,
            1
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
        "functionName": "sorted",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6686": {
    "functionNames": [
      "same_sorted_values_4"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2
          ],
          [
            1,
            2,
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
            1,
            1
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
        "functionName": "sorted",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6687": {
    "functionNames": [
      "same_sorted_values_5"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2
          ],
          [
            1,
            2,
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
            1,
            1
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
        "functionName": "sorted",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6688": {
    "functionNames": [
      "count_equal_plus_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 3
      },
      {
        "args": [
          [],
          3
        ],
        "expected": 1
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": 1
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6689": {
    "functionNames": [
      "count_equal_plus_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 4
      },
      {
        "args": [
          [],
          3
        ],
        "expected": 2
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6690": {
    "functionNames": [
      "count_equal_plus_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 5
      },
      {
        "args": [
          [],
          3
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
        "expected": 3
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6691": {
    "functionNames": [
      "count_equal_plus_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 6
      },
      {
        "args": [
          [],
          3
        ],
        "expected": 4
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": 4
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6692": {
    "functionNames": [
      "count_equal_plus_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 7
      },
      {
        "args": [
          [],
          3
        ],
        "expected": 5
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6693": {
    "functionNames": [
      "all_equal_1"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            3
          ],
          2
        ],
        "expected": false
      },
      {
        "args": [
          [],
          1
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6694": {
    "functionNames": [
      "all_equal_2"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            3
          ],
          2
        ],
        "expected": false
      },
      {
        "args": [
          [],
          1
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6695": {
    "functionNames": [
      "all_equal_3"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            3
          ],
          2
        ],
        "expected": false
      },
      {
        "args": [
          [],
          1
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6696": {
    "functionNames": [
      "all_equal_4"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            3
          ],
          2
        ],
        "expected": false
      },
      {
        "args": [
          [],
          1
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6697": {
    "functionNames": [
      "all_equal_5"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            3
          ],
          2
        ],
        "expected": false
      },
      {
        "args": [
          [],
          1
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6698": {
    "functionNames": [
      "exact_boolean_1"
    ],
    "tests": [
      {
        "args": [
          true
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6699": {
    "functionNames": [
      "exact_boolean_2"
    ],
    "tests": [
      {
        "args": [
          false
        ],
        "expected": true
      },
      {
        "args": [
          true
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6700": {
    "functionNames": [
      "exact_boolean_3"
    ],
    "tests": [
      {
        "args": [
          true
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6701": {
    "functionNames": [
      "exact_boolean_4"
    ],
    "tests": [
      {
        "args": [
          false
        ],
        "expected": true
      },
      {
        "args": [
          true
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6702": {
    "functionNames": [
      "exact_boolean_5"
    ],
    "tests": [
      {
        "args": [
          true
        ],
        "expected": true
      },
      {
        "args": [
          false
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "Is"
    ]
  },
  "6703": {
    "functionNames": [
      "mapping_value_equal_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 2
          },
          "a",
          2
        ],
        "expected": true
      },
      {
        "args": [
          {},
          "x",
          1
        ],
        "expected": true
      },
      {
        "args": [
          {
            "a": 1
          },
          "a",
          9
        ],
        "expected": false
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "get",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6704": {
    "functionNames": [
      "mapping_value_equal_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 2
          },
          "a",
          2
        ],
        "expected": true
      },
      {
        "args": [
          {},
          "x",
          2
        ],
        "expected": true
      },
      {
        "args": [
          {
            "a": 1
          },
          "a",
          9
        ],
        "expected": false
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "get",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6705": {
    "functionNames": [
      "mapping_value_equal_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 2
          },
          "a",
          2
        ],
        "expected": true
      },
      {
        "args": [
          {},
          "x",
          3
        ],
        "expected": true
      },
      {
        "args": [
          {
            "a": 1
          },
          "a",
          9
        ],
        "expected": false
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "get",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6706": {
    "functionNames": [
      "mapping_value_equal_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 2
          },
          "a",
          2
        ],
        "expected": true
      },
      {
        "args": [
          {},
          "x",
          4
        ],
        "expected": true
      },
      {
        "args": [
          {
            "a": 1
          },
          "a",
          9
        ],
        "expected": false
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "get",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6707": {
    "functionNames": [
      "mapping_value_equal_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 2
          },
          "a",
          2
        ],
        "expected": true
      },
      {
        "args": [
          {},
          "x",
          5
        ],
        "expected": true
      },
      {
        "args": [
          {
            "a": 1
          },
          "a",
          9
        ],
        "expected": false
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "get",
        "minArgs": 0
      }
    ],
    "requiredAstOperators": [
      "Eq"
    ]
  },
  "6708": {
    "functionNames": [
      "format_greeting_1"
    ],
    "tests": [
      {
        "args": [
          "Ada"
        ],
        "expected": "Hello, Ada! [1]"
      },
      {
        "args": [
          ""
        ],
        "expected": "Hello, ! [1]"
      },
      {
        "args": [
          "Noll"
        ],
        "expected": "Hello, Noll! [1]"
      }
    ]
  },
  "6709": {
    "functionNames": [
      "format_greeting_2"
    ],
    "tests": [
      {
        "args": [
          "Ada"
        ],
        "expected": "Hello, Ada! [2]"
      },
      {
        "args": [
          ""
        ],
        "expected": "Hello, ! [2]"
      },
      {
        "args": [
          "Noll"
        ],
        "expected": "Hello, Noll! [2]"
      }
    ]
  },
  "6710": {
    "functionNames": [
      "format_greeting_3"
    ],
    "tests": [
      {
        "args": [
          "Ada"
        ],
        "expected": "Hello, Ada! [3]"
      },
      {
        "args": [
          ""
        ],
        "expected": "Hello, ! [3]"
      },
      {
        "args": [
          "Noll"
        ],
        "expected": "Hello, Noll! [3]"
      }
    ]
  },
  "6711": {
    "functionNames": [
      "format_greeting_4"
    ],
    "tests": [
      {
        "args": [
          "Ada"
        ],
        "expected": "Hello, Ada! [4]"
      },
      {
        "args": [
          ""
        ],
        "expected": "Hello, ! [4]"
      },
      {
        "args": [
          "Noll"
        ],
        "expected": "Hello, Noll! [4]"
      }
    ]
  },
  "6712": {
    "functionNames": [
      "format_greeting_5"
    ],
    "tests": [
      {
        "args": [
          "Ada"
        ],
        "expected": "Hello, Ada! [5]"
      },
      {
        "args": [
          ""
        ],
        "expected": "Hello, ! [5]"
      },
      {
        "args": [
          "Noll"
        ],
        "expected": "Hello, Noll! [5]"
      }
    ]
  },
  "6713": {
    "functionNames": [
      "format_fixed_1"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": "3.1"
      },
      {
        "args": [
          2
        ],
        "expected": "2.0"
      },
      {
        "args": [
          -1.26
        ],
        "expected": "-1.3"
      }
    ]
  },
  "6714": {
    "functionNames": [
      "format_fixed_2"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": "3.14"
      },
      {
        "args": [
          2
        ],
        "expected": "2.00"
      },
      {
        "args": [
          -1.26
        ],
        "expected": "-1.26"
      }
    ]
  },
  "6715": {
    "functionNames": [
      "format_fixed_3"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": "3.142"
      },
      {
        "args": [
          2
        ],
        "expected": "2.000"
      },
      {
        "args": [
          -1.26
        ],
        "expected": "-1.260"
      }
    ]
  },
  "6716": {
    "functionNames": [
      "format_fixed_4"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": "3.1416"
      },
      {
        "args": [
          2
        ],
        "expected": "2.0000"
      },
      {
        "args": [
          -1.26
        ],
        "expected": "-1.2600"
      }
    ]
  },
  "6717": {
    "functionNames": [
      "format_fixed_5"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": "3.14159"
      },
      {
        "args": [
          2
        ],
        "expected": "2.00000"
      },
      {
        "args": [
          -1.26
        ],
        "expected": "-1.26000"
      }
    ]
  },
  "6718": {
    "functionNames": [
      "format_zero_pad_1"
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": "0007"
      },
      {
        "args": [
          42
        ],
        "expected": "0042"
      },
      {
        "args": [
          0
        ],
        "expected": "0000"
      }
    ]
  },
  "6719": {
    "functionNames": [
      "format_zero_pad_2"
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": "00007"
      },
      {
        "args": [
          42
        ],
        "expected": "00042"
      },
      {
        "args": [
          0
        ],
        "expected": "00000"
      }
    ]
  },
  "6720": {
    "functionNames": [
      "format_zero_pad_3"
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": "000007"
      },
      {
        "args": [
          42
        ],
        "expected": "000042"
      },
      {
        "args": [
          0
        ],
        "expected": "000000"
      }
    ]
  },
  "6721": {
    "functionNames": [
      "format_zero_pad_4"
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": "0000007"
      },
      {
        "args": [
          42
        ],
        "expected": "0000042"
      },
      {
        "args": [
          0
        ],
        "expected": "0000000"
      }
    ]
  },
  "6722": {
    "functionNames": [
      "format_zero_pad_5"
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": "00000007"
      },
      {
        "args": [
          42
        ],
        "expected": "00000042"
      },
      {
        "args": [
          0
        ],
        "expected": "00000000"
      }
    ]
  },
  "6723": {
    "functionNames": [
      "format_right_align_1"
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "    cat"
      },
      {
        "args": [
          ""
        ],
        "expected": "       "
      },
      {
        "args": [
          "python"
        ],
        "expected": " python"
      }
    ]
  },
  "6724": {
    "functionNames": [
      "format_right_align_2"
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "     cat"
      },
      {
        "args": [
          ""
        ],
        "expected": "        "
      },
      {
        "args": [
          "python"
        ],
        "expected": "  python"
      }
    ]
  },
  "6725": {
    "functionNames": [
      "format_right_align_3"
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "      cat"
      },
      {
        "args": [
          ""
        ],
        "expected": "         "
      },
      {
        "args": [
          "python"
        ],
        "expected": "   python"
      }
    ]
  },
  "6726": {
    "functionNames": [
      "format_right_align_4"
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "       cat"
      },
      {
        "args": [
          ""
        ],
        "expected": "          "
      },
      {
        "args": [
          "python"
        ],
        "expected": "    python"
      }
    ]
  },
  "6727": {
    "functionNames": [
      "format_right_align_5"
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "        cat"
      },
      {
        "args": [
          ""
        ],
        "expected": "           "
      },
      {
        "args": [
          "python"
        ],
        "expected": "     python"
      }
    ]
  },
  "6728": {
    "functionNames": [
      "format_percent_1"
    ],
    "tests": [
      {
        "args": [
          0.25
        ],
        "expected": "25.0%"
      },
      {
        "args": [
          1
        ],
        "expected": "100.0%"
      },
      {
        "args": [
          0.035
        ],
        "expected": "3.5%"
      }
    ]
  },
  "6729": {
    "functionNames": [
      "format_percent_2"
    ],
    "tests": [
      {
        "args": [
          0.25
        ],
        "expected": "25.00%"
      },
      {
        "args": [
          1
        ],
        "expected": "100.00%"
      },
      {
        "args": [
          0.035
        ],
        "expected": "3.50%"
      }
    ]
  },
  "6730": {
    "functionNames": [
      "format_percent_3"
    ],
    "tests": [
      {
        "args": [
          0.25
        ],
        "expected": "25.000%"
      },
      {
        "args": [
          1
        ],
        "expected": "100.000%"
      },
      {
        "args": [
          0.035
        ],
        "expected": "3.500%"
      }
    ]
  },
  "6731": {
    "functionNames": [
      "format_percent_4"
    ],
    "tests": [
      {
        "args": [
          0.25
        ],
        "expected": "25.0000%"
      },
      {
        "args": [
          1
        ],
        "expected": "100.0000%"
      },
      {
        "args": [
          0.035
        ],
        "expected": "3.5000%"
      }
    ]
  },
  "6732": {
    "functionNames": [
      "format_percent_5"
    ],
    "tests": [
      {
        "args": [
          0.25
        ],
        "expected": "25.00000%"
      },
      {
        "args": [
          1
        ],
        "expected": "100.00000%"
      },
      {
        "args": [
          0.035
        ],
        "expected": "3.50000%"
      }
    ]
  },
  "6733": {
    "functionNames": [
      "format_signed_1"
    ],
    "tests": [
      {
        "args": [
          3.5
        ],
        "expected": "+3.5"
      },
      {
        "args": [
          -2
        ],
        "expected": "-2.0"
      },
      {
        "args": [
          0
        ],
        "expected": "+0.0"
      }
    ]
  },
  "6734": {
    "functionNames": [
      "format_signed_2"
    ],
    "tests": [
      {
        "args": [
          3.5
        ],
        "expected": "+3.50"
      },
      {
        "args": [
          -2
        ],
        "expected": "-2.00"
      },
      {
        "args": [
          0
        ],
        "expected": "+0.00"
      }
    ]
  },
  "6735": {
    "functionNames": [
      "format_signed_3"
    ],
    "tests": [
      {
        "args": [
          3.5
        ],
        "expected": "+3.500"
      },
      {
        "args": [
          -2
        ],
        "expected": "-2.000"
      },
      {
        "args": [
          0
        ],
        "expected": "+0.000"
      }
    ]
  },
  "6736": {
    "functionNames": [
      "format_signed_4"
    ],
    "tests": [
      {
        "args": [
          3.5
        ],
        "expected": "+3.5000"
      },
      {
        "args": [
          -2
        ],
        "expected": "-2.0000"
      },
      {
        "args": [
          0
        ],
        "expected": "+0.0000"
      }
    ]
  },
  "6737": {
    "functionNames": [
      "format_signed_5"
    ],
    "tests": [
      {
        "args": [
          3.5
        ],
        "expected": "+3.50000"
      },
      {
        "args": [
          -2
        ],
        "expected": "-2.00000"
      },
      {
        "args": [
          0
        ],
        "expected": "+0.00000"
      }
    ]
  },
  "6738": {
    "functionNames": [
      "format_grouped_1"
    ],
    "tests": [
      {
        "args": [
          1234567
        ],
        "expected": "1,234,567|1"
      },
      {
        "args": [
          1000
        ],
        "expected": "1,000|1"
      },
      {
        "args": [
          42
        ],
        "expected": "42|1"
      }
    ]
  },
  "6739": {
    "functionNames": [
      "format_grouped_2"
    ],
    "tests": [
      {
        "args": [
          1234567
        ],
        "expected": "1,234,567|2"
      },
      {
        "args": [
          1000
        ],
        "expected": "1,000|2"
      },
      {
        "args": [
          42
        ],
        "expected": "42|2"
      }
    ]
  },
  "6740": {
    "functionNames": [
      "format_grouped_3"
    ],
    "tests": [
      {
        "args": [
          1234567
        ],
        "expected": "1,234,567|3"
      },
      {
        "args": [
          1000
        ],
        "expected": "1,000|3"
      },
      {
        "args": [
          42
        ],
        "expected": "42|3"
      }
    ]
  },
  "6741": {
    "functionNames": [
      "format_grouped_4"
    ],
    "tests": [
      {
        "args": [
          1234567
        ],
        "expected": "1,234,567|4"
      },
      {
        "args": [
          1000
        ],
        "expected": "1,000|4"
      },
      {
        "args": [
          42
        ],
        "expected": "42|4"
      }
    ]
  },
  "6742": {
    "functionNames": [
      "format_grouped_5"
    ],
    "tests": [
      {
        "args": [
          1234567
        ],
        "expected": "1,234,567|5"
      },
      {
        "args": [
          1000
        ],
        "expected": "1,000|5"
      },
      {
        "args": [
          42
        ],
        "expected": "42|5"
      }
    ]
  },
  "6743": {
    "functionNames": [
      "format_record_1"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          9
        ],
        "expected": "Ada:   9"
      },
      {
        "args": [
          "Bob",
          100
        ],
        "expected": "Bob: 100"
      },
      {
        "args": [
          "",
          0
        ],
        "expected": ":   0"
      }
    ]
  },
  "6744": {
    "functionNames": [
      "format_record_2"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          9
        ],
        "expected": "Ada:    9"
      },
      {
        "args": [
          "Bob",
          100
        ],
        "expected": "Bob:  100"
      },
      {
        "args": [
          "",
          0
        ],
        "expected": ":    0"
      }
    ]
  },
  "6745": {
    "functionNames": [
      "format_record_3"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          9
        ],
        "expected": "Ada:     9"
      },
      {
        "args": [
          "Bob",
          100
        ],
        "expected": "Bob:   100"
      },
      {
        "args": [
          "",
          0
        ],
        "expected": ":     0"
      }
    ]
  },
  "6746": {
    "functionNames": [
      "format_record_4"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          9
        ],
        "expected": "Ada:      9"
      },
      {
        "args": [
          "Bob",
          100
        ],
        "expected": "Bob:    100"
      },
      {
        "args": [
          "",
          0
        ],
        "expected": ":      0"
      }
    ]
  },
  "6747": {
    "functionNames": [
      "format_record_5"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          9
        ],
        "expected": "Ada:       9"
      },
      {
        "args": [
          "Bob",
          100
        ],
        "expected": "Bob:     100"
      },
      {
        "args": [
          "",
          0
        ],
        "expected": ":       0"
      }
    ]
  },
  "6748": {
    "functionNames": [
      "format_coordinates_1"
    ],
    "tests": [
      {
        "args": [
          1.2,
          3.4
        ],
        "expected": "(1.2, 3.4)"
      },
      {
        "args": [
          0,
          -2.5
        ],
        "expected": "(0.0, -2.5)"
      },
      {
        "args": [
          9.876,
          1.234
        ],
        "expected": "(9.9, 1.2)"
      }
    ]
  },
  "6749": {
    "functionNames": [
      "format_coordinates_2"
    ],
    "tests": [
      {
        "args": [
          1.2,
          3.4
        ],
        "expected": "(1.20, 3.40)"
      },
      {
        "args": [
          0,
          -2.5
        ],
        "expected": "(0.00, -2.50)"
      },
      {
        "args": [
          9.876,
          1.234
        ],
        "expected": "(9.88, 1.23)"
      }
    ]
  },
  "6750": {
    "functionNames": [
      "format_coordinates_3"
    ],
    "tests": [
      {
        "args": [
          1.2,
          3.4
        ],
        "expected": "(1.200, 3.400)"
      },
      {
        "args": [
          0,
          -2.5
        ],
        "expected": "(0.000, -2.500)"
      },
      {
        "args": [
          9.876,
          1.234
        ],
        "expected": "(9.876, 1.234)"
      }
    ]
  },
  "6751": {
    "functionNames": [
      "format_coordinates_4"
    ],
    "tests": [
      {
        "args": [
          1.2,
          3.4
        ],
        "expected": "(1.2000, 3.4000)"
      },
      {
        "args": [
          0,
          -2.5
        ],
        "expected": "(0.0000, -2.5000)"
      },
      {
        "args": [
          9.876,
          1.234
        ],
        "expected": "(9.8760, 1.2340)"
      }
    ]
  },
  "6752": {
    "functionNames": [
      "format_coordinates_5"
    ],
    "tests": [
      {
        "args": [
          1.2,
          3.4
        ],
        "expected": "(1.20000, 3.40000)"
      },
      {
        "args": [
          0,
          -2.5
        ],
        "expected": "(0.00000, -2.50000)"
      },
      {
        "args": [
          9.876,
          1.234
        ],
        "expected": "(9.87600, 1.23400)"
      }
    ]
  },
  "6753": {
    "functionNames": [
      "format_centered_1"
    ],
    "tests": [
      {
        "args": [
          "AI"
        ],
        "expected": "...AI...."
      },
      {
        "args": [
          "x"
        ],
        "expected": "....x...."
      },
      {
        "args": [
          "python"
        ],
        "expected": ".python.."
      }
    ]
  },
  "6754": {
    "functionNames": [
      "format_centered_2"
    ],
    "tests": [
      {
        "args": [
          "AI"
        ],
        "expected": "....AI....."
      },
      {
        "args": [
          "x"
        ],
        "expected": ".....x....."
      },
      {
        "args": [
          "python"
        ],
        "expected": "..python..."
      }
    ]
  },
  "6755": {
    "functionNames": [
      "format_centered_3"
    ],
    "tests": [
      {
        "args": [
          "AI"
        ],
        "expected": ".....AI......"
      },
      {
        "args": [
          "x"
        ],
        "expected": "......x......"
      },
      {
        "args": [
          "python"
        ],
        "expected": "...python...."
      }
    ]
  },
  "6756": {
    "functionNames": [
      "format_centered_4"
    ],
    "tests": [
      {
        "args": [
          "AI"
        ],
        "expected": "......AI......."
      },
      {
        "args": [
          "x"
        ],
        "expected": ".......x......."
      },
      {
        "args": [
          "python"
        ],
        "expected": "....python....."
      }
    ]
  },
  "6757": {
    "functionNames": [
      "format_centered_5"
    ],
    "tests": [
      {
        "args": [
          "AI"
        ],
        "expected": ".......AI........"
      },
      {
        "args": [
          "x"
        ],
        "expected": "........x........"
      },
      {
        "args": [
          "python"
        ],
        "expected": ".....python......"
      }
    ]
  },
  "6758": {
    "functionNames": [
      "rounded_sum_1"
    ],
    "tests": [
      {
        "args": [
          1.2345,
          2.3456
        ],
        "expected": 3.6
      },
      {
        "args": [
          0.1,
          0.2
        ],
        "expected": 0.3
      },
      {
        "args": [
          -1.25,
          0.5
        ],
        "expected": -0.8
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6759": {
    "functionNames": [
      "rounded_sum_2"
    ],
    "tests": [
      {
        "args": [
          1.2345,
          2.3456
        ],
        "expected": 3.58
      },
      {
        "args": [
          0.1,
          0.2
        ],
        "expected": 0.3
      },
      {
        "args": [
          -1.25,
          0.5
        ],
        "expected": -0.75
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6760": {
    "functionNames": [
      "rounded_sum_3"
    ],
    "tests": [
      {
        "args": [
          1.2345,
          2.3456
        ],
        "expected": 3.58
      },
      {
        "args": [
          0.1,
          0.2
        ],
        "expected": 0.3
      },
      {
        "args": [
          -1.25,
          0.5
        ],
        "expected": -0.75
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6761": {
    "functionNames": [
      "rounded_sum_4"
    ],
    "tests": [
      {
        "args": [
          1.2345,
          2.3456
        ],
        "expected": 3.5801
      },
      {
        "args": [
          0.1,
          0.2
        ],
        "expected": 0.3
      },
      {
        "args": [
          -1.25,
          0.5
        ],
        "expected": -0.75
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6762": {
    "functionNames": [
      "rounded_sum_5"
    ],
    "tests": [
      {
        "args": [
          1.2345,
          2.3456
        ],
        "expected": 3.5801
      },
      {
        "args": [
          0.1,
          0.2
        ],
        "expected": 0.3
      },
      {
        "args": [
          -1.25,
          0.5
        ],
        "expected": -0.75
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6763": {
    "functionNames": [
      "safe_percentage_1"
    ],
    "tests": [
      {
        "args": [
          1,
          4
        ],
        "expected": 25
      },
      {
        "args": [
          2,
          3
        ],
        "expected": 66.7
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6764": {
    "functionNames": [
      "safe_percentage_2"
    ],
    "tests": [
      {
        "args": [
          1,
          4
        ],
        "expected": 25
      },
      {
        "args": [
          2,
          3
        ],
        "expected": 66.67
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6765": {
    "functionNames": [
      "safe_percentage_3"
    ],
    "tests": [
      {
        "args": [
          1,
          4
        ],
        "expected": 25
      },
      {
        "args": [
          2,
          3
        ],
        "expected": 66.667
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6766": {
    "functionNames": [
      "safe_percentage_4"
    ],
    "tests": [
      {
        "args": [
          1,
          4
        ],
        "expected": 25
      },
      {
        "args": [
          2,
          3
        ],
        "expected": 66.6667
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6767": {
    "functionNames": [
      "safe_percentage_5"
    ],
    "tests": [
      {
        "args": [
          1,
          4
        ],
        "expected": 25
      },
      {
        "args": [
          2,
          3
        ],
        "expected": 66.66667
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6768": {
    "functionNames": [
      "quotient_remainder_1"
    ],
    "tests": [
      {
        "args": [
          17
        ],
        "expected": [
          8,
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          0
        ]
      },
      {
        "args": [
          42
        ],
        "expected": [
          21,
          0
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "divmod",
        "minArgs": 0
      }
    ]
  },
  "6769": {
    "functionNames": [
      "quotient_remainder_2"
    ],
    "tests": [
      {
        "args": [
          17
        ],
        "expected": [
          5,
          2
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          0
        ]
      },
      {
        "args": [
          42
        ],
        "expected": [
          14,
          0
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "divmod",
        "minArgs": 0
      }
    ]
  },
  "6770": {
    "functionNames": [
      "quotient_remainder_3"
    ],
    "tests": [
      {
        "args": [
          17
        ],
        "expected": [
          4,
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          0
        ]
      },
      {
        "args": [
          42
        ],
        "expected": [
          10,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "divmod",
        "minArgs": 0
      }
    ]
  },
  "6771": {
    "functionNames": [
      "quotient_remainder_4"
    ],
    "tests": [
      {
        "args": [
          17
        ],
        "expected": [
          3,
          2
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          0
        ]
      },
      {
        "args": [
          42
        ],
        "expected": [
          8,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "divmod",
        "minArgs": 0
      }
    ]
  },
  "6772": {
    "functionNames": [
      "quotient_remainder_5"
    ],
    "tests": [
      {
        "args": [
          17
        ],
        "expected": [
          2,
          5
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          0
        ]
      },
      {
        "args": [
          42
        ],
        "expected": [
          7,
          0
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "divmod",
        "minArgs": 0
      }
    ]
  },
  "6773": {
    "functionNames": [
      "clamp_number_1"
    ],
    "tests": [
      {
        "args": [
          -20
        ],
        "expected": -1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          20
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      },
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "6774": {
    "functionNames": [
      "clamp_number_2"
    ],
    "tests": [
      {
        "args": [
          -20
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          20
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      },
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "6775": {
    "functionNames": [
      "clamp_number_3"
    ],
    "tests": [
      {
        "args": [
          -20
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          20
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      },
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "6776": {
    "functionNames": [
      "clamp_number_4"
    ],
    "tests": [
      {
        "args": [
          -20
        ],
        "expected": -4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          20
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      },
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "6777": {
    "functionNames": [
      "clamp_number_5"
    ],
    "tests": [
      {
        "args": [
          -20
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          20
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      },
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "6778": {
    "functionNames": [
      "rounded_average_1"
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
            1,
            2
          ]
        ],
        "expected": 1.5
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6779": {
    "functionNames": [
      "rounded_average_2"
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
            1,
            2
          ]
        ],
        "expected": 1.5
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6780": {
    "functionNames": [
      "rounded_average_3"
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
            1,
            2
          ]
        ],
        "expected": 1.5
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6781": {
    "functionNames": [
      "rounded_average_4"
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
            1,
            2
          ]
        ],
        "expected": 1.5
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6782": {
    "functionNames": [
      "rounded_average_5"
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
            1,
            2
          ]
        ],
        "expected": 1.5
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6783": {
    "functionNames": [
      "nearly_equal_1"
    ],
    "tests": [
      {
        "args": [
          1,
          1.05
        ],
        "expected": true
      },
      {
        "args": [
          1,
          1.2
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
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "6784": {
    "functionNames": [
      "nearly_equal_2"
    ],
    "tests": [
      {
        "args": [
          1,
          1.005
        ],
        "expected": true
      },
      {
        "args": [
          1,
          1.02
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
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "6785": {
    "functionNames": [
      "nearly_equal_3"
    ],
    "tests": [
      {
        "args": [
          1,
          1.0005
        ],
        "expected": true
      },
      {
        "args": [
          1,
          1.002
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
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "6786": {
    "functionNames": [
      "nearly_equal_4"
    ],
    "tests": [
      {
        "args": [
          1,
          1.00005
        ],
        "expected": true
      },
      {
        "args": [
          1,
          1.0002
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
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "6787": {
    "functionNames": [
      "nearly_equal_5"
    ],
    "tests": [
      {
        "args": [
          1,
          1.000005
        ],
        "expected": true
      },
      {
        "args": [
          1,
          1.00002
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
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "6788": {
    "functionNames": [
      "decimal_sum_1"
    ],
    "tests": [
      {
        "args": [
          "0.1",
          "0.2"
        ],
        "expected": "0.3"
      },
      {
        "args": [
          "1.25",
          "2.5"
        ],
        "expected": "3.8"
      },
      {
        "args": [
          "-1",
          "0.5"
        ],
        "expected": "-0.5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Decimal",
        "minArgs": 0
      }
    ]
  },
  "6789": {
    "functionNames": [
      "decimal_sum_2"
    ],
    "tests": [
      {
        "args": [
          "0.1",
          "0.2"
        ],
        "expected": "0.30"
      },
      {
        "args": [
          "1.25",
          "2.5"
        ],
        "expected": "3.75"
      },
      {
        "args": [
          "-1",
          "0.5"
        ],
        "expected": "-0.50"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Decimal",
        "minArgs": 0
      }
    ]
  },
  "6790": {
    "functionNames": [
      "decimal_sum_3"
    ],
    "tests": [
      {
        "args": [
          "0.1",
          "0.2"
        ],
        "expected": "0.300"
      },
      {
        "args": [
          "1.25",
          "2.5"
        ],
        "expected": "3.750"
      },
      {
        "args": [
          "-1",
          "0.5"
        ],
        "expected": "-0.500"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Decimal",
        "minArgs": 0
      }
    ]
  },
  "6791": {
    "functionNames": [
      "decimal_sum_4"
    ],
    "tests": [
      {
        "args": [
          "0.1",
          "0.2"
        ],
        "expected": "0.3000"
      },
      {
        "args": [
          "1.25",
          "2.5"
        ],
        "expected": "3.7500"
      },
      {
        "args": [
          "-1",
          "0.5"
        ],
        "expected": "-0.5000"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Decimal",
        "minArgs": 0
      }
    ]
  },
  "6792": {
    "functionNames": [
      "decimal_sum_5"
    ],
    "tests": [
      {
        "args": [
          "0.1",
          "0.2"
        ],
        "expected": "0.30000"
      },
      {
        "args": [
          "1.25",
          "2.5"
        ],
        "expected": "3.75000"
      },
      {
        "args": [
          "-1",
          "0.5"
        ],
        "expected": "-0.50000"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Decimal",
        "minArgs": 0
      }
    ]
  },
  "6793": {
    "functionNames": [
      "compound_once_1"
    ],
    "tests": [
      {
        "args": [
          100,
          5
        ],
        "expected": 105
      },
      {
        "args": [
          80,
          12.5
        ],
        "expected": 90
      },
      {
        "args": [
          50,
          -10
        ],
        "expected": 45
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6794": {
    "functionNames": [
      "compound_once_2"
    ],
    "tests": [
      {
        "args": [
          100,
          5
        ],
        "expected": 105
      },
      {
        "args": [
          80,
          12.5
        ],
        "expected": 90
      },
      {
        "args": [
          50,
          -10
        ],
        "expected": 45
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6795": {
    "functionNames": [
      "compound_once_3"
    ],
    "tests": [
      {
        "args": [
          100,
          5
        ],
        "expected": 105
      },
      {
        "args": [
          80,
          12.5
        ],
        "expected": 90
      },
      {
        "args": [
          50,
          -10
        ],
        "expected": 45
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6796": {
    "functionNames": [
      "compound_once_4"
    ],
    "tests": [
      {
        "args": [
          100,
          5
        ],
        "expected": 105
      },
      {
        "args": [
          80,
          12.5
        ],
        "expected": 90
      },
      {
        "args": [
          50,
          -10
        ],
        "expected": 45
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6797": {
    "functionNames": [
      "compound_once_5"
    ],
    "tests": [
      {
        "args": [
          100,
          5
        ],
        "expected": 105
      },
      {
        "args": [
          80,
          12.5
        ],
        "expected": 90
      },
      {
        "args": [
          50,
          -10
        ],
        "expected": 45
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6798": {
    "functionNames": [
      "split_money_1"
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3.3
      },
      {
        "args": [
          20,
          4
        ],
        "expected": 5
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6799": {
    "functionNames": [
      "split_money_2"
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3.33
      },
      {
        "args": [
          20,
          4
        ],
        "expected": 5
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6800": {
    "functionNames": [
      "split_money_3"
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3.333
      },
      {
        "args": [
          20,
          4
        ],
        "expected": 5
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6801": {
    "functionNames": [
      "split_money_4"
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3.3333
      },
      {
        "args": [
          20,
          4
        ],
        "expected": 5
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6802": {
    "functionNames": [
      "split_money_5"
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3.33333
      },
      {
        "args": [
          20,
          4
        ],
        "expected": 5
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "6803": {
    "functionNames": [
      "weighted_average_1"
    ],
    "tests": [
      {
        "args": [
          [
            10,
            20
          ],
          [
            1,
            3
          ]
        ],
        "expected": 17.5
      },
      {
        "args": [
          [
            5
          ],
          [
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            0,
            0
          ]
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      },
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "6804": {
    "functionNames": [
      "weighted_average_2"
    ],
    "tests": [
      {
        "args": [
          [
            10,
            20
          ],
          [
            1,
            3
          ]
        ],
        "expected": 17.5
      },
      {
        "args": [
          [
            5
          ],
          [
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            0,
            0
          ]
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      },
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "6805": {
    "functionNames": [
      "weighted_average_3"
    ],
    "tests": [
      {
        "args": [
          [
            10,
            20
          ],
          [
            1,
            3
          ]
        ],
        "expected": 17.5
      },
      {
        "args": [
          [
            5
          ],
          [
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            0,
            0
          ]
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      },
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "6806": {
    "functionNames": [
      "weighted_average_4"
    ],
    "tests": [
      {
        "args": [
          [
            10,
            20
          ],
          [
            1,
            3
          ]
        ],
        "expected": 17.5
      },
      {
        "args": [
          [
            5
          ],
          [
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            0,
            0
          ]
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      },
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "6807": {
    "functionNames": [
      "weighted_average_5"
    ],
    "tests": [
      {
        "args": [
          [
            10,
            20
          ],
          [
            1,
            3
          ]
        ],
        "expected": 17.5
      },
      {
        "args": [
          [
            5
          ],
          [
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            0,
            0
          ]
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      },
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "6808": {
    "functionNames": [
      "copy_append_1"
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
          1,
          2,
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
            1
          ]
        ],
        "expected": [
          1,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6809": {
    "functionNames": [
      "copy_append_2"
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
          1,
          2,
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
            2
          ]
        ],
        "expected": [
          2,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6810": {
    "functionNames": [
      "copy_append_3"
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
          1,
          2,
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
            3
          ]
        ],
        "expected": [
          3,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6811": {
    "functionNames": [
      "copy_append_4"
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
          1,
          2,
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
            4
          ]
        ],
        "expected": [
          4,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6812": {
    "functionNames": [
      "copy_append_5"
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
          1,
          2,
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
            5
          ]
        ],
        "expected": [
          5,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6813": {
    "functionNames": [
      "copy_replace_first_1"
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
            9
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6814": {
    "functionNames": [
      "copy_replace_first_2"
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
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6815": {
    "functionNames": [
      "copy_replace_first_3"
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
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6816": {
    "functionNames": [
      "copy_replace_first_4"
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
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6817": {
    "functionNames": [
      "copy_replace_first_5"
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
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6818": {
    "functionNames": [
      "copy_dict_marker_1"
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
          "marker": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": 1
        }
      },
      {
        "args": [
          {
            "marker": 9
          }
        ],
        "expected": {
          "marker": 1
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6819": {
    "functionNames": [
      "copy_dict_marker_2"
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
          "marker": 2
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": 2
        }
      },
      {
        "args": [
          {
            "marker": 9
          }
        ],
        "expected": {
          "marker": 2
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6820": {
    "functionNames": [
      "copy_dict_marker_3"
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
          "marker": 3
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": 3
        }
      },
      {
        "args": [
          {
            "marker": 9
          }
        ],
        "expected": {
          "marker": 3
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6821": {
    "functionNames": [
      "copy_dict_marker_4"
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
          "marker": 4
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": 4
        }
      },
      {
        "args": [
          {
            "marker": 9
          }
        ],
        "expected": {
          "marker": 4
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6822": {
    "functionNames": [
      "copy_dict_marker_5"
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
          "marker": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": 5
        }
      },
      {
        "args": [
          {
            "marker": 9
          }
        ],
        "expected": {
          "marker": 5
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6823": {
    "functionNames": [
      "copy_remove_1"
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
        "expected": [
          2,
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
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "remove",
        "minArgs": 0
      }
    ]
  },
  "6824": {
    "functionNames": [
      "copy_remove_2"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2,
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
            1,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "remove",
        "minArgs": 0
      }
    ]
  },
  "6825": {
    "functionNames": [
      "copy_remove_3"
    ],
    "tests": [
      {
        "args": [
          [
            3,
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
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "remove",
        "minArgs": 0
      }
    ]
  },
  "6826": {
    "functionNames": [
      "copy_remove_4"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            2,
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
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "remove",
        "minArgs": 0
      }
    ]
  },
  "6827": {
    "functionNames": [
      "copy_remove_5"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            2,
            5
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
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "remove",
        "minArgs": 0
      }
    ]
  },
  "6828": {
    "functionNames": [
      "copy_extend_1"
    ],
    "tests": [
      {
        "args": [
          [
            1
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
      },
      {
        "args": [
          [
            9
          ],
          []
        ],
        "expected": [
          9,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "extend",
        "minArgs": 0
      }
    ]
  },
  "6829": {
    "functionNames": [
      "copy_extend_2"
    ],
    "tests": [
      {
        "args": [
          [
            1
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
      },
      {
        "args": [
          [
            9
          ],
          []
        ],
        "expected": [
          9,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "extend",
        "minArgs": 0
      }
    ]
  },
  "6830": {
    "functionNames": [
      "copy_extend_3"
    ],
    "tests": [
      {
        "args": [
          [
            1
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
      },
      {
        "args": [
          [
            9
          ],
          []
        ],
        "expected": [
          9,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "extend",
        "minArgs": 0
      }
    ]
  },
  "6831": {
    "functionNames": [
      "copy_extend_4"
    ],
    "tests": [
      {
        "args": [
          [
            1
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
          []
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          [
            9
          ],
          []
        ],
        "expected": [
          9,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "extend",
        "minArgs": 0
      }
    ]
  },
  "6832": {
    "functionNames": [
      "copy_extend_5"
    ],
    "tests": [
      {
        "args": [
          [
            1
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
          []
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            9
          ],
          []
        ],
        "expected": [
          9,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "extend",
        "minArgs": 0
      }
    ]
  },
  "6833": {
    "functionNames": [
      "nested_row_copy_1"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1
            ],
            [
              2
            ]
          ]
        ],
        "expected": [
          [
            1,
            1
          ],
          [
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
            [
              9
            ]
          ]
        ],
        "expected": [
          [
            9,
            1
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6834": {
    "functionNames": [
      "nested_row_copy_2"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1
            ],
            [
              2
            ]
          ]
        ],
        "expected": [
          [
            1,
            2
          ],
          [
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
            [
              9
            ]
          ]
        ],
        "expected": [
          [
            9,
            2
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6835": {
    "functionNames": [
      "nested_row_copy_3"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1
            ],
            [
              2
            ]
          ]
        ],
        "expected": [
          [
            1,
            3
          ],
          [
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
            [
              9
            ]
          ]
        ],
        "expected": [
          [
            9,
            3
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6836": {
    "functionNames": [
      "nested_row_copy_4"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1
            ],
            [
              2
            ]
          ]
        ],
        "expected": [
          [
            1,
            4
          ],
          [
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
            [
              9
            ]
          ]
        ],
        "expected": [
          [
            9,
            4
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6837": {
    "functionNames": [
      "nested_row_copy_5"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1
            ],
            [
              2
            ]
          ]
        ],
        "expected": [
          [
            1,
            5
          ],
          [
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
            [
              9
            ]
          ]
        ],
        "expected": [
          [
            9,
            5
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      }
    ]
  },
  "6838": {
    "functionNames": [
      "merged_mapping_copy_1"
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
            "a": 1
          },
          {
            "a": 9
          }
        ],
        "expected": {
          "a": 9,
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "update",
        "minArgs": 0
      }
    ]
  },
  "6839": {
    "functionNames": [
      "merged_mapping_copy_2"
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
            "a": 1
          },
          {
            "a": 9
          }
        ],
        "expected": {
          "a": 9,
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "update",
        "minArgs": 0
      }
    ]
  },
  "6840": {
    "functionNames": [
      "merged_mapping_copy_3"
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
            "a": 1
          },
          {
            "a": 9
          }
        ],
        "expected": {
          "a": 9,
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "update",
        "minArgs": 0
      }
    ]
  },
  "6841": {
    "functionNames": [
      "merged_mapping_copy_4"
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
            "a": 1
          },
          {
            "a": 9
          }
        ],
        "expected": {
          "a": 9,
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "update",
        "minArgs": 0
      }
    ]
  },
  "6842": {
    "functionNames": [
      "merged_mapping_copy_5"
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
            "a": 1
          },
          {
            "a": 9
          }
        ],
        "expected": {
          "a": 9,
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "update",
        "minArgs": 0
      }
    ]
  },
  "6843": {
    "functionNames": [
      "sorted_copy_plus_1"
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
            -1,
            4
          ]
        ],
        "expected": [
          -1,
          4,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "sort",
        "minArgs": 0
      }
    ]
  },
  "6844": {
    "functionNames": [
      "sorted_copy_plus_2"
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
            -1,
            4
          ]
        ],
        "expected": [
          -1,
          4,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "sort",
        "minArgs": 0
      }
    ]
  },
  "6845": {
    "functionNames": [
      "sorted_copy_plus_3"
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
            -1,
            4
          ]
        ],
        "expected": [
          -1,
          4,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "sort",
        "minArgs": 0
      }
    ]
  },
  "6846": {
    "functionNames": [
      "sorted_copy_plus_4"
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
            -1,
            4
          ]
        ],
        "expected": [
          -1,
          4,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "sort",
        "minArgs": 0
      }
    ]
  },
  "6847": {
    "functionNames": [
      "sorted_copy_plus_5"
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
            -1,
            4
          ]
        ],
        "expected": [
          -1,
          4,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "copy",
        "minArgs": 0
      },
      {
        "functionName": "sort",
        "minArgs": 0
      }
    ]
  },
  "6848": {
    "functionNames": [
      "deepcopy_nested_1"
    ],
    "tests": [
      {
        "args": [
          {
            "items": [
              1,
              2
            ]
          }
        ],
        "expected": {
          "items": [
            1,
            2
          ],
          "marker": {
            "value": 1
          }
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": {
            "value": 1
          }
        }
      },
      {
        "args": [
          {
            "marker": {
              "value": 9
            }
          }
        ],
        "expected": {
          "marker": {
            "value": 1
          }
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deepcopy",
        "minArgs": 0
      }
    ]
  },
  "6849": {
    "functionNames": [
      "deepcopy_nested_2"
    ],
    "tests": [
      {
        "args": [
          {
            "items": [
              1,
              2
            ]
          }
        ],
        "expected": {
          "items": [
            1,
            2
          ],
          "marker": {
            "value": 2
          }
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": {
            "value": 2
          }
        }
      },
      {
        "args": [
          {
            "marker": {
              "value": 9
            }
          }
        ],
        "expected": {
          "marker": {
            "value": 2
          }
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deepcopy",
        "minArgs": 0
      }
    ]
  },
  "6850": {
    "functionNames": [
      "deepcopy_nested_3"
    ],
    "tests": [
      {
        "args": [
          {
            "items": [
              1,
              2
            ]
          }
        ],
        "expected": {
          "items": [
            1,
            2
          ],
          "marker": {
            "value": 3
          }
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": {
            "value": 3
          }
        }
      },
      {
        "args": [
          {
            "marker": {
              "value": 9
            }
          }
        ],
        "expected": {
          "marker": {
            "value": 3
          }
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deepcopy",
        "minArgs": 0
      }
    ]
  },
  "6851": {
    "functionNames": [
      "deepcopy_nested_4"
    ],
    "tests": [
      {
        "args": [
          {
            "items": [
              1,
              2
            ]
          }
        ],
        "expected": {
          "items": [
            1,
            2
          ],
          "marker": {
            "value": 4
          }
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": {
            "value": 4
          }
        }
      },
      {
        "args": [
          {
            "marker": {
              "value": 9
            }
          }
        ],
        "expected": {
          "marker": {
            "value": 4
          }
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deepcopy",
        "minArgs": 0
      }
    ]
  },
  "6852": {
    "functionNames": [
      "deepcopy_nested_5"
    ],
    "tests": [
      {
        "args": [
          {
            "items": [
              1,
              2
            ]
          }
        ],
        "expected": {
          "items": [
            1,
            2
          ],
          "marker": {
            "value": 5
          }
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "marker": {
            "value": 5
          }
        }
      },
      {
        "args": [
          {
            "marker": {
              "value": 9
            }
          }
        ],
        "expected": {
          "marker": {
            "value": 5
          }
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deepcopy",
        "minArgs": 0
      }
    ]
  },
  "6853": {
    "functionNames": [
      "alias_append_1"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          [
            1,
            1
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
        "expected": [
          [
            1
          ],
          [
            1
          ]
        ]
      },
      {
        "args": [
          [
            9,
            8
          ]
        ],
        "expected": [
          [
            9,
            8,
            1
          ],
          [
            9,
            8,
            1
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6854": {
    "functionNames": [
      "alias_append_2"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [
            2
          ],
          [
            2
          ]
        ]
      },
      {
        "args": [
          [
            9,
            8
          ]
        ],
        "expected": [
          [
            9,
            8,
            2
          ],
          [
            9,
            8,
            2
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6855": {
    "functionNames": [
      "alias_append_3"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          [
            1,
            3
          ],
          [
            1,
            3
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [
            3
          ],
          [
            3
          ]
        ]
      },
      {
        "args": [
          [
            9,
            8
          ]
        ],
        "expected": [
          [
            9,
            8,
            3
          ],
          [
            9,
            8,
            3
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6856": {
    "functionNames": [
      "alias_append_4"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          [
            1,
            4
          ],
          [
            1,
            4
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [
            4
          ],
          [
            4
          ]
        ]
      },
      {
        "args": [
          [
            9,
            8
          ]
        ],
        "expected": [
          [
            9,
            8,
            4
          ],
          [
            9,
            8,
            4
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6857": {
    "functionNames": [
      "alias_append_5"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          [
            1,
            5
          ],
          [
            1,
            5
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [
            5
          ],
          [
            5
          ]
        ]
      },
      {
        "args": [
          [
            9,
            8
          ]
        ],
        "expected": [
          [
            9,
            8,
            5
          ],
          [
            9,
            8,
            5
          ]
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6858": {
    "functionNames": [
      "stack_push_1"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6859": {
    "functionNames": [
      "stack_push_2"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6860": {
    "functionNames": [
      "stack_push_3"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6861": {
    "functionNames": [
      "stack_push_4"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6862": {
    "functionNames": [
      "stack_push_5"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6863": {
    "functionNames": [
      "stack_pop_or_1"
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
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6864": {
    "functionNames": [
      "stack_pop_or_2"
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
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6865": {
    "functionNames": [
      "stack_pop_or_3"
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
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6866": {
    "functionNames": [
      "stack_pop_or_4"
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
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6867": {
    "functionNames": [
      "stack_pop_or_5"
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
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6868": {
    "functionNames": [
      "reverse_with_stack_1"
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
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "a",
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6869": {
    "functionNames": [
      "reverse_with_stack_2"
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
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "a",
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6870": {
    "functionNames": [
      "reverse_with_stack_3"
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
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "a",
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6871": {
    "functionNames": [
      "reverse_with_stack_4"
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
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "a",
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6872": {
    "functionNames": [
      "reverse_with_stack_5"
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
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "a",
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6873": {
    "functionNames": [
      "balanced_parentheses_1"
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6874": {
    "functionNames": [
      "balanced_parentheses_2"
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6875": {
    "functionNames": [
      "balanced_parentheses_3"
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6876": {
    "functionNames": [
      "balanced_parentheses_4"
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6877": {
    "functionNames": [
      "balanced_parentheses_5"
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
    ],
    "requiredCallPatterns": [
      {
        "functionName": "pop",
        "minArgs": 0
      }
    ]
  },
  "6878": {
    "functionNames": [
      "queue_enqueue_1"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6879": {
    "functionNames": [
      "queue_enqueue_2"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6880": {
    "functionNames": [
      "queue_enqueue_3"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6881": {
    "functionNames": [
      "queue_enqueue_4"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6882": {
    "functionNames": [
      "queue_enqueue_5"
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
          1,
          2,
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
            9
          ]
        ],
        "expected": [
          9,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "append",
        "minArgs": 0
      }
    ]
  },
  "6883": {
    "functionNames": [
      "queue_dequeue_or_1"
    ],
    "tests": [
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6884": {
    "functionNames": [
      "queue_dequeue_or_2"
    ],
    "tests": [
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6885": {
    "functionNames": [
      "queue_dequeue_or_3"
    ],
    "tests": [
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6886": {
    "functionNames": [
      "queue_dequeue_or_4"
    ],
    "tests": [
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6887": {
    "functionNames": [
      "queue_dequeue_or_5"
    ],
    "tests": [
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6888": {
    "functionNames": [
      "queue_rotate_1"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "rotate",
        "minArgs": 0
      }
    ]
  },
  "6889": {
    "functionNames": [
      "queue_rotate_2"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "rotate",
        "minArgs": 0
      }
    ]
  },
  "6890": {
    "functionNames": [
      "queue_rotate_3"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "rotate",
        "minArgs": 0
      }
    ]
  },
  "6891": {
    "functionNames": [
      "queue_rotate_4"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "rotate",
        "minArgs": 0
      }
    ]
  },
  "6892": {
    "functionNames": [
      "queue_rotate_5"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "rotate",
        "minArgs": 0
      }
    ]
  },
  "6893": {
    "functionNames": [
      "serve_queue_1"
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6894": {
    "functionNames": [
      "serve_queue_2"
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6895": {
    "functionNames": [
      "serve_queue_3"
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6896": {
    "functionNames": [
      "serve_queue_4"
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6897": {
    "functionNames": [
      "serve_queue_5"
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6898": {
    "functionNames": [
      "interleave_queues_1"
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
          [
            1
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6899": {
    "functionNames": [
      "interleave_queues_2"
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
          [
            1
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6900": {
    "functionNames": [
      "interleave_queues_3"
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
          [
            1
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
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6901": {
    "functionNames": [
      "interleave_queues_4"
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
          [
            1
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
          []
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6902": {
    "functionNames": [
      "interleave_queues_5"
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
          [
            1
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
          []
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6903": {
    "functionNames": [
      "queue_last_after_1"
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
          1
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
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6904": {
    "functionNames": [
      "queue_last_after_2"
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
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6905": {
    "functionNames": [
      "queue_last_after_3"
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
            9
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6906": {
    "functionNames": [
      "queue_last_after_4"
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
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6907": {
    "functionNames": [
      "queue_last_after_5"
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
            9
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "popleft",
        "minArgs": 0
      }
    ]
  },
  "6908": {
    "functionNames": [
      "counter_with_marker_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
          "marker": 1
        }
      },
      {
        "args": [
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
          ]
        ],
        "expected": {
          "x": 1,
          "marker": 1
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6909": {
    "functionNames": [
      "counter_with_marker_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
          "marker": 2
        }
      },
      {
        "args": [
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
          ]
        ],
        "expected": {
          "x": 1,
          "marker": 2
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6910": {
    "functionNames": [
      "counter_with_marker_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
          "marker": 3
        }
      },
      {
        "args": [
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
          ]
        ],
        "expected": {
          "x": 1,
          "marker": 3
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6911": {
    "functionNames": [
      "counter_with_marker_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
          "marker": 4
        }
      },
      {
        "args": [
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
          ]
        ],
        "expected": {
          "x": 1,
          "marker": 4
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6912": {
    "functionNames": [
      "counter_with_marker_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
          "marker": 5
        }
      },
      {
        "args": [
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
          ]
        ],
        "expected": {
          "x": 1,
          "marker": 5
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6913": {
    "functionNames": [
      "most_common_sorted_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            3,
            2,
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
      },
      {
        "args": [
          [
            3,
            2,
            3,
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
        "functionName": "Counter",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "6914": {
    "functionNames": [
      "most_common_sorted_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            3,
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
            3,
            2,
            3,
            2
          ]
        ],
        "expected": [
          2,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "6915": {
    "functionNames": [
      "most_common_sorted_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            3,
            2,
            1
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
            3,
            2,
            3,
            2
          ]
        ],
        "expected": [
          2,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "6916": {
    "functionNames": [
      "most_common_sorted_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            3,
            2,
            1
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
            3,
            2,
            3,
            2
          ]
        ],
        "expected": [
          2,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "6917": {
    "functionNames": [
      "most_common_sorted_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            3,
            2,
            1
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
            3,
            2,
            3,
            2
          ]
        ],
        "expected": [
          2,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "6918": {
    "functionNames": [
      "counter_missing_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 3
      },
      {
        "args": [
          [],
          9
        ],
        "expected": 1
      },
      {
        "args": [
          [
            "a"
          ],
          "x"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6919": {
    "functionNames": [
      "counter_missing_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 4
      },
      {
        "args": [
          [],
          9
        ],
        "expected": 2
      },
      {
        "args": [
          [
            "a"
          ],
          "x"
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6920": {
    "functionNames": [
      "counter_missing_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 5
      },
      {
        "args": [
          [],
          9
        ],
        "expected": 3
      },
      {
        "args": [
          [
            "a"
          ],
          "x"
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6921": {
    "functionNames": [
      "counter_missing_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 6
      },
      {
        "args": [
          [],
          9
        ],
        "expected": 4
      },
      {
        "args": [
          [
            "a"
          ],
          "x"
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6922": {
    "functionNames": [
      "counter_missing_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ],
          1
        ],
        "expected": 7
      },
      {
        "args": [
          [],
          9
        ],
        "expected": 5
      },
      {
        "args": [
          [
            "a"
          ],
          "x"
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6923": {
    "functionNames": [
      "counter_merge_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a"
          ],
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
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
          []
        ],
        "expected": {
          "x": 1,
          "marker": 1
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6924": {
    "functionNames": [
      "counter_merge_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a"
          ],
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
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
          []
        ],
        "expected": {
          "x": 1,
          "marker": 2
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6925": {
    "functionNames": [
      "counter_merge_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a"
          ],
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
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
          []
        ],
        "expected": {
          "x": 1,
          "marker": 3
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6926": {
    "functionNames": [
      "counter_merge_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a"
          ],
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
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
          []
        ],
        "expected": {
          "x": 1,
          "marker": 4
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6927": {
    "functionNames": [
      "counter_merge_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a"
          ],
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 2,
          "b": 1,
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
          []
        ],
        "expected": {
          "x": 1,
          "marker": 5
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "Counter",
        "minArgs": 0
      }
    ]
  },
  "6928": {
    "functionNames": [
      "group_by_length_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "to",
            "b"
          ]
        ],
        "expected": {
          "1": [
            "a",
            "b"
          ],
          "2": [
            "to"
          ],
          "marker": [
            1
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": [
            1
          ]
        }
      },
      {
        "args": [
          [
            "python"
          ]
        ],
        "expected": {
          "6": [
            "python"
          ],
          "marker": [
            1
          ]
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6929": {
    "functionNames": [
      "group_by_length_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "to",
            "b"
          ]
        ],
        "expected": {
          "1": [
            "a",
            "b"
          ],
          "2": [
            "to"
          ],
          "marker": [
            2
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": [
            2
          ]
        }
      },
      {
        "args": [
          [
            "python"
          ]
        ],
        "expected": {
          "6": [
            "python"
          ],
          "marker": [
            2
          ]
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6930": {
    "functionNames": [
      "group_by_length_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "to",
            "b"
          ]
        ],
        "expected": {
          "1": [
            "a",
            "b"
          ],
          "2": [
            "to"
          ],
          "marker": [
            3
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": [
            3
          ]
        }
      },
      {
        "args": [
          [
            "python"
          ]
        ],
        "expected": {
          "6": [
            "python"
          ],
          "marker": [
            3
          ]
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6931": {
    "functionNames": [
      "group_by_length_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "to",
            "b"
          ]
        ],
        "expected": {
          "1": [
            "a",
            "b"
          ],
          "2": [
            "to"
          ],
          "marker": [
            4
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": [
            4
          ]
        }
      },
      {
        "args": [
          [
            "python"
          ]
        ],
        "expected": {
          "6": [
            "python"
          ],
          "marker": [
            4
          ]
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6932": {
    "functionNames": [
      "group_by_length_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "to",
            "b"
          ]
        ],
        "expected": {
          "1": [
            "a",
            "b"
          ],
          "2": [
            "to"
          ],
          "marker": [
            5
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": [
            5
          ]
        }
      },
      {
        "args": [
          [
            "python"
          ]
        ],
        "expected": {
          "6": [
            "python"
          ],
          "marker": [
            5
          ]
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6933": {
    "functionNames": [
      "sum_by_key_1"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              1
            ],
            [
              "a",
              2
            ],
            [
              "b",
              4
            ]
          ]
        ],
        "expected": {
          "a": 3,
          "b": 4,
          "marker": 1
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": 1
        }
      },
      {
        "args": [
          [
            [
              "x",
              -1
            ]
          ]
        ],
        "expected": {
          "x": -1,
          "marker": 1
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6934": {
    "functionNames": [
      "sum_by_key_2"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              1
            ],
            [
              "a",
              2
            ],
            [
              "b",
              4
            ]
          ]
        ],
        "expected": {
          "a": 3,
          "b": 4,
          "marker": 2
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": 2
        }
      },
      {
        "args": [
          [
            [
              "x",
              -1
            ]
          ]
        ],
        "expected": {
          "x": -1,
          "marker": 2
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6935": {
    "functionNames": [
      "sum_by_key_3"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              1
            ],
            [
              "a",
              2
            ],
            [
              "b",
              4
            ]
          ]
        ],
        "expected": {
          "a": 3,
          "b": 4,
          "marker": 3
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": 3
        }
      },
      {
        "args": [
          [
            [
              "x",
              -1
            ]
          ]
        ],
        "expected": {
          "x": -1,
          "marker": 3
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6936": {
    "functionNames": [
      "sum_by_key_4"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              1
            ],
            [
              "a",
              2
            ],
            [
              "b",
              4
            ]
          ]
        ],
        "expected": {
          "a": 3,
          "b": 4,
          "marker": 4
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": 4
        }
      },
      {
        "args": [
          [
            [
              "x",
              -1
            ]
          ]
        ],
        "expected": {
          "x": -1,
          "marker": 4
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6937": {
    "functionNames": [
      "sum_by_key_5"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              1
            ],
            [
              "a",
              2
            ],
            [
              "b",
              4
            ]
          ]
        ],
        "expected": {
          "a": 3,
          "b": 4,
          "marker": 5
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "marker": 5
        }
      },
      {
        "args": [
          [
            [
              "x",
              -1
            ]
          ]
        ],
        "expected": {
          "x": -1,
          "marker": 5
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "defaultdict",
        "minArgs": 0
      }
    ]
  },
  "6938": {
    "functionNames": [
      "deque_window_1"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      }
    ]
  },
  "6939": {
    "functionNames": [
      "deque_window_2"
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      }
    ]
  },
  "6940": {
    "functionNames": [
      "deque_window_3"
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
          4,
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      }
    ]
  },
  "6941": {
    "functionNames": [
      "deque_window_4"
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
          4,
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      }
    ]
  },
  "6942": {
    "functionNames": [
      "deque_window_5"
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
          2,
          3,
          4,
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
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      }
    ]
  },
  "6943": {
    "functionNames": [
      "deque_both_ends_1"
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
          1,
          1,
          2,
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          1,
          9,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "appendleft",
        "minArgs": 0
      }
    ]
  },
  "6944": {
    "functionNames": [
      "deque_both_ends_2"
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
          1,
          2,
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          2,
          9,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "appendleft",
        "minArgs": 0
      }
    ]
  },
  "6945": {
    "functionNames": [
      "deque_both_ends_3"
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
          1,
          2,
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          3,
          9,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "appendleft",
        "minArgs": 0
      }
    ]
  },
  "6946": {
    "functionNames": [
      "deque_both_ends_4"
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
          1,
          2,
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          4,
          9,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "appendleft",
        "minArgs": 0
      }
    ]
  },
  "6947": {
    "functionNames": [
      "deque_both_ends_5"
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
          1,
          2,
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          5,
          9,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "deque",
        "minArgs": 0
      },
      {
        "functionName": "appendleft",
        "minArgs": 0
      }
    ]
  },
  "6948": {
    "functionNames": [
      "named_point_total_1"
    ],
    "tests": [
      {
        "args": [
          1,
          2
        ],
        "expected": 4
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
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6949": {
    "functionNames": [
      "named_point_total_2"
    ],
    "tests": [
      {
        "args": [
          1,
          2
        ],
        "expected": 5
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
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6950": {
    "functionNames": [
      "named_point_total_3"
    ],
    "tests": [
      {
        "args": [
          1,
          2
        ],
        "expected": 6
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": 6
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6951": {
    "functionNames": [
      "named_point_total_4"
    ],
    "tests": [
      {
        "args": [
          1,
          2
        ],
        "expected": 7
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": 7
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6952": {
    "functionNames": [
      "named_point_total_5"
    ],
    "tests": [
      {
        "args": [
          1,
          2
        ],
        "expected": 8
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6953": {
    "functionNames": [
      "named_record_dict_1"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          10
        ],
        "expected": {
          "name": "Ada",
          "score": 11
        }
      },
      {
        "args": [
          "",
          0
        ],
        "expected": {
          "name": "",
          "score": 1
        }
      },
      {
        "args": [
          "Noll",
          -1
        ],
        "expected": {
          "name": "Noll",
          "score": 0
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6954": {
    "functionNames": [
      "named_record_dict_2"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          10
        ],
        "expected": {
          "name": "Ada",
          "score": 12
        }
      },
      {
        "args": [
          "",
          0
        ],
        "expected": {
          "name": "",
          "score": 2
        }
      },
      {
        "args": [
          "Noll",
          -1
        ],
        "expected": {
          "name": "Noll",
          "score": 1
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6955": {
    "functionNames": [
      "named_record_dict_3"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          10
        ],
        "expected": {
          "name": "Ada",
          "score": 13
        }
      },
      {
        "args": [
          "",
          0
        ],
        "expected": {
          "name": "",
          "score": 3
        }
      },
      {
        "args": [
          "Noll",
          -1
        ],
        "expected": {
          "name": "Noll",
          "score": 2
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6956": {
    "functionNames": [
      "named_record_dict_4"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          10
        ],
        "expected": {
          "name": "Ada",
          "score": 14
        }
      },
      {
        "args": [
          "",
          0
        ],
        "expected": {
          "name": "",
          "score": 4
        }
      },
      {
        "args": [
          "Noll",
          -1
        ],
        "expected": {
          "name": "Noll",
          "score": 3
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6957": {
    "functionNames": [
      "named_record_dict_5"
    ],
    "tests": [
      {
        "args": [
          "Ada",
          10
        ],
        "expected": {
          "name": "Ada",
          "score": 15
        }
      },
      {
        "args": [
          "",
          0
        ],
        "expected": {
          "name": "",
          "score": 5
        }
      },
      {
        "args": [
          "Noll",
          -1
        ],
        "expected": {
          "name": "Noll",
          "score": 4
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "namedtuple",
        "minArgs": 0
      }
    ]
  },
  "6958": {
    "functionNames": [
      "path_name_1"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme.txt|1"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "data.csv|1"
      },
      {
        "args": [
          "file.py"
        ],
        "expected": "file.py|1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6959": {
    "functionNames": [
      "path_name_2"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme.txt|2"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "data.csv|2"
      },
      {
        "args": [
          "file.py"
        ],
        "expected": "file.py|2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6960": {
    "functionNames": [
      "path_name_3"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme.txt|3"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "data.csv|3"
      },
      {
        "args": [
          "file.py"
        ],
        "expected": "file.py|3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6961": {
    "functionNames": [
      "path_name_4"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme.txt|4"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "data.csv|4"
      },
      {
        "args": [
          "file.py"
        ],
        "expected": "file.py|4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6962": {
    "functionNames": [
      "path_name_5"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme.txt|5"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "data.csv|5"
      },
      {
        "args": [
          "file.py"
        ],
        "expected": "file.py|5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6963": {
    "functionNames": [
      "path_stem_1"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme|1"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": "archive.tar|1"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file|1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6964": {
    "functionNames": [
      "path_stem_2"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme|2"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": "archive.tar|2"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file|2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6965": {
    "functionNames": [
      "path_stem_3"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme|3"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": "archive.tar|3"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file|3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6966": {
    "functionNames": [
      "path_stem_4"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme|4"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": "archive.tar|4"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file|4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6967": {
    "functionNames": [
      "path_stem_5"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "readme|5"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": "archive.tar|5"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file|5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6968": {
    "functionNames": [
      "path_suffix_1"
    ],
    "tests": [
      {
        "args": [
          "A/FILE.PY"
        ],
        "expected": ".py"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": ".gz"
      },
      {
        "args": [
          "README"
        ],
        "expected": ".x1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6969": {
    "functionNames": [
      "path_suffix_2"
    ],
    "tests": [
      {
        "args": [
          "A/FILE.PY"
        ],
        "expected": ".py"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": ".gz"
      },
      {
        "args": [
          "README"
        ],
        "expected": ".x2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6970": {
    "functionNames": [
      "path_suffix_3"
    ],
    "tests": [
      {
        "args": [
          "A/FILE.PY"
        ],
        "expected": ".py"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": ".gz"
      },
      {
        "args": [
          "README"
        ],
        "expected": ".x3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6971": {
    "functionNames": [
      "path_suffix_4"
    ],
    "tests": [
      {
        "args": [
          "A/FILE.PY"
        ],
        "expected": ".py"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": ".gz"
      },
      {
        "args": [
          "README"
        ],
        "expected": ".x4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6972": {
    "functionNames": [
      "path_suffix_5"
    ],
    "tests": [
      {
        "args": [
          "A/FILE.PY"
        ],
        "expected": ".py"
      },
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": ".gz"
      },
      {
        "args": [
          "README"
        ],
        "expected": ".x5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6973": {
    "functionNames": [
      "path_parent_name_1"
    ],
    "tests": [
      {
        "args": [
          "docs/guides/readme.txt"
        ],
        "expected": "guides|1"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "tmp|1"
      },
      {
        "args": [
          "folder/file"
        ],
        "expected": "folder|1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6974": {
    "functionNames": [
      "path_parent_name_2"
    ],
    "tests": [
      {
        "args": [
          "docs/guides/readme.txt"
        ],
        "expected": "guides|2"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "tmp|2"
      },
      {
        "args": [
          "folder/file"
        ],
        "expected": "folder|2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6975": {
    "functionNames": [
      "path_parent_name_3"
    ],
    "tests": [
      {
        "args": [
          "docs/guides/readme.txt"
        ],
        "expected": "guides|3"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "tmp|3"
      },
      {
        "args": [
          "folder/file"
        ],
        "expected": "folder|3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6976": {
    "functionNames": [
      "path_parent_name_4"
    ],
    "tests": [
      {
        "args": [
          "docs/guides/readme.txt"
        ],
        "expected": "guides|4"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "tmp|4"
      },
      {
        "args": [
          "folder/file"
        ],
        "expected": "folder|4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6977": {
    "functionNames": [
      "path_parent_name_5"
    ],
    "tests": [
      {
        "args": [
          "docs/guides/readme.txt"
        ],
        "expected": "guides|5"
      },
      {
        "args": [
          "/tmp/data.csv"
        ],
        "expected": "tmp|5"
      },
      {
        "args": [
          "folder/file"
        ],
        "expected": "folder|5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6978": {
    "functionNames": [
      "path_parts_from_1"
    ],
    "tests": [
      {
        "args": [
          "a/b/c/d/e/f"
        ],
        "expected": [
          "b",
          "c",
          "d",
          "e",
          "f"
        ]
      },
      {
        "args": [
          "one/two"
        ],
        "expected": [
          "two"
        ]
      },
      {
        "args": [
          "/root/sub/file"
        ],
        "expected": [
          "root",
          "sub",
          "file"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6979": {
    "functionNames": [
      "path_parts_from_2"
    ],
    "tests": [
      {
        "args": [
          "a/b/c/d/e/f"
        ],
        "expected": [
          "c",
          "d",
          "e",
          "f"
        ]
      },
      {
        "args": [
          "one/two"
        ],
        "expected": []
      },
      {
        "args": [
          "/root/sub/file"
        ],
        "expected": [
          "sub",
          "file"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6980": {
    "functionNames": [
      "path_parts_from_3"
    ],
    "tests": [
      {
        "args": [
          "a/b/c/d/e/f"
        ],
        "expected": [
          "d",
          "e",
          "f"
        ]
      },
      {
        "args": [
          "one/two"
        ],
        "expected": []
      },
      {
        "args": [
          "/root/sub/file"
        ],
        "expected": [
          "file"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6981": {
    "functionNames": [
      "path_parts_from_4"
    ],
    "tests": [
      {
        "args": [
          "a/b/c/d/e/f"
        ],
        "expected": [
          "e",
          "f"
        ]
      },
      {
        "args": [
          "one/two"
        ],
        "expected": []
      },
      {
        "args": [
          "/root/sub/file"
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6982": {
    "functionNames": [
      "path_parts_from_5"
    ],
    "tests": [
      {
        "args": [
          "a/b/c/d/e/f"
        ],
        "expected": [
          "f"
        ]
      },
      {
        "args": [
          "one/two"
        ],
        "expected": []
      },
      {
        "args": [
          "/root/sub/file"
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6983": {
    "functionNames": [
      "path_change_suffix_1"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "docs/readme.v1"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file.v1"
      },
      {
        "args": [
          "a/archive.tar.gz"
        ],
        "expected": "a/archive.tar.v1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "with_suffix",
        "minArgs": 0
      }
    ]
  },
  "6984": {
    "functionNames": [
      "path_change_suffix_2"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "docs/readme.v2"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file.v2"
      },
      {
        "args": [
          "a/archive.tar.gz"
        ],
        "expected": "a/archive.tar.v2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "with_suffix",
        "minArgs": 0
      }
    ]
  },
  "6985": {
    "functionNames": [
      "path_change_suffix_3"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "docs/readme.v3"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file.v3"
      },
      {
        "args": [
          "a/archive.tar.gz"
        ],
        "expected": "a/archive.tar.v3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "with_suffix",
        "minArgs": 0
      }
    ]
  },
  "6986": {
    "functionNames": [
      "path_change_suffix_4"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "docs/readme.v4"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file.v4"
      },
      {
        "args": [
          "a/archive.tar.gz"
        ],
        "expected": "a/archive.tar.v4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "with_suffix",
        "minArgs": 0
      }
    ]
  },
  "6987": {
    "functionNames": [
      "path_change_suffix_5"
    ],
    "tests": [
      {
        "args": [
          "docs/readme.txt"
        ],
        "expected": "docs/readme.v5"
      },
      {
        "args": [
          "file"
        ],
        "expected": "file.v5"
      },
      {
        "args": [
          "a/archive.tar.gz"
        ],
        "expected": "a/archive.tar.v5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "with_suffix",
        "minArgs": 0
      }
    ]
  },
  "6988": {
    "functionNames": [
      "path_join_1"
    ],
    "tests": [
      {
        "args": [
          "root",
          "docs"
        ],
        "expected": "root/docs/level_1"
      },
      {
        "args": [
          "/tmp",
          "data"
        ],
        "expected": "/tmp/data/level_1"
      },
      {
        "args": [
          "a/b",
          "c"
        ],
        "expected": "a/b/c/level_1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6989": {
    "functionNames": [
      "path_join_2"
    ],
    "tests": [
      {
        "args": [
          "root",
          "docs"
        ],
        "expected": "root/docs/level_2"
      },
      {
        "args": [
          "/tmp",
          "data"
        ],
        "expected": "/tmp/data/level_2"
      },
      {
        "args": [
          "a/b",
          "c"
        ],
        "expected": "a/b/c/level_2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6990": {
    "functionNames": [
      "path_join_3"
    ],
    "tests": [
      {
        "args": [
          "root",
          "docs"
        ],
        "expected": "root/docs/level_3"
      },
      {
        "args": [
          "/tmp",
          "data"
        ],
        "expected": "/tmp/data/level_3"
      },
      {
        "args": [
          "a/b",
          "c"
        ],
        "expected": "a/b/c/level_3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6991": {
    "functionNames": [
      "path_join_4"
    ],
    "tests": [
      {
        "args": [
          "root",
          "docs"
        ],
        "expected": "root/docs/level_4"
      },
      {
        "args": [
          "/tmp",
          "data"
        ],
        "expected": "/tmp/data/level_4"
      },
      {
        "args": [
          "a/b",
          "c"
        ],
        "expected": "a/b/c/level_4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6992": {
    "functionNames": [
      "path_join_5"
    ],
    "tests": [
      {
        "args": [
          "root",
          "docs"
        ],
        "expected": "root/docs/level_5"
      },
      {
        "args": [
          "/tmp",
          "data"
        ],
        "expected": "/tmp/data/level_5"
      },
      {
        "args": [
          "a/b",
          "c"
        ],
        "expected": "a/b/c/level_5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6993": {
    "functionNames": [
      "path_relative_1"
    ],
    "tests": [
      {
        "args": [
          "root/docs/file.txt",
          "root"
        ],
        "expected": "docs/file.txt/m1"
      },
      {
        "args": [
          "/a/b/c",
          "/a"
        ],
        "expected": "b/c/m1"
      },
      {
        "args": [
          "x/y",
          "x"
        ],
        "expected": "y/m1"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "relative_to",
        "minArgs": 0
      }
    ]
  },
  "6994": {
    "functionNames": [
      "path_relative_2"
    ],
    "tests": [
      {
        "args": [
          "root/docs/file.txt",
          "root"
        ],
        "expected": "docs/file.txt/m2"
      },
      {
        "args": [
          "/a/b/c",
          "/a"
        ],
        "expected": "b/c/m2"
      },
      {
        "args": [
          "x/y",
          "x"
        ],
        "expected": "y/m2"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "relative_to",
        "minArgs": 0
      }
    ]
  },
  "6995": {
    "functionNames": [
      "path_relative_3"
    ],
    "tests": [
      {
        "args": [
          "root/docs/file.txt",
          "root"
        ],
        "expected": "docs/file.txt/m3"
      },
      {
        "args": [
          "/a/b/c",
          "/a"
        ],
        "expected": "b/c/m3"
      },
      {
        "args": [
          "x/y",
          "x"
        ],
        "expected": "y/m3"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "relative_to",
        "minArgs": 0
      }
    ]
  },
  "6996": {
    "functionNames": [
      "path_relative_4"
    ],
    "tests": [
      {
        "args": [
          "root/docs/file.txt",
          "root"
        ],
        "expected": "docs/file.txt/m4"
      },
      {
        "args": [
          "/a/b/c",
          "/a"
        ],
        "expected": "b/c/m4"
      },
      {
        "args": [
          "x/y",
          "x"
        ],
        "expected": "y/m4"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "relative_to",
        "minArgs": 0
      }
    ]
  },
  "6997": {
    "functionNames": [
      "path_relative_5"
    ],
    "tests": [
      {
        "args": [
          "root/docs/file.txt",
          "root"
        ],
        "expected": "docs/file.txt/m5"
      },
      {
        "args": [
          "/a/b/c",
          "/a"
        ],
        "expected": "b/c/m5"
      },
      {
        "args": [
          "x/y",
          "x"
        ],
        "expected": "y/m5"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      },
      {
        "functionName": "relative_to",
        "minArgs": 0
      }
    ]
  },
  "6998": {
    "functionNames": [
      "filter_suffix_1"
    ],
    "tests": [
      {
        "args": [
          [
            "b.py",
            "a.PY",
            "c.txt"
          ],
          ".py"
        ],
        "expected": [
          "a.PY",
          "b.py",
          "marker_1"
        ]
      },
      {
        "args": [
          [],
          ".txt"
        ],
        "expected": [
          "marker_1"
        ]
      },
      {
        "args": [
          [
            "x.csv"
          ],
          ".json"
        ],
        "expected": [
          "marker_1"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "6999": {
    "functionNames": [
      "filter_suffix_2"
    ],
    "tests": [
      {
        "args": [
          [
            "b.py",
            "a.PY",
            "c.txt"
          ],
          ".py"
        ],
        "expected": [
          "a.PY",
          "b.py",
          "marker_2"
        ]
      },
      {
        "args": [
          [],
          ".txt"
        ],
        "expected": [
          "marker_2"
        ]
      },
      {
        "args": [
          [
            "x.csv"
          ],
          ".json"
        ],
        "expected": [
          "marker_2"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7000": {
    "functionNames": [
      "filter_suffix_3"
    ],
    "tests": [
      {
        "args": [
          [
            "b.py",
            "a.PY",
            "c.txt"
          ],
          ".py"
        ],
        "expected": [
          "a.PY",
          "b.py",
          "marker_3"
        ]
      },
      {
        "args": [
          [],
          ".txt"
        ],
        "expected": [
          "marker_3"
        ]
      },
      {
        "args": [
          [
            "x.csv"
          ],
          ".json"
        ],
        "expected": [
          "marker_3"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7001": {
    "functionNames": [
      "filter_suffix_4"
    ],
    "tests": [
      {
        "args": [
          [
            "b.py",
            "a.PY",
            "c.txt"
          ],
          ".py"
        ],
        "expected": [
          "a.PY",
          "b.py",
          "marker_4"
        ]
      },
      {
        "args": [
          [],
          ".txt"
        ],
        "expected": [
          "marker_4"
        ]
      },
      {
        "args": [
          [
            "x.csv"
          ],
          ".json"
        ],
        "expected": [
          "marker_4"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7002": {
    "functionNames": [
      "filter_suffix_5"
    ],
    "tests": [
      {
        "args": [
          [
            "b.py",
            "a.PY",
            "c.txt"
          ],
          ".py"
        ],
        "expected": [
          "a.PY",
          "b.py",
          "marker_5"
        ]
      },
      {
        "args": [
          [],
          ".txt"
        ],
        "expected": [
          "marker_5"
        ]
      },
      {
        "args": [
          [
            "x.csv"
          ],
          ".json"
        ],
        "expected": [
          "marker_5"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7003": {
    "functionNames": [
      "path_suffixes_1"
    ],
    "tests": [
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": [
          ".tar",
          ".gz",
          ".m1"
        ]
      },
      {
        "args": [
          "file.txt"
        ],
        "expected": [
          ".txt",
          ".m1"
        ]
      },
      {
        "args": [
          "README"
        ],
        "expected": [
          ".m1"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7004": {
    "functionNames": [
      "path_suffixes_2"
    ],
    "tests": [
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": [
          ".tar",
          ".gz",
          ".m2"
        ]
      },
      {
        "args": [
          "file.txt"
        ],
        "expected": [
          ".txt",
          ".m2"
        ]
      },
      {
        "args": [
          "README"
        ],
        "expected": [
          ".m2"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7005": {
    "functionNames": [
      "path_suffixes_3"
    ],
    "tests": [
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": [
          ".tar",
          ".gz",
          ".m3"
        ]
      },
      {
        "args": [
          "file.txt"
        ],
        "expected": [
          ".txt",
          ".m3"
        ]
      },
      {
        "args": [
          "README"
        ],
        "expected": [
          ".m3"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7006": {
    "functionNames": [
      "path_suffixes_4"
    ],
    "tests": [
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": [
          ".tar",
          ".gz",
          ".m4"
        ]
      },
      {
        "args": [
          "file.txt"
        ],
        "expected": [
          ".txt",
          ".m4"
        ]
      },
      {
        "args": [
          "README"
        ],
        "expected": [
          ".m4"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7007": {
    "functionNames": [
      "path_suffixes_5"
    ],
    "tests": [
      {
        "args": [
          "archive.tar.gz"
        ],
        "expected": [
          ".tar",
          ".gz",
          ".m5"
        ]
      },
      {
        "args": [
          "file.txt"
        ],
        "expected": [
          ".txt",
          ".m5"
        ]
      },
      {
        "args": [
          "README"
        ],
        "expected": [
          ".m5"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "PurePosixPath",
        "minArgs": 0
      }
    ]
  },
  "7008": {
    "functionNames": [
      "csv_first_row_1"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2"
        ],
        "expected": [
          "a",
          "b",
          "1"
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": [
          "1"
        ]
      },
      {
        "args": [
          "x"
        ],
        "expected": [
          "x",
          "1"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7009": {
    "functionNames": [
      "csv_first_row_2"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2"
        ],
        "expected": [
          "a",
          "b",
          "2"
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": [
          "2"
        ]
      },
      {
        "args": [
          "x"
        ],
        "expected": [
          "x",
          "2"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7010": {
    "functionNames": [
      "csv_first_row_3"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2"
        ],
        "expected": [
          "a",
          "b",
          "3"
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": [
          "3"
        ]
      },
      {
        "args": [
          "x"
        ],
        "expected": [
          "x",
          "3"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7011": {
    "functionNames": [
      "csv_first_row_4"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2"
        ],
        "expected": [
          "a",
          "b",
          "4"
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": [
          "4"
        ]
      },
      {
        "args": [
          "x"
        ],
        "expected": [
          "x",
          "4"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7012": {
    "functionNames": [
      "csv_first_row_5"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2"
        ],
        "expected": [
          "a",
          "b",
          "5"
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": [
          "5"
        ]
      },
      {
        "args": [
          "x"
        ],
        "expected": [
          "x",
          "5"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7013": {
    "functionNames": [
      "csv_integer_row_1"
    ],
    "tests": [
      {
        "args": [
          "1,2,3"
        ],
        "expected": [
          2,
          3,
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
          "-1,5"
        ],
        "expected": [
          0,
          6
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7014": {
    "functionNames": [
      "csv_integer_row_2"
    ],
    "tests": [
      {
        "args": [
          "1,2,3"
        ],
        "expected": [
          3,
          4,
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
          "-1,5"
        ],
        "expected": [
          1,
          7
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7015": {
    "functionNames": [
      "csv_integer_row_3"
    ],
    "tests": [
      {
        "args": [
          "1,2,3"
        ],
        "expected": [
          4,
          5,
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
          "-1,5"
        ],
        "expected": [
          2,
          8
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7016": {
    "functionNames": [
      "csv_integer_row_4"
    ],
    "tests": [
      {
        "args": [
          "1,2,3"
        ],
        "expected": [
          5,
          6,
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
          "-1,5"
        ],
        "expected": [
          3,
          9
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7017": {
    "functionNames": [
      "csv_integer_row_5"
    ],
    "tests": [
      {
        "args": [
          "1,2,3"
        ],
        "expected": [
          6,
          7,
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
          "-1,5"
        ],
        "expected": [
          4,
          10
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7018": {
    "functionNames": [
      "csv_column_1"
    ],
    "tests": [
      {
        "args": [
          "name,age\nAda,36\nBob,20",
          "name"
        ],
        "expected": [
          "Ada",
          "Bob",
          "1"
        ]
      },
      {
        "args": [
          "x\n1",
          "x"
        ],
        "expected": [
          "1",
          "1"
        ]
      },
      {
        "args": [
          "a,b\n",
          "b"
        ],
        "expected": [
          "1"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7019": {
    "functionNames": [
      "csv_column_2"
    ],
    "tests": [
      {
        "args": [
          "name,age\nAda,36\nBob,20",
          "name"
        ],
        "expected": [
          "Ada",
          "Bob",
          "2"
        ]
      },
      {
        "args": [
          "x\n1",
          "x"
        ],
        "expected": [
          "1",
          "2"
        ]
      },
      {
        "args": [
          "a,b\n",
          "b"
        ],
        "expected": [
          "2"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7020": {
    "functionNames": [
      "csv_column_3"
    ],
    "tests": [
      {
        "args": [
          "name,age\nAda,36\nBob,20",
          "name"
        ],
        "expected": [
          "Ada",
          "Bob",
          "3"
        ]
      },
      {
        "args": [
          "x\n1",
          "x"
        ],
        "expected": [
          "1",
          "3"
        ]
      },
      {
        "args": [
          "a,b\n",
          "b"
        ],
        "expected": [
          "3"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7021": {
    "functionNames": [
      "csv_column_4"
    ],
    "tests": [
      {
        "args": [
          "name,age\nAda,36\nBob,20",
          "name"
        ],
        "expected": [
          "Ada",
          "Bob",
          "4"
        ]
      },
      {
        "args": [
          "x\n1",
          "x"
        ],
        "expected": [
          "1",
          "4"
        ]
      },
      {
        "args": [
          "a,b\n",
          "b"
        ],
        "expected": [
          "4"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7022": {
    "functionNames": [
      "csv_column_5"
    ],
    "tests": [
      {
        "args": [
          "name,age\nAda,36\nBob,20",
          "name"
        ],
        "expected": [
          "Ada",
          "Bob",
          "5"
        ]
      },
      {
        "args": [
          "x\n1",
          "x"
        ],
        "expected": [
          "1",
          "5"
        ]
      },
      {
        "args": [
          "a,b\n",
          "b"
        ],
        "expected": [
          "5"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7023": {
    "functionNames": [
      "csv_row_count_1"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2\n3,4"
        ],
        "expected": 3
      },
      {
        "args": [
          "a"
        ],
        "expected": 1
      },
      {
        "args": [
          ""
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7024": {
    "functionNames": [
      "csv_row_count_2"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2\n3,4"
        ],
        "expected": 4
      },
      {
        "args": [
          "a"
        ],
        "expected": 2
      },
      {
        "args": [
          ""
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7025": {
    "functionNames": [
      "csv_row_count_3"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2\n3,4"
        ],
        "expected": 5
      },
      {
        "args": [
          "a"
        ],
        "expected": 3
      },
      {
        "args": [
          ""
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7026": {
    "functionNames": [
      "csv_row_count_4"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2\n3,4"
        ],
        "expected": 6
      },
      {
        "args": [
          "a"
        ],
        "expected": 4
      },
      {
        "args": [
          ""
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7027": {
    "functionNames": [
      "csv_row_count_5"
    ],
    "tests": [
      {
        "args": [
          "a,b\n1,2\n3,4"
        ],
        "expected": 7
      },
      {
        "args": [
          "a"
        ],
        "expected": 5
      },
      {
        "args": [
          ""
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "reader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7028": {
    "functionNames": [
      "csv_select_rows_1"
    ],
    "tests": [
      {
        "args": [
          "name,role\nAda,dev\nBob,test",
          "role",
          "dev"
        ],
        "expected": [
          {
            "name": "Ada",
            "role": "dev"
          },
          {
            "marker": "1"
          }
        ]
      },
      {
        "args": [
          "x\n1",
          "x",
          "9"
        ],
        "expected": [
          {
            "marker": "1"
          }
        ]
      },
      {
        "args": [
          "a,b\n",
          "a",
          "x"
        ],
        "expected": [
          {
            "marker": "1"
          }
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7029": {
    "functionNames": [
      "csv_select_rows_2"
    ],
    "tests": [
      {
        "args": [
          "name,role\nAda,dev\nBob,test",
          "role",
          "dev"
        ],
        "expected": [
          {
            "name": "Ada",
            "role": "dev"
          },
          {
            "marker": "2"
          }
        ]
      },
      {
        "args": [
          "x\n1",
          "x",
          "9"
        ],
        "expected": [
          {
            "marker": "2"
          }
        ]
      },
      {
        "args": [
          "a,b\n",
          "a",
          "x"
        ],
        "expected": [
          {
            "marker": "2"
          }
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7030": {
    "functionNames": [
      "csv_select_rows_3"
    ],
    "tests": [
      {
        "args": [
          "name,role\nAda,dev\nBob,test",
          "role",
          "dev"
        ],
        "expected": [
          {
            "name": "Ada",
            "role": "dev"
          },
          {
            "marker": "3"
          }
        ]
      },
      {
        "args": [
          "x\n1",
          "x",
          "9"
        ],
        "expected": [
          {
            "marker": "3"
          }
        ]
      },
      {
        "args": [
          "a,b\n",
          "a",
          "x"
        ],
        "expected": [
          {
            "marker": "3"
          }
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7031": {
    "functionNames": [
      "csv_select_rows_4"
    ],
    "tests": [
      {
        "args": [
          "name,role\nAda,dev\nBob,test",
          "role",
          "dev"
        ],
        "expected": [
          {
            "name": "Ada",
            "role": "dev"
          },
          {
            "marker": "4"
          }
        ]
      },
      {
        "args": [
          "x\n1",
          "x",
          "9"
        ],
        "expected": [
          {
            "marker": "4"
          }
        ]
      },
      {
        "args": [
          "a,b\n",
          "a",
          "x"
        ],
        "expected": [
          {
            "marker": "4"
          }
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7032": {
    "functionNames": [
      "csv_select_rows_5"
    ],
    "tests": [
      {
        "args": [
          "name,role\nAda,dev\nBob,test",
          "role",
          "dev"
        ],
        "expected": [
          {
            "name": "Ada",
            "role": "dev"
          },
          {
            "marker": "5"
          }
        ]
      },
      {
        "args": [
          "x\n1",
          "x",
          "9"
        ],
        "expected": [
          {
            "marker": "5"
          }
        ]
      },
      {
        "args": [
          "a,b\n",
          "a",
          "x"
        ],
        "expected": [
          {
            "marker": "5"
          }
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "DictReader",
        "minArgs": 0
      },
      {
        "functionName": "StringIO",
        "minArgs": 0
      }
    ]
  },
  "7033": {
    "functionNames": [
      "json_value_or_1"
    ],
    "tests": [
      {
        "args": [
          "{\"a\": 1}",
          "a"
        ],
        "expected": 1
      },
      {
        "args": [
          "{}",
          "x"
        ],
        "expected": 1
      },
      {
        "args": [
          "{\"x\": 0}",
          "x"
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7034": {
    "functionNames": [
      "json_value_or_2"
    ],
    "tests": [
      {
        "args": [
          "{\"a\": 1}",
          "a"
        ],
        "expected": 1
      },
      {
        "args": [
          "{}",
          "x"
        ],
        "expected": 2
      },
      {
        "args": [
          "{\"x\": 0}",
          "x"
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7035": {
    "functionNames": [
      "json_value_or_3"
    ],
    "tests": [
      {
        "args": [
          "{\"a\": 1}",
          "a"
        ],
        "expected": 1
      },
      {
        "args": [
          "{}",
          "x"
        ],
        "expected": 3
      },
      {
        "args": [
          "{\"x\": 0}",
          "x"
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7036": {
    "functionNames": [
      "json_value_or_4"
    ],
    "tests": [
      {
        "args": [
          "{\"a\": 1}",
          "a"
        ],
        "expected": 1
      },
      {
        "args": [
          "{}",
          "x"
        ],
        "expected": 4
      },
      {
        "args": [
          "{\"x\": 0}",
          "x"
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7037": {
    "functionNames": [
      "json_value_or_5"
    ],
    "tests": [
      {
        "args": [
          "{\"a\": 1}",
          "a"
        ],
        "expected": 1
      },
      {
        "args": [
          "{}",
          "x"
        ],
        "expected": 5
      },
      {
        "args": [
          "{\"x\": 0}",
          "x"
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7038": {
    "functionNames": [
      "json_sorted_keys_1"
    ],
    "tests": [
      {
        "args": [
          "{\"b\": 2, \"a\": 1}"
        ],
        "expected": [
          "a",
          "b",
          "marker_1"
        ]
      },
      {
        "args": [
          "{}"
        ],
        "expected": [
          "marker_1"
        ]
      },
      {
        "args": [
          "{\"x\": 0}"
        ],
        "expected": [
          "x",
          "marker_1"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "7039": {
    "functionNames": [
      "json_sorted_keys_2"
    ],
    "tests": [
      {
        "args": [
          "{\"b\": 2, \"a\": 1}"
        ],
        "expected": [
          "a",
          "b",
          "marker_2"
        ]
      },
      {
        "args": [
          "{}"
        ],
        "expected": [
          "marker_2"
        ]
      },
      {
        "args": [
          "{\"x\": 0}"
        ],
        "expected": [
          "x",
          "marker_2"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "7040": {
    "functionNames": [
      "json_sorted_keys_3"
    ],
    "tests": [
      {
        "args": [
          "{\"b\": 2, \"a\": 1}"
        ],
        "expected": [
          "a",
          "b",
          "marker_3"
        ]
      },
      {
        "args": [
          "{}"
        ],
        "expected": [
          "marker_3"
        ]
      },
      {
        "args": [
          "{\"x\": 0}"
        ],
        "expected": [
          "x",
          "marker_3"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "7041": {
    "functionNames": [
      "json_sorted_keys_4"
    ],
    "tests": [
      {
        "args": [
          "{\"b\": 2, \"a\": 1}"
        ],
        "expected": [
          "a",
          "b",
          "marker_4"
        ]
      },
      {
        "args": [
          "{}"
        ],
        "expected": [
          "marker_4"
        ]
      },
      {
        "args": [
          "{\"x\": 0}"
        ],
        "expected": [
          "x",
          "marker_4"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "7042": {
    "functionNames": [
      "json_sorted_keys_5"
    ],
    "tests": [
      {
        "args": [
          "{\"b\": 2, \"a\": 1}"
        ],
        "expected": [
          "a",
          "b",
          "marker_5"
        ]
      },
      {
        "args": [
          "{}"
        ],
        "expected": [
          "marker_5"
        ]
      },
      {
        "args": [
          "{\"x\": 0}"
        ],
        "expected": [
          "x",
          "marker_5"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "7043": {
    "functionNames": [
      "json_compact_1"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": "{\"marker\":1,\"value\":{\"a\":1,\"b\":2}}"
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": "{\"marker\":1,\"value\":[1,2]}"
      },
      {
        "args": [
          null
        ],
        "expected": "{\"marker\":1,\"value\":null}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7044": {
    "functionNames": [
      "json_compact_2"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": "{\"marker\":2,\"value\":{\"a\":1,\"b\":2}}"
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": "{\"marker\":2,\"value\":[1,2]}"
      },
      {
        "args": [
          null
        ],
        "expected": "{\"marker\":2,\"value\":null}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7045": {
    "functionNames": [
      "json_compact_3"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": "{\"marker\":3,\"value\":{\"a\":1,\"b\":2}}"
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": "{\"marker\":3,\"value\":[1,2]}"
      },
      {
        "args": [
          null
        ],
        "expected": "{\"marker\":3,\"value\":null}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7046": {
    "functionNames": [
      "json_compact_4"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": "{\"marker\":4,\"value\":{\"a\":1,\"b\":2}}"
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": "{\"marker\":4,\"value\":[1,2]}"
      },
      {
        "args": [
          null
        ],
        "expected": "{\"marker\":4,\"value\":null}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7047": {
    "functionNames": [
      "json_compact_5"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": "{\"marker\":5,\"value\":{\"a\":1,\"b\":2}}"
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": "{\"marker\":5,\"value\":[1,2]}"
      },
      {
        "args": [
          null
        ],
        "expected": "{\"marker\":5,\"value\":null}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7048": {
    "functionNames": [
      "json_nested_value_1"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":{\"b\":2}}",
          "a",
          "b"
        ],
        "expected": 2
      },
      {
        "args": [
          "{}",
          "x",
          "y"
        ],
        "expected": 1
      },
      {
        "args": [
          "{\"a\":1}",
          "a",
          "b"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7049": {
    "functionNames": [
      "json_nested_value_2"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":{\"b\":2}}",
          "a",
          "b"
        ],
        "expected": 2
      },
      {
        "args": [
          "{}",
          "x",
          "y"
        ],
        "expected": 2
      },
      {
        "args": [
          "{\"a\":1}",
          "a",
          "b"
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7050": {
    "functionNames": [
      "json_nested_value_3"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":{\"b\":2}}",
          "a",
          "b"
        ],
        "expected": 2
      },
      {
        "args": [
          "{}",
          "x",
          "y"
        ],
        "expected": 3
      },
      {
        "args": [
          "{\"a\":1}",
          "a",
          "b"
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7051": {
    "functionNames": [
      "json_nested_value_4"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":{\"b\":2}}",
          "a",
          "b"
        ],
        "expected": 2
      },
      {
        "args": [
          "{}",
          "x",
          "y"
        ],
        "expected": 4
      },
      {
        "args": [
          "{\"a\":1}",
          "a",
          "b"
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7052": {
    "functionNames": [
      "json_nested_value_5"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":{\"b\":2}}",
          "a",
          "b"
        ],
        "expected": 2
      },
      {
        "args": [
          "{}",
          "x",
          "y"
        ],
        "expected": 5
      },
      {
        "args": [
          "{\"a\":1}",
          "a",
          "b"
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      }
    ]
  },
  "7053": {
    "functionNames": [
      "json_update_1"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":1}",
          "b",
          2
        ],
        "expected": "{\"a\":1,\"b\":2,\"marker\":1}"
      },
      {
        "args": [
          "{}",
          "x",
          0
        ],
        "expected": "{\"marker\":1,\"x\":0}"
      },
      {
        "args": [
          "{\"marker\":9}",
          "a",
          true
        ],
        "expected": "{\"a\":true,\"marker\":1}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7054": {
    "functionNames": [
      "json_update_2"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":1}",
          "b",
          2
        ],
        "expected": "{\"a\":1,\"b\":2,\"marker\":2}"
      },
      {
        "args": [
          "{}",
          "x",
          0
        ],
        "expected": "{\"marker\":2,\"x\":0}"
      },
      {
        "args": [
          "{\"marker\":9}",
          "a",
          true
        ],
        "expected": "{\"a\":true,\"marker\":2}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7055": {
    "functionNames": [
      "json_update_3"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":1}",
          "b",
          2
        ],
        "expected": "{\"a\":1,\"b\":2,\"marker\":3}"
      },
      {
        "args": [
          "{}",
          "x",
          0
        ],
        "expected": "{\"marker\":3,\"x\":0}"
      },
      {
        "args": [
          "{\"marker\":9}",
          "a",
          true
        ],
        "expected": "{\"a\":true,\"marker\":3}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7056": {
    "functionNames": [
      "json_update_4"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":1}",
          "b",
          2
        ],
        "expected": "{\"a\":1,\"b\":2,\"marker\":4}"
      },
      {
        "args": [
          "{}",
          "x",
          0
        ],
        "expected": "{\"marker\":4,\"x\":0}"
      },
      {
        "args": [
          "{\"marker\":9}",
          "a",
          true
        ],
        "expected": "{\"a\":true,\"marker\":4}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7057": {
    "functionNames": [
      "json_update_5"
    ],
    "tests": [
      {
        "args": [
          "{\"a\":1}",
          "b",
          2
        ],
        "expected": "{\"a\":1,\"b\":2,\"marker\":5}"
      },
      {
        "args": [
          "{}",
          "x",
          0
        ],
        "expected": "{\"marker\":5,\"x\":0}"
      },
      {
        "args": [
          "{\"marker\":9}",
          "a",
          true
        ],
        "expected": "{\"a\":true,\"marker\":5}"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "loads",
        "minArgs": 0
      },
      {
        "functionName": "dumps",
        "minArgs": 0
      }
    ]
  },
  "7058": {
    "functionNames": [
      "linear_search_1"
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
  "7059": {
    "functionNames": [
      "linear_search_2"
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
  "7060": {
    "functionNames": [
      "linear_search_3"
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
  "7061": {
    "functionNames": [
      "linear_search_4"
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
  "7062": {
    "functionNames": [
      "linear_search_5"
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
  "7063": {
    "functionNames": [
      "prefix_sums_1"
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
  "7064": {
    "functionNames": [
      "prefix_sums_2"
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
  "7065": {
    "functionNames": [
      "prefix_sums_3"
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
  "7066": {
    "functionNames": [
      "prefix_sums_4"
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
  "7067": {
    "functionNames": [
      "prefix_sums_5"
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
  "7068": {
    "functionNames": [
      "dedupe_ordered_1"
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
            "a",
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b",
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
  "7069": {
    "functionNames": [
      "dedupe_ordered_2"
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
            "a",
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b",
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
  "7070": {
    "functionNames": [
      "dedupe_ordered_3"
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
            "a",
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b",
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
  "7071": {
    "functionNames": [
      "dedupe_ordered_4"
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
            "a",
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b",
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
  "7072": {
    "functionNames": [
      "dedupe_ordered_5"
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
            "a",
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b",
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
  "7073": {
    "functionNames": [
      "merge_sorted_1"
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
          [
            -2,
            5
          ],
          [
            -1,
            6
          ]
        ],
        "expected": [
          -2,
          -1,
          5,
          6,
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
  "7074": {
    "functionNames": [
      "merge_sorted_2"
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
          [
            -2,
            5
          ],
          [
            -1,
            6
          ]
        ],
        "expected": [
          -2,
          -1,
          5,
          6,
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
  "7075": {
    "functionNames": [
      "merge_sorted_3"
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
            1
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
            5
          ],
          [
            -1,
            6
          ]
        ],
        "expected": [
          -2,
          -1,
          5,
          6,
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
  "7076": {
    "functionNames": [
      "merge_sorted_4"
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
            1
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
            -2,
            5
          ],
          [
            -1,
            6
          ]
        ],
        "expected": [
          -2,
          -1,
          5,
          6,
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
  "7077": {
    "functionNames": [
      "merge_sorted_5"
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
            1
          ]
        ],
        "expected": [
          1,
          5
        ]
      },
      {
        "args": [
          [
            -2,
            5
          ],
          [
            -1,
            6
          ]
        ],
        "expected": [
          -2,
          -1,
          5,
          6,
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
  "7078": {
    "functionNames": [
      "binary_search_1"
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
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "7079": {
    "functionNames": [
      "binary_search_2"
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
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "7080": {
    "functionNames": [
      "binary_search_3"
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
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "7081": {
    "functionNames": [
      "binary_search_4"
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
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "7082": {
    "functionNames": [
      "binary_search_5"
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
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "7083": {
    "functionNames": [
      "selection_sort_1"
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
            -1,
            4,
            0
          ]
        ],
        "expected": [
          -1,
          0,
          4,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7084": {
    "functionNames": [
      "selection_sort_2"
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
            -1,
            4,
            0
          ]
        ],
        "expected": [
          -1,
          0,
          4,
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7085": {
    "functionNames": [
      "selection_sort_3"
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
            -1,
            4,
            0
          ]
        ],
        "expected": [
          -1,
          0,
          4,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7086": {
    "functionNames": [
      "selection_sort_4"
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
            -1,
            4,
            0
          ]
        ],
        "expected": [
          -1,
          0,
          4,
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7087": {
    "functionNames": [
      "selection_sort_5"
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
            -1,
            4,
            0
          ]
        ],
        "expected": [
          -1,
          0,
          4,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7088": {
    "functionNames": [
      "bubble_sort_1"
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
            5,
            -1,
            5
          ]
        ],
        "expected": [
          -1,
          5,
          5,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7089": {
    "functionNames": [
      "bubble_sort_2"
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
            5,
            -1,
            5
          ]
        ],
        "expected": [
          -1,
          5,
          5,
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7090": {
    "functionNames": [
      "bubble_sort_3"
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
            5,
            -1,
            5
          ]
        ],
        "expected": [
          -1,
          5,
          5,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7091": {
    "functionNames": [
      "bubble_sort_4"
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
            5,
            -1,
            5
          ]
        ],
        "expected": [
          -1,
          5,
          5,
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7092": {
    "functionNames": [
      "bubble_sort_5"
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
            5,
            -1,
            5
          ]
        ],
        "expected": [
          -1,
          5,
          5,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 2
      }
    ]
  },
  "7093": {
    "functionNames": [
      "has_pair_sum_1"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            7,
            11
          ],
          4
        ],
        "expected": false
      },
      {
        "args": [
          [
            1,
            2
          ],
          10
        ],
        "expected": false
      },
      {
        "args": [
          [
            1,
            1
          ],
          1
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7094": {
    "functionNames": [
      "has_pair_sum_2"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            7,
            11
          ],
          4
        ],
        "expected": false
      },
      {
        "args": [
          [
            1,
            2
          ],
          10
        ],
        "expected": false
      },
      {
        "args": [
          [
            2,
            2
          ],
          2
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7095": {
    "functionNames": [
      "has_pair_sum_3"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            7,
            11
          ],
          4
        ],
        "expected": false
      },
      {
        "args": [
          [
            1,
            2
          ],
          10
        ],
        "expected": false
      },
      {
        "args": [
          [
            3,
            3
          ],
          3
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7096": {
    "functionNames": [
      "has_pair_sum_4"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            7,
            11
          ],
          4
        ],
        "expected": false
      },
      {
        "args": [
          [
            1,
            2
          ],
          10
        ],
        "expected": false
      },
      {
        "args": [
          [
            4,
            4
          ],
          4
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7097": {
    "functionNames": [
      "has_pair_sum_5"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            7,
            11
          ],
          4
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            2
          ],
          10
        ],
        "expected": false
      },
      {
        "args": [
          [
            5,
            5
          ],
          5
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7098": {
    "functionNames": [
      "most_frequent_smallest_1"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2,
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
      },
      {
        "args": [
          [
            3,
            3,
            2
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7099": {
    "functionNames": [
      "most_frequent_smallest_2"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2,
            1
          ]
        ],
        "expected": 1
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
            3,
            3,
            2
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7100": {
    "functionNames": [
      "most_frequent_smallest_3"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2,
            1
          ]
        ],
        "expected": 1
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
            3,
            3,
            2
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7101": {
    "functionNames": [
      "most_frequent_smallest_4"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2,
            1
          ]
        ],
        "expected": 1
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
            3,
            3,
            2
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7102": {
    "functionNames": [
      "most_frequent_smallest_5"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1,
            2,
            1
          ]
        ],
        "expected": 1
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
            3,
            3,
            2
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "7103": {
    "functionNames": [
      "rotate_left_1"
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
          2,
          3,
          4,
          5,
          6,
          1
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
    ]
  },
  "7104": {
    "functionNames": [
      "rotate_left_2"
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
          4,
          5,
          6,
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
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ]
  },
  "7105": {
    "functionNames": [
      "rotate_left_3"
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
          4,
          5,
          6,
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
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ]
  },
  "7106": {
    "functionNames": [
      "rotate_left_4"
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
          5,
          6,
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
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ]
  },
  "7107": {
    "functionNames": [
      "rotate_left_5"
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
    ]
  }
};
