import type { Exercise } from './types';

export const EASY_CONCEPT_PRACTICE_EXERCISES: Exercise[] = [
  {
    "id": 5708,
    "title": "Problem 5708",
    "description": "Write a Python function called `count_step_1_while` that must count positive multiples of 2 that do not exceed `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_step_1_while(10) -> 5\n  count_step_1_while(0) -> 0",
    "initialCode": "def count_step_1_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_step_1_while(limit):\n    value = 2\n    count = 0\n    while value <= limit:\n        count += 1\n        value += 2\n    return count\n\nprint(count_step_1_while(10))  # Expected: 5\nprint(count_step_1_while(0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5708(limit):\n    def calculate():\n        value = 2\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 2\n        return count\n    return calculate()\n\nprint(solve_problem_5708(10))\n\n# Example 3: static method approach\nclass Problem5708Solution:\n    @staticmethod\n    def count_step_1_while(limit):\n        value = 2\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 2\n        return count\n\nprint(Problem5708Solution.count_step_1_while(0))\n\n# Example 4: assigned result approach\nresult = count_step_1_while(10)\nprint(result)\n\n# Example 5: direct call\nprint(count_step_1_while(17))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5709,
    "title": "Problem 5709",
    "description": "Write a Python function called `count_step_2_while` that must count positive multiples of 3 that do not exceed `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_step_2_while(10) -> 3\n  count_step_2_while(0) -> 0",
    "initialCode": "def count_step_2_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_step_2_while(limit):\n    value = 3\n    count = 0\n    while value <= limit:\n        count += 1\n        value += 3\n    return count\n\nprint(count_step_2_while(10))  # Expected: 3\nprint(count_step_2_while(0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5709(limit):\n    def calculate():\n        value = 3\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 3\n        return count\n    return calculate()\n\nprint(solve_problem_5709(10))\n\n# Example 3: static method approach\nclass Problem5709Solution:\n    @staticmethod\n    def count_step_2_while(limit):\n        value = 3\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 3\n        return count\n\nprint(Problem5709Solution.count_step_2_while(0))\n\n# Example 4: assigned result approach\nresult = count_step_2_while(10)\nprint(result)\n\n# Example 5: direct call\nprint(count_step_2_while(17))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5710,
    "title": "Problem 5710",
    "description": "Write a Python function called `count_step_3_while` that must count positive multiples of 4 that do not exceed `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_step_3_while(10) -> 2\n  count_step_3_while(0) -> 0",
    "initialCode": "def count_step_3_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_step_3_while(limit):\n    value = 4\n    count = 0\n    while value <= limit:\n        count += 1\n        value += 4\n    return count\n\nprint(count_step_3_while(10))  # Expected: 2\nprint(count_step_3_while(0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5710(limit):\n    def calculate():\n        value = 4\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 4\n        return count\n    return calculate()\n\nprint(solve_problem_5710(10))\n\n# Example 3: static method approach\nclass Problem5710Solution:\n    @staticmethod\n    def count_step_3_while(limit):\n        value = 4\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 4\n        return count\n\nprint(Problem5710Solution.count_step_3_while(0))\n\n# Example 4: assigned result approach\nresult = count_step_3_while(10)\nprint(result)\n\n# Example 5: direct call\nprint(count_step_3_while(17))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5711,
    "title": "Problem 5711",
    "description": "Write a Python function called `count_step_4_while` that must count positive multiples of 5 that do not exceed `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_step_4_while(10) -> 2\n  count_step_4_while(0) -> 0",
    "initialCode": "def count_step_4_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_step_4_while(limit):\n    value = 5\n    count = 0\n    while value <= limit:\n        count += 1\n        value += 5\n    return count\n\nprint(count_step_4_while(10))  # Expected: 2\nprint(count_step_4_while(0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5711(limit):\n    def calculate():\n        value = 5\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 5\n        return count\n    return calculate()\n\nprint(solve_problem_5711(10))\n\n# Example 3: static method approach\nclass Problem5711Solution:\n    @staticmethod\n    def count_step_4_while(limit):\n        value = 5\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 5\n        return count\n\nprint(Problem5711Solution.count_step_4_while(0))\n\n# Example 4: assigned result approach\nresult = count_step_4_while(10)\nprint(result)\n\n# Example 5: direct call\nprint(count_step_4_while(17))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5712,
    "title": "Problem 5712",
    "description": "Write a Python function called `count_step_5_while` that must count positive multiples of 6 that do not exceed `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_step_5_while(10) -> 1\n  count_step_5_while(0) -> 0",
    "initialCode": "def count_step_5_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_step_5_while(limit):\n    value = 6\n    count = 0\n    while value <= limit:\n        count += 1\n        value += 6\n    return count\n\nprint(count_step_5_while(10))  # Expected: 1\nprint(count_step_5_while(0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5712(limit):\n    def calculate():\n        value = 6\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 6\n        return count\n    return calculate()\n\nprint(solve_problem_5712(10))\n\n# Example 3: static method approach\nclass Problem5712Solution:\n    @staticmethod\n    def count_step_5_while(limit):\n        value = 6\n        count = 0\n        while value <= limit:\n            count += 1\n            value += 6\n        return count\n\nprint(Problem5712Solution.count_step_5_while(0))\n\n# Example 4: assigned result approach\nresult = count_step_5_while(10)\nprint(result)\n\n# Example 5: direct call\nprint(count_step_5_while(17))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5713,
    "title": "Problem 5713",
    "description": "Write a Python function called `sum_step_1_while` that must sum positive multiples of 2 through `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_step_1_while(12) -> 42\n  sum_step_1_while(1) -> 0",
    "initialCode": "def sum_step_1_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_step_1_while(limit):\n    value = 2\n    total = 0\n    while value <= limit:\n        total += value\n        value += 2\n    return total\n\nprint(sum_step_1_while(12))  # Expected: 42\nprint(sum_step_1_while(1))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5713(limit):\n    def calculate():\n        value = 2\n        total = 0\n        while value <= limit:\n            total += value\n            value += 2\n        return total\n    return calculate()\n\nprint(solve_problem_5713(12))\n\n# Example 3: static method approach\nclass Problem5713Solution:\n    @staticmethod\n    def sum_step_1_while(limit):\n        value = 2\n        total = 0\n        while value <= limit:\n            total += value\n            value += 2\n        return total\n\nprint(Problem5713Solution.sum_step_1_while(1))\n\n# Example 4: assigned result approach\nresult = sum_step_1_while(12)\nprint(result)\n\n# Example 5: direct call\nprint(sum_step_1_while(25))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5714,
    "title": "Problem 5714",
    "description": "Write a Python function called `sum_step_2_while` that must sum positive multiples of 3 through `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_step_2_while(12) -> 30\n  sum_step_2_while(1) -> 0",
    "initialCode": "def sum_step_2_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_step_2_while(limit):\n    value = 3\n    total = 0\n    while value <= limit:\n        total += value\n        value += 3\n    return total\n\nprint(sum_step_2_while(12))  # Expected: 30\nprint(sum_step_2_while(1))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5714(limit):\n    def calculate():\n        value = 3\n        total = 0\n        while value <= limit:\n            total += value\n            value += 3\n        return total\n    return calculate()\n\nprint(solve_problem_5714(12))\n\n# Example 3: static method approach\nclass Problem5714Solution:\n    @staticmethod\n    def sum_step_2_while(limit):\n        value = 3\n        total = 0\n        while value <= limit:\n            total += value\n            value += 3\n        return total\n\nprint(Problem5714Solution.sum_step_2_while(1))\n\n# Example 4: assigned result approach\nresult = sum_step_2_while(12)\nprint(result)\n\n# Example 5: direct call\nprint(sum_step_2_while(25))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5715,
    "title": "Problem 5715",
    "description": "Write a Python function called `sum_step_3_while` that must sum positive multiples of 4 through `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_step_3_while(12) -> 24\n  sum_step_3_while(1) -> 0",
    "initialCode": "def sum_step_3_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_step_3_while(limit):\n    value = 4\n    total = 0\n    while value <= limit:\n        total += value\n        value += 4\n    return total\n\nprint(sum_step_3_while(12))  # Expected: 24\nprint(sum_step_3_while(1))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5715(limit):\n    def calculate():\n        value = 4\n        total = 0\n        while value <= limit:\n            total += value\n            value += 4\n        return total\n    return calculate()\n\nprint(solve_problem_5715(12))\n\n# Example 3: static method approach\nclass Problem5715Solution:\n    @staticmethod\n    def sum_step_3_while(limit):\n        value = 4\n        total = 0\n        while value <= limit:\n            total += value\n            value += 4\n        return total\n\nprint(Problem5715Solution.sum_step_3_while(1))\n\n# Example 4: assigned result approach\nresult = sum_step_3_while(12)\nprint(result)\n\n# Example 5: direct call\nprint(sum_step_3_while(25))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5716,
    "title": "Problem 5716",
    "description": "Write a Python function called `sum_step_4_while` that must sum positive multiples of 5 through `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_step_4_while(12) -> 15\n  sum_step_4_while(1) -> 0",
    "initialCode": "def sum_step_4_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_step_4_while(limit):\n    value = 5\n    total = 0\n    while value <= limit:\n        total += value\n        value += 5\n    return total\n\nprint(sum_step_4_while(12))  # Expected: 15\nprint(sum_step_4_while(1))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5716(limit):\n    def calculate():\n        value = 5\n        total = 0\n        while value <= limit:\n            total += value\n            value += 5\n        return total\n    return calculate()\n\nprint(solve_problem_5716(12))\n\n# Example 3: static method approach\nclass Problem5716Solution:\n    @staticmethod\n    def sum_step_4_while(limit):\n        value = 5\n        total = 0\n        while value <= limit:\n            total += value\n            value += 5\n        return total\n\nprint(Problem5716Solution.sum_step_4_while(1))\n\n# Example 4: assigned result approach\nresult = sum_step_4_while(12)\nprint(result)\n\n# Example 5: direct call\nprint(sum_step_4_while(25))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5717,
    "title": "Problem 5717",
    "description": "Write a Python function called `sum_step_5_while` that must sum positive multiples of 6 through `limit`. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_step_5_while(12) -> 18\n  sum_step_5_while(1) -> 0",
    "initialCode": "def sum_step_5_while(limit):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_step_5_while(limit):\n    value = 6\n    total = 0\n    while value <= limit:\n        total += value\n        value += 6\n    return total\n\nprint(sum_step_5_while(12))  # Expected: 18\nprint(sum_step_5_while(1))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5717(limit):\n    def calculate():\n        value = 6\n        total = 0\n        while value <= limit:\n            total += value\n            value += 6\n        return total\n    return calculate()\n\nprint(solve_problem_5717(12))\n\n# Example 3: static method approach\nclass Problem5717Solution:\n    @staticmethod\n    def sum_step_5_while(limit):\n        value = 6\n        total = 0\n        while value <= limit:\n            total += value\n            value += 6\n        return total\n\nprint(Problem5717Solution.sum_step_5_while(1))\n\n# Example 4: assigned result approach\nresult = sum_step_5_while(12)\nprint(result)\n\n# Example 5: direct call\nprint(sum_step_5_while(25))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5718,
    "title": "Problem 5718",
    "description": "Write a Python function called `build_sequence_1_while` that must build `count` values beginning at `start` and increasing by 1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  build_sequence_1_while(2, 4) -> [2, 3, 4, 5]\n  build_sequence_1_while(-3, 3) -> [-3, -2, -1]",
    "initialCode": "def build_sequence_1_while(start, count):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef build_sequence_1_while(start, count):\n    result = []\n    while len(result) < count:\n        result.append(start)\n        start += 1\n    return result\n\nprint(build_sequence_1_while(2, 4))  # Expected: [2, 3, 4, 5]\nprint(build_sequence_1_while(-3, 3))  # Expected: [-3, -2, -1]\n\n# Example 2: nested helper approach\ndef solve_problem_5718(start, count):\n    def calculate():\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5718(2, 4))\n\n# Example 3: static method approach\nclass Problem5718Solution:\n    @staticmethod\n    def build_sequence_1_while(start, count):\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 1\n        return result\n\nprint(Problem5718Solution.build_sequence_1_while(-3, 3))\n\n# Example 4: assigned result approach\nresult = build_sequence_1_while(2, 4)\nprint(result)\n\n# Example 5: direct call\nprint(build_sequence_1_while(8, 0))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5719,
    "title": "Problem 5719",
    "description": "Write a Python function called `build_sequence_2_while` that must build `count` values beginning at `start` and increasing by 2. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  build_sequence_2_while(2, 4) -> [2, 4, 6, 8]\n  build_sequence_2_while(-3, 3) -> [-3, -1, 1]",
    "initialCode": "def build_sequence_2_while(start, count):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef build_sequence_2_while(start, count):\n    result = []\n    while len(result) < count:\n        result.append(start)\n        start += 2\n    return result\n\nprint(build_sequence_2_while(2, 4))  # Expected: [2, 4, 6, 8]\nprint(build_sequence_2_while(-3, 3))  # Expected: [-3, -1, 1]\n\n# Example 2: nested helper approach\ndef solve_problem_5719(start, count):\n    def calculate():\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 2\n        return result\n    return calculate()\n\nprint(solve_problem_5719(2, 4))\n\n# Example 3: static method approach\nclass Problem5719Solution:\n    @staticmethod\n    def build_sequence_2_while(start, count):\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 2\n        return result\n\nprint(Problem5719Solution.build_sequence_2_while(-3, 3))\n\n# Example 4: assigned result approach\nresult = build_sequence_2_while(2, 4)\nprint(result)\n\n# Example 5: direct call\nprint(build_sequence_2_while(8, 0))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5720,
    "title": "Problem 5720",
    "description": "Write a Python function called `build_sequence_3_while` that must build `count` values beginning at `start` and increasing by 3. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  build_sequence_3_while(2, 4) -> [2, 5, 8, 11]\n  build_sequence_3_while(-3, 3) -> [-3, 0, 3]",
    "initialCode": "def build_sequence_3_while(start, count):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef build_sequence_3_while(start, count):\n    result = []\n    while len(result) < count:\n        result.append(start)\n        start += 3\n    return result\n\nprint(build_sequence_3_while(2, 4))  # Expected: [2, 5, 8, 11]\nprint(build_sequence_3_while(-3, 3))  # Expected: [-3, 0, 3]\n\n# Example 2: nested helper approach\ndef solve_problem_5720(start, count):\n    def calculate():\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 3\n        return result\n    return calculate()\n\nprint(solve_problem_5720(2, 4))\n\n# Example 3: static method approach\nclass Problem5720Solution:\n    @staticmethod\n    def build_sequence_3_while(start, count):\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 3\n        return result\n\nprint(Problem5720Solution.build_sequence_3_while(-3, 3))\n\n# Example 4: assigned result approach\nresult = build_sequence_3_while(2, 4)\nprint(result)\n\n# Example 5: direct call\nprint(build_sequence_3_while(8, 0))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5721,
    "title": "Problem 5721",
    "description": "Write a Python function called `build_sequence_4_while` that must build `count` values beginning at `start` and increasing by 4. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  build_sequence_4_while(2, 4) -> [2, 6, 10, 14]\n  build_sequence_4_while(-3, 3) -> [-3, 1, 5]",
    "initialCode": "def build_sequence_4_while(start, count):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef build_sequence_4_while(start, count):\n    result = []\n    while len(result) < count:\n        result.append(start)\n        start += 4\n    return result\n\nprint(build_sequence_4_while(2, 4))  # Expected: [2, 6, 10, 14]\nprint(build_sequence_4_while(-3, 3))  # Expected: [-3, 1, 5]\n\n# Example 2: nested helper approach\ndef solve_problem_5721(start, count):\n    def calculate():\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 4\n        return result\n    return calculate()\n\nprint(solve_problem_5721(2, 4))\n\n# Example 3: static method approach\nclass Problem5721Solution:\n    @staticmethod\n    def build_sequence_4_while(start, count):\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 4\n        return result\n\nprint(Problem5721Solution.build_sequence_4_while(-3, 3))\n\n# Example 4: assigned result approach\nresult = build_sequence_4_while(2, 4)\nprint(result)\n\n# Example 5: direct call\nprint(build_sequence_4_while(8, 0))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5722,
    "title": "Problem 5722",
    "description": "Write a Python function called `build_sequence_5_while` that must build `count` values beginning at `start` and increasing by 5. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  build_sequence_5_while(2, 4) -> [2, 7, 12, 17]\n  build_sequence_5_while(-3, 3) -> [-3, 2, 7]",
    "initialCode": "def build_sequence_5_while(start, count):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef build_sequence_5_while(start, count):\n    result = []\n    while len(result) < count:\n        result.append(start)\n        start += 5\n    return result\n\nprint(build_sequence_5_while(2, 4))  # Expected: [2, 7, 12, 17]\nprint(build_sequence_5_while(-3, 3))  # Expected: [-3, 2, 7]\n\n# Example 2: nested helper approach\ndef solve_problem_5722(start, count):\n    def calculate():\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 5\n        return result\n    return calculate()\n\nprint(solve_problem_5722(2, 4))\n\n# Example 3: static method approach\nclass Problem5722Solution:\n    @staticmethod\n    def build_sequence_5_while(start, count):\n        result = []\n        while len(result) < count:\n            result.append(start)\n            start += 5\n        return result\n\nprint(Problem5722Solution.build_sequence_5_while(-3, 3))\n\n# Example 4: assigned result approach\nresult = build_sequence_5_while(2, 4)\nprint(result)\n\n# Example 5: direct call\nprint(build_sequence_5_while(8, 0))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5723,
    "title": "Problem 5723",
    "description": "Write a Python function called `repeat_text_1_while` that must repeat `text` exactly 1 times without using string multiplication. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  repeat_text_1_while(\"ab\") -> \"ab\"\n  repeat_text_1_while(\"x\") -> \"x\"",
    "initialCode": "def repeat_text_1_while(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef repeat_text_1_while(text):\n    result = \"\"\n    count = 0\n    while count < 1:\n        result += text\n        count += 1\n    return result\n\nprint(repeat_text_1_while(\"ab\"))  # Expected: \"ab\"\nprint(repeat_text_1_while(\"x\"))  # Expected: \"x\"\n\n# Example 2: nested helper approach\ndef solve_problem_5723(text):\n    def calculate():\n        result = \"\"\n        count = 0\n        while count < 1:\n            result += text\n            count += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5723(\"ab\"))\n\n# Example 3: static method approach\nclass Problem5723Solution:\n    @staticmethod\n    def repeat_text_1_while(text):\n        result = \"\"\n        count = 0\n        while count < 1:\n            result += text\n            count += 1\n        return result\n\nprint(Problem5723Solution.repeat_text_1_while(\"x\"))\n\n# Example 4: assigned result approach\nresult = repeat_text_1_while(\"ab\")\nprint(result)\n\n# Example 5: direct call\nprint(repeat_text_1_while(\"\"))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5724,
    "title": "Problem 5724",
    "description": "Write a Python function called `repeat_text_2_while` that must repeat `text` exactly 2 times without using string multiplication. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  repeat_text_2_while(\"ab\") -> \"abab\"\n  repeat_text_2_while(\"x\") -> \"xx\"",
    "initialCode": "def repeat_text_2_while(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef repeat_text_2_while(text):\n    result = \"\"\n    count = 0\n    while count < 2:\n        result += text\n        count += 1\n    return result\n\nprint(repeat_text_2_while(\"ab\"))  # Expected: \"abab\"\nprint(repeat_text_2_while(\"x\"))  # Expected: \"xx\"\n\n# Example 2: nested helper approach\ndef solve_problem_5724(text):\n    def calculate():\n        result = \"\"\n        count = 0\n        while count < 2:\n            result += text\n            count += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5724(\"ab\"))\n\n# Example 3: static method approach\nclass Problem5724Solution:\n    @staticmethod\n    def repeat_text_2_while(text):\n        result = \"\"\n        count = 0\n        while count < 2:\n            result += text\n            count += 1\n        return result\n\nprint(Problem5724Solution.repeat_text_2_while(\"x\"))\n\n# Example 4: assigned result approach\nresult = repeat_text_2_while(\"ab\")\nprint(result)\n\n# Example 5: direct call\nprint(repeat_text_2_while(\"\"))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5725,
    "title": "Problem 5725",
    "description": "Write a Python function called `repeat_text_3_while` that must repeat `text` exactly 3 times without using string multiplication. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  repeat_text_3_while(\"ab\") -> \"ababab\"\n  repeat_text_3_while(\"x\") -> \"xxx\"",
    "initialCode": "def repeat_text_3_while(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef repeat_text_3_while(text):\n    result = \"\"\n    count = 0\n    while count < 3:\n        result += text\n        count += 1\n    return result\n\nprint(repeat_text_3_while(\"ab\"))  # Expected: \"ababab\"\nprint(repeat_text_3_while(\"x\"))  # Expected: \"xxx\"\n\n# Example 2: nested helper approach\ndef solve_problem_5725(text):\n    def calculate():\n        result = \"\"\n        count = 0\n        while count < 3:\n            result += text\n            count += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5725(\"ab\"))\n\n# Example 3: static method approach\nclass Problem5725Solution:\n    @staticmethod\n    def repeat_text_3_while(text):\n        result = \"\"\n        count = 0\n        while count < 3:\n            result += text\n            count += 1\n        return result\n\nprint(Problem5725Solution.repeat_text_3_while(\"x\"))\n\n# Example 4: assigned result approach\nresult = repeat_text_3_while(\"ab\")\nprint(result)\n\n# Example 5: direct call\nprint(repeat_text_3_while(\"\"))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5726,
    "title": "Problem 5726",
    "description": "Write a Python function called `repeat_text_4_while` that must repeat `text` exactly 4 times without using string multiplication. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  repeat_text_4_while(\"ab\") -> \"abababab\"\n  repeat_text_4_while(\"x\") -> \"xxxx\"",
    "initialCode": "def repeat_text_4_while(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef repeat_text_4_while(text):\n    result = \"\"\n    count = 0\n    while count < 4:\n        result += text\n        count += 1\n    return result\n\nprint(repeat_text_4_while(\"ab\"))  # Expected: \"abababab\"\nprint(repeat_text_4_while(\"x\"))  # Expected: \"xxxx\"\n\n# Example 2: nested helper approach\ndef solve_problem_5726(text):\n    def calculate():\n        result = \"\"\n        count = 0\n        while count < 4:\n            result += text\n            count += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5726(\"ab\"))\n\n# Example 3: static method approach\nclass Problem5726Solution:\n    @staticmethod\n    def repeat_text_4_while(text):\n        result = \"\"\n        count = 0\n        while count < 4:\n            result += text\n            count += 1\n        return result\n\nprint(Problem5726Solution.repeat_text_4_while(\"x\"))\n\n# Example 4: assigned result approach\nresult = repeat_text_4_while(\"ab\")\nprint(result)\n\n# Example 5: direct call\nprint(repeat_text_4_while(\"\"))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5727,
    "title": "Problem 5727",
    "description": "Write a Python function called `repeat_text_5_while` that must repeat `text` exactly 5 times without using string multiplication. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  repeat_text_5_while(\"ab\") -> \"ababababab\"\n  repeat_text_5_while(\"x\") -> \"xxxxx\"",
    "initialCode": "def repeat_text_5_while(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef repeat_text_5_while(text):\n    result = \"\"\n    count = 0\n    while count < 5:\n        result += text\n        count += 1\n    return result\n\nprint(repeat_text_5_while(\"ab\"))  # Expected: \"ababababab\"\nprint(repeat_text_5_while(\"x\"))  # Expected: \"xxxxx\"\n\n# Example 2: nested helper approach\ndef solve_problem_5727(text):\n    def calculate():\n        result = \"\"\n        count = 0\n        while count < 5:\n            result += text\n            count += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5727(\"ab\"))\n\n# Example 3: static method approach\nclass Problem5727Solution:\n    @staticmethod\n    def repeat_text_5_while(text):\n        result = \"\"\n        count = 0\n        while count < 5:\n            result += text\n            count += 1\n        return result\n\nprint(Problem5727Solution.repeat_text_5_while(\"x\"))\n\n# Example 4: assigned result approach\nresult = repeat_text_5_while(\"ab\")\nprint(result)\n\n# Example 5: direct call\nprint(repeat_text_5_while(\"\"))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5728,
    "title": "Problem 5728",
    "description": "Write a Python function called `count_above_1_while` that must count list values greater than 1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_above_1_while([0, 2, 5, 9]) -> 3\n  count_above_1_while([1, 2]) -> 1",
    "initialCode": "def count_above_1_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_above_1_while(values):\n    index = 0\n    count = 0\n    while index < len(values):\n        if values[index] > 1:\n            count += 1\n        index += 1\n    return count\n\nprint(count_above_1_while([0, 2, 5, 9]))  # Expected: 3\nprint(count_above_1_while([1, 2]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5728(values):\n    def calculate():\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 1:\n                count += 1\n            index += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5728([0, 2, 5, 9]))\n\n# Example 3: static method approach\nclass Problem5728Solution:\n    @staticmethod\n    def count_above_1_while(values):\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 1:\n                count += 1\n            index += 1\n        return count\n\nprint(Problem5728Solution.count_above_1_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = count_above_1_while([0, 2, 5, 9])\nprint(result)\n\n# Example 5: direct call\nprint(count_above_1_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5729,
    "title": "Problem 5729",
    "description": "Write a Python function called `count_above_2_while` that must count list values greater than 2. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_above_2_while([0, 2, 5, 9]) -> 2\n  count_above_2_while([2, 3]) -> 1",
    "initialCode": "def count_above_2_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_above_2_while(values):\n    index = 0\n    count = 0\n    while index < len(values):\n        if values[index] > 2:\n            count += 1\n        index += 1\n    return count\n\nprint(count_above_2_while([0, 2, 5, 9]))  # Expected: 2\nprint(count_above_2_while([2, 3]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5729(values):\n    def calculate():\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 2:\n                count += 1\n            index += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5729([0, 2, 5, 9]))\n\n# Example 3: static method approach\nclass Problem5729Solution:\n    @staticmethod\n    def count_above_2_while(values):\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 2:\n                count += 1\n            index += 1\n        return count\n\nprint(Problem5729Solution.count_above_2_while([2, 3]))\n\n# Example 4: assigned result approach\nresult = count_above_2_while([0, 2, 5, 9])\nprint(result)\n\n# Example 5: direct call\nprint(count_above_2_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5730,
    "title": "Problem 5730",
    "description": "Write a Python function called `count_above_3_while` that must count list values greater than 3. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_above_3_while([0, 2, 5, 9]) -> 2\n  count_above_3_while([3, 4]) -> 1",
    "initialCode": "def count_above_3_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_above_3_while(values):\n    index = 0\n    count = 0\n    while index < len(values):\n        if values[index] > 3:\n            count += 1\n        index += 1\n    return count\n\nprint(count_above_3_while([0, 2, 5, 9]))  # Expected: 2\nprint(count_above_3_while([3, 4]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5730(values):\n    def calculate():\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 3:\n                count += 1\n            index += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5730([0, 2, 5, 9]))\n\n# Example 3: static method approach\nclass Problem5730Solution:\n    @staticmethod\n    def count_above_3_while(values):\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 3:\n                count += 1\n            index += 1\n        return count\n\nprint(Problem5730Solution.count_above_3_while([3, 4]))\n\n# Example 4: assigned result approach\nresult = count_above_3_while([0, 2, 5, 9])\nprint(result)\n\n# Example 5: direct call\nprint(count_above_3_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5731,
    "title": "Problem 5731",
    "description": "Write a Python function called `count_above_4_while` that must count list values greater than 4. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_above_4_while([0, 2, 5, 9]) -> 2\n  count_above_4_while([4, 5]) -> 1",
    "initialCode": "def count_above_4_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_above_4_while(values):\n    index = 0\n    count = 0\n    while index < len(values):\n        if values[index] > 4:\n            count += 1\n        index += 1\n    return count\n\nprint(count_above_4_while([0, 2, 5, 9]))  # Expected: 2\nprint(count_above_4_while([4, 5]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5731(values):\n    def calculate():\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 4:\n                count += 1\n            index += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5731([0, 2, 5, 9]))\n\n# Example 3: static method approach\nclass Problem5731Solution:\n    @staticmethod\n    def count_above_4_while(values):\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 4:\n                count += 1\n            index += 1\n        return count\n\nprint(Problem5731Solution.count_above_4_while([4, 5]))\n\n# Example 4: assigned result approach\nresult = count_above_4_while([0, 2, 5, 9])\nprint(result)\n\n# Example 5: direct call\nprint(count_above_4_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5732,
    "title": "Problem 5732",
    "description": "Write a Python function called `count_above_5_while` that must count list values greater than 5. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  count_above_5_while([0, 2, 5, 9]) -> 1\n  count_above_5_while([5, 6]) -> 1",
    "initialCode": "def count_above_5_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_above_5_while(values):\n    index = 0\n    count = 0\n    while index < len(values):\n        if values[index] > 5:\n            count += 1\n        index += 1\n    return count\n\nprint(count_above_5_while([0, 2, 5, 9]))  # Expected: 1\nprint(count_above_5_while([5, 6]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5732(values):\n    def calculate():\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 5:\n                count += 1\n            index += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5732([0, 2, 5, 9]))\n\n# Example 3: static method approach\nclass Problem5732Solution:\n    @staticmethod\n    def count_above_5_while(values):\n        index = 0\n        count = 0\n        while index < len(values):\n            if values[index] > 5:\n                count += 1\n            index += 1\n        return count\n\nprint(Problem5732Solution.count_above_5_while([5, 6]))\n\n# Example 4: assigned result approach\nresult = count_above_5_while([0, 2, 5, 9])\nprint(result)\n\n# Example 5: direct call\nprint(count_above_5_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5733,
    "title": "Problem 5733",
    "description": "Write a Python function called `first_below_1_while` that must return the first index containing a value below 1, or -1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  first_below_1_while([9, 0, 8]) -> 1\n  first_below_1_while([1, 2]) -> -1",
    "initialCode": "def first_below_1_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_below_1_while(values):\n    index = 0\n    while index < len(values):\n        if values[index] < 1:\n            return index\n        index += 1\n    return -1\n\nprint(first_below_1_while([9, 0, 8]))  # Expected: 1\nprint(first_below_1_while([1, 2]))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5733(values):\n    def calculate():\n        index = 0\n        while index < len(values):\n            if values[index] < 1:\n                return index\n            index += 1\n        return -1\n    return calculate()\n\nprint(solve_problem_5733([9, 0, 8]))\n\n# Example 3: static method approach\nclass Problem5733Solution:\n    @staticmethod\n    def first_below_1_while(values):\n        index = 0\n        while index < len(values):\n            if values[index] < 1:\n                return index\n            index += 1\n        return -1\n\nprint(Problem5733Solution.first_below_1_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = first_below_1_while([9, 0, 8])\nprint(result)\n\n# Example 5: direct call\nprint(first_below_1_while([-1]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5734,
    "title": "Problem 5734",
    "description": "Write a Python function called `first_below_2_while` that must return the first index containing a value below 2, or -1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  first_below_2_while([9, 1, 8]) -> 1\n  first_below_2_while([2, 3]) -> -1",
    "initialCode": "def first_below_2_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_below_2_while(values):\n    index = 0\n    while index < len(values):\n        if values[index] < 2:\n            return index\n        index += 1\n    return -1\n\nprint(first_below_2_while([9, 1, 8]))  # Expected: 1\nprint(first_below_2_while([2, 3]))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5734(values):\n    def calculate():\n        index = 0\n        while index < len(values):\n            if values[index] < 2:\n                return index\n            index += 1\n        return -1\n    return calculate()\n\nprint(solve_problem_5734([9, 1, 8]))\n\n# Example 3: static method approach\nclass Problem5734Solution:\n    @staticmethod\n    def first_below_2_while(values):\n        index = 0\n        while index < len(values):\n            if values[index] < 2:\n                return index\n            index += 1\n        return -1\n\nprint(Problem5734Solution.first_below_2_while([2, 3]))\n\n# Example 4: assigned result approach\nresult = first_below_2_while([9, 1, 8])\nprint(result)\n\n# Example 5: direct call\nprint(first_below_2_while([0]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5735,
    "title": "Problem 5735",
    "description": "Write a Python function called `first_below_3_while` that must return the first index containing a value below 3, or -1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  first_below_3_while([9, 2, 8]) -> 1\n  first_below_3_while([3, 4]) -> -1",
    "initialCode": "def first_below_3_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_below_3_while(values):\n    index = 0\n    while index < len(values):\n        if values[index] < 3:\n            return index\n        index += 1\n    return -1\n\nprint(first_below_3_while([9, 2, 8]))  # Expected: 1\nprint(first_below_3_while([3, 4]))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5735(values):\n    def calculate():\n        index = 0\n        while index < len(values):\n            if values[index] < 3:\n                return index\n            index += 1\n        return -1\n    return calculate()\n\nprint(solve_problem_5735([9, 2, 8]))\n\n# Example 3: static method approach\nclass Problem5735Solution:\n    @staticmethod\n    def first_below_3_while(values):\n        index = 0\n        while index < len(values):\n            if values[index] < 3:\n                return index\n            index += 1\n        return -1\n\nprint(Problem5735Solution.first_below_3_while([3, 4]))\n\n# Example 4: assigned result approach\nresult = first_below_3_while([9, 2, 8])\nprint(result)\n\n# Example 5: direct call\nprint(first_below_3_while([1]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5736,
    "title": "Problem 5736",
    "description": "Write a Python function called `first_below_4_while` that must return the first index containing a value below 4, or -1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  first_below_4_while([9, 3, 8]) -> 1\n  first_below_4_while([4, 5]) -> -1",
    "initialCode": "def first_below_4_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_below_4_while(values):\n    index = 0\n    while index < len(values):\n        if values[index] < 4:\n            return index\n        index += 1\n    return -1\n\nprint(first_below_4_while([9, 3, 8]))  # Expected: 1\nprint(first_below_4_while([4, 5]))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5736(values):\n    def calculate():\n        index = 0\n        while index < len(values):\n            if values[index] < 4:\n                return index\n            index += 1\n        return -1\n    return calculate()\n\nprint(solve_problem_5736([9, 3, 8]))\n\n# Example 3: static method approach\nclass Problem5736Solution:\n    @staticmethod\n    def first_below_4_while(values):\n        index = 0\n        while index < len(values):\n            if values[index] < 4:\n                return index\n            index += 1\n        return -1\n\nprint(Problem5736Solution.first_below_4_while([4, 5]))\n\n# Example 4: assigned result approach\nresult = first_below_4_while([9, 3, 8])\nprint(result)\n\n# Example 5: direct call\nprint(first_below_4_while([2]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5737,
    "title": "Problem 5737",
    "description": "Write a Python function called `first_below_5_while` that must return the first index containing a value below 5, or -1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  first_below_5_while([9, 4, 8]) -> 1\n  first_below_5_while([5, 6]) -> -1",
    "initialCode": "def first_below_5_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_below_5_while(values):\n    index = 0\n    while index < len(values):\n        if values[index] < 5:\n            return index\n        index += 1\n    return -1\n\nprint(first_below_5_while([9, 4, 8]))  # Expected: 1\nprint(first_below_5_while([5, 6]))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5737(values):\n    def calculate():\n        index = 0\n        while index < len(values):\n            if values[index] < 5:\n                return index\n            index += 1\n        return -1\n    return calculate()\n\nprint(solve_problem_5737([9, 4, 8]))\n\n# Example 3: static method approach\nclass Problem5737Solution:\n    @staticmethod\n    def first_below_5_while(values):\n        index = 0\n        while index < len(values):\n            if values[index] < 5:\n                return index\n            index += 1\n        return -1\n\nprint(Problem5737Solution.first_below_5_while([5, 6]))\n\n# Example 4: assigned result approach\nresult = first_below_5_while([9, 4, 8])\nprint(result)\n\n# Example 5: direct call\nprint(first_below_5_while([3]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5738,
    "title": "Problem 5738",
    "description": "Write a Python function called `reach_target_1_while` that must add 1 until `start` reaches or passes `target`, then return the result. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  reach_target_1_while(0, 11) -> 11\n  reach_target_1_while(5, 5) -> 5",
    "initialCode": "def reach_target_1_while(start, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef reach_target_1_while(start, target):\n    while start < target:\n        start += 1\n    return start\n\nprint(reach_target_1_while(0, 11))  # Expected: 11\nprint(reach_target_1_while(5, 5))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5738(start, target):\n    def calculate():\n        while start < target:\n            start += 1\n        return start\n    return calculate()\n\nprint(solve_problem_5738(0, 11))\n\n# Example 3: static method approach\nclass Problem5738Solution:\n    @staticmethod\n    def reach_target_1_while(start, target):\n        while start < target:\n            start += 1\n        return start\n\nprint(Problem5738Solution.reach_target_1_while(5, 5))\n\n# Example 4: assigned result approach\nresult = reach_target_1_while(0, 11)\nprint(result)\n\n# Example 5: direct call\nprint(reach_target_1_while(-2, 7))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5739,
    "title": "Problem 5739",
    "description": "Write a Python function called `reach_target_2_while` that must add 2 until `start` reaches or passes `target`, then return the result. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  reach_target_2_while(0, 11) -> 12\n  reach_target_2_while(5, 5) -> 5",
    "initialCode": "def reach_target_2_while(start, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef reach_target_2_while(start, target):\n    while start < target:\n        start += 2\n    return start\n\nprint(reach_target_2_while(0, 11))  # Expected: 12\nprint(reach_target_2_while(5, 5))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5739(start, target):\n    def calculate():\n        while start < target:\n            start += 2\n        return start\n    return calculate()\n\nprint(solve_problem_5739(0, 11))\n\n# Example 3: static method approach\nclass Problem5739Solution:\n    @staticmethod\n    def reach_target_2_while(start, target):\n        while start < target:\n            start += 2\n        return start\n\nprint(Problem5739Solution.reach_target_2_while(5, 5))\n\n# Example 4: assigned result approach\nresult = reach_target_2_while(0, 11)\nprint(result)\n\n# Example 5: direct call\nprint(reach_target_2_while(-2, 7))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5740,
    "title": "Problem 5740",
    "description": "Write a Python function called `reach_target_3_while` that must add 3 until `start` reaches or passes `target`, then return the result. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  reach_target_3_while(0, 11) -> 12\n  reach_target_3_while(5, 5) -> 5",
    "initialCode": "def reach_target_3_while(start, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef reach_target_3_while(start, target):\n    while start < target:\n        start += 3\n    return start\n\nprint(reach_target_3_while(0, 11))  # Expected: 12\nprint(reach_target_3_while(5, 5))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5740(start, target):\n    def calculate():\n        while start < target:\n            start += 3\n        return start\n    return calculate()\n\nprint(solve_problem_5740(0, 11))\n\n# Example 3: static method approach\nclass Problem5740Solution:\n    @staticmethod\n    def reach_target_3_while(start, target):\n        while start < target:\n            start += 3\n        return start\n\nprint(Problem5740Solution.reach_target_3_while(5, 5))\n\n# Example 4: assigned result approach\nresult = reach_target_3_while(0, 11)\nprint(result)\n\n# Example 5: direct call\nprint(reach_target_3_while(-2, 7))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5741,
    "title": "Problem 5741",
    "description": "Write a Python function called `reach_target_4_while` that must add 4 until `start` reaches or passes `target`, then return the result. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  reach_target_4_while(0, 11) -> 12\n  reach_target_4_while(5, 5) -> 5",
    "initialCode": "def reach_target_4_while(start, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef reach_target_4_while(start, target):\n    while start < target:\n        start += 4\n    return start\n\nprint(reach_target_4_while(0, 11))  # Expected: 12\nprint(reach_target_4_while(5, 5))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5741(start, target):\n    def calculate():\n        while start < target:\n            start += 4\n        return start\n    return calculate()\n\nprint(solve_problem_5741(0, 11))\n\n# Example 3: static method approach\nclass Problem5741Solution:\n    @staticmethod\n    def reach_target_4_while(start, target):\n        while start < target:\n            start += 4\n        return start\n\nprint(Problem5741Solution.reach_target_4_while(5, 5))\n\n# Example 4: assigned result approach\nresult = reach_target_4_while(0, 11)\nprint(result)\n\n# Example 5: direct call\nprint(reach_target_4_while(-2, 7))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5742,
    "title": "Problem 5742",
    "description": "Write a Python function called `reach_target_5_while` that must add 5 until `start` reaches or passes `target`, then return the result. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  reach_target_5_while(0, 11) -> 15\n  reach_target_5_while(5, 5) -> 5",
    "initialCode": "def reach_target_5_while(start, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef reach_target_5_while(start, target):\n    while start < target:\n        start += 5\n    return start\n\nprint(reach_target_5_while(0, 11))  # Expected: 15\nprint(reach_target_5_while(5, 5))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5742(start, target):\n    def calculate():\n        while start < target:\n            start += 5\n        return start\n    return calculate()\n\nprint(solve_problem_5742(0, 11))\n\n# Example 3: static method approach\nclass Problem5742Solution:\n    @staticmethod\n    def reach_target_5_while(start, target):\n        while start < target:\n            start += 5\n        return start\n\nprint(Problem5742Solution.reach_target_5_while(5, 5))\n\n# Example 4: assigned result approach\nresult = reach_target_5_while(0, 11)\nprint(result)\n\n# Example 5: direct call\nprint(reach_target_5_while(-2, 7))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5743,
    "title": "Problem 5743",
    "description": "Write a Python function called `take_prefix_1_while` that must return at most the first 1 list items. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  take_prefix_1_while([1, 2, 3, 4, 5, 6]) -> [1]\n  take_prefix_1_while([\"a\"]) -> [\"a\"]",
    "initialCode": "def take_prefix_1_while(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_prefix_1_while(items):\n    index = 0\n    result = []\n    while index < len(items) and index < 1:\n        result.append(items[index])\n        index += 1\n    return result\n\nprint(take_prefix_1_while([1, 2, 3, 4, 5, 6]))  # Expected: [1]\nprint(take_prefix_1_while([\"a\"]))  # Expected: [\"a\"]\n\n# Example 2: nested helper approach\ndef solve_problem_5743(items):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(items) and index < 1:\n            result.append(items[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5743([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem5743Solution:\n    @staticmethod\n    def take_prefix_1_while(items):\n        index = 0\n        result = []\n        while index < len(items) and index < 1:\n            result.append(items[index])\n            index += 1\n        return result\n\nprint(Problem5743Solution.take_prefix_1_while([\"a\"]))\n\n# Example 4: assigned result approach\nresult = take_prefix_1_while([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_prefix_1_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5744,
    "title": "Problem 5744",
    "description": "Write a Python function called `take_prefix_2_while` that must return at most the first 2 list items. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  take_prefix_2_while([1, 2, 3, 4, 5, 6]) -> [1, 2]\n  take_prefix_2_while([\"a\"]) -> [\"a\"]",
    "initialCode": "def take_prefix_2_while(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_prefix_2_while(items):\n    index = 0\n    result = []\n    while index < len(items) and index < 2:\n        result.append(items[index])\n        index += 1\n    return result\n\nprint(take_prefix_2_while([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2]\nprint(take_prefix_2_while([\"a\"]))  # Expected: [\"a\"]\n\n# Example 2: nested helper approach\ndef solve_problem_5744(items):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(items) and index < 2:\n            result.append(items[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5744([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem5744Solution:\n    @staticmethod\n    def take_prefix_2_while(items):\n        index = 0\n        result = []\n        while index < len(items) and index < 2:\n            result.append(items[index])\n            index += 1\n        return result\n\nprint(Problem5744Solution.take_prefix_2_while([\"a\"]))\n\n# Example 4: assigned result approach\nresult = take_prefix_2_while([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_prefix_2_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5745,
    "title": "Problem 5745",
    "description": "Write a Python function called `take_prefix_3_while` that must return at most the first 3 list items. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  take_prefix_3_while([1, 2, 3, 4, 5, 6]) -> [1, 2, 3]\n  take_prefix_3_while([\"a\"]) -> [\"a\"]",
    "initialCode": "def take_prefix_3_while(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_prefix_3_while(items):\n    index = 0\n    result = []\n    while index < len(items) and index < 3:\n        result.append(items[index])\n        index += 1\n    return result\n\nprint(take_prefix_3_while([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2, 3]\nprint(take_prefix_3_while([\"a\"]))  # Expected: [\"a\"]\n\n# Example 2: nested helper approach\ndef solve_problem_5745(items):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(items) and index < 3:\n            result.append(items[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5745([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem5745Solution:\n    @staticmethod\n    def take_prefix_3_while(items):\n        index = 0\n        result = []\n        while index < len(items) and index < 3:\n            result.append(items[index])\n            index += 1\n        return result\n\nprint(Problem5745Solution.take_prefix_3_while([\"a\"]))\n\n# Example 4: assigned result approach\nresult = take_prefix_3_while([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_prefix_3_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5746,
    "title": "Problem 5746",
    "description": "Write a Python function called `take_prefix_4_while` that must return at most the first 4 list items. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  take_prefix_4_while([1, 2, 3, 4, 5, 6]) -> [1, 2, 3, 4]\n  take_prefix_4_while([\"a\"]) -> [\"a\"]",
    "initialCode": "def take_prefix_4_while(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_prefix_4_while(items):\n    index = 0\n    result = []\n    while index < len(items) and index < 4:\n        result.append(items[index])\n        index += 1\n    return result\n\nprint(take_prefix_4_while([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2, 3, 4]\nprint(take_prefix_4_while([\"a\"]))  # Expected: [\"a\"]\n\n# Example 2: nested helper approach\ndef solve_problem_5746(items):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(items) and index < 4:\n            result.append(items[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5746([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem5746Solution:\n    @staticmethod\n    def take_prefix_4_while(items):\n        index = 0\n        result = []\n        while index < len(items) and index < 4:\n            result.append(items[index])\n            index += 1\n        return result\n\nprint(Problem5746Solution.take_prefix_4_while([\"a\"]))\n\n# Example 4: assigned result approach\nresult = take_prefix_4_while([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_prefix_4_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5747,
    "title": "Problem 5747",
    "description": "Write a Python function called `take_prefix_5_while` that must return at most the first 5 list items. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  take_prefix_5_while([1, 2, 3, 4, 5, 6]) -> [1, 2, 3, 4, 5]\n  take_prefix_5_while([\"a\"]) -> [\"a\"]",
    "initialCode": "def take_prefix_5_while(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_prefix_5_while(items):\n    index = 0\n    result = []\n    while index < len(items) and index < 5:\n        result.append(items[index])\n        index += 1\n    return result\n\nprint(take_prefix_5_while([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2, 3, 4, 5]\nprint(take_prefix_5_while([\"a\"]))  # Expected: [\"a\"]\n\n# Example 2: nested helper approach\ndef solve_problem_5747(items):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(items) and index < 5:\n            result.append(items[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5747([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem5747Solution:\n    @staticmethod\n    def take_prefix_5_while(items):\n        index = 0\n        result = []\n        while index < len(items) and index < 5:\n            result.append(items[index])\n            index += 1\n        return result\n\nprint(Problem5747Solution.take_prefix_5_while([\"a\"]))\n\n# Example 4: assigned result approach\nresult = take_prefix_5_while([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_prefix_5_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5748,
    "title": "Problem 5748",
    "description": "Write a Python function called `replace_negative_1_while` that must replace every negative list value with 1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  replace_negative_1_while([-2, 0, 4, -1]) -> [1, 0, 4, 1]\n  replace_negative_1_while([1, 2]) -> [1, 2]",
    "initialCode": "def replace_negative_1_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef replace_negative_1_while(values):\n    index = 0\n    result = []\n    while index < len(values):\n        result.append(1 if values[index] < 0 else values[index])\n        index += 1\n    return result\n\nprint(replace_negative_1_while([-2, 0, 4, -1]))  # Expected: [1, 0, 4, 1]\nprint(replace_negative_1_while([1, 2]))  # Expected: [1, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5748(values):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(1 if values[index] < 0 else values[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5748([-2, 0, 4, -1]))\n\n# Example 3: static method approach\nclass Problem5748Solution:\n    @staticmethod\n    def replace_negative_1_while(values):\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(1 if values[index] < 0 else values[index])\n            index += 1\n        return result\n\nprint(Problem5748Solution.replace_negative_1_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = replace_negative_1_while([-2, 0, 4, -1])\nprint(result)\n\n# Example 5: direct call\nprint(replace_negative_1_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5749,
    "title": "Problem 5749",
    "description": "Write a Python function called `replace_negative_2_while` that must replace every negative list value with 2. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  replace_negative_2_while([-2, 0, 4, -1]) -> [2, 0, 4, 2]\n  replace_negative_2_while([1, 2]) -> [1, 2]",
    "initialCode": "def replace_negative_2_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef replace_negative_2_while(values):\n    index = 0\n    result = []\n    while index < len(values):\n        result.append(2 if values[index] < 0 else values[index])\n        index += 1\n    return result\n\nprint(replace_negative_2_while([-2, 0, 4, -1]))  # Expected: [2, 0, 4, 2]\nprint(replace_negative_2_while([1, 2]))  # Expected: [1, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5749(values):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(2 if values[index] < 0 else values[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5749([-2, 0, 4, -1]))\n\n# Example 3: static method approach\nclass Problem5749Solution:\n    @staticmethod\n    def replace_negative_2_while(values):\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(2 if values[index] < 0 else values[index])\n            index += 1\n        return result\n\nprint(Problem5749Solution.replace_negative_2_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = replace_negative_2_while([-2, 0, 4, -1])\nprint(result)\n\n# Example 5: direct call\nprint(replace_negative_2_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5750,
    "title": "Problem 5750",
    "description": "Write a Python function called `replace_negative_3_while` that must replace every negative list value with 3. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  replace_negative_3_while([-2, 0, 4, -1]) -> [3, 0, 4, 3]\n  replace_negative_3_while([1, 2]) -> [1, 2]",
    "initialCode": "def replace_negative_3_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef replace_negative_3_while(values):\n    index = 0\n    result = []\n    while index < len(values):\n        result.append(3 if values[index] < 0 else values[index])\n        index += 1\n    return result\n\nprint(replace_negative_3_while([-2, 0, 4, -1]))  # Expected: [3, 0, 4, 3]\nprint(replace_negative_3_while([1, 2]))  # Expected: [1, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5750(values):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(3 if values[index] < 0 else values[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5750([-2, 0, 4, -1]))\n\n# Example 3: static method approach\nclass Problem5750Solution:\n    @staticmethod\n    def replace_negative_3_while(values):\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(3 if values[index] < 0 else values[index])\n            index += 1\n        return result\n\nprint(Problem5750Solution.replace_negative_3_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = replace_negative_3_while([-2, 0, 4, -1])\nprint(result)\n\n# Example 5: direct call\nprint(replace_negative_3_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5751,
    "title": "Problem 5751",
    "description": "Write a Python function called `replace_negative_4_while` that must replace every negative list value with 4. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  replace_negative_4_while([-2, 0, 4, -1]) -> [4, 0, 4, 4]\n  replace_negative_4_while([1, 2]) -> [1, 2]",
    "initialCode": "def replace_negative_4_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef replace_negative_4_while(values):\n    index = 0\n    result = []\n    while index < len(values):\n        result.append(4 if values[index] < 0 else values[index])\n        index += 1\n    return result\n\nprint(replace_negative_4_while([-2, 0, 4, -1]))  # Expected: [4, 0, 4, 4]\nprint(replace_negative_4_while([1, 2]))  # Expected: [1, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5751(values):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(4 if values[index] < 0 else values[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5751([-2, 0, 4, -1]))\n\n# Example 3: static method approach\nclass Problem5751Solution:\n    @staticmethod\n    def replace_negative_4_while(values):\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(4 if values[index] < 0 else values[index])\n            index += 1\n        return result\n\nprint(Problem5751Solution.replace_negative_4_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = replace_negative_4_while([-2, 0, 4, -1])\nprint(result)\n\n# Example 5: direct call\nprint(replace_negative_4_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5752,
    "title": "Problem 5752",
    "description": "Write a Python function called `replace_negative_5_while` that must replace every negative list value with 5. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  replace_negative_5_while([-2, 0, 4, -1]) -> [5, 0, 4, 5]\n  replace_negative_5_while([1, 2]) -> [1, 2]",
    "initialCode": "def replace_negative_5_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef replace_negative_5_while(values):\n    index = 0\n    result = []\n    while index < len(values):\n        result.append(5 if values[index] < 0 else values[index])\n        index += 1\n    return result\n\nprint(replace_negative_5_while([-2, 0, 4, -1]))  # Expected: [5, 0, 4, 5]\nprint(replace_negative_5_while([1, 2]))  # Expected: [1, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5752(values):\n    def calculate():\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(5 if values[index] < 0 else values[index])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5752([-2, 0, 4, -1]))\n\n# Example 3: static method approach\nclass Problem5752Solution:\n    @staticmethod\n    def replace_negative_5_while(values):\n        index = 0\n        result = []\n        while index < len(values):\n            result.append(5 if values[index] < 0 else values[index])\n            index += 1\n        return result\n\nprint(Problem5752Solution.replace_negative_5_while([1, 2]))\n\n# Example 4: assigned result approach\nresult = replace_negative_5_while([-2, 0, 4, -1])\nprint(result)\n\n# Example 5: direct call\nprint(replace_negative_5_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5753,
    "title": "Problem 5753",
    "description": "Write a Python function called `running_total_1_while` that must return running totals that begin with an initial total of 1. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  running_total_1_while([1, 2, 3]) -> [2, 4, 7]\n  running_total_1_while([-1, 4]) -> [0, 4]",
    "initialCode": "def running_total_1_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_total_1_while(values):\n    index = 0\n    total = 1\n    result = []\n    while index < len(values):\n        total += values[index]\n        result.append(total)\n        index += 1\n    return result\n\nprint(running_total_1_while([1, 2, 3]))  # Expected: [2, 4, 7]\nprint(running_total_1_while([-1, 4]))  # Expected: [0, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_5753(values):\n    def calculate():\n        index = 0\n        total = 1\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5753([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5753Solution:\n    @staticmethod\n    def running_total_1_while(values):\n        index = 0\n        total = 1\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n\nprint(Problem5753Solution.running_total_1_while([-1, 4]))\n\n# Example 4: assigned result approach\nresult = running_total_1_while([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_total_1_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5754,
    "title": "Problem 5754",
    "description": "Write a Python function called `running_total_2_while` that must return running totals that begin with an initial total of 2. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  running_total_2_while([1, 2, 3]) -> [3, 5, 8]\n  running_total_2_while([-1, 4]) -> [1, 5]",
    "initialCode": "def running_total_2_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_total_2_while(values):\n    index = 0\n    total = 2\n    result = []\n    while index < len(values):\n        total += values[index]\n        result.append(total)\n        index += 1\n    return result\n\nprint(running_total_2_while([1, 2, 3]))  # Expected: [3, 5, 8]\nprint(running_total_2_while([-1, 4]))  # Expected: [1, 5]\n\n# Example 2: nested helper approach\ndef solve_problem_5754(values):\n    def calculate():\n        index = 0\n        total = 2\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5754([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5754Solution:\n    @staticmethod\n    def running_total_2_while(values):\n        index = 0\n        total = 2\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n\nprint(Problem5754Solution.running_total_2_while([-1, 4]))\n\n# Example 4: assigned result approach\nresult = running_total_2_while([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_total_2_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5755,
    "title": "Problem 5755",
    "description": "Write a Python function called `running_total_3_while` that must return running totals that begin with an initial total of 3. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  running_total_3_while([1, 2, 3]) -> [4, 6, 9]\n  running_total_3_while([-1, 4]) -> [2, 6]",
    "initialCode": "def running_total_3_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_total_3_while(values):\n    index = 0\n    total = 3\n    result = []\n    while index < len(values):\n        total += values[index]\n        result.append(total)\n        index += 1\n    return result\n\nprint(running_total_3_while([1, 2, 3]))  # Expected: [4, 6, 9]\nprint(running_total_3_while([-1, 4]))  # Expected: [2, 6]\n\n# Example 2: nested helper approach\ndef solve_problem_5755(values):\n    def calculate():\n        index = 0\n        total = 3\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5755([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5755Solution:\n    @staticmethod\n    def running_total_3_while(values):\n        index = 0\n        total = 3\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n\nprint(Problem5755Solution.running_total_3_while([-1, 4]))\n\n# Example 4: assigned result approach\nresult = running_total_3_while([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_total_3_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5756,
    "title": "Problem 5756",
    "description": "Write a Python function called `running_total_4_while` that must return running totals that begin with an initial total of 4. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  running_total_4_while([1, 2, 3]) -> [5, 7, 10]\n  running_total_4_while([-1, 4]) -> [3, 7]",
    "initialCode": "def running_total_4_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_total_4_while(values):\n    index = 0\n    total = 4\n    result = []\n    while index < len(values):\n        total += values[index]\n        result.append(total)\n        index += 1\n    return result\n\nprint(running_total_4_while([1, 2, 3]))  # Expected: [5, 7, 10]\nprint(running_total_4_while([-1, 4]))  # Expected: [3, 7]\n\n# Example 2: nested helper approach\ndef solve_problem_5756(values):\n    def calculate():\n        index = 0\n        total = 4\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5756([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5756Solution:\n    @staticmethod\n    def running_total_4_while(values):\n        index = 0\n        total = 4\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n\nprint(Problem5756Solution.running_total_4_while([-1, 4]))\n\n# Example 4: assigned result approach\nresult = running_total_4_while([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_total_4_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5757,
    "title": "Problem 5757",
    "description": "Write a Python function called `running_total_5_while` that must return running totals that begin with an initial total of 5. Practice while loop syntax.\nDifficulty: Easy.\nExamples:\n  running_total_5_while([1, 2, 3]) -> [6, 8, 11]\n  running_total_5_while([-1, 4]) -> [4, 8]",
    "initialCode": "def running_total_5_while(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_total_5_while(values):\n    index = 0\n    total = 5\n    result = []\n    while index < len(values):\n        total += values[index]\n        result.append(total)\n        index += 1\n    return result\n\nprint(running_total_5_while([1, 2, 3]))  # Expected: [6, 8, 11]\nprint(running_total_5_while([-1, 4]))  # Expected: [4, 8]\n\n# Example 2: nested helper approach\ndef solve_problem_5757(values):\n    def calculate():\n        index = 0\n        total = 5\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_5757([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5757Solution:\n    @staticmethod\n    def running_total_5_while(values):\n        index = 0\n        total = 5\n        result = []\n        while index < len(values):\n            total += values[index]\n            result.append(total)\n            index += 1\n        return result\n\nprint(Problem5757Solution.running_total_5_while([-1, 4]))\n\n# Example 4: assigned result approach\nresult = running_total_5_while([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_total_5_while([]))",
    "hint": "Focus on the starting state, stopping condition, and state update. Use the required while loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the while loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "While Loop Easy"
  },
  {
    "id": 5758,
    "title": "Problem 5758",
    "description": "Write a Python function called `inside_1_boolean` that must return whether `value` is between -1 and 1, inclusive. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  inside_1_boolean(-8) -> False\n  inside_1_boolean(1) -> True",
    "initialCode": "def inside_1_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef inside_1_boolean(value):\n    return value >= -1 and value <= 1\n\nprint(inside_1_boolean(-8))  # Expected: False\nprint(inside_1_boolean(1))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5758(value):\n    def calculate():\n        return value >= -1 and value <= 1\n    return calculate()\n\nprint(solve_problem_5758(-8))\n\n# Example 3: static method approach\nclass Problem5758Solution:\n    @staticmethod\n    def inside_1_boolean(value):\n        return value >= -1 and value <= 1\n\nprint(Problem5758Solution.inside_1_boolean(1))\n\n# Example 4: assigned result approach\nresult = inside_1_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(inside_1_boolean(7))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5759,
    "title": "Problem 5759",
    "description": "Write a Python function called `inside_2_boolean` that must return whether `value` is between -2 and 2, inclusive. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  inside_2_boolean(-8) -> False\n  inside_2_boolean(2) -> True",
    "initialCode": "def inside_2_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef inside_2_boolean(value):\n    return value >= -2 and value <= 2\n\nprint(inside_2_boolean(-8))  # Expected: False\nprint(inside_2_boolean(2))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5759(value):\n    def calculate():\n        return value >= -2 and value <= 2\n    return calculate()\n\nprint(solve_problem_5759(-8))\n\n# Example 3: static method approach\nclass Problem5759Solution:\n    @staticmethod\n    def inside_2_boolean(value):\n        return value >= -2 and value <= 2\n\nprint(Problem5759Solution.inside_2_boolean(2))\n\n# Example 4: assigned result approach\nresult = inside_2_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(inside_2_boolean(8))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5760,
    "title": "Problem 5760",
    "description": "Write a Python function called `inside_3_boolean` that must return whether `value` is between -3 and 3, inclusive. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  inside_3_boolean(-8) -> False\n  inside_3_boolean(3) -> True",
    "initialCode": "def inside_3_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef inside_3_boolean(value):\n    return value >= -3 and value <= 3\n\nprint(inside_3_boolean(-8))  # Expected: False\nprint(inside_3_boolean(3))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5760(value):\n    def calculate():\n        return value >= -3 and value <= 3\n    return calculate()\n\nprint(solve_problem_5760(-8))\n\n# Example 3: static method approach\nclass Problem5760Solution:\n    @staticmethod\n    def inside_3_boolean(value):\n        return value >= -3 and value <= 3\n\nprint(Problem5760Solution.inside_3_boolean(3))\n\n# Example 4: assigned result approach\nresult = inside_3_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(inside_3_boolean(9))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5761,
    "title": "Problem 5761",
    "description": "Write a Python function called `inside_4_boolean` that must return whether `value` is between -4 and 4, inclusive. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  inside_4_boolean(-8) -> False\n  inside_4_boolean(4) -> True",
    "initialCode": "def inside_4_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef inside_4_boolean(value):\n    return value >= -4 and value <= 4\n\nprint(inside_4_boolean(-8))  # Expected: False\nprint(inside_4_boolean(4))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5761(value):\n    def calculate():\n        return value >= -4 and value <= 4\n    return calculate()\n\nprint(solve_problem_5761(-8))\n\n# Example 3: static method approach\nclass Problem5761Solution:\n    @staticmethod\n    def inside_4_boolean(value):\n        return value >= -4 and value <= 4\n\nprint(Problem5761Solution.inside_4_boolean(4))\n\n# Example 4: assigned result approach\nresult = inside_4_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(inside_4_boolean(10))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5762,
    "title": "Problem 5762",
    "description": "Write a Python function called `inside_5_boolean` that must return whether `value` is between -5 and 5, inclusive. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  inside_5_boolean(-8) -> False\n  inside_5_boolean(5) -> True",
    "initialCode": "def inside_5_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef inside_5_boolean(value):\n    return value >= -5 and value <= 5\n\nprint(inside_5_boolean(-8))  # Expected: False\nprint(inside_5_boolean(5))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5762(value):\n    def calculate():\n        return value >= -5 and value <= 5\n    return calculate()\n\nprint(solve_problem_5762(-8))\n\n# Example 3: static method approach\nclass Problem5762Solution:\n    @staticmethod\n    def inside_5_boolean(value):\n        return value >= -5 and value <= 5\n\nprint(Problem5762Solution.inside_5_boolean(5))\n\n# Example 4: assigned result approach\nresult = inside_5_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(inside_5_boolean(11))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5763,
    "title": "Problem 5763",
    "description": "Write a Python function called `outside_1_boolean` that must return whether `value` is below -1 or above 1. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  outside_1_boolean(-8) -> True\n  outside_1_boolean(1) -> False",
    "initialCode": "def outside_1_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef outside_1_boolean(value):\n    return value < -1 or value > 1\n\nprint(outside_1_boolean(-8))  # Expected: True\nprint(outside_1_boolean(1))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5763(value):\n    def calculate():\n        return value < -1 or value > 1\n    return calculate()\n\nprint(solve_problem_5763(-8))\n\n# Example 3: static method approach\nclass Problem5763Solution:\n    @staticmethod\n    def outside_1_boolean(value):\n        return value < -1 or value > 1\n\nprint(Problem5763Solution.outside_1_boolean(1))\n\n# Example 4: assigned result approach\nresult = outside_1_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(outside_1_boolean(7))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5764,
    "title": "Problem 5764",
    "description": "Write a Python function called `outside_2_boolean` that must return whether `value` is below -2 or above 2. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  outside_2_boolean(-8) -> True\n  outside_2_boolean(2) -> False",
    "initialCode": "def outside_2_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef outside_2_boolean(value):\n    return value < -2 or value > 2\n\nprint(outside_2_boolean(-8))  # Expected: True\nprint(outside_2_boolean(2))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5764(value):\n    def calculate():\n        return value < -2 or value > 2\n    return calculate()\n\nprint(solve_problem_5764(-8))\n\n# Example 3: static method approach\nclass Problem5764Solution:\n    @staticmethod\n    def outside_2_boolean(value):\n        return value < -2 or value > 2\n\nprint(Problem5764Solution.outside_2_boolean(2))\n\n# Example 4: assigned result approach\nresult = outside_2_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(outside_2_boolean(8))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5765,
    "title": "Problem 5765",
    "description": "Write a Python function called `outside_3_boolean` that must return whether `value` is below -3 or above 3. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  outside_3_boolean(-8) -> True\n  outside_3_boolean(3) -> False",
    "initialCode": "def outside_3_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef outside_3_boolean(value):\n    return value < -3 or value > 3\n\nprint(outside_3_boolean(-8))  # Expected: True\nprint(outside_3_boolean(3))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5765(value):\n    def calculate():\n        return value < -3 or value > 3\n    return calculate()\n\nprint(solve_problem_5765(-8))\n\n# Example 3: static method approach\nclass Problem5765Solution:\n    @staticmethod\n    def outside_3_boolean(value):\n        return value < -3 or value > 3\n\nprint(Problem5765Solution.outside_3_boolean(3))\n\n# Example 4: assigned result approach\nresult = outside_3_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(outside_3_boolean(9))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5766,
    "title": "Problem 5766",
    "description": "Write a Python function called `outside_4_boolean` that must return whether `value` is below -4 or above 4. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  outside_4_boolean(-8) -> True\n  outside_4_boolean(4) -> False",
    "initialCode": "def outside_4_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef outside_4_boolean(value):\n    return value < -4 or value > 4\n\nprint(outside_4_boolean(-8))  # Expected: True\nprint(outside_4_boolean(4))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5766(value):\n    def calculate():\n        return value < -4 or value > 4\n    return calculate()\n\nprint(solve_problem_5766(-8))\n\n# Example 3: static method approach\nclass Problem5766Solution:\n    @staticmethod\n    def outside_4_boolean(value):\n        return value < -4 or value > 4\n\nprint(Problem5766Solution.outside_4_boolean(4))\n\n# Example 4: assigned result approach\nresult = outside_4_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(outside_4_boolean(10))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5767,
    "title": "Problem 5767",
    "description": "Write a Python function called `outside_5_boolean` that must return whether `value` is below -5 or above 5. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  outside_5_boolean(-8) -> True\n  outside_5_boolean(5) -> False",
    "initialCode": "def outside_5_boolean(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef outside_5_boolean(value):\n    return value < -5 or value > 5\n\nprint(outside_5_boolean(-8))  # Expected: True\nprint(outside_5_boolean(5))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5767(value):\n    def calculate():\n        return value < -5 or value > 5\n    return calculate()\n\nprint(solve_problem_5767(-8))\n\n# Example 3: static method approach\nclass Problem5767Solution:\n    @staticmethod\n    def outside_5_boolean(value):\n        return value < -5 or value > 5\n\nprint(Problem5767Solution.outside_5_boolean(5))\n\n# Example 4: assigned result approach\nresult = outside_5_boolean(-8)\nprint(result)\n\n# Example 5: direct call\nprint(outside_5_boolean(11))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5768,
    "title": "Problem 5768",
    "description": "Write a Python function called `positive_even_after_1` that must return whether `value` is both greater than 1 and even. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  positive_even_after_1(1) -> False\n  positive_even_after_1(2) -> True",
    "initialCode": "def positive_even_after_1(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_even_after_1(value):\n    return value > 1 and value % 2 == 0\n\nprint(positive_even_after_1(1))  # Expected: False\nprint(positive_even_after_1(2))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5768(value):\n    def calculate():\n        return value > 1 and value % 2 == 0\n    return calculate()\n\nprint(solve_problem_5768(1))\n\n# Example 3: static method approach\nclass Problem5768Solution:\n    @staticmethod\n    def positive_even_after_1(value):\n        return value > 1 and value % 2 == 0\n\nprint(Problem5768Solution.positive_even_after_1(2))\n\n# Example 4: assigned result approach\nresult = positive_even_after_1(1)\nprint(result)\n\n# Example 5: direct call\nprint(positive_even_after_1(5))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5769,
    "title": "Problem 5769",
    "description": "Write a Python function called `positive_even_after_2` that must return whether `value` is both greater than 2 and even. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  positive_even_after_2(2) -> False\n  positive_even_after_2(3) -> False",
    "initialCode": "def positive_even_after_2(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_even_after_2(value):\n    return value > 2 and value % 2 == 0\n\nprint(positive_even_after_2(2))  # Expected: False\nprint(positive_even_after_2(3))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5769(value):\n    def calculate():\n        return value > 2 and value % 2 == 0\n    return calculate()\n\nprint(solve_problem_5769(2))\n\n# Example 3: static method approach\nclass Problem5769Solution:\n    @staticmethod\n    def positive_even_after_2(value):\n        return value > 2 and value % 2 == 0\n\nprint(Problem5769Solution.positive_even_after_2(3))\n\n# Example 4: assigned result approach\nresult = positive_even_after_2(2)\nprint(result)\n\n# Example 5: direct call\nprint(positive_even_after_2(6))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5770,
    "title": "Problem 5770",
    "description": "Write a Python function called `positive_even_after_3` that must return whether `value` is both greater than 3 and even. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  positive_even_after_3(3) -> False\n  positive_even_after_3(4) -> True",
    "initialCode": "def positive_even_after_3(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_even_after_3(value):\n    return value > 3 and value % 2 == 0\n\nprint(positive_even_after_3(3))  # Expected: False\nprint(positive_even_after_3(4))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5770(value):\n    def calculate():\n        return value > 3 and value % 2 == 0\n    return calculate()\n\nprint(solve_problem_5770(3))\n\n# Example 3: static method approach\nclass Problem5770Solution:\n    @staticmethod\n    def positive_even_after_3(value):\n        return value > 3 and value % 2 == 0\n\nprint(Problem5770Solution.positive_even_after_3(4))\n\n# Example 4: assigned result approach\nresult = positive_even_after_3(3)\nprint(result)\n\n# Example 5: direct call\nprint(positive_even_after_3(7))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5771,
    "title": "Problem 5771",
    "description": "Write a Python function called `positive_even_after_4` that must return whether `value` is both greater than 4 and even. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  positive_even_after_4(4) -> False\n  positive_even_after_4(5) -> False",
    "initialCode": "def positive_even_after_4(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_even_after_4(value):\n    return value > 4 and value % 2 == 0\n\nprint(positive_even_after_4(4))  # Expected: False\nprint(positive_even_after_4(5))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5771(value):\n    def calculate():\n        return value > 4 and value % 2 == 0\n    return calculate()\n\nprint(solve_problem_5771(4))\n\n# Example 3: static method approach\nclass Problem5771Solution:\n    @staticmethod\n    def positive_even_after_4(value):\n        return value > 4 and value % 2 == 0\n\nprint(Problem5771Solution.positive_even_after_4(5))\n\n# Example 4: assigned result approach\nresult = positive_even_after_4(4)\nprint(result)\n\n# Example 5: direct call\nprint(positive_even_after_4(8))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5772,
    "title": "Problem 5772",
    "description": "Write a Python function called `positive_even_after_5` that must return whether `value` is both greater than 5 and even. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  positive_even_after_5(5) -> False\n  positive_even_after_5(6) -> True",
    "initialCode": "def positive_even_after_5(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_even_after_5(value):\n    return value > 5 and value % 2 == 0\n\nprint(positive_even_after_5(5))  # Expected: False\nprint(positive_even_after_5(6))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5772(value):\n    def calculate():\n        return value > 5 and value % 2 == 0\n    return calculate()\n\nprint(solve_problem_5772(5))\n\n# Example 3: static method approach\nclass Problem5772Solution:\n    @staticmethod\n    def positive_even_after_5(value):\n        return value > 5 and value % 2 == 0\n\nprint(Problem5772Solution.positive_even_after_5(6))\n\n# Example 4: assigned result approach\nresult = positive_even_after_5(5)\nprint(result)\n\n# Example 5: direct call\nprint(positive_even_after_5(9))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5773,
    "title": "Problem 5773",
    "description": "Write a Python function called `divisible_choice_1` that must return whether `value` is divisible by 2 or 3. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  divisible_choice_1(2) -> True\n  divisible_choice_1(3) -> True",
    "initialCode": "def divisible_choice_1(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_choice_1(value):\n    return value % 2 == 0 or value % 3 == 0\n\nprint(divisible_choice_1(2))  # Expected: True\nprint(divisible_choice_1(3))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5773(value):\n    def calculate():\n        return value % 2 == 0 or value % 3 == 0\n    return calculate()\n\nprint(solve_problem_5773(2))\n\n# Example 3: static method approach\nclass Problem5773Solution:\n    @staticmethod\n    def divisible_choice_1(value):\n        return value % 2 == 0 or value % 3 == 0\n\nprint(Problem5773Solution.divisible_choice_1(3))\n\n# Example 4: assigned result approach\nresult = divisible_choice_1(2)\nprint(result)\n\n# Example 5: direct call\nprint(divisible_choice_1(7))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5774,
    "title": "Problem 5774",
    "description": "Write a Python function called `divisible_choice_2` that must return whether `value` is divisible by 3 or 4. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  divisible_choice_2(3) -> True\n  divisible_choice_2(4) -> True",
    "initialCode": "def divisible_choice_2(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_choice_2(value):\n    return value % 3 == 0 or value % 4 == 0\n\nprint(divisible_choice_2(3))  # Expected: True\nprint(divisible_choice_2(4))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5774(value):\n    def calculate():\n        return value % 3 == 0 or value % 4 == 0\n    return calculate()\n\nprint(solve_problem_5774(3))\n\n# Example 3: static method approach\nclass Problem5774Solution:\n    @staticmethod\n    def divisible_choice_2(value):\n        return value % 3 == 0 or value % 4 == 0\n\nprint(Problem5774Solution.divisible_choice_2(4))\n\n# Example 4: assigned result approach\nresult = divisible_choice_2(3)\nprint(result)\n\n# Example 5: direct call\nprint(divisible_choice_2(13))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5775,
    "title": "Problem 5775",
    "description": "Write a Python function called `divisible_choice_3` that must return whether `value` is divisible by 4 or 5. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  divisible_choice_3(4) -> True\n  divisible_choice_3(5) -> True",
    "initialCode": "def divisible_choice_3(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_choice_3(value):\n    return value % 4 == 0 or value % 5 == 0\n\nprint(divisible_choice_3(4))  # Expected: True\nprint(divisible_choice_3(5))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5775(value):\n    def calculate():\n        return value % 4 == 0 or value % 5 == 0\n    return calculate()\n\nprint(solve_problem_5775(4))\n\n# Example 3: static method approach\nclass Problem5775Solution:\n    @staticmethod\n    def divisible_choice_3(value):\n        return value % 4 == 0 or value % 5 == 0\n\nprint(Problem5775Solution.divisible_choice_3(5))\n\n# Example 4: assigned result approach\nresult = divisible_choice_3(4)\nprint(result)\n\n# Example 5: direct call\nprint(divisible_choice_3(21))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5776,
    "title": "Problem 5776",
    "description": "Write a Python function called `divisible_choice_4` that must return whether `value` is divisible by 5 or 6. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  divisible_choice_4(5) -> True\n  divisible_choice_4(6) -> True",
    "initialCode": "def divisible_choice_4(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_choice_4(value):\n    return value % 5 == 0 or value % 6 == 0\n\nprint(divisible_choice_4(5))  # Expected: True\nprint(divisible_choice_4(6))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5776(value):\n    def calculate():\n        return value % 5 == 0 or value % 6 == 0\n    return calculate()\n\nprint(solve_problem_5776(5))\n\n# Example 3: static method approach\nclass Problem5776Solution:\n    @staticmethod\n    def divisible_choice_4(value):\n        return value % 5 == 0 or value % 6 == 0\n\nprint(Problem5776Solution.divisible_choice_4(6))\n\n# Example 4: assigned result approach\nresult = divisible_choice_4(5)\nprint(result)\n\n# Example 5: direct call\nprint(divisible_choice_4(31))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5777,
    "title": "Problem 5777",
    "description": "Write a Python function called `divisible_choice_5` that must return whether `value` is divisible by 6 or 7. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  divisible_choice_5(6) -> True\n  divisible_choice_5(7) -> True",
    "initialCode": "def divisible_choice_5(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_choice_5(value):\n    return value % 6 == 0 or value % 7 == 0\n\nprint(divisible_choice_5(6))  # Expected: True\nprint(divisible_choice_5(7))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5777(value):\n    def calculate():\n        return value % 6 == 0 or value % 7 == 0\n    return calculate()\n\nprint(solve_problem_5777(6))\n\n# Example 3: static method approach\nclass Problem5777Solution:\n    @staticmethod\n    def divisible_choice_5(value):\n        return value % 6 == 0 or value % 7 == 0\n\nprint(Problem5777Solution.divisible_choice_5(7))\n\n# Example 4: assigned result approach\nresult = divisible_choice_5(6)\nprint(result)\n\n# Example 5: direct call\nprint(divisible_choice_5(43))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5778,
    "title": "Problem 5778",
    "description": "Write a Python function called `not_outside_1` that must use `not` to return whether `value` stays within -1 and 1. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  not_outside_1(-8) -> False\n  not_outside_1(1) -> True",
    "initialCode": "def not_outside_1(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef not_outside_1(value):\n    return not (value < -1 or value > 1)\n\nprint(not_outside_1(-8))  # Expected: False\nprint(not_outside_1(1))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5778(value):\n    def calculate():\n        return not (value < -1 or value > 1)\n    return calculate()\n\nprint(solve_problem_5778(-8))\n\n# Example 3: static method approach\nclass Problem5778Solution:\n    @staticmethod\n    def not_outside_1(value):\n        return not (value < -1 or value > 1)\n\nprint(Problem5778Solution.not_outside_1(1))\n\n# Example 4: assigned result approach\nresult = not_outside_1(-8)\nprint(result)\n\n# Example 5: direct call\nprint(not_outside_1(7))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5779,
    "title": "Problem 5779",
    "description": "Write a Python function called `not_outside_2` that must use `not` to return whether `value` stays within -2 and 2. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  not_outside_2(-8) -> False\n  not_outside_2(2) -> True",
    "initialCode": "def not_outside_2(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef not_outside_2(value):\n    return not (value < -2 or value > 2)\n\nprint(not_outside_2(-8))  # Expected: False\nprint(not_outside_2(2))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5779(value):\n    def calculate():\n        return not (value < -2 or value > 2)\n    return calculate()\n\nprint(solve_problem_5779(-8))\n\n# Example 3: static method approach\nclass Problem5779Solution:\n    @staticmethod\n    def not_outside_2(value):\n        return not (value < -2 or value > 2)\n\nprint(Problem5779Solution.not_outside_2(2))\n\n# Example 4: assigned result approach\nresult = not_outside_2(-8)\nprint(result)\n\n# Example 5: direct call\nprint(not_outside_2(8))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5780,
    "title": "Problem 5780",
    "description": "Write a Python function called `not_outside_3` that must use `not` to return whether `value` stays within -3 and 3. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  not_outside_3(-8) -> False\n  not_outside_3(3) -> True",
    "initialCode": "def not_outside_3(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef not_outside_3(value):\n    return not (value < -3 or value > 3)\n\nprint(not_outside_3(-8))  # Expected: False\nprint(not_outside_3(3))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5780(value):\n    def calculate():\n        return not (value < -3 or value > 3)\n    return calculate()\n\nprint(solve_problem_5780(-8))\n\n# Example 3: static method approach\nclass Problem5780Solution:\n    @staticmethod\n    def not_outside_3(value):\n        return not (value < -3 or value > 3)\n\nprint(Problem5780Solution.not_outside_3(3))\n\n# Example 4: assigned result approach\nresult = not_outside_3(-8)\nprint(result)\n\n# Example 5: direct call\nprint(not_outside_3(9))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5781,
    "title": "Problem 5781",
    "description": "Write a Python function called `not_outside_4` that must use `not` to return whether `value` stays within -4 and 4. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  not_outside_4(-8) -> False\n  not_outside_4(4) -> True",
    "initialCode": "def not_outside_4(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef not_outside_4(value):\n    return not (value < -4 or value > 4)\n\nprint(not_outside_4(-8))  # Expected: False\nprint(not_outside_4(4))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5781(value):\n    def calculate():\n        return not (value < -4 or value > 4)\n    return calculate()\n\nprint(solve_problem_5781(-8))\n\n# Example 3: static method approach\nclass Problem5781Solution:\n    @staticmethod\n    def not_outside_4(value):\n        return not (value < -4 or value > 4)\n\nprint(Problem5781Solution.not_outside_4(4))\n\n# Example 4: assigned result approach\nresult = not_outside_4(-8)\nprint(result)\n\n# Example 5: direct call\nprint(not_outside_4(10))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5782,
    "title": "Problem 5782",
    "description": "Write a Python function called `not_outside_5` that must use `not` to return whether `value` stays within -5 and 5. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  not_outside_5(-8) -> False\n  not_outside_5(5) -> True",
    "initialCode": "def not_outside_5(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef not_outside_5(value):\n    return not (value < -5 or value > 5)\n\nprint(not_outside_5(-8))  # Expected: False\nprint(not_outside_5(5))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5782(value):\n    def calculate():\n        return not (value < -5 or value > 5)\n    return calculate()\n\nprint(solve_problem_5782(-8))\n\n# Example 3: static method approach\nclass Problem5782Solution:\n    @staticmethod\n    def not_outside_5(value):\n        return not (value < -5 or value > 5)\n\nprint(Problem5782Solution.not_outside_5(5))\n\n# Example 4: assigned result approach\nresult = not_outside_5(-8)\nprint(result)\n\n# Example 5: direct call\nprint(not_outside_5(11))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5783,
    "title": "Problem 5783",
    "description": "Write a Python function called `text_starts_1_boolean` that must return whether text is non-empty and starts with \"1\". Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  text_starts_1_boolean(\"1abc\") -> True\n  text_starts_1_boolean(\"\") -> False",
    "initialCode": "def text_starts_1_boolean(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef text_starts_1_boolean(text):\n    return bool(text) and text.startswith(\"1\")\n\nprint(text_starts_1_boolean(\"1abc\"))  # Expected: True\nprint(text_starts_1_boolean(\"\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5783(text):\n    def calculate():\n        return bool(text) and text.startswith(\"1\")\n    return calculate()\n\nprint(solve_problem_5783(\"1abc\"))\n\n# Example 3: static method approach\nclass Problem5783Solution:\n    @staticmethod\n    def text_starts_1_boolean(text):\n        return bool(text) and text.startswith(\"1\")\n\nprint(Problem5783Solution.text_starts_1_boolean(\"\"))\n\n# Example 4: assigned result approach\nresult = text_starts_1_boolean(\"1abc\")\nprint(result)\n\n# Example 5: direct call\nprint(text_starts_1_boolean(\"x1\"))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5784,
    "title": "Problem 5784",
    "description": "Write a Python function called `text_starts_2_boolean` that must return whether text is non-empty and starts with \"2\". Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  text_starts_2_boolean(\"2abc\") -> True\n  text_starts_2_boolean(\"\") -> False",
    "initialCode": "def text_starts_2_boolean(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef text_starts_2_boolean(text):\n    return bool(text) and text.startswith(\"2\")\n\nprint(text_starts_2_boolean(\"2abc\"))  # Expected: True\nprint(text_starts_2_boolean(\"\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5784(text):\n    def calculate():\n        return bool(text) and text.startswith(\"2\")\n    return calculate()\n\nprint(solve_problem_5784(\"2abc\"))\n\n# Example 3: static method approach\nclass Problem5784Solution:\n    @staticmethod\n    def text_starts_2_boolean(text):\n        return bool(text) and text.startswith(\"2\")\n\nprint(Problem5784Solution.text_starts_2_boolean(\"\"))\n\n# Example 4: assigned result approach\nresult = text_starts_2_boolean(\"2abc\")\nprint(result)\n\n# Example 5: direct call\nprint(text_starts_2_boolean(\"x2\"))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5785,
    "title": "Problem 5785",
    "description": "Write a Python function called `text_starts_3_boolean` that must return whether text is non-empty and starts with \"3\". Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  text_starts_3_boolean(\"3abc\") -> True\n  text_starts_3_boolean(\"\") -> False",
    "initialCode": "def text_starts_3_boolean(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef text_starts_3_boolean(text):\n    return bool(text) and text.startswith(\"3\")\n\nprint(text_starts_3_boolean(\"3abc\"))  # Expected: True\nprint(text_starts_3_boolean(\"\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5785(text):\n    def calculate():\n        return bool(text) and text.startswith(\"3\")\n    return calculate()\n\nprint(solve_problem_5785(\"3abc\"))\n\n# Example 3: static method approach\nclass Problem5785Solution:\n    @staticmethod\n    def text_starts_3_boolean(text):\n        return bool(text) and text.startswith(\"3\")\n\nprint(Problem5785Solution.text_starts_3_boolean(\"\"))\n\n# Example 4: assigned result approach\nresult = text_starts_3_boolean(\"3abc\")\nprint(result)\n\n# Example 5: direct call\nprint(text_starts_3_boolean(\"x3\"))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5786,
    "title": "Problem 5786",
    "description": "Write a Python function called `text_starts_4_boolean` that must return whether text is non-empty and starts with \"4\". Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  text_starts_4_boolean(\"4abc\") -> True\n  text_starts_4_boolean(\"\") -> False",
    "initialCode": "def text_starts_4_boolean(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef text_starts_4_boolean(text):\n    return bool(text) and text.startswith(\"4\")\n\nprint(text_starts_4_boolean(\"4abc\"))  # Expected: True\nprint(text_starts_4_boolean(\"\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5786(text):\n    def calculate():\n        return bool(text) and text.startswith(\"4\")\n    return calculate()\n\nprint(solve_problem_5786(\"4abc\"))\n\n# Example 3: static method approach\nclass Problem5786Solution:\n    @staticmethod\n    def text_starts_4_boolean(text):\n        return bool(text) and text.startswith(\"4\")\n\nprint(Problem5786Solution.text_starts_4_boolean(\"\"))\n\n# Example 4: assigned result approach\nresult = text_starts_4_boolean(\"4abc\")\nprint(result)\n\n# Example 5: direct call\nprint(text_starts_4_boolean(\"x4\"))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5787,
    "title": "Problem 5787",
    "description": "Write a Python function called `text_starts_5_boolean` that must return whether text is non-empty and starts with \"5\". Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  text_starts_5_boolean(\"5abc\") -> True\n  text_starts_5_boolean(\"\") -> False",
    "initialCode": "def text_starts_5_boolean(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef text_starts_5_boolean(text):\n    return bool(text) and text.startswith(\"5\")\n\nprint(text_starts_5_boolean(\"5abc\"))  # Expected: True\nprint(text_starts_5_boolean(\"\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5787(text):\n    def calculate():\n        return bool(text) and text.startswith(\"5\")\n    return calculate()\n\nprint(solve_problem_5787(\"5abc\"))\n\n# Example 3: static method approach\nclass Problem5787Solution:\n    @staticmethod\n    def text_starts_5_boolean(text):\n        return bool(text) and text.startswith(\"5\")\n\nprint(Problem5787Solution.text_starts_5_boolean(\"\"))\n\n# Example 4: assigned result approach\nresult = text_starts_5_boolean(\"5abc\")\nprint(result)\n\n# Example 5: direct call\nprint(text_starts_5_boolean(\"x5\"))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5788,
    "title": "Problem 5788",
    "description": "Write a Python function called `valid_text_length_1` that must return whether the input is a string and has at least 1 characters. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  valid_text_length_1(\"python\") -> True\n  valid_text_length_1(\"x\") -> True",
    "initialCode": "def valid_text_length_1(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef valid_text_length_1(text):\n    return isinstance(text, str) and len(text) >= 1\n\nprint(valid_text_length_1(\"python\"))  # Expected: True\nprint(valid_text_length_1(\"x\"))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5788(text):\n    def calculate():\n        return isinstance(text, str) and len(text) >= 1\n    return calculate()\n\nprint(solve_problem_5788(\"python\"))\n\n# Example 3: static method approach\nclass Problem5788Solution:\n    @staticmethod\n    def valid_text_length_1(text):\n        return isinstance(text, str) and len(text) >= 1\n\nprint(Problem5788Solution.valid_text_length_1(\"x\"))\n\n# Example 4: assigned result approach\nresult = valid_text_length_1(\"python\")\nprint(result)\n\n# Example 5: direct call\nprint(valid_text_length_1(42))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5789,
    "title": "Problem 5789",
    "description": "Write a Python function called `valid_text_length_2` that must return whether the input is a string and has at least 2 characters. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  valid_text_length_2(\"python\") -> True\n  valid_text_length_2(\"x\") -> False",
    "initialCode": "def valid_text_length_2(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef valid_text_length_2(text):\n    return isinstance(text, str) and len(text) >= 2\n\nprint(valid_text_length_2(\"python\"))  # Expected: True\nprint(valid_text_length_2(\"x\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5789(text):\n    def calculate():\n        return isinstance(text, str) and len(text) >= 2\n    return calculate()\n\nprint(solve_problem_5789(\"python\"))\n\n# Example 3: static method approach\nclass Problem5789Solution:\n    @staticmethod\n    def valid_text_length_2(text):\n        return isinstance(text, str) and len(text) >= 2\n\nprint(Problem5789Solution.valid_text_length_2(\"x\"))\n\n# Example 4: assigned result approach\nresult = valid_text_length_2(\"python\")\nprint(result)\n\n# Example 5: direct call\nprint(valid_text_length_2(42))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5790,
    "title": "Problem 5790",
    "description": "Write a Python function called `valid_text_length_3` that must return whether the input is a string and has at least 3 characters. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  valid_text_length_3(\"python\") -> True\n  valid_text_length_3(\"x\") -> False",
    "initialCode": "def valid_text_length_3(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef valid_text_length_3(text):\n    return isinstance(text, str) and len(text) >= 3\n\nprint(valid_text_length_3(\"python\"))  # Expected: True\nprint(valid_text_length_3(\"x\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5790(text):\n    def calculate():\n        return isinstance(text, str) and len(text) >= 3\n    return calculate()\n\nprint(solve_problem_5790(\"python\"))\n\n# Example 3: static method approach\nclass Problem5790Solution:\n    @staticmethod\n    def valid_text_length_3(text):\n        return isinstance(text, str) and len(text) >= 3\n\nprint(Problem5790Solution.valid_text_length_3(\"x\"))\n\n# Example 4: assigned result approach\nresult = valid_text_length_3(\"python\")\nprint(result)\n\n# Example 5: direct call\nprint(valid_text_length_3(42))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5791,
    "title": "Problem 5791",
    "description": "Write a Python function called `valid_text_length_4` that must return whether the input is a string and has at least 4 characters. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  valid_text_length_4(\"python\") -> True\n  valid_text_length_4(\"x\") -> False",
    "initialCode": "def valid_text_length_4(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef valid_text_length_4(text):\n    return isinstance(text, str) and len(text) >= 4\n\nprint(valid_text_length_4(\"python\"))  # Expected: True\nprint(valid_text_length_4(\"x\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5791(text):\n    def calculate():\n        return isinstance(text, str) and len(text) >= 4\n    return calculate()\n\nprint(solve_problem_5791(\"python\"))\n\n# Example 3: static method approach\nclass Problem5791Solution:\n    @staticmethod\n    def valid_text_length_4(text):\n        return isinstance(text, str) and len(text) >= 4\n\nprint(Problem5791Solution.valid_text_length_4(\"x\"))\n\n# Example 4: assigned result approach\nresult = valid_text_length_4(\"python\")\nprint(result)\n\n# Example 5: direct call\nprint(valid_text_length_4(42))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5792,
    "title": "Problem 5792",
    "description": "Write a Python function called `valid_text_length_5` that must return whether the input is a string and has at least 5 characters. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  valid_text_length_5(\"python\") -> True\n  valid_text_length_5(\"x\") -> False",
    "initialCode": "def valid_text_length_5(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef valid_text_length_5(text):\n    return isinstance(text, str) and len(text) >= 5\n\nprint(valid_text_length_5(\"python\"))  # Expected: True\nprint(valid_text_length_5(\"x\"))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5792(text):\n    def calculate():\n        return isinstance(text, str) and len(text) >= 5\n    return calculate()\n\nprint(solve_problem_5792(\"python\"))\n\n# Example 3: static method approach\nclass Problem5792Solution:\n    @staticmethod\n    def valid_text_length_5(text):\n        return isinstance(text, str) and len(text) >= 5\n\nprint(Problem5792Solution.valid_text_length_5(\"x\"))\n\n# Example 4: assigned result approach\nresult = valid_text_length_5(\"python\")\nprint(result)\n\n# Example 5: direct call\nprint(valid_text_length_5(42))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5793,
    "title": "Problem 5793",
    "description": "Write a Python function called `exactly_one_above_1` that must return whether exactly one value is greater than 1. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  exactly_one_above_1(2, 1) -> True\n  exactly_one_above_1(3, 4) -> False",
    "initialCode": "def exactly_one_above_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef exactly_one_above_1(left, right):\n    return (left > 1) != (right > 1)\n\nprint(exactly_one_above_1(2, 1))  # Expected: True\nprint(exactly_one_above_1(3, 4))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5793(left, right):\n    def calculate():\n        return (left > 1) != (right > 1)\n    return calculate()\n\nprint(solve_problem_5793(2, 1))\n\n# Example 3: static method approach\nclass Problem5793Solution:\n    @staticmethod\n    def exactly_one_above_1(left, right):\n        return (left > 1) != (right > 1)\n\nprint(Problem5793Solution.exactly_one_above_1(3, 4))\n\n# Example 4: assigned result approach\nresult = exactly_one_above_1(2, 1)\nprint(result)\n\n# Example 5: direct call\nprint(exactly_one_above_1(0, 1))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5794,
    "title": "Problem 5794",
    "description": "Write a Python function called `exactly_one_above_2` that must return whether exactly one value is greater than 2. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  exactly_one_above_2(3, 2) -> True\n  exactly_one_above_2(4, 5) -> False",
    "initialCode": "def exactly_one_above_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef exactly_one_above_2(left, right):\n    return (left > 2) != (right > 2)\n\nprint(exactly_one_above_2(3, 2))  # Expected: True\nprint(exactly_one_above_2(4, 5))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5794(left, right):\n    def calculate():\n        return (left > 2) != (right > 2)\n    return calculate()\n\nprint(solve_problem_5794(3, 2))\n\n# Example 3: static method approach\nclass Problem5794Solution:\n    @staticmethod\n    def exactly_one_above_2(left, right):\n        return (left > 2) != (right > 2)\n\nprint(Problem5794Solution.exactly_one_above_2(4, 5))\n\n# Example 4: assigned result approach\nresult = exactly_one_above_2(3, 2)\nprint(result)\n\n# Example 5: direct call\nprint(exactly_one_above_2(1, 2))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5795,
    "title": "Problem 5795",
    "description": "Write a Python function called `exactly_one_above_3` that must return whether exactly one value is greater than 3. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  exactly_one_above_3(4, 3) -> True\n  exactly_one_above_3(5, 6) -> False",
    "initialCode": "def exactly_one_above_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef exactly_one_above_3(left, right):\n    return (left > 3) != (right > 3)\n\nprint(exactly_one_above_3(4, 3))  # Expected: True\nprint(exactly_one_above_3(5, 6))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5795(left, right):\n    def calculate():\n        return (left > 3) != (right > 3)\n    return calculate()\n\nprint(solve_problem_5795(4, 3))\n\n# Example 3: static method approach\nclass Problem5795Solution:\n    @staticmethod\n    def exactly_one_above_3(left, right):\n        return (left > 3) != (right > 3)\n\nprint(Problem5795Solution.exactly_one_above_3(5, 6))\n\n# Example 4: assigned result approach\nresult = exactly_one_above_3(4, 3)\nprint(result)\n\n# Example 5: direct call\nprint(exactly_one_above_3(2, 3))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5796,
    "title": "Problem 5796",
    "description": "Write a Python function called `exactly_one_above_4` that must return whether exactly one value is greater than 4. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  exactly_one_above_4(5, 4) -> True\n  exactly_one_above_4(6, 7) -> False",
    "initialCode": "def exactly_one_above_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef exactly_one_above_4(left, right):\n    return (left > 4) != (right > 4)\n\nprint(exactly_one_above_4(5, 4))  # Expected: True\nprint(exactly_one_above_4(6, 7))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5796(left, right):\n    def calculate():\n        return (left > 4) != (right > 4)\n    return calculate()\n\nprint(solve_problem_5796(5, 4))\n\n# Example 3: static method approach\nclass Problem5796Solution:\n    @staticmethod\n    def exactly_one_above_4(left, right):\n        return (left > 4) != (right > 4)\n\nprint(Problem5796Solution.exactly_one_above_4(6, 7))\n\n# Example 4: assigned result approach\nresult = exactly_one_above_4(5, 4)\nprint(result)\n\n# Example 5: direct call\nprint(exactly_one_above_4(3, 4))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5797,
    "title": "Problem 5797",
    "description": "Write a Python function called `exactly_one_above_5` that must return whether exactly one value is greater than 5. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  exactly_one_above_5(6, 5) -> True\n  exactly_one_above_5(7, 8) -> False",
    "initialCode": "def exactly_one_above_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef exactly_one_above_5(left, right):\n    return (left > 5) != (right > 5)\n\nprint(exactly_one_above_5(6, 5))  # Expected: True\nprint(exactly_one_above_5(7, 8))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5797(left, right):\n    def calculate():\n        return (left > 5) != (right > 5)\n    return calculate()\n\nprint(solve_problem_5797(6, 5))\n\n# Example 3: static method approach\nclass Problem5797Solution:\n    @staticmethod\n    def exactly_one_above_5(left, right):\n        return (left > 5) != (right > 5)\n\nprint(Problem5797Solution.exactly_one_above_5(7, 8))\n\n# Example 4: assigned result approach\nresult = exactly_one_above_5(6, 5)\nprint(result)\n\n# Example 5: direct call\nprint(exactly_one_above_5(4, 5))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5798,
    "title": "Problem 5798",
    "description": "Write a Python function called `flags_ready_1` that must return whether both readiness flags are true and the blocked flag is false for check 1. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  flags_ready_1(True, True, False) -> True\n  flags_ready_1(True, False, False) -> False",
    "initialCode": "def flags_ready_1(first, second, blocked):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flags_ready_1(first, second, blocked):\n    return first and second and not blocked\n\nprint(flags_ready_1(True, True, False))  # Expected: True\nprint(flags_ready_1(True, False, False))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5798(first, second, blocked):\n    def calculate():\n        return first and second and not blocked\n    return calculate()\n\nprint(solve_problem_5798(True, True, False))\n\n# Example 3: static method approach\nclass Problem5798Solution:\n    @staticmethod\n    def flags_ready_1(first, second, blocked):\n        return first and second and not blocked\n\nprint(Problem5798Solution.flags_ready_1(True, False, False))\n\n# Example 4: assigned result approach\nresult = flags_ready_1(True, True, False)\nprint(result)\n\n# Example 5: direct call\nprint(flags_ready_1(True, True, True))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5799,
    "title": "Problem 5799",
    "description": "Write a Python function called `flags_ready_2` that must return whether both readiness flags are true and the blocked flag is false for check 2. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  flags_ready_2(True, True, False) -> True\n  flags_ready_2(True, False, False) -> False",
    "initialCode": "def flags_ready_2(first, second, blocked):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flags_ready_2(first, second, blocked):\n    return first and second and not blocked\n\nprint(flags_ready_2(True, True, False))  # Expected: True\nprint(flags_ready_2(True, False, False))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5799(first, second, blocked):\n    def calculate():\n        return first and second and not blocked\n    return calculate()\n\nprint(solve_problem_5799(True, True, False))\n\n# Example 3: static method approach\nclass Problem5799Solution:\n    @staticmethod\n    def flags_ready_2(first, second, blocked):\n        return first and second and not blocked\n\nprint(Problem5799Solution.flags_ready_2(True, False, False))\n\n# Example 4: assigned result approach\nresult = flags_ready_2(True, True, False)\nprint(result)\n\n# Example 5: direct call\nprint(flags_ready_2(True, True, True))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5800,
    "title": "Problem 5800",
    "description": "Write a Python function called `flags_ready_3` that must return whether both readiness flags are true and the blocked flag is false for check 3. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  flags_ready_3(True, True, False) -> True\n  flags_ready_3(True, False, False) -> False",
    "initialCode": "def flags_ready_3(first, second, blocked):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flags_ready_3(first, second, blocked):\n    return first and second and not blocked\n\nprint(flags_ready_3(True, True, False))  # Expected: True\nprint(flags_ready_3(True, False, False))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5800(first, second, blocked):\n    def calculate():\n        return first and second and not blocked\n    return calculate()\n\nprint(solve_problem_5800(True, True, False))\n\n# Example 3: static method approach\nclass Problem5800Solution:\n    @staticmethod\n    def flags_ready_3(first, second, blocked):\n        return first and second and not blocked\n\nprint(Problem5800Solution.flags_ready_3(True, False, False))\n\n# Example 4: assigned result approach\nresult = flags_ready_3(True, True, False)\nprint(result)\n\n# Example 5: direct call\nprint(flags_ready_3(True, True, True))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5801,
    "title": "Problem 5801",
    "description": "Write a Python function called `flags_ready_4` that must return whether both readiness flags are true and the blocked flag is false for check 4. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  flags_ready_4(True, True, False) -> True\n  flags_ready_4(True, False, False) -> False",
    "initialCode": "def flags_ready_4(first, second, blocked):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flags_ready_4(first, second, blocked):\n    return first and second and not blocked\n\nprint(flags_ready_4(True, True, False))  # Expected: True\nprint(flags_ready_4(True, False, False))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5801(first, second, blocked):\n    def calculate():\n        return first and second and not blocked\n    return calculate()\n\nprint(solve_problem_5801(True, True, False))\n\n# Example 3: static method approach\nclass Problem5801Solution:\n    @staticmethod\n    def flags_ready_4(first, second, blocked):\n        return first and second and not blocked\n\nprint(Problem5801Solution.flags_ready_4(True, False, False))\n\n# Example 4: assigned result approach\nresult = flags_ready_4(True, True, False)\nprint(result)\n\n# Example 5: direct call\nprint(flags_ready_4(True, True, True))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5802,
    "title": "Problem 5802",
    "description": "Write a Python function called `flags_ready_5` that must return whether both readiness flags are true and the blocked flag is false for check 5. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  flags_ready_5(True, True, False) -> True\n  flags_ready_5(True, False, False) -> False",
    "initialCode": "def flags_ready_5(first, second, blocked):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flags_ready_5(first, second, blocked):\n    return first and second and not blocked\n\nprint(flags_ready_5(True, True, False))  # Expected: True\nprint(flags_ready_5(True, False, False))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5802(first, second, blocked):\n    def calculate():\n        return first and second and not blocked\n    return calculate()\n\nprint(solve_problem_5802(True, True, False))\n\n# Example 3: static method approach\nclass Problem5802Solution:\n    @staticmethod\n    def flags_ready_5(first, second, blocked):\n        return first and second and not blocked\n\nprint(Problem5802Solution.flags_ready_5(True, False, False))\n\n# Example 4: assigned result approach\nresult = flags_ready_5(True, True, False)\nprint(result)\n\n# Example 5: direct call\nprint(flags_ready_5(True, True, True))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5803,
    "title": "Problem 5803",
    "description": "Write a Python function called `score_band_1` that must return whether `score` lies from 10 through 30. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  score_band_1(10) -> True\n  score_band_1(31) -> False",
    "initialCode": "def score_band_1(score):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef score_band_1(score):\n    return score >= 10 and score <= 30\n\nprint(score_band_1(10))  # Expected: True\nprint(score_band_1(31))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5803(score):\n    def calculate():\n        return score >= 10 and score <= 30\n    return calculate()\n\nprint(solve_problem_5803(10))\n\n# Example 3: static method approach\nclass Problem5803Solution:\n    @staticmethod\n    def score_band_1(score):\n        return score >= 10 and score <= 30\n\nprint(Problem5803Solution.score_band_1(31))\n\n# Example 4: assigned result approach\nresult = score_band_1(10)\nprint(result)\n\n# Example 5: direct call\nprint(score_band_1(20))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5804,
    "title": "Problem 5804",
    "description": "Write a Python function called `score_band_2` that must return whether `score` lies from 20 through 40. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  score_band_2(20) -> True\n  score_band_2(41) -> False",
    "initialCode": "def score_band_2(score):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef score_band_2(score):\n    return score >= 20 and score <= 40\n\nprint(score_band_2(20))  # Expected: True\nprint(score_band_2(41))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5804(score):\n    def calculate():\n        return score >= 20 and score <= 40\n    return calculate()\n\nprint(solve_problem_5804(20))\n\n# Example 3: static method approach\nclass Problem5804Solution:\n    @staticmethod\n    def score_band_2(score):\n        return score >= 20 and score <= 40\n\nprint(Problem5804Solution.score_band_2(41))\n\n# Example 4: assigned result approach\nresult = score_band_2(20)\nprint(result)\n\n# Example 5: direct call\nprint(score_band_2(30))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5805,
    "title": "Problem 5805",
    "description": "Write a Python function called `score_band_3` that must return whether `score` lies from 30 through 50. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  score_band_3(30) -> True\n  score_band_3(51) -> False",
    "initialCode": "def score_band_3(score):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef score_band_3(score):\n    return score >= 30 and score <= 50\n\nprint(score_band_3(30))  # Expected: True\nprint(score_band_3(51))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5805(score):\n    def calculate():\n        return score >= 30 and score <= 50\n    return calculate()\n\nprint(solve_problem_5805(30))\n\n# Example 3: static method approach\nclass Problem5805Solution:\n    @staticmethod\n    def score_band_3(score):\n        return score >= 30 and score <= 50\n\nprint(Problem5805Solution.score_band_3(51))\n\n# Example 4: assigned result approach\nresult = score_band_3(30)\nprint(result)\n\n# Example 5: direct call\nprint(score_band_3(40))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5806,
    "title": "Problem 5806",
    "description": "Write a Python function called `score_band_4` that must return whether `score` lies from 40 through 60. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  score_band_4(40) -> True\n  score_band_4(61) -> False",
    "initialCode": "def score_band_4(score):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef score_band_4(score):\n    return score >= 40 and score <= 60\n\nprint(score_band_4(40))  # Expected: True\nprint(score_band_4(61))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5806(score):\n    def calculate():\n        return score >= 40 and score <= 60\n    return calculate()\n\nprint(solve_problem_5806(40))\n\n# Example 3: static method approach\nclass Problem5806Solution:\n    @staticmethod\n    def score_band_4(score):\n        return score >= 40 and score <= 60\n\nprint(Problem5806Solution.score_band_4(61))\n\n# Example 4: assigned result approach\nresult = score_band_4(40)\nprint(result)\n\n# Example 5: direct call\nprint(score_band_4(50))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5807,
    "title": "Problem 5807",
    "description": "Write a Python function called `score_band_5` that must return whether `score` lies from 50 through 70. Practice boolean logic syntax.\nDifficulty: Easy.\nExamples:\n  score_band_5(50) -> True\n  score_band_5(71) -> False",
    "initialCode": "def score_band_5(score):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef score_band_5(score):\n    return score >= 50 and score <= 70\n\nprint(score_band_5(50))  # Expected: True\nprint(score_band_5(71))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5807(score):\n    def calculate():\n        return score >= 50 and score <= 70\n    return calculate()\n\nprint(solve_problem_5807(50))\n\n# Example 3: static method approach\nclass Problem5807Solution:\n    @staticmethod\n    def score_band_5(score):\n        return score >= 50 and score <= 70\n\nprint(Problem5807Solution.score_band_5(71))\n\n# Example 4: assigned result approach\nresult = score_band_5(50)\nprint(result)\n\n# Example 5: direct call\nprint(score_band_5(60))",
    "hint": "Focus on the truth value of each comparison and the short-circuit order. Use the required boolean logic structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the boolean logic structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Boolean Logic Easy"
  },
  {
    "id": 5808,
    "title": "Problem 5808",
    "description": "Write a Python function called `length_plus_1_builtin` that must use the built-in `len()` and add 1 to the length. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  length_plus_1_builtin([1, 2, 3]) -> 4\n  length_plus_1_builtin([]) -> 1",
    "initialCode": "def length_plus_1_builtin(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef length_plus_1_builtin(items):\n    return len(items) + 1\n\nprint(length_plus_1_builtin([1, 2, 3]))  # Expected: 4\nprint(length_plus_1_builtin([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5808(items):\n    def calculate():\n        return len(items) + 1\n    return calculate()\n\nprint(solve_problem_5808([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5808Solution:\n    @staticmethod\n    def length_plus_1_builtin(items):\n        return len(items) + 1\n\nprint(Problem5808Solution.length_plus_1_builtin([]))\n\n# Example 4: assigned result approach\nresult = length_plus_1_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(length_plus_1_builtin(\"code\"))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5809,
    "title": "Problem 5809",
    "description": "Write a Python function called `length_plus_2_builtin` that must use the built-in `len()` and add 2 to the length. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  length_plus_2_builtin([1, 2, 3]) -> 5\n  length_plus_2_builtin([]) -> 2",
    "initialCode": "def length_plus_2_builtin(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef length_plus_2_builtin(items):\n    return len(items) + 2\n\nprint(length_plus_2_builtin([1, 2, 3]))  # Expected: 5\nprint(length_plus_2_builtin([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_5809(items):\n    def calculate():\n        return len(items) + 2\n    return calculate()\n\nprint(solve_problem_5809([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5809Solution:\n    @staticmethod\n    def length_plus_2_builtin(items):\n        return len(items) + 2\n\nprint(Problem5809Solution.length_plus_2_builtin([]))\n\n# Example 4: assigned result approach\nresult = length_plus_2_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(length_plus_2_builtin(\"code\"))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5810,
    "title": "Problem 5810",
    "description": "Write a Python function called `length_plus_3_builtin` that must use the built-in `len()` and add 3 to the length. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  length_plus_3_builtin([1, 2, 3]) -> 6\n  length_plus_3_builtin([]) -> 3",
    "initialCode": "def length_plus_3_builtin(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef length_plus_3_builtin(items):\n    return len(items) + 3\n\nprint(length_plus_3_builtin([1, 2, 3]))  # Expected: 6\nprint(length_plus_3_builtin([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_5810(items):\n    def calculate():\n        return len(items) + 3\n    return calculate()\n\nprint(solve_problem_5810([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5810Solution:\n    @staticmethod\n    def length_plus_3_builtin(items):\n        return len(items) + 3\n\nprint(Problem5810Solution.length_plus_3_builtin([]))\n\n# Example 4: assigned result approach\nresult = length_plus_3_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(length_plus_3_builtin(\"code\"))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5811,
    "title": "Problem 5811",
    "description": "Write a Python function called `length_plus_4_builtin` that must use the built-in `len()` and add 4 to the length. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  length_plus_4_builtin([1, 2, 3]) -> 7\n  length_plus_4_builtin([]) -> 4",
    "initialCode": "def length_plus_4_builtin(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef length_plus_4_builtin(items):\n    return len(items) + 4\n\nprint(length_plus_4_builtin([1, 2, 3]))  # Expected: 7\nprint(length_plus_4_builtin([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5811(items):\n    def calculate():\n        return len(items) + 4\n    return calculate()\n\nprint(solve_problem_5811([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5811Solution:\n    @staticmethod\n    def length_plus_4_builtin(items):\n        return len(items) + 4\n\nprint(Problem5811Solution.length_plus_4_builtin([]))\n\n# Example 4: assigned result approach\nresult = length_plus_4_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(length_plus_4_builtin(\"code\"))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5812,
    "title": "Problem 5812",
    "description": "Write a Python function called `length_plus_5_builtin` that must use the built-in `len()` and add 5 to the length. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  length_plus_5_builtin([1, 2, 3]) -> 8\n  length_plus_5_builtin([]) -> 5",
    "initialCode": "def length_plus_5_builtin(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef length_plus_5_builtin(items):\n    return len(items) + 5\n\nprint(length_plus_5_builtin([1, 2, 3]))  # Expected: 8\nprint(length_plus_5_builtin([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5812(items):\n    def calculate():\n        return len(items) + 5\n    return calculate()\n\nprint(solve_problem_5812([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5812Solution:\n    @staticmethod\n    def length_plus_5_builtin(items):\n        return len(items) + 5\n\nprint(Problem5812Solution.length_plus_5_builtin([]))\n\n# Example 4: assigned result approach\nresult = length_plus_5_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(length_plus_5_builtin(\"code\"))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5813,
    "title": "Problem 5813",
    "description": "Write a Python function called `sum_plus_1_builtin` that must use the built-in `sum()` and add 1 to the total. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_1_builtin([1, 2, 3]) -> 7\n  sum_plus_1_builtin([-2, 5]) -> 4",
    "initialCode": "def sum_plus_1_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_1_builtin(values):\n    return sum(values) + 1\n\nprint(sum_plus_1_builtin([1, 2, 3]))  # Expected: 7\nprint(sum_plus_1_builtin([-2, 5]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5813(values):\n    def calculate():\n        return sum(values) + 1\n    return calculate()\n\nprint(solve_problem_5813([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5813Solution:\n    @staticmethod\n    def sum_plus_1_builtin(values):\n        return sum(values) + 1\n\nprint(Problem5813Solution.sum_plus_1_builtin([-2, 5]))\n\n# Example 4: assigned result approach\nresult = sum_plus_1_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_1_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5814,
    "title": "Problem 5814",
    "description": "Write a Python function called `sum_plus_2_builtin` that must use the built-in `sum()` and add 2 to the total. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_2_builtin([1, 2, 3]) -> 8\n  sum_plus_2_builtin([-2, 5]) -> 5",
    "initialCode": "def sum_plus_2_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_2_builtin(values):\n    return sum(values) + 2\n\nprint(sum_plus_2_builtin([1, 2, 3]))  # Expected: 8\nprint(sum_plus_2_builtin([-2, 5]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5814(values):\n    def calculate():\n        return sum(values) + 2\n    return calculate()\n\nprint(solve_problem_5814([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5814Solution:\n    @staticmethod\n    def sum_plus_2_builtin(values):\n        return sum(values) + 2\n\nprint(Problem5814Solution.sum_plus_2_builtin([-2, 5]))\n\n# Example 4: assigned result approach\nresult = sum_plus_2_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_2_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5815,
    "title": "Problem 5815",
    "description": "Write a Python function called `sum_plus_3_builtin` that must use the built-in `sum()` and add 3 to the total. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_3_builtin([1, 2, 3]) -> 9\n  sum_plus_3_builtin([-2, 5]) -> 6",
    "initialCode": "def sum_plus_3_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_3_builtin(values):\n    return sum(values) + 3\n\nprint(sum_plus_3_builtin([1, 2, 3]))  # Expected: 9\nprint(sum_plus_3_builtin([-2, 5]))  # Expected: 6\n\n# Example 2: nested helper approach\ndef solve_problem_5815(values):\n    def calculate():\n        return sum(values) + 3\n    return calculate()\n\nprint(solve_problem_5815([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5815Solution:\n    @staticmethod\n    def sum_plus_3_builtin(values):\n        return sum(values) + 3\n\nprint(Problem5815Solution.sum_plus_3_builtin([-2, 5]))\n\n# Example 4: assigned result approach\nresult = sum_plus_3_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_3_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5816,
    "title": "Problem 5816",
    "description": "Write a Python function called `sum_plus_4_builtin` that must use the built-in `sum()` and add 4 to the total. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_4_builtin([1, 2, 3]) -> 10\n  sum_plus_4_builtin([-2, 5]) -> 7",
    "initialCode": "def sum_plus_4_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_4_builtin(values):\n    return sum(values) + 4\n\nprint(sum_plus_4_builtin([1, 2, 3]))  # Expected: 10\nprint(sum_plus_4_builtin([-2, 5]))  # Expected: 7\n\n# Example 2: nested helper approach\ndef solve_problem_5816(values):\n    def calculate():\n        return sum(values) + 4\n    return calculate()\n\nprint(solve_problem_5816([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5816Solution:\n    @staticmethod\n    def sum_plus_4_builtin(values):\n        return sum(values) + 4\n\nprint(Problem5816Solution.sum_plus_4_builtin([-2, 5]))\n\n# Example 4: assigned result approach\nresult = sum_plus_4_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_4_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5817,
    "title": "Problem 5817",
    "description": "Write a Python function called `sum_plus_5_builtin` that must use the built-in `sum()` and add 5 to the total. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_5_builtin([1, 2, 3]) -> 11\n  sum_plus_5_builtin([-2, 5]) -> 8",
    "initialCode": "def sum_plus_5_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_5_builtin(values):\n    return sum(values) + 5\n\nprint(sum_plus_5_builtin([1, 2, 3]))  # Expected: 11\nprint(sum_plus_5_builtin([-2, 5]))  # Expected: 8\n\n# Example 2: nested helper approach\ndef solve_problem_5817(values):\n    def calculate():\n        return sum(values) + 5\n    return calculate()\n\nprint(solve_problem_5817([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5817Solution:\n    @staticmethod\n    def sum_plus_5_builtin(values):\n        return sum(values) + 5\n\nprint(Problem5817Solution.sum_plus_5_builtin([-2, 5]))\n\n# Example 4: assigned result approach\nresult = sum_plus_5_builtin([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_5_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5818,
    "title": "Problem 5818",
    "description": "Write a Python function called `safe_max_1_builtin` that must use the built-in `max()` with default 1 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_max_1_builtin([1, 8, 3]) -> 8\n  safe_max_1_builtin([]) -> 1",
    "initialCode": "def safe_max_1_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_max_1_builtin(values):\n    return max(values, default=1)\n\nprint(safe_max_1_builtin([1, 8, 3]))  # Expected: 8\nprint(safe_max_1_builtin([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5818(values):\n    def calculate():\n        return max(values, default=1)\n    return calculate()\n\nprint(solve_problem_5818([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5818Solution:\n    @staticmethod\n    def safe_max_1_builtin(values):\n        return max(values, default=1)\n\nprint(Problem5818Solution.safe_max_1_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_max_1_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_max_1_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5819,
    "title": "Problem 5819",
    "description": "Write a Python function called `safe_max_2_builtin` that must use the built-in `max()` with default 2 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_max_2_builtin([1, 8, 3]) -> 8\n  safe_max_2_builtin([]) -> 2",
    "initialCode": "def safe_max_2_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_max_2_builtin(values):\n    return max(values, default=2)\n\nprint(safe_max_2_builtin([1, 8, 3]))  # Expected: 8\nprint(safe_max_2_builtin([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_5819(values):\n    def calculate():\n        return max(values, default=2)\n    return calculate()\n\nprint(solve_problem_5819([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5819Solution:\n    @staticmethod\n    def safe_max_2_builtin(values):\n        return max(values, default=2)\n\nprint(Problem5819Solution.safe_max_2_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_max_2_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_max_2_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5820,
    "title": "Problem 5820",
    "description": "Write a Python function called `safe_max_3_builtin` that must use the built-in `max()` with default 3 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_max_3_builtin([1, 8, 3]) -> 8\n  safe_max_3_builtin([]) -> 3",
    "initialCode": "def safe_max_3_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_max_3_builtin(values):\n    return max(values, default=3)\n\nprint(safe_max_3_builtin([1, 8, 3]))  # Expected: 8\nprint(safe_max_3_builtin([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_5820(values):\n    def calculate():\n        return max(values, default=3)\n    return calculate()\n\nprint(solve_problem_5820([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5820Solution:\n    @staticmethod\n    def safe_max_3_builtin(values):\n        return max(values, default=3)\n\nprint(Problem5820Solution.safe_max_3_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_max_3_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_max_3_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5821,
    "title": "Problem 5821",
    "description": "Write a Python function called `safe_max_4_builtin` that must use the built-in `max()` with default 4 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_max_4_builtin([1, 8, 3]) -> 8\n  safe_max_4_builtin([]) -> 4",
    "initialCode": "def safe_max_4_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_max_4_builtin(values):\n    return max(values, default=4)\n\nprint(safe_max_4_builtin([1, 8, 3]))  # Expected: 8\nprint(safe_max_4_builtin([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5821(values):\n    def calculate():\n        return max(values, default=4)\n    return calculate()\n\nprint(solve_problem_5821([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5821Solution:\n    @staticmethod\n    def safe_max_4_builtin(values):\n        return max(values, default=4)\n\nprint(Problem5821Solution.safe_max_4_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_max_4_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_max_4_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5822,
    "title": "Problem 5822",
    "description": "Write a Python function called `safe_max_5_builtin` that must use the built-in `max()` with default 5 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_max_5_builtin([1, 8, 3]) -> 8\n  safe_max_5_builtin([]) -> 5",
    "initialCode": "def safe_max_5_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_max_5_builtin(values):\n    return max(values, default=5)\n\nprint(safe_max_5_builtin([1, 8, 3]))  # Expected: 8\nprint(safe_max_5_builtin([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5822(values):\n    def calculate():\n        return max(values, default=5)\n    return calculate()\n\nprint(solve_problem_5822([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5822Solution:\n    @staticmethod\n    def safe_max_5_builtin(values):\n        return max(values, default=5)\n\nprint(Problem5822Solution.safe_max_5_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_max_5_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_max_5_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5823,
    "title": "Problem 5823",
    "description": "Write a Python function called `safe_min_1_builtin` that must use the built-in `min()` with default -1 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_min_1_builtin([1, 8, 3]) -> 1\n  safe_min_1_builtin([]) -> -1",
    "initialCode": "def safe_min_1_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_min_1_builtin(values):\n    return min(values, default=-1)\n\nprint(safe_min_1_builtin([1, 8, 3]))  # Expected: 1\nprint(safe_min_1_builtin([]))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5823(values):\n    def calculate():\n        return min(values, default=-1)\n    return calculate()\n\nprint(solve_problem_5823([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5823Solution:\n    @staticmethod\n    def safe_min_1_builtin(values):\n        return min(values, default=-1)\n\nprint(Problem5823Solution.safe_min_1_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_min_1_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_min_1_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5824,
    "title": "Problem 5824",
    "description": "Write a Python function called `safe_min_2_builtin` that must use the built-in `min()` with default -2 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_min_2_builtin([1, 8, 3]) -> 1\n  safe_min_2_builtin([]) -> -2",
    "initialCode": "def safe_min_2_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_min_2_builtin(values):\n    return min(values, default=-2)\n\nprint(safe_min_2_builtin([1, 8, 3]))  # Expected: 1\nprint(safe_min_2_builtin([]))  # Expected: -2\n\n# Example 2: nested helper approach\ndef solve_problem_5824(values):\n    def calculate():\n        return min(values, default=-2)\n    return calculate()\n\nprint(solve_problem_5824([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5824Solution:\n    @staticmethod\n    def safe_min_2_builtin(values):\n        return min(values, default=-2)\n\nprint(Problem5824Solution.safe_min_2_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_min_2_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_min_2_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5825,
    "title": "Problem 5825",
    "description": "Write a Python function called `safe_min_3_builtin` that must use the built-in `min()` with default -3 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_min_3_builtin([1, 8, 3]) -> 1\n  safe_min_3_builtin([]) -> -3",
    "initialCode": "def safe_min_3_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_min_3_builtin(values):\n    return min(values, default=-3)\n\nprint(safe_min_3_builtin([1, 8, 3]))  # Expected: 1\nprint(safe_min_3_builtin([]))  # Expected: -3\n\n# Example 2: nested helper approach\ndef solve_problem_5825(values):\n    def calculate():\n        return min(values, default=-3)\n    return calculate()\n\nprint(solve_problem_5825([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5825Solution:\n    @staticmethod\n    def safe_min_3_builtin(values):\n        return min(values, default=-3)\n\nprint(Problem5825Solution.safe_min_3_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_min_3_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_min_3_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5826,
    "title": "Problem 5826",
    "description": "Write a Python function called `safe_min_4_builtin` that must use the built-in `min()` with default -4 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_min_4_builtin([1, 8, 3]) -> 1\n  safe_min_4_builtin([]) -> -4",
    "initialCode": "def safe_min_4_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_min_4_builtin(values):\n    return min(values, default=-4)\n\nprint(safe_min_4_builtin([1, 8, 3]))  # Expected: 1\nprint(safe_min_4_builtin([]))  # Expected: -4\n\n# Example 2: nested helper approach\ndef solve_problem_5826(values):\n    def calculate():\n        return min(values, default=-4)\n    return calculate()\n\nprint(solve_problem_5826([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5826Solution:\n    @staticmethod\n    def safe_min_4_builtin(values):\n        return min(values, default=-4)\n\nprint(Problem5826Solution.safe_min_4_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_min_4_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_min_4_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5827,
    "title": "Problem 5827",
    "description": "Write a Python function called `safe_min_5_builtin` that must use the built-in `min()` with default -5 for an empty list. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  safe_min_5_builtin([1, 8, 3]) -> 1\n  safe_min_5_builtin([]) -> -5",
    "initialCode": "def safe_min_5_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_min_5_builtin(values):\n    return min(values, default=-5)\n\nprint(safe_min_5_builtin([1, 8, 3]))  # Expected: 1\nprint(safe_min_5_builtin([]))  # Expected: -5\n\n# Example 2: nested helper approach\ndef solve_problem_5827(values):\n    def calculate():\n        return min(values, default=-5)\n    return calculate()\n\nprint(solve_problem_5827([1, 8, 3]))\n\n# Example 3: static method approach\nclass Problem5827Solution:\n    @staticmethod\n    def safe_min_5_builtin(values):\n        return min(values, default=-5)\n\nprint(Problem5827Solution.safe_min_5_builtin([]))\n\n# Example 4: assigned result approach\nresult = safe_min_5_builtin([1, 8, 3])\nprint(result)\n\n# Example 5: direct call\nprint(safe_min_5_builtin([-5, -2]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5828,
    "title": "Problem 5828",
    "description": "Write a Python function called `descending_marker_1_builtin` that must use the built-in `sorted()` to sort descending, then append 1. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  descending_marker_1_builtin([3, 1, 2]) -> [3, 2, 1, 1]\n  descending_marker_1_builtin([]) -> [1]",
    "initialCode": "def descending_marker_1_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef descending_marker_1_builtin(values):\n    return sorted(values, reverse=True) + [1]\n\nprint(descending_marker_1_builtin([3, 1, 2]))  # Expected: [3, 2, 1, 1]\nprint(descending_marker_1_builtin([]))  # Expected: [1]\n\n# Example 2: nested helper approach\ndef solve_problem_5828(values):\n    def calculate():\n        return sorted(values, reverse=True) + [1]\n    return calculate()\n\nprint(solve_problem_5828([3, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5828Solution:\n    @staticmethod\n    def descending_marker_1_builtin(values):\n        return sorted(values, reverse=True) + [1]\n\nprint(Problem5828Solution.descending_marker_1_builtin([]))\n\n# Example 4: assigned result approach\nresult = descending_marker_1_builtin([3, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(descending_marker_1_builtin([-1, 4]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5829,
    "title": "Problem 5829",
    "description": "Write a Python function called `descending_marker_2_builtin` that must use the built-in `sorted()` to sort descending, then append 2. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  descending_marker_2_builtin([3, 1, 2]) -> [3, 2, 1, 2]\n  descending_marker_2_builtin([]) -> [2]",
    "initialCode": "def descending_marker_2_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef descending_marker_2_builtin(values):\n    return sorted(values, reverse=True) + [2]\n\nprint(descending_marker_2_builtin([3, 1, 2]))  # Expected: [3, 2, 1, 2]\nprint(descending_marker_2_builtin([]))  # Expected: [2]\n\n# Example 2: nested helper approach\ndef solve_problem_5829(values):\n    def calculate():\n        return sorted(values, reverse=True) + [2]\n    return calculate()\n\nprint(solve_problem_5829([3, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5829Solution:\n    @staticmethod\n    def descending_marker_2_builtin(values):\n        return sorted(values, reverse=True) + [2]\n\nprint(Problem5829Solution.descending_marker_2_builtin([]))\n\n# Example 4: assigned result approach\nresult = descending_marker_2_builtin([3, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(descending_marker_2_builtin([-1, 4]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5830,
    "title": "Problem 5830",
    "description": "Write a Python function called `descending_marker_3_builtin` that must use the built-in `sorted()` to sort descending, then append 3. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  descending_marker_3_builtin([3, 1, 2]) -> [3, 2, 1, 3]\n  descending_marker_3_builtin([]) -> [3]",
    "initialCode": "def descending_marker_3_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef descending_marker_3_builtin(values):\n    return sorted(values, reverse=True) + [3]\n\nprint(descending_marker_3_builtin([3, 1, 2]))  # Expected: [3, 2, 1, 3]\nprint(descending_marker_3_builtin([]))  # Expected: [3]\n\n# Example 2: nested helper approach\ndef solve_problem_5830(values):\n    def calculate():\n        return sorted(values, reverse=True) + [3]\n    return calculate()\n\nprint(solve_problem_5830([3, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5830Solution:\n    @staticmethod\n    def descending_marker_3_builtin(values):\n        return sorted(values, reverse=True) + [3]\n\nprint(Problem5830Solution.descending_marker_3_builtin([]))\n\n# Example 4: assigned result approach\nresult = descending_marker_3_builtin([3, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(descending_marker_3_builtin([-1, 4]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5831,
    "title": "Problem 5831",
    "description": "Write a Python function called `descending_marker_4_builtin` that must use the built-in `sorted()` to sort descending, then append 4. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  descending_marker_4_builtin([3, 1, 2]) -> [3, 2, 1, 4]\n  descending_marker_4_builtin([]) -> [4]",
    "initialCode": "def descending_marker_4_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef descending_marker_4_builtin(values):\n    return sorted(values, reverse=True) + [4]\n\nprint(descending_marker_4_builtin([3, 1, 2]))  # Expected: [3, 2, 1, 4]\nprint(descending_marker_4_builtin([]))  # Expected: [4]\n\n# Example 2: nested helper approach\ndef solve_problem_5831(values):\n    def calculate():\n        return sorted(values, reverse=True) + [4]\n    return calculate()\n\nprint(solve_problem_5831([3, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5831Solution:\n    @staticmethod\n    def descending_marker_4_builtin(values):\n        return sorted(values, reverse=True) + [4]\n\nprint(Problem5831Solution.descending_marker_4_builtin([]))\n\n# Example 4: assigned result approach\nresult = descending_marker_4_builtin([3, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(descending_marker_4_builtin([-1, 4]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5832,
    "title": "Problem 5832",
    "description": "Write a Python function called `descending_marker_5_builtin` that must use the built-in `sorted()` to sort descending, then append 5. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  descending_marker_5_builtin([3, 1, 2]) -> [3, 2, 1, 5]\n  descending_marker_5_builtin([]) -> [5]",
    "initialCode": "def descending_marker_5_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef descending_marker_5_builtin(values):\n    return sorted(values, reverse=True) + [5]\n\nprint(descending_marker_5_builtin([3, 1, 2]))  # Expected: [3, 2, 1, 5]\nprint(descending_marker_5_builtin([]))  # Expected: [5]\n\n# Example 2: nested helper approach\ndef solve_problem_5832(values):\n    def calculate():\n        return sorted(values, reverse=True) + [5]\n    return calculate()\n\nprint(solve_problem_5832([3, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5832Solution:\n    @staticmethod\n    def descending_marker_5_builtin(values):\n        return sorted(values, reverse=True) + [5]\n\nprint(Problem5832Solution.descending_marker_5_builtin([]))\n\n# Example 4: assigned result approach\nresult = descending_marker_5_builtin([3, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(descending_marker_5_builtin([-1, 4]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5833,
    "title": "Problem 5833",
    "description": "Write a Python function called `round_to_1_builtin` that must use the built-in `round()` to keep 1 decimal places. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  round_to_1_builtin(3.1415926) -> 3.1\n  round_to_1_builtin(2.555555) -> 2.6",
    "initialCode": "def round_to_1_builtin(number):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef round_to_1_builtin(number):\n    return round(number, 1)\n\nprint(round_to_1_builtin(3.1415926))  # Expected: 3.1\nprint(round_to_1_builtin(2.555555))  # Expected: 2.6\n\n# Example 2: nested helper approach\ndef solve_problem_5833(number):\n    def calculate():\n        return round(number, 1)\n    return calculate()\n\nprint(solve_problem_5833(3.1415926))\n\n# Example 3: static method approach\nclass Problem5833Solution:\n    @staticmethod\n    def round_to_1_builtin(number):\n        return round(number, 1)\n\nprint(Problem5833Solution.round_to_1_builtin(2.555555))\n\n# Example 4: assigned result approach\nresult = round_to_1_builtin(3.1415926)\nprint(result)\n\n# Example 5: direct call\nprint(round_to_1_builtin(-1.234567))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5834,
    "title": "Problem 5834",
    "description": "Write a Python function called `round_to_2_builtin` that must use the built-in `round()` to keep 2 decimal places. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  round_to_2_builtin(3.1415926) -> 3.14\n  round_to_2_builtin(2.555555) -> 2.56",
    "initialCode": "def round_to_2_builtin(number):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef round_to_2_builtin(number):\n    return round(number, 2)\n\nprint(round_to_2_builtin(3.1415926))  # Expected: 3.14\nprint(round_to_2_builtin(2.555555))  # Expected: 2.56\n\n# Example 2: nested helper approach\ndef solve_problem_5834(number):\n    def calculate():\n        return round(number, 2)\n    return calculate()\n\nprint(solve_problem_5834(3.1415926))\n\n# Example 3: static method approach\nclass Problem5834Solution:\n    @staticmethod\n    def round_to_2_builtin(number):\n        return round(number, 2)\n\nprint(Problem5834Solution.round_to_2_builtin(2.555555))\n\n# Example 4: assigned result approach\nresult = round_to_2_builtin(3.1415926)\nprint(result)\n\n# Example 5: direct call\nprint(round_to_2_builtin(-1.234567))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5835,
    "title": "Problem 5835",
    "description": "Write a Python function called `round_to_3_builtin` that must use the built-in `round()` to keep 3 decimal places. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  round_to_3_builtin(3.1415926) -> 3.142\n  round_to_3_builtin(2.555555) -> 2.556",
    "initialCode": "def round_to_3_builtin(number):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef round_to_3_builtin(number):\n    return round(number, 3)\n\nprint(round_to_3_builtin(3.1415926))  # Expected: 3.142\nprint(round_to_3_builtin(2.555555))  # Expected: 2.556\n\n# Example 2: nested helper approach\ndef solve_problem_5835(number):\n    def calculate():\n        return round(number, 3)\n    return calculate()\n\nprint(solve_problem_5835(3.1415926))\n\n# Example 3: static method approach\nclass Problem5835Solution:\n    @staticmethod\n    def round_to_3_builtin(number):\n        return round(number, 3)\n\nprint(Problem5835Solution.round_to_3_builtin(2.555555))\n\n# Example 4: assigned result approach\nresult = round_to_3_builtin(3.1415926)\nprint(result)\n\n# Example 5: direct call\nprint(round_to_3_builtin(-1.234567))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5836,
    "title": "Problem 5836",
    "description": "Write a Python function called `round_to_4_builtin` that must use the built-in `round()` to keep 4 decimal places. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  round_to_4_builtin(3.1415926) -> 3.1416\n  round_to_4_builtin(2.555555) -> 2.5556",
    "initialCode": "def round_to_4_builtin(number):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef round_to_4_builtin(number):\n    return round(number, 4)\n\nprint(round_to_4_builtin(3.1415926))  # Expected: 3.1416\nprint(round_to_4_builtin(2.555555))  # Expected: 2.5556\n\n# Example 2: nested helper approach\ndef solve_problem_5836(number):\n    def calculate():\n        return round(number, 4)\n    return calculate()\n\nprint(solve_problem_5836(3.1415926))\n\n# Example 3: static method approach\nclass Problem5836Solution:\n    @staticmethod\n    def round_to_4_builtin(number):\n        return round(number, 4)\n\nprint(Problem5836Solution.round_to_4_builtin(2.555555))\n\n# Example 4: assigned result approach\nresult = round_to_4_builtin(3.1415926)\nprint(result)\n\n# Example 5: direct call\nprint(round_to_4_builtin(-1.234567))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5837,
    "title": "Problem 5837",
    "description": "Write a Python function called `round_to_5_builtin` that must use the built-in `round()` to keep 5 decimal places. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  round_to_5_builtin(3.1415926) -> 3.14159\n  round_to_5_builtin(2.555555) -> 2.55556",
    "initialCode": "def round_to_5_builtin(number):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef round_to_5_builtin(number):\n    return round(number, 5)\n\nprint(round_to_5_builtin(3.1415926))  # Expected: 3.14159\nprint(round_to_5_builtin(2.555555))  # Expected: 2.55556\n\n# Example 2: nested helper approach\ndef solve_problem_5837(number):\n    def calculate():\n        return round(number, 5)\n    return calculate()\n\nprint(solve_problem_5837(3.1415926))\n\n# Example 3: static method approach\nclass Problem5837Solution:\n    @staticmethod\n    def round_to_5_builtin(number):\n        return round(number, 5)\n\nprint(Problem5837Solution.round_to_5_builtin(2.555555))\n\n# Example 4: assigned result approach\nresult = round_to_5_builtin(3.1415926)\nprint(result)\n\n# Example 5: direct call\nprint(round_to_5_builtin(-1.234567))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5838,
    "title": "Problem 5838",
    "description": "Write a Python function called `distance_from_1_builtin` that must use the built-in `abs()` to measure distance from 1. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  distance_from_1_builtin(10) -> 9\n  distance_from_1_builtin(-3) -> 4",
    "initialCode": "def distance_from_1_builtin(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef distance_from_1_builtin(value):\n    return abs(value - 1)\n\nprint(distance_from_1_builtin(10))  # Expected: 9\nprint(distance_from_1_builtin(-3))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5838(value):\n    def calculate():\n        return abs(value - 1)\n    return calculate()\n\nprint(solve_problem_5838(10))\n\n# Example 3: static method approach\nclass Problem5838Solution:\n    @staticmethod\n    def distance_from_1_builtin(value):\n        return abs(value - 1)\n\nprint(Problem5838Solution.distance_from_1_builtin(-3))\n\n# Example 4: assigned result approach\nresult = distance_from_1_builtin(10)\nprint(result)\n\n# Example 5: direct call\nprint(distance_from_1_builtin(1))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5839,
    "title": "Problem 5839",
    "description": "Write a Python function called `distance_from_2_builtin` that must use the built-in `abs()` to measure distance from 2. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  distance_from_2_builtin(10) -> 8\n  distance_from_2_builtin(-3) -> 5",
    "initialCode": "def distance_from_2_builtin(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef distance_from_2_builtin(value):\n    return abs(value - 2)\n\nprint(distance_from_2_builtin(10))  # Expected: 8\nprint(distance_from_2_builtin(-3))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5839(value):\n    def calculate():\n        return abs(value - 2)\n    return calculate()\n\nprint(solve_problem_5839(10))\n\n# Example 3: static method approach\nclass Problem5839Solution:\n    @staticmethod\n    def distance_from_2_builtin(value):\n        return abs(value - 2)\n\nprint(Problem5839Solution.distance_from_2_builtin(-3))\n\n# Example 4: assigned result approach\nresult = distance_from_2_builtin(10)\nprint(result)\n\n# Example 5: direct call\nprint(distance_from_2_builtin(2))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5840,
    "title": "Problem 5840",
    "description": "Write a Python function called `distance_from_3_builtin` that must use the built-in `abs()` to measure distance from 3. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  distance_from_3_builtin(10) -> 7\n  distance_from_3_builtin(-3) -> 6",
    "initialCode": "def distance_from_3_builtin(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef distance_from_3_builtin(value):\n    return abs(value - 3)\n\nprint(distance_from_3_builtin(10))  # Expected: 7\nprint(distance_from_3_builtin(-3))  # Expected: 6\n\n# Example 2: nested helper approach\ndef solve_problem_5840(value):\n    def calculate():\n        return abs(value - 3)\n    return calculate()\n\nprint(solve_problem_5840(10))\n\n# Example 3: static method approach\nclass Problem5840Solution:\n    @staticmethod\n    def distance_from_3_builtin(value):\n        return abs(value - 3)\n\nprint(Problem5840Solution.distance_from_3_builtin(-3))\n\n# Example 4: assigned result approach\nresult = distance_from_3_builtin(10)\nprint(result)\n\n# Example 5: direct call\nprint(distance_from_3_builtin(3))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5841,
    "title": "Problem 5841",
    "description": "Write a Python function called `distance_from_4_builtin` that must use the built-in `abs()` to measure distance from 4. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  distance_from_4_builtin(10) -> 6\n  distance_from_4_builtin(-3) -> 7",
    "initialCode": "def distance_from_4_builtin(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef distance_from_4_builtin(value):\n    return abs(value - 4)\n\nprint(distance_from_4_builtin(10))  # Expected: 6\nprint(distance_from_4_builtin(-3))  # Expected: 7\n\n# Example 2: nested helper approach\ndef solve_problem_5841(value):\n    def calculate():\n        return abs(value - 4)\n    return calculate()\n\nprint(solve_problem_5841(10))\n\n# Example 3: static method approach\nclass Problem5841Solution:\n    @staticmethod\n    def distance_from_4_builtin(value):\n        return abs(value - 4)\n\nprint(Problem5841Solution.distance_from_4_builtin(-3))\n\n# Example 4: assigned result approach\nresult = distance_from_4_builtin(10)\nprint(result)\n\n# Example 5: direct call\nprint(distance_from_4_builtin(4))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5842,
    "title": "Problem 5842",
    "description": "Write a Python function called `distance_from_5_builtin` that must use the built-in `abs()` to measure distance from 5. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  distance_from_5_builtin(10) -> 5\n  distance_from_5_builtin(-3) -> 8",
    "initialCode": "def distance_from_5_builtin(value):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef distance_from_5_builtin(value):\n    return abs(value - 5)\n\nprint(distance_from_5_builtin(10))  # Expected: 5\nprint(distance_from_5_builtin(-3))  # Expected: 8\n\n# Example 2: nested helper approach\ndef solve_problem_5842(value):\n    def calculate():\n        return abs(value - 5)\n    return calculate()\n\nprint(solve_problem_5842(10))\n\n# Example 3: static method approach\nclass Problem5842Solution:\n    @staticmethod\n    def distance_from_5_builtin(value):\n        return abs(value - 5)\n\nprint(Problem5842Solution.distance_from_5_builtin(-3))\n\n# Example 4: assigned result approach\nresult = distance_from_5_builtin(10)\nprint(result)\n\n# Example 5: direct call\nprint(distance_from_5_builtin(5))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5843,
    "title": "Problem 5843",
    "description": "Write a Python function called `any_above_1_builtin` that must use the built-in `any()` to test whether one value exceeds 1. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  any_above_1_builtin([0, 2]) -> True\n  any_above_1_builtin([1, 0]) -> False",
    "initialCode": "def any_above_1_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef any_above_1_builtin(values):\n    return any(value > 1 for value in values)\n\nprint(any_above_1_builtin([0, 2]))  # Expected: True\nprint(any_above_1_builtin([1, 0]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5843(values):\n    def calculate():\n        return any(value > 1 for value in values)\n    return calculate()\n\nprint(solve_problem_5843([0, 2]))\n\n# Example 3: static method approach\nclass Problem5843Solution:\n    @staticmethod\n    def any_above_1_builtin(values):\n        return any(value > 1 for value in values)\n\nprint(Problem5843Solution.any_above_1_builtin([1, 0]))\n\n# Example 4: assigned result approach\nresult = any_above_1_builtin([0, 2])\nprint(result)\n\n# Example 5: direct call\nprint(any_above_1_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5844,
    "title": "Problem 5844",
    "description": "Write a Python function called `any_above_2_builtin` that must use the built-in `any()` to test whether one value exceeds 2. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  any_above_2_builtin([0, 3]) -> True\n  any_above_2_builtin([2, 1]) -> False",
    "initialCode": "def any_above_2_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef any_above_2_builtin(values):\n    return any(value > 2 for value in values)\n\nprint(any_above_2_builtin([0, 3]))  # Expected: True\nprint(any_above_2_builtin([2, 1]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5844(values):\n    def calculate():\n        return any(value > 2 for value in values)\n    return calculate()\n\nprint(solve_problem_5844([0, 3]))\n\n# Example 3: static method approach\nclass Problem5844Solution:\n    @staticmethod\n    def any_above_2_builtin(values):\n        return any(value > 2 for value in values)\n\nprint(Problem5844Solution.any_above_2_builtin([2, 1]))\n\n# Example 4: assigned result approach\nresult = any_above_2_builtin([0, 3])\nprint(result)\n\n# Example 5: direct call\nprint(any_above_2_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5845,
    "title": "Problem 5845",
    "description": "Write a Python function called `any_above_3_builtin` that must use the built-in `any()` to test whether one value exceeds 3. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  any_above_3_builtin([0, 4]) -> True\n  any_above_3_builtin([3, 2]) -> False",
    "initialCode": "def any_above_3_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef any_above_3_builtin(values):\n    return any(value > 3 for value in values)\n\nprint(any_above_3_builtin([0, 4]))  # Expected: True\nprint(any_above_3_builtin([3, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5845(values):\n    def calculate():\n        return any(value > 3 for value in values)\n    return calculate()\n\nprint(solve_problem_5845([0, 4]))\n\n# Example 3: static method approach\nclass Problem5845Solution:\n    @staticmethod\n    def any_above_3_builtin(values):\n        return any(value > 3 for value in values)\n\nprint(Problem5845Solution.any_above_3_builtin([3, 2]))\n\n# Example 4: assigned result approach\nresult = any_above_3_builtin([0, 4])\nprint(result)\n\n# Example 5: direct call\nprint(any_above_3_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5846,
    "title": "Problem 5846",
    "description": "Write a Python function called `any_above_4_builtin` that must use the built-in `any()` to test whether one value exceeds 4. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  any_above_4_builtin([0, 5]) -> True\n  any_above_4_builtin([4, 3]) -> False",
    "initialCode": "def any_above_4_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef any_above_4_builtin(values):\n    return any(value > 4 for value in values)\n\nprint(any_above_4_builtin([0, 5]))  # Expected: True\nprint(any_above_4_builtin([4, 3]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5846(values):\n    def calculate():\n        return any(value > 4 for value in values)\n    return calculate()\n\nprint(solve_problem_5846([0, 5]))\n\n# Example 3: static method approach\nclass Problem5846Solution:\n    @staticmethod\n    def any_above_4_builtin(values):\n        return any(value > 4 for value in values)\n\nprint(Problem5846Solution.any_above_4_builtin([4, 3]))\n\n# Example 4: assigned result approach\nresult = any_above_4_builtin([0, 5])\nprint(result)\n\n# Example 5: direct call\nprint(any_above_4_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5847,
    "title": "Problem 5847",
    "description": "Write a Python function called `any_above_5_builtin` that must use the built-in `any()` to test whether one value exceeds 5. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  any_above_5_builtin([0, 6]) -> True\n  any_above_5_builtin([5, 4]) -> False",
    "initialCode": "def any_above_5_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef any_above_5_builtin(values):\n    return any(value > 5 for value in values)\n\nprint(any_above_5_builtin([0, 6]))  # Expected: True\nprint(any_above_5_builtin([5, 4]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5847(values):\n    def calculate():\n        return any(value > 5 for value in values)\n    return calculate()\n\nprint(solve_problem_5847([0, 6]))\n\n# Example 3: static method approach\nclass Problem5847Solution:\n    @staticmethod\n    def any_above_5_builtin(values):\n        return any(value > 5 for value in values)\n\nprint(Problem5847Solution.any_above_5_builtin([5, 4]))\n\n# Example 4: assigned result approach\nresult = any_above_5_builtin([0, 6])\nprint(result)\n\n# Example 5: direct call\nprint(any_above_5_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5848,
    "title": "Problem 5848",
    "description": "Write a Python function called `all_at_least_1_builtin` that must use the built-in `all()` to test whether every value is at least -1. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  all_at_least_1_builtin([0, 2]) -> True\n  all_at_least_1_builtin([-2, 2]) -> False",
    "initialCode": "def all_at_least_1_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef all_at_least_1_builtin(values):\n    return all(value >= -1 for value in values)\n\nprint(all_at_least_1_builtin([0, 2]))  # Expected: True\nprint(all_at_least_1_builtin([-2, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5848(values):\n    def calculate():\n        return all(value >= -1 for value in values)\n    return calculate()\n\nprint(solve_problem_5848([0, 2]))\n\n# Example 3: static method approach\nclass Problem5848Solution:\n    @staticmethod\n    def all_at_least_1_builtin(values):\n        return all(value >= -1 for value in values)\n\nprint(Problem5848Solution.all_at_least_1_builtin([-2, 2]))\n\n# Example 4: assigned result approach\nresult = all_at_least_1_builtin([0, 2])\nprint(result)\n\n# Example 5: direct call\nprint(all_at_least_1_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5849,
    "title": "Problem 5849",
    "description": "Write a Python function called `all_at_least_2_builtin` that must use the built-in `all()` to test whether every value is at least -2. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  all_at_least_2_builtin([0, 2]) -> True\n  all_at_least_2_builtin([-3, 2]) -> False",
    "initialCode": "def all_at_least_2_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef all_at_least_2_builtin(values):\n    return all(value >= -2 for value in values)\n\nprint(all_at_least_2_builtin([0, 2]))  # Expected: True\nprint(all_at_least_2_builtin([-3, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5849(values):\n    def calculate():\n        return all(value >= -2 for value in values)\n    return calculate()\n\nprint(solve_problem_5849([0, 2]))\n\n# Example 3: static method approach\nclass Problem5849Solution:\n    @staticmethod\n    def all_at_least_2_builtin(values):\n        return all(value >= -2 for value in values)\n\nprint(Problem5849Solution.all_at_least_2_builtin([-3, 2]))\n\n# Example 4: assigned result approach\nresult = all_at_least_2_builtin([0, 2])\nprint(result)\n\n# Example 5: direct call\nprint(all_at_least_2_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5850,
    "title": "Problem 5850",
    "description": "Write a Python function called `all_at_least_3_builtin` that must use the built-in `all()` to test whether every value is at least -3. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  all_at_least_3_builtin([0, 2]) -> True\n  all_at_least_3_builtin([-4, 2]) -> False",
    "initialCode": "def all_at_least_3_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef all_at_least_3_builtin(values):\n    return all(value >= -3 for value in values)\n\nprint(all_at_least_3_builtin([0, 2]))  # Expected: True\nprint(all_at_least_3_builtin([-4, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5850(values):\n    def calculate():\n        return all(value >= -3 for value in values)\n    return calculate()\n\nprint(solve_problem_5850([0, 2]))\n\n# Example 3: static method approach\nclass Problem5850Solution:\n    @staticmethod\n    def all_at_least_3_builtin(values):\n        return all(value >= -3 for value in values)\n\nprint(Problem5850Solution.all_at_least_3_builtin([-4, 2]))\n\n# Example 4: assigned result approach\nresult = all_at_least_3_builtin([0, 2])\nprint(result)\n\n# Example 5: direct call\nprint(all_at_least_3_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5851,
    "title": "Problem 5851",
    "description": "Write a Python function called `all_at_least_4_builtin` that must use the built-in `all()` to test whether every value is at least -4. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  all_at_least_4_builtin([0, 2]) -> True\n  all_at_least_4_builtin([-5, 2]) -> False",
    "initialCode": "def all_at_least_4_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef all_at_least_4_builtin(values):\n    return all(value >= -4 for value in values)\n\nprint(all_at_least_4_builtin([0, 2]))  # Expected: True\nprint(all_at_least_4_builtin([-5, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5851(values):\n    def calculate():\n        return all(value >= -4 for value in values)\n    return calculate()\n\nprint(solve_problem_5851([0, 2]))\n\n# Example 3: static method approach\nclass Problem5851Solution:\n    @staticmethod\n    def all_at_least_4_builtin(values):\n        return all(value >= -4 for value in values)\n\nprint(Problem5851Solution.all_at_least_4_builtin([-5, 2]))\n\n# Example 4: assigned result approach\nresult = all_at_least_4_builtin([0, 2])\nprint(result)\n\n# Example 5: direct call\nprint(all_at_least_4_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5852,
    "title": "Problem 5852",
    "description": "Write a Python function called `all_at_least_5_builtin` that must use the built-in `all()` to test whether every value is at least -5. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  all_at_least_5_builtin([0, 2]) -> True\n  all_at_least_5_builtin([-6, 2]) -> False",
    "initialCode": "def all_at_least_5_builtin(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef all_at_least_5_builtin(values):\n    return all(value >= -5 for value in values)\n\nprint(all_at_least_5_builtin([0, 2]))  # Expected: True\nprint(all_at_least_5_builtin([-6, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5852(values):\n    def calculate():\n        return all(value >= -5 for value in values)\n    return calculate()\n\nprint(solve_problem_5852([0, 2]))\n\n# Example 3: static method approach\nclass Problem5852Solution:\n    @staticmethod\n    def all_at_least_5_builtin(values):\n        return all(value >= -5 for value in values)\n\nprint(Problem5852Solution.all_at_least_5_builtin([-6, 2]))\n\n# Example 4: assigned result approach\nresult = all_at_least_5_builtin([0, 2])\nprint(result)\n\n# Example 5: direct call\nprint(all_at_least_5_builtin([]))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5853,
    "title": "Problem 5853",
    "description": "Write a Python function called `zip_with_marker_1_builtin` that must use the built-ins `zip()` and `dict()`, then store marker 1. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  zip_with_marker_1_builtin([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker\": 1}\n  zip_with_marker_1_builtin([\"x\"], [9]) -> {\"x\": 9, \"marker\": 1}",
    "initialCode": "def zip_with_marker_1_builtin(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_with_marker_1_builtin(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker\"] = 1\n    return result\n\nprint(zip_with_marker_1_builtin([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker\": 1}\nprint(zip_with_marker_1_builtin([\"x\"], [9]))  # Expected: {\"x\": 9, \"marker\": 1}\n\n# Example 2: nested helper approach\ndef solve_problem_5853(keys, values):\n    def calculate():\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 1\n        return result\n    return calculate()\n\nprint(solve_problem_5853([\"a\", \"b\"], [1, 2]))\n\n# Example 3: static method approach\nclass Problem5853Solution:\n    @staticmethod\n    def zip_with_marker_1_builtin(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 1\n        return result\n\nprint(Problem5853Solution.zip_with_marker_1_builtin([\"x\"], [9]))\n\n# Example 4: assigned result approach\nresult = zip_with_marker_1_builtin([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(zip_with_marker_1_builtin([], []))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5854,
    "title": "Problem 5854",
    "description": "Write a Python function called `zip_with_marker_2_builtin` that must use the built-ins `zip()` and `dict()`, then store marker 2. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  zip_with_marker_2_builtin([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker\": 2}\n  zip_with_marker_2_builtin([\"x\"], [9]) -> {\"x\": 9, \"marker\": 2}",
    "initialCode": "def zip_with_marker_2_builtin(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_with_marker_2_builtin(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker\"] = 2\n    return result\n\nprint(zip_with_marker_2_builtin([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker\": 2}\nprint(zip_with_marker_2_builtin([\"x\"], [9]))  # Expected: {\"x\": 9, \"marker\": 2}\n\n# Example 2: nested helper approach\ndef solve_problem_5854(keys, values):\n    def calculate():\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 2\n        return result\n    return calculate()\n\nprint(solve_problem_5854([\"a\", \"b\"], [1, 2]))\n\n# Example 3: static method approach\nclass Problem5854Solution:\n    @staticmethod\n    def zip_with_marker_2_builtin(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 2\n        return result\n\nprint(Problem5854Solution.zip_with_marker_2_builtin([\"x\"], [9]))\n\n# Example 4: assigned result approach\nresult = zip_with_marker_2_builtin([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(zip_with_marker_2_builtin([], []))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5855,
    "title": "Problem 5855",
    "description": "Write a Python function called `zip_with_marker_3_builtin` that must use the built-ins `zip()` and `dict()`, then store marker 3. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  zip_with_marker_3_builtin([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker\": 3}\n  zip_with_marker_3_builtin([\"x\"], [9]) -> {\"x\": 9, \"marker\": 3}",
    "initialCode": "def zip_with_marker_3_builtin(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_with_marker_3_builtin(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker\"] = 3\n    return result\n\nprint(zip_with_marker_3_builtin([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker\": 3}\nprint(zip_with_marker_3_builtin([\"x\"], [9]))  # Expected: {\"x\": 9, \"marker\": 3}\n\n# Example 2: nested helper approach\ndef solve_problem_5855(keys, values):\n    def calculate():\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 3\n        return result\n    return calculate()\n\nprint(solve_problem_5855([\"a\", \"b\"], [1, 2]))\n\n# Example 3: static method approach\nclass Problem5855Solution:\n    @staticmethod\n    def zip_with_marker_3_builtin(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 3\n        return result\n\nprint(Problem5855Solution.zip_with_marker_3_builtin([\"x\"], [9]))\n\n# Example 4: assigned result approach\nresult = zip_with_marker_3_builtin([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(zip_with_marker_3_builtin([], []))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5856,
    "title": "Problem 5856",
    "description": "Write a Python function called `zip_with_marker_4_builtin` that must use the built-ins `zip()` and `dict()`, then store marker 4. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  zip_with_marker_4_builtin([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker\": 4}\n  zip_with_marker_4_builtin([\"x\"], [9]) -> {\"x\": 9, \"marker\": 4}",
    "initialCode": "def zip_with_marker_4_builtin(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_with_marker_4_builtin(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker\"] = 4\n    return result\n\nprint(zip_with_marker_4_builtin([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker\": 4}\nprint(zip_with_marker_4_builtin([\"x\"], [9]))  # Expected: {\"x\": 9, \"marker\": 4}\n\n# Example 2: nested helper approach\ndef solve_problem_5856(keys, values):\n    def calculate():\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 4\n        return result\n    return calculate()\n\nprint(solve_problem_5856([\"a\", \"b\"], [1, 2]))\n\n# Example 3: static method approach\nclass Problem5856Solution:\n    @staticmethod\n    def zip_with_marker_4_builtin(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 4\n        return result\n\nprint(Problem5856Solution.zip_with_marker_4_builtin([\"x\"], [9]))\n\n# Example 4: assigned result approach\nresult = zip_with_marker_4_builtin([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(zip_with_marker_4_builtin([], []))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5857,
    "title": "Problem 5857",
    "description": "Write a Python function called `zip_with_marker_5_builtin` that must use the built-ins `zip()` and `dict()`, then store marker 5. Practice built-in syntax.\nDifficulty: Easy.\nExamples:\n  zip_with_marker_5_builtin([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker\": 5}\n  zip_with_marker_5_builtin([\"x\"], [9]) -> {\"x\": 9, \"marker\": 5}",
    "initialCode": "def zip_with_marker_5_builtin(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_with_marker_5_builtin(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker\"] = 5\n    return result\n\nprint(zip_with_marker_5_builtin([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker\": 5}\nprint(zip_with_marker_5_builtin([\"x\"], [9]))  # Expected: {\"x\": 9, \"marker\": 5}\n\n# Example 2: nested helper approach\ndef solve_problem_5857(keys, values):\n    def calculate():\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 5\n        return result\n    return calculate()\n\nprint(solve_problem_5857([\"a\", \"b\"], [1, 2]))\n\n# Example 3: static method approach\nclass Problem5857Solution:\n    @staticmethod\n    def zip_with_marker_5_builtin(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker\"] = 5\n        return result\n\nprint(Problem5857Solution.zip_with_marker_5_builtin([\"x\"], [9]))\n\n# Example 4: assigned result approach\nresult = zip_with_marker_5_builtin([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(zip_with_marker_5_builtin([], []))",
    "hint": "Focus on the built-in signature, argument order, and returned type. Use the required built-in structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the built-in structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Built-in Easy"
  },
  {
    "id": 5858,
    "title": "Problem 5858",
    "description": "Write a Python function called `unique_count_plus_1_set` that must count unique values with a set, then add 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_count_plus_1_set([1, 1, 2]) -> 3\n  unique_count_plus_1_set([]) -> 1",
    "initialCode": "def unique_count_plus_1_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_count_plus_1_set(values):\n    return len(set(values)) + 1\n\nprint(unique_count_plus_1_set([1, 1, 2]))  # Expected: 3\nprint(unique_count_plus_1_set([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5858(values):\n    def calculate():\n        return len(set(values)) + 1\n    return calculate()\n\nprint(solve_problem_5858([1, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5858Solution:\n    @staticmethod\n    def unique_count_plus_1_set(values):\n        return len(set(values)) + 1\n\nprint(Problem5858Solution.unique_count_plus_1_set([]))\n\n# Example 4: assigned result approach\nresult = unique_count_plus_1_set([1, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(unique_count_plus_1_set([\"a\", \"b\", \"a\"]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5859,
    "title": "Problem 5859",
    "description": "Write a Python function called `unique_count_plus_2_set` that must count unique values with a set, then add 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_count_plus_2_set([1, 1, 2]) -> 4\n  unique_count_plus_2_set([]) -> 2",
    "initialCode": "def unique_count_plus_2_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_count_plus_2_set(values):\n    return len(set(values)) + 2\n\nprint(unique_count_plus_2_set([1, 1, 2]))  # Expected: 4\nprint(unique_count_plus_2_set([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_5859(values):\n    def calculate():\n        return len(set(values)) + 2\n    return calculate()\n\nprint(solve_problem_5859([1, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5859Solution:\n    @staticmethod\n    def unique_count_plus_2_set(values):\n        return len(set(values)) + 2\n\nprint(Problem5859Solution.unique_count_plus_2_set([]))\n\n# Example 4: assigned result approach\nresult = unique_count_plus_2_set([1, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(unique_count_plus_2_set([\"a\", \"b\", \"a\"]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5860,
    "title": "Problem 5860",
    "description": "Write a Python function called `unique_count_plus_3_set` that must count unique values with a set, then add 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_count_plus_3_set([1, 1, 2]) -> 5\n  unique_count_plus_3_set([]) -> 3",
    "initialCode": "def unique_count_plus_3_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_count_plus_3_set(values):\n    return len(set(values)) + 3\n\nprint(unique_count_plus_3_set([1, 1, 2]))  # Expected: 5\nprint(unique_count_plus_3_set([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_5860(values):\n    def calculate():\n        return len(set(values)) + 3\n    return calculate()\n\nprint(solve_problem_5860([1, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5860Solution:\n    @staticmethod\n    def unique_count_plus_3_set(values):\n        return len(set(values)) + 3\n\nprint(Problem5860Solution.unique_count_plus_3_set([]))\n\n# Example 4: assigned result approach\nresult = unique_count_plus_3_set([1, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(unique_count_plus_3_set([\"a\", \"b\", \"a\"]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5861,
    "title": "Problem 5861",
    "description": "Write a Python function called `unique_count_plus_4_set` that must count unique values with a set, then add 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_count_plus_4_set([1, 1, 2]) -> 6\n  unique_count_plus_4_set([]) -> 4",
    "initialCode": "def unique_count_plus_4_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_count_plus_4_set(values):\n    return len(set(values)) + 4\n\nprint(unique_count_plus_4_set([1, 1, 2]))  # Expected: 6\nprint(unique_count_plus_4_set([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5861(values):\n    def calculate():\n        return len(set(values)) + 4\n    return calculate()\n\nprint(solve_problem_5861([1, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5861Solution:\n    @staticmethod\n    def unique_count_plus_4_set(values):\n        return len(set(values)) + 4\n\nprint(Problem5861Solution.unique_count_plus_4_set([]))\n\n# Example 4: assigned result approach\nresult = unique_count_plus_4_set([1, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(unique_count_plus_4_set([\"a\", \"b\", \"a\"]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5862,
    "title": "Problem 5862",
    "description": "Write a Python function called `unique_count_plus_5_set` that must count unique values with a set, then add 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_count_plus_5_set([1, 1, 2]) -> 7\n  unique_count_plus_5_set([]) -> 5",
    "initialCode": "def unique_count_plus_5_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_count_plus_5_set(values):\n    return len(set(values)) + 5\n\nprint(unique_count_plus_5_set([1, 1, 2]))  # Expected: 7\nprint(unique_count_plus_5_set([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5862(values):\n    def calculate():\n        return len(set(values)) + 5\n    return calculate()\n\nprint(solve_problem_5862([1, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5862Solution:\n    @staticmethod\n    def unique_count_plus_5_set(values):\n        return len(set(values)) + 5\n\nprint(Problem5862Solution.unique_count_plus_5_set([]))\n\n# Example 4: assigned result approach\nresult = unique_count_plus_5_set([1, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(unique_count_plus_5_set([\"a\", \"b\", \"a\"]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5863,
    "title": "Problem 5863",
    "description": "Write a Python function called `union_marker_1_set` that must return the sorted set union after adding marker 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  union_marker_1_set([1, 2], [2, 3]) -> [1, 2, 3]\n  union_marker_1_set([], [4]) -> [1, 4]",
    "initialCode": "def union_marker_1_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef union_marker_1_set(left, right):\n    return sorted(set(left).union(right, {1}))\n\nprint(union_marker_1_set([1, 2], [2, 3]))  # Expected: [1, 2, 3]\nprint(union_marker_1_set([], [4]))  # Expected: [1, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_5863(left, right):\n    def calculate():\n        return sorted(set(left).union(right, {1}))\n    return calculate()\n\nprint(solve_problem_5863([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5863Solution:\n    @staticmethod\n    def union_marker_1_set(left, right):\n        return sorted(set(left).union(right, {1}))\n\nprint(Problem5863Solution.union_marker_1_set([], [4]))\n\n# Example 4: assigned result approach\nresult = union_marker_1_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(union_marker_1_set([1], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5864,
    "title": "Problem 5864",
    "description": "Write a Python function called `union_marker_2_set` that must return the sorted set union after adding marker 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  union_marker_2_set([1, 2], [2, 3]) -> [1, 2, 3]\n  union_marker_2_set([], [4]) -> [2, 4]",
    "initialCode": "def union_marker_2_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef union_marker_2_set(left, right):\n    return sorted(set(left).union(right, {2}))\n\nprint(union_marker_2_set([1, 2], [2, 3]))  # Expected: [1, 2, 3]\nprint(union_marker_2_set([], [4]))  # Expected: [2, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_5864(left, right):\n    def calculate():\n        return sorted(set(left).union(right, {2}))\n    return calculate()\n\nprint(solve_problem_5864([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5864Solution:\n    @staticmethod\n    def union_marker_2_set(left, right):\n        return sorted(set(left).union(right, {2}))\n\nprint(Problem5864Solution.union_marker_2_set([], [4]))\n\n# Example 4: assigned result approach\nresult = union_marker_2_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(union_marker_2_set([2], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5865,
    "title": "Problem 5865",
    "description": "Write a Python function called `union_marker_3_set` that must return the sorted set union after adding marker 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  union_marker_3_set([1, 2], [2, 3]) -> [1, 2, 3]\n  union_marker_3_set([], [4]) -> [3, 4]",
    "initialCode": "def union_marker_3_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef union_marker_3_set(left, right):\n    return sorted(set(left).union(right, {3}))\n\nprint(union_marker_3_set([1, 2], [2, 3]))  # Expected: [1, 2, 3]\nprint(union_marker_3_set([], [4]))  # Expected: [3, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_5865(left, right):\n    def calculate():\n        return sorted(set(left).union(right, {3}))\n    return calculate()\n\nprint(solve_problem_5865([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5865Solution:\n    @staticmethod\n    def union_marker_3_set(left, right):\n        return sorted(set(left).union(right, {3}))\n\nprint(Problem5865Solution.union_marker_3_set([], [4]))\n\n# Example 4: assigned result approach\nresult = union_marker_3_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(union_marker_3_set([3], [3]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5866,
    "title": "Problem 5866",
    "description": "Write a Python function called `union_marker_4_set` that must return the sorted set union after adding marker 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  union_marker_4_set([1, 2], [2, 3]) -> [1, 2, 3, 4]\n  union_marker_4_set([], [4]) -> [4]",
    "initialCode": "def union_marker_4_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef union_marker_4_set(left, right):\n    return sorted(set(left).union(right, {4}))\n\nprint(union_marker_4_set([1, 2], [2, 3]))  # Expected: [1, 2, 3, 4]\nprint(union_marker_4_set([], [4]))  # Expected: [4]\n\n# Example 2: nested helper approach\ndef solve_problem_5866(left, right):\n    def calculate():\n        return sorted(set(left).union(right, {4}))\n    return calculate()\n\nprint(solve_problem_5866([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5866Solution:\n    @staticmethod\n    def union_marker_4_set(left, right):\n        return sorted(set(left).union(right, {4}))\n\nprint(Problem5866Solution.union_marker_4_set([], [4]))\n\n# Example 4: assigned result approach\nresult = union_marker_4_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(union_marker_4_set([4], [4]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5867,
    "title": "Problem 5867",
    "description": "Write a Python function called `union_marker_5_set` that must return the sorted set union after adding marker 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  union_marker_5_set([1, 2], [2, 3]) -> [1, 2, 3, 5]\n  union_marker_5_set([], [4]) -> [4, 5]",
    "initialCode": "def union_marker_5_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef union_marker_5_set(left, right):\n    return sorted(set(left).union(right, {5}))\n\nprint(union_marker_5_set([1, 2], [2, 3]))  # Expected: [1, 2, 3, 5]\nprint(union_marker_5_set([], [4]))  # Expected: [4, 5]\n\n# Example 2: nested helper approach\ndef solve_problem_5867(left, right):\n    def calculate():\n        return sorted(set(left).union(right, {5}))\n    return calculate()\n\nprint(solve_problem_5867([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5867Solution:\n    @staticmethod\n    def union_marker_5_set(left, right):\n        return sorted(set(left).union(right, {5}))\n\nprint(Problem5867Solution.union_marker_5_set([], [4]))\n\n# Example 4: assigned result approach\nresult = union_marker_5_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(union_marker_5_set([5], [5]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5868,
    "title": "Problem 5868",
    "description": "Write a Python function called `intersection_without_1_set` that must return the sorted set intersection after removing 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  intersection_without_1_set([1, 2, 3], [2, 3]) -> [2, 3]\n  intersection_without_1_set([1], [1]) -> []",
    "initialCode": "def intersection_without_1_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef intersection_without_1_set(left, right):\n    return sorted(set(left).intersection(right) - {1})\n\nprint(intersection_without_1_set([1, 2, 3], [2, 3]))  # Expected: [2, 3]\nprint(intersection_without_1_set([1], [1]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5868(left, right):\n    def calculate():\n        return sorted(set(left).intersection(right) - {1})\n    return calculate()\n\nprint(solve_problem_5868([1, 2, 3], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5868Solution:\n    @staticmethod\n    def intersection_without_1_set(left, right):\n        return sorted(set(left).intersection(right) - {1})\n\nprint(Problem5868Solution.intersection_without_1_set([1], [1]))\n\n# Example 4: assigned result approach\nresult = intersection_without_1_set([1, 2, 3], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(intersection_without_1_set([], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5869,
    "title": "Problem 5869",
    "description": "Write a Python function called `intersection_without_2_set` that must return the sorted set intersection after removing 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  intersection_without_2_set([1, 2, 3], [2, 3]) -> [3]\n  intersection_without_2_set([2], [2]) -> []",
    "initialCode": "def intersection_without_2_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef intersection_without_2_set(left, right):\n    return sorted(set(left).intersection(right) - {2})\n\nprint(intersection_without_2_set([1, 2, 3], [2, 3]))  # Expected: [3]\nprint(intersection_without_2_set([2], [2]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5869(left, right):\n    def calculate():\n        return sorted(set(left).intersection(right) - {2})\n    return calculate()\n\nprint(solve_problem_5869([1, 2, 3], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5869Solution:\n    @staticmethod\n    def intersection_without_2_set(left, right):\n        return sorted(set(left).intersection(right) - {2})\n\nprint(Problem5869Solution.intersection_without_2_set([2], [2]))\n\n# Example 4: assigned result approach\nresult = intersection_without_2_set([1, 2, 3], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(intersection_without_2_set([], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5870,
    "title": "Problem 5870",
    "description": "Write a Python function called `intersection_without_3_set` that must return the sorted set intersection after removing 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  intersection_without_3_set([1, 2, 3], [2, 3]) -> [2]\n  intersection_without_3_set([3], [3]) -> []",
    "initialCode": "def intersection_without_3_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef intersection_without_3_set(left, right):\n    return sorted(set(left).intersection(right) - {3})\n\nprint(intersection_without_3_set([1, 2, 3], [2, 3]))  # Expected: [2]\nprint(intersection_without_3_set([3], [3]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5870(left, right):\n    def calculate():\n        return sorted(set(left).intersection(right) - {3})\n    return calculate()\n\nprint(solve_problem_5870([1, 2, 3], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5870Solution:\n    @staticmethod\n    def intersection_without_3_set(left, right):\n        return sorted(set(left).intersection(right) - {3})\n\nprint(Problem5870Solution.intersection_without_3_set([3], [3]))\n\n# Example 4: assigned result approach\nresult = intersection_without_3_set([1, 2, 3], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(intersection_without_3_set([], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5871,
    "title": "Problem 5871",
    "description": "Write a Python function called `intersection_without_4_set` that must return the sorted set intersection after removing 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  intersection_without_4_set([1, 2, 3], [2, 3]) -> [2, 3]\n  intersection_without_4_set([4], [4]) -> []",
    "initialCode": "def intersection_without_4_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef intersection_without_4_set(left, right):\n    return sorted(set(left).intersection(right) - {4})\n\nprint(intersection_without_4_set([1, 2, 3], [2, 3]))  # Expected: [2, 3]\nprint(intersection_without_4_set([4], [4]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5871(left, right):\n    def calculate():\n        return sorted(set(left).intersection(right) - {4})\n    return calculate()\n\nprint(solve_problem_5871([1, 2, 3], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5871Solution:\n    @staticmethod\n    def intersection_without_4_set(left, right):\n        return sorted(set(left).intersection(right) - {4})\n\nprint(Problem5871Solution.intersection_without_4_set([4], [4]))\n\n# Example 4: assigned result approach\nresult = intersection_without_4_set([1, 2, 3], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(intersection_without_4_set([], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5872,
    "title": "Problem 5872",
    "description": "Write a Python function called `intersection_without_5_set` that must return the sorted set intersection after removing 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  intersection_without_5_set([1, 2, 3], [2, 3]) -> [2, 3]\n  intersection_without_5_set([5], [5]) -> []",
    "initialCode": "def intersection_without_5_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef intersection_without_5_set(left, right):\n    return sorted(set(left).intersection(right) - {5})\n\nprint(intersection_without_5_set([1, 2, 3], [2, 3]))  # Expected: [2, 3]\nprint(intersection_without_5_set([5], [5]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5872(left, right):\n    def calculate():\n        return sorted(set(left).intersection(right) - {5})\n    return calculate()\n\nprint(solve_problem_5872([1, 2, 3], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5872Solution:\n    @staticmethod\n    def intersection_without_5_set(left, right):\n        return sorted(set(left).intersection(right) - {5})\n\nprint(Problem5872Solution.intersection_without_5_set([5], [5]))\n\n# Example 4: assigned result approach\nresult = intersection_without_5_set([1, 2, 3], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(intersection_without_5_set([], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5873,
    "title": "Problem 5873",
    "description": "Write a Python function called `difference_marker_1_set` that must return the sorted set difference and include marker 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  difference_marker_1_set([1, 2, 3], [2]) -> [1, 3]\n  difference_marker_1_set([1], [1]) -> [1]",
    "initialCode": "def difference_marker_1_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef difference_marker_1_set(left, right):\n    return sorted(set(left).difference(right).union({1}))\n\nprint(difference_marker_1_set([1, 2, 3], [2]))  # Expected: [1, 3]\nprint(difference_marker_1_set([1], [1]))  # Expected: [1]\n\n# Example 2: nested helper approach\ndef solve_problem_5873(left, right):\n    def calculate():\n        return sorted(set(left).difference(right).union({1}))\n    return calculate()\n\nprint(solve_problem_5873([1, 2, 3], [2]))\n\n# Example 3: static method approach\nclass Problem5873Solution:\n    @staticmethod\n    def difference_marker_1_set(left, right):\n        return sorted(set(left).difference(right).union({1}))\n\nprint(Problem5873Solution.difference_marker_1_set([1], [1]))\n\n# Example 4: assigned result approach\nresult = difference_marker_1_set([1, 2, 3], [2])\nprint(result)\n\n# Example 5: direct call\nprint(difference_marker_1_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5874,
    "title": "Problem 5874",
    "description": "Write a Python function called `difference_marker_2_set` that must return the sorted set difference and include marker 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  difference_marker_2_set([1, 2, 3], [2]) -> [1, 2, 3]\n  difference_marker_2_set([2], [2]) -> [2]",
    "initialCode": "def difference_marker_2_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef difference_marker_2_set(left, right):\n    return sorted(set(left).difference(right).union({2}))\n\nprint(difference_marker_2_set([1, 2, 3], [2]))  # Expected: [1, 2, 3]\nprint(difference_marker_2_set([2], [2]))  # Expected: [2]\n\n# Example 2: nested helper approach\ndef solve_problem_5874(left, right):\n    def calculate():\n        return sorted(set(left).difference(right).union({2}))\n    return calculate()\n\nprint(solve_problem_5874([1, 2, 3], [2]))\n\n# Example 3: static method approach\nclass Problem5874Solution:\n    @staticmethod\n    def difference_marker_2_set(left, right):\n        return sorted(set(left).difference(right).union({2}))\n\nprint(Problem5874Solution.difference_marker_2_set([2], [2]))\n\n# Example 4: assigned result approach\nresult = difference_marker_2_set([1, 2, 3], [2])\nprint(result)\n\n# Example 5: direct call\nprint(difference_marker_2_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5875,
    "title": "Problem 5875",
    "description": "Write a Python function called `difference_marker_3_set` that must return the sorted set difference and include marker 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  difference_marker_3_set([1, 2, 3], [2]) -> [1, 3]\n  difference_marker_3_set([3], [3]) -> [3]",
    "initialCode": "def difference_marker_3_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef difference_marker_3_set(left, right):\n    return sorted(set(left).difference(right).union({3}))\n\nprint(difference_marker_3_set([1, 2, 3], [2]))  # Expected: [1, 3]\nprint(difference_marker_3_set([3], [3]))  # Expected: [3]\n\n# Example 2: nested helper approach\ndef solve_problem_5875(left, right):\n    def calculate():\n        return sorted(set(left).difference(right).union({3}))\n    return calculate()\n\nprint(solve_problem_5875([1, 2, 3], [2]))\n\n# Example 3: static method approach\nclass Problem5875Solution:\n    @staticmethod\n    def difference_marker_3_set(left, right):\n        return sorted(set(left).difference(right).union({3}))\n\nprint(Problem5875Solution.difference_marker_3_set([3], [3]))\n\n# Example 4: assigned result approach\nresult = difference_marker_3_set([1, 2, 3], [2])\nprint(result)\n\n# Example 5: direct call\nprint(difference_marker_3_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5876,
    "title": "Problem 5876",
    "description": "Write a Python function called `difference_marker_4_set` that must return the sorted set difference and include marker 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  difference_marker_4_set([1, 2, 3], [2]) -> [1, 3, 4]\n  difference_marker_4_set([4], [4]) -> [4]",
    "initialCode": "def difference_marker_4_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef difference_marker_4_set(left, right):\n    return sorted(set(left).difference(right).union({4}))\n\nprint(difference_marker_4_set([1, 2, 3], [2]))  # Expected: [1, 3, 4]\nprint(difference_marker_4_set([4], [4]))  # Expected: [4]\n\n# Example 2: nested helper approach\ndef solve_problem_5876(left, right):\n    def calculate():\n        return sorted(set(left).difference(right).union({4}))\n    return calculate()\n\nprint(solve_problem_5876([1, 2, 3], [2]))\n\n# Example 3: static method approach\nclass Problem5876Solution:\n    @staticmethod\n    def difference_marker_4_set(left, right):\n        return sorted(set(left).difference(right).union({4}))\n\nprint(Problem5876Solution.difference_marker_4_set([4], [4]))\n\n# Example 4: assigned result approach\nresult = difference_marker_4_set([1, 2, 3], [2])\nprint(result)\n\n# Example 5: direct call\nprint(difference_marker_4_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5877,
    "title": "Problem 5877",
    "description": "Write a Python function called `difference_marker_5_set` that must return the sorted set difference and include marker 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  difference_marker_5_set([1, 2, 3], [2]) -> [1, 3, 5]\n  difference_marker_5_set([5], [5]) -> [5]",
    "initialCode": "def difference_marker_5_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef difference_marker_5_set(left, right):\n    return sorted(set(left).difference(right).union({5}))\n\nprint(difference_marker_5_set([1, 2, 3], [2]))  # Expected: [1, 3, 5]\nprint(difference_marker_5_set([5], [5]))  # Expected: [5]\n\n# Example 2: nested helper approach\ndef solve_problem_5877(left, right):\n    def calculate():\n        return sorted(set(left).difference(right).union({5}))\n    return calculate()\n\nprint(solve_problem_5877([1, 2, 3], [2]))\n\n# Example 3: static method approach\nclass Problem5877Solution:\n    @staticmethod\n    def difference_marker_5_set(left, right):\n        return sorted(set(left).difference(right).union({5}))\n\nprint(Problem5877Solution.difference_marker_5_set([5], [5]))\n\n# Example 4: assigned result approach\nresult = difference_marker_5_set([1, 2, 3], [2])\nprint(result)\n\n# Example 5: direct call\nprint(difference_marker_5_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5878,
    "title": "Problem 5878",
    "description": "Write a Python function called `symmetric_size_1_set` that must return the symmetric-difference size plus 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  symmetric_size_1_set([1, 2], [2, 3]) -> 3\n  symmetric_size_1_set([], []) -> 1",
    "initialCode": "def symmetric_size_1_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef symmetric_size_1_set(left, right):\n    return len(set(left).symmetric_difference(right)) + 1\n\nprint(symmetric_size_1_set([1, 2], [2, 3]))  # Expected: 3\nprint(symmetric_size_1_set([], []))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5878(left, right):\n    def calculate():\n        return len(set(left).symmetric_difference(right)) + 1\n    return calculate()\n\nprint(solve_problem_5878([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5878Solution:\n    @staticmethod\n    def symmetric_size_1_set(left, right):\n        return len(set(left).symmetric_difference(right)) + 1\n\nprint(Problem5878Solution.symmetric_size_1_set([], []))\n\n# Example 4: assigned result approach\nresult = symmetric_size_1_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(symmetric_size_1_set([1], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5879,
    "title": "Problem 5879",
    "description": "Write a Python function called `symmetric_size_2_set` that must return the symmetric-difference size plus 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  symmetric_size_2_set([1, 2], [2, 3]) -> 4\n  symmetric_size_2_set([], []) -> 2",
    "initialCode": "def symmetric_size_2_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef symmetric_size_2_set(left, right):\n    return len(set(left).symmetric_difference(right)) + 2\n\nprint(symmetric_size_2_set([1, 2], [2, 3]))  # Expected: 4\nprint(symmetric_size_2_set([], []))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_5879(left, right):\n    def calculate():\n        return len(set(left).symmetric_difference(right)) + 2\n    return calculate()\n\nprint(solve_problem_5879([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5879Solution:\n    @staticmethod\n    def symmetric_size_2_set(left, right):\n        return len(set(left).symmetric_difference(right)) + 2\n\nprint(Problem5879Solution.symmetric_size_2_set([], []))\n\n# Example 4: assigned result approach\nresult = symmetric_size_2_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(symmetric_size_2_set([1], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5880,
    "title": "Problem 5880",
    "description": "Write a Python function called `symmetric_size_3_set` that must return the symmetric-difference size plus 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  symmetric_size_3_set([1, 2], [2, 3]) -> 5\n  symmetric_size_3_set([], []) -> 3",
    "initialCode": "def symmetric_size_3_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef symmetric_size_3_set(left, right):\n    return len(set(left).symmetric_difference(right)) + 3\n\nprint(symmetric_size_3_set([1, 2], [2, 3]))  # Expected: 5\nprint(symmetric_size_3_set([], []))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_5880(left, right):\n    def calculate():\n        return len(set(left).symmetric_difference(right)) + 3\n    return calculate()\n\nprint(solve_problem_5880([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5880Solution:\n    @staticmethod\n    def symmetric_size_3_set(left, right):\n        return len(set(left).symmetric_difference(right)) + 3\n\nprint(Problem5880Solution.symmetric_size_3_set([], []))\n\n# Example 4: assigned result approach\nresult = symmetric_size_3_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(symmetric_size_3_set([1], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5881,
    "title": "Problem 5881",
    "description": "Write a Python function called `symmetric_size_4_set` that must return the symmetric-difference size plus 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  symmetric_size_4_set([1, 2], [2, 3]) -> 6\n  symmetric_size_4_set([], []) -> 4",
    "initialCode": "def symmetric_size_4_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef symmetric_size_4_set(left, right):\n    return len(set(left).symmetric_difference(right)) + 4\n\nprint(symmetric_size_4_set([1, 2], [2, 3]))  # Expected: 6\nprint(symmetric_size_4_set([], []))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5881(left, right):\n    def calculate():\n        return len(set(left).symmetric_difference(right)) + 4\n    return calculate()\n\nprint(solve_problem_5881([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5881Solution:\n    @staticmethod\n    def symmetric_size_4_set(left, right):\n        return len(set(left).symmetric_difference(right)) + 4\n\nprint(Problem5881Solution.symmetric_size_4_set([], []))\n\n# Example 4: assigned result approach\nresult = symmetric_size_4_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(symmetric_size_4_set([1], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5882,
    "title": "Problem 5882",
    "description": "Write a Python function called `symmetric_size_5_set` that must return the symmetric-difference size plus 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  symmetric_size_5_set([1, 2], [2, 3]) -> 7\n  symmetric_size_5_set([], []) -> 5",
    "initialCode": "def symmetric_size_5_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef symmetric_size_5_set(left, right):\n    return len(set(left).symmetric_difference(right)) + 5\n\nprint(symmetric_size_5_set([1, 2], [2, 3]))  # Expected: 7\nprint(symmetric_size_5_set([], []))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5882(left, right):\n    def calculate():\n        return len(set(left).symmetric_difference(right)) + 5\n    return calculate()\n\nprint(solve_problem_5882([1, 2], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5882Solution:\n    @staticmethod\n    def symmetric_size_5_set(left, right):\n        return len(set(left).symmetric_difference(right)) + 5\n\nprint(Problem5882Solution.symmetric_size_5_set([], []))\n\n# Example 4: assigned result approach\nresult = symmetric_size_5_set([1, 2], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(symmetric_size_5_set([1], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5883,
    "title": "Problem 5883",
    "description": "Write a Python function called `required_subset_1_set` that must test whether required values form a subset after 1 is added. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  required_subset_1_set([1, 1], [1]) -> True\n  required_subset_1_set([9], [1, 2]) -> False",
    "initialCode": "def required_subset_1_set(required, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef required_subset_1_set(required, values):\n    return set(required).issubset(set(values).union({1}))\n\nprint(required_subset_1_set([1, 1], [1]))  # Expected: True\nprint(required_subset_1_set([9], [1, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5883(required, values):\n    def calculate():\n        return set(required).issubset(set(values).union({1}))\n    return calculate()\n\nprint(solve_problem_5883([1, 1], [1]))\n\n# Example 3: static method approach\nclass Problem5883Solution:\n    @staticmethod\n    def required_subset_1_set(required, values):\n        return set(required).issubset(set(values).union({1}))\n\nprint(Problem5883Solution.required_subset_1_set([9], [1, 2]))\n\n# Example 4: assigned result approach\nresult = required_subset_1_set([1, 1], [1])\nprint(result)\n\n# Example 5: direct call\nprint(required_subset_1_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5884,
    "title": "Problem 5884",
    "description": "Write a Python function called `required_subset_2_set` that must test whether required values form a subset after 2 is added. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  required_subset_2_set([1, 2], [1]) -> True\n  required_subset_2_set([9], [1, 2]) -> False",
    "initialCode": "def required_subset_2_set(required, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef required_subset_2_set(required, values):\n    return set(required).issubset(set(values).union({2}))\n\nprint(required_subset_2_set([1, 2], [1]))  # Expected: True\nprint(required_subset_2_set([9], [1, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5884(required, values):\n    def calculate():\n        return set(required).issubset(set(values).union({2}))\n    return calculate()\n\nprint(solve_problem_5884([1, 2], [1]))\n\n# Example 3: static method approach\nclass Problem5884Solution:\n    @staticmethod\n    def required_subset_2_set(required, values):\n        return set(required).issubset(set(values).union({2}))\n\nprint(Problem5884Solution.required_subset_2_set([9], [1, 2]))\n\n# Example 4: assigned result approach\nresult = required_subset_2_set([1, 2], [1])\nprint(result)\n\n# Example 5: direct call\nprint(required_subset_2_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5885,
    "title": "Problem 5885",
    "description": "Write a Python function called `required_subset_3_set` that must test whether required values form a subset after 3 is added. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  required_subset_3_set([1, 3], [1]) -> True\n  required_subset_3_set([9], [1, 2]) -> False",
    "initialCode": "def required_subset_3_set(required, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef required_subset_3_set(required, values):\n    return set(required).issubset(set(values).union({3}))\n\nprint(required_subset_3_set([1, 3], [1]))  # Expected: True\nprint(required_subset_3_set([9], [1, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5885(required, values):\n    def calculate():\n        return set(required).issubset(set(values).union({3}))\n    return calculate()\n\nprint(solve_problem_5885([1, 3], [1]))\n\n# Example 3: static method approach\nclass Problem5885Solution:\n    @staticmethod\n    def required_subset_3_set(required, values):\n        return set(required).issubset(set(values).union({3}))\n\nprint(Problem5885Solution.required_subset_3_set([9], [1, 2]))\n\n# Example 4: assigned result approach\nresult = required_subset_3_set([1, 3], [1])\nprint(result)\n\n# Example 5: direct call\nprint(required_subset_3_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5886,
    "title": "Problem 5886",
    "description": "Write a Python function called `required_subset_4_set` that must test whether required values form a subset after 4 is added. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  required_subset_4_set([1, 4], [1]) -> True\n  required_subset_4_set([9], [1, 2]) -> False",
    "initialCode": "def required_subset_4_set(required, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef required_subset_4_set(required, values):\n    return set(required).issubset(set(values).union({4}))\n\nprint(required_subset_4_set([1, 4], [1]))  # Expected: True\nprint(required_subset_4_set([9], [1, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5886(required, values):\n    def calculate():\n        return set(required).issubset(set(values).union({4}))\n    return calculate()\n\nprint(solve_problem_5886([1, 4], [1]))\n\n# Example 3: static method approach\nclass Problem5886Solution:\n    @staticmethod\n    def required_subset_4_set(required, values):\n        return set(required).issubset(set(values).union({4}))\n\nprint(Problem5886Solution.required_subset_4_set([9], [1, 2]))\n\n# Example 4: assigned result approach\nresult = required_subset_4_set([1, 4], [1])\nprint(result)\n\n# Example 5: direct call\nprint(required_subset_4_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5887,
    "title": "Problem 5887",
    "description": "Write a Python function called `required_subset_5_set` that must test whether required values form a subset after 5 is added. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  required_subset_5_set([1, 5], [1]) -> True\n  required_subset_5_set([9], [1, 2]) -> False",
    "initialCode": "def required_subset_5_set(required, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef required_subset_5_set(required, values):\n    return set(required).issubset(set(values).union({5}))\n\nprint(required_subset_5_set([1, 5], [1]))  # Expected: True\nprint(required_subset_5_set([9], [1, 2]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5887(required, values):\n    def calculate():\n        return set(required).issubset(set(values).union({5}))\n    return calculate()\n\nprint(solve_problem_5887([1, 5], [1]))\n\n# Example 3: static method approach\nclass Problem5887Solution:\n    @staticmethod\n    def required_subset_5_set(required, values):\n        return set(required).issubset(set(values).union({5}))\n\nprint(Problem5887Solution.required_subset_5_set([9], [1, 2]))\n\n# Example 4: assigned result approach\nresult = required_subset_5_set([1, 5], [1])\nprint(result)\n\n# Example 5: direct call\nprint(required_subset_5_set([], []))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5888,
    "title": "Problem 5888",
    "description": "Write a Python function called `disjoint_except_1_set` that must test whether sets are disjoint after ignoring value 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  disjoint_except_1_set([1, 1], [2, 1]) -> True\n  disjoint_except_1_set([1, 2], [2, 3]) -> False",
    "initialCode": "def disjoint_except_1_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef disjoint_except_1_set(left, right):\n    return (set(left) - {1}).isdisjoint(set(right) - {1})\n\nprint(disjoint_except_1_set([1, 1], [2, 1]))  # Expected: True\nprint(disjoint_except_1_set([1, 2], [2, 3]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5888(left, right):\n    def calculate():\n        return (set(left) - {1}).isdisjoint(set(right) - {1})\n    return calculate()\n\nprint(solve_problem_5888([1, 1], [2, 1]))\n\n# Example 3: static method approach\nclass Problem5888Solution:\n    @staticmethod\n    def disjoint_except_1_set(left, right):\n        return (set(left) - {1}).isdisjoint(set(right) - {1})\n\nprint(Problem5888Solution.disjoint_except_1_set([1, 2], [2, 3]))\n\n# Example 4: assigned result approach\nresult = disjoint_except_1_set([1, 1], [2, 1])\nprint(result)\n\n# Example 5: direct call\nprint(disjoint_except_1_set([], [1]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5889,
    "title": "Problem 5889",
    "description": "Write a Python function called `disjoint_except_2_set` that must test whether sets are disjoint after ignoring value 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  disjoint_except_2_set([1, 2], [2, 2]) -> True\n  disjoint_except_2_set([1, 2], [2, 3]) -> True",
    "initialCode": "def disjoint_except_2_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef disjoint_except_2_set(left, right):\n    return (set(left) - {2}).isdisjoint(set(right) - {2})\n\nprint(disjoint_except_2_set([1, 2], [2, 2]))  # Expected: True\nprint(disjoint_except_2_set([1, 2], [2, 3]))  # Expected: True\n\n# Example 2: nested helper approach\ndef solve_problem_5889(left, right):\n    def calculate():\n        return (set(left) - {2}).isdisjoint(set(right) - {2})\n    return calculate()\n\nprint(solve_problem_5889([1, 2], [2, 2]))\n\n# Example 3: static method approach\nclass Problem5889Solution:\n    @staticmethod\n    def disjoint_except_2_set(left, right):\n        return (set(left) - {2}).isdisjoint(set(right) - {2})\n\nprint(Problem5889Solution.disjoint_except_2_set([1, 2], [2, 3]))\n\n# Example 4: assigned result approach\nresult = disjoint_except_2_set([1, 2], [2, 2])\nprint(result)\n\n# Example 5: direct call\nprint(disjoint_except_2_set([], [2]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5890,
    "title": "Problem 5890",
    "description": "Write a Python function called `disjoint_except_3_set` that must test whether sets are disjoint after ignoring value 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  disjoint_except_3_set([1, 3], [2, 3]) -> True\n  disjoint_except_3_set([1, 2], [2, 3]) -> False",
    "initialCode": "def disjoint_except_3_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef disjoint_except_3_set(left, right):\n    return (set(left) - {3}).isdisjoint(set(right) - {3})\n\nprint(disjoint_except_3_set([1, 3], [2, 3]))  # Expected: True\nprint(disjoint_except_3_set([1, 2], [2, 3]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5890(left, right):\n    def calculate():\n        return (set(left) - {3}).isdisjoint(set(right) - {3})\n    return calculate()\n\nprint(solve_problem_5890([1, 3], [2, 3]))\n\n# Example 3: static method approach\nclass Problem5890Solution:\n    @staticmethod\n    def disjoint_except_3_set(left, right):\n        return (set(left) - {3}).isdisjoint(set(right) - {3})\n\nprint(Problem5890Solution.disjoint_except_3_set([1, 2], [2, 3]))\n\n# Example 4: assigned result approach\nresult = disjoint_except_3_set([1, 3], [2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(disjoint_except_3_set([], [3]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5891,
    "title": "Problem 5891",
    "description": "Write a Python function called `disjoint_except_4_set` that must test whether sets are disjoint after ignoring value 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  disjoint_except_4_set([1, 4], [2, 4]) -> True\n  disjoint_except_4_set([1, 2], [2, 3]) -> False",
    "initialCode": "def disjoint_except_4_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef disjoint_except_4_set(left, right):\n    return (set(left) - {4}).isdisjoint(set(right) - {4})\n\nprint(disjoint_except_4_set([1, 4], [2, 4]))  # Expected: True\nprint(disjoint_except_4_set([1, 2], [2, 3]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5891(left, right):\n    def calculate():\n        return (set(left) - {4}).isdisjoint(set(right) - {4})\n    return calculate()\n\nprint(solve_problem_5891([1, 4], [2, 4]))\n\n# Example 3: static method approach\nclass Problem5891Solution:\n    @staticmethod\n    def disjoint_except_4_set(left, right):\n        return (set(left) - {4}).isdisjoint(set(right) - {4})\n\nprint(Problem5891Solution.disjoint_except_4_set([1, 2], [2, 3]))\n\n# Example 4: assigned result approach\nresult = disjoint_except_4_set([1, 4], [2, 4])\nprint(result)\n\n# Example 5: direct call\nprint(disjoint_except_4_set([], [4]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5892,
    "title": "Problem 5892",
    "description": "Write a Python function called `disjoint_except_5_set` that must test whether sets are disjoint after ignoring value 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  disjoint_except_5_set([1, 5], [2, 5]) -> True\n  disjoint_except_5_set([1, 2], [2, 3]) -> False",
    "initialCode": "def disjoint_except_5_set(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef disjoint_except_5_set(left, right):\n    return (set(left) - {5}).isdisjoint(set(right) - {5})\n\nprint(disjoint_except_5_set([1, 5], [2, 5]))  # Expected: True\nprint(disjoint_except_5_set([1, 2], [2, 3]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_5892(left, right):\n    def calculate():\n        return (set(left) - {5}).isdisjoint(set(right) - {5})\n    return calculate()\n\nprint(solve_problem_5892([1, 5], [2, 5]))\n\n# Example 3: static method approach\nclass Problem5892Solution:\n    @staticmethod\n    def disjoint_except_5_set(left, right):\n        return (set(left) - {5}).isdisjoint(set(right) - {5})\n\nprint(Problem5892Solution.disjoint_except_5_set([1, 2], [2, 3]))\n\n# Example 4: assigned result approach\nresult = disjoint_except_5_set([1, 5], [2, 5])\nprint(result)\n\n# Example 5: direct call\nprint(disjoint_except_5_set([], [5]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5893,
    "title": "Problem 5893",
    "description": "Write a Python function called `unique_remainders_1_set` that must return sorted unique remainders modulo 3 using a set. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_remainders_1_set([1, 2, 3, 4, 5]) -> [0, 1, 2]\n  unique_remainders_1_set([]) -> []",
    "initialCode": "def unique_remainders_1_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_remainders_1_set(values):\n    return sorted({value % 3 for value in values})\n\nprint(unique_remainders_1_set([1, 2, 3, 4, 5]))  # Expected: [0, 1, 2]\nprint(unique_remainders_1_set([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5893(values):\n    def calculate():\n        return sorted({value % 3 for value in values})\n    return calculate()\n\nprint(solve_problem_5893([1, 2, 3, 4, 5]))\n\n# Example 3: static method approach\nclass Problem5893Solution:\n    @staticmethod\n    def unique_remainders_1_set(values):\n        return sorted({value % 3 for value in values})\n\nprint(Problem5893Solution.unique_remainders_1_set([]))\n\n# Example 4: assigned result approach\nresult = unique_remainders_1_set([1, 2, 3, 4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(unique_remainders_1_set([-1, 3]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5894,
    "title": "Problem 5894",
    "description": "Write a Python function called `unique_remainders_2_set` that must return sorted unique remainders modulo 4 using a set. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_remainders_2_set([1, 2, 3, 4, 5]) -> [0, 1, 2, 3]\n  unique_remainders_2_set([]) -> []",
    "initialCode": "def unique_remainders_2_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_remainders_2_set(values):\n    return sorted({value % 4 for value in values})\n\nprint(unique_remainders_2_set([1, 2, 3, 4, 5]))  # Expected: [0, 1, 2, 3]\nprint(unique_remainders_2_set([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5894(values):\n    def calculate():\n        return sorted({value % 4 for value in values})\n    return calculate()\n\nprint(solve_problem_5894([1, 2, 3, 4, 5]))\n\n# Example 3: static method approach\nclass Problem5894Solution:\n    @staticmethod\n    def unique_remainders_2_set(values):\n        return sorted({value % 4 for value in values})\n\nprint(Problem5894Solution.unique_remainders_2_set([]))\n\n# Example 4: assigned result approach\nresult = unique_remainders_2_set([1, 2, 3, 4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(unique_remainders_2_set([-1, 4]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5895,
    "title": "Problem 5895",
    "description": "Write a Python function called `unique_remainders_3_set` that must return sorted unique remainders modulo 5 using a set. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_remainders_3_set([1, 2, 3, 4, 5]) -> [0, 1, 2, 3, 4]\n  unique_remainders_3_set([]) -> []",
    "initialCode": "def unique_remainders_3_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_remainders_3_set(values):\n    return sorted({value % 5 for value in values})\n\nprint(unique_remainders_3_set([1, 2, 3, 4, 5]))  # Expected: [0, 1, 2, 3, 4]\nprint(unique_remainders_3_set([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5895(values):\n    def calculate():\n        return sorted({value % 5 for value in values})\n    return calculate()\n\nprint(solve_problem_5895([1, 2, 3, 4, 5]))\n\n# Example 3: static method approach\nclass Problem5895Solution:\n    @staticmethod\n    def unique_remainders_3_set(values):\n        return sorted({value % 5 for value in values})\n\nprint(Problem5895Solution.unique_remainders_3_set([]))\n\n# Example 4: assigned result approach\nresult = unique_remainders_3_set([1, 2, 3, 4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(unique_remainders_3_set([-1, 5]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5896,
    "title": "Problem 5896",
    "description": "Write a Python function called `unique_remainders_4_set` that must return sorted unique remainders modulo 6 using a set. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_remainders_4_set([1, 2, 3, 4, 5]) -> [1, 2, 3, 4, 5]\n  unique_remainders_4_set([]) -> []",
    "initialCode": "def unique_remainders_4_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_remainders_4_set(values):\n    return sorted({value % 6 for value in values})\n\nprint(unique_remainders_4_set([1, 2, 3, 4, 5]))  # Expected: [1, 2, 3, 4, 5]\nprint(unique_remainders_4_set([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5896(values):\n    def calculate():\n        return sorted({value % 6 for value in values})\n    return calculate()\n\nprint(solve_problem_5896([1, 2, 3, 4, 5]))\n\n# Example 3: static method approach\nclass Problem5896Solution:\n    @staticmethod\n    def unique_remainders_4_set(values):\n        return sorted({value % 6 for value in values})\n\nprint(Problem5896Solution.unique_remainders_4_set([]))\n\n# Example 4: assigned result approach\nresult = unique_remainders_4_set([1, 2, 3, 4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(unique_remainders_4_set([-1, 6]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5897,
    "title": "Problem 5897",
    "description": "Write a Python function called `unique_remainders_5_set` that must return sorted unique remainders modulo 7 using a set. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  unique_remainders_5_set([1, 2, 3, 4, 5]) -> [1, 2, 3, 4, 5]\n  unique_remainders_5_set([]) -> []",
    "initialCode": "def unique_remainders_5_set(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unique_remainders_5_set(values):\n    return sorted({value % 7 for value in values})\n\nprint(unique_remainders_5_set([1, 2, 3, 4, 5]))  # Expected: [1, 2, 3, 4, 5]\nprint(unique_remainders_5_set([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5897(values):\n    def calculate():\n        return sorted({value % 7 for value in values})\n    return calculate()\n\nprint(solve_problem_5897([1, 2, 3, 4, 5]))\n\n# Example 3: static method approach\nclass Problem5897Solution:\n    @staticmethod\n    def unique_remainders_5_set(values):\n        return sorted({value % 7 for value in values})\n\nprint(Problem5897Solution.unique_remainders_5_set([]))\n\n# Example 4: assigned result approach\nresult = unique_remainders_5_set([1, 2, 3, 4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(unique_remainders_5_set([-1, 7]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5898,
    "title": "Problem 5898",
    "description": "Write a Python function called `letter_set_without_1` that must return sorted unique characters except digit 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  letter_set_without_1(\"a1ba\") -> [\"a\", \"b\"]\n  letter_set_without_1(\"\") -> []",
    "initialCode": "def letter_set_without_1(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef letter_set_without_1(text):\n    return sorted(set(text) - {\"1\"})\n\nprint(letter_set_without_1(\"a1ba\"))  # Expected: [\"a\", \"b\"]\nprint(letter_set_without_1(\"\"))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5898(text):\n    def calculate():\n        return sorted(set(text) - {\"1\"})\n    return calculate()\n\nprint(solve_problem_5898(\"a1ba\"))\n\n# Example 3: static method approach\nclass Problem5898Solution:\n    @staticmethod\n    def letter_set_without_1(text):\n        return sorted(set(text) - {\"1\"})\n\nprint(Problem5898Solution.letter_set_without_1(\"\"))\n\n# Example 4: assigned result approach\nresult = letter_set_without_1(\"a1ba\")\nprint(result)\n\n# Example 5: direct call\nprint(letter_set_without_1(\"11x\"))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5899,
    "title": "Problem 5899",
    "description": "Write a Python function called `letter_set_without_2` that must return sorted unique characters except digit 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  letter_set_without_2(\"a2ba\") -> [\"a\", \"b\"]\n  letter_set_without_2(\"\") -> []",
    "initialCode": "def letter_set_without_2(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef letter_set_without_2(text):\n    return sorted(set(text) - {\"2\"})\n\nprint(letter_set_without_2(\"a2ba\"))  # Expected: [\"a\", \"b\"]\nprint(letter_set_without_2(\"\"))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5899(text):\n    def calculate():\n        return sorted(set(text) - {\"2\"})\n    return calculate()\n\nprint(solve_problem_5899(\"a2ba\"))\n\n# Example 3: static method approach\nclass Problem5899Solution:\n    @staticmethod\n    def letter_set_without_2(text):\n        return sorted(set(text) - {\"2\"})\n\nprint(Problem5899Solution.letter_set_without_2(\"\"))\n\n# Example 4: assigned result approach\nresult = letter_set_without_2(\"a2ba\")\nprint(result)\n\n# Example 5: direct call\nprint(letter_set_without_2(\"22x\"))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5900,
    "title": "Problem 5900",
    "description": "Write a Python function called `letter_set_without_3` that must return sorted unique characters except digit 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  letter_set_without_3(\"a3ba\") -> [\"a\", \"b\"]\n  letter_set_without_3(\"\") -> []",
    "initialCode": "def letter_set_without_3(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef letter_set_without_3(text):\n    return sorted(set(text) - {\"3\"})\n\nprint(letter_set_without_3(\"a3ba\"))  # Expected: [\"a\", \"b\"]\nprint(letter_set_without_3(\"\"))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5900(text):\n    def calculate():\n        return sorted(set(text) - {\"3\"})\n    return calculate()\n\nprint(solve_problem_5900(\"a3ba\"))\n\n# Example 3: static method approach\nclass Problem5900Solution:\n    @staticmethod\n    def letter_set_without_3(text):\n        return sorted(set(text) - {\"3\"})\n\nprint(Problem5900Solution.letter_set_without_3(\"\"))\n\n# Example 4: assigned result approach\nresult = letter_set_without_3(\"a3ba\")\nprint(result)\n\n# Example 5: direct call\nprint(letter_set_without_3(\"33x\"))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5901,
    "title": "Problem 5901",
    "description": "Write a Python function called `letter_set_without_4` that must return sorted unique characters except digit 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  letter_set_without_4(\"a4ba\") -> [\"a\", \"b\"]\n  letter_set_without_4(\"\") -> []",
    "initialCode": "def letter_set_without_4(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef letter_set_without_4(text):\n    return sorted(set(text) - {\"4\"})\n\nprint(letter_set_without_4(\"a4ba\"))  # Expected: [\"a\", \"b\"]\nprint(letter_set_without_4(\"\"))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5901(text):\n    def calculate():\n        return sorted(set(text) - {\"4\"})\n    return calculate()\n\nprint(solve_problem_5901(\"a4ba\"))\n\n# Example 3: static method approach\nclass Problem5901Solution:\n    @staticmethod\n    def letter_set_without_4(text):\n        return sorted(set(text) - {\"4\"})\n\nprint(Problem5901Solution.letter_set_without_4(\"\"))\n\n# Example 4: assigned result approach\nresult = letter_set_without_4(\"a4ba\")\nprint(result)\n\n# Example 5: direct call\nprint(letter_set_without_4(\"44x\"))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5902,
    "title": "Problem 5902",
    "description": "Write a Python function called `letter_set_without_5` that must return sorted unique characters except digit 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  letter_set_without_5(\"a5ba\") -> [\"a\", \"b\"]\n  letter_set_without_5(\"\") -> []",
    "initialCode": "def letter_set_without_5(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef letter_set_without_5(text):\n    return sorted(set(text) - {\"5\"})\n\nprint(letter_set_without_5(\"a5ba\"))  # Expected: [\"a\", \"b\"]\nprint(letter_set_without_5(\"\"))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5902(text):\n    def calculate():\n        return sorted(set(text) - {\"5\"})\n    return calculate()\n\nprint(solve_problem_5902(\"a5ba\"))\n\n# Example 3: static method approach\nclass Problem5902Solution:\n    @staticmethod\n    def letter_set_without_5(text):\n        return sorted(set(text) - {\"5\"})\n\nprint(Problem5902Solution.letter_set_without_5(\"\"))\n\n# Example 4: assigned result approach\nresult = letter_set_without_5(\"a5ba\")\nprint(result)\n\n# Example 5: direct call\nprint(letter_set_without_5(\"55x\"))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5903,
    "title": "Problem 5903",
    "description": "Write a Python function called `set_values_at_least_1` that must return sorted unique values that are at least 1. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  set_values_at_least_1([0, 1, 2, 1]) -> [1, 2]\n  set_values_at_least_1([]) -> []",
    "initialCode": "def set_values_at_least_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef set_values_at_least_1(values):\n    return sorted({value for value in values if value >= 1})\n\nprint(set_values_at_least_1([0, 1, 2, 1]))  # Expected: [1, 2]\nprint(set_values_at_least_1([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5903(values):\n    def calculate():\n        return sorted({value for value in values if value >= 1})\n    return calculate()\n\nprint(solve_problem_5903([0, 1, 2, 1]))\n\n# Example 3: static method approach\nclass Problem5903Solution:\n    @staticmethod\n    def set_values_at_least_1(values):\n        return sorted({value for value in values if value >= 1})\n\nprint(Problem5903Solution.set_values_at_least_1([]))\n\n# Example 4: assigned result approach\nresult = set_values_at_least_1([0, 1, 2, 1])\nprint(result)\n\n# Example 5: direct call\nprint(set_values_at_least_1([-2, 20]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5904,
    "title": "Problem 5904",
    "description": "Write a Python function called `set_values_at_least_2` that must return sorted unique values that are at least 2. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  set_values_at_least_2([0, 2, 3, 2]) -> [2, 3]\n  set_values_at_least_2([]) -> []",
    "initialCode": "def set_values_at_least_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef set_values_at_least_2(values):\n    return sorted({value for value in values if value >= 2})\n\nprint(set_values_at_least_2([0, 2, 3, 2]))  # Expected: [2, 3]\nprint(set_values_at_least_2([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5904(values):\n    def calculate():\n        return sorted({value for value in values if value >= 2})\n    return calculate()\n\nprint(solve_problem_5904([0, 2, 3, 2]))\n\n# Example 3: static method approach\nclass Problem5904Solution:\n    @staticmethod\n    def set_values_at_least_2(values):\n        return sorted({value for value in values if value >= 2})\n\nprint(Problem5904Solution.set_values_at_least_2([]))\n\n# Example 4: assigned result approach\nresult = set_values_at_least_2([0, 2, 3, 2])\nprint(result)\n\n# Example 5: direct call\nprint(set_values_at_least_2([-2, 20]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5905,
    "title": "Problem 5905",
    "description": "Write a Python function called `set_values_at_least_3` that must return sorted unique values that are at least 3. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  set_values_at_least_3([0, 3, 4, 3]) -> [3, 4]\n  set_values_at_least_3([]) -> []",
    "initialCode": "def set_values_at_least_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef set_values_at_least_3(values):\n    return sorted({value for value in values if value >= 3})\n\nprint(set_values_at_least_3([0, 3, 4, 3]))  # Expected: [3, 4]\nprint(set_values_at_least_3([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5905(values):\n    def calculate():\n        return sorted({value for value in values if value >= 3})\n    return calculate()\n\nprint(solve_problem_5905([0, 3, 4, 3]))\n\n# Example 3: static method approach\nclass Problem5905Solution:\n    @staticmethod\n    def set_values_at_least_3(values):\n        return sorted({value for value in values if value >= 3})\n\nprint(Problem5905Solution.set_values_at_least_3([]))\n\n# Example 4: assigned result approach\nresult = set_values_at_least_3([0, 3, 4, 3])\nprint(result)\n\n# Example 5: direct call\nprint(set_values_at_least_3([-2, 20]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5906,
    "title": "Problem 5906",
    "description": "Write a Python function called `set_values_at_least_4` that must return sorted unique values that are at least 4. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  set_values_at_least_4([0, 4, 5, 4]) -> [4, 5]\n  set_values_at_least_4([]) -> []",
    "initialCode": "def set_values_at_least_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef set_values_at_least_4(values):\n    return sorted({value for value in values if value >= 4})\n\nprint(set_values_at_least_4([0, 4, 5, 4]))  # Expected: [4, 5]\nprint(set_values_at_least_4([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5906(values):\n    def calculate():\n        return sorted({value for value in values if value >= 4})\n    return calculate()\n\nprint(solve_problem_5906([0, 4, 5, 4]))\n\n# Example 3: static method approach\nclass Problem5906Solution:\n    @staticmethod\n    def set_values_at_least_4(values):\n        return sorted({value for value in values if value >= 4})\n\nprint(Problem5906Solution.set_values_at_least_4([]))\n\n# Example 4: assigned result approach\nresult = set_values_at_least_4([0, 4, 5, 4])\nprint(result)\n\n# Example 5: direct call\nprint(set_values_at_least_4([-2, 20]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5907,
    "title": "Problem 5907",
    "description": "Write a Python function called `set_values_at_least_5` that must return sorted unique values that are at least 5. Practice set syntax.\nDifficulty: Easy.\nExamples:\n  set_values_at_least_5([0, 5, 6, 5]) -> [5, 6]\n  set_values_at_least_5([]) -> []",
    "initialCode": "def set_values_at_least_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef set_values_at_least_5(values):\n    return sorted({value for value in values if value >= 5})\n\nprint(set_values_at_least_5([0, 5, 6, 5]))  # Expected: [5, 6]\nprint(set_values_at_least_5([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5907(values):\n    def calculate():\n        return sorted({value for value in values if value >= 5})\n    return calculate()\n\nprint(solve_problem_5907([0, 5, 6, 5]))\n\n# Example 3: static method approach\nclass Problem5907Solution:\n    @staticmethod\n    def set_values_at_least_5(values):\n        return sorted({value for value in values if value >= 5})\n\nprint(Problem5907Solution.set_values_at_least_5([]))\n\n# Example 4: assigned result approach\nresult = set_values_at_least_5([0, 5, 6, 5])\nprint(result)\n\n# Example 5: direct call\nprint(set_values_at_least_5([-2, 20]))",
    "hint": "Focus on unique membership, the selected set operation, and deterministic sorted output. Use the required set structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the set structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Set Easy"
  },
  {
    "id": 5908,
    "title": "Problem 5908",
    "description": "Write a Python function called `square_plus_1_comprehension` that must return each value squared plus 1 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  square_plus_1_comprehension([1, 2, 3]) -> [2, 5, 10]\n  square_plus_1_comprehension([-2, 0]) -> [5, 1]",
    "initialCode": "def square_plus_1_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_plus_1_comprehension(values):\n    return [value ** 2 + 1 for value in values]\n\nprint(square_plus_1_comprehension([1, 2, 3]))  # Expected: [2, 5, 10]\nprint(square_plus_1_comprehension([-2, 0]))  # Expected: [5, 1]\n\n# Example 2: nested helper approach\ndef solve_problem_5908(values):\n    def calculate():\n        return [value ** 2 + 1 for value in values]\n    return calculate()\n\nprint(solve_problem_5908([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5908Solution:\n    @staticmethod\n    def square_plus_1_comprehension(values):\n        return [value ** 2 + 1 for value in values]\n\nprint(Problem5908Solution.square_plus_1_comprehension([-2, 0]))\n\n# Example 4: assigned result approach\nresult = square_plus_1_comprehension([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_plus_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5909,
    "title": "Problem 5909",
    "description": "Write a Python function called `square_plus_2_comprehension` that must return each value squared plus 2 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  square_plus_2_comprehension([1, 2, 3]) -> [3, 6, 11]\n  square_plus_2_comprehension([-2, 0]) -> [6, 2]",
    "initialCode": "def square_plus_2_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_plus_2_comprehension(values):\n    return [value ** 2 + 2 for value in values]\n\nprint(square_plus_2_comprehension([1, 2, 3]))  # Expected: [3, 6, 11]\nprint(square_plus_2_comprehension([-2, 0]))  # Expected: [6, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5909(values):\n    def calculate():\n        return [value ** 2 + 2 for value in values]\n    return calculate()\n\nprint(solve_problem_5909([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5909Solution:\n    @staticmethod\n    def square_plus_2_comprehension(values):\n        return [value ** 2 + 2 for value in values]\n\nprint(Problem5909Solution.square_plus_2_comprehension([-2, 0]))\n\n# Example 4: assigned result approach\nresult = square_plus_2_comprehension([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_plus_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5910,
    "title": "Problem 5910",
    "description": "Write a Python function called `square_plus_3_comprehension` that must return each value squared plus 3 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  square_plus_3_comprehension([1, 2, 3]) -> [4, 7, 12]\n  square_plus_3_comprehension([-2, 0]) -> [7, 3]",
    "initialCode": "def square_plus_3_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_plus_3_comprehension(values):\n    return [value ** 2 + 3 for value in values]\n\nprint(square_plus_3_comprehension([1, 2, 3]))  # Expected: [4, 7, 12]\nprint(square_plus_3_comprehension([-2, 0]))  # Expected: [7, 3]\n\n# Example 2: nested helper approach\ndef solve_problem_5910(values):\n    def calculate():\n        return [value ** 2 + 3 for value in values]\n    return calculate()\n\nprint(solve_problem_5910([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5910Solution:\n    @staticmethod\n    def square_plus_3_comprehension(values):\n        return [value ** 2 + 3 for value in values]\n\nprint(Problem5910Solution.square_plus_3_comprehension([-2, 0]))\n\n# Example 4: assigned result approach\nresult = square_plus_3_comprehension([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_plus_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5911,
    "title": "Problem 5911",
    "description": "Write a Python function called `square_plus_4_comprehension` that must return each value squared plus 4 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  square_plus_4_comprehension([1, 2, 3]) -> [5, 8, 13]\n  square_plus_4_comprehension([-2, 0]) -> [8, 4]",
    "initialCode": "def square_plus_4_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_plus_4_comprehension(values):\n    return [value ** 2 + 4 for value in values]\n\nprint(square_plus_4_comprehension([1, 2, 3]))  # Expected: [5, 8, 13]\nprint(square_plus_4_comprehension([-2, 0]))  # Expected: [8, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_5911(values):\n    def calculate():\n        return [value ** 2 + 4 for value in values]\n    return calculate()\n\nprint(solve_problem_5911([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5911Solution:\n    @staticmethod\n    def square_plus_4_comprehension(values):\n        return [value ** 2 + 4 for value in values]\n\nprint(Problem5911Solution.square_plus_4_comprehension([-2, 0]))\n\n# Example 4: assigned result approach\nresult = square_plus_4_comprehension([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_plus_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5912,
    "title": "Problem 5912",
    "description": "Write a Python function called `square_plus_5_comprehension` that must return each value squared plus 5 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  square_plus_5_comprehension([1, 2, 3]) -> [6, 9, 14]\n  square_plus_5_comprehension([-2, 0]) -> [9, 5]",
    "initialCode": "def square_plus_5_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_plus_5_comprehension(values):\n    return [value ** 2 + 5 for value in values]\n\nprint(square_plus_5_comprehension([1, 2, 3]))  # Expected: [6, 9, 14]\nprint(square_plus_5_comprehension([-2, 0]))  # Expected: [9, 5]\n\n# Example 2: nested helper approach\ndef solve_problem_5912(values):\n    def calculate():\n        return [value ** 2 + 5 for value in values]\n    return calculate()\n\nprint(solve_problem_5912([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5912Solution:\n    @staticmethod\n    def square_plus_5_comprehension(values):\n        return [value ** 2 + 5 for value in values]\n\nprint(Problem5912Solution.square_plus_5_comprehension([-2, 0]))\n\n# Example 4: assigned result approach\nresult = square_plus_5_comprehension([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_plus_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5913,
    "title": "Problem 5913",
    "description": "Write a Python function called `divisible_1_comprehension` that must keep values divisible by 2 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  divisible_1_comprehension([1, 2, 3, 4, 6]) -> [2, 4, 6]\n  divisible_1_comprehension([2]) -> [2]",
    "initialCode": "def divisible_1_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_1_comprehension(values):\n    return [value for value in values if value % 2 == 0]\n\nprint(divisible_1_comprehension([1, 2, 3, 4, 6]))  # Expected: [2, 4, 6]\nprint(divisible_1_comprehension([2]))  # Expected: [2]\n\n# Example 2: nested helper approach\ndef solve_problem_5913(values):\n    def calculate():\n        return [value for value in values if value % 2 == 0]\n    return calculate()\n\nprint(solve_problem_5913([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5913Solution:\n    @staticmethod\n    def divisible_1_comprehension(values):\n        return [value for value in values if value % 2 == 0]\n\nprint(Problem5913Solution.divisible_1_comprehension([2]))\n\n# Example 4: assigned result approach\nresult = divisible_1_comprehension([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(divisible_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5914,
    "title": "Problem 5914",
    "description": "Write a Python function called `divisible_2_comprehension` that must keep values divisible by 3 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  divisible_2_comprehension([1, 2, 3, 4, 6]) -> [3, 6]\n  divisible_2_comprehension([3]) -> [3]",
    "initialCode": "def divisible_2_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_2_comprehension(values):\n    return [value for value in values if value % 3 == 0]\n\nprint(divisible_2_comprehension([1, 2, 3, 4, 6]))  # Expected: [3, 6]\nprint(divisible_2_comprehension([3]))  # Expected: [3]\n\n# Example 2: nested helper approach\ndef solve_problem_5914(values):\n    def calculate():\n        return [value for value in values if value % 3 == 0]\n    return calculate()\n\nprint(solve_problem_5914([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5914Solution:\n    @staticmethod\n    def divisible_2_comprehension(values):\n        return [value for value in values if value % 3 == 0]\n\nprint(Problem5914Solution.divisible_2_comprehension([3]))\n\n# Example 4: assigned result approach\nresult = divisible_2_comprehension([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(divisible_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5915,
    "title": "Problem 5915",
    "description": "Write a Python function called `divisible_3_comprehension` that must keep values divisible by 4 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  divisible_3_comprehension([1, 2, 3, 4, 6]) -> [4]\n  divisible_3_comprehension([4]) -> [4]",
    "initialCode": "def divisible_3_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_3_comprehension(values):\n    return [value for value in values if value % 4 == 0]\n\nprint(divisible_3_comprehension([1, 2, 3, 4, 6]))  # Expected: [4]\nprint(divisible_3_comprehension([4]))  # Expected: [4]\n\n# Example 2: nested helper approach\ndef solve_problem_5915(values):\n    def calculate():\n        return [value for value in values if value % 4 == 0]\n    return calculate()\n\nprint(solve_problem_5915([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5915Solution:\n    @staticmethod\n    def divisible_3_comprehension(values):\n        return [value for value in values if value % 4 == 0]\n\nprint(Problem5915Solution.divisible_3_comprehension([4]))\n\n# Example 4: assigned result approach\nresult = divisible_3_comprehension([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(divisible_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5916,
    "title": "Problem 5916",
    "description": "Write a Python function called `divisible_4_comprehension` that must keep values divisible by 5 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  divisible_4_comprehension([1, 2, 3, 4, 6]) -> []\n  divisible_4_comprehension([5]) -> [5]",
    "initialCode": "def divisible_4_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_4_comprehension(values):\n    return [value for value in values if value % 5 == 0]\n\nprint(divisible_4_comprehension([1, 2, 3, 4, 6]))  # Expected: []\nprint(divisible_4_comprehension([5]))  # Expected: [5]\n\n# Example 2: nested helper approach\ndef solve_problem_5916(values):\n    def calculate():\n        return [value for value in values if value % 5 == 0]\n    return calculate()\n\nprint(solve_problem_5916([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5916Solution:\n    @staticmethod\n    def divisible_4_comprehension(values):\n        return [value for value in values if value % 5 == 0]\n\nprint(Problem5916Solution.divisible_4_comprehension([5]))\n\n# Example 4: assigned result approach\nresult = divisible_4_comprehension([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(divisible_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5917,
    "title": "Problem 5917",
    "description": "Write a Python function called `divisible_5_comprehension` that must keep values divisible by 6 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  divisible_5_comprehension([1, 2, 3, 4, 6]) -> [6]\n  divisible_5_comprehension([6]) -> [6]",
    "initialCode": "def divisible_5_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef divisible_5_comprehension(values):\n    return [value for value in values if value % 6 == 0]\n\nprint(divisible_5_comprehension([1, 2, 3, 4, 6]))  # Expected: [6]\nprint(divisible_5_comprehension([6]))  # Expected: [6]\n\n# Example 2: nested helper approach\ndef solve_problem_5917(values):\n    def calculate():\n        return [value for value in values if value % 6 == 0]\n    return calculate()\n\nprint(solve_problem_5917([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5917Solution:\n    @staticmethod\n    def divisible_5_comprehension(values):\n        return [value for value in values if value % 6 == 0]\n\nprint(Problem5917Solution.divisible_5_comprehension([6]))\n\n# Example 4: assigned result approach\nresult = divisible_5_comprehension([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(divisible_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5918,
    "title": "Problem 5918",
    "description": "Write a Python function called `mapping_plus_1_comprehension` that must map each value's text to that value plus 1 with a dictionary comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  mapping_plus_1_comprehension([1, 2]) -> {\"1\": 2, \"2\": 3}\n  mapping_plus_1_comprehension([-1, 0]) -> {\"0\": 1, \"-1\": 0}",
    "initialCode": "def mapping_plus_1_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef mapping_plus_1_comprehension(values):\n    return {str(value): value + 1 for value in values}\n\nprint(mapping_plus_1_comprehension([1, 2]))  # Expected: {\"1\": 2, \"2\": 3}\nprint(mapping_plus_1_comprehension([-1, 0]))  # Expected: {\"0\": 1, \"-1\": 0}\n\n# Example 2: nested helper approach\ndef solve_problem_5918(values):\n    def calculate():\n        return {str(value): value + 1 for value in values}\n    return calculate()\n\nprint(solve_problem_5918([1, 2]))\n\n# Example 3: static method approach\nclass Problem5918Solution:\n    @staticmethod\n    def mapping_plus_1_comprehension(values):\n        return {str(value): value + 1 for value in values}\n\nprint(Problem5918Solution.mapping_plus_1_comprehension([-1, 0]))\n\n# Example 4: assigned result approach\nresult = mapping_plus_1_comprehension([1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(mapping_plus_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5919,
    "title": "Problem 5919",
    "description": "Write a Python function called `mapping_plus_2_comprehension` that must map each value's text to that value plus 2 with a dictionary comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  mapping_plus_2_comprehension([1, 2]) -> {\"1\": 3, \"2\": 4}\n  mapping_plus_2_comprehension([-1, 0]) -> {\"0\": 2, \"-1\": 1}",
    "initialCode": "def mapping_plus_2_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef mapping_plus_2_comprehension(values):\n    return {str(value): value + 2 for value in values}\n\nprint(mapping_plus_2_comprehension([1, 2]))  # Expected: {\"1\": 3, \"2\": 4}\nprint(mapping_plus_2_comprehension([-1, 0]))  # Expected: {\"0\": 2, \"-1\": 1}\n\n# Example 2: nested helper approach\ndef solve_problem_5919(values):\n    def calculate():\n        return {str(value): value + 2 for value in values}\n    return calculate()\n\nprint(solve_problem_5919([1, 2]))\n\n# Example 3: static method approach\nclass Problem5919Solution:\n    @staticmethod\n    def mapping_plus_2_comprehension(values):\n        return {str(value): value + 2 for value in values}\n\nprint(Problem5919Solution.mapping_plus_2_comprehension([-1, 0]))\n\n# Example 4: assigned result approach\nresult = mapping_plus_2_comprehension([1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(mapping_plus_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5920,
    "title": "Problem 5920",
    "description": "Write a Python function called `mapping_plus_3_comprehension` that must map each value's text to that value plus 3 with a dictionary comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  mapping_plus_3_comprehension([1, 2]) -> {\"1\": 4, \"2\": 5}\n  mapping_plus_3_comprehension([-1, 0]) -> {\"0\": 3, \"-1\": 2}",
    "initialCode": "def mapping_plus_3_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef mapping_plus_3_comprehension(values):\n    return {str(value): value + 3 for value in values}\n\nprint(mapping_plus_3_comprehension([1, 2]))  # Expected: {\"1\": 4, \"2\": 5}\nprint(mapping_plus_3_comprehension([-1, 0]))  # Expected: {\"0\": 3, \"-1\": 2}\n\n# Example 2: nested helper approach\ndef solve_problem_5920(values):\n    def calculate():\n        return {str(value): value + 3 for value in values}\n    return calculate()\n\nprint(solve_problem_5920([1, 2]))\n\n# Example 3: static method approach\nclass Problem5920Solution:\n    @staticmethod\n    def mapping_plus_3_comprehension(values):\n        return {str(value): value + 3 for value in values}\n\nprint(Problem5920Solution.mapping_plus_3_comprehension([-1, 0]))\n\n# Example 4: assigned result approach\nresult = mapping_plus_3_comprehension([1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(mapping_plus_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5921,
    "title": "Problem 5921",
    "description": "Write a Python function called `mapping_plus_4_comprehension` that must map each value's text to that value plus 4 with a dictionary comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  mapping_plus_4_comprehension([1, 2]) -> {\"1\": 5, \"2\": 6}\n  mapping_plus_4_comprehension([-1, 0]) -> {\"0\": 4, \"-1\": 3}",
    "initialCode": "def mapping_plus_4_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef mapping_plus_4_comprehension(values):\n    return {str(value): value + 4 for value in values}\n\nprint(mapping_plus_4_comprehension([1, 2]))  # Expected: {\"1\": 5, \"2\": 6}\nprint(mapping_plus_4_comprehension([-1, 0]))  # Expected: {\"0\": 4, \"-1\": 3}\n\n# Example 2: nested helper approach\ndef solve_problem_5921(values):\n    def calculate():\n        return {str(value): value + 4 for value in values}\n    return calculate()\n\nprint(solve_problem_5921([1, 2]))\n\n# Example 3: static method approach\nclass Problem5921Solution:\n    @staticmethod\n    def mapping_plus_4_comprehension(values):\n        return {str(value): value + 4 for value in values}\n\nprint(Problem5921Solution.mapping_plus_4_comprehension([-1, 0]))\n\n# Example 4: assigned result approach\nresult = mapping_plus_4_comprehension([1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(mapping_plus_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5922,
    "title": "Problem 5922",
    "description": "Write a Python function called `mapping_plus_5_comprehension` that must map each value's text to that value plus 5 with a dictionary comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  mapping_plus_5_comprehension([1, 2]) -> {\"1\": 6, \"2\": 7}\n  mapping_plus_5_comprehension([-1, 0]) -> {\"0\": 5, \"-1\": 4}",
    "initialCode": "def mapping_plus_5_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef mapping_plus_5_comprehension(values):\n    return {str(value): value + 5 for value in values}\n\nprint(mapping_plus_5_comprehension([1, 2]))  # Expected: {\"1\": 6, \"2\": 7}\nprint(mapping_plus_5_comprehension([-1, 0]))  # Expected: {\"0\": 5, \"-1\": 4}\n\n# Example 2: nested helper approach\ndef solve_problem_5922(values):\n    def calculate():\n        return {str(value): value + 5 for value in values}\n    return calculate()\n\nprint(solve_problem_5922([1, 2]))\n\n# Example 3: static method approach\nclass Problem5922Solution:\n    @staticmethod\n    def mapping_plus_5_comprehension(values):\n        return {str(value): value + 5 for value in values}\n\nprint(Problem5922Solution.mapping_plus_5_comprehension([-1, 0]))\n\n# Example 4: assigned result approach\nresult = mapping_plus_5_comprehension([1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(mapping_plus_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5923,
    "title": "Problem 5923",
    "description": "Write a Python function called `remainder_1_comprehension` that must return sorted unique remainders modulo 3 with a set comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  remainder_1_comprehension([1, 2, 3, 4]) -> [0, 1, 2]\n  remainder_1_comprehension([-1, 3]) -> [0, 2]",
    "initialCode": "def remainder_1_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef remainder_1_comprehension(values):\n    return sorted({value % 3 for value in values})\n\nprint(remainder_1_comprehension([1, 2, 3, 4]))  # Expected: [0, 1, 2]\nprint(remainder_1_comprehension([-1, 3]))  # Expected: [0, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_5923(values):\n    def calculate():\n        return sorted({value % 3 for value in values})\n    return calculate()\n\nprint(solve_problem_5923([1, 2, 3, 4]))\n\n# Example 3: static method approach\nclass Problem5923Solution:\n    @staticmethod\n    def remainder_1_comprehension(values):\n        return sorted({value % 3 for value in values})\n\nprint(Problem5923Solution.remainder_1_comprehension([-1, 3]))\n\n# Example 4: assigned result approach\nresult = remainder_1_comprehension([1, 2, 3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(remainder_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5924,
    "title": "Problem 5924",
    "description": "Write a Python function called `remainder_2_comprehension` that must return sorted unique remainders modulo 4 with a set comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  remainder_2_comprehension([1, 2, 3, 4]) -> [0, 1, 2, 3]\n  remainder_2_comprehension([-1, 4]) -> [0, 3]",
    "initialCode": "def remainder_2_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef remainder_2_comprehension(values):\n    return sorted({value % 4 for value in values})\n\nprint(remainder_2_comprehension([1, 2, 3, 4]))  # Expected: [0, 1, 2, 3]\nprint(remainder_2_comprehension([-1, 4]))  # Expected: [0, 3]\n\n# Example 2: nested helper approach\ndef solve_problem_5924(values):\n    def calculate():\n        return sorted({value % 4 for value in values})\n    return calculate()\n\nprint(solve_problem_5924([1, 2, 3, 4]))\n\n# Example 3: static method approach\nclass Problem5924Solution:\n    @staticmethod\n    def remainder_2_comprehension(values):\n        return sorted({value % 4 for value in values})\n\nprint(Problem5924Solution.remainder_2_comprehension([-1, 4]))\n\n# Example 4: assigned result approach\nresult = remainder_2_comprehension([1, 2, 3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(remainder_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5925,
    "title": "Problem 5925",
    "description": "Write a Python function called `remainder_3_comprehension` that must return sorted unique remainders modulo 5 with a set comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  remainder_3_comprehension([1, 2, 3, 4]) -> [1, 2, 3, 4]\n  remainder_3_comprehension([-1, 5]) -> [0, 4]",
    "initialCode": "def remainder_3_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef remainder_3_comprehension(values):\n    return sorted({value % 5 for value in values})\n\nprint(remainder_3_comprehension([1, 2, 3, 4]))  # Expected: [1, 2, 3, 4]\nprint(remainder_3_comprehension([-1, 5]))  # Expected: [0, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_5925(values):\n    def calculate():\n        return sorted({value % 5 for value in values})\n    return calculate()\n\nprint(solve_problem_5925([1, 2, 3, 4]))\n\n# Example 3: static method approach\nclass Problem5925Solution:\n    @staticmethod\n    def remainder_3_comprehension(values):\n        return sorted({value % 5 for value in values})\n\nprint(Problem5925Solution.remainder_3_comprehension([-1, 5]))\n\n# Example 4: assigned result approach\nresult = remainder_3_comprehension([1, 2, 3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(remainder_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5926,
    "title": "Problem 5926",
    "description": "Write a Python function called `remainder_4_comprehension` that must return sorted unique remainders modulo 6 with a set comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  remainder_4_comprehension([1, 2, 3, 4]) -> [1, 2, 3, 4]\n  remainder_4_comprehension([-1, 6]) -> [0, 5]",
    "initialCode": "def remainder_4_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef remainder_4_comprehension(values):\n    return sorted({value % 6 for value in values})\n\nprint(remainder_4_comprehension([1, 2, 3, 4]))  # Expected: [1, 2, 3, 4]\nprint(remainder_4_comprehension([-1, 6]))  # Expected: [0, 5]\n\n# Example 2: nested helper approach\ndef solve_problem_5926(values):\n    def calculate():\n        return sorted({value % 6 for value in values})\n    return calculate()\n\nprint(solve_problem_5926([1, 2, 3, 4]))\n\n# Example 3: static method approach\nclass Problem5926Solution:\n    @staticmethod\n    def remainder_4_comprehension(values):\n        return sorted({value % 6 for value in values})\n\nprint(Problem5926Solution.remainder_4_comprehension([-1, 6]))\n\n# Example 4: assigned result approach\nresult = remainder_4_comprehension([1, 2, 3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(remainder_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5927,
    "title": "Problem 5927",
    "description": "Write a Python function called `remainder_5_comprehension` that must return sorted unique remainders modulo 7 with a set comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  remainder_5_comprehension([1, 2, 3, 4]) -> [1, 2, 3, 4]\n  remainder_5_comprehension([-1, 7]) -> [0, 6]",
    "initialCode": "def remainder_5_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef remainder_5_comprehension(values):\n    return sorted({value % 7 for value in values})\n\nprint(remainder_5_comprehension([1, 2, 3, 4]))  # Expected: [1, 2, 3, 4]\nprint(remainder_5_comprehension([-1, 7]))  # Expected: [0, 6]\n\n# Example 2: nested helper approach\ndef solve_problem_5927(values):\n    def calculate():\n        return sorted({value % 7 for value in values})\n    return calculate()\n\nprint(solve_problem_5927([1, 2, 3, 4]))\n\n# Example 3: static method approach\nclass Problem5927Solution:\n    @staticmethod\n    def remainder_5_comprehension(values):\n        return sorted({value % 7 for value in values})\n\nprint(Problem5927Solution.remainder_5_comprehension([-1, 7]))\n\n# Example 4: assigned result approach\nresult = remainder_5_comprehension([1, 2, 3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(remainder_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5928,
    "title": "Problem 5928",
    "description": "Write a Python function called `uppercase_long_1_comprehension` that must uppercase words with at least 1 characters using a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  uppercase_long_1_comprehension([\"a\", \"python\", \"code\"]) -> [\"A\", \"PYTHON\", \"CODE\"]\n  uppercase_long_1_comprehension([\"x\"]) -> [\"X\"]",
    "initialCode": "def uppercase_long_1_comprehension(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef uppercase_long_1_comprehension(words):\n    return [word.upper() for word in words if len(word) >= 1]\n\nprint(uppercase_long_1_comprehension([\"a\", \"python\", \"code\"]))  # Expected: [\"A\", \"PYTHON\", \"CODE\"]\nprint(uppercase_long_1_comprehension([\"x\"]))  # Expected: [\"X\"]\n\n# Example 2: nested helper approach\ndef solve_problem_5928(words):\n    def calculate():\n        return [word.upper() for word in words if len(word) >= 1]\n    return calculate()\n\nprint(solve_problem_5928([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5928Solution:\n    @staticmethod\n    def uppercase_long_1_comprehension(words):\n        return [word.upper() for word in words if len(word) >= 1]\n\nprint(Problem5928Solution.uppercase_long_1_comprehension([\"x\"]))\n\n# Example 4: assigned result approach\nresult = uppercase_long_1_comprehension([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(uppercase_long_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5929,
    "title": "Problem 5929",
    "description": "Write a Python function called `uppercase_long_2_comprehension` that must uppercase words with at least 2 characters using a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  uppercase_long_2_comprehension([\"a\", \"python\", \"code\"]) -> [\"PYTHON\", \"CODE\"]\n  uppercase_long_2_comprehension([\"x\"]) -> []",
    "initialCode": "def uppercase_long_2_comprehension(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef uppercase_long_2_comprehension(words):\n    return [word.upper() for word in words if len(word) >= 2]\n\nprint(uppercase_long_2_comprehension([\"a\", \"python\", \"code\"]))  # Expected: [\"PYTHON\", \"CODE\"]\nprint(uppercase_long_2_comprehension([\"x\"]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5929(words):\n    def calculate():\n        return [word.upper() for word in words if len(word) >= 2]\n    return calculate()\n\nprint(solve_problem_5929([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5929Solution:\n    @staticmethod\n    def uppercase_long_2_comprehension(words):\n        return [word.upper() for word in words if len(word) >= 2]\n\nprint(Problem5929Solution.uppercase_long_2_comprehension([\"x\"]))\n\n# Example 4: assigned result approach\nresult = uppercase_long_2_comprehension([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(uppercase_long_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5930,
    "title": "Problem 5930",
    "description": "Write a Python function called `uppercase_long_3_comprehension` that must uppercase words with at least 3 characters using a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  uppercase_long_3_comprehension([\"a\", \"python\", \"code\"]) -> [\"PYTHON\", \"CODE\"]\n  uppercase_long_3_comprehension([\"x\"]) -> []",
    "initialCode": "def uppercase_long_3_comprehension(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef uppercase_long_3_comprehension(words):\n    return [word.upper() for word in words if len(word) >= 3]\n\nprint(uppercase_long_3_comprehension([\"a\", \"python\", \"code\"]))  # Expected: [\"PYTHON\", \"CODE\"]\nprint(uppercase_long_3_comprehension([\"x\"]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5930(words):\n    def calculate():\n        return [word.upper() for word in words if len(word) >= 3]\n    return calculate()\n\nprint(solve_problem_5930([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5930Solution:\n    @staticmethod\n    def uppercase_long_3_comprehension(words):\n        return [word.upper() for word in words if len(word) >= 3]\n\nprint(Problem5930Solution.uppercase_long_3_comprehension([\"x\"]))\n\n# Example 4: assigned result approach\nresult = uppercase_long_3_comprehension([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(uppercase_long_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5931,
    "title": "Problem 5931",
    "description": "Write a Python function called `uppercase_long_4_comprehension` that must uppercase words with at least 4 characters using a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  uppercase_long_4_comprehension([\"a\", \"python\", \"code\"]) -> [\"PYTHON\", \"CODE\"]\n  uppercase_long_4_comprehension([\"x\"]) -> []",
    "initialCode": "def uppercase_long_4_comprehension(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef uppercase_long_4_comprehension(words):\n    return [word.upper() for word in words if len(word) >= 4]\n\nprint(uppercase_long_4_comprehension([\"a\", \"python\", \"code\"]))  # Expected: [\"PYTHON\", \"CODE\"]\nprint(uppercase_long_4_comprehension([\"x\"]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5931(words):\n    def calculate():\n        return [word.upper() for word in words if len(word) >= 4]\n    return calculate()\n\nprint(solve_problem_5931([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5931Solution:\n    @staticmethod\n    def uppercase_long_4_comprehension(words):\n        return [word.upper() for word in words if len(word) >= 4]\n\nprint(Problem5931Solution.uppercase_long_4_comprehension([\"x\"]))\n\n# Example 4: assigned result approach\nresult = uppercase_long_4_comprehension([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(uppercase_long_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5932,
    "title": "Problem 5932",
    "description": "Write a Python function called `uppercase_long_5_comprehension` that must uppercase words with at least 5 characters using a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  uppercase_long_5_comprehension([\"a\", \"python\", \"code\"]) -> [\"PYTHON\"]\n  uppercase_long_5_comprehension([\"x\"]) -> []",
    "initialCode": "def uppercase_long_5_comprehension(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef uppercase_long_5_comprehension(words):\n    return [word.upper() for word in words if len(word) >= 5]\n\nprint(uppercase_long_5_comprehension([\"a\", \"python\", \"code\"]))  # Expected: [\"PYTHON\"]\nprint(uppercase_long_5_comprehension([\"x\"]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5932(words):\n    def calculate():\n        return [word.upper() for word in words if len(word) >= 5]\n    return calculate()\n\nprint(solve_problem_5932([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5932Solution:\n    @staticmethod\n    def uppercase_long_5_comprehension(words):\n        return [word.upper() for word in words if len(word) >= 5]\n\nprint(Problem5932Solution.uppercase_long_5_comprehension([\"x\"]))\n\n# Example 4: assigned result approach\nresult = uppercase_long_5_comprehension([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(uppercase_long_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5933,
    "title": "Problem 5933",
    "description": "Write a Python function called `index_offset_1_comprehension` that must build a dictionary whose text keys are indexes starting at 1. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  index_offset_1_comprehension([\"a\", \"b\"]) -> {\"1\": \"a\", \"2\": \"b\"}\n  index_offset_1_comprehension([9]) -> {\"1\": 9}",
    "initialCode": "def index_offset_1_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef index_offset_1_comprehension(values):\n    return {str(index + 1): value for index, value in enumerate(values)}\n\nprint(index_offset_1_comprehension([\"a\", \"b\"]))  # Expected: {\"1\": \"a\", \"2\": \"b\"}\nprint(index_offset_1_comprehension([9]))  # Expected: {\"1\": 9}\n\n# Example 2: nested helper approach\ndef solve_problem_5933(values):\n    def calculate():\n        return {str(index + 1): value for index, value in enumerate(values)}\n    return calculate()\n\nprint(solve_problem_5933([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5933Solution:\n    @staticmethod\n    def index_offset_1_comprehension(values):\n        return {str(index + 1): value for index, value in enumerate(values)}\n\nprint(Problem5933Solution.index_offset_1_comprehension([9]))\n\n# Example 4: assigned result approach\nresult = index_offset_1_comprehension([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(index_offset_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5934,
    "title": "Problem 5934",
    "description": "Write a Python function called `index_offset_2_comprehension` that must build a dictionary whose text keys are indexes starting at 2. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  index_offset_2_comprehension([\"a\", \"b\"]) -> {\"2\": \"a\", \"3\": \"b\"}\n  index_offset_2_comprehension([9]) -> {\"2\": 9}",
    "initialCode": "def index_offset_2_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef index_offset_2_comprehension(values):\n    return {str(index + 2): value for index, value in enumerate(values)}\n\nprint(index_offset_2_comprehension([\"a\", \"b\"]))  # Expected: {\"2\": \"a\", \"3\": \"b\"}\nprint(index_offset_2_comprehension([9]))  # Expected: {\"2\": 9}\n\n# Example 2: nested helper approach\ndef solve_problem_5934(values):\n    def calculate():\n        return {str(index + 2): value for index, value in enumerate(values)}\n    return calculate()\n\nprint(solve_problem_5934([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5934Solution:\n    @staticmethod\n    def index_offset_2_comprehension(values):\n        return {str(index + 2): value for index, value in enumerate(values)}\n\nprint(Problem5934Solution.index_offset_2_comprehension([9]))\n\n# Example 4: assigned result approach\nresult = index_offset_2_comprehension([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(index_offset_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5935,
    "title": "Problem 5935",
    "description": "Write a Python function called `index_offset_3_comprehension` that must build a dictionary whose text keys are indexes starting at 3. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  index_offset_3_comprehension([\"a\", \"b\"]) -> {\"3\": \"a\", \"4\": \"b\"}\n  index_offset_3_comprehension([9]) -> {\"3\": 9}",
    "initialCode": "def index_offset_3_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef index_offset_3_comprehension(values):\n    return {str(index + 3): value for index, value in enumerate(values)}\n\nprint(index_offset_3_comprehension([\"a\", \"b\"]))  # Expected: {\"3\": \"a\", \"4\": \"b\"}\nprint(index_offset_3_comprehension([9]))  # Expected: {\"3\": 9}\n\n# Example 2: nested helper approach\ndef solve_problem_5935(values):\n    def calculate():\n        return {str(index + 3): value for index, value in enumerate(values)}\n    return calculate()\n\nprint(solve_problem_5935([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5935Solution:\n    @staticmethod\n    def index_offset_3_comprehension(values):\n        return {str(index + 3): value for index, value in enumerate(values)}\n\nprint(Problem5935Solution.index_offset_3_comprehension([9]))\n\n# Example 4: assigned result approach\nresult = index_offset_3_comprehension([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(index_offset_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5936,
    "title": "Problem 5936",
    "description": "Write a Python function called `index_offset_4_comprehension` that must build a dictionary whose text keys are indexes starting at 4. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  index_offset_4_comprehension([\"a\", \"b\"]) -> {\"4\": \"a\", \"5\": \"b\"}\n  index_offset_4_comprehension([9]) -> {\"4\": 9}",
    "initialCode": "def index_offset_4_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef index_offset_4_comprehension(values):\n    return {str(index + 4): value for index, value in enumerate(values)}\n\nprint(index_offset_4_comprehension([\"a\", \"b\"]))  # Expected: {\"4\": \"a\", \"5\": \"b\"}\nprint(index_offset_4_comprehension([9]))  # Expected: {\"4\": 9}\n\n# Example 2: nested helper approach\ndef solve_problem_5936(values):\n    def calculate():\n        return {str(index + 4): value for index, value in enumerate(values)}\n    return calculate()\n\nprint(solve_problem_5936([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5936Solution:\n    @staticmethod\n    def index_offset_4_comprehension(values):\n        return {str(index + 4): value for index, value in enumerate(values)}\n\nprint(Problem5936Solution.index_offset_4_comprehension([9]))\n\n# Example 4: assigned result approach\nresult = index_offset_4_comprehension([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(index_offset_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5937,
    "title": "Problem 5937",
    "description": "Write a Python function called `index_offset_5_comprehension` that must build a dictionary whose text keys are indexes starting at 5. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  index_offset_5_comprehension([\"a\", \"b\"]) -> {\"5\": \"a\", \"6\": \"b\"}\n  index_offset_5_comprehension([9]) -> {\"5\": 9}",
    "initialCode": "def index_offset_5_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef index_offset_5_comprehension(values):\n    return {str(index + 5): value for index, value in enumerate(values)}\n\nprint(index_offset_5_comprehension([\"a\", \"b\"]))  # Expected: {\"5\": \"a\", \"6\": \"b\"}\nprint(index_offset_5_comprehension([9]))  # Expected: {\"5\": 9}\n\n# Example 2: nested helper approach\ndef solve_problem_5937(values):\n    def calculate():\n        return {str(index + 5): value for index, value in enumerate(values)}\n    return calculate()\n\nprint(solve_problem_5937([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5937Solution:\n    @staticmethod\n    def index_offset_5_comprehension(values):\n        return {str(index + 5): value for index, value in enumerate(values)}\n\nprint(Problem5937Solution.index_offset_5_comprehension([9]))\n\n# Example 4: assigned result approach\nresult = index_offset_5_comprehension([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(index_offset_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5938,
    "title": "Problem 5938",
    "description": "Write a Python function called `flatten_plus_1_comprehension` that must flatten a matrix and add 1 to each value with a comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  flatten_plus_1_comprehension([[1, 2], [3]]) -> [2, 3, 4]\n  flatten_plus_1_comprehension([[]]) -> []",
    "initialCode": "def flatten_plus_1_comprehension(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_plus_1_comprehension(matrix):\n    return [value + 1 for row in matrix for value in row]\n\nprint(flatten_plus_1_comprehension([[1, 2], [3]]))  # Expected: [2, 3, 4]\nprint(flatten_plus_1_comprehension([[]]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5938(matrix):\n    def calculate():\n        return [value + 1 for row in matrix for value in row]\n    return calculate()\n\nprint(solve_problem_5938([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5938Solution:\n    @staticmethod\n    def flatten_plus_1_comprehension(matrix):\n        return [value + 1 for row in matrix for value in row]\n\nprint(Problem5938Solution.flatten_plus_1_comprehension([[]]))\n\n# Example 4: assigned result approach\nresult = flatten_plus_1_comprehension([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_plus_1_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5939,
    "title": "Problem 5939",
    "description": "Write a Python function called `flatten_plus_2_comprehension` that must flatten a matrix and add 2 to each value with a comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  flatten_plus_2_comprehension([[1, 2], [3]]) -> [3, 4, 5]\n  flatten_plus_2_comprehension([[]]) -> []",
    "initialCode": "def flatten_plus_2_comprehension(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_plus_2_comprehension(matrix):\n    return [value + 2 for row in matrix for value in row]\n\nprint(flatten_plus_2_comprehension([[1, 2], [3]]))  # Expected: [3, 4, 5]\nprint(flatten_plus_2_comprehension([[]]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5939(matrix):\n    def calculate():\n        return [value + 2 for row in matrix for value in row]\n    return calculate()\n\nprint(solve_problem_5939([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5939Solution:\n    @staticmethod\n    def flatten_plus_2_comprehension(matrix):\n        return [value + 2 for row in matrix for value in row]\n\nprint(Problem5939Solution.flatten_plus_2_comprehension([[]]))\n\n# Example 4: assigned result approach\nresult = flatten_plus_2_comprehension([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_plus_2_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5940,
    "title": "Problem 5940",
    "description": "Write a Python function called `flatten_plus_3_comprehension` that must flatten a matrix and add 3 to each value with a comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  flatten_plus_3_comprehension([[1, 2], [3]]) -> [4, 5, 6]\n  flatten_plus_3_comprehension([[]]) -> []",
    "initialCode": "def flatten_plus_3_comprehension(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_plus_3_comprehension(matrix):\n    return [value + 3 for row in matrix for value in row]\n\nprint(flatten_plus_3_comprehension([[1, 2], [3]]))  # Expected: [4, 5, 6]\nprint(flatten_plus_3_comprehension([[]]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5940(matrix):\n    def calculate():\n        return [value + 3 for row in matrix for value in row]\n    return calculate()\n\nprint(solve_problem_5940([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5940Solution:\n    @staticmethod\n    def flatten_plus_3_comprehension(matrix):\n        return [value + 3 for row in matrix for value in row]\n\nprint(Problem5940Solution.flatten_plus_3_comprehension([[]]))\n\n# Example 4: assigned result approach\nresult = flatten_plus_3_comprehension([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_plus_3_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5941,
    "title": "Problem 5941",
    "description": "Write a Python function called `flatten_plus_4_comprehension` that must flatten a matrix and add 4 to each value with a comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  flatten_plus_4_comprehension([[1, 2], [3]]) -> [5, 6, 7]\n  flatten_plus_4_comprehension([[]]) -> []",
    "initialCode": "def flatten_plus_4_comprehension(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_plus_4_comprehension(matrix):\n    return [value + 4 for row in matrix for value in row]\n\nprint(flatten_plus_4_comprehension([[1, 2], [3]]))  # Expected: [5, 6, 7]\nprint(flatten_plus_4_comprehension([[]]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5941(matrix):\n    def calculate():\n        return [value + 4 for row in matrix for value in row]\n    return calculate()\n\nprint(solve_problem_5941([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5941Solution:\n    @staticmethod\n    def flatten_plus_4_comprehension(matrix):\n        return [value + 4 for row in matrix for value in row]\n\nprint(Problem5941Solution.flatten_plus_4_comprehension([[]]))\n\n# Example 4: assigned result approach\nresult = flatten_plus_4_comprehension([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_plus_4_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5942,
    "title": "Problem 5942",
    "description": "Write a Python function called `flatten_plus_5_comprehension` that must flatten a matrix and add 5 to each value with a comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  flatten_plus_5_comprehension([[1, 2], [3]]) -> [6, 7, 8]\n  flatten_plus_5_comprehension([[]]) -> []",
    "initialCode": "def flatten_plus_5_comprehension(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_plus_5_comprehension(matrix):\n    return [value + 5 for row in matrix for value in row]\n\nprint(flatten_plus_5_comprehension([[1, 2], [3]]))  # Expected: [6, 7, 8]\nprint(flatten_plus_5_comprehension([[]]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5942(matrix):\n    def calculate():\n        return [value + 5 for row in matrix for value in row]\n    return calculate()\n\nprint(solve_problem_5942([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5942Solution:\n    @staticmethod\n    def flatten_plus_5_comprehension(matrix):\n        return [value + 5 for row in matrix for value in row]\n\nprint(Problem5942Solution.flatten_plus_5_comprehension([[]]))\n\n# Example 4: assigned result approach\nresult = flatten_plus_5_comprehension([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_plus_5_comprehension([]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5943,
    "title": "Problem 5943",
    "description": "Write a Python function called `character_code_1_comprehension` that must return each character code plus 1 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  character_code_1_comprehension(\"abc\") -> [98, 99, 100]\n  character_code_1_comprehension(\"A\") -> [66]",
    "initialCode": "def character_code_1_comprehension(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef character_code_1_comprehension(text):\n    return [ord(char) + 1 for char in text]\n\nprint(character_code_1_comprehension(\"abc\"))  # Expected: [98, 99, 100]\nprint(character_code_1_comprehension(\"A\"))  # Expected: [66]\n\n# Example 2: nested helper approach\ndef solve_problem_5943(text):\n    def calculate():\n        return [ord(char) + 1 for char in text]\n    return calculate()\n\nprint(solve_problem_5943(\"abc\"))\n\n# Example 3: static method approach\nclass Problem5943Solution:\n    @staticmethod\n    def character_code_1_comprehension(text):\n        return [ord(char) + 1 for char in text]\n\nprint(Problem5943Solution.character_code_1_comprehension(\"A\"))\n\n# Example 4: assigned result approach\nresult = character_code_1_comprehension(\"abc\")\nprint(result)\n\n# Example 5: direct call\nprint(character_code_1_comprehension(\"\"))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5944,
    "title": "Problem 5944",
    "description": "Write a Python function called `character_code_2_comprehension` that must return each character code plus 2 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  character_code_2_comprehension(\"abc\") -> [99, 100, 101]\n  character_code_2_comprehension(\"A\") -> [67]",
    "initialCode": "def character_code_2_comprehension(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef character_code_2_comprehension(text):\n    return [ord(char) + 2 for char in text]\n\nprint(character_code_2_comprehension(\"abc\"))  # Expected: [99, 100, 101]\nprint(character_code_2_comprehension(\"A\"))  # Expected: [67]\n\n# Example 2: nested helper approach\ndef solve_problem_5944(text):\n    def calculate():\n        return [ord(char) + 2 for char in text]\n    return calculate()\n\nprint(solve_problem_5944(\"abc\"))\n\n# Example 3: static method approach\nclass Problem5944Solution:\n    @staticmethod\n    def character_code_2_comprehension(text):\n        return [ord(char) + 2 for char in text]\n\nprint(Problem5944Solution.character_code_2_comprehension(\"A\"))\n\n# Example 4: assigned result approach\nresult = character_code_2_comprehension(\"abc\")\nprint(result)\n\n# Example 5: direct call\nprint(character_code_2_comprehension(\"\"))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5945,
    "title": "Problem 5945",
    "description": "Write a Python function called `character_code_3_comprehension` that must return each character code plus 3 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  character_code_3_comprehension(\"abc\") -> [100, 101, 102]\n  character_code_3_comprehension(\"A\") -> [68]",
    "initialCode": "def character_code_3_comprehension(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef character_code_3_comprehension(text):\n    return [ord(char) + 3 for char in text]\n\nprint(character_code_3_comprehension(\"abc\"))  # Expected: [100, 101, 102]\nprint(character_code_3_comprehension(\"A\"))  # Expected: [68]\n\n# Example 2: nested helper approach\ndef solve_problem_5945(text):\n    def calculate():\n        return [ord(char) + 3 for char in text]\n    return calculate()\n\nprint(solve_problem_5945(\"abc\"))\n\n# Example 3: static method approach\nclass Problem5945Solution:\n    @staticmethod\n    def character_code_3_comprehension(text):\n        return [ord(char) + 3 for char in text]\n\nprint(Problem5945Solution.character_code_3_comprehension(\"A\"))\n\n# Example 4: assigned result approach\nresult = character_code_3_comprehension(\"abc\")\nprint(result)\n\n# Example 5: direct call\nprint(character_code_3_comprehension(\"\"))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5946,
    "title": "Problem 5946",
    "description": "Write a Python function called `character_code_4_comprehension` that must return each character code plus 4 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  character_code_4_comprehension(\"abc\") -> [101, 102, 103]\n  character_code_4_comprehension(\"A\") -> [69]",
    "initialCode": "def character_code_4_comprehension(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef character_code_4_comprehension(text):\n    return [ord(char) + 4 for char in text]\n\nprint(character_code_4_comprehension(\"abc\"))  # Expected: [101, 102, 103]\nprint(character_code_4_comprehension(\"A\"))  # Expected: [69]\n\n# Example 2: nested helper approach\ndef solve_problem_5946(text):\n    def calculate():\n        return [ord(char) + 4 for char in text]\n    return calculate()\n\nprint(solve_problem_5946(\"abc\"))\n\n# Example 3: static method approach\nclass Problem5946Solution:\n    @staticmethod\n    def character_code_4_comprehension(text):\n        return [ord(char) + 4 for char in text]\n\nprint(Problem5946Solution.character_code_4_comprehension(\"A\"))\n\n# Example 4: assigned result approach\nresult = character_code_4_comprehension(\"abc\")\nprint(result)\n\n# Example 5: direct call\nprint(character_code_4_comprehension(\"\"))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5947,
    "title": "Problem 5947",
    "description": "Write a Python function called `character_code_5_comprehension` that must return each character code plus 5 with a list comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  character_code_5_comprehension(\"abc\") -> [102, 103, 104]\n  character_code_5_comprehension(\"A\") -> [70]",
    "initialCode": "def character_code_5_comprehension(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef character_code_5_comprehension(text):\n    return [ord(char) + 5 for char in text]\n\nprint(character_code_5_comprehension(\"abc\"))  # Expected: [102, 103, 104]\nprint(character_code_5_comprehension(\"A\"))  # Expected: [70]\n\n# Example 2: nested helper approach\ndef solve_problem_5947(text):\n    def calculate():\n        return [ord(char) + 5 for char in text]\n    return calculate()\n\nprint(solve_problem_5947(\"abc\"))\n\n# Example 3: static method approach\nclass Problem5947Solution:\n    @staticmethod\n    def character_code_5_comprehension(text):\n        return [ord(char) + 5 for char in text]\n\nprint(Problem5947Solution.character_code_5_comprehension(\"A\"))\n\n# Example 4: assigned result approach\nresult = character_code_5_comprehension(\"abc\")\nprint(result)\n\n# Example 5: direct call\nprint(character_code_5_comprehension(\"\"))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5948,
    "title": "Problem 5948",
    "description": "Write a Python function called `pair_sum_above_1_comprehension` that must return two-item lists whose sum exceeds 1 using a nested comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  pair_sum_above_1_comprehension([1, 3], [2, 4]) -> [[1, 2], [1, 4], [3, 2], [3, 4]]\n  pair_sum_above_1_comprehension([0], [0]) -> []",
    "initialCode": "def pair_sum_above_1_comprehension(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef pair_sum_above_1_comprehension(left, right):\n    return [[a, b] for a in left for b in right if a + b > 1]\n\nprint(pair_sum_above_1_comprehension([1, 3], [2, 4]))  # Expected: [[1, 2], [1, 4], [3, 2], [3, 4]]\nprint(pair_sum_above_1_comprehension([0], [0]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5948(left, right):\n    def calculate():\n        return [[a, b] for a in left for b in right if a + b > 1]\n    return calculate()\n\nprint(solve_problem_5948([1, 3], [2, 4]))\n\n# Example 3: static method approach\nclass Problem5948Solution:\n    @staticmethod\n    def pair_sum_above_1_comprehension(left, right):\n        return [[a, b] for a in left for b in right if a + b > 1]\n\nprint(Problem5948Solution.pair_sum_above_1_comprehension([0], [0]))\n\n# Example 4: assigned result approach\nresult = pair_sum_above_1_comprehension([1, 3], [2, 4])\nprint(result)\n\n# Example 5: direct call\nprint(pair_sum_above_1_comprehension([], [1]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5949,
    "title": "Problem 5949",
    "description": "Write a Python function called `pair_sum_above_2_comprehension` that must return two-item lists whose sum exceeds 2 using a nested comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  pair_sum_above_2_comprehension([1, 3], [2, 4]) -> [[1, 2], [1, 4], [3, 2], [3, 4]]\n  pair_sum_above_2_comprehension([0], [0]) -> []",
    "initialCode": "def pair_sum_above_2_comprehension(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef pair_sum_above_2_comprehension(left, right):\n    return [[a, b] for a in left for b in right if a + b > 2]\n\nprint(pair_sum_above_2_comprehension([1, 3], [2, 4]))  # Expected: [[1, 2], [1, 4], [3, 2], [3, 4]]\nprint(pair_sum_above_2_comprehension([0], [0]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5949(left, right):\n    def calculate():\n        return [[a, b] for a in left for b in right if a + b > 2]\n    return calculate()\n\nprint(solve_problem_5949([1, 3], [2, 4]))\n\n# Example 3: static method approach\nclass Problem5949Solution:\n    @staticmethod\n    def pair_sum_above_2_comprehension(left, right):\n        return [[a, b] for a in left for b in right if a + b > 2]\n\nprint(Problem5949Solution.pair_sum_above_2_comprehension([0], [0]))\n\n# Example 4: assigned result approach\nresult = pair_sum_above_2_comprehension([1, 3], [2, 4])\nprint(result)\n\n# Example 5: direct call\nprint(pair_sum_above_2_comprehension([], [1]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5950,
    "title": "Problem 5950",
    "description": "Write a Python function called `pair_sum_above_3_comprehension` that must return two-item lists whose sum exceeds 3 using a nested comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  pair_sum_above_3_comprehension([1, 3], [2, 4]) -> [[1, 4], [3, 2], [3, 4]]\n  pair_sum_above_3_comprehension([0], [0]) -> []",
    "initialCode": "def pair_sum_above_3_comprehension(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef pair_sum_above_3_comprehension(left, right):\n    return [[a, b] for a in left for b in right if a + b > 3]\n\nprint(pair_sum_above_3_comprehension([1, 3], [2, 4]))  # Expected: [[1, 4], [3, 2], [3, 4]]\nprint(pair_sum_above_3_comprehension([0], [0]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5950(left, right):\n    def calculate():\n        return [[a, b] for a in left for b in right if a + b > 3]\n    return calculate()\n\nprint(solve_problem_5950([1, 3], [2, 4]))\n\n# Example 3: static method approach\nclass Problem5950Solution:\n    @staticmethod\n    def pair_sum_above_3_comprehension(left, right):\n        return [[a, b] for a in left for b in right if a + b > 3]\n\nprint(Problem5950Solution.pair_sum_above_3_comprehension([0], [0]))\n\n# Example 4: assigned result approach\nresult = pair_sum_above_3_comprehension([1, 3], [2, 4])\nprint(result)\n\n# Example 5: direct call\nprint(pair_sum_above_3_comprehension([], [1]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5951,
    "title": "Problem 5951",
    "description": "Write a Python function called `pair_sum_above_4_comprehension` that must return two-item lists whose sum exceeds 4 using a nested comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  pair_sum_above_4_comprehension([1, 3], [2, 4]) -> [[1, 4], [3, 2], [3, 4]]\n  pair_sum_above_4_comprehension([0], [0]) -> []",
    "initialCode": "def pair_sum_above_4_comprehension(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef pair_sum_above_4_comprehension(left, right):\n    return [[a, b] for a in left for b in right if a + b > 4]\n\nprint(pair_sum_above_4_comprehension([1, 3], [2, 4]))  # Expected: [[1, 4], [3, 2], [3, 4]]\nprint(pair_sum_above_4_comprehension([0], [0]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5951(left, right):\n    def calculate():\n        return [[a, b] for a in left for b in right if a + b > 4]\n    return calculate()\n\nprint(solve_problem_5951([1, 3], [2, 4]))\n\n# Example 3: static method approach\nclass Problem5951Solution:\n    @staticmethod\n    def pair_sum_above_4_comprehension(left, right):\n        return [[a, b] for a in left for b in right if a + b > 4]\n\nprint(Problem5951Solution.pair_sum_above_4_comprehension([0], [0]))\n\n# Example 4: assigned result approach\nresult = pair_sum_above_4_comprehension([1, 3], [2, 4])\nprint(result)\n\n# Example 5: direct call\nprint(pair_sum_above_4_comprehension([], [1]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5952,
    "title": "Problem 5952",
    "description": "Write a Python function called `pair_sum_above_5_comprehension` that must return two-item lists whose sum exceeds 5 using a nested comprehension. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  pair_sum_above_5_comprehension([1, 3], [2, 4]) -> [[3, 4]]\n  pair_sum_above_5_comprehension([0], [0]) -> []",
    "initialCode": "def pair_sum_above_5_comprehension(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef pair_sum_above_5_comprehension(left, right):\n    return [[a, b] for a in left for b in right if a + b > 5]\n\nprint(pair_sum_above_5_comprehension([1, 3], [2, 4]))  # Expected: [[3, 4]]\nprint(pair_sum_above_5_comprehension([0], [0]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5952(left, right):\n    def calculate():\n        return [[a, b] for a in left for b in right if a + b > 5]\n    return calculate()\n\nprint(solve_problem_5952([1, 3], [2, 4]))\n\n# Example 3: static method approach\nclass Problem5952Solution:\n    @staticmethod\n    def pair_sum_above_5_comprehension(left, right):\n        return [[a, b] for a in left for b in right if a + b > 5]\n\nprint(Problem5952Solution.pair_sum_above_5_comprehension([0], [0]))\n\n# Example 4: assigned result approach\nresult = pair_sum_above_5_comprehension([1, 3], [2, 4])\nprint(result)\n\n# Example 5: direct call\nprint(pair_sum_above_5_comprehension([], [1]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5953,
    "title": "Problem 5953",
    "description": "Write a Python function called `comparison_flags_1_comprehension` that must return Boolean flags showing which values exceed 1. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  comparison_flags_1_comprehension([0, 1, 2]) -> [False, False, True]\n  comparison_flags_1_comprehension([]) -> []",
    "initialCode": "def comparison_flags_1_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef comparison_flags_1_comprehension(values):\n    return [value > 1 for value in values]\n\nprint(comparison_flags_1_comprehension([0, 1, 2]))  # Expected: [False, False, True]\nprint(comparison_flags_1_comprehension([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5953(values):\n    def calculate():\n        return [value > 1 for value in values]\n    return calculate()\n\nprint(solve_problem_5953([0, 1, 2]))\n\n# Example 3: static method approach\nclass Problem5953Solution:\n    @staticmethod\n    def comparison_flags_1_comprehension(values):\n        return [value > 1 for value in values]\n\nprint(Problem5953Solution.comparison_flags_1_comprehension([]))\n\n# Example 4: assigned result approach\nresult = comparison_flags_1_comprehension([0, 1, 2])\nprint(result)\n\n# Example 5: direct call\nprint(comparison_flags_1_comprehension([10]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5954,
    "title": "Problem 5954",
    "description": "Write a Python function called `comparison_flags_2_comprehension` that must return Boolean flags showing which values exceed 2. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  comparison_flags_2_comprehension([0, 2, 3]) -> [False, False, True]\n  comparison_flags_2_comprehension([]) -> []",
    "initialCode": "def comparison_flags_2_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef comparison_flags_2_comprehension(values):\n    return [value > 2 for value in values]\n\nprint(comparison_flags_2_comprehension([0, 2, 3]))  # Expected: [False, False, True]\nprint(comparison_flags_2_comprehension([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5954(values):\n    def calculate():\n        return [value > 2 for value in values]\n    return calculate()\n\nprint(solve_problem_5954([0, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5954Solution:\n    @staticmethod\n    def comparison_flags_2_comprehension(values):\n        return [value > 2 for value in values]\n\nprint(Problem5954Solution.comparison_flags_2_comprehension([]))\n\n# Example 4: assigned result approach\nresult = comparison_flags_2_comprehension([0, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(comparison_flags_2_comprehension([10]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5955,
    "title": "Problem 5955",
    "description": "Write a Python function called `comparison_flags_3_comprehension` that must return Boolean flags showing which values exceed 3. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  comparison_flags_3_comprehension([0, 3, 4]) -> [False, False, True]\n  comparison_flags_3_comprehension([]) -> []",
    "initialCode": "def comparison_flags_3_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef comparison_flags_3_comprehension(values):\n    return [value > 3 for value in values]\n\nprint(comparison_flags_3_comprehension([0, 3, 4]))  # Expected: [False, False, True]\nprint(comparison_flags_3_comprehension([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5955(values):\n    def calculate():\n        return [value > 3 for value in values]\n    return calculate()\n\nprint(solve_problem_5955([0, 3, 4]))\n\n# Example 3: static method approach\nclass Problem5955Solution:\n    @staticmethod\n    def comparison_flags_3_comprehension(values):\n        return [value > 3 for value in values]\n\nprint(Problem5955Solution.comparison_flags_3_comprehension([]))\n\n# Example 4: assigned result approach\nresult = comparison_flags_3_comprehension([0, 3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(comparison_flags_3_comprehension([10]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5956,
    "title": "Problem 5956",
    "description": "Write a Python function called `comparison_flags_4_comprehension` that must return Boolean flags showing which values exceed 4. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  comparison_flags_4_comprehension([0, 4, 5]) -> [False, False, True]\n  comparison_flags_4_comprehension([]) -> []",
    "initialCode": "def comparison_flags_4_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef comparison_flags_4_comprehension(values):\n    return [value > 4 for value in values]\n\nprint(comparison_flags_4_comprehension([0, 4, 5]))  # Expected: [False, False, True]\nprint(comparison_flags_4_comprehension([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5956(values):\n    def calculate():\n        return [value > 4 for value in values]\n    return calculate()\n\nprint(solve_problem_5956([0, 4, 5]))\n\n# Example 3: static method approach\nclass Problem5956Solution:\n    @staticmethod\n    def comparison_flags_4_comprehension(values):\n        return [value > 4 for value in values]\n\nprint(Problem5956Solution.comparison_flags_4_comprehension([]))\n\n# Example 4: assigned result approach\nresult = comparison_flags_4_comprehension([0, 4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(comparison_flags_4_comprehension([10]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5957,
    "title": "Problem 5957",
    "description": "Write a Python function called `comparison_flags_5_comprehension` that must return Boolean flags showing which values exceed 5. Practice comprehension syntax.\nDifficulty: Easy.\nExamples:\n  comparison_flags_5_comprehension([0, 5, 6]) -> [False, False, True]\n  comparison_flags_5_comprehension([]) -> []",
    "initialCode": "def comparison_flags_5_comprehension(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef comparison_flags_5_comprehension(values):\n    return [value > 5 for value in values]\n\nprint(comparison_flags_5_comprehension([0, 5, 6]))  # Expected: [False, False, True]\nprint(comparison_flags_5_comprehension([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5957(values):\n    def calculate():\n        return [value > 5 for value in values]\n    return calculate()\n\nprint(solve_problem_5957([0, 5, 6]))\n\n# Example 3: static method approach\nclass Problem5957Solution:\n    @staticmethod\n    def comparison_flags_5_comprehension(values):\n        return [value > 5 for value in values]\n\nprint(Problem5957Solution.comparison_flags_5_comprehension([]))\n\n# Example 4: assigned result approach\nresult = comparison_flags_5_comprehension([0, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(comparison_flags_5_comprehension([10]))",
    "hint": "Focus on the expression, iteration clauses, and optional filter order. Use the required comprehension structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the comprehension structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Comprehension Easy"
  },
  {
    "id": 5958,
    "title": "Problem 5958",
    "description": "Write a Python function called `sum_plus_1_for` that must sum all values with a for loop, starting the total at 1. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_1_for([1, 2, 3]) -> 7\n  sum_plus_1_for([]) -> 1",
    "initialCode": "def sum_plus_1_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_1_for(values):\n    total = 1\n    for value in values:\n        total += value\n    return total\n\nprint(sum_plus_1_for([1, 2, 3]))  # Expected: 7\nprint(sum_plus_1_for([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_5958(values):\n    def calculate():\n        total = 1\n        for value in values:\n            total += value\n        return total\n    return calculate()\n\nprint(solve_problem_5958([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5958Solution:\n    @staticmethod\n    def sum_plus_1_for(values):\n        total = 1\n        for value in values:\n            total += value\n        return total\n\nprint(Problem5958Solution.sum_plus_1_for([]))\n\n# Example 4: assigned result approach\nresult = sum_plus_1_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_1_for([-2, 5]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5959,
    "title": "Problem 5959",
    "description": "Write a Python function called `sum_plus_2_for` that must sum all values with a for loop, starting the total at 2. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_2_for([1, 2, 3]) -> 8\n  sum_plus_2_for([]) -> 2",
    "initialCode": "def sum_plus_2_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_2_for(values):\n    total = 2\n    for value in values:\n        total += value\n    return total\n\nprint(sum_plus_2_for([1, 2, 3]))  # Expected: 8\nprint(sum_plus_2_for([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_5959(values):\n    def calculate():\n        total = 2\n        for value in values:\n            total += value\n        return total\n    return calculate()\n\nprint(solve_problem_5959([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5959Solution:\n    @staticmethod\n    def sum_plus_2_for(values):\n        total = 2\n        for value in values:\n            total += value\n        return total\n\nprint(Problem5959Solution.sum_plus_2_for([]))\n\n# Example 4: assigned result approach\nresult = sum_plus_2_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_2_for([-2, 5]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5960,
    "title": "Problem 5960",
    "description": "Write a Python function called `sum_plus_3_for` that must sum all values with a for loop, starting the total at 3. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_3_for([1, 2, 3]) -> 9\n  sum_plus_3_for([]) -> 3",
    "initialCode": "def sum_plus_3_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_3_for(values):\n    total = 3\n    for value in values:\n        total += value\n    return total\n\nprint(sum_plus_3_for([1, 2, 3]))  # Expected: 9\nprint(sum_plus_3_for([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_5960(values):\n    def calculate():\n        total = 3\n        for value in values:\n            total += value\n        return total\n    return calculate()\n\nprint(solve_problem_5960([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5960Solution:\n    @staticmethod\n    def sum_plus_3_for(values):\n        total = 3\n        for value in values:\n            total += value\n        return total\n\nprint(Problem5960Solution.sum_plus_3_for([]))\n\n# Example 4: assigned result approach\nresult = sum_plus_3_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_3_for([-2, 5]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5961,
    "title": "Problem 5961",
    "description": "Write a Python function called `sum_plus_4_for` that must sum all values with a for loop, starting the total at 4. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_4_for([1, 2, 3]) -> 10\n  sum_plus_4_for([]) -> 4",
    "initialCode": "def sum_plus_4_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_4_for(values):\n    total = 4\n    for value in values:\n        total += value\n    return total\n\nprint(sum_plus_4_for([1, 2, 3]))  # Expected: 10\nprint(sum_plus_4_for([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_5961(values):\n    def calculate():\n        total = 4\n        for value in values:\n            total += value\n        return total\n    return calculate()\n\nprint(solve_problem_5961([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5961Solution:\n    @staticmethod\n    def sum_plus_4_for(values):\n        total = 4\n        for value in values:\n            total += value\n        return total\n\nprint(Problem5961Solution.sum_plus_4_for([]))\n\n# Example 4: assigned result approach\nresult = sum_plus_4_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_4_for([-2, 5]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5962,
    "title": "Problem 5962",
    "description": "Write a Python function called `sum_plus_5_for` that must sum all values with a for loop, starting the total at 5. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  sum_plus_5_for([1, 2, 3]) -> 11\n  sum_plus_5_for([]) -> 5",
    "initialCode": "def sum_plus_5_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sum_plus_5_for(values):\n    total = 5\n    for value in values:\n        total += value\n    return total\n\nprint(sum_plus_5_for([1, 2, 3]))  # Expected: 11\nprint(sum_plus_5_for([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_5962(values):\n    def calculate():\n        total = 5\n        for value in values:\n            total += value\n        return total\n    return calculate()\n\nprint(solve_problem_5962([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5962Solution:\n    @staticmethod\n    def sum_plus_5_for(values):\n        total = 5\n        for value in values:\n            total += value\n        return total\n\nprint(Problem5962Solution.sum_plus_5_for([]))\n\n# Example 4: assigned result approach\nresult = sum_plus_5_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(sum_plus_5_for([-2, 5]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5963,
    "title": "Problem 5963",
    "description": "Write a Python function called `count_divisible_1_for` that must count values divisible by 2 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_divisible_1_for([1, 2, 3, 4, 6]) -> 3\n  count_divisible_1_for([]) -> 0",
    "initialCode": "def count_divisible_1_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_divisible_1_for(values):\n    count = 0\n    for value in values:\n        if value % 2 == 0:\n            count += 1\n    return count\n\nprint(count_divisible_1_for([1, 2, 3, 4, 6]))  # Expected: 3\nprint(count_divisible_1_for([]))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5963(values):\n    def calculate():\n        count = 0\n        for value in values:\n            if value % 2 == 0:\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5963([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5963Solution:\n    @staticmethod\n    def count_divisible_1_for(values):\n        count = 0\n        for value in values:\n            if value % 2 == 0:\n                count += 1\n        return count\n\nprint(Problem5963Solution.count_divisible_1_for([]))\n\n# Example 4: assigned result approach\nresult = count_divisible_1_for([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(count_divisible_1_for([2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5964,
    "title": "Problem 5964",
    "description": "Write a Python function called `count_divisible_2_for` that must count values divisible by 3 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_divisible_2_for([1, 2, 3, 4, 6]) -> 2\n  count_divisible_2_for([]) -> 0",
    "initialCode": "def count_divisible_2_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_divisible_2_for(values):\n    count = 0\n    for value in values:\n        if value % 3 == 0:\n            count += 1\n    return count\n\nprint(count_divisible_2_for([1, 2, 3, 4, 6]))  # Expected: 2\nprint(count_divisible_2_for([]))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5964(values):\n    def calculate():\n        count = 0\n        for value in values:\n            if value % 3 == 0:\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5964([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5964Solution:\n    @staticmethod\n    def count_divisible_2_for(values):\n        count = 0\n        for value in values:\n            if value % 3 == 0:\n                count += 1\n        return count\n\nprint(Problem5964Solution.count_divisible_2_for([]))\n\n# Example 4: assigned result approach\nresult = count_divisible_2_for([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(count_divisible_2_for([3]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5965,
    "title": "Problem 5965",
    "description": "Write a Python function called `count_divisible_3_for` that must count values divisible by 4 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_divisible_3_for([1, 2, 3, 4, 6]) -> 1\n  count_divisible_3_for([]) -> 0",
    "initialCode": "def count_divisible_3_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_divisible_3_for(values):\n    count = 0\n    for value in values:\n        if value % 4 == 0:\n            count += 1\n    return count\n\nprint(count_divisible_3_for([1, 2, 3, 4, 6]))  # Expected: 1\nprint(count_divisible_3_for([]))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5965(values):\n    def calculate():\n        count = 0\n        for value in values:\n            if value % 4 == 0:\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5965([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5965Solution:\n    @staticmethod\n    def count_divisible_3_for(values):\n        count = 0\n        for value in values:\n            if value % 4 == 0:\n                count += 1\n        return count\n\nprint(Problem5965Solution.count_divisible_3_for([]))\n\n# Example 4: assigned result approach\nresult = count_divisible_3_for([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(count_divisible_3_for([4]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5966,
    "title": "Problem 5966",
    "description": "Write a Python function called `count_divisible_4_for` that must count values divisible by 5 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_divisible_4_for([1, 2, 3, 4, 6]) -> 0\n  count_divisible_4_for([]) -> 0",
    "initialCode": "def count_divisible_4_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_divisible_4_for(values):\n    count = 0\n    for value in values:\n        if value % 5 == 0:\n            count += 1\n    return count\n\nprint(count_divisible_4_for([1, 2, 3, 4, 6]))  # Expected: 0\nprint(count_divisible_4_for([]))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5966(values):\n    def calculate():\n        count = 0\n        for value in values:\n            if value % 5 == 0:\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5966([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5966Solution:\n    @staticmethod\n    def count_divisible_4_for(values):\n        count = 0\n        for value in values:\n            if value % 5 == 0:\n                count += 1\n        return count\n\nprint(Problem5966Solution.count_divisible_4_for([]))\n\n# Example 4: assigned result approach\nresult = count_divisible_4_for([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(count_divisible_4_for([5]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5967,
    "title": "Problem 5967",
    "description": "Write a Python function called `count_divisible_5_for` that must count values divisible by 6 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_divisible_5_for([1, 2, 3, 4, 6]) -> 1\n  count_divisible_5_for([]) -> 0",
    "initialCode": "def count_divisible_5_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_divisible_5_for(values):\n    count = 0\n    for value in values:\n        if value % 6 == 0:\n            count += 1\n    return count\n\nprint(count_divisible_5_for([1, 2, 3, 4, 6]))  # Expected: 1\nprint(count_divisible_5_for([]))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_5967(values):\n    def calculate():\n        count = 0\n        for value in values:\n            if value % 6 == 0:\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_5967([1, 2, 3, 4, 6]))\n\n# Example 3: static method approach\nclass Problem5967Solution:\n    @staticmethod\n    def count_divisible_5_for(values):\n        count = 0\n        for value in values:\n            if value % 6 == 0:\n                count += 1\n        return count\n\nprint(Problem5967Solution.count_divisible_5_for([]))\n\n# Example 4: assigned result approach\nresult = count_divisible_5_for([1, 2, 3, 4, 6])\nprint(result)\n\n# Example 5: direct call\nprint(count_divisible_5_for([6]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5968,
    "title": "Problem 5968",
    "description": "Write a Python function called `square_offset_1_for` that must build a list of squares plus 1 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  square_offset_1_for([1, 2, 3]) -> [2, 5, 10]\n  square_offset_1_for([]) -> []",
    "initialCode": "def square_offset_1_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_offset_1_for(values):\n    result = []\n    for value in values:\n        result.append(value ** 2 + 1)\n    return result\n\nprint(square_offset_1_for([1, 2, 3]))  # Expected: [2, 5, 10]\nprint(square_offset_1_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5968(values):\n    def calculate():\n        result = []\n        for value in values:\n            result.append(value ** 2 + 1)\n        return result\n    return calculate()\n\nprint(solve_problem_5968([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5968Solution:\n    @staticmethod\n    def square_offset_1_for(values):\n        result = []\n        for value in values:\n            result.append(value ** 2 + 1)\n        return result\n\nprint(Problem5968Solution.square_offset_1_for([]))\n\n# Example 4: assigned result approach\nresult = square_offset_1_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_offset_1_for([-2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5969,
    "title": "Problem 5969",
    "description": "Write a Python function called `square_offset_2_for` that must build a list of squares plus 2 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  square_offset_2_for([1, 2, 3]) -> [3, 6, 11]\n  square_offset_2_for([]) -> []",
    "initialCode": "def square_offset_2_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_offset_2_for(values):\n    result = []\n    for value in values:\n        result.append(value ** 2 + 2)\n    return result\n\nprint(square_offset_2_for([1, 2, 3]))  # Expected: [3, 6, 11]\nprint(square_offset_2_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5969(values):\n    def calculate():\n        result = []\n        for value in values:\n            result.append(value ** 2 + 2)\n        return result\n    return calculate()\n\nprint(solve_problem_5969([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5969Solution:\n    @staticmethod\n    def square_offset_2_for(values):\n        result = []\n        for value in values:\n            result.append(value ** 2 + 2)\n        return result\n\nprint(Problem5969Solution.square_offset_2_for([]))\n\n# Example 4: assigned result approach\nresult = square_offset_2_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_offset_2_for([-2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5970,
    "title": "Problem 5970",
    "description": "Write a Python function called `square_offset_3_for` that must build a list of squares plus 3 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  square_offset_3_for([1, 2, 3]) -> [4, 7, 12]\n  square_offset_3_for([]) -> []",
    "initialCode": "def square_offset_3_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_offset_3_for(values):\n    result = []\n    for value in values:\n        result.append(value ** 2 + 3)\n    return result\n\nprint(square_offset_3_for([1, 2, 3]))  # Expected: [4, 7, 12]\nprint(square_offset_3_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5970(values):\n    def calculate():\n        result = []\n        for value in values:\n            result.append(value ** 2 + 3)\n        return result\n    return calculate()\n\nprint(solve_problem_5970([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5970Solution:\n    @staticmethod\n    def square_offset_3_for(values):\n        result = []\n        for value in values:\n            result.append(value ** 2 + 3)\n        return result\n\nprint(Problem5970Solution.square_offset_3_for([]))\n\n# Example 4: assigned result approach\nresult = square_offset_3_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_offset_3_for([-2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5971,
    "title": "Problem 5971",
    "description": "Write a Python function called `square_offset_4_for` that must build a list of squares plus 4 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  square_offset_4_for([1, 2, 3]) -> [5, 8, 13]\n  square_offset_4_for([]) -> []",
    "initialCode": "def square_offset_4_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_offset_4_for(values):\n    result = []\n    for value in values:\n        result.append(value ** 2 + 4)\n    return result\n\nprint(square_offset_4_for([1, 2, 3]))  # Expected: [5, 8, 13]\nprint(square_offset_4_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5971(values):\n    def calculate():\n        result = []\n        for value in values:\n            result.append(value ** 2 + 4)\n        return result\n    return calculate()\n\nprint(solve_problem_5971([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5971Solution:\n    @staticmethod\n    def square_offset_4_for(values):\n        result = []\n        for value in values:\n            result.append(value ** 2 + 4)\n        return result\n\nprint(Problem5971Solution.square_offset_4_for([]))\n\n# Example 4: assigned result approach\nresult = square_offset_4_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_offset_4_for([-2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5972,
    "title": "Problem 5972",
    "description": "Write a Python function called `square_offset_5_for` that must build a list of squares plus 5 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  square_offset_5_for([1, 2, 3]) -> [6, 9, 14]\n  square_offset_5_for([]) -> []",
    "initialCode": "def square_offset_5_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef square_offset_5_for(values):\n    result = []\n    for value in values:\n        result.append(value ** 2 + 5)\n    return result\n\nprint(square_offset_5_for([1, 2, 3]))  # Expected: [6, 9, 14]\nprint(square_offset_5_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5972(values):\n    def calculate():\n        result = []\n        for value in values:\n            result.append(value ** 2 + 5)\n        return result\n    return calculate()\n\nprint(solve_problem_5972([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5972Solution:\n    @staticmethod\n    def square_offset_5_for(values):\n        result = []\n        for value in values:\n            result.append(value ** 2 + 5)\n        return result\n\nprint(Problem5972Solution.square_offset_5_for([]))\n\n# Example 4: assigned result approach\nresult = square_offset_5_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(square_offset_5_for([-2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5973,
    "title": "Problem 5973",
    "description": "Write a Python function called `long_words_1_for` that must collect words with at least 1 characters using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  long_words_1_for([\"a\", \"python\", \"code\"]) -> [\"a\", \"python\", \"code\"]\n  long_words_1_for([]) -> []",
    "initialCode": "def long_words_1_for(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef long_words_1_for(words):\n    result = []\n    for word in words:\n        if len(word) >= 1:\n            result.append(word)\n    return result\n\nprint(long_words_1_for([\"a\", \"python\", \"code\"]))  # Expected: [\"a\", \"python\", \"code\"]\nprint(long_words_1_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5973(words):\n    def calculate():\n        result = []\n        for word in words:\n            if len(word) >= 1:\n                result.append(word)\n        return result\n    return calculate()\n\nprint(solve_problem_5973([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5973Solution:\n    @staticmethod\n    def long_words_1_for(words):\n        result = []\n        for word in words:\n            if len(word) >= 1:\n                result.append(word)\n        return result\n\nprint(Problem5973Solution.long_words_1_for([]))\n\n# Example 4: assigned result approach\nresult = long_words_1_for([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(long_words_1_for([\"x\"]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5974,
    "title": "Problem 5974",
    "description": "Write a Python function called `long_words_2_for` that must collect words with at least 2 characters using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  long_words_2_for([\"a\", \"python\", \"code\"]) -> [\"python\", \"code\"]\n  long_words_2_for([]) -> []",
    "initialCode": "def long_words_2_for(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef long_words_2_for(words):\n    result = []\n    for word in words:\n        if len(word) >= 2:\n            result.append(word)\n    return result\n\nprint(long_words_2_for([\"a\", \"python\", \"code\"]))  # Expected: [\"python\", \"code\"]\nprint(long_words_2_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5974(words):\n    def calculate():\n        result = []\n        for word in words:\n            if len(word) >= 2:\n                result.append(word)\n        return result\n    return calculate()\n\nprint(solve_problem_5974([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5974Solution:\n    @staticmethod\n    def long_words_2_for(words):\n        result = []\n        for word in words:\n            if len(word) >= 2:\n                result.append(word)\n        return result\n\nprint(Problem5974Solution.long_words_2_for([]))\n\n# Example 4: assigned result approach\nresult = long_words_2_for([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(long_words_2_for([\"xx\"]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5975,
    "title": "Problem 5975",
    "description": "Write a Python function called `long_words_3_for` that must collect words with at least 3 characters using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  long_words_3_for([\"a\", \"python\", \"code\"]) -> [\"python\", \"code\"]\n  long_words_3_for([]) -> []",
    "initialCode": "def long_words_3_for(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef long_words_3_for(words):\n    result = []\n    for word in words:\n        if len(word) >= 3:\n            result.append(word)\n    return result\n\nprint(long_words_3_for([\"a\", \"python\", \"code\"]))  # Expected: [\"python\", \"code\"]\nprint(long_words_3_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5975(words):\n    def calculate():\n        result = []\n        for word in words:\n            if len(word) >= 3:\n                result.append(word)\n        return result\n    return calculate()\n\nprint(solve_problem_5975([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5975Solution:\n    @staticmethod\n    def long_words_3_for(words):\n        result = []\n        for word in words:\n            if len(word) >= 3:\n                result.append(word)\n        return result\n\nprint(Problem5975Solution.long_words_3_for([]))\n\n# Example 4: assigned result approach\nresult = long_words_3_for([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(long_words_3_for([\"xxx\"]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5976,
    "title": "Problem 5976",
    "description": "Write a Python function called `long_words_4_for` that must collect words with at least 4 characters using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  long_words_4_for([\"a\", \"python\", \"code\"]) -> [\"python\", \"code\"]\n  long_words_4_for([]) -> []",
    "initialCode": "def long_words_4_for(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef long_words_4_for(words):\n    result = []\n    for word in words:\n        if len(word) >= 4:\n            result.append(word)\n    return result\n\nprint(long_words_4_for([\"a\", \"python\", \"code\"]))  # Expected: [\"python\", \"code\"]\nprint(long_words_4_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5976(words):\n    def calculate():\n        result = []\n        for word in words:\n            if len(word) >= 4:\n                result.append(word)\n        return result\n    return calculate()\n\nprint(solve_problem_5976([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5976Solution:\n    @staticmethod\n    def long_words_4_for(words):\n        result = []\n        for word in words:\n            if len(word) >= 4:\n                result.append(word)\n        return result\n\nprint(Problem5976Solution.long_words_4_for([]))\n\n# Example 4: assigned result approach\nresult = long_words_4_for([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(long_words_4_for([\"xxxx\"]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5977,
    "title": "Problem 5977",
    "description": "Write a Python function called `long_words_5_for` that must collect words with at least 5 characters using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  long_words_5_for([\"a\", \"python\", \"code\"]) -> [\"python\"]\n  long_words_5_for([]) -> []",
    "initialCode": "def long_words_5_for(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef long_words_5_for(words):\n    result = []\n    for word in words:\n        if len(word) >= 5:\n            result.append(word)\n    return result\n\nprint(long_words_5_for([\"a\", \"python\", \"code\"]))  # Expected: [\"python\"]\nprint(long_words_5_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5977(words):\n    def calculate():\n        result = []\n        for word in words:\n            if len(word) >= 5:\n                result.append(word)\n        return result\n    return calculate()\n\nprint(solve_problem_5977([\"a\", \"python\", \"code\"]))\n\n# Example 3: static method approach\nclass Problem5977Solution:\n    @staticmethod\n    def long_words_5_for(words):\n        result = []\n        for word in words:\n            if len(word) >= 5:\n                result.append(word)\n        return result\n\nprint(Problem5977Solution.long_words_5_for([]))\n\n# Example 4: assigned result approach\nresult = long_words_5_for([\"a\", \"python\", \"code\"])\nprint(result)\n\n# Example 5: direct call\nprint(long_words_5_for([\"xxxxx\"]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5978,
    "title": "Problem 5978",
    "description": "Write a Python function called `positive_mapping_1_for` that must map each positive value's text to that value plus 1 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  positive_mapping_1_for([-1, 1, 3]) -> {\"1\": 2, \"3\": 4}\n  positive_mapping_1_for([]) -> {}",
    "initialCode": "def positive_mapping_1_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_mapping_1_for(values):\n    result = {}\n    for value in values:\n        if value > 0:\n            result[str(value)] = value + 1\n    return result\n\nprint(positive_mapping_1_for([-1, 1, 3]))  # Expected: {\"1\": 2, \"3\": 4}\nprint(positive_mapping_1_for([]))  # Expected: {}\n\n# Example 2: nested helper approach\ndef solve_problem_5978(values):\n    def calculate():\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 1\n        return result\n    return calculate()\n\nprint(solve_problem_5978([-1, 1, 3]))\n\n# Example 3: static method approach\nclass Problem5978Solution:\n    @staticmethod\n    def positive_mapping_1_for(values):\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 1\n        return result\n\nprint(Problem5978Solution.positive_mapping_1_for([]))\n\n# Example 4: assigned result approach\nresult = positive_mapping_1_for([-1, 1, 3])\nprint(result)\n\n# Example 5: direct call\nprint(positive_mapping_1_for([2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5979,
    "title": "Problem 5979",
    "description": "Write a Python function called `positive_mapping_2_for` that must map each positive value's text to that value plus 2 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  positive_mapping_2_for([-1, 1, 3]) -> {\"1\": 3, \"3\": 5}\n  positive_mapping_2_for([]) -> {}",
    "initialCode": "def positive_mapping_2_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_mapping_2_for(values):\n    result = {}\n    for value in values:\n        if value > 0:\n            result[str(value)] = value + 2\n    return result\n\nprint(positive_mapping_2_for([-1, 1, 3]))  # Expected: {\"1\": 3, \"3\": 5}\nprint(positive_mapping_2_for([]))  # Expected: {}\n\n# Example 2: nested helper approach\ndef solve_problem_5979(values):\n    def calculate():\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 2\n        return result\n    return calculate()\n\nprint(solve_problem_5979([-1, 1, 3]))\n\n# Example 3: static method approach\nclass Problem5979Solution:\n    @staticmethod\n    def positive_mapping_2_for(values):\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 2\n        return result\n\nprint(Problem5979Solution.positive_mapping_2_for([]))\n\n# Example 4: assigned result approach\nresult = positive_mapping_2_for([-1, 1, 3])\nprint(result)\n\n# Example 5: direct call\nprint(positive_mapping_2_for([2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5980,
    "title": "Problem 5980",
    "description": "Write a Python function called `positive_mapping_3_for` that must map each positive value's text to that value plus 3 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  positive_mapping_3_for([-1, 1, 3]) -> {\"1\": 4, \"3\": 6}\n  positive_mapping_3_for([]) -> {}",
    "initialCode": "def positive_mapping_3_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_mapping_3_for(values):\n    result = {}\n    for value in values:\n        if value > 0:\n            result[str(value)] = value + 3\n    return result\n\nprint(positive_mapping_3_for([-1, 1, 3]))  # Expected: {\"1\": 4, \"3\": 6}\nprint(positive_mapping_3_for([]))  # Expected: {}\n\n# Example 2: nested helper approach\ndef solve_problem_5980(values):\n    def calculate():\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 3\n        return result\n    return calculate()\n\nprint(solve_problem_5980([-1, 1, 3]))\n\n# Example 3: static method approach\nclass Problem5980Solution:\n    @staticmethod\n    def positive_mapping_3_for(values):\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 3\n        return result\n\nprint(Problem5980Solution.positive_mapping_3_for([]))\n\n# Example 4: assigned result approach\nresult = positive_mapping_3_for([-1, 1, 3])\nprint(result)\n\n# Example 5: direct call\nprint(positive_mapping_3_for([2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5981,
    "title": "Problem 5981",
    "description": "Write a Python function called `positive_mapping_4_for` that must map each positive value's text to that value plus 4 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  positive_mapping_4_for([-1, 1, 3]) -> {\"1\": 5, \"3\": 7}\n  positive_mapping_4_for([]) -> {}",
    "initialCode": "def positive_mapping_4_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_mapping_4_for(values):\n    result = {}\n    for value in values:\n        if value > 0:\n            result[str(value)] = value + 4\n    return result\n\nprint(positive_mapping_4_for([-1, 1, 3]))  # Expected: {\"1\": 5, \"3\": 7}\nprint(positive_mapping_4_for([]))  # Expected: {}\n\n# Example 2: nested helper approach\ndef solve_problem_5981(values):\n    def calculate():\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 4\n        return result\n    return calculate()\n\nprint(solve_problem_5981([-1, 1, 3]))\n\n# Example 3: static method approach\nclass Problem5981Solution:\n    @staticmethod\n    def positive_mapping_4_for(values):\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 4\n        return result\n\nprint(Problem5981Solution.positive_mapping_4_for([]))\n\n# Example 4: assigned result approach\nresult = positive_mapping_4_for([-1, 1, 3])\nprint(result)\n\n# Example 5: direct call\nprint(positive_mapping_4_for([2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5982,
    "title": "Problem 5982",
    "description": "Write a Python function called `positive_mapping_5_for` that must map each positive value's text to that value plus 5 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  positive_mapping_5_for([-1, 1, 3]) -> {\"1\": 6, \"3\": 8}\n  positive_mapping_5_for([]) -> {}",
    "initialCode": "def positive_mapping_5_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positive_mapping_5_for(values):\n    result = {}\n    for value in values:\n        if value > 0:\n            result[str(value)] = value + 5\n    return result\n\nprint(positive_mapping_5_for([-1, 1, 3]))  # Expected: {\"1\": 6, \"3\": 8}\nprint(positive_mapping_5_for([]))  # Expected: {}\n\n# Example 2: nested helper approach\ndef solve_problem_5982(values):\n    def calculate():\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 5\n        return result\n    return calculate()\n\nprint(solve_problem_5982([-1, 1, 3]))\n\n# Example 3: static method approach\nclass Problem5982Solution:\n    @staticmethod\n    def positive_mapping_5_for(values):\n        result = {}\n        for value in values:\n            if value > 0:\n                result[str(value)] = value + 5\n        return result\n\nprint(Problem5982Solution.positive_mapping_5_for([]))\n\n# Example 4: assigned result approach\nresult = positive_mapping_5_for([-1, 1, 3])\nprint(result)\n\n# Example 5: direct call\nprint(positive_mapping_5_for([2]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5983,
    "title": "Problem 5983",
    "description": "Write a Python function called `target_index_1_for` that must find the first target index with a for loop, then add 1 to a found index. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  target_index_1_for([4, 7, 7], 7) -> 2\n  target_index_1_for([1, 2], 9) -> -1",
    "initialCode": "def target_index_1_for(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef target_index_1_for(values, target):\n    for index, value in enumerate(values):\n        if value == target:\n            return index + 1\n    return -1\n\nprint(target_index_1_for([4, 7, 7], 7))  # Expected: 2\nprint(target_index_1_for([1, 2], 9))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5983(values, target):\n    def calculate():\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 1\n        return -1\n    return calculate()\n\nprint(solve_problem_5983([4, 7, 7], 7))\n\n# Example 3: static method approach\nclass Problem5983Solution:\n    @staticmethod\n    def target_index_1_for(values, target):\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 1\n        return -1\n\nprint(Problem5983Solution.target_index_1_for([1, 2], 9))\n\n# Example 4: assigned result approach\nresult = target_index_1_for([4, 7, 7], 7)\nprint(result)\n\n# Example 5: direct call\nprint(target_index_1_for([], 1))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5984,
    "title": "Problem 5984",
    "description": "Write a Python function called `target_index_2_for` that must find the first target index with a for loop, then add 2 to a found index. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  target_index_2_for([4, 7, 7], 7) -> 3\n  target_index_2_for([1, 2], 9) -> -1",
    "initialCode": "def target_index_2_for(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef target_index_2_for(values, target):\n    for index, value in enumerate(values):\n        if value == target:\n            return index + 2\n    return -1\n\nprint(target_index_2_for([4, 7, 7], 7))  # Expected: 3\nprint(target_index_2_for([1, 2], 9))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5984(values, target):\n    def calculate():\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 2\n        return -1\n    return calculate()\n\nprint(solve_problem_5984([4, 7, 7], 7))\n\n# Example 3: static method approach\nclass Problem5984Solution:\n    @staticmethod\n    def target_index_2_for(values, target):\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 2\n        return -1\n\nprint(Problem5984Solution.target_index_2_for([1, 2], 9))\n\n# Example 4: assigned result approach\nresult = target_index_2_for([4, 7, 7], 7)\nprint(result)\n\n# Example 5: direct call\nprint(target_index_2_for([], 1))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5985,
    "title": "Problem 5985",
    "description": "Write a Python function called `target_index_3_for` that must find the first target index with a for loop, then add 3 to a found index. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  target_index_3_for([4, 7, 7], 7) -> 4\n  target_index_3_for([1, 2], 9) -> -1",
    "initialCode": "def target_index_3_for(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef target_index_3_for(values, target):\n    for index, value in enumerate(values):\n        if value == target:\n            return index + 3\n    return -1\n\nprint(target_index_3_for([4, 7, 7], 7))  # Expected: 4\nprint(target_index_3_for([1, 2], 9))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5985(values, target):\n    def calculate():\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 3\n        return -1\n    return calculate()\n\nprint(solve_problem_5985([4, 7, 7], 7))\n\n# Example 3: static method approach\nclass Problem5985Solution:\n    @staticmethod\n    def target_index_3_for(values, target):\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 3\n        return -1\n\nprint(Problem5985Solution.target_index_3_for([1, 2], 9))\n\n# Example 4: assigned result approach\nresult = target_index_3_for([4, 7, 7], 7)\nprint(result)\n\n# Example 5: direct call\nprint(target_index_3_for([], 1))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5986,
    "title": "Problem 5986",
    "description": "Write a Python function called `target_index_4_for` that must find the first target index with a for loop, then add 4 to a found index. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  target_index_4_for([4, 7, 7], 7) -> 5\n  target_index_4_for([1, 2], 9) -> -1",
    "initialCode": "def target_index_4_for(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef target_index_4_for(values, target):\n    for index, value in enumerate(values):\n        if value == target:\n            return index + 4\n    return -1\n\nprint(target_index_4_for([4, 7, 7], 7))  # Expected: 5\nprint(target_index_4_for([1, 2], 9))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5986(values, target):\n    def calculate():\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 4\n        return -1\n    return calculate()\n\nprint(solve_problem_5986([4, 7, 7], 7))\n\n# Example 3: static method approach\nclass Problem5986Solution:\n    @staticmethod\n    def target_index_4_for(values, target):\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 4\n        return -1\n\nprint(Problem5986Solution.target_index_4_for([1, 2], 9))\n\n# Example 4: assigned result approach\nresult = target_index_4_for([4, 7, 7], 7)\nprint(result)\n\n# Example 5: direct call\nprint(target_index_4_for([], 1))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5987,
    "title": "Problem 5987",
    "description": "Write a Python function called `target_index_5_for` that must find the first target index with a for loop, then add 5 to a found index. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  target_index_5_for([4, 7, 7], 7) -> 6\n  target_index_5_for([1, 2], 9) -> -1",
    "initialCode": "def target_index_5_for(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef target_index_5_for(values, target):\n    for index, value in enumerate(values):\n        if value == target:\n            return index + 5\n    return -1\n\nprint(target_index_5_for([4, 7, 7], 7))  # Expected: 6\nprint(target_index_5_for([1, 2], 9))  # Expected: -1\n\n# Example 2: nested helper approach\ndef solve_problem_5987(values, target):\n    def calculate():\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 5\n        return -1\n    return calculate()\n\nprint(solve_problem_5987([4, 7, 7], 7))\n\n# Example 3: static method approach\nclass Problem5987Solution:\n    @staticmethod\n    def target_index_5_for(values, target):\n        for index, value in enumerate(values):\n            if value == target:\n                return index + 5\n        return -1\n\nprint(Problem5987Solution.target_index_5_for([1, 2], 9))\n\n# Example 4: assigned result approach\nresult = target_index_5_for([4, 7, 7], 7)\nprint(result)\n\n# Example 5: direct call\nprint(target_index_5_for([], 1))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5988,
    "title": "Problem 5988",
    "description": "Write a Python function called `flatten_rows_1_for` that must flatten rows with a for loop and append marker 1. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  flatten_rows_1_for([[1, 2], [3]]) -> [1, 2, 3, 1]\n  flatten_rows_1_for([]) -> [1]",
    "initialCode": "def flatten_rows_1_for(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_rows_1_for(matrix):\n    result = []\n    for row in matrix:\n        result.extend(row)\n    result.append(1)\n    return result\n\nprint(flatten_rows_1_for([[1, 2], [3]]))  # Expected: [1, 2, 3, 1]\nprint(flatten_rows_1_for([]))  # Expected: [1]\n\n# Example 2: nested helper approach\ndef solve_problem_5988(matrix):\n    def calculate():\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(1)\n        return result\n    return calculate()\n\nprint(solve_problem_5988([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5988Solution:\n    @staticmethod\n    def flatten_rows_1_for(matrix):\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(1)\n        return result\n\nprint(Problem5988Solution.flatten_rows_1_for([]))\n\n# Example 4: assigned result approach\nresult = flatten_rows_1_for([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_rows_1_for([[]]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5989,
    "title": "Problem 5989",
    "description": "Write a Python function called `flatten_rows_2_for` that must flatten rows with a for loop and append marker 2. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  flatten_rows_2_for([[1, 2], [3]]) -> [1, 2, 3, 2]\n  flatten_rows_2_for([]) -> [2]",
    "initialCode": "def flatten_rows_2_for(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_rows_2_for(matrix):\n    result = []\n    for row in matrix:\n        result.extend(row)\n    result.append(2)\n    return result\n\nprint(flatten_rows_2_for([[1, 2], [3]]))  # Expected: [1, 2, 3, 2]\nprint(flatten_rows_2_for([]))  # Expected: [2]\n\n# Example 2: nested helper approach\ndef solve_problem_5989(matrix):\n    def calculate():\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(2)\n        return result\n    return calculate()\n\nprint(solve_problem_5989([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5989Solution:\n    @staticmethod\n    def flatten_rows_2_for(matrix):\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(2)\n        return result\n\nprint(Problem5989Solution.flatten_rows_2_for([]))\n\n# Example 4: assigned result approach\nresult = flatten_rows_2_for([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_rows_2_for([[]]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5990,
    "title": "Problem 5990",
    "description": "Write a Python function called `flatten_rows_3_for` that must flatten rows with a for loop and append marker 3. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  flatten_rows_3_for([[1, 2], [3]]) -> [1, 2, 3, 3]\n  flatten_rows_3_for([]) -> [3]",
    "initialCode": "def flatten_rows_3_for(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_rows_3_for(matrix):\n    result = []\n    for row in matrix:\n        result.extend(row)\n    result.append(3)\n    return result\n\nprint(flatten_rows_3_for([[1, 2], [3]]))  # Expected: [1, 2, 3, 3]\nprint(flatten_rows_3_for([]))  # Expected: [3]\n\n# Example 2: nested helper approach\ndef solve_problem_5990(matrix):\n    def calculate():\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(3)\n        return result\n    return calculate()\n\nprint(solve_problem_5990([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5990Solution:\n    @staticmethod\n    def flatten_rows_3_for(matrix):\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(3)\n        return result\n\nprint(Problem5990Solution.flatten_rows_3_for([]))\n\n# Example 4: assigned result approach\nresult = flatten_rows_3_for([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_rows_3_for([[]]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5991,
    "title": "Problem 5991",
    "description": "Write a Python function called `flatten_rows_4_for` that must flatten rows with a for loop and append marker 4. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  flatten_rows_4_for([[1, 2], [3]]) -> [1, 2, 3, 4]\n  flatten_rows_4_for([]) -> [4]",
    "initialCode": "def flatten_rows_4_for(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_rows_4_for(matrix):\n    result = []\n    for row in matrix:\n        result.extend(row)\n    result.append(4)\n    return result\n\nprint(flatten_rows_4_for([[1, 2], [3]]))  # Expected: [1, 2, 3, 4]\nprint(flatten_rows_4_for([]))  # Expected: [4]\n\n# Example 2: nested helper approach\ndef solve_problem_5991(matrix):\n    def calculate():\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(4)\n        return result\n    return calculate()\n\nprint(solve_problem_5991([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5991Solution:\n    @staticmethod\n    def flatten_rows_4_for(matrix):\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(4)\n        return result\n\nprint(Problem5991Solution.flatten_rows_4_for([]))\n\n# Example 4: assigned result approach\nresult = flatten_rows_4_for([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_rows_4_for([[]]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5992,
    "title": "Problem 5992",
    "description": "Write a Python function called `flatten_rows_5_for` that must flatten rows with a for loop and append marker 5. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  flatten_rows_5_for([[1, 2], [3]]) -> [1, 2, 3, 5]\n  flatten_rows_5_for([]) -> [5]",
    "initialCode": "def flatten_rows_5_for(matrix):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef flatten_rows_5_for(matrix):\n    result = []\n    for row in matrix:\n        result.extend(row)\n    result.append(5)\n    return result\n\nprint(flatten_rows_5_for([[1, 2], [3]]))  # Expected: [1, 2, 3, 5]\nprint(flatten_rows_5_for([]))  # Expected: [5]\n\n# Example 2: nested helper approach\ndef solve_problem_5992(matrix):\n    def calculate():\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(5)\n        return result\n    return calculate()\n\nprint(solve_problem_5992([[1, 2], [3]]))\n\n# Example 3: static method approach\nclass Problem5992Solution:\n    @staticmethod\n    def flatten_rows_5_for(matrix):\n        result = []\n        for row in matrix:\n            result.extend(row)\n        result.append(5)\n        return result\n\nprint(Problem5992Solution.flatten_rows_5_for([]))\n\n# Example 4: assigned result approach\nresult = flatten_rows_5_for([[1, 2], [3]])\nprint(result)\n\n# Example 5: direct call\nprint(flatten_rows_5_for([[]]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5993,
    "title": "Problem 5993",
    "description": "Write a Python function called `running_totals_1_for` that must return running totals beginning at 1 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  running_totals_1_for([1, 2, 3]) -> [2, 4, 7]\n  running_totals_1_for([]) -> []",
    "initialCode": "def running_totals_1_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_totals_1_for(values):\n    total = 1\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result\n\nprint(running_totals_1_for([1, 2, 3]))  # Expected: [2, 4, 7]\nprint(running_totals_1_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5993(values):\n    def calculate():\n        total = 1\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n    return calculate()\n\nprint(solve_problem_5993([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5993Solution:\n    @staticmethod\n    def running_totals_1_for(values):\n        total = 1\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n\nprint(Problem5993Solution.running_totals_1_for([]))\n\n# Example 4: assigned result approach\nresult = running_totals_1_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_totals_1_for([-1, 4]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5994,
    "title": "Problem 5994",
    "description": "Write a Python function called `running_totals_2_for` that must return running totals beginning at 2 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  running_totals_2_for([1, 2, 3]) -> [3, 5, 8]\n  running_totals_2_for([]) -> []",
    "initialCode": "def running_totals_2_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_totals_2_for(values):\n    total = 2\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result\n\nprint(running_totals_2_for([1, 2, 3]))  # Expected: [3, 5, 8]\nprint(running_totals_2_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5994(values):\n    def calculate():\n        total = 2\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n    return calculate()\n\nprint(solve_problem_5994([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5994Solution:\n    @staticmethod\n    def running_totals_2_for(values):\n        total = 2\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n\nprint(Problem5994Solution.running_totals_2_for([]))\n\n# Example 4: assigned result approach\nresult = running_totals_2_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_totals_2_for([-1, 4]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5995,
    "title": "Problem 5995",
    "description": "Write a Python function called `running_totals_3_for` that must return running totals beginning at 3 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  running_totals_3_for([1, 2, 3]) -> [4, 6, 9]\n  running_totals_3_for([]) -> []",
    "initialCode": "def running_totals_3_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_totals_3_for(values):\n    total = 3\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result\n\nprint(running_totals_3_for([1, 2, 3]))  # Expected: [4, 6, 9]\nprint(running_totals_3_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5995(values):\n    def calculate():\n        total = 3\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n    return calculate()\n\nprint(solve_problem_5995([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5995Solution:\n    @staticmethod\n    def running_totals_3_for(values):\n        total = 3\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n\nprint(Problem5995Solution.running_totals_3_for([]))\n\n# Example 4: assigned result approach\nresult = running_totals_3_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_totals_3_for([-1, 4]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5996,
    "title": "Problem 5996",
    "description": "Write a Python function called `running_totals_4_for` that must return running totals beginning at 4 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  running_totals_4_for([1, 2, 3]) -> [5, 7, 10]\n  running_totals_4_for([]) -> []",
    "initialCode": "def running_totals_4_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_totals_4_for(values):\n    total = 4\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result\n\nprint(running_totals_4_for([1, 2, 3]))  # Expected: [5, 7, 10]\nprint(running_totals_4_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5996(values):\n    def calculate():\n        total = 4\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n    return calculate()\n\nprint(solve_problem_5996([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5996Solution:\n    @staticmethod\n    def running_totals_4_for(values):\n        total = 4\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n\nprint(Problem5996Solution.running_totals_4_for([]))\n\n# Example 4: assigned result approach\nresult = running_totals_4_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_totals_4_for([-1, 4]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5997,
    "title": "Problem 5997",
    "description": "Write a Python function called `running_totals_5_for` that must return running totals beginning at 5 using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  running_totals_5_for([1, 2, 3]) -> [6, 8, 11]\n  running_totals_5_for([]) -> []",
    "initialCode": "def running_totals_5_for(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef running_totals_5_for(values):\n    total = 5\n    result = []\n    for value in values:\n        total += value\n        result.append(total)\n    return result\n\nprint(running_totals_5_for([1, 2, 3]))  # Expected: [6, 8, 11]\nprint(running_totals_5_for([]))  # Expected: []\n\n# Example 2: nested helper approach\ndef solve_problem_5997(values):\n    def calculate():\n        total = 5\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n    return calculate()\n\nprint(solve_problem_5997([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem5997Solution:\n    @staticmethod\n    def running_totals_5_for(values):\n        total = 5\n        result = []\n        for value in values:\n            total += value\n            result.append(total)\n        return result\n\nprint(Problem5997Solution.running_totals_5_for([]))\n\n# Example 4: assigned result approach\nresult = running_totals_5_for([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(running_totals_5_for([-1, 4]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5998,
    "title": "Problem 5998",
    "description": "Write a Python function called `join_with_1_for` that must join item text with separator \"-1-\" using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  join_with_1_for([\"a\", \"b\"]) -> \"a-1-b\"\n  join_with_1_for([1]) -> \"1\"",
    "initialCode": "def join_with_1_for(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef join_with_1_for(items):\n    result = \"\"\n    for item in items:\n        if result:\n            result += \"-1-\"\n        result += str(item)\n    return result\n\nprint(join_with_1_for([\"a\", \"b\"]))  # Expected: \"a-1-b\"\nprint(join_with_1_for([1]))  # Expected: \"1\"\n\n# Example 2: nested helper approach\ndef solve_problem_5998(items):\n    def calculate():\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-1-\"\n            result += str(item)\n        return result\n    return calculate()\n\nprint(solve_problem_5998([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5998Solution:\n    @staticmethod\n    def join_with_1_for(items):\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-1-\"\n            result += str(item)\n        return result\n\nprint(Problem5998Solution.join_with_1_for([1]))\n\n# Example 4: assigned result approach\nresult = join_with_1_for([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(join_with_1_for([]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 5999,
    "title": "Problem 5999",
    "description": "Write a Python function called `join_with_2_for` that must join item text with separator \"-2-\" using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  join_with_2_for([\"a\", \"b\"]) -> \"a-2-b\"\n  join_with_2_for([1]) -> \"1\"",
    "initialCode": "def join_with_2_for(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef join_with_2_for(items):\n    result = \"\"\n    for item in items:\n        if result:\n            result += \"-2-\"\n        result += str(item)\n    return result\n\nprint(join_with_2_for([\"a\", \"b\"]))  # Expected: \"a-2-b\"\nprint(join_with_2_for([1]))  # Expected: \"1\"\n\n# Example 2: nested helper approach\ndef solve_problem_5999(items):\n    def calculate():\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-2-\"\n            result += str(item)\n        return result\n    return calculate()\n\nprint(solve_problem_5999([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem5999Solution:\n    @staticmethod\n    def join_with_2_for(items):\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-2-\"\n            result += str(item)\n        return result\n\nprint(Problem5999Solution.join_with_2_for([1]))\n\n# Example 4: assigned result approach\nresult = join_with_2_for([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(join_with_2_for([]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6000,
    "title": "Problem 6000",
    "description": "Write a Python function called `join_with_3_for` that must join item text with separator \"-3-\" using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  join_with_3_for([\"a\", \"b\"]) -> \"a-3-b\"\n  join_with_3_for([1]) -> \"1\"",
    "initialCode": "def join_with_3_for(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef join_with_3_for(items):\n    result = \"\"\n    for item in items:\n        if result:\n            result += \"-3-\"\n        result += str(item)\n    return result\n\nprint(join_with_3_for([\"a\", \"b\"]))  # Expected: \"a-3-b\"\nprint(join_with_3_for([1]))  # Expected: \"1\"\n\n# Example 2: nested helper approach\ndef solve_problem_6000(items):\n    def calculate():\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-3-\"\n            result += str(item)\n        return result\n    return calculate()\n\nprint(solve_problem_6000([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6000Solution:\n    @staticmethod\n    def join_with_3_for(items):\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-3-\"\n            result += str(item)\n        return result\n\nprint(Problem6000Solution.join_with_3_for([1]))\n\n# Example 4: assigned result approach\nresult = join_with_3_for([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(join_with_3_for([]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6001,
    "title": "Problem 6001",
    "description": "Write a Python function called `join_with_4_for` that must join item text with separator \"-4-\" using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  join_with_4_for([\"a\", \"b\"]) -> \"a-4-b\"\n  join_with_4_for([1]) -> \"1\"",
    "initialCode": "def join_with_4_for(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef join_with_4_for(items):\n    result = \"\"\n    for item in items:\n        if result:\n            result += \"-4-\"\n        result += str(item)\n    return result\n\nprint(join_with_4_for([\"a\", \"b\"]))  # Expected: \"a-4-b\"\nprint(join_with_4_for([1]))  # Expected: \"1\"\n\n# Example 2: nested helper approach\ndef solve_problem_6001(items):\n    def calculate():\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-4-\"\n            result += str(item)\n        return result\n    return calculate()\n\nprint(solve_problem_6001([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6001Solution:\n    @staticmethod\n    def join_with_4_for(items):\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-4-\"\n            result += str(item)\n        return result\n\nprint(Problem6001Solution.join_with_4_for([1]))\n\n# Example 4: assigned result approach\nresult = join_with_4_for([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(join_with_4_for([]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6002,
    "title": "Problem 6002",
    "description": "Write a Python function called `join_with_5_for` that must join item text with separator \"-5-\" using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  join_with_5_for([\"a\", \"b\"]) -> \"a-5-b\"\n  join_with_5_for([1]) -> \"1\"",
    "initialCode": "def join_with_5_for(items):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef join_with_5_for(items):\n    result = \"\"\n    for item in items:\n        if result:\n            result += \"-5-\"\n        result += str(item)\n    return result\n\nprint(join_with_5_for([\"a\", \"b\"]))  # Expected: \"a-5-b\"\nprint(join_with_5_for([1]))  # Expected: \"1\"\n\n# Example 2: nested helper approach\ndef solve_problem_6002(items):\n    def calculate():\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-5-\"\n            result += str(item)\n        return result\n    return calculate()\n\nprint(solve_problem_6002([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6002Solution:\n    @staticmethod\n    def join_with_5_for(items):\n        result = \"\"\n        for item in items:\n            if result:\n                result += \"-5-\"\n            result += str(item)\n        return result\n\nprint(Problem6002Solution.join_with_5_for([1]))\n\n# Example 4: assigned result approach\nresult = join_with_5_for([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(join_with_5_for([]))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6003,
    "title": "Problem 6003",
    "description": "Write a Python function called `count_digit_1_for` that must count digit 1 in text using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_digit_1_for(\"1a1\") -> 2\n  count_digit_1_for(\"abc\") -> 0",
    "initialCode": "def count_digit_1_for(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_digit_1_for(text):\n    count = 0\n    for char in text:\n        if char == \"1\":\n            count += 1\n    return count\n\nprint(count_digit_1_for(\"1a1\"))  # Expected: 2\nprint(count_digit_1_for(\"abc\"))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6003(text):\n    def calculate():\n        count = 0\n        for char in text:\n            if char == \"1\":\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6003(\"1a1\"))\n\n# Example 3: static method approach\nclass Problem6003Solution:\n    @staticmethod\n    def count_digit_1_for(text):\n        count = 0\n        for char in text:\n            if char == \"1\":\n                count += 1\n        return count\n\nprint(Problem6003Solution.count_digit_1_for(\"abc\"))\n\n# Example 4: assigned result approach\nresult = count_digit_1_for(\"1a1\")\nprint(result)\n\n# Example 5: direct call\nprint(count_digit_1_for(\"\"))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6004,
    "title": "Problem 6004",
    "description": "Write a Python function called `count_digit_2_for` that must count digit 2 in text using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_digit_2_for(\"2a2\") -> 2\n  count_digit_2_for(\"abc\") -> 0",
    "initialCode": "def count_digit_2_for(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_digit_2_for(text):\n    count = 0\n    for char in text:\n        if char == \"2\":\n            count += 1\n    return count\n\nprint(count_digit_2_for(\"2a2\"))  # Expected: 2\nprint(count_digit_2_for(\"abc\"))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6004(text):\n    def calculate():\n        count = 0\n        for char in text:\n            if char == \"2\":\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6004(\"2a2\"))\n\n# Example 3: static method approach\nclass Problem6004Solution:\n    @staticmethod\n    def count_digit_2_for(text):\n        count = 0\n        for char in text:\n            if char == \"2\":\n                count += 1\n        return count\n\nprint(Problem6004Solution.count_digit_2_for(\"abc\"))\n\n# Example 4: assigned result approach\nresult = count_digit_2_for(\"2a2\")\nprint(result)\n\n# Example 5: direct call\nprint(count_digit_2_for(\"\"))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6005,
    "title": "Problem 6005",
    "description": "Write a Python function called `count_digit_3_for` that must count digit 3 in text using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_digit_3_for(\"3a3\") -> 2\n  count_digit_3_for(\"abc\") -> 0",
    "initialCode": "def count_digit_3_for(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_digit_3_for(text):\n    count = 0\n    for char in text:\n        if char == \"3\":\n            count += 1\n    return count\n\nprint(count_digit_3_for(\"3a3\"))  # Expected: 2\nprint(count_digit_3_for(\"abc\"))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6005(text):\n    def calculate():\n        count = 0\n        for char in text:\n            if char == \"3\":\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6005(\"3a3\"))\n\n# Example 3: static method approach\nclass Problem6005Solution:\n    @staticmethod\n    def count_digit_3_for(text):\n        count = 0\n        for char in text:\n            if char == \"3\":\n                count += 1\n        return count\n\nprint(Problem6005Solution.count_digit_3_for(\"abc\"))\n\n# Example 4: assigned result approach\nresult = count_digit_3_for(\"3a3\")\nprint(result)\n\n# Example 5: direct call\nprint(count_digit_3_for(\"\"))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6006,
    "title": "Problem 6006",
    "description": "Write a Python function called `count_digit_4_for` that must count digit 4 in text using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_digit_4_for(\"4a4\") -> 2\n  count_digit_4_for(\"abc\") -> 0",
    "initialCode": "def count_digit_4_for(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_digit_4_for(text):\n    count = 0\n    for char in text:\n        if char == \"4\":\n            count += 1\n    return count\n\nprint(count_digit_4_for(\"4a4\"))  # Expected: 2\nprint(count_digit_4_for(\"abc\"))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6006(text):\n    def calculate():\n        count = 0\n        for char in text:\n            if char == \"4\":\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6006(\"4a4\"))\n\n# Example 3: static method approach\nclass Problem6006Solution:\n    @staticmethod\n    def count_digit_4_for(text):\n        count = 0\n        for char in text:\n            if char == \"4\":\n                count += 1\n        return count\n\nprint(Problem6006Solution.count_digit_4_for(\"abc\"))\n\n# Example 4: assigned result approach\nresult = count_digit_4_for(\"4a4\")\nprint(result)\n\n# Example 5: direct call\nprint(count_digit_4_for(\"\"))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6007,
    "title": "Problem 6007",
    "description": "Write a Python function called `count_digit_5_for` that must count digit 5 in text using a for loop. Practice for loop syntax.\nDifficulty: Easy.\nExamples:\n  count_digit_5_for(\"5a5\") -> 2\n  count_digit_5_for(\"abc\") -> 0",
    "initialCode": "def count_digit_5_for(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_digit_5_for(text):\n    count = 0\n    for char in text:\n        if char == \"5\":\n            count += 1\n    return count\n\nprint(count_digit_5_for(\"5a5\"))  # Expected: 2\nprint(count_digit_5_for(\"abc\"))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6007(text):\n    def calculate():\n        count = 0\n        for char in text:\n            if char == \"5\":\n                count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6007(\"5a5\"))\n\n# Example 3: static method approach\nclass Problem6007Solution:\n    @staticmethod\n    def count_digit_5_for(text):\n        count = 0\n        for char in text:\n            if char == \"5\":\n                count += 1\n        return count\n\nprint(Problem6007Solution.count_digit_5_for(\"abc\"))\n\n# Example 4: assigned result approach\nresult = count_digit_5_for(\"5a5\")\nprint(result)\n\n# Example 5: direct call\nprint(count_digit_5_for(\"\"))",
    "hint": "Focus on the iterable, per-item operation, and final return position. Use the required for loop structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the for loop structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "For Loop Easy"
  },
  {
    "id": 6008,
    "title": "Problem 6008",
    "description": "Write a Python function called `first_or_1_iterator` that must use an iterator to return the first value, or 1 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_or_1_iterator([9, 2]) -> 9\n  first_or_1_iterator([]) -> 1",
    "initialCode": "def first_or_1_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_or_1_iterator(values):\n    iterator = iter(values)\n    return next(iterator, 1)\n\nprint(first_or_1_iterator([9, 2]))  # Expected: 9\nprint(first_or_1_iterator([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_6008(values):\n    def calculate():\n        iterator = iter(values)\n        return next(iterator, 1)\n    return calculate()\n\nprint(solve_problem_6008([9, 2]))\n\n# Example 3: static method approach\nclass Problem6008Solution:\n    @staticmethod\n    def first_or_1_iterator(values):\n        iterator = iter(values)\n        return next(iterator, 1)\n\nprint(Problem6008Solution.first_or_1_iterator([]))\n\n# Example 4: assigned result approach\nresult = first_or_1_iterator([9, 2])\nprint(result)\n\n# Example 5: direct call\nprint(first_or_1_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6009,
    "title": "Problem 6009",
    "description": "Write a Python function called `first_or_2_iterator` that must use an iterator to return the first value, or 2 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_or_2_iterator([9, 2]) -> 9\n  first_or_2_iterator([]) -> 2",
    "initialCode": "def first_or_2_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_or_2_iterator(values):\n    iterator = iter(values)\n    return next(iterator, 2)\n\nprint(first_or_2_iterator([9, 2]))  # Expected: 9\nprint(first_or_2_iterator([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_6009(values):\n    def calculate():\n        iterator = iter(values)\n        return next(iterator, 2)\n    return calculate()\n\nprint(solve_problem_6009([9, 2]))\n\n# Example 3: static method approach\nclass Problem6009Solution:\n    @staticmethod\n    def first_or_2_iterator(values):\n        iterator = iter(values)\n        return next(iterator, 2)\n\nprint(Problem6009Solution.first_or_2_iterator([]))\n\n# Example 4: assigned result approach\nresult = first_or_2_iterator([9, 2])\nprint(result)\n\n# Example 5: direct call\nprint(first_or_2_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6010,
    "title": "Problem 6010",
    "description": "Write a Python function called `first_or_3_iterator` that must use an iterator to return the first value, or 3 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_or_3_iterator([9, 2]) -> 9\n  first_or_3_iterator([]) -> 3",
    "initialCode": "def first_or_3_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_or_3_iterator(values):\n    iterator = iter(values)\n    return next(iterator, 3)\n\nprint(first_or_3_iterator([9, 2]))  # Expected: 9\nprint(first_or_3_iterator([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_6010(values):\n    def calculate():\n        iterator = iter(values)\n        return next(iterator, 3)\n    return calculate()\n\nprint(solve_problem_6010([9, 2]))\n\n# Example 3: static method approach\nclass Problem6010Solution:\n    @staticmethod\n    def first_or_3_iterator(values):\n        iterator = iter(values)\n        return next(iterator, 3)\n\nprint(Problem6010Solution.first_or_3_iterator([]))\n\n# Example 4: assigned result approach\nresult = first_or_3_iterator([9, 2])\nprint(result)\n\n# Example 5: direct call\nprint(first_or_3_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6011,
    "title": "Problem 6011",
    "description": "Write a Python function called `first_or_4_iterator` that must use an iterator to return the first value, or 4 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_or_4_iterator([9, 2]) -> 9\n  first_or_4_iterator([]) -> 4",
    "initialCode": "def first_or_4_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_or_4_iterator(values):\n    iterator = iter(values)\n    return next(iterator, 4)\n\nprint(first_or_4_iterator([9, 2]))  # Expected: 9\nprint(first_or_4_iterator([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_6011(values):\n    def calculate():\n        iterator = iter(values)\n        return next(iterator, 4)\n    return calculate()\n\nprint(solve_problem_6011([9, 2]))\n\n# Example 3: static method approach\nclass Problem6011Solution:\n    @staticmethod\n    def first_or_4_iterator(values):\n        iterator = iter(values)\n        return next(iterator, 4)\n\nprint(Problem6011Solution.first_or_4_iterator([]))\n\n# Example 4: assigned result approach\nresult = first_or_4_iterator([9, 2])\nprint(result)\n\n# Example 5: direct call\nprint(first_or_4_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6012,
    "title": "Problem 6012",
    "description": "Write a Python function called `first_or_5_iterator` that must use an iterator to return the first value, or 5 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_or_5_iterator([9, 2]) -> 9\n  first_or_5_iterator([]) -> 5",
    "initialCode": "def first_or_5_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_or_5_iterator(values):\n    iterator = iter(values)\n    return next(iterator, 5)\n\nprint(first_or_5_iterator([9, 2]))  # Expected: 9\nprint(first_or_5_iterator([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_6012(values):\n    def calculate():\n        iterator = iter(values)\n        return next(iterator, 5)\n    return calculate()\n\nprint(solve_problem_6012([9, 2]))\n\n# Example 3: static method approach\nclass Problem6012Solution:\n    @staticmethod\n    def first_or_5_iterator(values):\n        iterator = iter(values)\n        return next(iterator, 5)\n\nprint(Problem6012Solution.first_or_5_iterator([]))\n\n# Example 4: assigned result approach\nresult = first_or_5_iterator([9, 2])\nprint(result)\n\n# Example 5: direct call\nprint(first_or_5_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6013,
    "title": "Problem 6013",
    "description": "Write a Python function called `second_or_1_iterator` that must use an iterator to return the second value, or 1 when unavailable. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  second_or_1_iterator([9, 2, 3]) -> 2\n  second_or_1_iterator([1]) -> 1",
    "initialCode": "def second_or_1_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef second_or_1_iterator(values):\n    iterator = iter(values)\n    next(iterator, None)\n    return next(iterator, 1)\n\nprint(second_or_1_iterator([9, 2, 3]))  # Expected: 2\nprint(second_or_1_iterator([1]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_6013(values):\n    def calculate():\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 1)\n    return calculate()\n\nprint(solve_problem_6013([9, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6013Solution:\n    @staticmethod\n    def second_or_1_iterator(values):\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 1)\n\nprint(Problem6013Solution.second_or_1_iterator([1]))\n\n# Example 4: assigned result approach\nresult = second_or_1_iterator([9, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(second_or_1_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6014,
    "title": "Problem 6014",
    "description": "Write a Python function called `second_or_2_iterator` that must use an iterator to return the second value, or 2 when unavailable. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  second_or_2_iterator([9, 2, 3]) -> 2\n  second_or_2_iterator([1]) -> 2",
    "initialCode": "def second_or_2_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef second_or_2_iterator(values):\n    iterator = iter(values)\n    next(iterator, None)\n    return next(iterator, 2)\n\nprint(second_or_2_iterator([9, 2, 3]))  # Expected: 2\nprint(second_or_2_iterator([1]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_6014(values):\n    def calculate():\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 2)\n    return calculate()\n\nprint(solve_problem_6014([9, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6014Solution:\n    @staticmethod\n    def second_or_2_iterator(values):\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 2)\n\nprint(Problem6014Solution.second_or_2_iterator([1]))\n\n# Example 4: assigned result approach\nresult = second_or_2_iterator([9, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(second_or_2_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6015,
    "title": "Problem 6015",
    "description": "Write a Python function called `second_or_3_iterator` that must use an iterator to return the second value, or 3 when unavailable. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  second_or_3_iterator([9, 2, 3]) -> 2\n  second_or_3_iterator([1]) -> 3",
    "initialCode": "def second_or_3_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef second_or_3_iterator(values):\n    iterator = iter(values)\n    next(iterator, None)\n    return next(iterator, 3)\n\nprint(second_or_3_iterator([9, 2, 3]))  # Expected: 2\nprint(second_or_3_iterator([1]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_6015(values):\n    def calculate():\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 3)\n    return calculate()\n\nprint(solve_problem_6015([9, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6015Solution:\n    @staticmethod\n    def second_or_3_iterator(values):\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 3)\n\nprint(Problem6015Solution.second_or_3_iterator([1]))\n\n# Example 4: assigned result approach\nresult = second_or_3_iterator([9, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(second_or_3_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6016,
    "title": "Problem 6016",
    "description": "Write a Python function called `second_or_4_iterator` that must use an iterator to return the second value, or 4 when unavailable. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  second_or_4_iterator([9, 2, 3]) -> 2\n  second_or_4_iterator([1]) -> 4",
    "initialCode": "def second_or_4_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef second_or_4_iterator(values):\n    iterator = iter(values)\n    next(iterator, None)\n    return next(iterator, 4)\n\nprint(second_or_4_iterator([9, 2, 3]))  # Expected: 2\nprint(second_or_4_iterator([1]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_6016(values):\n    def calculate():\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 4)\n    return calculate()\n\nprint(solve_problem_6016([9, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6016Solution:\n    @staticmethod\n    def second_or_4_iterator(values):\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 4)\n\nprint(Problem6016Solution.second_or_4_iterator([1]))\n\n# Example 4: assigned result approach\nresult = second_or_4_iterator([9, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(second_or_4_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6017,
    "title": "Problem 6017",
    "description": "Write a Python function called `second_or_5_iterator` that must use an iterator to return the second value, or 5 when unavailable. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  second_or_5_iterator([9, 2, 3]) -> 2\n  second_or_5_iterator([1]) -> 5",
    "initialCode": "def second_or_5_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef second_or_5_iterator(values):\n    iterator = iter(values)\n    next(iterator, None)\n    return next(iterator, 5)\n\nprint(second_or_5_iterator([9, 2, 3]))  # Expected: 2\nprint(second_or_5_iterator([1]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_6017(values):\n    def calculate():\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 5)\n    return calculate()\n\nprint(solve_problem_6017([9, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6017Solution:\n    @staticmethod\n    def second_or_5_iterator(values):\n        iterator = iter(values)\n        next(iterator, None)\n        return next(iterator, 5)\n\nprint(Problem6017Solution.second_or_5_iterator([1]))\n\n# Example 4: assigned result approach\nresult = second_or_5_iterator([9, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(second_or_5_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6018,
    "title": "Problem 6018",
    "description": "Write a Python function called `take_1_iterator` that must take at most 1 values by repeatedly calling `next()` on an iterator. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  take_1_iterator([1, 2, 3, 4, 5, 6]) -> [1]\n  take_1_iterator([9]) -> [9]",
    "initialCode": "def take_1_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_1_iterator(values):\n    iterator = iter(values)\n    result = []\n    for _ in range(1):\n        marker = object()\n        value = next(iterator, marker)\n        if value is marker:\n            break\n        result.append(value)\n    return result\n\nprint(take_1_iterator([1, 2, 3, 4, 5, 6]))  # Expected: [1]\nprint(take_1_iterator([9]))  # Expected: [9]\n\n# Example 2: nested helper approach\ndef solve_problem_6018(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        for _ in range(1):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n    return calculate()\n\nprint(solve_problem_6018([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem6018Solution:\n    @staticmethod\n    def take_1_iterator(values):\n        iterator = iter(values)\n        result = []\n        for _ in range(1):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n\nprint(Problem6018Solution.take_1_iterator([9]))\n\n# Example 4: assigned result approach\nresult = take_1_iterator([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_1_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6019,
    "title": "Problem 6019",
    "description": "Write a Python function called `take_2_iterator` that must take at most 2 values by repeatedly calling `next()` on an iterator. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  take_2_iterator([1, 2, 3, 4, 5, 6]) -> [1, 2]\n  take_2_iterator([9]) -> [9]",
    "initialCode": "def take_2_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_2_iterator(values):\n    iterator = iter(values)\n    result = []\n    for _ in range(2):\n        marker = object()\n        value = next(iterator, marker)\n        if value is marker:\n            break\n        result.append(value)\n    return result\n\nprint(take_2_iterator([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2]\nprint(take_2_iterator([9]))  # Expected: [9]\n\n# Example 2: nested helper approach\ndef solve_problem_6019(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        for _ in range(2):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n    return calculate()\n\nprint(solve_problem_6019([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem6019Solution:\n    @staticmethod\n    def take_2_iterator(values):\n        iterator = iter(values)\n        result = []\n        for _ in range(2):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n\nprint(Problem6019Solution.take_2_iterator([9]))\n\n# Example 4: assigned result approach\nresult = take_2_iterator([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_2_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6020,
    "title": "Problem 6020",
    "description": "Write a Python function called `take_3_iterator` that must take at most 3 values by repeatedly calling `next()` on an iterator. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  take_3_iterator([1, 2, 3, 4, 5, 6]) -> [1, 2, 3]\n  take_3_iterator([9]) -> [9]",
    "initialCode": "def take_3_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_3_iterator(values):\n    iterator = iter(values)\n    result = []\n    for _ in range(3):\n        marker = object()\n        value = next(iterator, marker)\n        if value is marker:\n            break\n        result.append(value)\n    return result\n\nprint(take_3_iterator([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2, 3]\nprint(take_3_iterator([9]))  # Expected: [9]\n\n# Example 2: nested helper approach\ndef solve_problem_6020(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        for _ in range(3):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n    return calculate()\n\nprint(solve_problem_6020([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem6020Solution:\n    @staticmethod\n    def take_3_iterator(values):\n        iterator = iter(values)\n        result = []\n        for _ in range(3):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n\nprint(Problem6020Solution.take_3_iterator([9]))\n\n# Example 4: assigned result approach\nresult = take_3_iterator([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_3_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6021,
    "title": "Problem 6021",
    "description": "Write a Python function called `take_4_iterator` that must take at most 4 values by repeatedly calling `next()` on an iterator. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  take_4_iterator([1, 2, 3, 4, 5, 6]) -> [1, 2, 3, 4]\n  take_4_iterator([9]) -> [9]",
    "initialCode": "def take_4_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_4_iterator(values):\n    iterator = iter(values)\n    result = []\n    for _ in range(4):\n        marker = object()\n        value = next(iterator, marker)\n        if value is marker:\n            break\n        result.append(value)\n    return result\n\nprint(take_4_iterator([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2, 3, 4]\nprint(take_4_iterator([9]))  # Expected: [9]\n\n# Example 2: nested helper approach\ndef solve_problem_6021(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        for _ in range(4):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n    return calculate()\n\nprint(solve_problem_6021([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem6021Solution:\n    @staticmethod\n    def take_4_iterator(values):\n        iterator = iter(values)\n        result = []\n        for _ in range(4):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n\nprint(Problem6021Solution.take_4_iterator([9]))\n\n# Example 4: assigned result approach\nresult = take_4_iterator([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_4_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6022,
    "title": "Problem 6022",
    "description": "Write a Python function called `take_5_iterator` that must take at most 5 values by repeatedly calling `next()` on an iterator. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  take_5_iterator([1, 2, 3, 4, 5, 6]) -> [1, 2, 3, 4, 5]\n  take_5_iterator([9]) -> [9]",
    "initialCode": "def take_5_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef take_5_iterator(values):\n    iterator = iter(values)\n    result = []\n    for _ in range(5):\n        marker = object()\n        value = next(iterator, marker)\n        if value is marker:\n            break\n        result.append(value)\n    return result\n\nprint(take_5_iterator([1, 2, 3, 4, 5, 6]))  # Expected: [1, 2, 3, 4, 5]\nprint(take_5_iterator([9]))  # Expected: [9]\n\n# Example 2: nested helper approach\ndef solve_problem_6022(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        for _ in range(5):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n    return calculate()\n\nprint(solve_problem_6022([1, 2, 3, 4, 5, 6]))\n\n# Example 3: static method approach\nclass Problem6022Solution:\n    @staticmethod\n    def take_5_iterator(values):\n        iterator = iter(values)\n        result = []\n        for _ in range(5):\n            marker = object()\n            value = next(iterator, marker)\n            if value is marker:\n                break\n            result.append(value)\n        return result\n\nprint(Problem6022Solution.take_5_iterator([9]))\n\n# Example 4: assigned result approach\nresult = take_5_iterator([1, 2, 3, 4, 5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(take_5_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6023,
    "title": "Problem 6023",
    "description": "Write a Python function called `iterator_sum_plus_1` that must sum an iterator and add 1. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_sum_plus_1([1, 2, 3]) -> 7\n  iterator_sum_plus_1([]) -> 1",
    "initialCode": "def iterator_sum_plus_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_sum_plus_1(values):\n    iterator = iter(values)\n    return sum(iterator) + 1\n\nprint(iterator_sum_plus_1([1, 2, 3]))  # Expected: 7\nprint(iterator_sum_plus_1([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_6023(values):\n    def calculate():\n        iterator = iter(values)\n        return sum(iterator) + 1\n    return calculate()\n\nprint(solve_problem_6023([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6023Solution:\n    @staticmethod\n    def iterator_sum_plus_1(values):\n        iterator = iter(values)\n        return sum(iterator) + 1\n\nprint(Problem6023Solution.iterator_sum_plus_1([]))\n\n# Example 4: assigned result approach\nresult = iterator_sum_plus_1([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_sum_plus_1([-2, 5]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6024,
    "title": "Problem 6024",
    "description": "Write a Python function called `iterator_sum_plus_2` that must sum an iterator and add 2. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_sum_plus_2([1, 2, 3]) -> 8\n  iterator_sum_plus_2([]) -> 2",
    "initialCode": "def iterator_sum_plus_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_sum_plus_2(values):\n    iterator = iter(values)\n    return sum(iterator) + 2\n\nprint(iterator_sum_plus_2([1, 2, 3]))  # Expected: 8\nprint(iterator_sum_plus_2([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_6024(values):\n    def calculate():\n        iterator = iter(values)\n        return sum(iterator) + 2\n    return calculate()\n\nprint(solve_problem_6024([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6024Solution:\n    @staticmethod\n    def iterator_sum_plus_2(values):\n        iterator = iter(values)\n        return sum(iterator) + 2\n\nprint(Problem6024Solution.iterator_sum_plus_2([]))\n\n# Example 4: assigned result approach\nresult = iterator_sum_plus_2([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_sum_plus_2([-2, 5]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6025,
    "title": "Problem 6025",
    "description": "Write a Python function called `iterator_sum_plus_3` that must sum an iterator and add 3. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_sum_plus_3([1, 2, 3]) -> 9\n  iterator_sum_plus_3([]) -> 3",
    "initialCode": "def iterator_sum_plus_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_sum_plus_3(values):\n    iterator = iter(values)\n    return sum(iterator) + 3\n\nprint(iterator_sum_plus_3([1, 2, 3]))  # Expected: 9\nprint(iterator_sum_plus_3([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_6025(values):\n    def calculate():\n        iterator = iter(values)\n        return sum(iterator) + 3\n    return calculate()\n\nprint(solve_problem_6025([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6025Solution:\n    @staticmethod\n    def iterator_sum_plus_3(values):\n        iterator = iter(values)\n        return sum(iterator) + 3\n\nprint(Problem6025Solution.iterator_sum_plus_3([]))\n\n# Example 4: assigned result approach\nresult = iterator_sum_plus_3([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_sum_plus_3([-2, 5]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6026,
    "title": "Problem 6026",
    "description": "Write a Python function called `iterator_sum_plus_4` that must sum an iterator and add 4. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_sum_plus_4([1, 2, 3]) -> 10\n  iterator_sum_plus_4([]) -> 4",
    "initialCode": "def iterator_sum_plus_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_sum_plus_4(values):\n    iterator = iter(values)\n    return sum(iterator) + 4\n\nprint(iterator_sum_plus_4([1, 2, 3]))  # Expected: 10\nprint(iterator_sum_plus_4([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_6026(values):\n    def calculate():\n        iterator = iter(values)\n        return sum(iterator) + 4\n    return calculate()\n\nprint(solve_problem_6026([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6026Solution:\n    @staticmethod\n    def iterator_sum_plus_4(values):\n        iterator = iter(values)\n        return sum(iterator) + 4\n\nprint(Problem6026Solution.iterator_sum_plus_4([]))\n\n# Example 4: assigned result approach\nresult = iterator_sum_plus_4([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_sum_plus_4([-2, 5]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6027,
    "title": "Problem 6027",
    "description": "Write a Python function called `iterator_sum_plus_5` that must sum an iterator and add 5. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_sum_plus_5([1, 2, 3]) -> 11\n  iterator_sum_plus_5([]) -> 5",
    "initialCode": "def iterator_sum_plus_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_sum_plus_5(values):\n    iterator = iter(values)\n    return sum(iterator) + 5\n\nprint(iterator_sum_plus_5([1, 2, 3]))  # Expected: 11\nprint(iterator_sum_plus_5([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_6027(values):\n    def calculate():\n        iterator = iter(values)\n        return sum(iterator) + 5\n    return calculate()\n\nprint(solve_problem_6027([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6027Solution:\n    @staticmethod\n    def iterator_sum_plus_5(values):\n        iterator = iter(values)\n        return sum(iterator) + 5\n\nprint(Problem6027Solution.iterator_sum_plus_5([]))\n\n# Example 4: assigned result approach\nresult = iterator_sum_plus_5([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_sum_plus_5([-2, 5]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6028,
    "title": "Problem 6028",
    "description": "Write a Python function called `skip_1_iterator` that must skip 1 iterator values and return the next one or `default`. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  skip_1_iterator([1, 2, 3, 4, 5, 6], -1) -> 2\n  skip_1_iterator([9], 0) -> 0",
    "initialCode": "def skip_1_iterator(values, default):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef skip_1_iterator(values, default):\n    iterator = iter(values)\n    for _ in range(1):\n        next(iterator, default)\n    return next(iterator, default)\n\nprint(skip_1_iterator([1, 2, 3, 4, 5, 6], -1))  # Expected: 2\nprint(skip_1_iterator([9], 0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6028(values, default):\n    def calculate():\n        iterator = iter(values)\n        for _ in range(1):\n            next(iterator, default)\n        return next(iterator, default)\n    return calculate()\n\nprint(solve_problem_6028([1, 2, 3, 4, 5, 6], -1))\n\n# Example 3: static method approach\nclass Problem6028Solution:\n    @staticmethod\n    def skip_1_iterator(values, default):\n        iterator = iter(values)\n        for _ in range(1):\n            next(iterator, default)\n        return next(iterator, default)\n\nprint(Problem6028Solution.skip_1_iterator([9], 0))\n\n# Example 4: assigned result approach\nresult = skip_1_iterator([1, 2, 3, 4, 5, 6], -1)\nprint(result)\n\n# Example 5: direct call\nprint(skip_1_iterator([], 7))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6029,
    "title": "Problem 6029",
    "description": "Write a Python function called `skip_2_iterator` that must skip 2 iterator values and return the next one or `default`. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  skip_2_iterator([1, 2, 3, 4, 5, 6], -1) -> 3\n  skip_2_iterator([9], 0) -> 0",
    "initialCode": "def skip_2_iterator(values, default):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef skip_2_iterator(values, default):\n    iterator = iter(values)\n    for _ in range(2):\n        next(iterator, default)\n    return next(iterator, default)\n\nprint(skip_2_iterator([1, 2, 3, 4, 5, 6], -1))  # Expected: 3\nprint(skip_2_iterator([9], 0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6029(values, default):\n    def calculate():\n        iterator = iter(values)\n        for _ in range(2):\n            next(iterator, default)\n        return next(iterator, default)\n    return calculate()\n\nprint(solve_problem_6029([1, 2, 3, 4, 5, 6], -1))\n\n# Example 3: static method approach\nclass Problem6029Solution:\n    @staticmethod\n    def skip_2_iterator(values, default):\n        iterator = iter(values)\n        for _ in range(2):\n            next(iterator, default)\n        return next(iterator, default)\n\nprint(Problem6029Solution.skip_2_iterator([9], 0))\n\n# Example 4: assigned result approach\nresult = skip_2_iterator([1, 2, 3, 4, 5, 6], -1)\nprint(result)\n\n# Example 5: direct call\nprint(skip_2_iterator([], 7))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6030,
    "title": "Problem 6030",
    "description": "Write a Python function called `skip_3_iterator` that must skip 3 iterator values and return the next one or `default`. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  skip_3_iterator([1, 2, 3, 4, 5, 6], -1) -> 4\n  skip_3_iterator([9], 0) -> 0",
    "initialCode": "def skip_3_iterator(values, default):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef skip_3_iterator(values, default):\n    iterator = iter(values)\n    for _ in range(3):\n        next(iterator, default)\n    return next(iterator, default)\n\nprint(skip_3_iterator([1, 2, 3, 4, 5, 6], -1))  # Expected: 4\nprint(skip_3_iterator([9], 0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6030(values, default):\n    def calculate():\n        iterator = iter(values)\n        for _ in range(3):\n            next(iterator, default)\n        return next(iterator, default)\n    return calculate()\n\nprint(solve_problem_6030([1, 2, 3, 4, 5, 6], -1))\n\n# Example 3: static method approach\nclass Problem6030Solution:\n    @staticmethod\n    def skip_3_iterator(values, default):\n        iterator = iter(values)\n        for _ in range(3):\n            next(iterator, default)\n        return next(iterator, default)\n\nprint(Problem6030Solution.skip_3_iterator([9], 0))\n\n# Example 4: assigned result approach\nresult = skip_3_iterator([1, 2, 3, 4, 5, 6], -1)\nprint(result)\n\n# Example 5: direct call\nprint(skip_3_iterator([], 7))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6031,
    "title": "Problem 6031",
    "description": "Write a Python function called `skip_4_iterator` that must skip 4 iterator values and return the next one or `default`. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  skip_4_iterator([1, 2, 3, 4, 5, 6], -1) -> 5\n  skip_4_iterator([9], 0) -> 0",
    "initialCode": "def skip_4_iterator(values, default):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef skip_4_iterator(values, default):\n    iterator = iter(values)\n    for _ in range(4):\n        next(iterator, default)\n    return next(iterator, default)\n\nprint(skip_4_iterator([1, 2, 3, 4, 5, 6], -1))  # Expected: 5\nprint(skip_4_iterator([9], 0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6031(values, default):\n    def calculate():\n        iterator = iter(values)\n        for _ in range(4):\n            next(iterator, default)\n        return next(iterator, default)\n    return calculate()\n\nprint(solve_problem_6031([1, 2, 3, 4, 5, 6], -1))\n\n# Example 3: static method approach\nclass Problem6031Solution:\n    @staticmethod\n    def skip_4_iterator(values, default):\n        iterator = iter(values)\n        for _ in range(4):\n            next(iterator, default)\n        return next(iterator, default)\n\nprint(Problem6031Solution.skip_4_iterator([9], 0))\n\n# Example 4: assigned result approach\nresult = skip_4_iterator([1, 2, 3, 4, 5, 6], -1)\nprint(result)\n\n# Example 5: direct call\nprint(skip_4_iterator([], 7))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6032,
    "title": "Problem 6032",
    "description": "Write a Python function called `skip_5_iterator` that must skip 5 iterator values and return the next one or `default`. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  skip_5_iterator([1, 2, 3, 4, 5, 6], -1) -> 6\n  skip_5_iterator([9], 0) -> 0",
    "initialCode": "def skip_5_iterator(values, default):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef skip_5_iterator(values, default):\n    iterator = iter(values)\n    for _ in range(5):\n        next(iterator, default)\n    return next(iterator, default)\n\nprint(skip_5_iterator([1, 2, 3, 4, 5, 6], -1))  # Expected: 6\nprint(skip_5_iterator([9], 0))  # Expected: 0\n\n# Example 2: nested helper approach\ndef solve_problem_6032(values, default):\n    def calculate():\n        iterator = iter(values)\n        for _ in range(5):\n            next(iterator, default)\n        return next(iterator, default)\n    return calculate()\n\nprint(solve_problem_6032([1, 2, 3, 4, 5, 6], -1))\n\n# Example 3: static method approach\nclass Problem6032Solution:\n    @staticmethod\n    def skip_5_iterator(values, default):\n        iterator = iter(values)\n        for _ in range(5):\n            next(iterator, default)\n        return next(iterator, default)\n\nprint(Problem6032Solution.skip_5_iterator([9], 0))\n\n# Example 4: assigned result approach\nresult = skip_5_iterator([1, 2, 3, 4, 5, 6], -1)\nprint(result)\n\n# Example 5: direct call\nprint(skip_5_iterator([], 7))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6033,
    "title": "Problem 6033",
    "description": "Write a Python function called `first_pair_1_iterator` that must return the first two iterator values as a list, using 1 for each missing value. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_pair_1_iterator([1, 2, 3]) -> [1, 2]\n  first_pair_1_iterator([9]) -> [9, 1]",
    "initialCode": "def first_pair_1_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_pair_1_iterator(values):\n    iterator = iter(values)\n    return [next(iterator, 1), next(iterator, 1)]\n\nprint(first_pair_1_iterator([1, 2, 3]))  # Expected: [1, 2]\nprint(first_pair_1_iterator([9]))  # Expected: [9, 1]\n\n# Example 2: nested helper approach\ndef solve_problem_6033(values):\n    def calculate():\n        iterator = iter(values)\n        return [next(iterator, 1), next(iterator, 1)]\n    return calculate()\n\nprint(solve_problem_6033([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6033Solution:\n    @staticmethod\n    def first_pair_1_iterator(values):\n        iterator = iter(values)\n        return [next(iterator, 1), next(iterator, 1)]\n\nprint(Problem6033Solution.first_pair_1_iterator([9]))\n\n# Example 4: assigned result approach\nresult = first_pair_1_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(first_pair_1_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6034,
    "title": "Problem 6034",
    "description": "Write a Python function called `first_pair_2_iterator` that must return the first two iterator values as a list, using 2 for each missing value. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_pair_2_iterator([1, 2, 3]) -> [1, 2]\n  first_pair_2_iterator([9]) -> [9, 2]",
    "initialCode": "def first_pair_2_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_pair_2_iterator(values):\n    iterator = iter(values)\n    return [next(iterator, 2), next(iterator, 2)]\n\nprint(first_pair_2_iterator([1, 2, 3]))  # Expected: [1, 2]\nprint(first_pair_2_iterator([9]))  # Expected: [9, 2]\n\n# Example 2: nested helper approach\ndef solve_problem_6034(values):\n    def calculate():\n        iterator = iter(values)\n        return [next(iterator, 2), next(iterator, 2)]\n    return calculate()\n\nprint(solve_problem_6034([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6034Solution:\n    @staticmethod\n    def first_pair_2_iterator(values):\n        iterator = iter(values)\n        return [next(iterator, 2), next(iterator, 2)]\n\nprint(Problem6034Solution.first_pair_2_iterator([9]))\n\n# Example 4: assigned result approach\nresult = first_pair_2_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(first_pair_2_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6035,
    "title": "Problem 6035",
    "description": "Write a Python function called `first_pair_3_iterator` that must return the first two iterator values as a list, using 3 for each missing value. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_pair_3_iterator([1, 2, 3]) -> [1, 2]\n  first_pair_3_iterator([9]) -> [9, 3]",
    "initialCode": "def first_pair_3_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_pair_3_iterator(values):\n    iterator = iter(values)\n    return [next(iterator, 3), next(iterator, 3)]\n\nprint(first_pair_3_iterator([1, 2, 3]))  # Expected: [1, 2]\nprint(first_pair_3_iterator([9]))  # Expected: [9, 3]\n\n# Example 2: nested helper approach\ndef solve_problem_6035(values):\n    def calculate():\n        iterator = iter(values)\n        return [next(iterator, 3), next(iterator, 3)]\n    return calculate()\n\nprint(solve_problem_6035([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6035Solution:\n    @staticmethod\n    def first_pair_3_iterator(values):\n        iterator = iter(values)\n        return [next(iterator, 3), next(iterator, 3)]\n\nprint(Problem6035Solution.first_pair_3_iterator([9]))\n\n# Example 4: assigned result approach\nresult = first_pair_3_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(first_pair_3_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6036,
    "title": "Problem 6036",
    "description": "Write a Python function called `first_pair_4_iterator` that must return the first two iterator values as a list, using 4 for each missing value. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_pair_4_iterator([1, 2, 3]) -> [1, 2]\n  first_pair_4_iterator([9]) -> [9, 4]",
    "initialCode": "def first_pair_4_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_pair_4_iterator(values):\n    iterator = iter(values)\n    return [next(iterator, 4), next(iterator, 4)]\n\nprint(first_pair_4_iterator([1, 2, 3]))  # Expected: [1, 2]\nprint(first_pair_4_iterator([9]))  # Expected: [9, 4]\n\n# Example 2: nested helper approach\ndef solve_problem_6036(values):\n    def calculate():\n        iterator = iter(values)\n        return [next(iterator, 4), next(iterator, 4)]\n    return calculate()\n\nprint(solve_problem_6036([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6036Solution:\n    @staticmethod\n    def first_pair_4_iterator(values):\n        iterator = iter(values)\n        return [next(iterator, 4), next(iterator, 4)]\n\nprint(Problem6036Solution.first_pair_4_iterator([9]))\n\n# Example 4: assigned result approach\nresult = first_pair_4_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(first_pair_4_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6037,
    "title": "Problem 6037",
    "description": "Write a Python function called `first_pair_5_iterator` that must return the first two iterator values as a list, using 5 for each missing value. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  first_pair_5_iterator([1, 2, 3]) -> [1, 2]\n  first_pair_5_iterator([9]) -> [9, 5]",
    "initialCode": "def first_pair_5_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_pair_5_iterator(values):\n    iterator = iter(values)\n    return [next(iterator, 5), next(iterator, 5)]\n\nprint(first_pair_5_iterator([1, 2, 3]))  # Expected: [1, 2]\nprint(first_pair_5_iterator([9]))  # Expected: [9, 5]\n\n# Example 2: nested helper approach\ndef solve_problem_6037(values):\n    def calculate():\n        iterator = iter(values)\n        return [next(iterator, 5), next(iterator, 5)]\n    return calculate()\n\nprint(solve_problem_6037([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6037Solution:\n    @staticmethod\n    def first_pair_5_iterator(values):\n        iterator = iter(values)\n        return [next(iterator, 5), next(iterator, 5)]\n\nprint(Problem6037Solution.first_pair_5_iterator([9]))\n\n# Example 4: assigned result approach\nresult = first_pair_5_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(first_pair_5_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6038,
    "title": "Problem 6038",
    "description": "Write a Python function called `iterator_count_plus_1` that must count values consumed from an iterator and add 1. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_count_plus_1([1, 2, 3]) -> 4\n  iterator_count_plus_1([]) -> 1",
    "initialCode": "def iterator_count_plus_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_count_plus_1(values):\n    iterator = iter(values)\n    count = 1\n    for _ in iterator:\n        count += 1\n    return count\n\nprint(iterator_count_plus_1([1, 2, 3]))  # Expected: 4\nprint(iterator_count_plus_1([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_6038(values):\n    def calculate():\n        iterator = iter(values)\n        count = 1\n        for _ in iterator:\n            count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6038([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6038Solution:\n    @staticmethod\n    def iterator_count_plus_1(values):\n        iterator = iter(values)\n        count = 1\n        for _ in iterator:\n            count += 1\n        return count\n\nprint(Problem6038Solution.iterator_count_plus_1([]))\n\n# Example 4: assigned result approach\nresult = iterator_count_plus_1([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_count_plus_1([\"a\"]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6039,
    "title": "Problem 6039",
    "description": "Write a Python function called `iterator_count_plus_2` that must count values consumed from an iterator and add 2. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_count_plus_2([1, 2, 3]) -> 5\n  iterator_count_plus_2([]) -> 2",
    "initialCode": "def iterator_count_plus_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_count_plus_2(values):\n    iterator = iter(values)\n    count = 2\n    for _ in iterator:\n        count += 1\n    return count\n\nprint(iterator_count_plus_2([1, 2, 3]))  # Expected: 5\nprint(iterator_count_plus_2([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_6039(values):\n    def calculate():\n        iterator = iter(values)\n        count = 2\n        for _ in iterator:\n            count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6039([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6039Solution:\n    @staticmethod\n    def iterator_count_plus_2(values):\n        iterator = iter(values)\n        count = 2\n        for _ in iterator:\n            count += 1\n        return count\n\nprint(Problem6039Solution.iterator_count_plus_2([]))\n\n# Example 4: assigned result approach\nresult = iterator_count_plus_2([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_count_plus_2([\"a\"]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6040,
    "title": "Problem 6040",
    "description": "Write a Python function called `iterator_count_plus_3` that must count values consumed from an iterator and add 3. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_count_plus_3([1, 2, 3]) -> 6\n  iterator_count_plus_3([]) -> 3",
    "initialCode": "def iterator_count_plus_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_count_plus_3(values):\n    iterator = iter(values)\n    count = 3\n    for _ in iterator:\n        count += 1\n    return count\n\nprint(iterator_count_plus_3([1, 2, 3]))  # Expected: 6\nprint(iterator_count_plus_3([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_6040(values):\n    def calculate():\n        iterator = iter(values)\n        count = 3\n        for _ in iterator:\n            count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6040([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6040Solution:\n    @staticmethod\n    def iterator_count_plus_3(values):\n        iterator = iter(values)\n        count = 3\n        for _ in iterator:\n            count += 1\n        return count\n\nprint(Problem6040Solution.iterator_count_plus_3([]))\n\n# Example 4: assigned result approach\nresult = iterator_count_plus_3([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_count_plus_3([\"a\"]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6041,
    "title": "Problem 6041",
    "description": "Write a Python function called `iterator_count_plus_4` that must count values consumed from an iterator and add 4. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_count_plus_4([1, 2, 3]) -> 7\n  iterator_count_plus_4([]) -> 4",
    "initialCode": "def iterator_count_plus_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_count_plus_4(values):\n    iterator = iter(values)\n    count = 4\n    for _ in iterator:\n        count += 1\n    return count\n\nprint(iterator_count_plus_4([1, 2, 3]))  # Expected: 7\nprint(iterator_count_plus_4([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_6041(values):\n    def calculate():\n        iterator = iter(values)\n        count = 4\n        for _ in iterator:\n            count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6041([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6041Solution:\n    @staticmethod\n    def iterator_count_plus_4(values):\n        iterator = iter(values)\n        count = 4\n        for _ in iterator:\n            count += 1\n        return count\n\nprint(Problem6041Solution.iterator_count_plus_4([]))\n\n# Example 4: assigned result approach\nresult = iterator_count_plus_4([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_count_plus_4([\"a\"]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6042,
    "title": "Problem 6042",
    "description": "Write a Python function called `iterator_count_plus_5` that must count values consumed from an iterator and add 5. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_count_plus_5([1, 2, 3]) -> 8\n  iterator_count_plus_5([]) -> 5",
    "initialCode": "def iterator_count_plus_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_count_plus_5(values):\n    iterator = iter(values)\n    count = 5\n    for _ in iterator:\n        count += 1\n    return count\n\nprint(iterator_count_plus_5([1, 2, 3]))  # Expected: 8\nprint(iterator_count_plus_5([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_6042(values):\n    def calculate():\n        iterator = iter(values)\n        count = 5\n        for _ in iterator:\n            count += 1\n        return count\n    return calculate()\n\nprint(solve_problem_6042([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6042Solution:\n    @staticmethod\n    def iterator_count_plus_5(values):\n        iterator = iter(values)\n        count = 5\n        for _ in iterator:\n            count += 1\n        return count\n\nprint(Problem6042Solution.iterator_count_plus_5([]))\n\n# Example 4: assigned result approach\nresult = iterator_count_plus_5([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_count_plus_5([\"a\"]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6043,
    "title": "Problem 6043",
    "description": "Write a Python function called `last_or_1_iterator` that must consume an iterator and return its last value, or 1 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  last_or_1_iterator([1, 2, 3]) -> 3\n  last_or_1_iterator([]) -> 1",
    "initialCode": "def last_or_1_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef last_or_1_iterator(values):\n    iterator = iter(values)\n    result = 1\n    for value in iterator:\n        result = value\n    return result\n\nprint(last_or_1_iterator([1, 2, 3]))  # Expected: 3\nprint(last_or_1_iterator([]))  # Expected: 1\n\n# Example 2: nested helper approach\ndef solve_problem_6043(values):\n    def calculate():\n        iterator = iter(values)\n        result = 1\n        for value in iterator:\n            result = value\n        return result\n    return calculate()\n\nprint(solve_problem_6043([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6043Solution:\n    @staticmethod\n    def last_or_1_iterator(values):\n        iterator = iter(values)\n        result = 1\n        for value in iterator:\n            result = value\n        return result\n\nprint(Problem6043Solution.last_or_1_iterator([]))\n\n# Example 4: assigned result approach\nresult = last_or_1_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(last_or_1_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6044,
    "title": "Problem 6044",
    "description": "Write a Python function called `last_or_2_iterator` that must consume an iterator and return its last value, or 2 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  last_or_2_iterator([1, 2, 3]) -> 3\n  last_or_2_iterator([]) -> 2",
    "initialCode": "def last_or_2_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef last_or_2_iterator(values):\n    iterator = iter(values)\n    result = 2\n    for value in iterator:\n        result = value\n    return result\n\nprint(last_or_2_iterator([1, 2, 3]))  # Expected: 3\nprint(last_or_2_iterator([]))  # Expected: 2\n\n# Example 2: nested helper approach\ndef solve_problem_6044(values):\n    def calculate():\n        iterator = iter(values)\n        result = 2\n        for value in iterator:\n            result = value\n        return result\n    return calculate()\n\nprint(solve_problem_6044([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6044Solution:\n    @staticmethod\n    def last_or_2_iterator(values):\n        iterator = iter(values)\n        result = 2\n        for value in iterator:\n            result = value\n        return result\n\nprint(Problem6044Solution.last_or_2_iterator([]))\n\n# Example 4: assigned result approach\nresult = last_or_2_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(last_or_2_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6045,
    "title": "Problem 6045",
    "description": "Write a Python function called `last_or_3_iterator` that must consume an iterator and return its last value, or 3 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  last_or_3_iterator([1, 2, 3]) -> 3\n  last_or_3_iterator([]) -> 3",
    "initialCode": "def last_or_3_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef last_or_3_iterator(values):\n    iterator = iter(values)\n    result = 3\n    for value in iterator:\n        result = value\n    return result\n\nprint(last_or_3_iterator([1, 2, 3]))  # Expected: 3\nprint(last_or_3_iterator([]))  # Expected: 3\n\n# Example 2: nested helper approach\ndef solve_problem_6045(values):\n    def calculate():\n        iterator = iter(values)\n        result = 3\n        for value in iterator:\n            result = value\n        return result\n    return calculate()\n\nprint(solve_problem_6045([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6045Solution:\n    @staticmethod\n    def last_or_3_iterator(values):\n        iterator = iter(values)\n        result = 3\n        for value in iterator:\n            result = value\n        return result\n\nprint(Problem6045Solution.last_or_3_iterator([]))\n\n# Example 4: assigned result approach\nresult = last_or_3_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(last_or_3_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6046,
    "title": "Problem 6046",
    "description": "Write a Python function called `last_or_4_iterator` that must consume an iterator and return its last value, or 4 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  last_or_4_iterator([1, 2, 3]) -> 3\n  last_or_4_iterator([]) -> 4",
    "initialCode": "def last_or_4_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef last_or_4_iterator(values):\n    iterator = iter(values)\n    result = 4\n    for value in iterator:\n        result = value\n    return result\n\nprint(last_or_4_iterator([1, 2, 3]))  # Expected: 3\nprint(last_or_4_iterator([]))  # Expected: 4\n\n# Example 2: nested helper approach\ndef solve_problem_6046(values):\n    def calculate():\n        iterator = iter(values)\n        result = 4\n        for value in iterator:\n            result = value\n        return result\n    return calculate()\n\nprint(solve_problem_6046([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6046Solution:\n    @staticmethod\n    def last_or_4_iterator(values):\n        iterator = iter(values)\n        result = 4\n        for value in iterator:\n            result = value\n        return result\n\nprint(Problem6046Solution.last_or_4_iterator([]))\n\n# Example 4: assigned result approach\nresult = last_or_4_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(last_or_4_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6047,
    "title": "Problem 6047",
    "description": "Write a Python function called `last_or_5_iterator` that must consume an iterator and return its last value, or 5 when empty. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  last_or_5_iterator([1, 2, 3]) -> 3\n  last_or_5_iterator([]) -> 5",
    "initialCode": "def last_or_5_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef last_or_5_iterator(values):\n    iterator = iter(values)\n    result = 5\n    for value in iterator:\n        result = value\n    return result\n\nprint(last_or_5_iterator([1, 2, 3]))  # Expected: 3\nprint(last_or_5_iterator([]))  # Expected: 5\n\n# Example 2: nested helper approach\ndef solve_problem_6047(values):\n    def calculate():\n        iterator = iter(values)\n        result = 5\n        for value in iterator:\n            result = value\n        return result\n    return calculate()\n\nprint(solve_problem_6047([1, 2, 3]))\n\n# Example 3: static method approach\nclass Problem6047Solution:\n    @staticmethod\n    def last_or_5_iterator(values):\n        iterator = iter(values)\n        result = 5\n        for value in iterator:\n            result = value\n        return result\n\nprint(Problem6047Solution.last_or_5_iterator([]))\n\n# Example 4: assigned result approach\nresult = last_or_5_iterator([1, 2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(last_or_5_iterator([-1]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6048,
    "title": "Problem 6048",
    "description": "Write a Python function called `iterator_all_above_1` that must use an iterator to test whether every value exceeds 1. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_all_above_1([2, 3]) -> True\n  iterator_all_above_1([1, 3]) -> False",
    "initialCode": "def iterator_all_above_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_all_above_1(values):\n    iterator = iter(values)\n    for value in iterator:\n        if value <= 1:\n            return False\n    return True\n\nprint(iterator_all_above_1([2, 3]))  # Expected: True\nprint(iterator_all_above_1([1, 3]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_6048(values):\n    def calculate():\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 1:\n                return False\n        return True\n    return calculate()\n\nprint(solve_problem_6048([2, 3]))\n\n# Example 3: static method approach\nclass Problem6048Solution:\n    @staticmethod\n    def iterator_all_above_1(values):\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 1:\n                return False\n        return True\n\nprint(Problem6048Solution.iterator_all_above_1([1, 3]))\n\n# Example 4: assigned result approach\nresult = iterator_all_above_1([2, 3])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_all_above_1([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6049,
    "title": "Problem 6049",
    "description": "Write a Python function called `iterator_all_above_2` that must use an iterator to test whether every value exceeds 2. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_all_above_2([3, 4]) -> True\n  iterator_all_above_2([2, 4]) -> False",
    "initialCode": "def iterator_all_above_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_all_above_2(values):\n    iterator = iter(values)\n    for value in iterator:\n        if value <= 2:\n            return False\n    return True\n\nprint(iterator_all_above_2([3, 4]))  # Expected: True\nprint(iterator_all_above_2([2, 4]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_6049(values):\n    def calculate():\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 2:\n                return False\n        return True\n    return calculate()\n\nprint(solve_problem_6049([3, 4]))\n\n# Example 3: static method approach\nclass Problem6049Solution:\n    @staticmethod\n    def iterator_all_above_2(values):\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 2:\n                return False\n        return True\n\nprint(Problem6049Solution.iterator_all_above_2([2, 4]))\n\n# Example 4: assigned result approach\nresult = iterator_all_above_2([3, 4])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_all_above_2([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6050,
    "title": "Problem 6050",
    "description": "Write a Python function called `iterator_all_above_3` that must use an iterator to test whether every value exceeds 3. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_all_above_3([4, 5]) -> True\n  iterator_all_above_3([3, 5]) -> False",
    "initialCode": "def iterator_all_above_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_all_above_3(values):\n    iterator = iter(values)\n    for value in iterator:\n        if value <= 3:\n            return False\n    return True\n\nprint(iterator_all_above_3([4, 5]))  # Expected: True\nprint(iterator_all_above_3([3, 5]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_6050(values):\n    def calculate():\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 3:\n                return False\n        return True\n    return calculate()\n\nprint(solve_problem_6050([4, 5]))\n\n# Example 3: static method approach\nclass Problem6050Solution:\n    @staticmethod\n    def iterator_all_above_3(values):\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 3:\n                return False\n        return True\n\nprint(Problem6050Solution.iterator_all_above_3([3, 5]))\n\n# Example 4: assigned result approach\nresult = iterator_all_above_3([4, 5])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_all_above_3([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6051,
    "title": "Problem 6051",
    "description": "Write a Python function called `iterator_all_above_4` that must use an iterator to test whether every value exceeds 4. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_all_above_4([5, 6]) -> True\n  iterator_all_above_4([4, 6]) -> False",
    "initialCode": "def iterator_all_above_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_all_above_4(values):\n    iterator = iter(values)\n    for value in iterator:\n        if value <= 4:\n            return False\n    return True\n\nprint(iterator_all_above_4([5, 6]))  # Expected: True\nprint(iterator_all_above_4([4, 6]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_6051(values):\n    def calculate():\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 4:\n                return False\n        return True\n    return calculate()\n\nprint(solve_problem_6051([5, 6]))\n\n# Example 3: static method approach\nclass Problem6051Solution:\n    @staticmethod\n    def iterator_all_above_4(values):\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 4:\n                return False\n        return True\n\nprint(Problem6051Solution.iterator_all_above_4([4, 6]))\n\n# Example 4: assigned result approach\nresult = iterator_all_above_4([5, 6])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_all_above_4([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6052,
    "title": "Problem 6052",
    "description": "Write a Python function called `iterator_all_above_5` that must use an iterator to test whether every value exceeds 5. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  iterator_all_above_5([6, 7]) -> True\n  iterator_all_above_5([5, 7]) -> False",
    "initialCode": "def iterator_all_above_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef iterator_all_above_5(values):\n    iterator = iter(values)\n    for value in iterator:\n        if value <= 5:\n            return False\n    return True\n\nprint(iterator_all_above_5([6, 7]))  # Expected: True\nprint(iterator_all_above_5([5, 7]))  # Expected: False\n\n# Example 2: nested helper approach\ndef solve_problem_6052(values):\n    def calculate():\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 5:\n                return False\n        return True\n    return calculate()\n\nprint(solve_problem_6052([6, 7]))\n\n# Example 3: static method approach\nclass Problem6052Solution:\n    @staticmethod\n    def iterator_all_above_5(values):\n        iterator = iter(values)\n        for value in iterator:\n            if value <= 5:\n                return False\n        return True\n\nprint(Problem6052Solution.iterator_all_above_5([5, 7]))\n\n# Example 4: assigned result approach\nresult = iterator_all_above_5([6, 7])\nprint(result)\n\n# Example 5: direct call\nprint(iterator_all_above_5([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6053,
    "title": "Problem 6053",
    "description": "Write a Python function called `indexed_from_1_iterator` that must consume an iterator and pair values with indexes in two-item lists beginning at 1. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  indexed_from_1_iterator([\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"]]\n  indexed_from_1_iterator([9]) -> [[1, 9]]",
    "initialCode": "def indexed_from_1_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_from_1_iterator(values):\n    iterator = iter(values)\n    result = []\n    index = 1\n    for value in iterator:\n        result.append([index, value])\n        index += 1\n    return result\n\nprint(indexed_from_1_iterator([\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"]]\nprint(indexed_from_1_iterator([9]))  # Expected: [[1, 9]]\n\n# Example 2: nested helper approach\ndef solve_problem_6053(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        index = 1\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_6053([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6053Solution:\n    @staticmethod\n    def indexed_from_1_iterator(values):\n        iterator = iter(values)\n        result = []\n        index = 1\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n\nprint(Problem6053Solution.indexed_from_1_iterator([9]))\n\n# Example 4: assigned result approach\nresult = indexed_from_1_iterator([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(indexed_from_1_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6054,
    "title": "Problem 6054",
    "description": "Write a Python function called `indexed_from_2_iterator` that must consume an iterator and pair values with indexes in two-item lists beginning at 2. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  indexed_from_2_iterator([\"a\", \"b\"]) -> [[2, \"a\"], [3, \"b\"]]\n  indexed_from_2_iterator([9]) -> [[2, 9]]",
    "initialCode": "def indexed_from_2_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_from_2_iterator(values):\n    iterator = iter(values)\n    result = []\n    index = 2\n    for value in iterator:\n        result.append([index, value])\n        index += 1\n    return result\n\nprint(indexed_from_2_iterator([\"a\", \"b\"]))  # Expected: [[2, \"a\"], [3, \"b\"]]\nprint(indexed_from_2_iterator([9]))  # Expected: [[2, 9]]\n\n# Example 2: nested helper approach\ndef solve_problem_6054(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        index = 2\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_6054([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6054Solution:\n    @staticmethod\n    def indexed_from_2_iterator(values):\n        iterator = iter(values)\n        result = []\n        index = 2\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n\nprint(Problem6054Solution.indexed_from_2_iterator([9]))\n\n# Example 4: assigned result approach\nresult = indexed_from_2_iterator([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(indexed_from_2_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6055,
    "title": "Problem 6055",
    "description": "Write a Python function called `indexed_from_3_iterator` that must consume an iterator and pair values with indexes in two-item lists beginning at 3. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  indexed_from_3_iterator([\"a\", \"b\"]) -> [[3, \"a\"], [4, \"b\"]]\n  indexed_from_3_iterator([9]) -> [[3, 9]]",
    "initialCode": "def indexed_from_3_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_from_3_iterator(values):\n    iterator = iter(values)\n    result = []\n    index = 3\n    for value in iterator:\n        result.append([index, value])\n        index += 1\n    return result\n\nprint(indexed_from_3_iterator([\"a\", \"b\"]))  # Expected: [[3, \"a\"], [4, \"b\"]]\nprint(indexed_from_3_iterator([9]))  # Expected: [[3, 9]]\n\n# Example 2: nested helper approach\ndef solve_problem_6055(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        index = 3\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_6055([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6055Solution:\n    @staticmethod\n    def indexed_from_3_iterator(values):\n        iterator = iter(values)\n        result = []\n        index = 3\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n\nprint(Problem6055Solution.indexed_from_3_iterator([9]))\n\n# Example 4: assigned result approach\nresult = indexed_from_3_iterator([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(indexed_from_3_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6056,
    "title": "Problem 6056",
    "description": "Write a Python function called `indexed_from_4_iterator` that must consume an iterator and pair values with indexes in two-item lists beginning at 4. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  indexed_from_4_iterator([\"a\", \"b\"]) -> [[4, \"a\"], [5, \"b\"]]\n  indexed_from_4_iterator([9]) -> [[4, 9]]",
    "initialCode": "def indexed_from_4_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_from_4_iterator(values):\n    iterator = iter(values)\n    result = []\n    index = 4\n    for value in iterator:\n        result.append([index, value])\n        index += 1\n    return result\n\nprint(indexed_from_4_iterator([\"a\", \"b\"]))  # Expected: [[4, \"a\"], [5, \"b\"]]\nprint(indexed_from_4_iterator([9]))  # Expected: [[4, 9]]\n\n# Example 2: nested helper approach\ndef solve_problem_6056(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        index = 4\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_6056([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6056Solution:\n    @staticmethod\n    def indexed_from_4_iterator(values):\n        iterator = iter(values)\n        result = []\n        index = 4\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n\nprint(Problem6056Solution.indexed_from_4_iterator([9]))\n\n# Example 4: assigned result approach\nresult = indexed_from_4_iterator([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(indexed_from_4_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  },
  {
    "id": 6057,
    "title": "Problem 6057",
    "description": "Write a Python function called `indexed_from_5_iterator` that must consume an iterator and pair values with indexes in two-item lists beginning at 5. Practice iterator syntax.\nDifficulty: Easy.\nExamples:\n  indexed_from_5_iterator([\"a\", \"b\"]) -> [[5, \"a\"], [6, \"b\"]]\n  indexed_from_5_iterator([9]) -> [[5, 9]]",
    "initialCode": "def indexed_from_5_iterator(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_from_5_iterator(values):\n    iterator = iter(values)\n    result = []\n    index = 5\n    for value in iterator:\n        result.append([index, value])\n        index += 1\n    return result\n\nprint(indexed_from_5_iterator([\"a\", \"b\"]))  # Expected: [[5, \"a\"], [6, \"b\"]]\nprint(indexed_from_5_iterator([9]))  # Expected: [[5, 9]]\n\n# Example 2: nested helper approach\ndef solve_problem_6057(values):\n    def calculate():\n        iterator = iter(values)\n        result = []\n        index = 5\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n    return calculate()\n\nprint(solve_problem_6057([\"a\", \"b\"]))\n\n# Example 3: static method approach\nclass Problem6057Solution:\n    @staticmethod\n    def indexed_from_5_iterator(values):\n        iterator = iter(values)\n        result = []\n        index = 5\n        for value in iterator:\n            result.append([index, value])\n            index += 1\n        return result\n\nprint(Problem6057Solution.indexed_from_5_iterator([9]))\n\n# Example 4: assigned result approach\nresult = indexed_from_5_iterator([\"a\", \"b\"])\nprint(result)\n\n# Example 5: direct call\nprint(indexed_from_5_iterator([]))",
    "hint": "Focus on creating the iterator, consuming values in order, and handling exhaustion safely. Use the required iterator structure instead of hard-coding an example.",
    "breakdown": "1. Identify each parameter and the required return type.\n2. Build the iterator structure named in the task.\n3. Trace the first example one operation at a time.\n4. Check the empty or boundary input in the hidden cases.\n5. Return the completed value without copying an expected output.",
    "category": "Iterator Easy"
  }
];
