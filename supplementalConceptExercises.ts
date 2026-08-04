import type { Exercise } from './types';

export const SUPPLEMENTAL_CONCEPT_EXERCISES: Exercise[] = [
  {
    "id": 7108,
    "title": "Problem 7108",
    "description": "Write a Python function called `sort_numbers_ascending_1` that must return numbers in ascending order followed by marker 1. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_1([3, 1, 2]) -> [1, 2, 3, 1]\n  sort_numbers_ascending_1([-1, 4, 0]) -> [-1, 0, 4, 1]",
    "initialCode": "def sort_numbers_ascending_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_1(values):\n    return sorted(values) + [1]\n\nprint(sort_numbers_ascending_1([3, 1, 2]))  # Expected: [1, 2, 3, 1]\nprint(sort_numbers_ascending_1([-1, 4, 0]))  # Expected: [-1, 0, 4, 1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7108(values):\n    return sort_numbers_ascending_1(values)\n\n# Example 3: static method approach\nclass Problem7108Solution:\n    @staticmethod\n    def sort_numbers_ascending_1(values):\n        return sorted(values) + [1]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_1([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7109,
    "title": "Problem 7109",
    "description": "Write a Python function called `sort_numbers_ascending_2` that must return numbers in ascending order followed by marker 2. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_2([3, 1, 2]) -> [1, 2, 3, 2]\n  sort_numbers_ascending_2([-1, 4, 0]) -> [-1, 0, 4, 2]",
    "initialCode": "def sort_numbers_ascending_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_2(values):\n    return sorted(values) + [2]\n\nprint(sort_numbers_ascending_2([3, 1, 2]))  # Expected: [1, 2, 3, 2]\nprint(sort_numbers_ascending_2([-1, 4, 0]))  # Expected: [-1, 0, 4, 2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7109(values):\n    return sort_numbers_ascending_2(values)\n\n# Example 3: static method approach\nclass Problem7109Solution:\n    @staticmethod\n    def sort_numbers_ascending_2(values):\n        return sorted(values) + [2]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_2([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7110,
    "title": "Problem 7110",
    "description": "Write a Python function called `sort_numbers_ascending_3` that must return numbers in ascending order followed by marker 3. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_3([3, 1, 2]) -> [1, 2, 3, 3]\n  sort_numbers_ascending_3([-1, 4, 0]) -> [-1, 0, 4, 3]",
    "initialCode": "def sort_numbers_ascending_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_3(values):\n    return sorted(values) + [3]\n\nprint(sort_numbers_ascending_3([3, 1, 2]))  # Expected: [1, 2, 3, 3]\nprint(sort_numbers_ascending_3([-1, 4, 0]))  # Expected: [-1, 0, 4, 3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7110(values):\n    return sort_numbers_ascending_3(values)\n\n# Example 3: static method approach\nclass Problem7110Solution:\n    @staticmethod\n    def sort_numbers_ascending_3(values):\n        return sorted(values) + [3]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_3([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7111,
    "title": "Problem 7111",
    "description": "Write a Python function called `sort_numbers_ascending_4` that must return numbers in ascending order followed by marker 4. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_4([3, 1, 2]) -> [1, 2, 3, 4]\n  sort_numbers_ascending_4([-1, 4, 0]) -> [-1, 0, 4, 4]",
    "initialCode": "def sort_numbers_ascending_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_4(values):\n    return sorted(values) + [4]\n\nprint(sort_numbers_ascending_4([3, 1, 2]))  # Expected: [1, 2, 3, 4]\nprint(sort_numbers_ascending_4([-1, 4, 0]))  # Expected: [-1, 0, 4, 4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7111(values):\n    return sort_numbers_ascending_4(values)\n\n# Example 3: static method approach\nclass Problem7111Solution:\n    @staticmethod\n    def sort_numbers_ascending_4(values):\n        return sorted(values) + [4]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_4([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7112,
    "title": "Problem 7112",
    "description": "Write a Python function called `sort_numbers_ascending_5` that must return numbers in ascending order followed by marker 5. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_5([3, 1, 2]) -> [1, 2, 3, 5]\n  sort_numbers_ascending_5([-1, 4, 0]) -> [-1, 0, 4, 5]",
    "initialCode": "def sort_numbers_ascending_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_5(values):\n    return sorted(values) + [5]\n\nprint(sort_numbers_ascending_5([3, 1, 2]))  # Expected: [1, 2, 3, 5]\nprint(sort_numbers_ascending_5([-1, 4, 0]))  # Expected: [-1, 0, 4, 5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7112(values):\n    return sort_numbers_ascending_5(values)\n\n# Example 3: static method approach\nclass Problem7112Solution:\n    @staticmethod\n    def sort_numbers_ascending_5(values):\n        return sorted(values) + [5]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_5([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7113,
    "title": "Problem 7113",
    "description": "Write a Python function called `sort_numbers_ascending_6` that must return numbers in ascending order followed by marker 6. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_6([3, 1, 2]) -> [1, 2, 3, 6]\n  sort_numbers_ascending_6([-1, 4, 0]) -> [-1, 0, 4, 6]",
    "initialCode": "def sort_numbers_ascending_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_6(values):\n    return sorted(values) + [6]\n\nprint(sort_numbers_ascending_6([3, 1, 2]))  # Expected: [1, 2, 3, 6]\nprint(sort_numbers_ascending_6([-1, 4, 0]))  # Expected: [-1, 0, 4, 6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7113(values):\n    return sort_numbers_ascending_6(values)\n\n# Example 3: static method approach\nclass Problem7113Solution:\n    @staticmethod\n    def sort_numbers_ascending_6(values):\n        return sorted(values) + [6]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_6([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7114,
    "title": "Problem 7114",
    "description": "Write a Python function called `sort_numbers_ascending_7` that must return numbers in ascending order followed by marker 7. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_7([3, 1, 2]) -> [1, 2, 3, 7]\n  sort_numbers_ascending_7([-1, 4, 0]) -> [-1, 0, 4, 7]",
    "initialCode": "def sort_numbers_ascending_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_7(values):\n    return sorted(values) + [7]\n\nprint(sort_numbers_ascending_7([3, 1, 2]))  # Expected: [1, 2, 3, 7]\nprint(sort_numbers_ascending_7([-1, 4, 0]))  # Expected: [-1, 0, 4, 7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7114(values):\n    return sort_numbers_ascending_7(values)\n\n# Example 3: static method approach\nclass Problem7114Solution:\n    @staticmethod\n    def sort_numbers_ascending_7(values):\n        return sorted(values) + [7]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_7([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7115,
    "title": "Problem 7115",
    "description": "Write a Python function called `sort_numbers_ascending_8` that must return numbers in ascending order followed by marker 8. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_8([3, 1, 2]) -> [1, 2, 3, 8]\n  sort_numbers_ascending_8([-1, 4, 0]) -> [-1, 0, 4, 8]",
    "initialCode": "def sort_numbers_ascending_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_8(values):\n    return sorted(values) + [8]\n\nprint(sort_numbers_ascending_8([3, 1, 2]))  # Expected: [1, 2, 3, 8]\nprint(sort_numbers_ascending_8([-1, 4, 0]))  # Expected: [-1, 0, 4, 8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7115(values):\n    return sort_numbers_ascending_8(values)\n\n# Example 3: static method approach\nclass Problem7115Solution:\n    @staticmethod\n    def sort_numbers_ascending_8(values):\n        return sorted(values) + [8]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_8([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7116,
    "title": "Problem 7116",
    "description": "Write a Python function called `sort_numbers_ascending_9` that must return numbers in ascending order followed by marker 9. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_9([3, 1, 2]) -> [1, 2, 3, 9]\n  sort_numbers_ascending_9([-1, 4, 0]) -> [-1, 0, 4, 9]",
    "initialCode": "def sort_numbers_ascending_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_9(values):\n    return sorted(values) + [9]\n\nprint(sort_numbers_ascending_9([3, 1, 2]))  # Expected: [1, 2, 3, 9]\nprint(sort_numbers_ascending_9([-1, 4, 0]))  # Expected: [-1, 0, 4, 9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7116(values):\n    return sort_numbers_ascending_9(values)\n\n# Example 3: static method approach\nclass Problem7116Solution:\n    @staticmethod\n    def sort_numbers_ascending_9(values):\n        return sorted(values) + [9]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_9([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7117,
    "title": "Problem 7117",
    "description": "Write a Python function called `sort_numbers_ascending_10` that must return numbers in ascending order followed by marker 10. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_ascending_10([3, 1, 2]) -> [1, 2, 3, 10]\n  sort_numbers_ascending_10([-1, 4, 0]) -> [-1, 0, 4, 10]",
    "initialCode": "def sort_numbers_ascending_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_ascending_10(values):\n    return sorted(values) + [10]\n\nprint(sort_numbers_ascending_10([3, 1, 2]))  # Expected: [1, 2, 3, 10]\nprint(sort_numbers_ascending_10([-1, 4, 0]))  # Expected: [-1, 0, 4, 10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7117(values):\n    return sort_numbers_ascending_10(values)\n\n# Example 3: static method approach\nclass Problem7117Solution:\n    @staticmethod\n    def sort_numbers_ascending_10(values):\n        return sorted(values) + [10]\n\n# Example 4: assigned result approach\nresult = sort_numbers_ascending_10([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_ascending_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7118,
    "title": "Problem 7118",
    "description": "Write a Python function called `sort_numbers_descending_1` that must return marker 1 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_1([3, 1, 2]) -> [1, 3, 2, 1]\n  sort_numbers_descending_1([-1, 4, 0]) -> [1, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_1(values):\n    return [1] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_1([3, 1, 2]))  # Expected: [1, 3, 2, 1]\nprint(sort_numbers_descending_1([-1, 4, 0]))  # Expected: [1, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7118(values):\n    return sort_numbers_descending_1(values)\n\n# Example 3: static method approach\nclass Problem7118Solution:\n    @staticmethod\n    def sort_numbers_descending_1(values):\n        return [1] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_1([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7119,
    "title": "Problem 7119",
    "description": "Write a Python function called `sort_numbers_descending_2` that must return marker 2 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_2([3, 1, 2]) -> [2, 3, 2, 1]\n  sort_numbers_descending_2([-1, 4, 0]) -> [2, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_2(values):\n    return [2] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_2([3, 1, 2]))  # Expected: [2, 3, 2, 1]\nprint(sort_numbers_descending_2([-1, 4, 0]))  # Expected: [2, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7119(values):\n    return sort_numbers_descending_2(values)\n\n# Example 3: static method approach\nclass Problem7119Solution:\n    @staticmethod\n    def sort_numbers_descending_2(values):\n        return [2] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_2([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7120,
    "title": "Problem 7120",
    "description": "Write a Python function called `sort_numbers_descending_3` that must return marker 3 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_3([3, 1, 2]) -> [3, 3, 2, 1]\n  sort_numbers_descending_3([-1, 4, 0]) -> [3, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_3(values):\n    return [3] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_3([3, 1, 2]))  # Expected: [3, 3, 2, 1]\nprint(sort_numbers_descending_3([-1, 4, 0]))  # Expected: [3, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7120(values):\n    return sort_numbers_descending_3(values)\n\n# Example 3: static method approach\nclass Problem7120Solution:\n    @staticmethod\n    def sort_numbers_descending_3(values):\n        return [3] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_3([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7121,
    "title": "Problem 7121",
    "description": "Write a Python function called `sort_numbers_descending_4` that must return marker 4 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_4([3, 1, 2]) -> [4, 3, 2, 1]\n  sort_numbers_descending_4([-1, 4, 0]) -> [4, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_4(values):\n    return [4] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_4([3, 1, 2]))  # Expected: [4, 3, 2, 1]\nprint(sort_numbers_descending_4([-1, 4, 0]))  # Expected: [4, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7121(values):\n    return sort_numbers_descending_4(values)\n\n# Example 3: static method approach\nclass Problem7121Solution:\n    @staticmethod\n    def sort_numbers_descending_4(values):\n        return [4] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_4([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7122,
    "title": "Problem 7122",
    "description": "Write a Python function called `sort_numbers_descending_5` that must return marker 5 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_5([3, 1, 2]) -> [5, 3, 2, 1]\n  sort_numbers_descending_5([-1, 4, 0]) -> [5, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_5(values):\n    return [5] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_5([3, 1, 2]))  # Expected: [5, 3, 2, 1]\nprint(sort_numbers_descending_5([-1, 4, 0]))  # Expected: [5, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7122(values):\n    return sort_numbers_descending_5(values)\n\n# Example 3: static method approach\nclass Problem7122Solution:\n    @staticmethod\n    def sort_numbers_descending_5(values):\n        return [5] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_5([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7123,
    "title": "Problem 7123",
    "description": "Write a Python function called `sort_numbers_descending_6` that must return marker 6 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_6([3, 1, 2]) -> [6, 3, 2, 1]\n  sort_numbers_descending_6([-1, 4, 0]) -> [6, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_6(values):\n    return [6] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_6([3, 1, 2]))  # Expected: [6, 3, 2, 1]\nprint(sort_numbers_descending_6([-1, 4, 0]))  # Expected: [6, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7123(values):\n    return sort_numbers_descending_6(values)\n\n# Example 3: static method approach\nclass Problem7123Solution:\n    @staticmethod\n    def sort_numbers_descending_6(values):\n        return [6] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_6([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7124,
    "title": "Problem 7124",
    "description": "Write a Python function called `sort_numbers_descending_7` that must return marker 7 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_7([3, 1, 2]) -> [7, 3, 2, 1]\n  sort_numbers_descending_7([-1, 4, 0]) -> [7, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_7(values):\n    return [7] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_7([3, 1, 2]))  # Expected: [7, 3, 2, 1]\nprint(sort_numbers_descending_7([-1, 4, 0]))  # Expected: [7, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7124(values):\n    return sort_numbers_descending_7(values)\n\n# Example 3: static method approach\nclass Problem7124Solution:\n    @staticmethod\n    def sort_numbers_descending_7(values):\n        return [7] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_7([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7125,
    "title": "Problem 7125",
    "description": "Write a Python function called `sort_numbers_descending_8` that must return marker 8 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_8([3, 1, 2]) -> [8, 3, 2, 1]\n  sort_numbers_descending_8([-1, 4, 0]) -> [8, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_8(values):\n    return [8] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_8([3, 1, 2]))  # Expected: [8, 3, 2, 1]\nprint(sort_numbers_descending_8([-1, 4, 0]))  # Expected: [8, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7125(values):\n    return sort_numbers_descending_8(values)\n\n# Example 3: static method approach\nclass Problem7125Solution:\n    @staticmethod\n    def sort_numbers_descending_8(values):\n        return [8] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_8([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7126,
    "title": "Problem 7126",
    "description": "Write a Python function called `sort_numbers_descending_9` that must return marker 9 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_9([3, 1, 2]) -> [9, 3, 2, 1]\n  sort_numbers_descending_9([-1, 4, 0]) -> [9, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_9(values):\n    return [9] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_9([3, 1, 2]))  # Expected: [9, 3, 2, 1]\nprint(sort_numbers_descending_9([-1, 4, 0]))  # Expected: [9, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7126(values):\n    return sort_numbers_descending_9(values)\n\n# Example 3: static method approach\nclass Problem7126Solution:\n    @staticmethod\n    def sort_numbers_descending_9(values):\n        return [9] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_9([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7127,
    "title": "Problem 7127",
    "description": "Write a Python function called `sort_numbers_descending_10` that must return marker 10 followed by numbers in descending order. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_numbers_descending_10([3, 1, 2]) -> [10, 3, 2, 1]\n  sort_numbers_descending_10([-1, 4, 0]) -> [10, 4, 0, -1]",
    "initialCode": "def sort_numbers_descending_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_numbers_descending_10(values):\n    return [10] + sorted(values, reverse=True)\n\nprint(sort_numbers_descending_10([3, 1, 2]))  # Expected: [10, 3, 2, 1]\nprint(sort_numbers_descending_10([-1, 4, 0]))  # Expected: [10, 4, 0, -1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7127(values):\n    return sort_numbers_descending_10(values)\n\n# Example 3: static method approach\nclass Problem7127Solution:\n    @staticmethod\n    def sort_numbers_descending_10(values):\n        return [10] + sorted(values, reverse=True)\n\n# Example 4: assigned result approach\nresult = sort_numbers_descending_10([3, 1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_numbers_descending_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7128,
    "title": "Problem 7128",
    "description": "Write a Python function called `sort_words_by_length_1` that must sort words by length then alphabetically and append marker_1. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_1([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_1\"]\n  sort_words_by_length_1([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_1\"]",
    "initialCode": "def sort_words_by_length_1(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_1(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_1\"]\n\nprint(sort_words_by_length_1([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_1\"]\nprint(sort_words_by_length_1([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_1\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7128(words):\n    return sort_words_by_length_1(words)\n\n# Example 3: static method approach\nclass Problem7128Solution:\n    @staticmethod\n    def sort_words_by_length_1(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_1\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_1([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7129,
    "title": "Problem 7129",
    "description": "Write a Python function called `sort_words_by_length_2` that must sort words by length then alphabetically and append marker_2. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_2([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_2\"]\n  sort_words_by_length_2([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_2\"]",
    "initialCode": "def sort_words_by_length_2(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_2(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_2\"]\n\nprint(sort_words_by_length_2([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_2\"]\nprint(sort_words_by_length_2([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_2\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7129(words):\n    return sort_words_by_length_2(words)\n\n# Example 3: static method approach\nclass Problem7129Solution:\n    @staticmethod\n    def sort_words_by_length_2(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_2\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_2([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7130,
    "title": "Problem 7130",
    "description": "Write a Python function called `sort_words_by_length_3` that must sort words by length then alphabetically and append marker_3. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_3([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_3\"]\n  sort_words_by_length_3([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_3\"]",
    "initialCode": "def sort_words_by_length_3(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_3(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_3\"]\n\nprint(sort_words_by_length_3([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_3\"]\nprint(sort_words_by_length_3([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_3\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7130(words):\n    return sort_words_by_length_3(words)\n\n# Example 3: static method approach\nclass Problem7130Solution:\n    @staticmethod\n    def sort_words_by_length_3(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_3\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_3([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7131,
    "title": "Problem 7131",
    "description": "Write a Python function called `sort_words_by_length_4` that must sort words by length then alphabetically and append marker_4. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_4([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_4\"]\n  sort_words_by_length_4([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_4\"]",
    "initialCode": "def sort_words_by_length_4(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_4(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_4\"]\n\nprint(sort_words_by_length_4([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_4\"]\nprint(sort_words_by_length_4([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_4\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7131(words):\n    return sort_words_by_length_4(words)\n\n# Example 3: static method approach\nclass Problem7131Solution:\n    @staticmethod\n    def sort_words_by_length_4(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_4\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_4([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7132,
    "title": "Problem 7132",
    "description": "Write a Python function called `sort_words_by_length_5` that must sort words by length then alphabetically and append marker_5. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_5([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_5\"]\n  sort_words_by_length_5([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_5\"]",
    "initialCode": "def sort_words_by_length_5(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_5(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_5\"]\n\nprint(sort_words_by_length_5([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_5\"]\nprint(sort_words_by_length_5([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_5\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7132(words):\n    return sort_words_by_length_5(words)\n\n# Example 3: static method approach\nclass Problem7132Solution:\n    @staticmethod\n    def sort_words_by_length_5(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_5\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_5([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7133,
    "title": "Problem 7133",
    "description": "Write a Python function called `sort_words_by_length_6` that must sort words by length then alphabetically and append marker_6. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_6([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_6\"]\n  sort_words_by_length_6([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_6\"]",
    "initialCode": "def sort_words_by_length_6(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_6(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_6\"]\n\nprint(sort_words_by_length_6([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_6\"]\nprint(sort_words_by_length_6([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_6\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7133(words):\n    return sort_words_by_length_6(words)\n\n# Example 3: static method approach\nclass Problem7133Solution:\n    @staticmethod\n    def sort_words_by_length_6(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_6\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_6([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7134,
    "title": "Problem 7134",
    "description": "Write a Python function called `sort_words_by_length_7` that must sort words by length then alphabetically and append marker_7. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_7([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_7\"]\n  sort_words_by_length_7([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_7\"]",
    "initialCode": "def sort_words_by_length_7(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_7(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_7\"]\n\nprint(sort_words_by_length_7([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_7\"]\nprint(sort_words_by_length_7([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_7\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7134(words):\n    return sort_words_by_length_7(words)\n\n# Example 3: static method approach\nclass Problem7134Solution:\n    @staticmethod\n    def sort_words_by_length_7(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_7\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_7([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7135,
    "title": "Problem 7135",
    "description": "Write a Python function called `sort_words_by_length_8` that must sort words by length then alphabetically and append marker_8. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_8([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_8\"]\n  sort_words_by_length_8([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_8\"]",
    "initialCode": "def sort_words_by_length_8(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_8(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_8\"]\n\nprint(sort_words_by_length_8([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_8\"]\nprint(sort_words_by_length_8([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_8\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7135(words):\n    return sort_words_by_length_8(words)\n\n# Example 3: static method approach\nclass Problem7135Solution:\n    @staticmethod\n    def sort_words_by_length_8(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_8\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_8([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7136,
    "title": "Problem 7136",
    "description": "Write a Python function called `sort_words_by_length_9` that must sort words by length then alphabetically and append marker_9. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_9([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_9\"]\n  sort_words_by_length_9([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_9\"]",
    "initialCode": "def sort_words_by_length_9(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_9(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_9\"]\n\nprint(sort_words_by_length_9([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_9\"]\nprint(sort_words_by_length_9([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_9\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7136(words):\n    return sort_words_by_length_9(words)\n\n# Example 3: static method approach\nclass Problem7136Solution:\n    @staticmethod\n    def sort_words_by_length_9(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_9\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_9([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7137,
    "title": "Problem 7137",
    "description": "Write a Python function called `sort_words_by_length_10` that must sort words by length then alphabetically and append marker_10. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_by_length_10([\"pear\", \"a\", \"fig\"]) -> [\"a\", \"fig\", \"pear\", \"marker_10\"]\n  sort_words_by_length_10([\"bb\", \"aa\", \"c\"]) -> [\"c\", \"aa\", \"bb\", \"marker_10\"]",
    "initialCode": "def sort_words_by_length_10(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_by_length_10(words):\n    return sorted(words, key=lambda word: (len(word), word)) + [\"marker_10\"]\n\nprint(sort_words_by_length_10([\"pear\", \"a\", \"fig\"]))  # Expected: [\"a\", \"fig\", \"pear\", \"marker_10\"]\nprint(sort_words_by_length_10([\"bb\", \"aa\", \"c\"]))  # Expected: [\"c\", \"aa\", \"bb\", \"marker_10\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7137(words):\n    return sort_words_by_length_10(words)\n\n# Example 3: static method approach\nclass Problem7137Solution:\n    @staticmethod\n    def sort_words_by_length_10(words):\n        return sorted(words, key=lambda word: (len(word), word)) + [\"marker_10\"]\n\n# Example 4: assigned result approach\nresult = sort_words_by_length_10([\"pear\", \"a\", \"fig\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_by_length_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7138,
    "title": "Problem 7138",
    "description": "Write a Python function called `sort_words_casefold_1` that must sort words without case sensitivity and append marker_1. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_1([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_1\"]\n  sort_words_casefold_1([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_1\"]",
    "initialCode": "def sort_words_casefold_1(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_1(words):\n    return sorted(words, key=str.casefold) + [\"marker_1\"]\n\nprint(sort_words_casefold_1([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_1\"]\nprint(sort_words_casefold_1([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_1\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7138(words):\n    return sort_words_casefold_1(words)\n\n# Example 3: static method approach\nclass Problem7138Solution:\n    @staticmethod\n    def sort_words_casefold_1(words):\n        return sorted(words, key=str.casefold) + [\"marker_1\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_1([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7139,
    "title": "Problem 7139",
    "description": "Write a Python function called `sort_words_casefold_2` that must sort words without case sensitivity and append marker_2. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_2([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_2\"]\n  sort_words_casefold_2([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_2\"]",
    "initialCode": "def sort_words_casefold_2(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_2(words):\n    return sorted(words, key=str.casefold) + [\"marker_2\"]\n\nprint(sort_words_casefold_2([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_2\"]\nprint(sort_words_casefold_2([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_2\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7139(words):\n    return sort_words_casefold_2(words)\n\n# Example 3: static method approach\nclass Problem7139Solution:\n    @staticmethod\n    def sort_words_casefold_2(words):\n        return sorted(words, key=str.casefold) + [\"marker_2\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_2([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7140,
    "title": "Problem 7140",
    "description": "Write a Python function called `sort_words_casefold_3` that must sort words without case sensitivity and append marker_3. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_3([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_3\"]\n  sort_words_casefold_3([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_3\"]",
    "initialCode": "def sort_words_casefold_3(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_3(words):\n    return sorted(words, key=str.casefold) + [\"marker_3\"]\n\nprint(sort_words_casefold_3([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_3\"]\nprint(sort_words_casefold_3([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_3\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7140(words):\n    return sort_words_casefold_3(words)\n\n# Example 3: static method approach\nclass Problem7140Solution:\n    @staticmethod\n    def sort_words_casefold_3(words):\n        return sorted(words, key=str.casefold) + [\"marker_3\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_3([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7141,
    "title": "Problem 7141",
    "description": "Write a Python function called `sort_words_casefold_4` that must sort words without case sensitivity and append marker_4. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_4([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_4\"]\n  sort_words_casefold_4([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_4\"]",
    "initialCode": "def sort_words_casefold_4(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_4(words):\n    return sorted(words, key=str.casefold) + [\"marker_4\"]\n\nprint(sort_words_casefold_4([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_4\"]\nprint(sort_words_casefold_4([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_4\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7141(words):\n    return sort_words_casefold_4(words)\n\n# Example 3: static method approach\nclass Problem7141Solution:\n    @staticmethod\n    def sort_words_casefold_4(words):\n        return sorted(words, key=str.casefold) + [\"marker_4\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_4([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7142,
    "title": "Problem 7142",
    "description": "Write a Python function called `sort_words_casefold_5` that must sort words without case sensitivity and append marker_5. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_5([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_5\"]\n  sort_words_casefold_5([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_5\"]",
    "initialCode": "def sort_words_casefold_5(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_5(words):\n    return sorted(words, key=str.casefold) + [\"marker_5\"]\n\nprint(sort_words_casefold_5([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_5\"]\nprint(sort_words_casefold_5([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_5\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7142(words):\n    return sort_words_casefold_5(words)\n\n# Example 3: static method approach\nclass Problem7142Solution:\n    @staticmethod\n    def sort_words_casefold_5(words):\n        return sorted(words, key=str.casefold) + [\"marker_5\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_5([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7143,
    "title": "Problem 7143",
    "description": "Write a Python function called `sort_words_casefold_6` that must sort words without case sensitivity and append marker_6. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_6([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_6\"]\n  sort_words_casefold_6([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_6\"]",
    "initialCode": "def sort_words_casefold_6(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_6(words):\n    return sorted(words, key=str.casefold) + [\"marker_6\"]\n\nprint(sort_words_casefold_6([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_6\"]\nprint(sort_words_casefold_6([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_6\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7143(words):\n    return sort_words_casefold_6(words)\n\n# Example 3: static method approach\nclass Problem7143Solution:\n    @staticmethod\n    def sort_words_casefold_6(words):\n        return sorted(words, key=str.casefold) + [\"marker_6\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_6([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7144,
    "title": "Problem 7144",
    "description": "Write a Python function called `sort_words_casefold_7` that must sort words without case sensitivity and append marker_7. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_7([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_7\"]\n  sort_words_casefold_7([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_7\"]",
    "initialCode": "def sort_words_casefold_7(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_7(words):\n    return sorted(words, key=str.casefold) + [\"marker_7\"]\n\nprint(sort_words_casefold_7([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_7\"]\nprint(sort_words_casefold_7([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_7\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7144(words):\n    return sort_words_casefold_7(words)\n\n# Example 3: static method approach\nclass Problem7144Solution:\n    @staticmethod\n    def sort_words_casefold_7(words):\n        return sorted(words, key=str.casefold) + [\"marker_7\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_7([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7145,
    "title": "Problem 7145",
    "description": "Write a Python function called `sort_words_casefold_8` that must sort words without case sensitivity and append marker_8. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_8([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_8\"]\n  sort_words_casefold_8([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_8\"]",
    "initialCode": "def sort_words_casefold_8(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_8(words):\n    return sorted(words, key=str.casefold) + [\"marker_8\"]\n\nprint(sort_words_casefold_8([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_8\"]\nprint(sort_words_casefold_8([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_8\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7145(words):\n    return sort_words_casefold_8(words)\n\n# Example 3: static method approach\nclass Problem7145Solution:\n    @staticmethod\n    def sort_words_casefold_8(words):\n        return sorted(words, key=str.casefold) + [\"marker_8\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_8([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7146,
    "title": "Problem 7146",
    "description": "Write a Python function called `sort_words_casefold_9` that must sort words without case sensitivity and append marker_9. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_9([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_9\"]\n  sort_words_casefold_9([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_9\"]",
    "initialCode": "def sort_words_casefold_9(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_9(words):\n    return sorted(words, key=str.casefold) + [\"marker_9\"]\n\nprint(sort_words_casefold_9([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_9\"]\nprint(sort_words_casefold_9([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_9\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7146(words):\n    return sort_words_casefold_9(words)\n\n# Example 3: static method approach\nclass Problem7146Solution:\n    @staticmethod\n    def sort_words_casefold_9(words):\n        return sorted(words, key=str.casefold) + [\"marker_9\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_9([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7147,
    "title": "Problem 7147",
    "description": "Write a Python function called `sort_words_casefold_10` that must sort words without case sensitivity and append marker_10. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_words_casefold_10([\"Zoo\", \"apple\", \"Banana\"]) -> [\"apple\", \"Banana\", \"Zoo\", \"marker_10\"]\n  sort_words_casefold_10([\"b\", \"A\"]) -> [\"A\", \"b\", \"marker_10\"]",
    "initialCode": "def sort_words_casefold_10(words):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_words_casefold_10(words):\n    return sorted(words, key=str.casefold) + [\"marker_10\"]\n\nprint(sort_words_casefold_10([\"Zoo\", \"apple\", \"Banana\"]))  # Expected: [\"apple\", \"Banana\", \"Zoo\", \"marker_10\"]\nprint(sort_words_casefold_10([\"b\", \"A\"]))  # Expected: [\"A\", \"b\", \"marker_10\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7147(words):\n    return sort_words_casefold_10(words)\n\n# Example 3: static method approach\nclass Problem7147Solution:\n    @staticmethod\n    def sort_words_casefold_10(words):\n        return sorted(words, key=str.casefold) + [\"marker_10\"]\n\n# Example 4: assigned result approach\nresult = sort_words_casefold_10([\"Zoo\", \"apple\", \"Banana\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_words_casefold_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7148,
    "title": "Problem 7148",
    "description": "Write a Python function called `sort_pairs_second_1` that must sort pairs by second item then first item and append marker pair 1. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_1([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 1]]\n  sort_pairs_second_1([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 1]]",
    "initialCode": "def sort_pairs_second_1(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_1(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 1]]\n\nprint(sort_pairs_second_1([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 1]]\nprint(sort_pairs_second_1([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7148(pairs):\n    return sort_pairs_second_1(pairs)\n\n# Example 3: static method approach\nclass Problem7148Solution:\n    @staticmethod\n    def sort_pairs_second_1(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 1]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_1([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7149,
    "title": "Problem 7149",
    "description": "Write a Python function called `sort_pairs_second_2` that must sort pairs by second item then first item and append marker pair 2. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_2([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 2]]\n  sort_pairs_second_2([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 2]]",
    "initialCode": "def sort_pairs_second_2(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_2(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 2]]\n\nprint(sort_pairs_second_2([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 2]]\nprint(sort_pairs_second_2([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 2]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7149(pairs):\n    return sort_pairs_second_2(pairs)\n\n# Example 3: static method approach\nclass Problem7149Solution:\n    @staticmethod\n    def sort_pairs_second_2(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 2]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_2([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7150,
    "title": "Problem 7150",
    "description": "Write a Python function called `sort_pairs_second_3` that must sort pairs by second item then first item and append marker pair 3. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_3([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 3]]\n  sort_pairs_second_3([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 3]]",
    "initialCode": "def sort_pairs_second_3(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_3(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 3]]\n\nprint(sort_pairs_second_3([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 3]]\nprint(sort_pairs_second_3([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 3]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7150(pairs):\n    return sort_pairs_second_3(pairs)\n\n# Example 3: static method approach\nclass Problem7150Solution:\n    @staticmethod\n    def sort_pairs_second_3(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 3]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_3([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7151,
    "title": "Problem 7151",
    "description": "Write a Python function called `sort_pairs_second_4` that must sort pairs by second item then first item and append marker pair 4. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_4([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 4]]\n  sort_pairs_second_4([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 4]]",
    "initialCode": "def sort_pairs_second_4(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_4(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 4]]\n\nprint(sort_pairs_second_4([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 4]]\nprint(sort_pairs_second_4([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 4]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7151(pairs):\n    return sort_pairs_second_4(pairs)\n\n# Example 3: static method approach\nclass Problem7151Solution:\n    @staticmethod\n    def sort_pairs_second_4(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 4]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_4([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7152,
    "title": "Problem 7152",
    "description": "Write a Python function called `sort_pairs_second_5` that must sort pairs by second item then first item and append marker pair 5. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_5([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 5]]\n  sort_pairs_second_5([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 5]]",
    "initialCode": "def sort_pairs_second_5(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_5(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 5]]\n\nprint(sort_pairs_second_5([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 5]]\nprint(sort_pairs_second_5([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 5]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7152(pairs):\n    return sort_pairs_second_5(pairs)\n\n# Example 3: static method approach\nclass Problem7152Solution:\n    @staticmethod\n    def sort_pairs_second_5(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 5]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_5([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7153,
    "title": "Problem 7153",
    "description": "Write a Python function called `sort_pairs_second_6` that must sort pairs by second item then first item and append marker pair 6. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_6([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 6]]\n  sort_pairs_second_6([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 6]]",
    "initialCode": "def sort_pairs_second_6(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_6(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 6]]\n\nprint(sort_pairs_second_6([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 6]]\nprint(sort_pairs_second_6([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 6]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7153(pairs):\n    return sort_pairs_second_6(pairs)\n\n# Example 3: static method approach\nclass Problem7153Solution:\n    @staticmethod\n    def sort_pairs_second_6(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 6]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_6([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7154,
    "title": "Problem 7154",
    "description": "Write a Python function called `sort_pairs_second_7` that must sort pairs by second item then first item and append marker pair 7. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_7([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 7]]\n  sort_pairs_second_7([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 7]]",
    "initialCode": "def sort_pairs_second_7(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_7(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 7]]\n\nprint(sort_pairs_second_7([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 7]]\nprint(sort_pairs_second_7([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 7]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7154(pairs):\n    return sort_pairs_second_7(pairs)\n\n# Example 3: static method approach\nclass Problem7154Solution:\n    @staticmethod\n    def sort_pairs_second_7(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 7]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_7([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7155,
    "title": "Problem 7155",
    "description": "Write a Python function called `sort_pairs_second_8` that must sort pairs by second item then first item and append marker pair 8. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_8([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 8]]\n  sort_pairs_second_8([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 8]]",
    "initialCode": "def sort_pairs_second_8(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_8(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 8]]\n\nprint(sort_pairs_second_8([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 8]]\nprint(sort_pairs_second_8([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 8]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7155(pairs):\n    return sort_pairs_second_8(pairs)\n\n# Example 3: static method approach\nclass Problem7155Solution:\n    @staticmethod\n    def sort_pairs_second_8(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 8]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_8([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7156,
    "title": "Problem 7156",
    "description": "Write a Python function called `sort_pairs_second_9` that must sort pairs by second item then first item and append marker pair 9. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_9([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 9]]\n  sort_pairs_second_9([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 9]]",
    "initialCode": "def sort_pairs_second_9(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_9(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 9]]\n\nprint(sort_pairs_second_9([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 9]]\nprint(sort_pairs_second_9([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 9]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7156(pairs):\n    return sort_pairs_second_9(pairs)\n\n# Example 3: static method approach\nclass Problem7156Solution:\n    @staticmethod\n    def sort_pairs_second_9(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 9]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_9([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7157,
    "title": "Problem 7157",
    "description": "Write a Python function called `sort_pairs_second_10` that must sort pairs by second item then first item and append marker pair 10. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_pairs_second_10([[\"b\", 2], [\"a\", 1], [\"c\", 1]]) -> [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 10]]\n  sort_pairs_second_10([[\"x\", 0]]) -> [[\"x\", 0], [\"marker\", 10]]",
    "initialCode": "def sort_pairs_second_10(pairs):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_pairs_second_10(pairs):\n    return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 10]]\n\nprint(sort_pairs_second_10([[\"b\", 2], [\"a\", 1], [\"c\", 1]]))  # Expected: [[\"a\", 1], [\"c\", 1], [\"b\", 2], [\"marker\", 10]]\nprint(sort_pairs_second_10([[\"x\", 0]]))  # Expected: [[\"x\", 0], [\"marker\", 10]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7157(pairs):\n    return sort_pairs_second_10(pairs)\n\n# Example 3: static method approach\nclass Problem7157Solution:\n    @staticmethod\n    def sort_pairs_second_10(pairs):\n        return sorted(pairs, key=lambda pair: (pair[1], pair[0])) + [[\"marker\", 10]]\n\n# Example 4: assigned result approach\nresult = sort_pairs_second_10([[\"b\", 2], [\"a\", 1], [\"c\", 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_pairs_second_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7158,
    "title": "Problem 7158",
    "description": "Write a Python function called `sort_records_field_1` that must sort dictionaries by a named numeric field and append marker record 1. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_1([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 1}]\n  sort_records_field_1([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 1}]",
    "initialCode": "def sort_records_field_1(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_1(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 1}]\n\nprint(sort_records_field_1([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 1}]\nprint(sort_records_field_1([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 1}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7158(records, field):\n    return sort_records_field_1(records, field)\n\n# Example 3: static method approach\nclass Problem7158Solution:\n    @staticmethod\n    def sort_records_field_1(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 1}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_1([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_1([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7159,
    "title": "Problem 7159",
    "description": "Write a Python function called `sort_records_field_2` that must sort dictionaries by a named numeric field and append marker record 2. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_2([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 2}]\n  sort_records_field_2([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 2}]",
    "initialCode": "def sort_records_field_2(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_2(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 2}]\n\nprint(sort_records_field_2([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 2}]\nprint(sort_records_field_2([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 2}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7159(records, field):\n    return sort_records_field_2(records, field)\n\n# Example 3: static method approach\nclass Problem7159Solution:\n    @staticmethod\n    def sort_records_field_2(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 2}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_2([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_2([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7160,
    "title": "Problem 7160",
    "description": "Write a Python function called `sort_records_field_3` that must sort dictionaries by a named numeric field and append marker record 3. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_3([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 3}]\n  sort_records_field_3([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 3}]",
    "initialCode": "def sort_records_field_3(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_3(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 3}]\n\nprint(sort_records_field_3([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 3}]\nprint(sort_records_field_3([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 3}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7160(records, field):\n    return sort_records_field_3(records, field)\n\n# Example 3: static method approach\nclass Problem7160Solution:\n    @staticmethod\n    def sort_records_field_3(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 3}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_3([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_3([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7161,
    "title": "Problem 7161",
    "description": "Write a Python function called `sort_records_field_4` that must sort dictionaries by a named numeric field and append marker record 4. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_4([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 4}]\n  sort_records_field_4([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 4}]",
    "initialCode": "def sort_records_field_4(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_4(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 4}]\n\nprint(sort_records_field_4([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 4}]\nprint(sort_records_field_4([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 4}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7161(records, field):\n    return sort_records_field_4(records, field)\n\n# Example 3: static method approach\nclass Problem7161Solution:\n    @staticmethod\n    def sort_records_field_4(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 4}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_4([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_4([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7162,
    "title": "Problem 7162",
    "description": "Write a Python function called `sort_records_field_5` that must sort dictionaries by a named numeric field and append marker record 5. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_5([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 5}]\n  sort_records_field_5([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 5}]",
    "initialCode": "def sort_records_field_5(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_5(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 5}]\n\nprint(sort_records_field_5([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 5}]\nprint(sort_records_field_5([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 5}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7162(records, field):\n    return sort_records_field_5(records, field)\n\n# Example 3: static method approach\nclass Problem7162Solution:\n    @staticmethod\n    def sort_records_field_5(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 5}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_5([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_5([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7163,
    "title": "Problem 7163",
    "description": "Write a Python function called `sort_records_field_6` that must sort dictionaries by a named numeric field and append marker record 6. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_6([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 6}]\n  sort_records_field_6([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 6}]",
    "initialCode": "def sort_records_field_6(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_6(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 6}]\n\nprint(sort_records_field_6([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 6}]\nprint(sort_records_field_6([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 6}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7163(records, field):\n    return sort_records_field_6(records, field)\n\n# Example 3: static method approach\nclass Problem7163Solution:\n    @staticmethod\n    def sort_records_field_6(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 6}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_6([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_6([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7164,
    "title": "Problem 7164",
    "description": "Write a Python function called `sort_records_field_7` that must sort dictionaries by a named numeric field and append marker record 7. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_7([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 7}]\n  sort_records_field_7([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 7}]",
    "initialCode": "def sort_records_field_7(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_7(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 7}]\n\nprint(sort_records_field_7([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 7}]\nprint(sort_records_field_7([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 7}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7164(records, field):\n    return sort_records_field_7(records, field)\n\n# Example 3: static method approach\nclass Problem7164Solution:\n    @staticmethod\n    def sort_records_field_7(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 7}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_7([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_7([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7165,
    "title": "Problem 7165",
    "description": "Write a Python function called `sort_records_field_8` that must sort dictionaries by a named numeric field and append marker record 8. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_8([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 8}]\n  sort_records_field_8([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 8}]",
    "initialCode": "def sort_records_field_8(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_8(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 8}]\n\nprint(sort_records_field_8([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 8}]\nprint(sort_records_field_8([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 8}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7165(records, field):\n    return sort_records_field_8(records, field)\n\n# Example 3: static method approach\nclass Problem7165Solution:\n    @staticmethod\n    def sort_records_field_8(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 8}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_8([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_8([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7166,
    "title": "Problem 7166",
    "description": "Write a Python function called `sort_records_field_9` that must sort dictionaries by a named numeric field and append marker record 9. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_9([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 9}]\n  sort_records_field_9([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 9}]",
    "initialCode": "def sort_records_field_9(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_9(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 9}]\n\nprint(sort_records_field_9([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 9}]\nprint(sort_records_field_9([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 9}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7166(records, field):\n    return sort_records_field_9(records, field)\n\n# Example 3: static method approach\nclass Problem7166Solution:\n    @staticmethod\n    def sort_records_field_9(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 9}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_9([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_9([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7167,
    "title": "Problem 7167",
    "description": "Write a Python function called `sort_records_field_10` that must sort dictionaries by a named numeric field and append marker record 10. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_records_field_10([{\"score\": 3}, {\"score\": 1}], \"score\") -> [{\"score\": 1}, {\"score\": 3}, {\"marker\": 10}]\n  sort_records_field_10([{\"age\": 4}], \"age\") -> [{\"age\": 4}, {\"marker\": 10}]",
    "initialCode": "def sort_records_field_10(records, field):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_records_field_10(records, field):\n    return sorted(records, key=lambda record: record[field]) + [{\"marker\": 10}]\n\nprint(sort_records_field_10([{\"score\": 3}, {\"score\": 1}], \"score\"))  # Expected: [{\"score\": 1}, {\"score\": 3}, {\"marker\": 10}]\nprint(sort_records_field_10([{\"age\": 4}], \"age\"))  # Expected: [{\"age\": 4}, {\"marker\": 10}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7167(records, field):\n    return sort_records_field_10(records, field)\n\n# Example 3: static method approach\nclass Problem7167Solution:\n    @staticmethod\n    def sort_records_field_10(records, field):\n        return sorted(records, key=lambda record: record[field]) + [{\"marker\": 10}]\n\n# Example 4: assigned result approach\nresult = sort_records_field_10([{\"score\": 3}, {\"score\": 1}], \"score\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_records_field_10([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7168,
    "title": "Problem 7168",
    "description": "Write a Python function called `sort_by_absolute_1` that must sort numbers by absolute value then numeric value and append 1. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_1([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 1]\n  sort_by_absolute_1([0, -5, 4]) -> [0, 4, -5, 1]",
    "initialCode": "def sort_by_absolute_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_1(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [1]\n\nprint(sort_by_absolute_1([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 1]\nprint(sort_by_absolute_1([0, -5, 4]))  # Expected: [0, 4, -5, 1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7168(values):\n    return sort_by_absolute_1(values)\n\n# Example 3: static method approach\nclass Problem7168Solution:\n    @staticmethod\n    def sort_by_absolute_1(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [1]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_1([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7169,
    "title": "Problem 7169",
    "description": "Write a Python function called `sort_by_absolute_2` that must sort numbers by absolute value then numeric value and append 2. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_2([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 2]\n  sort_by_absolute_2([0, -5, 4]) -> [0, 4, -5, 2]",
    "initialCode": "def sort_by_absolute_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_2(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [2]\n\nprint(sort_by_absolute_2([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 2]\nprint(sort_by_absolute_2([0, -5, 4]))  # Expected: [0, 4, -5, 2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7169(values):\n    return sort_by_absolute_2(values)\n\n# Example 3: static method approach\nclass Problem7169Solution:\n    @staticmethod\n    def sort_by_absolute_2(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [2]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_2([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7170,
    "title": "Problem 7170",
    "description": "Write a Python function called `sort_by_absolute_3` that must sort numbers by absolute value then numeric value and append 3. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_3([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 3]\n  sort_by_absolute_3([0, -5, 4]) -> [0, 4, -5, 3]",
    "initialCode": "def sort_by_absolute_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_3(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [3]\n\nprint(sort_by_absolute_3([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 3]\nprint(sort_by_absolute_3([0, -5, 4]))  # Expected: [0, 4, -5, 3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7170(values):\n    return sort_by_absolute_3(values)\n\n# Example 3: static method approach\nclass Problem7170Solution:\n    @staticmethod\n    def sort_by_absolute_3(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [3]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_3([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7171,
    "title": "Problem 7171",
    "description": "Write a Python function called `sort_by_absolute_4` that must sort numbers by absolute value then numeric value and append 4. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_4([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 4]\n  sort_by_absolute_4([0, -5, 4]) -> [0, 4, -5, 4]",
    "initialCode": "def sort_by_absolute_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_4(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [4]\n\nprint(sort_by_absolute_4([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 4]\nprint(sort_by_absolute_4([0, -5, 4]))  # Expected: [0, 4, -5, 4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7171(values):\n    return sort_by_absolute_4(values)\n\n# Example 3: static method approach\nclass Problem7171Solution:\n    @staticmethod\n    def sort_by_absolute_4(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [4]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_4([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7172,
    "title": "Problem 7172",
    "description": "Write a Python function called `sort_by_absolute_5` that must sort numbers by absolute value then numeric value and append 5. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_5([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 5]\n  sort_by_absolute_5([0, -5, 4]) -> [0, 4, -5, 5]",
    "initialCode": "def sort_by_absolute_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_5(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [5]\n\nprint(sort_by_absolute_5([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 5]\nprint(sort_by_absolute_5([0, -5, 4]))  # Expected: [0, 4, -5, 5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7172(values):\n    return sort_by_absolute_5(values)\n\n# Example 3: static method approach\nclass Problem7172Solution:\n    @staticmethod\n    def sort_by_absolute_5(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [5]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_5([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7173,
    "title": "Problem 7173",
    "description": "Write a Python function called `sort_by_absolute_6` that must sort numbers by absolute value then numeric value and append 6. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_6([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 6]\n  sort_by_absolute_6([0, -5, 4]) -> [0, 4, -5, 6]",
    "initialCode": "def sort_by_absolute_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_6(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [6]\n\nprint(sort_by_absolute_6([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 6]\nprint(sort_by_absolute_6([0, -5, 4]))  # Expected: [0, 4, -5, 6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7173(values):\n    return sort_by_absolute_6(values)\n\n# Example 3: static method approach\nclass Problem7173Solution:\n    @staticmethod\n    def sort_by_absolute_6(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [6]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_6([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7174,
    "title": "Problem 7174",
    "description": "Write a Python function called `sort_by_absolute_7` that must sort numbers by absolute value then numeric value and append 7. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_7([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 7]\n  sort_by_absolute_7([0, -5, 4]) -> [0, 4, -5, 7]",
    "initialCode": "def sort_by_absolute_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_7(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [7]\n\nprint(sort_by_absolute_7([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 7]\nprint(sort_by_absolute_7([0, -5, 4]))  # Expected: [0, 4, -5, 7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7174(values):\n    return sort_by_absolute_7(values)\n\n# Example 3: static method approach\nclass Problem7174Solution:\n    @staticmethod\n    def sort_by_absolute_7(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [7]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_7([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7175,
    "title": "Problem 7175",
    "description": "Write a Python function called `sort_by_absolute_8` that must sort numbers by absolute value then numeric value and append 8. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_8([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 8]\n  sort_by_absolute_8([0, -5, 4]) -> [0, 4, -5, 8]",
    "initialCode": "def sort_by_absolute_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_8(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [8]\n\nprint(sort_by_absolute_8([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 8]\nprint(sort_by_absolute_8([0, -5, 4]))  # Expected: [0, 4, -5, 8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7175(values):\n    return sort_by_absolute_8(values)\n\n# Example 3: static method approach\nclass Problem7175Solution:\n    @staticmethod\n    def sort_by_absolute_8(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [8]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_8([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7176,
    "title": "Problem 7176",
    "description": "Write a Python function called `sort_by_absolute_9` that must sort numbers by absolute value then numeric value and append 9. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_9([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 9]\n  sort_by_absolute_9([0, -5, 4]) -> [0, 4, -5, 9]",
    "initialCode": "def sort_by_absolute_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_9(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [9]\n\nprint(sort_by_absolute_9([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 9]\nprint(sort_by_absolute_9([0, -5, 4]))  # Expected: [0, 4, -5, 9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7176(values):\n    return sort_by_absolute_9(values)\n\n# Example 3: static method approach\nclass Problem7176Solution:\n    @staticmethod\n    def sort_by_absolute_9(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [9]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_9([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7177,
    "title": "Problem 7177",
    "description": "Write a Python function called `sort_by_absolute_10` that must sort numbers by absolute value then numeric value and append 10. Practice sorting key.\nDifficulty: Easy.\nExamples:\n  sort_by_absolute_10([-3, 1, -1, 2]) -> [-1, 1, 2, -3, 10]\n  sort_by_absolute_10([0, -5, 4]) -> [0, 4, -5, 10]",
    "initialCode": "def sort_by_absolute_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_absolute_10(values):\n    return sorted(values, key=lambda value: (abs(value), value)) + [10]\n\nprint(sort_by_absolute_10([-3, 1, -1, 2]))  # Expected: [-1, 1, 2, -3, 10]\nprint(sort_by_absolute_10([0, -5, 4]))  # Expected: [0, 4, -5, 10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7177(values):\n    return sort_by_absolute_10(values)\n\n# Example 3: static method approach\nclass Problem7177Solution:\n    @staticmethod\n    def sort_by_absolute_10(values):\n        return sorted(values, key=lambda value: (abs(value), value)) + [10]\n\n# Example 4: assigned result approach\nresult = sort_by_absolute_10([-3, 1, -1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_absolute_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Easy"
  },
  {
    "id": 7178,
    "title": "Problem 7178",
    "description": "Write a Python function called `sort_even_before_odd_1` that must sort even numbers before odd numbers with ascending values, then append 1. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_1([5, 2, 3, 4]) -> [2, 4, 3, 5, 1]\n  sort_even_before_odd_1([-1, -2, 0]) -> [-2, 0, -1, 1]",
    "initialCode": "def sort_even_before_odd_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_1(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [1]\n\nprint(sort_even_before_odd_1([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 1]\nprint(sort_even_before_odd_1([-1, -2, 0]))  # Expected: [-2, 0, -1, 1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7178(values):\n    return sort_even_before_odd_1(values)\n\n# Example 3: static method approach\nclass Problem7178Solution:\n    @staticmethod\n    def sort_even_before_odd_1(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [1]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_1([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7179,
    "title": "Problem 7179",
    "description": "Write a Python function called `sort_even_before_odd_2` that must sort even numbers before odd numbers with ascending values, then append 2. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_2([5, 2, 3, 4]) -> [2, 4, 3, 5, 2]\n  sort_even_before_odd_2([-1, -2, 0]) -> [-2, 0, -1, 2]",
    "initialCode": "def sort_even_before_odd_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_2(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [2]\n\nprint(sort_even_before_odd_2([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 2]\nprint(sort_even_before_odd_2([-1, -2, 0]))  # Expected: [-2, 0, -1, 2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7179(values):\n    return sort_even_before_odd_2(values)\n\n# Example 3: static method approach\nclass Problem7179Solution:\n    @staticmethod\n    def sort_even_before_odd_2(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [2]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_2([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7180,
    "title": "Problem 7180",
    "description": "Write a Python function called `sort_even_before_odd_3` that must sort even numbers before odd numbers with ascending values, then append 3. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_3([5, 2, 3, 4]) -> [2, 4, 3, 5, 3]\n  sort_even_before_odd_3([-1, -2, 0]) -> [-2, 0, -1, 3]",
    "initialCode": "def sort_even_before_odd_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_3(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [3]\n\nprint(sort_even_before_odd_3([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 3]\nprint(sort_even_before_odd_3([-1, -2, 0]))  # Expected: [-2, 0, -1, 3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7180(values):\n    return sort_even_before_odd_3(values)\n\n# Example 3: static method approach\nclass Problem7180Solution:\n    @staticmethod\n    def sort_even_before_odd_3(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [3]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_3([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7181,
    "title": "Problem 7181",
    "description": "Write a Python function called `sort_even_before_odd_4` that must sort even numbers before odd numbers with ascending values, then append 4. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_4([5, 2, 3, 4]) -> [2, 4, 3, 5, 4]\n  sort_even_before_odd_4([-1, -2, 0]) -> [-2, 0, -1, 4]",
    "initialCode": "def sort_even_before_odd_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_4(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [4]\n\nprint(sort_even_before_odd_4([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 4]\nprint(sort_even_before_odd_4([-1, -2, 0]))  # Expected: [-2, 0, -1, 4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7181(values):\n    return sort_even_before_odd_4(values)\n\n# Example 3: static method approach\nclass Problem7181Solution:\n    @staticmethod\n    def sort_even_before_odd_4(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [4]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_4([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7182,
    "title": "Problem 7182",
    "description": "Write a Python function called `sort_even_before_odd_5` that must sort even numbers before odd numbers with ascending values, then append 5. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_5([5, 2, 3, 4]) -> [2, 4, 3, 5, 5]\n  sort_even_before_odd_5([-1, -2, 0]) -> [-2, 0, -1, 5]",
    "initialCode": "def sort_even_before_odd_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_5(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [5]\n\nprint(sort_even_before_odd_5([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 5]\nprint(sort_even_before_odd_5([-1, -2, 0]))  # Expected: [-2, 0, -1, 5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7182(values):\n    return sort_even_before_odd_5(values)\n\n# Example 3: static method approach\nclass Problem7182Solution:\n    @staticmethod\n    def sort_even_before_odd_5(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [5]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_5([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7183,
    "title": "Problem 7183",
    "description": "Write a Python function called `sort_even_before_odd_6` that must sort even numbers before odd numbers with ascending values, then append 6. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_6([5, 2, 3, 4]) -> [2, 4, 3, 5, 6]\n  sort_even_before_odd_6([-1, -2, 0]) -> [-2, 0, -1, 6]",
    "initialCode": "def sort_even_before_odd_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_6(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [6]\n\nprint(sort_even_before_odd_6([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 6]\nprint(sort_even_before_odd_6([-1, -2, 0]))  # Expected: [-2, 0, -1, 6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7183(values):\n    return sort_even_before_odd_6(values)\n\n# Example 3: static method approach\nclass Problem7183Solution:\n    @staticmethod\n    def sort_even_before_odd_6(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [6]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_6([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7184,
    "title": "Problem 7184",
    "description": "Write a Python function called `sort_even_before_odd_7` that must sort even numbers before odd numbers with ascending values, then append 7. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_7([5, 2, 3, 4]) -> [2, 4, 3, 5, 7]\n  sort_even_before_odd_7([-1, -2, 0]) -> [-2, 0, -1, 7]",
    "initialCode": "def sort_even_before_odd_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_7(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [7]\n\nprint(sort_even_before_odd_7([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 7]\nprint(sort_even_before_odd_7([-1, -2, 0]))  # Expected: [-2, 0, -1, 7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7184(values):\n    return sort_even_before_odd_7(values)\n\n# Example 3: static method approach\nclass Problem7184Solution:\n    @staticmethod\n    def sort_even_before_odd_7(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [7]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_7([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7185,
    "title": "Problem 7185",
    "description": "Write a Python function called `sort_even_before_odd_8` that must sort even numbers before odd numbers with ascending values, then append 8. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_8([5, 2, 3, 4]) -> [2, 4, 3, 5, 8]\n  sort_even_before_odd_8([-1, -2, 0]) -> [-2, 0, -1, 8]",
    "initialCode": "def sort_even_before_odd_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_8(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [8]\n\nprint(sort_even_before_odd_8([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 8]\nprint(sort_even_before_odd_8([-1, -2, 0]))  # Expected: [-2, 0, -1, 8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7185(values):\n    return sort_even_before_odd_8(values)\n\n# Example 3: static method approach\nclass Problem7185Solution:\n    @staticmethod\n    def sort_even_before_odd_8(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [8]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_8([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7186,
    "title": "Problem 7186",
    "description": "Write a Python function called `sort_even_before_odd_9` that must sort even numbers before odd numbers with ascending values, then append 9. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_9([5, 2, 3, 4]) -> [2, 4, 3, 5, 9]\n  sort_even_before_odd_9([-1, -2, 0]) -> [-2, 0, -1, 9]",
    "initialCode": "def sort_even_before_odd_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_9(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [9]\n\nprint(sort_even_before_odd_9([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 9]\nprint(sort_even_before_odd_9([-1, -2, 0]))  # Expected: [-2, 0, -1, 9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7186(values):\n    return sort_even_before_odd_9(values)\n\n# Example 3: static method approach\nclass Problem7186Solution:\n    @staticmethod\n    def sort_even_before_odd_9(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [9]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_9([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7187,
    "title": "Problem 7187",
    "description": "Write a Python function called `sort_even_before_odd_10` that must sort even numbers before odd numbers with ascending values, then append 10. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_even_before_odd_10([5, 2, 3, 4]) -> [2, 4, 3, 5, 10]\n  sort_even_before_odd_10([-1, -2, 0]) -> [-2, 0, -1, 10]",
    "initialCode": "def sort_even_before_odd_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_even_before_odd_10(values):\n    return sorted(values, key=lambda value: (value % 2, value)) + [10]\n\nprint(sort_even_before_odd_10([5, 2, 3, 4]))  # Expected: [2, 4, 3, 5, 10]\nprint(sort_even_before_odd_10([-1, -2, 0]))  # Expected: [-2, 0, -1, 10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7187(values):\n    return sort_even_before_odd_10(values)\n\n# Example 3: static method approach\nclass Problem7187Solution:\n    @staticmethod\n    def sort_even_before_odd_10(values):\n        return sorted(values, key=lambda value: (value % 2, value)) + [10]\n\n# Example 4: assigned result approach\nresult = sort_even_before_odd_10([5, 2, 3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_even_before_odd_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7188,
    "title": "Problem 7188",
    "description": "Write a Python function called `sort_by_distance_1` that must sort values by distance from target then by value and append 1. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_1([1, 8, 4], 5) -> [4, 8, 1, 1]\n  sort_by_distance_1([-3, 2, 7], 0) -> [2, -3, 7, 1]",
    "initialCode": "def sort_by_distance_1(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_1(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [1]\n\nprint(sort_by_distance_1([1, 8, 4], 5))  # Expected: [4, 8, 1, 1]\nprint(sort_by_distance_1([-3, 2, 7], 0))  # Expected: [2, -3, 7, 1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7188(values, target):\n    return sort_by_distance_1(values, target)\n\n# Example 3: static method approach\nclass Problem7188Solution:\n    @staticmethod\n    def sort_by_distance_1(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [1]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_1([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_1([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7189,
    "title": "Problem 7189",
    "description": "Write a Python function called `sort_by_distance_2` that must sort values by distance from target then by value and append 2. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_2([1, 8, 4], 5) -> [4, 8, 1, 2]\n  sort_by_distance_2([-3, 2, 7], 0) -> [2, -3, 7, 2]",
    "initialCode": "def sort_by_distance_2(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_2(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [2]\n\nprint(sort_by_distance_2([1, 8, 4], 5))  # Expected: [4, 8, 1, 2]\nprint(sort_by_distance_2([-3, 2, 7], 0))  # Expected: [2, -3, 7, 2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7189(values, target):\n    return sort_by_distance_2(values, target)\n\n# Example 3: static method approach\nclass Problem7189Solution:\n    @staticmethod\n    def sort_by_distance_2(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [2]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_2([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_2([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7190,
    "title": "Problem 7190",
    "description": "Write a Python function called `sort_by_distance_3` that must sort values by distance from target then by value and append 3. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_3([1, 8, 4], 5) -> [4, 8, 1, 3]\n  sort_by_distance_3([-3, 2, 7], 0) -> [2, -3, 7, 3]",
    "initialCode": "def sort_by_distance_3(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_3(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [3]\n\nprint(sort_by_distance_3([1, 8, 4], 5))  # Expected: [4, 8, 1, 3]\nprint(sort_by_distance_3([-3, 2, 7], 0))  # Expected: [2, -3, 7, 3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7190(values, target):\n    return sort_by_distance_3(values, target)\n\n# Example 3: static method approach\nclass Problem7190Solution:\n    @staticmethod\n    def sort_by_distance_3(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [3]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_3([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_3([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7191,
    "title": "Problem 7191",
    "description": "Write a Python function called `sort_by_distance_4` that must sort values by distance from target then by value and append 4. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_4([1, 8, 4], 5) -> [4, 8, 1, 4]\n  sort_by_distance_4([-3, 2, 7], 0) -> [2, -3, 7, 4]",
    "initialCode": "def sort_by_distance_4(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_4(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [4]\n\nprint(sort_by_distance_4([1, 8, 4], 5))  # Expected: [4, 8, 1, 4]\nprint(sort_by_distance_4([-3, 2, 7], 0))  # Expected: [2, -3, 7, 4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7191(values, target):\n    return sort_by_distance_4(values, target)\n\n# Example 3: static method approach\nclass Problem7191Solution:\n    @staticmethod\n    def sort_by_distance_4(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [4]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_4([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_4([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7192,
    "title": "Problem 7192",
    "description": "Write a Python function called `sort_by_distance_5` that must sort values by distance from target then by value and append 5. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_5([1, 8, 4], 5) -> [4, 8, 1, 5]\n  sort_by_distance_5([-3, 2, 7], 0) -> [2, -3, 7, 5]",
    "initialCode": "def sort_by_distance_5(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_5(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [5]\n\nprint(sort_by_distance_5([1, 8, 4], 5))  # Expected: [4, 8, 1, 5]\nprint(sort_by_distance_5([-3, 2, 7], 0))  # Expected: [2, -3, 7, 5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7192(values, target):\n    return sort_by_distance_5(values, target)\n\n# Example 3: static method approach\nclass Problem7192Solution:\n    @staticmethod\n    def sort_by_distance_5(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [5]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_5([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_5([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7193,
    "title": "Problem 7193",
    "description": "Write a Python function called `sort_by_distance_6` that must sort values by distance from target then by value and append 6. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_6([1, 8, 4], 5) -> [4, 8, 1, 6]\n  sort_by_distance_6([-3, 2, 7], 0) -> [2, -3, 7, 6]",
    "initialCode": "def sort_by_distance_6(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_6(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [6]\n\nprint(sort_by_distance_6([1, 8, 4], 5))  # Expected: [4, 8, 1, 6]\nprint(sort_by_distance_6([-3, 2, 7], 0))  # Expected: [2, -3, 7, 6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7193(values, target):\n    return sort_by_distance_6(values, target)\n\n# Example 3: static method approach\nclass Problem7193Solution:\n    @staticmethod\n    def sort_by_distance_6(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [6]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_6([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_6([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7194,
    "title": "Problem 7194",
    "description": "Write a Python function called `sort_by_distance_7` that must sort values by distance from target then by value and append 7. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_7([1, 8, 4], 5) -> [4, 8, 1, 7]\n  sort_by_distance_7([-3, 2, 7], 0) -> [2, -3, 7, 7]",
    "initialCode": "def sort_by_distance_7(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_7(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [7]\n\nprint(sort_by_distance_7([1, 8, 4], 5))  # Expected: [4, 8, 1, 7]\nprint(sort_by_distance_7([-3, 2, 7], 0))  # Expected: [2, -3, 7, 7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7194(values, target):\n    return sort_by_distance_7(values, target)\n\n# Example 3: static method approach\nclass Problem7194Solution:\n    @staticmethod\n    def sort_by_distance_7(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [7]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_7([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_7([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7195,
    "title": "Problem 7195",
    "description": "Write a Python function called `sort_by_distance_8` that must sort values by distance from target then by value and append 8. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_8([1, 8, 4], 5) -> [4, 8, 1, 8]\n  sort_by_distance_8([-3, 2, 7], 0) -> [2, -3, 7, 8]",
    "initialCode": "def sort_by_distance_8(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_8(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [8]\n\nprint(sort_by_distance_8([1, 8, 4], 5))  # Expected: [4, 8, 1, 8]\nprint(sort_by_distance_8([-3, 2, 7], 0))  # Expected: [2, -3, 7, 8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7195(values, target):\n    return sort_by_distance_8(values, target)\n\n# Example 3: static method approach\nclass Problem7195Solution:\n    @staticmethod\n    def sort_by_distance_8(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [8]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_8([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_8([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7196,
    "title": "Problem 7196",
    "description": "Write a Python function called `sort_by_distance_9` that must sort values by distance from target then by value and append 9. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_9([1, 8, 4], 5) -> [4, 8, 1, 9]\n  sort_by_distance_9([-3, 2, 7], 0) -> [2, -3, 7, 9]",
    "initialCode": "def sort_by_distance_9(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_9(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [9]\n\nprint(sort_by_distance_9([1, 8, 4], 5))  # Expected: [4, 8, 1, 9]\nprint(sort_by_distance_9([-3, 2, 7], 0))  # Expected: [2, -3, 7, 9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7196(values, target):\n    return sort_by_distance_9(values, target)\n\n# Example 3: static method approach\nclass Problem7196Solution:\n    @staticmethod\n    def sort_by_distance_9(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [9]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_9([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_9([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7197,
    "title": "Problem 7197",
    "description": "Write a Python function called `sort_by_distance_10` that must sort values by distance from target then by value and append 10. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_distance_10([1, 8, 4], 5) -> [4, 8, 1, 10]\n  sort_by_distance_10([-3, 2, 7], 0) -> [2, -3, 7, 10]",
    "initialCode": "def sort_by_distance_10(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_distance_10(values, target):\n    return sorted(values, key=lambda value: (abs(value - target), value)) + [10]\n\nprint(sort_by_distance_10([1, 8, 4], 5))  # Expected: [4, 8, 1, 10]\nprint(sort_by_distance_10([-3, 2, 7], 0))  # Expected: [2, -3, 7, 10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7197(values, target):\n    return sort_by_distance_10(values, target)\n\n# Example 3: static method approach\nclass Problem7197Solution:\n    @staticmethod\n    def sort_by_distance_10(values, target):\n        return sorted(values, key=lambda value: (abs(value - target), value)) + [10]\n\n# Example 4: assigned result approach\nresult = sort_by_distance_10([1, 8, 4], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_distance_10([], 9))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7198,
    "title": "Problem 7198",
    "description": "Write a Python function called `sort_by_character_count_1` that must sort words by descending character count then alphabetically and append marker_1. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_1([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_1\"]\n  sort_by_character_count_1([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_1\"]",
    "initialCode": "def sort_by_character_count_1(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_1(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_1\"]\n\nprint(sort_by_character_count_1([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_1\"]\nprint(sort_by_character_count_1([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_1\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7198(words, character):\n    return sort_by_character_count_1(words, character)\n\n# Example 3: static method approach\nclass Problem7198Solution:\n    @staticmethod\n    def sort_by_character_count_1(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_1\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_1([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_1([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7199,
    "title": "Problem 7199",
    "description": "Write a Python function called `sort_by_character_count_2` that must sort words by descending character count then alphabetically and append marker_2. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_2([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_2\"]\n  sort_by_character_count_2([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_2\"]",
    "initialCode": "def sort_by_character_count_2(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_2(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_2\"]\n\nprint(sort_by_character_count_2([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_2\"]\nprint(sort_by_character_count_2([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_2\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7199(words, character):\n    return sort_by_character_count_2(words, character)\n\n# Example 3: static method approach\nclass Problem7199Solution:\n    @staticmethod\n    def sort_by_character_count_2(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_2\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_2([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_2([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7200,
    "title": "Problem 7200",
    "description": "Write a Python function called `sort_by_character_count_3` that must sort words by descending character count then alphabetically and append marker_3. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_3([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_3\"]\n  sort_by_character_count_3([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_3\"]",
    "initialCode": "def sort_by_character_count_3(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_3(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_3\"]\n\nprint(sort_by_character_count_3([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_3\"]\nprint(sort_by_character_count_3([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_3\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7200(words, character):\n    return sort_by_character_count_3(words, character)\n\n# Example 3: static method approach\nclass Problem7200Solution:\n    @staticmethod\n    def sort_by_character_count_3(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_3\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_3([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_3([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7201,
    "title": "Problem 7201",
    "description": "Write a Python function called `sort_by_character_count_4` that must sort words by descending character count then alphabetically and append marker_4. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_4([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_4\"]\n  sort_by_character_count_4([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_4\"]",
    "initialCode": "def sort_by_character_count_4(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_4(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_4\"]\n\nprint(sort_by_character_count_4([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_4\"]\nprint(sort_by_character_count_4([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_4\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7201(words, character):\n    return sort_by_character_count_4(words, character)\n\n# Example 3: static method approach\nclass Problem7201Solution:\n    @staticmethod\n    def sort_by_character_count_4(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_4\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_4([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_4([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7202,
    "title": "Problem 7202",
    "description": "Write a Python function called `sort_by_character_count_5` that must sort words by descending character count then alphabetically and append marker_5. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_5([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_5\"]\n  sort_by_character_count_5([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_5\"]",
    "initialCode": "def sort_by_character_count_5(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_5(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_5\"]\n\nprint(sort_by_character_count_5([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_5\"]\nprint(sort_by_character_count_5([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_5\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7202(words, character):\n    return sort_by_character_count_5(words, character)\n\n# Example 3: static method approach\nclass Problem7202Solution:\n    @staticmethod\n    def sort_by_character_count_5(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_5\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_5([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_5([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7203,
    "title": "Problem 7203",
    "description": "Write a Python function called `sort_by_character_count_6` that must sort words by descending character count then alphabetically and append marker_6. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_6([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_6\"]\n  sort_by_character_count_6([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_6\"]",
    "initialCode": "def sort_by_character_count_6(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_6(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_6\"]\n\nprint(sort_by_character_count_6([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_6\"]\nprint(sort_by_character_count_6([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_6\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7203(words, character):\n    return sort_by_character_count_6(words, character)\n\n# Example 3: static method approach\nclass Problem7203Solution:\n    @staticmethod\n    def sort_by_character_count_6(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_6\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_6([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_6([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7204,
    "title": "Problem 7204",
    "description": "Write a Python function called `sort_by_character_count_7` that must sort words by descending character count then alphabetically and append marker_7. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_7([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_7\"]\n  sort_by_character_count_7([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_7\"]",
    "initialCode": "def sort_by_character_count_7(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_7(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_7\"]\n\nprint(sort_by_character_count_7([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_7\"]\nprint(sort_by_character_count_7([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_7\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7204(words, character):\n    return sort_by_character_count_7(words, character)\n\n# Example 3: static method approach\nclass Problem7204Solution:\n    @staticmethod\n    def sort_by_character_count_7(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_7\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_7([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_7([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7205,
    "title": "Problem 7205",
    "description": "Write a Python function called `sort_by_character_count_8` that must sort words by descending character count then alphabetically and append marker_8. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_8([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_8\"]\n  sort_by_character_count_8([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_8\"]",
    "initialCode": "def sort_by_character_count_8(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_8(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_8\"]\n\nprint(sort_by_character_count_8([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_8\"]\nprint(sort_by_character_count_8([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_8\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7205(words, character):\n    return sort_by_character_count_8(words, character)\n\n# Example 3: static method approach\nclass Problem7205Solution:\n    @staticmethod\n    def sort_by_character_count_8(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_8\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_8([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_8([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7206,
    "title": "Problem 7206",
    "description": "Write a Python function called `sort_by_character_count_9` that must sort words by descending character count then alphabetically and append marker_9. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_9([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_9\"]\n  sort_by_character_count_9([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_9\"]",
    "initialCode": "def sort_by_character_count_9(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_9(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_9\"]\n\nprint(sort_by_character_count_9([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_9\"]\nprint(sort_by_character_count_9([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_9\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7206(words, character):\n    return sort_by_character_count_9(words, character)\n\n# Example 3: static method approach\nclass Problem7206Solution:\n    @staticmethod\n    def sort_by_character_count_9(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_9\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_9([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_9([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7207,
    "title": "Problem 7207",
    "description": "Write a Python function called `sort_by_character_count_10` that must sort words by descending character count then alphabetically and append marker_10. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_by_character_count_10([\"banana\", \"pear\", \"apple\"], \"a\") -> [\"banana\", \"apple\", \"pear\", \"marker_10\"]\n  sort_by_character_count_10([\"test\", \"tree\"], \"t\") -> [\"test\", \"tree\", \"marker_10\"]",
    "initialCode": "def sort_by_character_count_10(words, character):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_character_count_10(words, character):\n    return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_10\"]\n\nprint(sort_by_character_count_10([\"banana\", \"pear\", \"apple\"], \"a\"))  # Expected: [\"banana\", \"apple\", \"pear\", \"marker_10\"]\nprint(sort_by_character_count_10([\"test\", \"tree\"], \"t\"))  # Expected: [\"test\", \"tree\", \"marker_10\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7207(words, character):\n    return sort_by_character_count_10(words, character)\n\n# Example 3: static method approach\nclass Problem7207Solution:\n    @staticmethod\n    def sort_by_character_count_10(words, character):\n        return sorted(words, key=lambda word: (-word.count(character), word)) + [\"marker_10\"]\n\n# Example 4: assigned result approach\nresult = sort_by_character_count_10([\"banana\", \"pear\", \"apple\"], \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_character_count_10([], \"x\"))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7208,
    "title": "Problem 7208",
    "description": "Write a Python function called `sort_people_multiple_fields_1` that must sort people by descending score, ascending age, then name and append marker 1. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_1([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 1}]\n  sort_people_multiple_fields_1([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 1}]",
    "initialCode": "def sort_people_multiple_fields_1(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_1(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 1}]\n\nprint(sort_people_multiple_fields_1([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 1}]\nprint(sort_people_multiple_fields_1([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 1}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7208(people):\n    return sort_people_multiple_fields_1(people)\n\n# Example 3: static method approach\nclass Problem7208Solution:\n    @staticmethod\n    def sort_people_multiple_fields_1(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 1}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_1([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7209,
    "title": "Problem 7209",
    "description": "Write a Python function called `sort_people_multiple_fields_2` that must sort people by descending score, ascending age, then name and append marker 2. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_2([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 2}]\n  sort_people_multiple_fields_2([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 2}]",
    "initialCode": "def sort_people_multiple_fields_2(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_2(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 2}]\n\nprint(sort_people_multiple_fields_2([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 2}]\nprint(sort_people_multiple_fields_2([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 2}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7209(people):\n    return sort_people_multiple_fields_2(people)\n\n# Example 3: static method approach\nclass Problem7209Solution:\n    @staticmethod\n    def sort_people_multiple_fields_2(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 2}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_2([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7210,
    "title": "Problem 7210",
    "description": "Write a Python function called `sort_people_multiple_fields_3` that must sort people by descending score, ascending age, then name and append marker 3. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_3([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 3}]\n  sort_people_multiple_fields_3([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 3}]",
    "initialCode": "def sort_people_multiple_fields_3(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_3(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 3}]\n\nprint(sort_people_multiple_fields_3([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 3}]\nprint(sort_people_multiple_fields_3([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 3}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7210(people):\n    return sort_people_multiple_fields_3(people)\n\n# Example 3: static method approach\nclass Problem7210Solution:\n    @staticmethod\n    def sort_people_multiple_fields_3(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 3}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_3([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7211,
    "title": "Problem 7211",
    "description": "Write a Python function called `sort_people_multiple_fields_4` that must sort people by descending score, ascending age, then name and append marker 4. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_4([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 4}]\n  sort_people_multiple_fields_4([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 4}]",
    "initialCode": "def sort_people_multiple_fields_4(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_4(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 4}]\n\nprint(sort_people_multiple_fields_4([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 4}]\nprint(sort_people_multiple_fields_4([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 4}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7211(people):\n    return sort_people_multiple_fields_4(people)\n\n# Example 3: static method approach\nclass Problem7211Solution:\n    @staticmethod\n    def sort_people_multiple_fields_4(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 4}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_4([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7212,
    "title": "Problem 7212",
    "description": "Write a Python function called `sort_people_multiple_fields_5` that must sort people by descending score, ascending age, then name and append marker 5. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_5([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 5}]\n  sort_people_multiple_fields_5([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 5}]",
    "initialCode": "def sort_people_multiple_fields_5(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_5(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 5}]\n\nprint(sort_people_multiple_fields_5([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 5}]\nprint(sort_people_multiple_fields_5([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 5}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7212(people):\n    return sort_people_multiple_fields_5(people)\n\n# Example 3: static method approach\nclass Problem7212Solution:\n    @staticmethod\n    def sort_people_multiple_fields_5(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 5}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_5([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7213,
    "title": "Problem 7213",
    "description": "Write a Python function called `sort_people_multiple_fields_6` that must sort people by descending score, ascending age, then name and append marker 6. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_6([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 6}]\n  sort_people_multiple_fields_6([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 6}]",
    "initialCode": "def sort_people_multiple_fields_6(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_6(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 6}]\n\nprint(sort_people_multiple_fields_6([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 6}]\nprint(sort_people_multiple_fields_6([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 6}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7213(people):\n    return sort_people_multiple_fields_6(people)\n\n# Example 3: static method approach\nclass Problem7213Solution:\n    @staticmethod\n    def sort_people_multiple_fields_6(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 6}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_6([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7214,
    "title": "Problem 7214",
    "description": "Write a Python function called `sort_people_multiple_fields_7` that must sort people by descending score, ascending age, then name and append marker 7. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_7([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 7}]\n  sort_people_multiple_fields_7([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 7}]",
    "initialCode": "def sort_people_multiple_fields_7(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_7(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 7}]\n\nprint(sort_people_multiple_fields_7([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 7}]\nprint(sort_people_multiple_fields_7([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 7}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7214(people):\n    return sort_people_multiple_fields_7(people)\n\n# Example 3: static method approach\nclass Problem7214Solution:\n    @staticmethod\n    def sort_people_multiple_fields_7(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 7}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_7([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7215,
    "title": "Problem 7215",
    "description": "Write a Python function called `sort_people_multiple_fields_8` that must sort people by descending score, ascending age, then name and append marker 8. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_8([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 8}]\n  sort_people_multiple_fields_8([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 8}]",
    "initialCode": "def sort_people_multiple_fields_8(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_8(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 8}]\n\nprint(sort_people_multiple_fields_8([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 8}]\nprint(sort_people_multiple_fields_8([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 8}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7215(people):\n    return sort_people_multiple_fields_8(people)\n\n# Example 3: static method approach\nclass Problem7215Solution:\n    @staticmethod\n    def sort_people_multiple_fields_8(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 8}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_8([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7216,
    "title": "Problem 7216",
    "description": "Write a Python function called `sort_people_multiple_fields_9` that must sort people by descending score, ascending age, then name and append marker 9. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_9([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 9}]\n  sort_people_multiple_fields_9([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 9}]",
    "initialCode": "def sort_people_multiple_fields_9(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_9(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 9}]\n\nprint(sort_people_multiple_fields_9([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 9}]\nprint(sort_people_multiple_fields_9([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 9}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7216(people):\n    return sort_people_multiple_fields_9(people)\n\n# Example 3: static method approach\nclass Problem7216Solution:\n    @staticmethod\n    def sort_people_multiple_fields_9(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 9}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_9([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7217,
    "title": "Problem 7217",
    "description": "Write a Python function called `sort_people_multiple_fields_10` that must sort people by descending score, ascending age, then name and append marker 10. Practice sorting key.\nDifficulty: Intermediate.\nExamples:\n  sort_people_multiple_fields_10([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]) -> [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 10}]\n  sort_people_multiple_fields_10([{\"name\": \"X\", \"score\": 1, \"age\": 2}]) -> [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 10}]",
    "initialCode": "def sort_people_multiple_fields_10(people):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_people_multiple_fields_10(people):\n    return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 10}]\n\nprint(sort_people_multiple_fields_10([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}]))  # Expected: [{\"name\": \"A\", \"score\": 9, \"age\": 20}, {\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"marker\": 10}]\nprint(sort_people_multiple_fields_10([{\"name\": \"X\", \"score\": 1, \"age\": 2}]))  # Expected: [{\"name\": \"X\", \"score\": 1, \"age\": 2}, {\"marker\": 10}]\n\n# Example 2: named wrapper approach\ndef solve_problem_7217(people):\n    return sort_people_multiple_fields_10(people)\n\n# Example 3: static method approach\nclass Problem7217Solution:\n    @staticmethod\n    def sort_people_multiple_fields_10(people):\n        return sorted(people, key=lambda person: (-person[\"score\"], person[\"age\"], person[\"name\"])) + [{\"marker\": 10}]\n\n# Example 4: assigned result approach\nresult = sort_people_multiple_fields_10([{\"name\": \"B\", \"score\": 9, \"age\": 30}, {\"name\": \"A\", \"score\": 9, \"age\": 20}])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_people_multiple_fields_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Intermediate"
  },
  {
    "id": 7218,
    "title": "Problem 7218",
    "description": "Write a Python function called `sort_nested_by_sum_1` that must sort nested number lists by sum, length, then contents and append marker list 1. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_1([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [1]]\n  sort_nested_by_sum_1([[3], [-1, 1]]) -> [[-1, 1], [3], [1]]",
    "initialCode": "def sort_nested_by_sum_1(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_1(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[1]]\n\nprint(sort_nested_by_sum_1([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [1]]\nprint(sort_nested_by_sum_1([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7218(groups):\n    return sort_nested_by_sum_1(groups)\n\n# Example 3: static method approach\nclass Problem7218Solution:\n    @staticmethod\n    def sort_nested_by_sum_1(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[1]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_1([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7219,
    "title": "Problem 7219",
    "description": "Write a Python function called `sort_nested_by_sum_2` that must sort nested number lists by sum, length, then contents and append marker list 2. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_2([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [2]]\n  sort_nested_by_sum_2([[3], [-1, 1]]) -> [[-1, 1], [3], [2]]",
    "initialCode": "def sort_nested_by_sum_2(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_2(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[2]]\n\nprint(sort_nested_by_sum_2([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [2]]\nprint(sort_nested_by_sum_2([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [2]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7219(groups):\n    return sort_nested_by_sum_2(groups)\n\n# Example 3: static method approach\nclass Problem7219Solution:\n    @staticmethod\n    def sort_nested_by_sum_2(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[2]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_2([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7220,
    "title": "Problem 7220",
    "description": "Write a Python function called `sort_nested_by_sum_3` that must sort nested number lists by sum, length, then contents and append marker list 3. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_3([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [3]]\n  sort_nested_by_sum_3([[3], [-1, 1]]) -> [[-1, 1], [3], [3]]",
    "initialCode": "def sort_nested_by_sum_3(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_3(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[3]]\n\nprint(sort_nested_by_sum_3([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [3]]\nprint(sort_nested_by_sum_3([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [3]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7220(groups):\n    return sort_nested_by_sum_3(groups)\n\n# Example 3: static method approach\nclass Problem7220Solution:\n    @staticmethod\n    def sort_nested_by_sum_3(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[3]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_3([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7221,
    "title": "Problem 7221",
    "description": "Write a Python function called `sort_nested_by_sum_4` that must sort nested number lists by sum, length, then contents and append marker list 4. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_4([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [4]]\n  sort_nested_by_sum_4([[3], [-1, 1]]) -> [[-1, 1], [3], [4]]",
    "initialCode": "def sort_nested_by_sum_4(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_4(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[4]]\n\nprint(sort_nested_by_sum_4([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [4]]\nprint(sort_nested_by_sum_4([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [4]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7221(groups):\n    return sort_nested_by_sum_4(groups)\n\n# Example 3: static method approach\nclass Problem7221Solution:\n    @staticmethod\n    def sort_nested_by_sum_4(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[4]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_4([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7222,
    "title": "Problem 7222",
    "description": "Write a Python function called `sort_nested_by_sum_5` that must sort nested number lists by sum, length, then contents and append marker list 5. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_5([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [5]]\n  sort_nested_by_sum_5([[3], [-1, 1]]) -> [[-1, 1], [3], [5]]",
    "initialCode": "def sort_nested_by_sum_5(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_5(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[5]]\n\nprint(sort_nested_by_sum_5([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [5]]\nprint(sort_nested_by_sum_5([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [5]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7222(groups):\n    return sort_nested_by_sum_5(groups)\n\n# Example 3: static method approach\nclass Problem7222Solution:\n    @staticmethod\n    def sort_nested_by_sum_5(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[5]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_5([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7223,
    "title": "Problem 7223",
    "description": "Write a Python function called `sort_nested_by_sum_6` that must sort nested number lists by sum, length, then contents and append marker list 6. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_6([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [6]]\n  sort_nested_by_sum_6([[3], [-1, 1]]) -> [[-1, 1], [3], [6]]",
    "initialCode": "def sort_nested_by_sum_6(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_6(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[6]]\n\nprint(sort_nested_by_sum_6([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [6]]\nprint(sort_nested_by_sum_6([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [6]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7223(groups):\n    return sort_nested_by_sum_6(groups)\n\n# Example 3: static method approach\nclass Problem7223Solution:\n    @staticmethod\n    def sort_nested_by_sum_6(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[6]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_6([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7224,
    "title": "Problem 7224",
    "description": "Write a Python function called `sort_nested_by_sum_7` that must sort nested number lists by sum, length, then contents and append marker list 7. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_7([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [7]]\n  sort_nested_by_sum_7([[3], [-1, 1]]) -> [[-1, 1], [3], [7]]",
    "initialCode": "def sort_nested_by_sum_7(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_7(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[7]]\n\nprint(sort_nested_by_sum_7([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [7]]\nprint(sort_nested_by_sum_7([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [7]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7224(groups):\n    return sort_nested_by_sum_7(groups)\n\n# Example 3: static method approach\nclass Problem7224Solution:\n    @staticmethod\n    def sort_nested_by_sum_7(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[7]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_7([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7225,
    "title": "Problem 7225",
    "description": "Write a Python function called `sort_nested_by_sum_8` that must sort nested number lists by sum, length, then contents and append marker list 8. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_8([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [8]]\n  sort_nested_by_sum_8([[3], [-1, 1]]) -> [[-1, 1], [3], [8]]",
    "initialCode": "def sort_nested_by_sum_8(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_8(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[8]]\n\nprint(sort_nested_by_sum_8([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [8]]\nprint(sort_nested_by_sum_8([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [8]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7225(groups):\n    return sort_nested_by_sum_8(groups)\n\n# Example 3: static method approach\nclass Problem7225Solution:\n    @staticmethod\n    def sort_nested_by_sum_8(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[8]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_8([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7226,
    "title": "Problem 7226",
    "description": "Write a Python function called `sort_nested_by_sum_9` that must sort nested number lists by sum, length, then contents and append marker list 9. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_9([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [9]]\n  sort_nested_by_sum_9([[3], [-1, 1]]) -> [[-1, 1], [3], [9]]",
    "initialCode": "def sort_nested_by_sum_9(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_9(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[9]]\n\nprint(sort_nested_by_sum_9([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [9]]\nprint(sort_nested_by_sum_9([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [9]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7226(groups):\n    return sort_nested_by_sum_9(groups)\n\n# Example 3: static method approach\nclass Problem7226Solution:\n    @staticmethod\n    def sort_nested_by_sum_9(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[9]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_9([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7227,
    "title": "Problem 7227",
    "description": "Write a Python function called `sort_nested_by_sum_10` that must sort nested number lists by sum, length, then contents and append marker list 10. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_nested_by_sum_10([[2, 2], [1], [0, 1]]) -> [[1], [0, 1], [2, 2], [10]]\n  sort_nested_by_sum_10([[3], [-1, 1]]) -> [[-1, 1], [3], [10]]",
    "initialCode": "def sort_nested_by_sum_10(groups):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_nested_by_sum_10(groups):\n    return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[10]]\n\nprint(sort_nested_by_sum_10([[2, 2], [1], [0, 1]]))  # Expected: [[1], [0, 1], [2, 2], [10]]\nprint(sort_nested_by_sum_10([[3], [-1, 1]]))  # Expected: [[-1, 1], [3], [10]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7227(groups):\n    return sort_nested_by_sum_10(groups)\n\n# Example 3: static method approach\nclass Problem7227Solution:\n    @staticmethod\n    def sort_nested_by_sum_10(groups):\n        return sorted(groups, key=lambda group: (sum(group), len(group), group)) + [[10]]\n\n# Example 4: assigned result approach\nresult = sort_nested_by_sum_10([[2, 2], [1], [0, 1]])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_nested_by_sum_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7228,
    "title": "Problem 7228",
    "description": "Write a Python function called `sort_files_extension_1` that must sort filenames by lowercase extension then lowercase name and append marker_1.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_1([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_1.txt\"]\n  sort_files_extension_1([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_1.txt\"]",
    "initialCode": "def sort_files_extension_1(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_1(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_1.txt\"]\n\nprint(sort_files_extension_1([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_1.txt\"]\nprint(sort_files_extension_1([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_1.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7228(names):\n    return sort_files_extension_1(names)\n\n# Example 3: static method approach\nclass Problem7228Solution:\n    @staticmethod\n    def sort_files_extension_1(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_1.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_1([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7229,
    "title": "Problem 7229",
    "description": "Write a Python function called `sort_files_extension_2` that must sort filenames by lowercase extension then lowercase name and append marker_2.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_2([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_2.txt\"]\n  sort_files_extension_2([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_2.txt\"]",
    "initialCode": "def sort_files_extension_2(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_2(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_2.txt\"]\n\nprint(sort_files_extension_2([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_2.txt\"]\nprint(sort_files_extension_2([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_2.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7229(names):\n    return sort_files_extension_2(names)\n\n# Example 3: static method approach\nclass Problem7229Solution:\n    @staticmethod\n    def sort_files_extension_2(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_2.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_2([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7230,
    "title": "Problem 7230",
    "description": "Write a Python function called `sort_files_extension_3` that must sort filenames by lowercase extension then lowercase name and append marker_3.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_3([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_3.txt\"]\n  sort_files_extension_3([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_3.txt\"]",
    "initialCode": "def sort_files_extension_3(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_3(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_3.txt\"]\n\nprint(sort_files_extension_3([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_3.txt\"]\nprint(sort_files_extension_3([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_3.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7230(names):\n    return sort_files_extension_3(names)\n\n# Example 3: static method approach\nclass Problem7230Solution:\n    @staticmethod\n    def sort_files_extension_3(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_3.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_3([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7231,
    "title": "Problem 7231",
    "description": "Write a Python function called `sort_files_extension_4` that must sort filenames by lowercase extension then lowercase name and append marker_4.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_4([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_4.txt\"]\n  sort_files_extension_4([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_4.txt\"]",
    "initialCode": "def sort_files_extension_4(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_4(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_4.txt\"]\n\nprint(sort_files_extension_4([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_4.txt\"]\nprint(sort_files_extension_4([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_4.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7231(names):\n    return sort_files_extension_4(names)\n\n# Example 3: static method approach\nclass Problem7231Solution:\n    @staticmethod\n    def sort_files_extension_4(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_4.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_4([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7232,
    "title": "Problem 7232",
    "description": "Write a Python function called `sort_files_extension_5` that must sort filenames by lowercase extension then lowercase name and append marker_5.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_5([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_5.txt\"]\n  sort_files_extension_5([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_5.txt\"]",
    "initialCode": "def sort_files_extension_5(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_5(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_5.txt\"]\n\nprint(sort_files_extension_5([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_5.txt\"]\nprint(sort_files_extension_5([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_5.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7232(names):\n    return sort_files_extension_5(names)\n\n# Example 3: static method approach\nclass Problem7232Solution:\n    @staticmethod\n    def sort_files_extension_5(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_5.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_5([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7233,
    "title": "Problem 7233",
    "description": "Write a Python function called `sort_files_extension_6` that must sort filenames by lowercase extension then lowercase name and append marker_6.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_6([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_6.txt\"]\n  sort_files_extension_6([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_6.txt\"]",
    "initialCode": "def sort_files_extension_6(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_6(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_6.txt\"]\n\nprint(sort_files_extension_6([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_6.txt\"]\nprint(sort_files_extension_6([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_6.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7233(names):\n    return sort_files_extension_6(names)\n\n# Example 3: static method approach\nclass Problem7233Solution:\n    @staticmethod\n    def sort_files_extension_6(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_6.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_6([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7234,
    "title": "Problem 7234",
    "description": "Write a Python function called `sort_files_extension_7` that must sort filenames by lowercase extension then lowercase name and append marker_7.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_7([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_7.txt\"]\n  sort_files_extension_7([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_7.txt\"]",
    "initialCode": "def sort_files_extension_7(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_7(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_7.txt\"]\n\nprint(sort_files_extension_7([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_7.txt\"]\nprint(sort_files_extension_7([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_7.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7234(names):\n    return sort_files_extension_7(names)\n\n# Example 3: static method approach\nclass Problem7234Solution:\n    @staticmethod\n    def sort_files_extension_7(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_7.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_7([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7235,
    "title": "Problem 7235",
    "description": "Write a Python function called `sort_files_extension_8` that must sort filenames by lowercase extension then lowercase name and append marker_8.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_8([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_8.txt\"]\n  sort_files_extension_8([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_8.txt\"]",
    "initialCode": "def sort_files_extension_8(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_8(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_8.txt\"]\n\nprint(sort_files_extension_8([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_8.txt\"]\nprint(sort_files_extension_8([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_8.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7235(names):\n    return sort_files_extension_8(names)\n\n# Example 3: static method approach\nclass Problem7235Solution:\n    @staticmethod\n    def sort_files_extension_8(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_8.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_8([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7236,
    "title": "Problem 7236",
    "description": "Write a Python function called `sort_files_extension_9` that must sort filenames by lowercase extension then lowercase name and append marker_9.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_9([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_9.txt\"]\n  sort_files_extension_9([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_9.txt\"]",
    "initialCode": "def sort_files_extension_9(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_9(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_9.txt\"]\n\nprint(sort_files_extension_9([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_9.txt\"]\nprint(sort_files_extension_9([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_9.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7236(names):\n    return sort_files_extension_9(names)\n\n# Example 3: static method approach\nclass Problem7236Solution:\n    @staticmethod\n    def sort_files_extension_9(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_9.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_9([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7237,
    "title": "Problem 7237",
    "description": "Write a Python function called `sort_files_extension_10` that must sort filenames by lowercase extension then lowercase name and append marker_10.txt. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_files_extension_10([\"b.py\", \"a.TXT\", \"README\"]) -> [\"README\", \"b.py\", \"a.TXT\", \"marker_10.txt\"]\n  sort_files_extension_10([\"z.csv\", \"A.csv\"]) -> [\"A.csv\", \"z.csv\", \"marker_10.txt\"]",
    "initialCode": "def sort_files_extension_10(names):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_files_extension_10(names):\n    def key(name):\n        stem, separator, extension = name.rpartition(\".\")\n        return (extension.casefold() if separator else \"\", name.casefold())\n    return sorted(names, key=key) + [\"marker_10.txt\"]\n\nprint(sort_files_extension_10([\"b.py\", \"a.TXT\", \"README\"]))  # Expected: [\"README\", \"b.py\", \"a.TXT\", \"marker_10.txt\"]\nprint(sort_files_extension_10([\"z.csv\", \"A.csv\"]))  # Expected: [\"A.csv\", \"z.csv\", \"marker_10.txt\"]\n\n# Example 2: named wrapper approach\ndef solve_problem_7237(names):\n    return sort_files_extension_10(names)\n\n# Example 3: static method approach\nclass Problem7237Solution:\n    @staticmethod\n    def sort_files_extension_10(names):\n        def key(name):\n            stem, separator, extension = name.rpartition(\".\")\n            return (extension.casefold() if separator else \"\", name.casefold())\n        return sorted(names, key=key) + [\"marker_10.txt\"]\n\n# Example 4: assigned result approach\nresult = sort_files_extension_10([\"b.py\", \"a.TXT\", \"README\"])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_files_extension_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7238,
    "title": "Problem 7238",
    "description": "Write a Python function called `sort_by_frequency_1` that must sort values by descending frequency then numeric value and append 1. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_1([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 1]\n  sort_by_frequency_1([2, 2, 1]) -> [2, 2, 1, 1]",
    "initialCode": "def sort_by_frequency_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_1(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [1]\n\nprint(sort_by_frequency_1([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 1]\nprint(sort_by_frequency_1([2, 2, 1]))  # Expected: [2, 2, 1, 1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7238(values):\n    return sort_by_frequency_1(values)\n\n# Example 3: static method approach\nclass Problem7238Solution:\n    @staticmethod\n    def sort_by_frequency_1(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [1]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_1([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_1([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7239,
    "title": "Problem 7239",
    "description": "Write a Python function called `sort_by_frequency_2` that must sort values by descending frequency then numeric value and append 2. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_2([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 2]\n  sort_by_frequency_2([2, 2, 1]) -> [2, 2, 1, 2]",
    "initialCode": "def sort_by_frequency_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_2(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [2]\n\nprint(sort_by_frequency_2([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 2]\nprint(sort_by_frequency_2([2, 2, 1]))  # Expected: [2, 2, 1, 2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7239(values):\n    return sort_by_frequency_2(values)\n\n# Example 3: static method approach\nclass Problem7239Solution:\n    @staticmethod\n    def sort_by_frequency_2(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [2]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_2([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_2([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7240,
    "title": "Problem 7240",
    "description": "Write a Python function called `sort_by_frequency_3` that must sort values by descending frequency then numeric value and append 3. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_3([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 3]\n  sort_by_frequency_3([2, 2, 1]) -> [2, 2, 1, 3]",
    "initialCode": "def sort_by_frequency_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_3(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [3]\n\nprint(sort_by_frequency_3([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 3]\nprint(sort_by_frequency_3([2, 2, 1]))  # Expected: [2, 2, 1, 3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7240(values):\n    return sort_by_frequency_3(values)\n\n# Example 3: static method approach\nclass Problem7240Solution:\n    @staticmethod\n    def sort_by_frequency_3(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [3]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_3([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_3([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7241,
    "title": "Problem 7241",
    "description": "Write a Python function called `sort_by_frequency_4` that must sort values by descending frequency then numeric value and append 4. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_4([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 4]\n  sort_by_frequency_4([2, 2, 1]) -> [2, 2, 1, 4]",
    "initialCode": "def sort_by_frequency_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_4(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [4]\n\nprint(sort_by_frequency_4([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 4]\nprint(sort_by_frequency_4([2, 2, 1]))  # Expected: [2, 2, 1, 4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7241(values):\n    return sort_by_frequency_4(values)\n\n# Example 3: static method approach\nclass Problem7241Solution:\n    @staticmethod\n    def sort_by_frequency_4(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [4]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_4([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_4([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7242,
    "title": "Problem 7242",
    "description": "Write a Python function called `sort_by_frequency_5` that must sort values by descending frequency then numeric value and append 5. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_5([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 5]\n  sort_by_frequency_5([2, 2, 1]) -> [2, 2, 1, 5]",
    "initialCode": "def sort_by_frequency_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_5(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [5]\n\nprint(sort_by_frequency_5([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 5]\nprint(sort_by_frequency_5([2, 2, 1]))  # Expected: [2, 2, 1, 5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7242(values):\n    return sort_by_frequency_5(values)\n\n# Example 3: static method approach\nclass Problem7242Solution:\n    @staticmethod\n    def sort_by_frequency_5(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [5]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_5([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_5([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7243,
    "title": "Problem 7243",
    "description": "Write a Python function called `sort_by_frequency_6` that must sort values by descending frequency then numeric value and append 6. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_6([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 6]\n  sort_by_frequency_6([2, 2, 1]) -> [2, 2, 1, 6]",
    "initialCode": "def sort_by_frequency_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_6(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [6]\n\nprint(sort_by_frequency_6([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 6]\nprint(sort_by_frequency_6([2, 2, 1]))  # Expected: [2, 2, 1, 6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7243(values):\n    return sort_by_frequency_6(values)\n\n# Example 3: static method approach\nclass Problem7243Solution:\n    @staticmethod\n    def sort_by_frequency_6(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [6]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_6([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_6([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7244,
    "title": "Problem 7244",
    "description": "Write a Python function called `sort_by_frequency_7` that must sort values by descending frequency then numeric value and append 7. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_7([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 7]\n  sort_by_frequency_7([2, 2, 1]) -> [2, 2, 1, 7]",
    "initialCode": "def sort_by_frequency_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_7(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [7]\n\nprint(sort_by_frequency_7([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 7]\nprint(sort_by_frequency_7([2, 2, 1]))  # Expected: [2, 2, 1, 7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7244(values):\n    return sort_by_frequency_7(values)\n\n# Example 3: static method approach\nclass Problem7244Solution:\n    @staticmethod\n    def sort_by_frequency_7(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [7]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_7([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_7([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7245,
    "title": "Problem 7245",
    "description": "Write a Python function called `sort_by_frequency_8` that must sort values by descending frequency then numeric value and append 8. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_8([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 8]\n  sort_by_frequency_8([2, 2, 1]) -> [2, 2, 1, 8]",
    "initialCode": "def sort_by_frequency_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_8(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [8]\n\nprint(sort_by_frequency_8([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 8]\nprint(sort_by_frequency_8([2, 2, 1]))  # Expected: [2, 2, 1, 8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7245(values):\n    return sort_by_frequency_8(values)\n\n# Example 3: static method approach\nclass Problem7245Solution:\n    @staticmethod\n    def sort_by_frequency_8(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [8]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_8([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_8([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7246,
    "title": "Problem 7246",
    "description": "Write a Python function called `sort_by_frequency_9` that must sort values by descending frequency then numeric value and append 9. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_9([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 9]\n  sort_by_frequency_9([2, 2, 1]) -> [2, 2, 1, 9]",
    "initialCode": "def sort_by_frequency_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_9(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [9]\n\nprint(sort_by_frequency_9([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 9]\nprint(sort_by_frequency_9([2, 2, 1]))  # Expected: [2, 2, 1, 9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7246(values):\n    return sort_by_frequency_9(values)\n\n# Example 3: static method approach\nclass Problem7246Solution:\n    @staticmethod\n    def sort_by_frequency_9(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [9]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_9([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_9([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7247,
    "title": "Problem 7247",
    "description": "Write a Python function called `sort_by_frequency_10` that must sort values by descending frequency then numeric value and append 10. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_frequency_10([3, 1, 3, 2, 1, 3]) -> [3, 3, 3, 1, 1, 2, 10]\n  sort_by_frequency_10([2, 2, 1]) -> [2, 2, 1, 10]",
    "initialCode": "def sort_by_frequency_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_frequency_10(values):\n    counts = {value: values.count(value) for value in set(values)}\n    return sorted(values, key=lambda value: (-counts[value], value)) + [10]\n\nprint(sort_by_frequency_10([3, 1, 3, 2, 1, 3]))  # Expected: [3, 3, 3, 1, 1, 2, 10]\nprint(sort_by_frequency_10([2, 2, 1]))  # Expected: [2, 2, 1, 10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7247(values):\n    return sort_by_frequency_10(values)\n\n# Example 3: static method approach\nclass Problem7247Solution:\n    @staticmethod\n    def sort_by_frequency_10(values):\n        counts = {value: values.count(value) for value in set(values)}\n        return sorted(values, key=lambda value: (-counts[value], value)) + [10]\n\n# Example 4: assigned result approach\nresult = sort_by_frequency_10([3, 1, 3, 2, 1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_frequency_10([]))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7248,
    "title": "Problem 7248",
    "description": "Write a Python function called `sort_by_modulo_1` that must sort values by remainder, quotient, then value and append 1. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_1([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 1]\n  sort_by_modulo_1([10, -1, 4], 4) -> [4, 10, -1, 1]",
    "initialCode": "def sort_by_modulo_1(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_1(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [1]\n\nprint(sort_by_modulo_1([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 1]\nprint(sort_by_modulo_1([10, -1, 4], 4))  # Expected: [4, 10, -1, 1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7248(values, divisor):\n    return sort_by_modulo_1(values, divisor)\n\n# Example 3: static method approach\nclass Problem7248Solution:\n    @staticmethod\n    def sort_by_modulo_1(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [1]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_1([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_1([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7249,
    "title": "Problem 7249",
    "description": "Write a Python function called `sort_by_modulo_2` that must sort values by remainder, quotient, then value and append 2. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_2([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 2]\n  sort_by_modulo_2([10, -1, 4], 4) -> [4, 10, -1, 2]",
    "initialCode": "def sort_by_modulo_2(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_2(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [2]\n\nprint(sort_by_modulo_2([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 2]\nprint(sort_by_modulo_2([10, -1, 4], 4))  # Expected: [4, 10, -1, 2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7249(values, divisor):\n    return sort_by_modulo_2(values, divisor)\n\n# Example 3: static method approach\nclass Problem7249Solution:\n    @staticmethod\n    def sort_by_modulo_2(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [2]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_2([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_2([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7250,
    "title": "Problem 7250",
    "description": "Write a Python function called `sort_by_modulo_3` that must sort values by remainder, quotient, then value and append 3. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_3([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 3]\n  sort_by_modulo_3([10, -1, 4], 4) -> [4, 10, -1, 3]",
    "initialCode": "def sort_by_modulo_3(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_3(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [3]\n\nprint(sort_by_modulo_3([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 3]\nprint(sort_by_modulo_3([10, -1, 4], 4))  # Expected: [4, 10, -1, 3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7250(values, divisor):\n    return sort_by_modulo_3(values, divisor)\n\n# Example 3: static method approach\nclass Problem7250Solution:\n    @staticmethod\n    def sort_by_modulo_3(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [3]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_3([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_3([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7251,
    "title": "Problem 7251",
    "description": "Write a Python function called `sort_by_modulo_4` that must sort values by remainder, quotient, then value and append 4. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_4([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 4]\n  sort_by_modulo_4([10, -1, 4], 4) -> [4, 10, -1, 4]",
    "initialCode": "def sort_by_modulo_4(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_4(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [4]\n\nprint(sort_by_modulo_4([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 4]\nprint(sort_by_modulo_4([10, -1, 4], 4))  # Expected: [4, 10, -1, 4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7251(values, divisor):\n    return sort_by_modulo_4(values, divisor)\n\n# Example 3: static method approach\nclass Problem7251Solution:\n    @staticmethod\n    def sort_by_modulo_4(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [4]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_4([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_4([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7252,
    "title": "Problem 7252",
    "description": "Write a Python function called `sort_by_modulo_5` that must sort values by remainder, quotient, then value and append 5. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_5([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 5]\n  sort_by_modulo_5([10, -1, 4], 4) -> [4, 10, -1, 5]",
    "initialCode": "def sort_by_modulo_5(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_5(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [5]\n\nprint(sort_by_modulo_5([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 5]\nprint(sort_by_modulo_5([10, -1, 4], 4))  # Expected: [4, 10, -1, 5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7252(values, divisor):\n    return sort_by_modulo_5(values, divisor)\n\n# Example 3: static method approach\nclass Problem7252Solution:\n    @staticmethod\n    def sort_by_modulo_5(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [5]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_5([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_5([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7253,
    "title": "Problem 7253",
    "description": "Write a Python function called `sort_by_modulo_6` that must sort values by remainder, quotient, then value and append 6. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_6([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 6]\n  sort_by_modulo_6([10, -1, 4], 4) -> [4, 10, -1, 6]",
    "initialCode": "def sort_by_modulo_6(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_6(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [6]\n\nprint(sort_by_modulo_6([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 6]\nprint(sort_by_modulo_6([10, -1, 4], 4))  # Expected: [4, 10, -1, 6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7253(values, divisor):\n    return sort_by_modulo_6(values, divisor)\n\n# Example 3: static method approach\nclass Problem7253Solution:\n    @staticmethod\n    def sort_by_modulo_6(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [6]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_6([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_6([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7254,
    "title": "Problem 7254",
    "description": "Write a Python function called `sort_by_modulo_7` that must sort values by remainder, quotient, then value and append 7. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_7([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 7]\n  sort_by_modulo_7([10, -1, 4], 4) -> [4, 10, -1, 7]",
    "initialCode": "def sort_by_modulo_7(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_7(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [7]\n\nprint(sort_by_modulo_7([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 7]\nprint(sort_by_modulo_7([10, -1, 4], 4))  # Expected: [4, 10, -1, 7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7254(values, divisor):\n    return sort_by_modulo_7(values, divisor)\n\n# Example 3: static method approach\nclass Problem7254Solution:\n    @staticmethod\n    def sort_by_modulo_7(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [7]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_7([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_7([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7255,
    "title": "Problem 7255",
    "description": "Write a Python function called `sort_by_modulo_8` that must sort values by remainder, quotient, then value and append 8. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_8([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 8]\n  sort_by_modulo_8([10, -1, 4], 4) -> [4, 10, -1, 8]",
    "initialCode": "def sort_by_modulo_8(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_8(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [8]\n\nprint(sort_by_modulo_8([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 8]\nprint(sort_by_modulo_8([10, -1, 4], 4))  # Expected: [4, 10, -1, 8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7255(values, divisor):\n    return sort_by_modulo_8(values, divisor)\n\n# Example 3: static method approach\nclass Problem7255Solution:\n    @staticmethod\n    def sort_by_modulo_8(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [8]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_8([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_8([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7256,
    "title": "Problem 7256",
    "description": "Write a Python function called `sort_by_modulo_9` that must sort values by remainder, quotient, then value and append 9. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_9([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 9]\n  sort_by_modulo_9([10, -1, 4], 4) -> [4, 10, -1, 9]",
    "initialCode": "def sort_by_modulo_9(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_9(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [9]\n\nprint(sort_by_modulo_9([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 9]\nprint(sort_by_modulo_9([10, -1, 4], 4))  # Expected: [4, 10, -1, 9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7256(values, divisor):\n    return sort_by_modulo_9(values, divisor)\n\n# Example 3: static method approach\nclass Problem7256Solution:\n    @staticmethod\n    def sort_by_modulo_9(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [9]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_9([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_9([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7257,
    "title": "Problem 7257",
    "description": "Write a Python function called `sort_by_modulo_10` that must sort values by remainder, quotient, then value and append 10. Practice sorting key.\nDifficulty: Expert.\nExamples:\n  sort_by_modulo_10([8, 3, 5, 2], 3) -> [3, 2, 5, 8, 10]\n  sort_by_modulo_10([10, -1, 4], 4) -> [4, 10, -1, 10]",
    "initialCode": "def sort_by_modulo_10(values, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sort_by_modulo_10(values, divisor):\n    return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [10]\n\nprint(sort_by_modulo_10([8, 3, 5, 2], 3))  # Expected: [3, 2, 5, 8, 10]\nprint(sort_by_modulo_10([10, -1, 4], 4))  # Expected: [4, 10, -1, 10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7257(values, divisor):\n    return sort_by_modulo_10(values, divisor)\n\n# Example 3: static method approach\nclass Problem7257Solution:\n    @staticmethod\n    def sort_by_modulo_10(values, divisor):\n        return sorted(values, key=lambda value: (value % divisor, value // divisor, value)) + [10]\n\n# Example 4: assigned result approach\nresult = sort_by_modulo_10([8, 3, 5, 2], 3)\nprint(result)\n\n# Example 5: boundary case\nprint(sort_by_modulo_10([], 2))",
    "hint": "Focus on the key tuple, ascending versus descending fields, tie breakers, and stable ordering. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required sorting key rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Sorting Key Difficult"
  },
  {
    "id": 7258,
    "title": "Problem 7258",
    "description": "Write a Python function called `compare_test_outputs_1` that must return per-item equality results and append test marker 1. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_1([1, 2], [1, 3]) -> [True, False, 1]\n  compare_test_outputs_1([], []) -> [1]",
    "initialCode": "def compare_test_outputs_1(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_1(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [1]\n\nprint(compare_test_outputs_1([1, 2], [1, 3]))  # Expected: [True, False, 1]\nprint(compare_test_outputs_1([], []))  # Expected: [1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7258(actual, expected):\n    return compare_test_outputs_1(actual, expected)\n\n# Example 3: static method approach\nclass Problem7258Solution:\n    @staticmethod\n    def compare_test_outputs_1(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [1]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_1([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_1([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7259,
    "title": "Problem 7259",
    "description": "Write a Python function called `compare_test_outputs_2` that must return per-item equality results and append test marker 2. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_2([1, 2], [1, 3]) -> [True, False, 2]\n  compare_test_outputs_2([], []) -> [2]",
    "initialCode": "def compare_test_outputs_2(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_2(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [2]\n\nprint(compare_test_outputs_2([1, 2], [1, 3]))  # Expected: [True, False, 2]\nprint(compare_test_outputs_2([], []))  # Expected: [2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7259(actual, expected):\n    return compare_test_outputs_2(actual, expected)\n\n# Example 3: static method approach\nclass Problem7259Solution:\n    @staticmethod\n    def compare_test_outputs_2(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [2]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_2([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_2([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7260,
    "title": "Problem 7260",
    "description": "Write a Python function called `compare_test_outputs_3` that must return per-item equality results and append test marker 3. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_3([1, 2], [1, 3]) -> [True, False, 3]\n  compare_test_outputs_3([], []) -> [3]",
    "initialCode": "def compare_test_outputs_3(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_3(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [3]\n\nprint(compare_test_outputs_3([1, 2], [1, 3]))  # Expected: [True, False, 3]\nprint(compare_test_outputs_3([], []))  # Expected: [3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7260(actual, expected):\n    return compare_test_outputs_3(actual, expected)\n\n# Example 3: static method approach\nclass Problem7260Solution:\n    @staticmethod\n    def compare_test_outputs_3(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [3]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_3([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_3([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7261,
    "title": "Problem 7261",
    "description": "Write a Python function called `compare_test_outputs_4` that must return per-item equality results and append test marker 4. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_4([1, 2], [1, 3]) -> [True, False, 4]\n  compare_test_outputs_4([], []) -> [4]",
    "initialCode": "def compare_test_outputs_4(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_4(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [4]\n\nprint(compare_test_outputs_4([1, 2], [1, 3]))  # Expected: [True, False, 4]\nprint(compare_test_outputs_4([], []))  # Expected: [4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7261(actual, expected):\n    return compare_test_outputs_4(actual, expected)\n\n# Example 3: static method approach\nclass Problem7261Solution:\n    @staticmethod\n    def compare_test_outputs_4(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [4]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_4([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_4([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7262,
    "title": "Problem 7262",
    "description": "Write a Python function called `compare_test_outputs_5` that must return per-item equality results and append test marker 5. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_5([1, 2], [1, 3]) -> [True, False, 5]\n  compare_test_outputs_5([], []) -> [5]",
    "initialCode": "def compare_test_outputs_5(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_5(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [5]\n\nprint(compare_test_outputs_5([1, 2], [1, 3]))  # Expected: [True, False, 5]\nprint(compare_test_outputs_5([], []))  # Expected: [5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7262(actual, expected):\n    return compare_test_outputs_5(actual, expected)\n\n# Example 3: static method approach\nclass Problem7262Solution:\n    @staticmethod\n    def compare_test_outputs_5(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [5]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_5([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_5([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7263,
    "title": "Problem 7263",
    "description": "Write a Python function called `compare_test_outputs_6` that must return per-item equality results and append test marker 6. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_6([1, 2], [1, 3]) -> [True, False, 6]\n  compare_test_outputs_6([], []) -> [6]",
    "initialCode": "def compare_test_outputs_6(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_6(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [6]\n\nprint(compare_test_outputs_6([1, 2], [1, 3]))  # Expected: [True, False, 6]\nprint(compare_test_outputs_6([], []))  # Expected: [6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7263(actual, expected):\n    return compare_test_outputs_6(actual, expected)\n\n# Example 3: static method approach\nclass Problem7263Solution:\n    @staticmethod\n    def compare_test_outputs_6(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [6]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_6([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_6([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7264,
    "title": "Problem 7264",
    "description": "Write a Python function called `compare_test_outputs_7` that must return per-item equality results and append test marker 7. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_7([1, 2], [1, 3]) -> [True, False, 7]\n  compare_test_outputs_7([], []) -> [7]",
    "initialCode": "def compare_test_outputs_7(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_7(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [7]\n\nprint(compare_test_outputs_7([1, 2], [1, 3]))  # Expected: [True, False, 7]\nprint(compare_test_outputs_7([], []))  # Expected: [7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7264(actual, expected):\n    return compare_test_outputs_7(actual, expected)\n\n# Example 3: static method approach\nclass Problem7264Solution:\n    @staticmethod\n    def compare_test_outputs_7(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [7]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_7([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_7([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7265,
    "title": "Problem 7265",
    "description": "Write a Python function called `compare_test_outputs_8` that must return per-item equality results and append test marker 8. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_8([1, 2], [1, 3]) -> [True, False, 8]\n  compare_test_outputs_8([], []) -> [8]",
    "initialCode": "def compare_test_outputs_8(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_8(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [8]\n\nprint(compare_test_outputs_8([1, 2], [1, 3]))  # Expected: [True, False, 8]\nprint(compare_test_outputs_8([], []))  # Expected: [8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7265(actual, expected):\n    return compare_test_outputs_8(actual, expected)\n\n# Example 3: static method approach\nclass Problem7265Solution:\n    @staticmethod\n    def compare_test_outputs_8(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [8]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_8([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_8([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7266,
    "title": "Problem 7266",
    "description": "Write a Python function called `compare_test_outputs_9` that must return per-item equality results and append test marker 9. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_9([1, 2], [1, 3]) -> [True, False, 9]\n  compare_test_outputs_9([], []) -> [9]",
    "initialCode": "def compare_test_outputs_9(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_9(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [9]\n\nprint(compare_test_outputs_9([1, 2], [1, 3]))  # Expected: [True, False, 9]\nprint(compare_test_outputs_9([], []))  # Expected: [9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7266(actual, expected):\n    return compare_test_outputs_9(actual, expected)\n\n# Example 3: static method approach\nclass Problem7266Solution:\n    @staticmethod\n    def compare_test_outputs_9(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [9]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_9([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_9([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7267,
    "title": "Problem 7267",
    "description": "Write a Python function called `compare_test_outputs_10` that must return per-item equality results and append test marker 10. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  compare_test_outputs_10([1, 2], [1, 3]) -> [True, False, 10]\n  compare_test_outputs_10([], []) -> [10]",
    "initialCode": "def compare_test_outputs_10(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef compare_test_outputs_10(actual, expected):\n    assert isinstance(actual, list) and isinstance(expected, list)\n    return [left == right for left, right in zip(actual, expected)] + [10]\n\nprint(compare_test_outputs_10([1, 2], [1, 3]))  # Expected: [True, False, 10]\nprint(compare_test_outputs_10([], []))  # Expected: [10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7267(actual, expected):\n    return compare_test_outputs_10(actual, expected)\n\n# Example 3: static method approach\nclass Problem7267Solution:\n    @staticmethod\n    def compare_test_outputs_10(actual, expected):\n        assert isinstance(actual, list) and isinstance(expected, list)\n        return [left == right for left, right in zip(actual, expected)] + [10]\n\n# Example 4: assigned result approach\nresult = compare_test_outputs_10([1, 2], [1, 3])\nprint(result)\n\n# Example 5: boundary case\nprint(compare_test_outputs_10([\"a\"], [\"a\"]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7268,
    "title": "Problem 7268",
    "description": "Write a Python function called `first_test_failure_1` that must return the first mismatching index plus 1, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_1([1, 9], [1, 2]) -> 2\n  first_test_failure_1([1], [1]) -> -1",
    "initialCode": "def first_test_failure_1(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_1(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 1\n    return -1\n\nprint(first_test_failure_1([1, 9], [1, 2]))  # Expected: 2\nprint(first_test_failure_1([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7268(actual, expected):\n    return first_test_failure_1(actual, expected)\n\n# Example 3: static method approach\nclass Problem7268Solution:\n    @staticmethod\n    def first_test_failure_1(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 1\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_1([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_1([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7269,
    "title": "Problem 7269",
    "description": "Write a Python function called `first_test_failure_2` that must return the first mismatching index plus 2, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_2([1, 9], [1, 2]) -> 3\n  first_test_failure_2([1], [1]) -> -1",
    "initialCode": "def first_test_failure_2(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_2(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 2\n    return -1\n\nprint(first_test_failure_2([1, 9], [1, 2]))  # Expected: 3\nprint(first_test_failure_2([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7269(actual, expected):\n    return first_test_failure_2(actual, expected)\n\n# Example 3: static method approach\nclass Problem7269Solution:\n    @staticmethod\n    def first_test_failure_2(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 2\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_2([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_2([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7270,
    "title": "Problem 7270",
    "description": "Write a Python function called `first_test_failure_3` that must return the first mismatching index plus 3, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_3([1, 9], [1, 2]) -> 4\n  first_test_failure_3([1], [1]) -> -1",
    "initialCode": "def first_test_failure_3(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_3(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 3\n    return -1\n\nprint(first_test_failure_3([1, 9], [1, 2]))  # Expected: 4\nprint(first_test_failure_3([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7270(actual, expected):\n    return first_test_failure_3(actual, expected)\n\n# Example 3: static method approach\nclass Problem7270Solution:\n    @staticmethod\n    def first_test_failure_3(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 3\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_3([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_3([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7271,
    "title": "Problem 7271",
    "description": "Write a Python function called `first_test_failure_4` that must return the first mismatching index plus 4, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_4([1, 9], [1, 2]) -> 5\n  first_test_failure_4([1], [1]) -> -1",
    "initialCode": "def first_test_failure_4(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_4(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 4\n    return -1\n\nprint(first_test_failure_4([1, 9], [1, 2]))  # Expected: 5\nprint(first_test_failure_4([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7271(actual, expected):\n    return first_test_failure_4(actual, expected)\n\n# Example 3: static method approach\nclass Problem7271Solution:\n    @staticmethod\n    def first_test_failure_4(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 4\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_4([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_4([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7272,
    "title": "Problem 7272",
    "description": "Write a Python function called `first_test_failure_5` that must return the first mismatching index plus 5, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_5([1, 9], [1, 2]) -> 6\n  first_test_failure_5([1], [1]) -> -1",
    "initialCode": "def first_test_failure_5(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_5(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 5\n    return -1\n\nprint(first_test_failure_5([1, 9], [1, 2]))  # Expected: 6\nprint(first_test_failure_5([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7272(actual, expected):\n    return first_test_failure_5(actual, expected)\n\n# Example 3: static method approach\nclass Problem7272Solution:\n    @staticmethod\n    def first_test_failure_5(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 5\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_5([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_5([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7273,
    "title": "Problem 7273",
    "description": "Write a Python function called `first_test_failure_6` that must return the first mismatching index plus 6, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_6([1, 9], [1, 2]) -> 7\n  first_test_failure_6([1], [1]) -> -1",
    "initialCode": "def first_test_failure_6(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_6(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 6\n    return -1\n\nprint(first_test_failure_6([1, 9], [1, 2]))  # Expected: 7\nprint(first_test_failure_6([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7273(actual, expected):\n    return first_test_failure_6(actual, expected)\n\n# Example 3: static method approach\nclass Problem7273Solution:\n    @staticmethod\n    def first_test_failure_6(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 6\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_6([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_6([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7274,
    "title": "Problem 7274",
    "description": "Write a Python function called `first_test_failure_7` that must return the first mismatching index plus 7, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_7([1, 9], [1, 2]) -> 8\n  first_test_failure_7([1], [1]) -> -1",
    "initialCode": "def first_test_failure_7(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_7(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 7\n    return -1\n\nprint(first_test_failure_7([1, 9], [1, 2]))  # Expected: 8\nprint(first_test_failure_7([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7274(actual, expected):\n    return first_test_failure_7(actual, expected)\n\n# Example 3: static method approach\nclass Problem7274Solution:\n    @staticmethod\n    def first_test_failure_7(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 7\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_7([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_7([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7275,
    "title": "Problem 7275",
    "description": "Write a Python function called `first_test_failure_8` that must return the first mismatching index plus 8, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_8([1, 9], [1, 2]) -> 9\n  first_test_failure_8([1], [1]) -> -1",
    "initialCode": "def first_test_failure_8(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_8(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 8\n    return -1\n\nprint(first_test_failure_8([1, 9], [1, 2]))  # Expected: 9\nprint(first_test_failure_8([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7275(actual, expected):\n    return first_test_failure_8(actual, expected)\n\n# Example 3: static method approach\nclass Problem7275Solution:\n    @staticmethod\n    def first_test_failure_8(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 8\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_8([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_8([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7276,
    "title": "Problem 7276",
    "description": "Write a Python function called `first_test_failure_9` that must return the first mismatching index plus 9, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_9([1, 9], [1, 2]) -> 10\n  first_test_failure_9([1], [1]) -> -1",
    "initialCode": "def first_test_failure_9(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_9(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 9\n    return -1\n\nprint(first_test_failure_9([1, 9], [1, 2]))  # Expected: 10\nprint(first_test_failure_9([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7276(actual, expected):\n    return first_test_failure_9(actual, expected)\n\n# Example 3: static method approach\nclass Problem7276Solution:\n    @staticmethod\n    def first_test_failure_9(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 9\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_9([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_9([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7277,
    "title": "Problem 7277",
    "description": "Write a Python function called `first_test_failure_10` that must return the first mismatching index plus 10, or -1 when all tested values match. Practice testing & debugging.\nDifficulty: Easy.\nExamples:\n  first_test_failure_10([1, 9], [1, 2]) -> 11\n  first_test_failure_10([1], [1]) -> -1",
    "initialCode": "def first_test_failure_10(actual, expected):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef first_test_failure_10(actual, expected):\n    assert len(actual) == len(expected)\n    for index, (left, right) in enumerate(zip(actual, expected)):\n        if left != right:\n            return index + 10\n    return -1\n\nprint(first_test_failure_10([1, 9], [1, 2]))  # Expected: 11\nprint(first_test_failure_10([1], [1]))  # Expected: -1\n\n# Example 2: named wrapper approach\ndef solve_problem_7277(actual, expected):\n    return first_test_failure_10(actual, expected)\n\n# Example 3: static method approach\nclass Problem7277Solution:\n    @staticmethod\n    def first_test_failure_10(actual, expected):\n        assert len(actual) == len(expected)\n        for index, (left, right) in enumerate(zip(actual, expected)):\n            if left != right:\n                return index + 10\n        return -1\n\n# Example 4: assigned result approach\nresult = first_test_failure_10([1, 9], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(first_test_failure_10([], []))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Easy"
  },
  {
    "id": 7278,
    "title": "Problem 7278",
    "description": "Write a Python function called `approximately_equal_1` that must test whether two numbers differ by at most 1 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_1(1, 1.0005) -> True\n  approximately_equal_1(1, 1.002) -> False",
    "initialCode": "import math\n\ndef approximately_equal_1(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_1(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=1 / 1000)\n\nprint(approximately_equal_1(1, 1.0005))  # Expected: True\nprint(approximately_equal_1(1, 1.002))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7278(left, right):\n    return approximately_equal_1(left, right)\n\n# Example 3: static method approach\nclass Problem7278Solution:\n    @staticmethod\n    def approximately_equal_1(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=1 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_1(1, 1.0005)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_1(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7279,
    "title": "Problem 7279",
    "description": "Write a Python function called `approximately_equal_2` that must test whether two numbers differ by at most 2 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_2(1, 1.001) -> True\n  approximately_equal_2(1, 1.004) -> False",
    "initialCode": "import math\n\ndef approximately_equal_2(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_2(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=2 / 1000)\n\nprint(approximately_equal_2(1, 1.001))  # Expected: True\nprint(approximately_equal_2(1, 1.004))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7279(left, right):\n    return approximately_equal_2(left, right)\n\n# Example 3: static method approach\nclass Problem7279Solution:\n    @staticmethod\n    def approximately_equal_2(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=2 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_2(1, 1.001)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_2(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7280,
    "title": "Problem 7280",
    "description": "Write a Python function called `approximately_equal_3` that must test whether two numbers differ by at most 3 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_3(1, 1.0015) -> True\n  approximately_equal_3(1, 1.006) -> False",
    "initialCode": "import math\n\ndef approximately_equal_3(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_3(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=3 / 1000)\n\nprint(approximately_equal_3(1, 1.0015))  # Expected: True\nprint(approximately_equal_3(1, 1.006))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7280(left, right):\n    return approximately_equal_3(left, right)\n\n# Example 3: static method approach\nclass Problem7280Solution:\n    @staticmethod\n    def approximately_equal_3(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=3 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_3(1, 1.0015)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_3(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7281,
    "title": "Problem 7281",
    "description": "Write a Python function called `approximately_equal_4` that must test whether two numbers differ by at most 4 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_4(1, 1.002) -> True\n  approximately_equal_4(1, 1.008) -> False",
    "initialCode": "import math\n\ndef approximately_equal_4(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_4(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=4 / 1000)\n\nprint(approximately_equal_4(1, 1.002))  # Expected: True\nprint(approximately_equal_4(1, 1.008))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7281(left, right):\n    return approximately_equal_4(left, right)\n\n# Example 3: static method approach\nclass Problem7281Solution:\n    @staticmethod\n    def approximately_equal_4(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=4 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_4(1, 1.002)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_4(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7282,
    "title": "Problem 7282",
    "description": "Write a Python function called `approximately_equal_5` that must test whether two numbers differ by at most 5 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_5(1, 1.0025) -> True\n  approximately_equal_5(1, 1.01) -> False",
    "initialCode": "import math\n\ndef approximately_equal_5(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_5(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=5 / 1000)\n\nprint(approximately_equal_5(1, 1.0025))  # Expected: True\nprint(approximately_equal_5(1, 1.01))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7282(left, right):\n    return approximately_equal_5(left, right)\n\n# Example 3: static method approach\nclass Problem7282Solution:\n    @staticmethod\n    def approximately_equal_5(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=5 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_5(1, 1.0025)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_5(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7283,
    "title": "Problem 7283",
    "description": "Write a Python function called `approximately_equal_6` that must test whether two numbers differ by at most 6 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_6(1, 1.003) -> True\n  approximately_equal_6(1, 1.012) -> False",
    "initialCode": "import math\n\ndef approximately_equal_6(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_6(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=6 / 1000)\n\nprint(approximately_equal_6(1, 1.003))  # Expected: True\nprint(approximately_equal_6(1, 1.012))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7283(left, right):\n    return approximately_equal_6(left, right)\n\n# Example 3: static method approach\nclass Problem7283Solution:\n    @staticmethod\n    def approximately_equal_6(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=6 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_6(1, 1.003)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_6(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7284,
    "title": "Problem 7284",
    "description": "Write a Python function called `approximately_equal_7` that must test whether two numbers differ by at most 7 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_7(1, 1.0035) -> True\n  approximately_equal_7(1, 1.014) -> False",
    "initialCode": "import math\n\ndef approximately_equal_7(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_7(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=7 / 1000)\n\nprint(approximately_equal_7(1, 1.0035))  # Expected: True\nprint(approximately_equal_7(1, 1.014))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7284(left, right):\n    return approximately_equal_7(left, right)\n\n# Example 3: static method approach\nclass Problem7284Solution:\n    @staticmethod\n    def approximately_equal_7(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=7 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_7(1, 1.0035)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_7(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7285,
    "title": "Problem 7285",
    "description": "Write a Python function called `approximately_equal_8` that must test whether two numbers differ by at most 8 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_8(1, 1.004) -> True\n  approximately_equal_8(1, 1.016) -> False",
    "initialCode": "import math\n\ndef approximately_equal_8(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_8(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=8 / 1000)\n\nprint(approximately_equal_8(1, 1.004))  # Expected: True\nprint(approximately_equal_8(1, 1.016))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7285(left, right):\n    return approximately_equal_8(left, right)\n\n# Example 3: static method approach\nclass Problem7285Solution:\n    @staticmethod\n    def approximately_equal_8(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=8 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_8(1, 1.004)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_8(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7286,
    "title": "Problem 7286",
    "description": "Write a Python function called `approximately_equal_9` that must test whether two numbers differ by at most 9 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_9(1, 1.0045) -> True\n  approximately_equal_9(1, 1.018) -> False",
    "initialCode": "import math\n\ndef approximately_equal_9(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_9(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=9 / 1000)\n\nprint(approximately_equal_9(1, 1.0045))  # Expected: True\nprint(approximately_equal_9(1, 1.018))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7286(left, right):\n    return approximately_equal_9(left, right)\n\n# Example 3: static method approach\nclass Problem7286Solution:\n    @staticmethod\n    def approximately_equal_9(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=9 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_9(1, 1.0045)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_9(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7287,
    "title": "Problem 7287",
    "description": "Write a Python function called `approximately_equal_10` that must test whether two numbers differ by at most 10 thousandth(s). Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  approximately_equal_10(1, 1.005) -> True\n  approximately_equal_10(1, 1.02) -> False",
    "initialCode": "import math\n\ndef approximately_equal_10(left, right):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef approximately_equal_10(left, right):\n    assert isinstance(left, (int, float))\n    return math.isclose(left, right, rel_tol=0.0, abs_tol=10 / 1000)\n\nprint(approximately_equal_10(1, 1.005))  # Expected: True\nprint(approximately_equal_10(1, 1.02))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7287(left, right):\n    return approximately_equal_10(left, right)\n\n# Example 3: static method approach\nclass Problem7287Solution:\n    @staticmethod\n    def approximately_equal_10(left, right):\n        assert isinstance(left, (int, float))\n        return math.isclose(left, right, rel_tol=0.0, abs_tol=10 / 1000)\n\n# Example 4: assigned result approach\nresult = approximately_equal_10(1, 1.005)\nprint(result)\n\n# Example 5: boundary case\nprint(approximately_equal_10(-2, -2))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7288,
    "title": "Problem 7288",
    "description": "Write a Python function called `count_passing_cases_1` that must count values meeting the minimum and add 1 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_1([1, 5, 7], 5) -> 3\n  count_passing_cases_1([], 0) -> 1",
    "initialCode": "def count_passing_cases_1(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_1(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 1\n\nprint(count_passing_cases_1([1, 5, 7], 5))  # Expected: 3\nprint(count_passing_cases_1([], 0))  # Expected: 1\n\n# Example 2: named wrapper approach\ndef solve_problem_7288(values, minimum):\n    return count_passing_cases_1(values, minimum)\n\n# Example 3: static method approach\nclass Problem7288Solution:\n    @staticmethod\n    def count_passing_cases_1(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 1\n\n# Example 4: assigned result approach\nresult = count_passing_cases_1([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_1([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7289,
    "title": "Problem 7289",
    "description": "Write a Python function called `count_passing_cases_2` that must count values meeting the minimum and add 2 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_2([1, 5, 7], 5) -> 4\n  count_passing_cases_2([], 0) -> 2",
    "initialCode": "def count_passing_cases_2(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_2(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 2\n\nprint(count_passing_cases_2([1, 5, 7], 5))  # Expected: 4\nprint(count_passing_cases_2([], 0))  # Expected: 2\n\n# Example 2: named wrapper approach\ndef solve_problem_7289(values, minimum):\n    return count_passing_cases_2(values, minimum)\n\n# Example 3: static method approach\nclass Problem7289Solution:\n    @staticmethod\n    def count_passing_cases_2(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 2\n\n# Example 4: assigned result approach\nresult = count_passing_cases_2([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_2([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7290,
    "title": "Problem 7290",
    "description": "Write a Python function called `count_passing_cases_3` that must count values meeting the minimum and add 3 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_3([1, 5, 7], 5) -> 5\n  count_passing_cases_3([], 0) -> 3",
    "initialCode": "def count_passing_cases_3(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_3(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 3\n\nprint(count_passing_cases_3([1, 5, 7], 5))  # Expected: 5\nprint(count_passing_cases_3([], 0))  # Expected: 3\n\n# Example 2: named wrapper approach\ndef solve_problem_7290(values, minimum):\n    return count_passing_cases_3(values, minimum)\n\n# Example 3: static method approach\nclass Problem7290Solution:\n    @staticmethod\n    def count_passing_cases_3(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 3\n\n# Example 4: assigned result approach\nresult = count_passing_cases_3([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_3([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7291,
    "title": "Problem 7291",
    "description": "Write a Python function called `count_passing_cases_4` that must count values meeting the minimum and add 4 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_4([1, 5, 7], 5) -> 6\n  count_passing_cases_4([], 0) -> 4",
    "initialCode": "def count_passing_cases_4(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_4(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 4\n\nprint(count_passing_cases_4([1, 5, 7], 5))  # Expected: 6\nprint(count_passing_cases_4([], 0))  # Expected: 4\n\n# Example 2: named wrapper approach\ndef solve_problem_7291(values, minimum):\n    return count_passing_cases_4(values, minimum)\n\n# Example 3: static method approach\nclass Problem7291Solution:\n    @staticmethod\n    def count_passing_cases_4(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 4\n\n# Example 4: assigned result approach\nresult = count_passing_cases_4([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_4([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7292,
    "title": "Problem 7292",
    "description": "Write a Python function called `count_passing_cases_5` that must count values meeting the minimum and add 5 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_5([1, 5, 7], 5) -> 7\n  count_passing_cases_5([], 0) -> 5",
    "initialCode": "def count_passing_cases_5(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_5(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 5\n\nprint(count_passing_cases_5([1, 5, 7], 5))  # Expected: 7\nprint(count_passing_cases_5([], 0))  # Expected: 5\n\n# Example 2: named wrapper approach\ndef solve_problem_7292(values, minimum):\n    return count_passing_cases_5(values, minimum)\n\n# Example 3: static method approach\nclass Problem7292Solution:\n    @staticmethod\n    def count_passing_cases_5(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 5\n\n# Example 4: assigned result approach\nresult = count_passing_cases_5([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_5([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7293,
    "title": "Problem 7293",
    "description": "Write a Python function called `count_passing_cases_6` that must count values meeting the minimum and add 6 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_6([1, 5, 7], 5) -> 8\n  count_passing_cases_6([], 0) -> 6",
    "initialCode": "def count_passing_cases_6(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_6(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 6\n\nprint(count_passing_cases_6([1, 5, 7], 5))  # Expected: 8\nprint(count_passing_cases_6([], 0))  # Expected: 6\n\n# Example 2: named wrapper approach\ndef solve_problem_7293(values, minimum):\n    return count_passing_cases_6(values, minimum)\n\n# Example 3: static method approach\nclass Problem7293Solution:\n    @staticmethod\n    def count_passing_cases_6(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 6\n\n# Example 4: assigned result approach\nresult = count_passing_cases_6([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_6([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7294,
    "title": "Problem 7294",
    "description": "Write a Python function called `count_passing_cases_7` that must count values meeting the minimum and add 7 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_7([1, 5, 7], 5) -> 9\n  count_passing_cases_7([], 0) -> 7",
    "initialCode": "def count_passing_cases_7(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_7(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 7\n\nprint(count_passing_cases_7([1, 5, 7], 5))  # Expected: 9\nprint(count_passing_cases_7([], 0))  # Expected: 7\n\n# Example 2: named wrapper approach\ndef solve_problem_7294(values, minimum):\n    return count_passing_cases_7(values, minimum)\n\n# Example 3: static method approach\nclass Problem7294Solution:\n    @staticmethod\n    def count_passing_cases_7(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 7\n\n# Example 4: assigned result approach\nresult = count_passing_cases_7([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_7([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7295,
    "title": "Problem 7295",
    "description": "Write a Python function called `count_passing_cases_8` that must count values meeting the minimum and add 8 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_8([1, 5, 7], 5) -> 10\n  count_passing_cases_8([], 0) -> 8",
    "initialCode": "def count_passing_cases_8(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_8(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 8\n\nprint(count_passing_cases_8([1, 5, 7], 5))  # Expected: 10\nprint(count_passing_cases_8([], 0))  # Expected: 8\n\n# Example 2: named wrapper approach\ndef solve_problem_7295(values, minimum):\n    return count_passing_cases_8(values, minimum)\n\n# Example 3: static method approach\nclass Problem7295Solution:\n    @staticmethod\n    def count_passing_cases_8(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 8\n\n# Example 4: assigned result approach\nresult = count_passing_cases_8([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_8([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7296,
    "title": "Problem 7296",
    "description": "Write a Python function called `count_passing_cases_9` that must count values meeting the minimum and add 9 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_9([1, 5, 7], 5) -> 11\n  count_passing_cases_9([], 0) -> 9",
    "initialCode": "def count_passing_cases_9(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_9(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 9\n\nprint(count_passing_cases_9([1, 5, 7], 5))  # Expected: 11\nprint(count_passing_cases_9([], 0))  # Expected: 9\n\n# Example 2: named wrapper approach\ndef solve_problem_7296(values, minimum):\n    return count_passing_cases_9(values, minimum)\n\n# Example 3: static method approach\nclass Problem7296Solution:\n    @staticmethod\n    def count_passing_cases_9(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 9\n\n# Example 4: assigned result approach\nresult = count_passing_cases_9([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_9([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7297,
    "title": "Problem 7297",
    "description": "Write a Python function called `count_passing_cases_10` that must count values meeting the minimum and add 10 to the test count. Practice testing & debugging.\nDifficulty: Intermediate.\nExamples:\n  count_passing_cases_10([1, 5, 7], 5) -> 12\n  count_passing_cases_10([], 0) -> 10",
    "initialCode": "def count_passing_cases_10(values, minimum):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef count_passing_cases_10(values, minimum):\n    assert all(isinstance(value, (int, float)) for value in values)\n    return sum(value >= minimum for value in values) + 10\n\nprint(count_passing_cases_10([1, 5, 7], 5))  # Expected: 12\nprint(count_passing_cases_10([], 0))  # Expected: 10\n\n# Example 2: named wrapper approach\ndef solve_problem_7297(values, minimum):\n    return count_passing_cases_10(values, minimum)\n\n# Example 3: static method approach\nclass Problem7297Solution:\n    @staticmethod\n    def count_passing_cases_10(values, minimum):\n        assert all(isinstance(value, (int, float)) for value in values)\n        return sum(value >= minimum for value in values) + 10\n\n# Example 4: assigned result approach\nresult = count_passing_cases_10([1, 5, 7], 5)\nprint(result)\n\n# Example 5: boundary case\nprint(count_passing_cases_10([-2, 0], -1))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Intermediate"
  },
  {
    "id": 7298,
    "title": "Problem 7298",
    "description": "Write a Python function called `invalid_integer_positions_1` that must debug integer input by returning invalid positions followed by marker 1. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_1([\"1\", \"x\", \"3\"]) -> [1, 1]\n  invalid_integer_positions_1([\"-2\", \"0\"]) -> [1]",
    "initialCode": "def invalid_integer_positions_1(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_1(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [1]\n\nprint(invalid_integer_positions_1([\"1\", \"x\", \"3\"]))  # Expected: [1, 1]\nprint(invalid_integer_positions_1([\"-2\", \"0\"]))  # Expected: [1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7298(texts):\n    return invalid_integer_positions_1(texts)\n\n# Example 3: static method approach\nclass Problem7298Solution:\n    @staticmethod\n    def invalid_integer_positions_1(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [1]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_1([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_1([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7299,
    "title": "Problem 7299",
    "description": "Write a Python function called `invalid_integer_positions_2` that must debug integer input by returning invalid positions followed by marker 2. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_2([\"1\", \"x\", \"3\"]) -> [1, 2]\n  invalid_integer_positions_2([\"-2\", \"0\"]) -> [2]",
    "initialCode": "def invalid_integer_positions_2(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_2(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [2]\n\nprint(invalid_integer_positions_2([\"1\", \"x\", \"3\"]))  # Expected: [1, 2]\nprint(invalid_integer_positions_2([\"-2\", \"0\"]))  # Expected: [2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7299(texts):\n    return invalid_integer_positions_2(texts)\n\n# Example 3: static method approach\nclass Problem7299Solution:\n    @staticmethod\n    def invalid_integer_positions_2(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [2]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_2([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_2([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7300,
    "title": "Problem 7300",
    "description": "Write a Python function called `invalid_integer_positions_3` that must debug integer input by returning invalid positions followed by marker 3. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_3([\"1\", \"x\", \"3\"]) -> [1, 3]\n  invalid_integer_positions_3([\"-2\", \"0\"]) -> [3]",
    "initialCode": "def invalid_integer_positions_3(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_3(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [3]\n\nprint(invalid_integer_positions_3([\"1\", \"x\", \"3\"]))  # Expected: [1, 3]\nprint(invalid_integer_positions_3([\"-2\", \"0\"]))  # Expected: [3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7300(texts):\n    return invalid_integer_positions_3(texts)\n\n# Example 3: static method approach\nclass Problem7300Solution:\n    @staticmethod\n    def invalid_integer_positions_3(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [3]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_3([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_3([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7301,
    "title": "Problem 7301",
    "description": "Write a Python function called `invalid_integer_positions_4` that must debug integer input by returning invalid positions followed by marker 4. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_4([\"1\", \"x\", \"3\"]) -> [1, 4]\n  invalid_integer_positions_4([\"-2\", \"0\"]) -> [4]",
    "initialCode": "def invalid_integer_positions_4(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_4(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [4]\n\nprint(invalid_integer_positions_4([\"1\", \"x\", \"3\"]))  # Expected: [1, 4]\nprint(invalid_integer_positions_4([\"-2\", \"0\"]))  # Expected: [4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7301(texts):\n    return invalid_integer_positions_4(texts)\n\n# Example 3: static method approach\nclass Problem7301Solution:\n    @staticmethod\n    def invalid_integer_positions_4(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [4]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_4([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_4([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7302,
    "title": "Problem 7302",
    "description": "Write a Python function called `invalid_integer_positions_5` that must debug integer input by returning invalid positions followed by marker 5. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_5([\"1\", \"x\", \"3\"]) -> [1, 5]\n  invalid_integer_positions_5([\"-2\", \"0\"]) -> [5]",
    "initialCode": "def invalid_integer_positions_5(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_5(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [5]\n\nprint(invalid_integer_positions_5([\"1\", \"x\", \"3\"]))  # Expected: [1, 5]\nprint(invalid_integer_positions_5([\"-2\", \"0\"]))  # Expected: [5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7302(texts):\n    return invalid_integer_positions_5(texts)\n\n# Example 3: static method approach\nclass Problem7302Solution:\n    @staticmethod\n    def invalid_integer_positions_5(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [5]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_5([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_5([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7303,
    "title": "Problem 7303",
    "description": "Write a Python function called `invalid_integer_positions_6` that must debug integer input by returning invalid positions followed by marker 6. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_6([\"1\", \"x\", \"3\"]) -> [1, 6]\n  invalid_integer_positions_6([\"-2\", \"0\"]) -> [6]",
    "initialCode": "def invalid_integer_positions_6(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_6(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [6]\n\nprint(invalid_integer_positions_6([\"1\", \"x\", \"3\"]))  # Expected: [1, 6]\nprint(invalid_integer_positions_6([\"-2\", \"0\"]))  # Expected: [6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7303(texts):\n    return invalid_integer_positions_6(texts)\n\n# Example 3: static method approach\nclass Problem7303Solution:\n    @staticmethod\n    def invalid_integer_positions_6(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [6]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_6([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_6([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7304,
    "title": "Problem 7304",
    "description": "Write a Python function called `invalid_integer_positions_7` that must debug integer input by returning invalid positions followed by marker 7. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_7([\"1\", \"x\", \"3\"]) -> [1, 7]\n  invalid_integer_positions_7([\"-2\", \"0\"]) -> [7]",
    "initialCode": "def invalid_integer_positions_7(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_7(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [7]\n\nprint(invalid_integer_positions_7([\"1\", \"x\", \"3\"]))  # Expected: [1, 7]\nprint(invalid_integer_positions_7([\"-2\", \"0\"]))  # Expected: [7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7304(texts):\n    return invalid_integer_positions_7(texts)\n\n# Example 3: static method approach\nclass Problem7304Solution:\n    @staticmethod\n    def invalid_integer_positions_7(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [7]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_7([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_7([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7305,
    "title": "Problem 7305",
    "description": "Write a Python function called `invalid_integer_positions_8` that must debug integer input by returning invalid positions followed by marker 8. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_8([\"1\", \"x\", \"3\"]) -> [1, 8]\n  invalid_integer_positions_8([\"-2\", \"0\"]) -> [8]",
    "initialCode": "def invalid_integer_positions_8(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_8(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [8]\n\nprint(invalid_integer_positions_8([\"1\", \"x\", \"3\"]))  # Expected: [1, 8]\nprint(invalid_integer_positions_8([\"-2\", \"0\"]))  # Expected: [8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7305(texts):\n    return invalid_integer_positions_8(texts)\n\n# Example 3: static method approach\nclass Problem7305Solution:\n    @staticmethod\n    def invalid_integer_positions_8(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [8]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_8([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_8([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7306,
    "title": "Problem 7306",
    "description": "Write a Python function called `invalid_integer_positions_9` that must debug integer input by returning invalid positions followed by marker 9. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_9([\"1\", \"x\", \"3\"]) -> [1, 9]\n  invalid_integer_positions_9([\"-2\", \"0\"]) -> [9]",
    "initialCode": "def invalid_integer_positions_9(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_9(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [9]\n\nprint(invalid_integer_positions_9([\"1\", \"x\", \"3\"]))  # Expected: [1, 9]\nprint(invalid_integer_positions_9([\"-2\", \"0\"]))  # Expected: [9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7306(texts):\n    return invalid_integer_positions_9(texts)\n\n# Example 3: static method approach\nclass Problem7306Solution:\n    @staticmethod\n    def invalid_integer_positions_9(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [9]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_9([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_9([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7307,
    "title": "Problem 7307",
    "description": "Write a Python function called `invalid_integer_positions_10` that must debug integer input by returning invalid positions followed by marker 10. Practice testing & debugging.\nDifficulty: Expert.\nExamples:\n  invalid_integer_positions_10([\"1\", \"x\", \"3\"]) -> [1, 10]\n  invalid_integer_positions_10([\"-2\", \"0\"]) -> [10]",
    "initialCode": "def invalid_integer_positions_10(texts):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef invalid_integer_positions_10(texts):\n    invalid = []\n    for index, text in enumerate(texts):\n        try:\n            int(text)\n        except (TypeError, ValueError):\n            invalid.append(index)\n    return invalid + [10]\n\nprint(invalid_integer_positions_10([\"1\", \"x\", \"3\"]))  # Expected: [1, 10]\nprint(invalid_integer_positions_10([\"-2\", \"0\"]))  # Expected: [10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7307(texts):\n    return invalid_integer_positions_10(texts)\n\n# Example 3: static method approach\nclass Problem7307Solution:\n    @staticmethod\n    def invalid_integer_positions_10(texts):\n        invalid = []\n        for index, text in enumerate(texts):\n            try:\n                int(text)\n            except (TypeError, ValueError):\n                invalid.append(index)\n        return invalid + [10]\n\n# Example 4: assigned result approach\nresult = invalid_integer_positions_10([\"1\", \"x\", \"3\"])\nprint(result)\n\n# Example 5: boundary case\nprint(invalid_integer_positions_10([]))",
    "hint": "Focus on the tested invariant, expected versus actual values, failure location, and useful diagnostics. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required testing & debugging rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Testing & Debugging Difficult"
  },
  {
    "id": 7308,
    "title": "Problem 7308",
    "description": "Write a Python function called `typed_scale_1` that must multiply an integer by 1 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_1(3) -> 3\n  typed_scale_1(-2) -> -2",
    "initialCode": "def typed_scale_1(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_1(value: int) -> int:\n    return value * 1\n\nprint(typed_scale_1(3))  # Expected: 3\nprint(typed_scale_1(-2))  # Expected: -2\n\n# Example 2: named wrapper approach\ndef solve_problem_7308(value: int):\n    return typed_scale_1(value)\n\n# Example 3: static method approach\nclass Problem7308Solution:\n    @staticmethod\n    def typed_scale_1(value: int) -> int:\n        return value * 1\n\n# Example 4: assigned result approach\nresult = typed_scale_1(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_1(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7309,
    "title": "Problem 7309",
    "description": "Write a Python function called `typed_scale_2` that must multiply an integer by 2 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_2(3) -> 6\n  typed_scale_2(-2) -> -4",
    "initialCode": "def typed_scale_2(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_2(value: int) -> int:\n    return value * 2\n\nprint(typed_scale_2(3))  # Expected: 6\nprint(typed_scale_2(-2))  # Expected: -4\n\n# Example 2: named wrapper approach\ndef solve_problem_7309(value: int):\n    return typed_scale_2(value)\n\n# Example 3: static method approach\nclass Problem7309Solution:\n    @staticmethod\n    def typed_scale_2(value: int) -> int:\n        return value * 2\n\n# Example 4: assigned result approach\nresult = typed_scale_2(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_2(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7310,
    "title": "Problem 7310",
    "description": "Write a Python function called `typed_scale_3` that must multiply an integer by 3 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_3(3) -> 9\n  typed_scale_3(-2) -> -6",
    "initialCode": "def typed_scale_3(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_3(value: int) -> int:\n    return value * 3\n\nprint(typed_scale_3(3))  # Expected: 9\nprint(typed_scale_3(-2))  # Expected: -6\n\n# Example 2: named wrapper approach\ndef solve_problem_7310(value: int):\n    return typed_scale_3(value)\n\n# Example 3: static method approach\nclass Problem7310Solution:\n    @staticmethod\n    def typed_scale_3(value: int) -> int:\n        return value * 3\n\n# Example 4: assigned result approach\nresult = typed_scale_3(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_3(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7311,
    "title": "Problem 7311",
    "description": "Write a Python function called `typed_scale_4` that must multiply an integer by 4 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_4(3) -> 12\n  typed_scale_4(-2) -> -8",
    "initialCode": "def typed_scale_4(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_4(value: int) -> int:\n    return value * 4\n\nprint(typed_scale_4(3))  # Expected: 12\nprint(typed_scale_4(-2))  # Expected: -8\n\n# Example 2: named wrapper approach\ndef solve_problem_7311(value: int):\n    return typed_scale_4(value)\n\n# Example 3: static method approach\nclass Problem7311Solution:\n    @staticmethod\n    def typed_scale_4(value: int) -> int:\n        return value * 4\n\n# Example 4: assigned result approach\nresult = typed_scale_4(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_4(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7312,
    "title": "Problem 7312",
    "description": "Write a Python function called `typed_scale_5` that must multiply an integer by 5 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_5(3) -> 15\n  typed_scale_5(-2) -> -10",
    "initialCode": "def typed_scale_5(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_5(value: int) -> int:\n    return value * 5\n\nprint(typed_scale_5(3))  # Expected: 15\nprint(typed_scale_5(-2))  # Expected: -10\n\n# Example 2: named wrapper approach\ndef solve_problem_7312(value: int):\n    return typed_scale_5(value)\n\n# Example 3: static method approach\nclass Problem7312Solution:\n    @staticmethod\n    def typed_scale_5(value: int) -> int:\n        return value * 5\n\n# Example 4: assigned result approach\nresult = typed_scale_5(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_5(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7313,
    "title": "Problem 7313",
    "description": "Write a Python function called `typed_scale_6` that must multiply an integer by 6 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_6(3) -> 18\n  typed_scale_6(-2) -> -12",
    "initialCode": "def typed_scale_6(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_6(value: int) -> int:\n    return value * 6\n\nprint(typed_scale_6(3))  # Expected: 18\nprint(typed_scale_6(-2))  # Expected: -12\n\n# Example 2: named wrapper approach\ndef solve_problem_7313(value: int):\n    return typed_scale_6(value)\n\n# Example 3: static method approach\nclass Problem7313Solution:\n    @staticmethod\n    def typed_scale_6(value: int) -> int:\n        return value * 6\n\n# Example 4: assigned result approach\nresult = typed_scale_6(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_6(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7314,
    "title": "Problem 7314",
    "description": "Write a Python function called `typed_scale_7` that must multiply an integer by 7 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_7(3) -> 21\n  typed_scale_7(-2) -> -14",
    "initialCode": "def typed_scale_7(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_7(value: int) -> int:\n    return value * 7\n\nprint(typed_scale_7(3))  # Expected: 21\nprint(typed_scale_7(-2))  # Expected: -14\n\n# Example 2: named wrapper approach\ndef solve_problem_7314(value: int):\n    return typed_scale_7(value)\n\n# Example 3: static method approach\nclass Problem7314Solution:\n    @staticmethod\n    def typed_scale_7(value: int) -> int:\n        return value * 7\n\n# Example 4: assigned result approach\nresult = typed_scale_7(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_7(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7315,
    "title": "Problem 7315",
    "description": "Write a Python function called `typed_scale_8` that must multiply an integer by 8 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_8(3) -> 24\n  typed_scale_8(-2) -> -16",
    "initialCode": "def typed_scale_8(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_8(value: int) -> int:\n    return value * 8\n\nprint(typed_scale_8(3))  # Expected: 24\nprint(typed_scale_8(-2))  # Expected: -16\n\n# Example 2: named wrapper approach\ndef solve_problem_7315(value: int):\n    return typed_scale_8(value)\n\n# Example 3: static method approach\nclass Problem7315Solution:\n    @staticmethod\n    def typed_scale_8(value: int) -> int:\n        return value * 8\n\n# Example 4: assigned result approach\nresult = typed_scale_8(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_8(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7316,
    "title": "Problem 7316",
    "description": "Write a Python function called `typed_scale_9` that must multiply an integer by 9 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_9(3) -> 27\n  typed_scale_9(-2) -> -18",
    "initialCode": "def typed_scale_9(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_9(value: int) -> int:\n    return value * 9\n\nprint(typed_scale_9(3))  # Expected: 27\nprint(typed_scale_9(-2))  # Expected: -18\n\n# Example 2: named wrapper approach\ndef solve_problem_7316(value: int):\n    return typed_scale_9(value)\n\n# Example 3: static method approach\nclass Problem7316Solution:\n    @staticmethod\n    def typed_scale_9(value: int) -> int:\n        return value * 9\n\n# Example 4: assigned result approach\nresult = typed_scale_9(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_9(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7317,
    "title": "Problem 7317",
    "description": "Write a Python function called `typed_scale_10` that must multiply an integer by 10 with complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_scale_10(3) -> 30\n  typed_scale_10(-2) -> -20",
    "initialCode": "def typed_scale_10(value: int) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_scale_10(value: int) -> int:\n    return value * 10\n\nprint(typed_scale_10(3))  # Expected: 30\nprint(typed_scale_10(-2))  # Expected: -20\n\n# Example 2: named wrapper approach\ndef solve_problem_7317(value: int):\n    return typed_scale_10(value)\n\n# Example 3: static method approach\nclass Problem7317Solution:\n    @staticmethod\n    def typed_scale_10(value: int) -> int:\n        return value * 10\n\n# Example 4: assigned result approach\nresult = typed_scale_10(3)\nprint(result)\n\n# Example 5: boundary case\nprint(typed_scale_10(0))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7318,
    "title": "Problem 7318",
    "description": "Write a Python function called `typed_prefix_1` that must prefix text with label_1: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_1(\"abc\") -> \"label_1:abc\"\n  typed_prefix_1(\"\") -> \"label_1:\"",
    "initialCode": "def typed_prefix_1(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_1(text: str) -> str:\n    return \"label_1:\" + text\n\nprint(typed_prefix_1(\"abc\"))  # Expected: \"label_1:abc\"\nprint(typed_prefix_1(\"\"))  # Expected: \"label_1:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7318(text: str):\n    return typed_prefix_1(text)\n\n# Example 3: static method approach\nclass Problem7318Solution:\n    @staticmethod\n    def typed_prefix_1(text: str) -> str:\n        return \"label_1:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_1(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_1(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7319,
    "title": "Problem 7319",
    "description": "Write a Python function called `typed_prefix_2` that must prefix text with label_2: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_2(\"abc\") -> \"label_2:abc\"\n  typed_prefix_2(\"\") -> \"label_2:\"",
    "initialCode": "def typed_prefix_2(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_2(text: str) -> str:\n    return \"label_2:\" + text\n\nprint(typed_prefix_2(\"abc\"))  # Expected: \"label_2:abc\"\nprint(typed_prefix_2(\"\"))  # Expected: \"label_2:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7319(text: str):\n    return typed_prefix_2(text)\n\n# Example 3: static method approach\nclass Problem7319Solution:\n    @staticmethod\n    def typed_prefix_2(text: str) -> str:\n        return \"label_2:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_2(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_2(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7320,
    "title": "Problem 7320",
    "description": "Write a Python function called `typed_prefix_3` that must prefix text with label_3: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_3(\"abc\") -> \"label_3:abc\"\n  typed_prefix_3(\"\") -> \"label_3:\"",
    "initialCode": "def typed_prefix_3(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_3(text: str) -> str:\n    return \"label_3:\" + text\n\nprint(typed_prefix_3(\"abc\"))  # Expected: \"label_3:abc\"\nprint(typed_prefix_3(\"\"))  # Expected: \"label_3:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7320(text: str):\n    return typed_prefix_3(text)\n\n# Example 3: static method approach\nclass Problem7320Solution:\n    @staticmethod\n    def typed_prefix_3(text: str) -> str:\n        return \"label_3:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_3(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_3(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7321,
    "title": "Problem 7321",
    "description": "Write a Python function called `typed_prefix_4` that must prefix text with label_4: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_4(\"abc\") -> \"label_4:abc\"\n  typed_prefix_4(\"\") -> \"label_4:\"",
    "initialCode": "def typed_prefix_4(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_4(text: str) -> str:\n    return \"label_4:\" + text\n\nprint(typed_prefix_4(\"abc\"))  # Expected: \"label_4:abc\"\nprint(typed_prefix_4(\"\"))  # Expected: \"label_4:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7321(text: str):\n    return typed_prefix_4(text)\n\n# Example 3: static method approach\nclass Problem7321Solution:\n    @staticmethod\n    def typed_prefix_4(text: str) -> str:\n        return \"label_4:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_4(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_4(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7322,
    "title": "Problem 7322",
    "description": "Write a Python function called `typed_prefix_5` that must prefix text with label_5: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_5(\"abc\") -> \"label_5:abc\"\n  typed_prefix_5(\"\") -> \"label_5:\"",
    "initialCode": "def typed_prefix_5(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_5(text: str) -> str:\n    return \"label_5:\" + text\n\nprint(typed_prefix_5(\"abc\"))  # Expected: \"label_5:abc\"\nprint(typed_prefix_5(\"\"))  # Expected: \"label_5:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7322(text: str):\n    return typed_prefix_5(text)\n\n# Example 3: static method approach\nclass Problem7322Solution:\n    @staticmethod\n    def typed_prefix_5(text: str) -> str:\n        return \"label_5:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_5(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_5(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7323,
    "title": "Problem 7323",
    "description": "Write a Python function called `typed_prefix_6` that must prefix text with label_6: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_6(\"abc\") -> \"label_6:abc\"\n  typed_prefix_6(\"\") -> \"label_6:\"",
    "initialCode": "def typed_prefix_6(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_6(text: str) -> str:\n    return \"label_6:\" + text\n\nprint(typed_prefix_6(\"abc\"))  # Expected: \"label_6:abc\"\nprint(typed_prefix_6(\"\"))  # Expected: \"label_6:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7323(text: str):\n    return typed_prefix_6(text)\n\n# Example 3: static method approach\nclass Problem7323Solution:\n    @staticmethod\n    def typed_prefix_6(text: str) -> str:\n        return \"label_6:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_6(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_6(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7324,
    "title": "Problem 7324",
    "description": "Write a Python function called `typed_prefix_7` that must prefix text with label_7: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_7(\"abc\") -> \"label_7:abc\"\n  typed_prefix_7(\"\") -> \"label_7:\"",
    "initialCode": "def typed_prefix_7(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_7(text: str) -> str:\n    return \"label_7:\" + text\n\nprint(typed_prefix_7(\"abc\"))  # Expected: \"label_7:abc\"\nprint(typed_prefix_7(\"\"))  # Expected: \"label_7:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7324(text: str):\n    return typed_prefix_7(text)\n\n# Example 3: static method approach\nclass Problem7324Solution:\n    @staticmethod\n    def typed_prefix_7(text: str) -> str:\n        return \"label_7:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_7(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_7(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7325,
    "title": "Problem 7325",
    "description": "Write a Python function called `typed_prefix_8` that must prefix text with label_8: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_8(\"abc\") -> \"label_8:abc\"\n  typed_prefix_8(\"\") -> \"label_8:\"",
    "initialCode": "def typed_prefix_8(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_8(text: str) -> str:\n    return \"label_8:\" + text\n\nprint(typed_prefix_8(\"abc\"))  # Expected: \"label_8:abc\"\nprint(typed_prefix_8(\"\"))  # Expected: \"label_8:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7325(text: str):\n    return typed_prefix_8(text)\n\n# Example 3: static method approach\nclass Problem7325Solution:\n    @staticmethod\n    def typed_prefix_8(text: str) -> str:\n        return \"label_8:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_8(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_8(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7326,
    "title": "Problem 7326",
    "description": "Write a Python function called `typed_prefix_9` that must prefix text with label_9: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_9(\"abc\") -> \"label_9:abc\"\n  typed_prefix_9(\"\") -> \"label_9:\"",
    "initialCode": "def typed_prefix_9(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_9(text: str) -> str:\n    return \"label_9:\" + text\n\nprint(typed_prefix_9(\"abc\"))  # Expected: \"label_9:abc\"\nprint(typed_prefix_9(\"\"))  # Expected: \"label_9:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7326(text: str):\n    return typed_prefix_9(text)\n\n# Example 3: static method approach\nclass Problem7326Solution:\n    @staticmethod\n    def typed_prefix_9(text: str) -> str:\n        return \"label_9:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_9(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_9(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7327,
    "title": "Problem 7327",
    "description": "Write a Python function called `typed_prefix_10` that must prefix text with label_10: using complete type hints. Practice type hint.\nDifficulty: Easy.\nExamples:\n  typed_prefix_10(\"abc\") -> \"label_10:abc\"\n  typed_prefix_10(\"\") -> \"label_10:\"",
    "initialCode": "def typed_prefix_10(text: str) -> str:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_prefix_10(text: str) -> str:\n    return \"label_10:\" + text\n\nprint(typed_prefix_10(\"abc\"))  # Expected: \"label_10:abc\"\nprint(typed_prefix_10(\"\"))  # Expected: \"label_10:\"\n\n# Example 2: named wrapper approach\ndef solve_problem_7327(text: str):\n    return typed_prefix_10(text)\n\n# Example 3: static method approach\nclass Problem7327Solution:\n    @staticmethod\n    def typed_prefix_10(text: str) -> str:\n        return \"label_10:\" + text\n\n# Example 4: assigned result approach\nresult = typed_prefix_10(\"abc\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_prefix_10(\"Python\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Easy"
  },
  {
    "id": 7328,
    "title": "Problem 7328",
    "description": "Write a Python function called `typed_filter_1` that must return integers at least 1 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_1([1, 5, 10]) -> [1, 5, 10]\n  typed_filter_1([1]) -> [1]",
    "initialCode": "def typed_filter_1(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_1(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 1]\n\nprint(typed_filter_1([1, 5, 10]))  # Expected: [1, 5, 10]\nprint(typed_filter_1([1]))  # Expected: [1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7328(values: list[int]):\n    return typed_filter_1(values)\n\n# Example 3: static method approach\nclass Problem7328Solution:\n    @staticmethod\n    def typed_filter_1(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 1]\n\n# Example 4: assigned result approach\nresult = typed_filter_1([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_1([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7329,
    "title": "Problem 7329",
    "description": "Write a Python function called `typed_filter_2` that must return integers at least 2 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_2([1, 5, 10]) -> [5, 10]\n  typed_filter_2([2]) -> [2]",
    "initialCode": "def typed_filter_2(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_2(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 2]\n\nprint(typed_filter_2([1, 5, 10]))  # Expected: [5, 10]\nprint(typed_filter_2([2]))  # Expected: [2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7329(values: list[int]):\n    return typed_filter_2(values)\n\n# Example 3: static method approach\nclass Problem7329Solution:\n    @staticmethod\n    def typed_filter_2(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 2]\n\n# Example 4: assigned result approach\nresult = typed_filter_2([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_2([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7330,
    "title": "Problem 7330",
    "description": "Write a Python function called `typed_filter_3` that must return integers at least 3 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_3([1, 5, 10]) -> [5, 10]\n  typed_filter_3([3]) -> [3]",
    "initialCode": "def typed_filter_3(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_3(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 3]\n\nprint(typed_filter_3([1, 5, 10]))  # Expected: [5, 10]\nprint(typed_filter_3([3]))  # Expected: [3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7330(values: list[int]):\n    return typed_filter_3(values)\n\n# Example 3: static method approach\nclass Problem7330Solution:\n    @staticmethod\n    def typed_filter_3(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 3]\n\n# Example 4: assigned result approach\nresult = typed_filter_3([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_3([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7331,
    "title": "Problem 7331",
    "description": "Write a Python function called `typed_filter_4` that must return integers at least 4 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_4([1, 5, 10]) -> [5, 10]\n  typed_filter_4([4]) -> [4]",
    "initialCode": "def typed_filter_4(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_4(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 4]\n\nprint(typed_filter_4([1, 5, 10]))  # Expected: [5, 10]\nprint(typed_filter_4([4]))  # Expected: [4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7331(values: list[int]):\n    return typed_filter_4(values)\n\n# Example 3: static method approach\nclass Problem7331Solution:\n    @staticmethod\n    def typed_filter_4(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 4]\n\n# Example 4: assigned result approach\nresult = typed_filter_4([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_4([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7332,
    "title": "Problem 7332",
    "description": "Write a Python function called `typed_filter_5` that must return integers at least 5 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_5([1, 5, 10]) -> [5, 10]\n  typed_filter_5([5]) -> [5]",
    "initialCode": "def typed_filter_5(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_5(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 5]\n\nprint(typed_filter_5([1, 5, 10]))  # Expected: [5, 10]\nprint(typed_filter_5([5]))  # Expected: [5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7332(values: list[int]):\n    return typed_filter_5(values)\n\n# Example 3: static method approach\nclass Problem7332Solution:\n    @staticmethod\n    def typed_filter_5(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 5]\n\n# Example 4: assigned result approach\nresult = typed_filter_5([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_5([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7333,
    "title": "Problem 7333",
    "description": "Write a Python function called `typed_filter_6` that must return integers at least 6 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_6([1, 5, 10]) -> [10]\n  typed_filter_6([6]) -> [6]",
    "initialCode": "def typed_filter_6(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_6(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 6]\n\nprint(typed_filter_6([1, 5, 10]))  # Expected: [10]\nprint(typed_filter_6([6]))  # Expected: [6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7333(values: list[int]):\n    return typed_filter_6(values)\n\n# Example 3: static method approach\nclass Problem7333Solution:\n    @staticmethod\n    def typed_filter_6(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 6]\n\n# Example 4: assigned result approach\nresult = typed_filter_6([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_6([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7334,
    "title": "Problem 7334",
    "description": "Write a Python function called `typed_filter_7` that must return integers at least 7 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_7([1, 5, 10]) -> [10]\n  typed_filter_7([7]) -> [7]",
    "initialCode": "def typed_filter_7(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_7(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 7]\n\nprint(typed_filter_7([1, 5, 10]))  # Expected: [10]\nprint(typed_filter_7([7]))  # Expected: [7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7334(values: list[int]):\n    return typed_filter_7(values)\n\n# Example 3: static method approach\nclass Problem7334Solution:\n    @staticmethod\n    def typed_filter_7(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 7]\n\n# Example 4: assigned result approach\nresult = typed_filter_7([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_7([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7335,
    "title": "Problem 7335",
    "description": "Write a Python function called `typed_filter_8` that must return integers at least 8 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_8([1, 5, 10]) -> [10]\n  typed_filter_8([8]) -> [8]",
    "initialCode": "def typed_filter_8(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_8(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 8]\n\nprint(typed_filter_8([1, 5, 10]))  # Expected: [10]\nprint(typed_filter_8([8]))  # Expected: [8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7335(values: list[int]):\n    return typed_filter_8(values)\n\n# Example 3: static method approach\nclass Problem7335Solution:\n    @staticmethod\n    def typed_filter_8(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 8]\n\n# Example 4: assigned result approach\nresult = typed_filter_8([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_8([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7336,
    "title": "Problem 7336",
    "description": "Write a Python function called `typed_filter_9` that must return integers at least 9 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_9([1, 5, 10]) -> [10]\n  typed_filter_9([9]) -> [9]",
    "initialCode": "def typed_filter_9(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_9(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 9]\n\nprint(typed_filter_9([1, 5, 10]))  # Expected: [10]\nprint(typed_filter_9([9]))  # Expected: [9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7336(values: list[int]):\n    return typed_filter_9(values)\n\n# Example 3: static method approach\nclass Problem7336Solution:\n    @staticmethod\n    def typed_filter_9(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 9]\n\n# Example 4: assigned result approach\nresult = typed_filter_9([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_9([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7337,
    "title": "Problem 7337",
    "description": "Write a Python function called `typed_filter_10` that must return integers at least 10 with collection type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_filter_10([1, 5, 10]) -> [10]\n  typed_filter_10([10]) -> [10]",
    "initialCode": "def typed_filter_10(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_filter_10(values: list[int]) -> list[int]:\n    return [value for value in values if value >= 10]\n\nprint(typed_filter_10([1, 5, 10]))  # Expected: [10]\nprint(typed_filter_10([10]))  # Expected: [10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7337(values: list[int]):\n    return typed_filter_10(values)\n\n# Example 3: static method approach\nclass Problem7337Solution:\n    @staticmethod\n    def typed_filter_10(values: list[int]) -> list[int]:\n        return [value for value in values if value >= 10]\n\n# Example 4: assigned result approach\nresult = typed_filter_10([1, 5, 10])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_filter_10([]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7338,
    "title": "Problem 7338",
    "description": "Write a Python function called `typed_lookup_1` that must look up an integer by string key or return 1, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_1({\"a\": 1}, \"a\") -> 1\n  typed_lookup_1({}, \"x\") -> 1",
    "initialCode": "def typed_lookup_1(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_1(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 1)\n\nprint(typed_lookup_1({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_1({}, \"x\"))  # Expected: 1\n\n# Example 2: named wrapper approach\ndef solve_problem_7338(mapping: dict[str, int], key: str):\n    return typed_lookup_1(mapping, key)\n\n# Example 3: static method approach\nclass Problem7338Solution:\n    @staticmethod\n    def typed_lookup_1(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 1)\n\n# Example 4: assigned result approach\nresult = typed_lookup_1({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_1({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7339,
    "title": "Problem 7339",
    "description": "Write a Python function called `typed_lookup_2` that must look up an integer by string key or return 2, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_2({\"a\": 1}, \"a\") -> 1\n  typed_lookup_2({}, \"x\") -> 2",
    "initialCode": "def typed_lookup_2(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_2(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 2)\n\nprint(typed_lookup_2({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_2({}, \"x\"))  # Expected: 2\n\n# Example 2: named wrapper approach\ndef solve_problem_7339(mapping: dict[str, int], key: str):\n    return typed_lookup_2(mapping, key)\n\n# Example 3: static method approach\nclass Problem7339Solution:\n    @staticmethod\n    def typed_lookup_2(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 2)\n\n# Example 4: assigned result approach\nresult = typed_lookup_2({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_2({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7340,
    "title": "Problem 7340",
    "description": "Write a Python function called `typed_lookup_3` that must look up an integer by string key or return 3, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_3({\"a\": 1}, \"a\") -> 1\n  typed_lookup_3({}, \"x\") -> 3",
    "initialCode": "def typed_lookup_3(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_3(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 3)\n\nprint(typed_lookup_3({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_3({}, \"x\"))  # Expected: 3\n\n# Example 2: named wrapper approach\ndef solve_problem_7340(mapping: dict[str, int], key: str):\n    return typed_lookup_3(mapping, key)\n\n# Example 3: static method approach\nclass Problem7340Solution:\n    @staticmethod\n    def typed_lookup_3(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 3)\n\n# Example 4: assigned result approach\nresult = typed_lookup_3({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_3({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7341,
    "title": "Problem 7341",
    "description": "Write a Python function called `typed_lookup_4` that must look up an integer by string key or return 4, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_4({\"a\": 1}, \"a\") -> 1\n  typed_lookup_4({}, \"x\") -> 4",
    "initialCode": "def typed_lookup_4(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_4(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 4)\n\nprint(typed_lookup_4({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_4({}, \"x\"))  # Expected: 4\n\n# Example 2: named wrapper approach\ndef solve_problem_7341(mapping: dict[str, int], key: str):\n    return typed_lookup_4(mapping, key)\n\n# Example 3: static method approach\nclass Problem7341Solution:\n    @staticmethod\n    def typed_lookup_4(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 4)\n\n# Example 4: assigned result approach\nresult = typed_lookup_4({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_4({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7342,
    "title": "Problem 7342",
    "description": "Write a Python function called `typed_lookup_5` that must look up an integer by string key or return 5, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_5({\"a\": 1}, \"a\") -> 1\n  typed_lookup_5({}, \"x\") -> 5",
    "initialCode": "def typed_lookup_5(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_5(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 5)\n\nprint(typed_lookup_5({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_5({}, \"x\"))  # Expected: 5\n\n# Example 2: named wrapper approach\ndef solve_problem_7342(mapping: dict[str, int], key: str):\n    return typed_lookup_5(mapping, key)\n\n# Example 3: static method approach\nclass Problem7342Solution:\n    @staticmethod\n    def typed_lookup_5(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 5)\n\n# Example 4: assigned result approach\nresult = typed_lookup_5({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_5({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7343,
    "title": "Problem 7343",
    "description": "Write a Python function called `typed_lookup_6` that must look up an integer by string key or return 6, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_6({\"a\": 1}, \"a\") -> 1\n  typed_lookup_6({}, \"x\") -> 6",
    "initialCode": "def typed_lookup_6(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_6(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 6)\n\nprint(typed_lookup_6({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_6({}, \"x\"))  # Expected: 6\n\n# Example 2: named wrapper approach\ndef solve_problem_7343(mapping: dict[str, int], key: str):\n    return typed_lookup_6(mapping, key)\n\n# Example 3: static method approach\nclass Problem7343Solution:\n    @staticmethod\n    def typed_lookup_6(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 6)\n\n# Example 4: assigned result approach\nresult = typed_lookup_6({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_6({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7344,
    "title": "Problem 7344",
    "description": "Write a Python function called `typed_lookup_7` that must look up an integer by string key or return 7, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_7({\"a\": 1}, \"a\") -> 1\n  typed_lookup_7({}, \"x\") -> 7",
    "initialCode": "def typed_lookup_7(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_7(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 7)\n\nprint(typed_lookup_7({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_7({}, \"x\"))  # Expected: 7\n\n# Example 2: named wrapper approach\ndef solve_problem_7344(mapping: dict[str, int], key: str):\n    return typed_lookup_7(mapping, key)\n\n# Example 3: static method approach\nclass Problem7344Solution:\n    @staticmethod\n    def typed_lookup_7(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 7)\n\n# Example 4: assigned result approach\nresult = typed_lookup_7({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_7({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7345,
    "title": "Problem 7345",
    "description": "Write a Python function called `typed_lookup_8` that must look up an integer by string key or return 8, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_8({\"a\": 1}, \"a\") -> 1\n  typed_lookup_8({}, \"x\") -> 8",
    "initialCode": "def typed_lookup_8(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_8(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 8)\n\nprint(typed_lookup_8({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_8({}, \"x\"))  # Expected: 8\n\n# Example 2: named wrapper approach\ndef solve_problem_7345(mapping: dict[str, int], key: str):\n    return typed_lookup_8(mapping, key)\n\n# Example 3: static method approach\nclass Problem7345Solution:\n    @staticmethod\n    def typed_lookup_8(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 8)\n\n# Example 4: assigned result approach\nresult = typed_lookup_8({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_8({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7346,
    "title": "Problem 7346",
    "description": "Write a Python function called `typed_lookup_9` that must look up an integer by string key or return 9, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_9({\"a\": 1}, \"a\") -> 1\n  typed_lookup_9({}, \"x\") -> 9",
    "initialCode": "def typed_lookup_9(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_9(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 9)\n\nprint(typed_lookup_9({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_9({}, \"x\"))  # Expected: 9\n\n# Example 2: named wrapper approach\ndef solve_problem_7346(mapping: dict[str, int], key: str):\n    return typed_lookup_9(mapping, key)\n\n# Example 3: static method approach\nclass Problem7346Solution:\n    @staticmethod\n    def typed_lookup_9(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 9)\n\n# Example 4: assigned result approach\nresult = typed_lookup_9({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_9({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7347,
    "title": "Problem 7347",
    "description": "Write a Python function called `typed_lookup_10` that must look up an integer by string key or return 10, with type hints. Practice type hint.\nDifficulty: Intermediate.\nExamples:\n  typed_lookup_10({\"a\": 1}, \"a\") -> 1\n  typed_lookup_10({}, \"x\") -> 10",
    "initialCode": "def typed_lookup_10(mapping: dict[str, int], key: str) -> int:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_lookup_10(mapping: dict[str, int], key: str) -> int:\n    return mapping.get(key, 10)\n\nprint(typed_lookup_10({\"a\": 1}, \"a\"))  # Expected: 1\nprint(typed_lookup_10({}, \"x\"))  # Expected: 10\n\n# Example 2: named wrapper approach\ndef solve_problem_7347(mapping: dict[str, int], key: str):\n    return typed_lookup_10(mapping, key)\n\n# Example 3: static method approach\nclass Problem7347Solution:\n    @staticmethod\n    def typed_lookup_10(mapping: dict[str, int], key: str) -> int:\n        return mapping.get(key, 10)\n\n# Example 4: assigned result approach\nresult = typed_lookup_10({\"a\": 1}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(typed_lookup_10({\"x\": 0}, \"x\"))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Intermediate"
  },
  {
    "id": 7348,
    "title": "Problem 7348",
    "description": "Write a Python function called `typed_summary_1` that must return sum plus 1 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_1([1, 2]) -> [4, 2]\n  typed_summary_1([]) -> [1, 0]",
    "initialCode": "def typed_summary_1(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_1(values: list[int]) -> list[int]:\n    return [sum(values) + 1, len(values)]\n\nprint(typed_summary_1([1, 2]))  # Expected: [4, 2]\nprint(typed_summary_1([]))  # Expected: [1, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7348(values: list[int]):\n    return typed_summary_1(values)\n\n# Example 3: static method approach\nclass Problem7348Solution:\n    @staticmethod\n    def typed_summary_1(values: list[int]) -> list[int]:\n        return [sum(values) + 1, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_1([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_1([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7349,
    "title": "Problem 7349",
    "description": "Write a Python function called `typed_summary_2` that must return sum plus 2 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_2([1, 2]) -> [5, 2]\n  typed_summary_2([]) -> [2, 0]",
    "initialCode": "def typed_summary_2(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_2(values: list[int]) -> list[int]:\n    return [sum(values) + 2, len(values)]\n\nprint(typed_summary_2([1, 2]))  # Expected: [5, 2]\nprint(typed_summary_2([]))  # Expected: [2, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7349(values: list[int]):\n    return typed_summary_2(values)\n\n# Example 3: static method approach\nclass Problem7349Solution:\n    @staticmethod\n    def typed_summary_2(values: list[int]) -> list[int]:\n        return [sum(values) + 2, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_2([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_2([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7350,
    "title": "Problem 7350",
    "description": "Write a Python function called `typed_summary_3` that must return sum plus 3 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_3([1, 2]) -> [6, 2]\n  typed_summary_3([]) -> [3, 0]",
    "initialCode": "def typed_summary_3(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_3(values: list[int]) -> list[int]:\n    return [sum(values) + 3, len(values)]\n\nprint(typed_summary_3([1, 2]))  # Expected: [6, 2]\nprint(typed_summary_3([]))  # Expected: [3, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7350(values: list[int]):\n    return typed_summary_3(values)\n\n# Example 3: static method approach\nclass Problem7350Solution:\n    @staticmethod\n    def typed_summary_3(values: list[int]) -> list[int]:\n        return [sum(values) + 3, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_3([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_3([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7351,
    "title": "Problem 7351",
    "description": "Write a Python function called `typed_summary_4` that must return sum plus 4 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_4([1, 2]) -> [7, 2]\n  typed_summary_4([]) -> [4, 0]",
    "initialCode": "def typed_summary_4(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_4(values: list[int]) -> list[int]:\n    return [sum(values) + 4, len(values)]\n\nprint(typed_summary_4([1, 2]))  # Expected: [7, 2]\nprint(typed_summary_4([]))  # Expected: [4, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7351(values: list[int]):\n    return typed_summary_4(values)\n\n# Example 3: static method approach\nclass Problem7351Solution:\n    @staticmethod\n    def typed_summary_4(values: list[int]) -> list[int]:\n        return [sum(values) + 4, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_4([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_4([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7352,
    "title": "Problem 7352",
    "description": "Write a Python function called `typed_summary_5` that must return sum plus 5 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_5([1, 2]) -> [8, 2]\n  typed_summary_5([]) -> [5, 0]",
    "initialCode": "def typed_summary_5(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_5(values: list[int]) -> list[int]:\n    return [sum(values) + 5, len(values)]\n\nprint(typed_summary_5([1, 2]))  # Expected: [8, 2]\nprint(typed_summary_5([]))  # Expected: [5, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7352(values: list[int]):\n    return typed_summary_5(values)\n\n# Example 3: static method approach\nclass Problem7352Solution:\n    @staticmethod\n    def typed_summary_5(values: list[int]) -> list[int]:\n        return [sum(values) + 5, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_5([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_5([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7353,
    "title": "Problem 7353",
    "description": "Write a Python function called `typed_summary_6` that must return sum plus 6 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_6([1, 2]) -> [9, 2]\n  typed_summary_6([]) -> [6, 0]",
    "initialCode": "def typed_summary_6(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_6(values: list[int]) -> list[int]:\n    return [sum(values) + 6, len(values)]\n\nprint(typed_summary_6([1, 2]))  # Expected: [9, 2]\nprint(typed_summary_6([]))  # Expected: [6, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7353(values: list[int]):\n    return typed_summary_6(values)\n\n# Example 3: static method approach\nclass Problem7353Solution:\n    @staticmethod\n    def typed_summary_6(values: list[int]) -> list[int]:\n        return [sum(values) + 6, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_6([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_6([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7354,
    "title": "Problem 7354",
    "description": "Write a Python function called `typed_summary_7` that must return sum plus 7 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_7([1, 2]) -> [10, 2]\n  typed_summary_7([]) -> [7, 0]",
    "initialCode": "def typed_summary_7(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_7(values: list[int]) -> list[int]:\n    return [sum(values) + 7, len(values)]\n\nprint(typed_summary_7([1, 2]))  # Expected: [10, 2]\nprint(typed_summary_7([]))  # Expected: [7, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7354(values: list[int]):\n    return typed_summary_7(values)\n\n# Example 3: static method approach\nclass Problem7354Solution:\n    @staticmethod\n    def typed_summary_7(values: list[int]) -> list[int]:\n        return [sum(values) + 7, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_7([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_7([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7355,
    "title": "Problem 7355",
    "description": "Write a Python function called `typed_summary_8` that must return sum plus 8 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_8([1, 2]) -> [11, 2]\n  typed_summary_8([]) -> [8, 0]",
    "initialCode": "def typed_summary_8(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_8(values: list[int]) -> list[int]:\n    return [sum(values) + 8, len(values)]\n\nprint(typed_summary_8([1, 2]))  # Expected: [11, 2]\nprint(typed_summary_8([]))  # Expected: [8, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7355(values: list[int]):\n    return typed_summary_8(values)\n\n# Example 3: static method approach\nclass Problem7355Solution:\n    @staticmethod\n    def typed_summary_8(values: list[int]) -> list[int]:\n        return [sum(values) + 8, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_8([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_8([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7356,
    "title": "Problem 7356",
    "description": "Write a Python function called `typed_summary_9` that must return sum plus 9 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_9([1, 2]) -> [12, 2]\n  typed_summary_9([]) -> [9, 0]",
    "initialCode": "def typed_summary_9(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_9(values: list[int]) -> list[int]:\n    return [sum(values) + 9, len(values)]\n\nprint(typed_summary_9([1, 2]))  # Expected: [12, 2]\nprint(typed_summary_9([]))  # Expected: [9, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7356(values: list[int]):\n    return typed_summary_9(values)\n\n# Example 3: static method approach\nclass Problem7356Solution:\n    @staticmethod\n    def typed_summary_9(values: list[int]) -> list[int]:\n        return [sum(values) + 9, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_9([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_9([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7357,
    "title": "Problem 7357",
    "description": "Write a Python function called `typed_summary_10` that must return sum plus 10 and item count as a typed two-item list. Practice type hint.\nDifficulty: Expert.\nExamples:\n  typed_summary_10([1, 2]) -> [13, 2]\n  typed_summary_10([]) -> [10, 0]",
    "initialCode": "def typed_summary_10(values: list[int]) -> list[int]:\n    pass",
    "solution": "# Example 1: canonical function approach\ndef typed_summary_10(values: list[int]) -> list[int]:\n    return [sum(values) + 10, len(values)]\n\nprint(typed_summary_10([1, 2]))  # Expected: [13, 2]\nprint(typed_summary_10([]))  # Expected: [10, 0]\n\n# Example 2: named wrapper approach\ndef solve_problem_7357(values: list[int]):\n    return typed_summary_10(values)\n\n# Example 3: static method approach\nclass Problem7357Solution:\n    @staticmethod\n    def typed_summary_10(values: list[int]) -> list[int]:\n        return [sum(values) + 10, len(values)]\n\n# Example 4: assigned result approach\nresult = typed_summary_10([1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(typed_summary_10([-1, 1]))",
    "hint": "Focus on every parameter annotation, the return annotation, collection element types, and agreement between annotations and behavior. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required type hint rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Type Hint Difficult"
  },
  {
    "id": 7358,
    "title": "Problem 7358",
    "description": "Write a Python function called `safe_integer_offset_1` that must convert text to an integer plus 1, or return 1 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_1(\"5\") -> 6\n  safe_integer_offset_1(\"bad\") -> 1",
    "initialCode": "def safe_integer_offset_1(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_1(text):\n    try:\n        return int(text) + 1\n    except (TypeError, ValueError):\n        return 1\n\nprint(safe_integer_offset_1(\"5\"))  # Expected: 6\nprint(safe_integer_offset_1(\"bad\"))  # Expected: 1\n\n# Example 2: named wrapper approach\ndef solve_problem_7358(text):\n    return safe_integer_offset_1(text)\n\n# Example 3: static method approach\nclass Problem7358Solution:\n    @staticmethod\n    def safe_integer_offset_1(text):\n        try:\n            return int(text) + 1\n        except (TypeError, ValueError):\n            return 1\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_1(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_1(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7359,
    "title": "Problem 7359",
    "description": "Write a Python function called `safe_integer_offset_2` that must convert text to an integer plus 2, or return 2 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_2(\"5\") -> 7\n  safe_integer_offset_2(\"bad\") -> 2",
    "initialCode": "def safe_integer_offset_2(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_2(text):\n    try:\n        return int(text) + 2\n    except (TypeError, ValueError):\n        return 2\n\nprint(safe_integer_offset_2(\"5\"))  # Expected: 7\nprint(safe_integer_offset_2(\"bad\"))  # Expected: 2\n\n# Example 2: named wrapper approach\ndef solve_problem_7359(text):\n    return safe_integer_offset_2(text)\n\n# Example 3: static method approach\nclass Problem7359Solution:\n    @staticmethod\n    def safe_integer_offset_2(text):\n        try:\n            return int(text) + 2\n        except (TypeError, ValueError):\n            return 2\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_2(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_2(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7360,
    "title": "Problem 7360",
    "description": "Write a Python function called `safe_integer_offset_3` that must convert text to an integer plus 3, or return 3 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_3(\"5\") -> 8\n  safe_integer_offset_3(\"bad\") -> 3",
    "initialCode": "def safe_integer_offset_3(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_3(text):\n    try:\n        return int(text) + 3\n    except (TypeError, ValueError):\n        return 3\n\nprint(safe_integer_offset_3(\"5\"))  # Expected: 8\nprint(safe_integer_offset_3(\"bad\"))  # Expected: 3\n\n# Example 2: named wrapper approach\ndef solve_problem_7360(text):\n    return safe_integer_offset_3(text)\n\n# Example 3: static method approach\nclass Problem7360Solution:\n    @staticmethod\n    def safe_integer_offset_3(text):\n        try:\n            return int(text) + 3\n        except (TypeError, ValueError):\n            return 3\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_3(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_3(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7361,
    "title": "Problem 7361",
    "description": "Write a Python function called `safe_integer_offset_4` that must convert text to an integer plus 4, or return 4 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_4(\"5\") -> 9\n  safe_integer_offset_4(\"bad\") -> 4",
    "initialCode": "def safe_integer_offset_4(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_4(text):\n    try:\n        return int(text) + 4\n    except (TypeError, ValueError):\n        return 4\n\nprint(safe_integer_offset_4(\"5\"))  # Expected: 9\nprint(safe_integer_offset_4(\"bad\"))  # Expected: 4\n\n# Example 2: named wrapper approach\ndef solve_problem_7361(text):\n    return safe_integer_offset_4(text)\n\n# Example 3: static method approach\nclass Problem7361Solution:\n    @staticmethod\n    def safe_integer_offset_4(text):\n        try:\n            return int(text) + 4\n        except (TypeError, ValueError):\n            return 4\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_4(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_4(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7362,
    "title": "Problem 7362",
    "description": "Write a Python function called `safe_integer_offset_5` that must convert text to an integer plus 5, or return 5 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_5(\"5\") -> 10\n  safe_integer_offset_5(\"bad\") -> 5",
    "initialCode": "def safe_integer_offset_5(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_5(text):\n    try:\n        return int(text) + 5\n    except (TypeError, ValueError):\n        return 5\n\nprint(safe_integer_offset_5(\"5\"))  # Expected: 10\nprint(safe_integer_offset_5(\"bad\"))  # Expected: 5\n\n# Example 2: named wrapper approach\ndef solve_problem_7362(text):\n    return safe_integer_offset_5(text)\n\n# Example 3: static method approach\nclass Problem7362Solution:\n    @staticmethod\n    def safe_integer_offset_5(text):\n        try:\n            return int(text) + 5\n        except (TypeError, ValueError):\n            return 5\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_5(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_5(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7363,
    "title": "Problem 7363",
    "description": "Write a Python function called `safe_integer_offset_6` that must convert text to an integer plus 6, or return 6 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_6(\"5\") -> 11\n  safe_integer_offset_6(\"bad\") -> 6",
    "initialCode": "def safe_integer_offset_6(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_6(text):\n    try:\n        return int(text) + 6\n    except (TypeError, ValueError):\n        return 6\n\nprint(safe_integer_offset_6(\"5\"))  # Expected: 11\nprint(safe_integer_offset_6(\"bad\"))  # Expected: 6\n\n# Example 2: named wrapper approach\ndef solve_problem_7363(text):\n    return safe_integer_offset_6(text)\n\n# Example 3: static method approach\nclass Problem7363Solution:\n    @staticmethod\n    def safe_integer_offset_6(text):\n        try:\n            return int(text) + 6\n        except (TypeError, ValueError):\n            return 6\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_6(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_6(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7364,
    "title": "Problem 7364",
    "description": "Write a Python function called `safe_integer_offset_7` that must convert text to an integer plus 7, or return 7 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_7(\"5\") -> 12\n  safe_integer_offset_7(\"bad\") -> 7",
    "initialCode": "def safe_integer_offset_7(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_7(text):\n    try:\n        return int(text) + 7\n    except (TypeError, ValueError):\n        return 7\n\nprint(safe_integer_offset_7(\"5\"))  # Expected: 12\nprint(safe_integer_offset_7(\"bad\"))  # Expected: 7\n\n# Example 2: named wrapper approach\ndef solve_problem_7364(text):\n    return safe_integer_offset_7(text)\n\n# Example 3: static method approach\nclass Problem7364Solution:\n    @staticmethod\n    def safe_integer_offset_7(text):\n        try:\n            return int(text) + 7\n        except (TypeError, ValueError):\n            return 7\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_7(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_7(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7365,
    "title": "Problem 7365",
    "description": "Write a Python function called `safe_integer_offset_8` that must convert text to an integer plus 8, or return 8 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_8(\"5\") -> 13\n  safe_integer_offset_8(\"bad\") -> 8",
    "initialCode": "def safe_integer_offset_8(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_8(text):\n    try:\n        return int(text) + 8\n    except (TypeError, ValueError):\n        return 8\n\nprint(safe_integer_offset_8(\"5\"))  # Expected: 13\nprint(safe_integer_offset_8(\"bad\"))  # Expected: 8\n\n# Example 2: named wrapper approach\ndef solve_problem_7365(text):\n    return safe_integer_offset_8(text)\n\n# Example 3: static method approach\nclass Problem7365Solution:\n    @staticmethod\n    def safe_integer_offset_8(text):\n        try:\n            return int(text) + 8\n        except (TypeError, ValueError):\n            return 8\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_8(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_8(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7366,
    "title": "Problem 7366",
    "description": "Write a Python function called `safe_integer_offset_9` that must convert text to an integer plus 9, or return 9 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_9(\"5\") -> 14\n  safe_integer_offset_9(\"bad\") -> 9",
    "initialCode": "def safe_integer_offset_9(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_9(text):\n    try:\n        return int(text) + 9\n    except (TypeError, ValueError):\n        return 9\n\nprint(safe_integer_offset_9(\"5\"))  # Expected: 14\nprint(safe_integer_offset_9(\"bad\"))  # Expected: 9\n\n# Example 2: named wrapper approach\ndef solve_problem_7366(text):\n    return safe_integer_offset_9(text)\n\n# Example 3: static method approach\nclass Problem7366Solution:\n    @staticmethod\n    def safe_integer_offset_9(text):\n        try:\n            return int(text) + 9\n        except (TypeError, ValueError):\n            return 9\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_9(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_9(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7367,
    "title": "Problem 7367",
    "description": "Write a Python function called `safe_integer_offset_10` that must convert text to an integer plus 10, or return 10 when conversion fails. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_integer_offset_10(\"5\") -> 15\n  safe_integer_offset_10(\"bad\") -> 10",
    "initialCode": "def safe_integer_offset_10(text):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_integer_offset_10(text):\n    try:\n        return int(text) + 10\n    except (TypeError, ValueError):\n        return 10\n\nprint(safe_integer_offset_10(\"5\"))  # Expected: 15\nprint(safe_integer_offset_10(\"bad\"))  # Expected: 10\n\n# Example 2: named wrapper approach\ndef solve_problem_7367(text):\n    return safe_integer_offset_10(text)\n\n# Example 3: static method approach\nclass Problem7367Solution:\n    @staticmethod\n    def safe_integer_offset_10(text):\n        try:\n            return int(text) + 10\n        except (TypeError, ValueError):\n            return 10\n\n# Example 4: assigned result approach\nresult = safe_integer_offset_10(\"5\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_integer_offset_10(None))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7368,
    "title": "Problem 7368",
    "description": "Write a Python function called `safe_division_1` that must divide value by divisor and add 1, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_1(10, 2) -> 6\n  safe_division_1(5, 0) -> None",
    "initialCode": "def safe_division_1(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_1(value, divisor):\n    try:\n        return value / divisor + 1\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_1(10, 2))  # Expected: 6\nprint(safe_division_1(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7368(value, divisor):\n    return safe_division_1(value, divisor)\n\n# Example 3: static method approach\nclass Problem7368Solution:\n    @staticmethod\n    def safe_division_1(value, divisor):\n        try:\n            return value / divisor + 1\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_1(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_1(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7369,
    "title": "Problem 7369",
    "description": "Write a Python function called `safe_division_2` that must divide value by divisor and add 2, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_2(10, 2) -> 7\n  safe_division_2(5, 0) -> None",
    "initialCode": "def safe_division_2(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_2(value, divisor):\n    try:\n        return value / divisor + 2\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_2(10, 2))  # Expected: 7\nprint(safe_division_2(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7369(value, divisor):\n    return safe_division_2(value, divisor)\n\n# Example 3: static method approach\nclass Problem7369Solution:\n    @staticmethod\n    def safe_division_2(value, divisor):\n        try:\n            return value / divisor + 2\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_2(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_2(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7370,
    "title": "Problem 7370",
    "description": "Write a Python function called `safe_division_3` that must divide value by divisor and add 3, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_3(10, 2) -> 8\n  safe_division_3(5, 0) -> None",
    "initialCode": "def safe_division_3(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_3(value, divisor):\n    try:\n        return value / divisor + 3\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_3(10, 2))  # Expected: 8\nprint(safe_division_3(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7370(value, divisor):\n    return safe_division_3(value, divisor)\n\n# Example 3: static method approach\nclass Problem7370Solution:\n    @staticmethod\n    def safe_division_3(value, divisor):\n        try:\n            return value / divisor + 3\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_3(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_3(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7371,
    "title": "Problem 7371",
    "description": "Write a Python function called `safe_division_4` that must divide value by divisor and add 4, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_4(10, 2) -> 9\n  safe_division_4(5, 0) -> None",
    "initialCode": "def safe_division_4(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_4(value, divisor):\n    try:\n        return value / divisor + 4\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_4(10, 2))  # Expected: 9\nprint(safe_division_4(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7371(value, divisor):\n    return safe_division_4(value, divisor)\n\n# Example 3: static method approach\nclass Problem7371Solution:\n    @staticmethod\n    def safe_division_4(value, divisor):\n        try:\n            return value / divisor + 4\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_4(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_4(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7372,
    "title": "Problem 7372",
    "description": "Write a Python function called `safe_division_5` that must divide value by divisor and add 5, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_5(10, 2) -> 10\n  safe_division_5(5, 0) -> None",
    "initialCode": "def safe_division_5(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_5(value, divisor):\n    try:\n        return value / divisor + 5\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_5(10, 2))  # Expected: 10\nprint(safe_division_5(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7372(value, divisor):\n    return safe_division_5(value, divisor)\n\n# Example 3: static method approach\nclass Problem7372Solution:\n    @staticmethod\n    def safe_division_5(value, divisor):\n        try:\n            return value / divisor + 5\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_5(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_5(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7373,
    "title": "Problem 7373",
    "description": "Write a Python function called `safe_division_6` that must divide value by divisor and add 6, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_6(10, 2) -> 11\n  safe_division_6(5, 0) -> None",
    "initialCode": "def safe_division_6(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_6(value, divisor):\n    try:\n        return value / divisor + 6\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_6(10, 2))  # Expected: 11\nprint(safe_division_6(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7373(value, divisor):\n    return safe_division_6(value, divisor)\n\n# Example 3: static method approach\nclass Problem7373Solution:\n    @staticmethod\n    def safe_division_6(value, divisor):\n        try:\n            return value / divisor + 6\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_6(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_6(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7374,
    "title": "Problem 7374",
    "description": "Write a Python function called `safe_division_7` that must divide value by divisor and add 7, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_7(10, 2) -> 12\n  safe_division_7(5, 0) -> None",
    "initialCode": "def safe_division_7(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_7(value, divisor):\n    try:\n        return value / divisor + 7\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_7(10, 2))  # Expected: 12\nprint(safe_division_7(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7374(value, divisor):\n    return safe_division_7(value, divisor)\n\n# Example 3: static method approach\nclass Problem7374Solution:\n    @staticmethod\n    def safe_division_7(value, divisor):\n        try:\n            return value / divisor + 7\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_7(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_7(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7375,
    "title": "Problem 7375",
    "description": "Write a Python function called `safe_division_8` that must divide value by divisor and add 8, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_8(10, 2) -> 13\n  safe_division_8(5, 0) -> None",
    "initialCode": "def safe_division_8(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_8(value, divisor):\n    try:\n        return value / divisor + 8\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_8(10, 2))  # Expected: 13\nprint(safe_division_8(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7375(value, divisor):\n    return safe_division_8(value, divisor)\n\n# Example 3: static method approach\nclass Problem7375Solution:\n    @staticmethod\n    def safe_division_8(value, divisor):\n        try:\n            return value / divisor + 8\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_8(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_8(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7376,
    "title": "Problem 7376",
    "description": "Write a Python function called `safe_division_9` that must divide value by divisor and add 9, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_9(10, 2) -> 14\n  safe_division_9(5, 0) -> None",
    "initialCode": "def safe_division_9(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_9(value, divisor):\n    try:\n        return value / divisor + 9\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_9(10, 2))  # Expected: 14\nprint(safe_division_9(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7376(value, divisor):\n    return safe_division_9(value, divisor)\n\n# Example 3: static method approach\nclass Problem7376Solution:\n    @staticmethod\n    def safe_division_9(value, divisor):\n        try:\n            return value / divisor + 9\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_9(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_9(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7377,
    "title": "Problem 7377",
    "description": "Write a Python function called `safe_division_10` that must divide value by divisor and add 10, returning None for invalid division. Practice exceptions.\nDifficulty: Easy.\nExamples:\n  safe_division_10(10, 2) -> 15\n  safe_division_10(5, 0) -> None",
    "initialCode": "def safe_division_10(value, divisor):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_division_10(value, divisor):\n    try:\n        return value / divisor + 10\n    except (TypeError, ZeroDivisionError):\n        return None\n\nprint(safe_division_10(10, 2))  # Expected: 15\nprint(safe_division_10(5, 0))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7377(value, divisor):\n    return safe_division_10(value, divisor)\n\n# Example 3: static method approach\nclass Problem7377Solution:\n    @staticmethod\n    def safe_division_10(value, divisor):\n        try:\n            return value / divisor + 10\n        except (TypeError, ZeroDivisionError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_division_10(10, 2)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_division_10(\"x\", 2))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Easy"
  },
  {
    "id": 7378,
    "title": "Problem 7378",
    "description": "Write a Python function called `safe_list_item_1` that must return a list item plus 1, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_1([1, 5], 1) -> 6\n  safe_list_item_1([1], 9) -> None",
    "initialCode": "def safe_list_item_1(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_1(values, index):\n    try:\n        return values[index] + 1\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_1([1, 5], 1))  # Expected: 6\nprint(safe_list_item_1([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7378(values, index):\n    return safe_list_item_1(values, index)\n\n# Example 3: static method approach\nclass Problem7378Solution:\n    @staticmethod\n    def safe_list_item_1(values, index):\n        try:\n            return values[index] + 1\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_1([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_1([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7379,
    "title": "Problem 7379",
    "description": "Write a Python function called `safe_list_item_2` that must return a list item plus 2, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_2([1, 5], 1) -> 7\n  safe_list_item_2([1], 9) -> None",
    "initialCode": "def safe_list_item_2(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_2(values, index):\n    try:\n        return values[index] + 2\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_2([1, 5], 1))  # Expected: 7\nprint(safe_list_item_2([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7379(values, index):\n    return safe_list_item_2(values, index)\n\n# Example 3: static method approach\nclass Problem7379Solution:\n    @staticmethod\n    def safe_list_item_2(values, index):\n        try:\n            return values[index] + 2\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_2([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_2([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7380,
    "title": "Problem 7380",
    "description": "Write a Python function called `safe_list_item_3` that must return a list item plus 3, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_3([1, 5], 1) -> 8\n  safe_list_item_3([1], 9) -> None",
    "initialCode": "def safe_list_item_3(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_3(values, index):\n    try:\n        return values[index] + 3\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_3([1, 5], 1))  # Expected: 8\nprint(safe_list_item_3([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7380(values, index):\n    return safe_list_item_3(values, index)\n\n# Example 3: static method approach\nclass Problem7380Solution:\n    @staticmethod\n    def safe_list_item_3(values, index):\n        try:\n            return values[index] + 3\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_3([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_3([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7381,
    "title": "Problem 7381",
    "description": "Write a Python function called `safe_list_item_4` that must return a list item plus 4, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_4([1, 5], 1) -> 9\n  safe_list_item_4([1], 9) -> None",
    "initialCode": "def safe_list_item_4(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_4(values, index):\n    try:\n        return values[index] + 4\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_4([1, 5], 1))  # Expected: 9\nprint(safe_list_item_4([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7381(values, index):\n    return safe_list_item_4(values, index)\n\n# Example 3: static method approach\nclass Problem7381Solution:\n    @staticmethod\n    def safe_list_item_4(values, index):\n        try:\n            return values[index] + 4\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_4([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_4([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7382,
    "title": "Problem 7382",
    "description": "Write a Python function called `safe_list_item_5` that must return a list item plus 5, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_5([1, 5], 1) -> 10\n  safe_list_item_5([1], 9) -> None",
    "initialCode": "def safe_list_item_5(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_5(values, index):\n    try:\n        return values[index] + 5\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_5([1, 5], 1))  # Expected: 10\nprint(safe_list_item_5([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7382(values, index):\n    return safe_list_item_5(values, index)\n\n# Example 3: static method approach\nclass Problem7382Solution:\n    @staticmethod\n    def safe_list_item_5(values, index):\n        try:\n            return values[index] + 5\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_5([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_5([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7383,
    "title": "Problem 7383",
    "description": "Write a Python function called `safe_list_item_6` that must return a list item plus 6, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_6([1, 5], 1) -> 11\n  safe_list_item_6([1], 9) -> None",
    "initialCode": "def safe_list_item_6(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_6(values, index):\n    try:\n        return values[index] + 6\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_6([1, 5], 1))  # Expected: 11\nprint(safe_list_item_6([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7383(values, index):\n    return safe_list_item_6(values, index)\n\n# Example 3: static method approach\nclass Problem7383Solution:\n    @staticmethod\n    def safe_list_item_6(values, index):\n        try:\n            return values[index] + 6\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_6([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_6([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7384,
    "title": "Problem 7384",
    "description": "Write a Python function called `safe_list_item_7` that must return a list item plus 7, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_7([1, 5], 1) -> 12\n  safe_list_item_7([1], 9) -> None",
    "initialCode": "def safe_list_item_7(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_7(values, index):\n    try:\n        return values[index] + 7\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_7([1, 5], 1))  # Expected: 12\nprint(safe_list_item_7([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7384(values, index):\n    return safe_list_item_7(values, index)\n\n# Example 3: static method approach\nclass Problem7384Solution:\n    @staticmethod\n    def safe_list_item_7(values, index):\n        try:\n            return values[index] + 7\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_7([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_7([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7385,
    "title": "Problem 7385",
    "description": "Write a Python function called `safe_list_item_8` that must return a list item plus 8, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_8([1, 5], 1) -> 13\n  safe_list_item_8([1], 9) -> None",
    "initialCode": "def safe_list_item_8(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_8(values, index):\n    try:\n        return values[index] + 8\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_8([1, 5], 1))  # Expected: 13\nprint(safe_list_item_8([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7385(values, index):\n    return safe_list_item_8(values, index)\n\n# Example 3: static method approach\nclass Problem7385Solution:\n    @staticmethod\n    def safe_list_item_8(values, index):\n        try:\n            return values[index] + 8\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_8([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_8([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7386,
    "title": "Problem 7386",
    "description": "Write a Python function called `safe_list_item_9` that must return a list item plus 9, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_9([1, 5], 1) -> 14\n  safe_list_item_9([1], 9) -> None",
    "initialCode": "def safe_list_item_9(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_9(values, index):\n    try:\n        return values[index] + 9\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_9([1, 5], 1))  # Expected: 14\nprint(safe_list_item_9([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7386(values, index):\n    return safe_list_item_9(values, index)\n\n# Example 3: static method approach\nclass Problem7386Solution:\n    @staticmethod\n    def safe_list_item_9(values, index):\n        try:\n            return values[index] + 9\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_9([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_9([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7387,
    "title": "Problem 7387",
    "description": "Write a Python function called `safe_list_item_10` that must return a list item plus 10, or None for an invalid index or value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_list_item_10([1, 5], 1) -> 15\n  safe_list_item_10([1], 9) -> None",
    "initialCode": "def safe_list_item_10(values, index):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_list_item_10(values, index):\n    try:\n        return values[index] + 10\n    except (IndexError, TypeError):\n        return None\n\nprint(safe_list_item_10([1, 5], 1))  # Expected: 15\nprint(safe_list_item_10([1], 9))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7387(values, index):\n    return safe_list_item_10(values, index)\n\n# Example 3: static method approach\nclass Problem7387Solution:\n    @staticmethod\n    def safe_list_item_10(values, index):\n        try:\n            return values[index] + 10\n        except (IndexError, TypeError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_list_item_10([1, 5], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_list_item_10([\"x\"], 0))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7388,
    "title": "Problem 7388",
    "description": "Write a Python function called `safe_mapping_value_1` that must return a numeric mapping value plus 1, or 1 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_1({\"a\": 2}, \"a\") -> 3\n  safe_mapping_value_1({}, \"x\") -> 1",
    "initialCode": "def safe_mapping_value_1(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_1(mapping, key):\n    try:\n        return mapping[key] + 1\n    except (KeyError, TypeError):\n        return 1\n\nprint(safe_mapping_value_1({\"a\": 2}, \"a\"))  # Expected: 3\nprint(safe_mapping_value_1({}, \"x\"))  # Expected: 1\n\n# Example 2: named wrapper approach\ndef solve_problem_7388(mapping, key):\n    return safe_mapping_value_1(mapping, key)\n\n# Example 3: static method approach\nclass Problem7388Solution:\n    @staticmethod\n    def safe_mapping_value_1(mapping, key):\n        try:\n            return mapping[key] + 1\n        except (KeyError, TypeError):\n            return 1\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_1({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_1({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7389,
    "title": "Problem 7389",
    "description": "Write a Python function called `safe_mapping_value_2` that must return a numeric mapping value plus 2, or 2 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_2({\"a\": 2}, \"a\") -> 4\n  safe_mapping_value_2({}, \"x\") -> 2",
    "initialCode": "def safe_mapping_value_2(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_2(mapping, key):\n    try:\n        return mapping[key] + 2\n    except (KeyError, TypeError):\n        return 2\n\nprint(safe_mapping_value_2({\"a\": 2}, \"a\"))  # Expected: 4\nprint(safe_mapping_value_2({}, \"x\"))  # Expected: 2\n\n# Example 2: named wrapper approach\ndef solve_problem_7389(mapping, key):\n    return safe_mapping_value_2(mapping, key)\n\n# Example 3: static method approach\nclass Problem7389Solution:\n    @staticmethod\n    def safe_mapping_value_2(mapping, key):\n        try:\n            return mapping[key] + 2\n        except (KeyError, TypeError):\n            return 2\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_2({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_2({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7390,
    "title": "Problem 7390",
    "description": "Write a Python function called `safe_mapping_value_3` that must return a numeric mapping value plus 3, or 3 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_3({\"a\": 2}, \"a\") -> 5\n  safe_mapping_value_3({}, \"x\") -> 3",
    "initialCode": "def safe_mapping_value_3(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_3(mapping, key):\n    try:\n        return mapping[key] + 3\n    except (KeyError, TypeError):\n        return 3\n\nprint(safe_mapping_value_3({\"a\": 2}, \"a\"))  # Expected: 5\nprint(safe_mapping_value_3({}, \"x\"))  # Expected: 3\n\n# Example 2: named wrapper approach\ndef solve_problem_7390(mapping, key):\n    return safe_mapping_value_3(mapping, key)\n\n# Example 3: static method approach\nclass Problem7390Solution:\n    @staticmethod\n    def safe_mapping_value_3(mapping, key):\n        try:\n            return mapping[key] + 3\n        except (KeyError, TypeError):\n            return 3\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_3({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_3({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7391,
    "title": "Problem 7391",
    "description": "Write a Python function called `safe_mapping_value_4` that must return a numeric mapping value plus 4, or 4 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_4({\"a\": 2}, \"a\") -> 6\n  safe_mapping_value_4({}, \"x\") -> 4",
    "initialCode": "def safe_mapping_value_4(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_4(mapping, key):\n    try:\n        return mapping[key] + 4\n    except (KeyError, TypeError):\n        return 4\n\nprint(safe_mapping_value_4({\"a\": 2}, \"a\"))  # Expected: 6\nprint(safe_mapping_value_4({}, \"x\"))  # Expected: 4\n\n# Example 2: named wrapper approach\ndef solve_problem_7391(mapping, key):\n    return safe_mapping_value_4(mapping, key)\n\n# Example 3: static method approach\nclass Problem7391Solution:\n    @staticmethod\n    def safe_mapping_value_4(mapping, key):\n        try:\n            return mapping[key] + 4\n        except (KeyError, TypeError):\n            return 4\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_4({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_4({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7392,
    "title": "Problem 7392",
    "description": "Write a Python function called `safe_mapping_value_5` that must return a numeric mapping value plus 5, or 5 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_5({\"a\": 2}, \"a\") -> 7\n  safe_mapping_value_5({}, \"x\") -> 5",
    "initialCode": "def safe_mapping_value_5(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_5(mapping, key):\n    try:\n        return mapping[key] + 5\n    except (KeyError, TypeError):\n        return 5\n\nprint(safe_mapping_value_5({\"a\": 2}, \"a\"))  # Expected: 7\nprint(safe_mapping_value_5({}, \"x\"))  # Expected: 5\n\n# Example 2: named wrapper approach\ndef solve_problem_7392(mapping, key):\n    return safe_mapping_value_5(mapping, key)\n\n# Example 3: static method approach\nclass Problem7392Solution:\n    @staticmethod\n    def safe_mapping_value_5(mapping, key):\n        try:\n            return mapping[key] + 5\n        except (KeyError, TypeError):\n            return 5\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_5({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_5({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7393,
    "title": "Problem 7393",
    "description": "Write a Python function called `safe_mapping_value_6` that must return a numeric mapping value plus 6, or 6 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_6({\"a\": 2}, \"a\") -> 8\n  safe_mapping_value_6({}, \"x\") -> 6",
    "initialCode": "def safe_mapping_value_6(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_6(mapping, key):\n    try:\n        return mapping[key] + 6\n    except (KeyError, TypeError):\n        return 6\n\nprint(safe_mapping_value_6({\"a\": 2}, \"a\"))  # Expected: 8\nprint(safe_mapping_value_6({}, \"x\"))  # Expected: 6\n\n# Example 2: named wrapper approach\ndef solve_problem_7393(mapping, key):\n    return safe_mapping_value_6(mapping, key)\n\n# Example 3: static method approach\nclass Problem7393Solution:\n    @staticmethod\n    def safe_mapping_value_6(mapping, key):\n        try:\n            return mapping[key] + 6\n        except (KeyError, TypeError):\n            return 6\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_6({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_6({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7394,
    "title": "Problem 7394",
    "description": "Write a Python function called `safe_mapping_value_7` that must return a numeric mapping value plus 7, or 7 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_7({\"a\": 2}, \"a\") -> 9\n  safe_mapping_value_7({}, \"x\") -> 7",
    "initialCode": "def safe_mapping_value_7(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_7(mapping, key):\n    try:\n        return mapping[key] + 7\n    except (KeyError, TypeError):\n        return 7\n\nprint(safe_mapping_value_7({\"a\": 2}, \"a\"))  # Expected: 9\nprint(safe_mapping_value_7({}, \"x\"))  # Expected: 7\n\n# Example 2: named wrapper approach\ndef solve_problem_7394(mapping, key):\n    return safe_mapping_value_7(mapping, key)\n\n# Example 3: static method approach\nclass Problem7394Solution:\n    @staticmethod\n    def safe_mapping_value_7(mapping, key):\n        try:\n            return mapping[key] + 7\n        except (KeyError, TypeError):\n            return 7\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_7({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_7({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7395,
    "title": "Problem 7395",
    "description": "Write a Python function called `safe_mapping_value_8` that must return a numeric mapping value plus 8, or 8 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_8({\"a\": 2}, \"a\") -> 10\n  safe_mapping_value_8({}, \"x\") -> 8",
    "initialCode": "def safe_mapping_value_8(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_8(mapping, key):\n    try:\n        return mapping[key] + 8\n    except (KeyError, TypeError):\n        return 8\n\nprint(safe_mapping_value_8({\"a\": 2}, \"a\"))  # Expected: 10\nprint(safe_mapping_value_8({}, \"x\"))  # Expected: 8\n\n# Example 2: named wrapper approach\ndef solve_problem_7395(mapping, key):\n    return safe_mapping_value_8(mapping, key)\n\n# Example 3: static method approach\nclass Problem7395Solution:\n    @staticmethod\n    def safe_mapping_value_8(mapping, key):\n        try:\n            return mapping[key] + 8\n        except (KeyError, TypeError):\n            return 8\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_8({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_8({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7396,
    "title": "Problem 7396",
    "description": "Write a Python function called `safe_mapping_value_9` that must return a numeric mapping value plus 9, or 9 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_9({\"a\": 2}, \"a\") -> 11\n  safe_mapping_value_9({}, \"x\") -> 9",
    "initialCode": "def safe_mapping_value_9(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_9(mapping, key):\n    try:\n        return mapping[key] + 9\n    except (KeyError, TypeError):\n        return 9\n\nprint(safe_mapping_value_9({\"a\": 2}, \"a\"))  # Expected: 11\nprint(safe_mapping_value_9({}, \"x\"))  # Expected: 9\n\n# Example 2: named wrapper approach\ndef solve_problem_7396(mapping, key):\n    return safe_mapping_value_9(mapping, key)\n\n# Example 3: static method approach\nclass Problem7396Solution:\n    @staticmethod\n    def safe_mapping_value_9(mapping, key):\n        try:\n            return mapping[key] + 9\n        except (KeyError, TypeError):\n            return 9\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_9({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_9({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7397,
    "title": "Problem 7397",
    "description": "Write a Python function called `safe_mapping_value_10` that must return a numeric mapping value plus 10, or 10 for a missing or invalid value. Practice exceptions.\nDifficulty: Intermediate.\nExamples:\n  safe_mapping_value_10({\"a\": 2}, \"a\") -> 12\n  safe_mapping_value_10({}, \"x\") -> 10",
    "initialCode": "def safe_mapping_value_10(mapping, key):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef safe_mapping_value_10(mapping, key):\n    try:\n        return mapping[key] + 10\n    except (KeyError, TypeError):\n        return 10\n\nprint(safe_mapping_value_10({\"a\": 2}, \"a\"))  # Expected: 12\nprint(safe_mapping_value_10({}, \"x\"))  # Expected: 10\n\n# Example 2: named wrapper approach\ndef solve_problem_7397(mapping, key):\n    return safe_mapping_value_10(mapping, key)\n\n# Example 3: static method approach\nclass Problem7397Solution:\n    @staticmethod\n    def safe_mapping_value_10(mapping, key):\n        try:\n            return mapping[key] + 10\n        except (KeyError, TypeError):\n            return 10\n\n# Example 4: assigned result approach\nresult = safe_mapping_value_10({\"a\": 2}, \"a\")\nprint(result)\n\n# Example 5: boundary case\nprint(safe_mapping_value_10({\"x\": \"bad\"}, \"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Intermediate"
  },
  {
    "id": 7398,
    "title": "Problem 7398",
    "description": "Write a Python function called `safe_square_root_1` that must return square root plus 1, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_1(9) -> 4\n  safe_square_root_1(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_1(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_1(value):\n    try:\n        return math.sqrt(value) + 1\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_1(9))  # Expected: 4\nprint(safe_square_root_1(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7398(value):\n    return safe_square_root_1(value)\n\n# Example 3: static method approach\nclass Problem7398Solution:\n    @staticmethod\n    def safe_square_root_1(value):\n        try:\n            return math.sqrt(value) + 1\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_1(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_1(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7399,
    "title": "Problem 7399",
    "description": "Write a Python function called `safe_square_root_2` that must return square root plus 2, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_2(9) -> 5\n  safe_square_root_2(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_2(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_2(value):\n    try:\n        return math.sqrt(value) + 2\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_2(9))  # Expected: 5\nprint(safe_square_root_2(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7399(value):\n    return safe_square_root_2(value)\n\n# Example 3: static method approach\nclass Problem7399Solution:\n    @staticmethod\n    def safe_square_root_2(value):\n        try:\n            return math.sqrt(value) + 2\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_2(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_2(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7400,
    "title": "Problem 7400",
    "description": "Write a Python function called `safe_square_root_3` that must return square root plus 3, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_3(9) -> 6\n  safe_square_root_3(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_3(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_3(value):\n    try:\n        return math.sqrt(value) + 3\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_3(9))  # Expected: 6\nprint(safe_square_root_3(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7400(value):\n    return safe_square_root_3(value)\n\n# Example 3: static method approach\nclass Problem7400Solution:\n    @staticmethod\n    def safe_square_root_3(value):\n        try:\n            return math.sqrt(value) + 3\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_3(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_3(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7401,
    "title": "Problem 7401",
    "description": "Write a Python function called `safe_square_root_4` that must return square root plus 4, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_4(9) -> 7\n  safe_square_root_4(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_4(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_4(value):\n    try:\n        return math.sqrt(value) + 4\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_4(9))  # Expected: 7\nprint(safe_square_root_4(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7401(value):\n    return safe_square_root_4(value)\n\n# Example 3: static method approach\nclass Problem7401Solution:\n    @staticmethod\n    def safe_square_root_4(value):\n        try:\n            return math.sqrt(value) + 4\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_4(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_4(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7402,
    "title": "Problem 7402",
    "description": "Write a Python function called `safe_square_root_5` that must return square root plus 5, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_5(9) -> 8\n  safe_square_root_5(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_5(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_5(value):\n    try:\n        return math.sqrt(value) + 5\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_5(9))  # Expected: 8\nprint(safe_square_root_5(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7402(value):\n    return safe_square_root_5(value)\n\n# Example 3: static method approach\nclass Problem7402Solution:\n    @staticmethod\n    def safe_square_root_5(value):\n        try:\n            return math.sqrt(value) + 5\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_5(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_5(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7403,
    "title": "Problem 7403",
    "description": "Write a Python function called `safe_square_root_6` that must return square root plus 6, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_6(9) -> 9\n  safe_square_root_6(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_6(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_6(value):\n    try:\n        return math.sqrt(value) + 6\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_6(9))  # Expected: 9\nprint(safe_square_root_6(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7403(value):\n    return safe_square_root_6(value)\n\n# Example 3: static method approach\nclass Problem7403Solution:\n    @staticmethod\n    def safe_square_root_6(value):\n        try:\n            return math.sqrt(value) + 6\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_6(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_6(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7404,
    "title": "Problem 7404",
    "description": "Write a Python function called `safe_square_root_7` that must return square root plus 7, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_7(9) -> 10\n  safe_square_root_7(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_7(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_7(value):\n    try:\n        return math.sqrt(value) + 7\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_7(9))  # Expected: 10\nprint(safe_square_root_7(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7404(value):\n    return safe_square_root_7(value)\n\n# Example 3: static method approach\nclass Problem7404Solution:\n    @staticmethod\n    def safe_square_root_7(value):\n        try:\n            return math.sqrt(value) + 7\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_7(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_7(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7405,
    "title": "Problem 7405",
    "description": "Write a Python function called `safe_square_root_8` that must return square root plus 8, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_8(9) -> 11\n  safe_square_root_8(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_8(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_8(value):\n    try:\n        return math.sqrt(value) + 8\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_8(9))  # Expected: 11\nprint(safe_square_root_8(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7405(value):\n    return safe_square_root_8(value)\n\n# Example 3: static method approach\nclass Problem7405Solution:\n    @staticmethod\n    def safe_square_root_8(value):\n        try:\n            return math.sqrt(value) + 8\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_8(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_8(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7406,
    "title": "Problem 7406",
    "description": "Write a Python function called `safe_square_root_9` that must return square root plus 9, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_9(9) -> 12\n  safe_square_root_9(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_9(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_9(value):\n    try:\n        return math.sqrt(value) + 9\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_9(9))  # Expected: 12\nprint(safe_square_root_9(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7406(value):\n    return safe_square_root_9(value)\n\n# Example 3: static method approach\nclass Problem7406Solution:\n    @staticmethod\n    def safe_square_root_9(value):\n        try:\n            return math.sqrt(value) + 9\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_9(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_9(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7407,
    "title": "Problem 7407",
    "description": "Write a Python function called `safe_square_root_10` that must return square root plus 10, or None for a negative or invalid value. Practice exceptions.\nDifficulty: Expert.\nExamples:\n  safe_square_root_10(9) -> 13\n  safe_square_root_10(-1) -> None",
    "initialCode": "import math\n\ndef safe_square_root_10(value):\n    pass",
    "solution": "import math\n\n# Example 1: canonical function approach\ndef safe_square_root_10(value):\n    try:\n        return math.sqrt(value) + 10\n    except (TypeError, ValueError):\n        return None\n\nprint(safe_square_root_10(9))  # Expected: 13\nprint(safe_square_root_10(-1))  # Expected: None\n\n# Example 2: named wrapper approach\ndef solve_problem_7407(value):\n    return safe_square_root_10(value)\n\n# Example 3: static method approach\nclass Problem7407Solution:\n    @staticmethod\n    def safe_square_root_10(value):\n        try:\n            return math.sqrt(value) + 10\n        except (TypeError, ValueError):\n            return None\n\n# Example 4: assigned result approach\nresult = safe_square_root_10(9)\nprint(result)\n\n# Example 5: boundary case\nprint(safe_square_root_10(\"x\"))",
    "hint": "Focus on the exact operation that may fail, narrow exception types, fallback behavior, and successful return path. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required exceptions rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Exceptions Difficult"
  },
  {
    "id": 7408,
    "title": "Problem 7408",
    "description": "Write a Python function called `normalized_text_equal_1` that must compare text after trimming and casefolding, variant 1. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_1(\" Python \", \"python\") -> True\n  normalized_text_equal_1(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_1(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_1(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_1(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7408(left, right):\n    return normalized_text_equal_1(left, right)\n\n# Example 3: static method approach\nclass Problem7408Solution:\n    @staticmethod\n    def normalized_text_equal_1(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_1(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_1(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7409,
    "title": "Problem 7409",
    "description": "Write a Python function called `normalized_text_equal_2` that must compare text after trimming and casefolding, variant 2. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_2(\" Python \", \"python\") -> True\n  normalized_text_equal_2(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_2(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_2(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_2(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7409(left, right):\n    return normalized_text_equal_2(left, right)\n\n# Example 3: static method approach\nclass Problem7409Solution:\n    @staticmethod\n    def normalized_text_equal_2(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_2(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_2(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7410,
    "title": "Problem 7410",
    "description": "Write a Python function called `normalized_text_equal_3` that must compare text after trimming and casefolding, variant 3. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_3(\" Python \", \"python\") -> True\n  normalized_text_equal_3(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_3(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_3(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_3(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7410(left, right):\n    return normalized_text_equal_3(left, right)\n\n# Example 3: static method approach\nclass Problem7410Solution:\n    @staticmethod\n    def normalized_text_equal_3(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_3(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_3(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7411,
    "title": "Problem 7411",
    "description": "Write a Python function called `normalized_text_equal_4` that must compare text after trimming and casefolding, variant 4. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_4(\" Python \", \"python\") -> True\n  normalized_text_equal_4(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_4(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_4(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_4(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7411(left, right):\n    return normalized_text_equal_4(left, right)\n\n# Example 3: static method approach\nclass Problem7411Solution:\n    @staticmethod\n    def normalized_text_equal_4(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_4(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_4(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7412,
    "title": "Problem 7412",
    "description": "Write a Python function called `normalized_text_equal_5` that must compare text after trimming and casefolding, variant 5. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_5(\" Python \", \"python\") -> True\n  normalized_text_equal_5(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_5(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_5(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_5(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7412(left, right):\n    return normalized_text_equal_5(left, right)\n\n# Example 3: static method approach\nclass Problem7412Solution:\n    @staticmethod\n    def normalized_text_equal_5(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_5(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_5(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7413,
    "title": "Problem 7413",
    "description": "Write a Python function called `normalized_text_equal_6` that must compare text after trimming and casefolding, variant 6. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_6(\" Python \", \"python\") -> True\n  normalized_text_equal_6(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_6(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_6(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_6(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7413(left, right):\n    return normalized_text_equal_6(left, right)\n\n# Example 3: static method approach\nclass Problem7413Solution:\n    @staticmethod\n    def normalized_text_equal_6(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_6(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_6(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7414,
    "title": "Problem 7414",
    "description": "Write a Python function called `normalized_text_equal_7` that must compare text after trimming and casefolding, variant 7. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_7(\" Python \", \"python\") -> True\n  normalized_text_equal_7(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_7(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_7(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_7(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7414(left, right):\n    return normalized_text_equal_7(left, right)\n\n# Example 3: static method approach\nclass Problem7414Solution:\n    @staticmethod\n    def normalized_text_equal_7(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_7(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_7(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7415,
    "title": "Problem 7415",
    "description": "Write a Python function called `normalized_text_equal_8` that must compare text after trimming and casefolding, variant 8. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_8(\" Python \", \"python\") -> True\n  normalized_text_equal_8(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_8(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_8(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_8(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7415(left, right):\n    return normalized_text_equal_8(left, right)\n\n# Example 3: static method approach\nclass Problem7415Solution:\n    @staticmethod\n    def normalized_text_equal_8(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_8(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_8(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7416,
    "title": "Problem 7416",
    "description": "Write a Python function called `normalized_text_equal_9` that must compare text after trimming and casefolding, variant 9. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_9(\" Python \", \"python\") -> True\n  normalized_text_equal_9(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_9(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_9(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_9(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7416(left, right):\n    return normalized_text_equal_9(left, right)\n\n# Example 3: static method approach\nclass Problem7416Solution:\n    @staticmethod\n    def normalized_text_equal_9(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_9(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_9(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7417,
    "title": "Problem 7417",
    "description": "Write a Python function called `normalized_text_equal_10` that must compare text after trimming and casefolding, variant 10. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  normalized_text_equal_10(\" Python \", \"python\") -> True\n  normalized_text_equal_10(\"A\", \"b\") -> False",
    "initialCode": "def normalized_text_equal_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef normalized_text_equal_10(left, right):\n    return left.strip().casefold() == right.strip().casefold()\n\nprint(normalized_text_equal_10(\" Python \", \"python\"))  # Expected: True\nprint(normalized_text_equal_10(\"A\", \"b\"))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7417(left, right):\n    return normalized_text_equal_10(left, right)\n\n# Example 3: static method approach\nclass Problem7417Solution:\n    @staticmethod\n    def normalized_text_equal_10(left, right):\n        return left.strip().casefold() == right.strip().casefold()\n\n# Example 4: assigned result approach\nresult = normalized_text_equal_10(\" Python \", \"python\")\nprint(result)\n\n# Example 5: boundary case\nprint(normalized_text_equal_10(\"\", \" \"))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7418,
    "title": "Problem 7418",
    "description": "Write a Python function called `strict_value_equal_1` that must test equal value and identical type, variant 1. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_1(1, 1) -> True\n  strict_value_equal_1(1, True) -> False",
    "initialCode": "def strict_value_equal_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_1(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_1(1, 1))  # Expected: True\nprint(strict_value_equal_1(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7418(left, right):\n    return strict_value_equal_1(left, right)\n\n# Example 3: static method approach\nclass Problem7418Solution:\n    @staticmethod\n    def strict_value_equal_1(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_1(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_1(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7419,
    "title": "Problem 7419",
    "description": "Write a Python function called `strict_value_equal_2` that must test equal value and identical type, variant 2. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_2(1, 1) -> True\n  strict_value_equal_2(1, True) -> False",
    "initialCode": "def strict_value_equal_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_2(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_2(1, 1))  # Expected: True\nprint(strict_value_equal_2(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7419(left, right):\n    return strict_value_equal_2(left, right)\n\n# Example 3: static method approach\nclass Problem7419Solution:\n    @staticmethod\n    def strict_value_equal_2(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_2(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_2(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7420,
    "title": "Problem 7420",
    "description": "Write a Python function called `strict_value_equal_3` that must test equal value and identical type, variant 3. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_3(1, 1) -> True\n  strict_value_equal_3(1, True) -> False",
    "initialCode": "def strict_value_equal_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_3(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_3(1, 1))  # Expected: True\nprint(strict_value_equal_3(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7420(left, right):\n    return strict_value_equal_3(left, right)\n\n# Example 3: static method approach\nclass Problem7420Solution:\n    @staticmethod\n    def strict_value_equal_3(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_3(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_3(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7421,
    "title": "Problem 7421",
    "description": "Write a Python function called `strict_value_equal_4` that must test equal value and identical type, variant 4. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_4(1, 1) -> True\n  strict_value_equal_4(1, True) -> False",
    "initialCode": "def strict_value_equal_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_4(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_4(1, 1))  # Expected: True\nprint(strict_value_equal_4(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7421(left, right):\n    return strict_value_equal_4(left, right)\n\n# Example 3: static method approach\nclass Problem7421Solution:\n    @staticmethod\n    def strict_value_equal_4(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_4(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_4(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7422,
    "title": "Problem 7422",
    "description": "Write a Python function called `strict_value_equal_5` that must test equal value and identical type, variant 5. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_5(1, 1) -> True\n  strict_value_equal_5(1, True) -> False",
    "initialCode": "def strict_value_equal_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_5(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_5(1, 1))  # Expected: True\nprint(strict_value_equal_5(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7422(left, right):\n    return strict_value_equal_5(left, right)\n\n# Example 3: static method approach\nclass Problem7422Solution:\n    @staticmethod\n    def strict_value_equal_5(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_5(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_5(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7423,
    "title": "Problem 7423",
    "description": "Write a Python function called `strict_value_equal_6` that must test equal value and identical type, variant 6. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_6(1, 1) -> True\n  strict_value_equal_6(1, True) -> False",
    "initialCode": "def strict_value_equal_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_6(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_6(1, 1))  # Expected: True\nprint(strict_value_equal_6(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7423(left, right):\n    return strict_value_equal_6(left, right)\n\n# Example 3: static method approach\nclass Problem7423Solution:\n    @staticmethod\n    def strict_value_equal_6(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_6(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_6(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7424,
    "title": "Problem 7424",
    "description": "Write a Python function called `strict_value_equal_7` that must test equal value and identical type, variant 7. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_7(1, 1) -> True\n  strict_value_equal_7(1, True) -> False",
    "initialCode": "def strict_value_equal_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_7(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_7(1, 1))  # Expected: True\nprint(strict_value_equal_7(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7424(left, right):\n    return strict_value_equal_7(left, right)\n\n# Example 3: static method approach\nclass Problem7424Solution:\n    @staticmethod\n    def strict_value_equal_7(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_7(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_7(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7425,
    "title": "Problem 7425",
    "description": "Write a Python function called `strict_value_equal_8` that must test equal value and identical type, variant 8. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_8(1, 1) -> True\n  strict_value_equal_8(1, True) -> False",
    "initialCode": "def strict_value_equal_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_8(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_8(1, 1))  # Expected: True\nprint(strict_value_equal_8(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7425(left, right):\n    return strict_value_equal_8(left, right)\n\n# Example 3: static method approach\nclass Problem7425Solution:\n    @staticmethod\n    def strict_value_equal_8(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_8(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_8(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7426,
    "title": "Problem 7426",
    "description": "Write a Python function called `strict_value_equal_9` that must test equal value and identical type, variant 9. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_9(1, 1) -> True\n  strict_value_equal_9(1, True) -> False",
    "initialCode": "def strict_value_equal_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_9(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_9(1, 1))  # Expected: True\nprint(strict_value_equal_9(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7426(left, right):\n    return strict_value_equal_9(left, right)\n\n# Example 3: static method approach\nclass Problem7426Solution:\n    @staticmethod\n    def strict_value_equal_9(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_9(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_9(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7427,
    "title": "Problem 7427",
    "description": "Write a Python function called `strict_value_equal_10` that must test equal value and identical type, variant 10. Practice equality & identity.\nDifficulty: Easy.\nExamples:\n  strict_value_equal_10(1, 1) -> True\n  strict_value_equal_10(1, True) -> False",
    "initialCode": "def strict_value_equal_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef strict_value_equal_10(left, right):\n    return type(left) is type(right) and left == right\n\nprint(strict_value_equal_10(1, 1))  # Expected: True\nprint(strict_value_equal_10(1, True))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7427(left, right):\n    return strict_value_equal_10(left, right)\n\n# Example 3: static method approach\nclass Problem7427Solution:\n    @staticmethod\n    def strict_value_equal_10(left, right):\n        return type(left) is type(right) and left == right\n\n# Example 4: assigned result approach\nresult = strict_value_equal_10(1, 1)\nprint(result)\n\n# Example 5: boundary case\nprint(strict_value_equal_10(\"1\", 1))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Easy"
  },
  {
    "id": 7428,
    "title": "Problem 7428",
    "description": "Write a Python function called `sequence_equal_1` that must test whether two sequences have equal ordered contents, variant 1. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_1([1, 2], [1, 2]) -> True\n  sequence_equal_1([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_1(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_1([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_1([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7428(left, right):\n    return sequence_equal_1(left, right)\n\n# Example 3: static method approach\nclass Problem7428Solution:\n    @staticmethod\n    def sequence_equal_1(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_1([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_1([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7429,
    "title": "Problem 7429",
    "description": "Write a Python function called `sequence_equal_2` that must test whether two sequences have equal ordered contents, variant 2. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_2([1, 2], [1, 2]) -> True\n  sequence_equal_2([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_2(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_2([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_2([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7429(left, right):\n    return sequence_equal_2(left, right)\n\n# Example 3: static method approach\nclass Problem7429Solution:\n    @staticmethod\n    def sequence_equal_2(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_2([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_2([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7430,
    "title": "Problem 7430",
    "description": "Write a Python function called `sequence_equal_3` that must test whether two sequences have equal ordered contents, variant 3. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_3([1, 2], [1, 2]) -> True\n  sequence_equal_3([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_3(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_3([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_3([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7430(left, right):\n    return sequence_equal_3(left, right)\n\n# Example 3: static method approach\nclass Problem7430Solution:\n    @staticmethod\n    def sequence_equal_3(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_3([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_3([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7431,
    "title": "Problem 7431",
    "description": "Write a Python function called `sequence_equal_4` that must test whether two sequences have equal ordered contents, variant 4. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_4([1, 2], [1, 2]) -> True\n  sequence_equal_4([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_4(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_4([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_4([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7431(left, right):\n    return sequence_equal_4(left, right)\n\n# Example 3: static method approach\nclass Problem7431Solution:\n    @staticmethod\n    def sequence_equal_4(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_4([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_4([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7432,
    "title": "Problem 7432",
    "description": "Write a Python function called `sequence_equal_5` that must test whether two sequences have equal ordered contents, variant 5. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_5([1, 2], [1, 2]) -> True\n  sequence_equal_5([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_5(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_5([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_5([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7432(left, right):\n    return sequence_equal_5(left, right)\n\n# Example 3: static method approach\nclass Problem7432Solution:\n    @staticmethod\n    def sequence_equal_5(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_5([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_5([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7433,
    "title": "Problem 7433",
    "description": "Write a Python function called `sequence_equal_6` that must test whether two sequences have equal ordered contents, variant 6. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_6([1, 2], [1, 2]) -> True\n  sequence_equal_6([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_6(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_6([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_6([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7433(left, right):\n    return sequence_equal_6(left, right)\n\n# Example 3: static method approach\nclass Problem7433Solution:\n    @staticmethod\n    def sequence_equal_6(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_6([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_6([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7434,
    "title": "Problem 7434",
    "description": "Write a Python function called `sequence_equal_7` that must test whether two sequences have equal ordered contents, variant 7. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_7([1, 2], [1, 2]) -> True\n  sequence_equal_7([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_7(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_7([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_7([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7434(left, right):\n    return sequence_equal_7(left, right)\n\n# Example 3: static method approach\nclass Problem7434Solution:\n    @staticmethod\n    def sequence_equal_7(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_7([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_7([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7435,
    "title": "Problem 7435",
    "description": "Write a Python function called `sequence_equal_8` that must test whether two sequences have equal ordered contents, variant 8. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_8([1, 2], [1, 2]) -> True\n  sequence_equal_8([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_8(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_8([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_8([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7435(left, right):\n    return sequence_equal_8(left, right)\n\n# Example 3: static method approach\nclass Problem7435Solution:\n    @staticmethod\n    def sequence_equal_8(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_8([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_8([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7436,
    "title": "Problem 7436",
    "description": "Write a Python function called `sequence_equal_9` that must test whether two sequences have equal ordered contents, variant 9. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_9([1, 2], [1, 2]) -> True\n  sequence_equal_9([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_9(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_9([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_9([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7436(left, right):\n    return sequence_equal_9(left, right)\n\n# Example 3: static method approach\nclass Problem7436Solution:\n    @staticmethod\n    def sequence_equal_9(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_9([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_9([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7437,
    "title": "Problem 7437",
    "description": "Write a Python function called `sequence_equal_10` that must test whether two sequences have equal ordered contents, variant 10. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  sequence_equal_10([1, 2], [1, 2]) -> True\n  sequence_equal_10([1, 2], [2, 1]) -> False",
    "initialCode": "def sequence_equal_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef sequence_equal_10(left, right):\n    return list(left) == list(right)\n\nprint(sequence_equal_10([1, 2], [1, 2]))  # Expected: True\nprint(sequence_equal_10([1, 2], [2, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7437(left, right):\n    return sequence_equal_10(left, right)\n\n# Example 3: static method approach\nclass Problem7437Solution:\n    @staticmethod\n    def sequence_equal_10(left, right):\n        return list(left) == list(right)\n\n# Example 4: assigned result approach\nresult = sequence_equal_10([1, 2], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(sequence_equal_10([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7438,
    "title": "Problem 7438",
    "description": "Write a Python function called `both_none_identity_1` that must use identity to test whether both values are None, variant 1. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_1(None, None) -> True\n  both_none_identity_1(None, 0) -> False",
    "initialCode": "def both_none_identity_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_1(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_1(None, None))  # Expected: True\nprint(both_none_identity_1(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7438(left, right):\n    return both_none_identity_1(left, right)\n\n# Example 3: static method approach\nclass Problem7438Solution:\n    @staticmethod\n    def both_none_identity_1(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_1(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_1(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7439,
    "title": "Problem 7439",
    "description": "Write a Python function called `both_none_identity_2` that must use identity to test whether both values are None, variant 2. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_2(None, None) -> True\n  both_none_identity_2(None, 0) -> False",
    "initialCode": "def both_none_identity_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_2(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_2(None, None))  # Expected: True\nprint(both_none_identity_2(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7439(left, right):\n    return both_none_identity_2(left, right)\n\n# Example 3: static method approach\nclass Problem7439Solution:\n    @staticmethod\n    def both_none_identity_2(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_2(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_2(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7440,
    "title": "Problem 7440",
    "description": "Write a Python function called `both_none_identity_3` that must use identity to test whether both values are None, variant 3. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_3(None, None) -> True\n  both_none_identity_3(None, 0) -> False",
    "initialCode": "def both_none_identity_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_3(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_3(None, None))  # Expected: True\nprint(both_none_identity_3(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7440(left, right):\n    return both_none_identity_3(left, right)\n\n# Example 3: static method approach\nclass Problem7440Solution:\n    @staticmethod\n    def both_none_identity_3(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_3(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_3(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7441,
    "title": "Problem 7441",
    "description": "Write a Python function called `both_none_identity_4` that must use identity to test whether both values are None, variant 4. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_4(None, None) -> True\n  both_none_identity_4(None, 0) -> False",
    "initialCode": "def both_none_identity_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_4(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_4(None, None))  # Expected: True\nprint(both_none_identity_4(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7441(left, right):\n    return both_none_identity_4(left, right)\n\n# Example 3: static method approach\nclass Problem7441Solution:\n    @staticmethod\n    def both_none_identity_4(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_4(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_4(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7442,
    "title": "Problem 7442",
    "description": "Write a Python function called `both_none_identity_5` that must use identity to test whether both values are None, variant 5. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_5(None, None) -> True\n  both_none_identity_5(None, 0) -> False",
    "initialCode": "def both_none_identity_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_5(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_5(None, None))  # Expected: True\nprint(both_none_identity_5(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7442(left, right):\n    return both_none_identity_5(left, right)\n\n# Example 3: static method approach\nclass Problem7442Solution:\n    @staticmethod\n    def both_none_identity_5(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_5(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_5(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7443,
    "title": "Problem 7443",
    "description": "Write a Python function called `both_none_identity_6` that must use identity to test whether both values are None, variant 6. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_6(None, None) -> True\n  both_none_identity_6(None, 0) -> False",
    "initialCode": "def both_none_identity_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_6(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_6(None, None))  # Expected: True\nprint(both_none_identity_6(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7443(left, right):\n    return both_none_identity_6(left, right)\n\n# Example 3: static method approach\nclass Problem7443Solution:\n    @staticmethod\n    def both_none_identity_6(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_6(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_6(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7444,
    "title": "Problem 7444",
    "description": "Write a Python function called `both_none_identity_7` that must use identity to test whether both values are None, variant 7. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_7(None, None) -> True\n  both_none_identity_7(None, 0) -> False",
    "initialCode": "def both_none_identity_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_7(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_7(None, None))  # Expected: True\nprint(both_none_identity_7(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7444(left, right):\n    return both_none_identity_7(left, right)\n\n# Example 3: static method approach\nclass Problem7444Solution:\n    @staticmethod\n    def both_none_identity_7(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_7(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_7(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7445,
    "title": "Problem 7445",
    "description": "Write a Python function called `both_none_identity_8` that must use identity to test whether both values are None, variant 8. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_8(None, None) -> True\n  both_none_identity_8(None, 0) -> False",
    "initialCode": "def both_none_identity_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_8(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_8(None, None))  # Expected: True\nprint(both_none_identity_8(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7445(left, right):\n    return both_none_identity_8(left, right)\n\n# Example 3: static method approach\nclass Problem7445Solution:\n    @staticmethod\n    def both_none_identity_8(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_8(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_8(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7446,
    "title": "Problem 7446",
    "description": "Write a Python function called `both_none_identity_9` that must use identity to test whether both values are None, variant 9. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_9(None, None) -> True\n  both_none_identity_9(None, 0) -> False",
    "initialCode": "def both_none_identity_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_9(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_9(None, None))  # Expected: True\nprint(both_none_identity_9(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7446(left, right):\n    return both_none_identity_9(left, right)\n\n# Example 3: static method approach\nclass Problem7446Solution:\n    @staticmethod\n    def both_none_identity_9(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_9(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_9(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7447,
    "title": "Problem 7447",
    "description": "Write a Python function called `both_none_identity_10` that must use identity to test whether both values are None, variant 10. Practice equality & identity.\nDifficulty: Intermediate.\nExamples:\n  both_none_identity_10(None, None) -> True\n  both_none_identity_10(None, 0) -> False",
    "initialCode": "def both_none_identity_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef both_none_identity_10(left, right):\n    return left is None and right is None\n\nprint(both_none_identity_10(None, None))  # Expected: True\nprint(both_none_identity_10(None, 0))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7447(left, right):\n    return both_none_identity_10(left, right)\n\n# Example 3: static method approach\nclass Problem7447Solution:\n    @staticmethod\n    def both_none_identity_10(left, right):\n        return left is None and right is None\n\n# Example 4: assigned result approach\nresult = both_none_identity_10(None, None)\nprint(result)\n\n# Example 5: boundary case\nprint(both_none_identity_10(False, False))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Intermediate"
  },
  {
    "id": 7448,
    "title": "Problem 7448",
    "description": "Write a Python function called `unordered_values_equal_1` that must test whether two integer lists contain equal values with equal duplicate counts, variant 1. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_1([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_1([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_1(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_1([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_1([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7448(left, right):\n    return unordered_values_equal_1(left, right)\n\n# Example 3: static method approach\nclass Problem7448Solution:\n    @staticmethod\n    def unordered_values_equal_1(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_1([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_1([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7449,
    "title": "Problem 7449",
    "description": "Write a Python function called `unordered_values_equal_2` that must test whether two integer lists contain equal values with equal duplicate counts, variant 2. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_2([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_2([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_2(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_2([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_2([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7449(left, right):\n    return unordered_values_equal_2(left, right)\n\n# Example 3: static method approach\nclass Problem7449Solution:\n    @staticmethod\n    def unordered_values_equal_2(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_2([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_2([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7450,
    "title": "Problem 7450",
    "description": "Write a Python function called `unordered_values_equal_3` that must test whether two integer lists contain equal values with equal duplicate counts, variant 3. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_3([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_3([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_3(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_3([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_3([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7450(left, right):\n    return unordered_values_equal_3(left, right)\n\n# Example 3: static method approach\nclass Problem7450Solution:\n    @staticmethod\n    def unordered_values_equal_3(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_3([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_3([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7451,
    "title": "Problem 7451",
    "description": "Write a Python function called `unordered_values_equal_4` that must test whether two integer lists contain equal values with equal duplicate counts, variant 4. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_4([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_4([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_4(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_4([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_4([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7451(left, right):\n    return unordered_values_equal_4(left, right)\n\n# Example 3: static method approach\nclass Problem7451Solution:\n    @staticmethod\n    def unordered_values_equal_4(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_4([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_4([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7452,
    "title": "Problem 7452",
    "description": "Write a Python function called `unordered_values_equal_5` that must test whether two integer lists contain equal values with equal duplicate counts, variant 5. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_5([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_5([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_5(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_5([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_5([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7452(left, right):\n    return unordered_values_equal_5(left, right)\n\n# Example 3: static method approach\nclass Problem7452Solution:\n    @staticmethod\n    def unordered_values_equal_5(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_5([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_5([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7453,
    "title": "Problem 7453",
    "description": "Write a Python function called `unordered_values_equal_6` that must test whether two integer lists contain equal values with equal duplicate counts, variant 6. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_6([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_6([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_6(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_6([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_6([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7453(left, right):\n    return unordered_values_equal_6(left, right)\n\n# Example 3: static method approach\nclass Problem7453Solution:\n    @staticmethod\n    def unordered_values_equal_6(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_6([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_6([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7454,
    "title": "Problem 7454",
    "description": "Write a Python function called `unordered_values_equal_7` that must test whether two integer lists contain equal values with equal duplicate counts, variant 7. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_7([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_7([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_7(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_7([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_7([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7454(left, right):\n    return unordered_values_equal_7(left, right)\n\n# Example 3: static method approach\nclass Problem7454Solution:\n    @staticmethod\n    def unordered_values_equal_7(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_7([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_7([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7455,
    "title": "Problem 7455",
    "description": "Write a Python function called `unordered_values_equal_8` that must test whether two integer lists contain equal values with equal duplicate counts, variant 8. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_8([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_8([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_8(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_8([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_8([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7455(left, right):\n    return unordered_values_equal_8(left, right)\n\n# Example 3: static method approach\nclass Problem7455Solution:\n    @staticmethod\n    def unordered_values_equal_8(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_8([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_8([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7456,
    "title": "Problem 7456",
    "description": "Write a Python function called `unordered_values_equal_9` that must test whether two integer lists contain equal values with equal duplicate counts, variant 9. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_9([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_9([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_9(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_9([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_9([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7456(left, right):\n    return unordered_values_equal_9(left, right)\n\n# Example 3: static method approach\nclass Problem7456Solution:\n    @staticmethod\n    def unordered_values_equal_9(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_9([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_9([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7457,
    "title": "Problem 7457",
    "description": "Write a Python function called `unordered_values_equal_10` that must test whether two integer lists contain equal values with equal duplicate counts, variant 10. Practice equality & identity.\nDifficulty: Expert.\nExamples:\n  unordered_values_equal_10([1, 2, 1], [2, 1, 1]) -> True\n  unordered_values_equal_10([1, 2], [1, 1]) -> False",
    "initialCode": "def unordered_values_equal_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef unordered_values_equal_10(left, right):\n    return sorted(left) == sorted(right)\n\nprint(unordered_values_equal_10([1, 2, 1], [2, 1, 1]))  # Expected: True\nprint(unordered_values_equal_10([1, 2], [1, 1]))  # Expected: False\n\n# Example 2: named wrapper approach\ndef solve_problem_7457(left, right):\n    return unordered_values_equal_10(left, right)\n\n# Example 3: static method approach\nclass Problem7457Solution:\n    @staticmethod\n    def unordered_values_equal_10(left, right):\n        return sorted(left) == sorted(right)\n\n# Example 4: assigned result approach\nresult = unordered_values_equal_10([1, 2, 1], [2, 1, 1])\nprint(result)\n\n# Example 5: boundary case\nprint(unordered_values_equal_10([], []))",
    "hint": "Focus on value equality versus object identity, normalization, type sensitivity, order, and duplicate counts. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required equality & identity rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Equality & Identity Difficult"
  },
  {
    "id": 7458,
    "title": "Problem 7458",
    "description": "Write a Python function called `enumerated_pairs_1` that must return index-value lists starting at 1. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_1([\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"]]\n  enumerated_pairs_1([]) -> []",
    "initialCode": "def enumerated_pairs_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_1(values):\n    return [[index, value] for index, value in enumerate(values, start=1)]\n\nprint(enumerated_pairs_1([\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"]]\nprint(enumerated_pairs_1([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7458(values):\n    return enumerated_pairs_1(values)\n\n# Example 3: static method approach\nclass Problem7458Solution:\n    @staticmethod\n    def enumerated_pairs_1(values):\n        return [[index, value] for index, value in enumerate(values, start=1)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_1([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_1([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7459,
    "title": "Problem 7459",
    "description": "Write a Python function called `enumerated_pairs_2` that must return index-value lists starting at 2. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_2([\"a\", \"b\"]) -> [[2, \"a\"], [3, \"b\"]]\n  enumerated_pairs_2([]) -> []",
    "initialCode": "def enumerated_pairs_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_2(values):\n    return [[index, value] for index, value in enumerate(values, start=2)]\n\nprint(enumerated_pairs_2([\"a\", \"b\"]))  # Expected: [[2, \"a\"], [3, \"b\"]]\nprint(enumerated_pairs_2([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7459(values):\n    return enumerated_pairs_2(values)\n\n# Example 3: static method approach\nclass Problem7459Solution:\n    @staticmethod\n    def enumerated_pairs_2(values):\n        return [[index, value] for index, value in enumerate(values, start=2)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_2([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_2([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7460,
    "title": "Problem 7460",
    "description": "Write a Python function called `enumerated_pairs_3` that must return index-value lists starting at 3. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_3([\"a\", \"b\"]) -> [[3, \"a\"], [4, \"b\"]]\n  enumerated_pairs_3([]) -> []",
    "initialCode": "def enumerated_pairs_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_3(values):\n    return [[index, value] for index, value in enumerate(values, start=3)]\n\nprint(enumerated_pairs_3([\"a\", \"b\"]))  # Expected: [[3, \"a\"], [4, \"b\"]]\nprint(enumerated_pairs_3([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7460(values):\n    return enumerated_pairs_3(values)\n\n# Example 3: static method approach\nclass Problem7460Solution:\n    @staticmethod\n    def enumerated_pairs_3(values):\n        return [[index, value] for index, value in enumerate(values, start=3)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_3([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_3([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7461,
    "title": "Problem 7461",
    "description": "Write a Python function called `enumerated_pairs_4` that must return index-value lists starting at 4. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_4([\"a\", \"b\"]) -> [[4, \"a\"], [5, \"b\"]]\n  enumerated_pairs_4([]) -> []",
    "initialCode": "def enumerated_pairs_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_4(values):\n    return [[index, value] for index, value in enumerate(values, start=4)]\n\nprint(enumerated_pairs_4([\"a\", \"b\"]))  # Expected: [[4, \"a\"], [5, \"b\"]]\nprint(enumerated_pairs_4([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7461(values):\n    return enumerated_pairs_4(values)\n\n# Example 3: static method approach\nclass Problem7461Solution:\n    @staticmethod\n    def enumerated_pairs_4(values):\n        return [[index, value] for index, value in enumerate(values, start=4)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_4([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_4([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7462,
    "title": "Problem 7462",
    "description": "Write a Python function called `enumerated_pairs_5` that must return index-value lists starting at 5. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_5([\"a\", \"b\"]) -> [[5, \"a\"], [6, \"b\"]]\n  enumerated_pairs_5([]) -> []",
    "initialCode": "def enumerated_pairs_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_5(values):\n    return [[index, value] for index, value in enumerate(values, start=5)]\n\nprint(enumerated_pairs_5([\"a\", \"b\"]))  # Expected: [[5, \"a\"], [6, \"b\"]]\nprint(enumerated_pairs_5([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7462(values):\n    return enumerated_pairs_5(values)\n\n# Example 3: static method approach\nclass Problem7462Solution:\n    @staticmethod\n    def enumerated_pairs_5(values):\n        return [[index, value] for index, value in enumerate(values, start=5)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_5([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_5([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7463,
    "title": "Problem 7463",
    "description": "Write a Python function called `enumerated_pairs_6` that must return index-value lists starting at 6. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_6([\"a\", \"b\"]) -> [[6, \"a\"], [7, \"b\"]]\n  enumerated_pairs_6([]) -> []",
    "initialCode": "def enumerated_pairs_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_6(values):\n    return [[index, value] for index, value in enumerate(values, start=6)]\n\nprint(enumerated_pairs_6([\"a\", \"b\"]))  # Expected: [[6, \"a\"], [7, \"b\"]]\nprint(enumerated_pairs_6([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7463(values):\n    return enumerated_pairs_6(values)\n\n# Example 3: static method approach\nclass Problem7463Solution:\n    @staticmethod\n    def enumerated_pairs_6(values):\n        return [[index, value] for index, value in enumerate(values, start=6)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_6([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_6([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7464,
    "title": "Problem 7464",
    "description": "Write a Python function called `enumerated_pairs_7` that must return index-value lists starting at 7. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_7([\"a\", \"b\"]) -> [[7, \"a\"], [8, \"b\"]]\n  enumerated_pairs_7([]) -> []",
    "initialCode": "def enumerated_pairs_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_7(values):\n    return [[index, value] for index, value in enumerate(values, start=7)]\n\nprint(enumerated_pairs_7([\"a\", \"b\"]))  # Expected: [[7, \"a\"], [8, \"b\"]]\nprint(enumerated_pairs_7([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7464(values):\n    return enumerated_pairs_7(values)\n\n# Example 3: static method approach\nclass Problem7464Solution:\n    @staticmethod\n    def enumerated_pairs_7(values):\n        return [[index, value] for index, value in enumerate(values, start=7)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_7([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_7([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7465,
    "title": "Problem 7465",
    "description": "Write a Python function called `enumerated_pairs_8` that must return index-value lists starting at 8. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_8([\"a\", \"b\"]) -> [[8, \"a\"], [9, \"b\"]]\n  enumerated_pairs_8([]) -> []",
    "initialCode": "def enumerated_pairs_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_8(values):\n    return [[index, value] for index, value in enumerate(values, start=8)]\n\nprint(enumerated_pairs_8([\"a\", \"b\"]))  # Expected: [[8, \"a\"], [9, \"b\"]]\nprint(enumerated_pairs_8([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7465(values):\n    return enumerated_pairs_8(values)\n\n# Example 3: static method approach\nclass Problem7465Solution:\n    @staticmethod\n    def enumerated_pairs_8(values):\n        return [[index, value] for index, value in enumerate(values, start=8)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_8([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_8([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7466,
    "title": "Problem 7466",
    "description": "Write a Python function called `enumerated_pairs_9` that must return index-value lists starting at 9. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_9([\"a\", \"b\"]) -> [[9, \"a\"], [10, \"b\"]]\n  enumerated_pairs_9([]) -> []",
    "initialCode": "def enumerated_pairs_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_9(values):\n    return [[index, value] for index, value in enumerate(values, start=9)]\n\nprint(enumerated_pairs_9([\"a\", \"b\"]))  # Expected: [[9, \"a\"], [10, \"b\"]]\nprint(enumerated_pairs_9([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7466(values):\n    return enumerated_pairs_9(values)\n\n# Example 3: static method approach\nclass Problem7466Solution:\n    @staticmethod\n    def enumerated_pairs_9(values):\n        return [[index, value] for index, value in enumerate(values, start=9)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_9([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_9([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7467,
    "title": "Problem 7467",
    "description": "Write a Python function called `enumerated_pairs_10` that must return index-value lists starting at 10. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_pairs_10([\"a\", \"b\"]) -> [[10, \"a\"], [11, \"b\"]]\n  enumerated_pairs_10([]) -> []",
    "initialCode": "def enumerated_pairs_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_pairs_10(values):\n    return [[index, value] for index, value in enumerate(values, start=10)]\n\nprint(enumerated_pairs_10([\"a\", \"b\"]))  # Expected: [[10, \"a\"], [11, \"b\"]]\nprint(enumerated_pairs_10([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7467(values):\n    return enumerated_pairs_10(values)\n\n# Example 3: static method approach\nclass Problem7467Solution:\n    @staticmethod\n    def enumerated_pairs_10(values):\n        return [[index, value] for index, value in enumerate(values, start=10)]\n\n# Example 4: assigned result approach\nresult = enumerated_pairs_10([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_pairs_10([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7468,
    "title": "Problem 7468",
    "description": "Write a Python function called `enumerated_labels_1` that must return labels combining indexes from 1 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_1([\"a\", \"b\"]) -> [\"1:a\", \"2:b\"]\n  enumerated_labels_1([]) -> []",
    "initialCode": "def enumerated_labels_1(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_1(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=1)]\n\nprint(enumerated_labels_1([\"a\", \"b\"]))  # Expected: [\"1:a\", \"2:b\"]\nprint(enumerated_labels_1([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7468(values):\n    return enumerated_labels_1(values)\n\n# Example 3: static method approach\nclass Problem7468Solution:\n    @staticmethod\n    def enumerated_labels_1(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=1)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_1([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_1([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7469,
    "title": "Problem 7469",
    "description": "Write a Python function called `enumerated_labels_2` that must return labels combining indexes from 2 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_2([\"a\", \"b\"]) -> [\"2:a\", \"3:b\"]\n  enumerated_labels_2([]) -> []",
    "initialCode": "def enumerated_labels_2(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_2(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=2)]\n\nprint(enumerated_labels_2([\"a\", \"b\"]))  # Expected: [\"2:a\", \"3:b\"]\nprint(enumerated_labels_2([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7469(values):\n    return enumerated_labels_2(values)\n\n# Example 3: static method approach\nclass Problem7469Solution:\n    @staticmethod\n    def enumerated_labels_2(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=2)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_2([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_2([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7470,
    "title": "Problem 7470",
    "description": "Write a Python function called `enumerated_labels_3` that must return labels combining indexes from 3 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_3([\"a\", \"b\"]) -> [\"3:a\", \"4:b\"]\n  enumerated_labels_3([]) -> []",
    "initialCode": "def enumerated_labels_3(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_3(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=3)]\n\nprint(enumerated_labels_3([\"a\", \"b\"]))  # Expected: [\"3:a\", \"4:b\"]\nprint(enumerated_labels_3([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7470(values):\n    return enumerated_labels_3(values)\n\n# Example 3: static method approach\nclass Problem7470Solution:\n    @staticmethod\n    def enumerated_labels_3(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=3)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_3([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_3([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7471,
    "title": "Problem 7471",
    "description": "Write a Python function called `enumerated_labels_4` that must return labels combining indexes from 4 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_4([\"a\", \"b\"]) -> [\"4:a\", \"5:b\"]\n  enumerated_labels_4([]) -> []",
    "initialCode": "def enumerated_labels_4(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_4(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=4)]\n\nprint(enumerated_labels_4([\"a\", \"b\"]))  # Expected: [\"4:a\", \"5:b\"]\nprint(enumerated_labels_4([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7471(values):\n    return enumerated_labels_4(values)\n\n# Example 3: static method approach\nclass Problem7471Solution:\n    @staticmethod\n    def enumerated_labels_4(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=4)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_4([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_4([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7472,
    "title": "Problem 7472",
    "description": "Write a Python function called `enumerated_labels_5` that must return labels combining indexes from 5 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_5([\"a\", \"b\"]) -> [\"5:a\", \"6:b\"]\n  enumerated_labels_5([]) -> []",
    "initialCode": "def enumerated_labels_5(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_5(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=5)]\n\nprint(enumerated_labels_5([\"a\", \"b\"]))  # Expected: [\"5:a\", \"6:b\"]\nprint(enumerated_labels_5([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7472(values):\n    return enumerated_labels_5(values)\n\n# Example 3: static method approach\nclass Problem7472Solution:\n    @staticmethod\n    def enumerated_labels_5(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=5)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_5([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_5([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7473,
    "title": "Problem 7473",
    "description": "Write a Python function called `enumerated_labels_6` that must return labels combining indexes from 6 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_6([\"a\", \"b\"]) -> [\"6:a\", \"7:b\"]\n  enumerated_labels_6([]) -> []",
    "initialCode": "def enumerated_labels_6(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_6(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=6)]\n\nprint(enumerated_labels_6([\"a\", \"b\"]))  # Expected: [\"6:a\", \"7:b\"]\nprint(enumerated_labels_6([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7473(values):\n    return enumerated_labels_6(values)\n\n# Example 3: static method approach\nclass Problem7473Solution:\n    @staticmethod\n    def enumerated_labels_6(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=6)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_6([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_6([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7474,
    "title": "Problem 7474",
    "description": "Write a Python function called `enumerated_labels_7` that must return labels combining indexes from 7 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_7([\"a\", \"b\"]) -> [\"7:a\", \"8:b\"]\n  enumerated_labels_7([]) -> []",
    "initialCode": "def enumerated_labels_7(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_7(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=7)]\n\nprint(enumerated_labels_7([\"a\", \"b\"]))  # Expected: [\"7:a\", \"8:b\"]\nprint(enumerated_labels_7([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7474(values):\n    return enumerated_labels_7(values)\n\n# Example 3: static method approach\nclass Problem7474Solution:\n    @staticmethod\n    def enumerated_labels_7(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=7)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_7([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_7([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7475,
    "title": "Problem 7475",
    "description": "Write a Python function called `enumerated_labels_8` that must return labels combining indexes from 8 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_8([\"a\", \"b\"]) -> [\"8:a\", \"9:b\"]\n  enumerated_labels_8([]) -> []",
    "initialCode": "def enumerated_labels_8(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_8(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=8)]\n\nprint(enumerated_labels_8([\"a\", \"b\"]))  # Expected: [\"8:a\", \"9:b\"]\nprint(enumerated_labels_8([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7475(values):\n    return enumerated_labels_8(values)\n\n# Example 3: static method approach\nclass Problem7475Solution:\n    @staticmethod\n    def enumerated_labels_8(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=8)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_8([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_8([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7476,
    "title": "Problem 7476",
    "description": "Write a Python function called `enumerated_labels_9` that must return labels combining indexes from 9 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_9([\"a\", \"b\"]) -> [\"9:a\", \"10:b\"]\n  enumerated_labels_9([]) -> []",
    "initialCode": "def enumerated_labels_9(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_9(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=9)]\n\nprint(enumerated_labels_9([\"a\", \"b\"]))  # Expected: [\"9:a\", \"10:b\"]\nprint(enumerated_labels_9([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7476(values):\n    return enumerated_labels_9(values)\n\n# Example 3: static method approach\nclass Problem7476Solution:\n    @staticmethod\n    def enumerated_labels_9(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=9)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_9([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_9([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7477,
    "title": "Problem 7477",
    "description": "Write a Python function called `enumerated_labels_10` that must return labels combining indexes from 10 with values. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  enumerated_labels_10([\"a\", \"b\"]) -> [\"10:a\", \"11:b\"]\n  enumerated_labels_10([]) -> []",
    "initialCode": "def enumerated_labels_10(values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerated_labels_10(values):\n    return [f\"{index}:{value}\" for index, value in enumerate(values, start=10)]\n\nprint(enumerated_labels_10([\"a\", \"b\"]))  # Expected: [\"10:a\", \"11:b\"]\nprint(enumerated_labels_10([]))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7477(values):\n    return enumerated_labels_10(values)\n\n# Example 3: static method approach\nclass Problem7477Solution:\n    @staticmethod\n    def enumerated_labels_10(values):\n        return [f\"{index}:{value}\" for index, value in enumerate(values, start=10)]\n\n# Example 4: assigned result approach\nresult = enumerated_labels_10([\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerated_labels_10([9]))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7478,
    "title": "Problem 7478",
    "description": "Write a Python function called `positions_matching_1` that must return matching indexes offset by 1. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_1([1, 2, 1], 1) -> [1, 3]\n  positions_matching_1([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_1(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_1(values, target):\n    return [index + 1 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_1([1, 2, 1], 1))  # Expected: [1, 3]\nprint(positions_matching_1([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7478(values, target):\n    return positions_matching_1(values, target)\n\n# Example 3: static method approach\nclass Problem7478Solution:\n    @staticmethod\n    def positions_matching_1(values, target):\n        return [index + 1 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_1([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_1([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7479,
    "title": "Problem 7479",
    "description": "Write a Python function called `positions_matching_2` that must return matching indexes offset by 2. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_2([1, 2, 1], 1) -> [2, 4]\n  positions_matching_2([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_2(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_2(values, target):\n    return [index + 2 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_2([1, 2, 1], 1))  # Expected: [2, 4]\nprint(positions_matching_2([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7479(values, target):\n    return positions_matching_2(values, target)\n\n# Example 3: static method approach\nclass Problem7479Solution:\n    @staticmethod\n    def positions_matching_2(values, target):\n        return [index + 2 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_2([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_2([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7480,
    "title": "Problem 7480",
    "description": "Write a Python function called `positions_matching_3` that must return matching indexes offset by 3. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_3([1, 2, 1], 1) -> [3, 5]\n  positions_matching_3([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_3(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_3(values, target):\n    return [index + 3 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_3([1, 2, 1], 1))  # Expected: [3, 5]\nprint(positions_matching_3([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7480(values, target):\n    return positions_matching_3(values, target)\n\n# Example 3: static method approach\nclass Problem7480Solution:\n    @staticmethod\n    def positions_matching_3(values, target):\n        return [index + 3 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_3([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_3([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7481,
    "title": "Problem 7481",
    "description": "Write a Python function called `positions_matching_4` that must return matching indexes offset by 4. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_4([1, 2, 1], 1) -> [4, 6]\n  positions_matching_4([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_4(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_4(values, target):\n    return [index + 4 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_4([1, 2, 1], 1))  # Expected: [4, 6]\nprint(positions_matching_4([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7481(values, target):\n    return positions_matching_4(values, target)\n\n# Example 3: static method approach\nclass Problem7481Solution:\n    @staticmethod\n    def positions_matching_4(values, target):\n        return [index + 4 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_4([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_4([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7482,
    "title": "Problem 7482",
    "description": "Write a Python function called `positions_matching_5` that must return matching indexes offset by 5. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_5([1, 2, 1], 1) -> [5, 7]\n  positions_matching_5([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_5(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_5(values, target):\n    return [index + 5 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_5([1, 2, 1], 1))  # Expected: [5, 7]\nprint(positions_matching_5([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7482(values, target):\n    return positions_matching_5(values, target)\n\n# Example 3: static method approach\nclass Problem7482Solution:\n    @staticmethod\n    def positions_matching_5(values, target):\n        return [index + 5 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_5([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_5([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7483,
    "title": "Problem 7483",
    "description": "Write a Python function called `positions_matching_6` that must return matching indexes offset by 6. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_6([1, 2, 1], 1) -> [6, 8]\n  positions_matching_6([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_6(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_6(values, target):\n    return [index + 6 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_6([1, 2, 1], 1))  # Expected: [6, 8]\nprint(positions_matching_6([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7483(values, target):\n    return positions_matching_6(values, target)\n\n# Example 3: static method approach\nclass Problem7483Solution:\n    @staticmethod\n    def positions_matching_6(values, target):\n        return [index + 6 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_6([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_6([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7484,
    "title": "Problem 7484",
    "description": "Write a Python function called `positions_matching_7` that must return matching indexes offset by 7. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_7([1, 2, 1], 1) -> [7, 9]\n  positions_matching_7([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_7(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_7(values, target):\n    return [index + 7 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_7([1, 2, 1], 1))  # Expected: [7, 9]\nprint(positions_matching_7([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7484(values, target):\n    return positions_matching_7(values, target)\n\n# Example 3: static method approach\nclass Problem7484Solution:\n    @staticmethod\n    def positions_matching_7(values, target):\n        return [index + 7 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_7([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_7([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7485,
    "title": "Problem 7485",
    "description": "Write a Python function called `positions_matching_8` that must return matching indexes offset by 8. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_8([1, 2, 1], 1) -> [8, 10]\n  positions_matching_8([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_8(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_8(values, target):\n    return [index + 8 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_8([1, 2, 1], 1))  # Expected: [8, 10]\nprint(positions_matching_8([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7485(values, target):\n    return positions_matching_8(values, target)\n\n# Example 3: static method approach\nclass Problem7485Solution:\n    @staticmethod\n    def positions_matching_8(values, target):\n        return [index + 8 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_8([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_8([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7486,
    "title": "Problem 7486",
    "description": "Write a Python function called `positions_matching_9` that must return matching indexes offset by 9. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_9([1, 2, 1], 1) -> [9, 11]\n  positions_matching_9([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_9(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_9(values, target):\n    return [index + 9 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_9([1, 2, 1], 1))  # Expected: [9, 11]\nprint(positions_matching_9([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7486(values, target):\n    return positions_matching_9(values, target)\n\n# Example 3: static method approach\nclass Problem7486Solution:\n    @staticmethod\n    def positions_matching_9(values, target):\n        return [index + 9 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_9([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_9([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7487,
    "title": "Problem 7487",
    "description": "Write a Python function called `positions_matching_10` that must return matching indexes offset by 10. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  positions_matching_10([1, 2, 1], 1) -> [10, 12]\n  positions_matching_10([\"a\"], \"x\") -> []",
    "initialCode": "def positions_matching_10(values, target):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef positions_matching_10(values, target):\n    return [index + 10 for index, value in enumerate(values) if value == target]\n\nprint(positions_matching_10([1, 2, 1], 1))  # Expected: [10, 12]\nprint(positions_matching_10([\"a\"], \"x\"))  # Expected: []\n\n# Example 2: named wrapper approach\ndef solve_problem_7487(values, target):\n    return positions_matching_10(values, target)\n\n# Example 3: static method approach\nclass Problem7487Solution:\n    @staticmethod\n    def positions_matching_10(values, target):\n        return [index + 10 for index, value in enumerate(values) if value == target]\n\n# Example 4: assigned result approach\nresult = positions_matching_10([1, 2, 1], 1)\nprint(result)\n\n# Example 5: boundary case\nprint(positions_matching_10([], 0))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7488,
    "title": "Problem 7488",
    "description": "Write a Python function called `zip_to_pairs_1` that must zip two inputs into lists and append marker pair 1. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_1([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 1]]\n  zip_to_pairs_1([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 1]]",
    "initialCode": "def zip_to_pairs_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_1(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 1]]\n\nprint(zip_to_pairs_1([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 1]]\nprint(zip_to_pairs_1([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7488(left, right):\n    return zip_to_pairs_1(left, right)\n\n# Example 3: static method approach\nclass Problem7488Solution:\n    @staticmethod\n    def zip_to_pairs_1(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 1]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_1([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7489,
    "title": "Problem 7489",
    "description": "Write a Python function called `zip_to_pairs_2` that must zip two inputs into lists and append marker pair 2. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_2([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 2]]\n  zip_to_pairs_2([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 2]]",
    "initialCode": "def zip_to_pairs_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_2(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 2]]\n\nprint(zip_to_pairs_2([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 2]]\nprint(zip_to_pairs_2([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 2]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7489(left, right):\n    return zip_to_pairs_2(left, right)\n\n# Example 3: static method approach\nclass Problem7489Solution:\n    @staticmethod\n    def zip_to_pairs_2(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 2]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_2([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7490,
    "title": "Problem 7490",
    "description": "Write a Python function called `zip_to_pairs_3` that must zip two inputs into lists and append marker pair 3. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_3([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 3]]\n  zip_to_pairs_3([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 3]]",
    "initialCode": "def zip_to_pairs_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_3(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 3]]\n\nprint(zip_to_pairs_3([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 3]]\nprint(zip_to_pairs_3([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 3]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7490(left, right):\n    return zip_to_pairs_3(left, right)\n\n# Example 3: static method approach\nclass Problem7490Solution:\n    @staticmethod\n    def zip_to_pairs_3(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 3]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_3([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7491,
    "title": "Problem 7491",
    "description": "Write a Python function called `zip_to_pairs_4` that must zip two inputs into lists and append marker pair 4. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_4([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 4]]\n  zip_to_pairs_4([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 4]]",
    "initialCode": "def zip_to_pairs_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_4(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 4]]\n\nprint(zip_to_pairs_4([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 4]]\nprint(zip_to_pairs_4([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 4]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7491(left, right):\n    return zip_to_pairs_4(left, right)\n\n# Example 3: static method approach\nclass Problem7491Solution:\n    @staticmethod\n    def zip_to_pairs_4(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 4]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_4([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7492,
    "title": "Problem 7492",
    "description": "Write a Python function called `zip_to_pairs_5` that must zip two inputs into lists and append marker pair 5. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_5([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 5]]\n  zip_to_pairs_5([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 5]]",
    "initialCode": "def zip_to_pairs_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_5(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 5]]\n\nprint(zip_to_pairs_5([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 5]]\nprint(zip_to_pairs_5([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 5]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7492(left, right):\n    return zip_to_pairs_5(left, right)\n\n# Example 3: static method approach\nclass Problem7492Solution:\n    @staticmethod\n    def zip_to_pairs_5(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 5]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_5([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7493,
    "title": "Problem 7493",
    "description": "Write a Python function called `zip_to_pairs_6` that must zip two inputs into lists and append marker pair 6. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_6([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 6]]\n  zip_to_pairs_6([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 6]]",
    "initialCode": "def zip_to_pairs_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_6(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 6]]\n\nprint(zip_to_pairs_6([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 6]]\nprint(zip_to_pairs_6([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 6]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7493(left, right):\n    return zip_to_pairs_6(left, right)\n\n# Example 3: static method approach\nclass Problem7493Solution:\n    @staticmethod\n    def zip_to_pairs_6(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 6]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_6([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7494,
    "title": "Problem 7494",
    "description": "Write a Python function called `zip_to_pairs_7` that must zip two inputs into lists and append marker pair 7. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_7([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 7]]\n  zip_to_pairs_7([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 7]]",
    "initialCode": "def zip_to_pairs_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_7(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 7]]\n\nprint(zip_to_pairs_7([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 7]]\nprint(zip_to_pairs_7([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 7]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7494(left, right):\n    return zip_to_pairs_7(left, right)\n\n# Example 3: static method approach\nclass Problem7494Solution:\n    @staticmethod\n    def zip_to_pairs_7(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 7]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_7([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7495,
    "title": "Problem 7495",
    "description": "Write a Python function called `zip_to_pairs_8` that must zip two inputs into lists and append marker pair 8. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_8([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 8]]\n  zip_to_pairs_8([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 8]]",
    "initialCode": "def zip_to_pairs_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_8(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 8]]\n\nprint(zip_to_pairs_8([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 8]]\nprint(zip_to_pairs_8([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 8]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7495(left, right):\n    return zip_to_pairs_8(left, right)\n\n# Example 3: static method approach\nclass Problem7495Solution:\n    @staticmethod\n    def zip_to_pairs_8(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 8]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_8([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7496,
    "title": "Problem 7496",
    "description": "Write a Python function called `zip_to_pairs_9` that must zip two inputs into lists and append marker pair 9. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_9([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 9]]\n  zip_to_pairs_9([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 9]]",
    "initialCode": "def zip_to_pairs_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_9(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 9]]\n\nprint(zip_to_pairs_9([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 9]]\nprint(zip_to_pairs_9([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 9]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7496(left, right):\n    return zip_to_pairs_9(left, right)\n\n# Example 3: static method approach\nclass Problem7496Solution:\n    @staticmethod\n    def zip_to_pairs_9(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 9]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_9([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7497,
    "title": "Problem 7497",
    "description": "Write a Python function called `zip_to_pairs_10` that must zip two inputs into lists and append marker pair 10. Practice enumerate & zip.\nDifficulty: Easy.\nExamples:\n  zip_to_pairs_10([1, 2], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"], [\"marker\", 10]]\n  zip_to_pairs_10([1], [\"a\", \"b\"]) -> [[1, \"a\"], [\"marker\", 10]]",
    "initialCode": "def zip_to_pairs_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_to_pairs_10(left, right):\n    return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 10]]\n\nprint(zip_to_pairs_10([1, 2], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"], [\"marker\", 10]]\nprint(zip_to_pairs_10([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [\"marker\", 10]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7497(left, right):\n    return zip_to_pairs_10(left, right)\n\n# Example 3: static method approach\nclass Problem7497Solution:\n    @staticmethod\n    def zip_to_pairs_10(left, right):\n        return [[a, b] for a, b in zip(left, right)] + [[\"marker\", 10]]\n\n# Example 4: assigned result approach\nresult = zip_to_pairs_10([1, 2], [\"a\", \"b\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_to_pairs_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Easy"
  },
  {
    "id": 7498,
    "title": "Problem 7498",
    "description": "Write a Python function called `zip_add_values_1` that must add parallel numbers plus 1. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_1([1, 2], [3, 4]) -> [5, 7]\n  zip_add_values_1([1], [2, 3]) -> [4]",
    "initialCode": "def zip_add_values_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_1(left, right):\n    return [a + b + 1 for a, b in zip(left, right)]\n\nprint(zip_add_values_1([1, 2], [3, 4]))  # Expected: [5, 7]\nprint(zip_add_values_1([1], [2, 3]))  # Expected: [4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7498(left, right):\n    return zip_add_values_1(left, right)\n\n# Example 3: static method approach\nclass Problem7498Solution:\n    @staticmethod\n    def zip_add_values_1(left, right):\n        return [a + b + 1 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_1([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7499,
    "title": "Problem 7499",
    "description": "Write a Python function called `zip_add_values_2` that must add parallel numbers plus 2. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_2([1, 2], [3, 4]) -> [6, 8]\n  zip_add_values_2([1], [2, 3]) -> [5]",
    "initialCode": "def zip_add_values_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_2(left, right):\n    return [a + b + 2 for a, b in zip(left, right)]\n\nprint(zip_add_values_2([1, 2], [3, 4]))  # Expected: [6, 8]\nprint(zip_add_values_2([1], [2, 3]))  # Expected: [5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7499(left, right):\n    return zip_add_values_2(left, right)\n\n# Example 3: static method approach\nclass Problem7499Solution:\n    @staticmethod\n    def zip_add_values_2(left, right):\n        return [a + b + 2 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_2([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7500,
    "title": "Problem 7500",
    "description": "Write a Python function called `zip_add_values_3` that must add parallel numbers plus 3. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_3([1, 2], [3, 4]) -> [7, 9]\n  zip_add_values_3([1], [2, 3]) -> [6]",
    "initialCode": "def zip_add_values_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_3(left, right):\n    return [a + b + 3 for a, b in zip(left, right)]\n\nprint(zip_add_values_3([1, 2], [3, 4]))  # Expected: [7, 9]\nprint(zip_add_values_3([1], [2, 3]))  # Expected: [6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7500(left, right):\n    return zip_add_values_3(left, right)\n\n# Example 3: static method approach\nclass Problem7500Solution:\n    @staticmethod\n    def zip_add_values_3(left, right):\n        return [a + b + 3 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_3([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7501,
    "title": "Problem 7501",
    "description": "Write a Python function called `zip_add_values_4` that must add parallel numbers plus 4. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_4([1, 2], [3, 4]) -> [8, 10]\n  zip_add_values_4([1], [2, 3]) -> [7]",
    "initialCode": "def zip_add_values_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_4(left, right):\n    return [a + b + 4 for a, b in zip(left, right)]\n\nprint(zip_add_values_4([1, 2], [3, 4]))  # Expected: [8, 10]\nprint(zip_add_values_4([1], [2, 3]))  # Expected: [7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7501(left, right):\n    return zip_add_values_4(left, right)\n\n# Example 3: static method approach\nclass Problem7501Solution:\n    @staticmethod\n    def zip_add_values_4(left, right):\n        return [a + b + 4 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_4([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7502,
    "title": "Problem 7502",
    "description": "Write a Python function called `zip_add_values_5` that must add parallel numbers plus 5. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_5([1, 2], [3, 4]) -> [9, 11]\n  zip_add_values_5([1], [2, 3]) -> [8]",
    "initialCode": "def zip_add_values_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_5(left, right):\n    return [a + b + 5 for a, b in zip(left, right)]\n\nprint(zip_add_values_5([1, 2], [3, 4]))  # Expected: [9, 11]\nprint(zip_add_values_5([1], [2, 3]))  # Expected: [8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7502(left, right):\n    return zip_add_values_5(left, right)\n\n# Example 3: static method approach\nclass Problem7502Solution:\n    @staticmethod\n    def zip_add_values_5(left, right):\n        return [a + b + 5 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_5([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7503,
    "title": "Problem 7503",
    "description": "Write a Python function called `zip_add_values_6` that must add parallel numbers plus 6. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_6([1, 2], [3, 4]) -> [10, 12]\n  zip_add_values_6([1], [2, 3]) -> [9]",
    "initialCode": "def zip_add_values_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_6(left, right):\n    return [a + b + 6 for a, b in zip(left, right)]\n\nprint(zip_add_values_6([1, 2], [3, 4]))  # Expected: [10, 12]\nprint(zip_add_values_6([1], [2, 3]))  # Expected: [9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7503(left, right):\n    return zip_add_values_6(left, right)\n\n# Example 3: static method approach\nclass Problem7503Solution:\n    @staticmethod\n    def zip_add_values_6(left, right):\n        return [a + b + 6 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_6([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7504,
    "title": "Problem 7504",
    "description": "Write a Python function called `zip_add_values_7` that must add parallel numbers plus 7. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_7([1, 2], [3, 4]) -> [11, 13]\n  zip_add_values_7([1], [2, 3]) -> [10]",
    "initialCode": "def zip_add_values_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_7(left, right):\n    return [a + b + 7 for a, b in zip(left, right)]\n\nprint(zip_add_values_7([1, 2], [3, 4]))  # Expected: [11, 13]\nprint(zip_add_values_7([1], [2, 3]))  # Expected: [10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7504(left, right):\n    return zip_add_values_7(left, right)\n\n# Example 3: static method approach\nclass Problem7504Solution:\n    @staticmethod\n    def zip_add_values_7(left, right):\n        return [a + b + 7 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_7([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7505,
    "title": "Problem 7505",
    "description": "Write a Python function called `zip_add_values_8` that must add parallel numbers plus 8. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_8([1, 2], [3, 4]) -> [12, 14]\n  zip_add_values_8([1], [2, 3]) -> [11]",
    "initialCode": "def zip_add_values_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_8(left, right):\n    return [a + b + 8 for a, b in zip(left, right)]\n\nprint(zip_add_values_8([1, 2], [3, 4]))  # Expected: [12, 14]\nprint(zip_add_values_8([1], [2, 3]))  # Expected: [11]\n\n# Example 2: named wrapper approach\ndef solve_problem_7505(left, right):\n    return zip_add_values_8(left, right)\n\n# Example 3: static method approach\nclass Problem7505Solution:\n    @staticmethod\n    def zip_add_values_8(left, right):\n        return [a + b + 8 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_8([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7506,
    "title": "Problem 7506",
    "description": "Write a Python function called `zip_add_values_9` that must add parallel numbers plus 9. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_9([1, 2], [3, 4]) -> [13, 15]\n  zip_add_values_9([1], [2, 3]) -> [12]",
    "initialCode": "def zip_add_values_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_9(left, right):\n    return [a + b + 9 for a, b in zip(left, right)]\n\nprint(zip_add_values_9([1, 2], [3, 4]))  # Expected: [13, 15]\nprint(zip_add_values_9([1], [2, 3]))  # Expected: [12]\n\n# Example 2: named wrapper approach\ndef solve_problem_7506(left, right):\n    return zip_add_values_9(left, right)\n\n# Example 3: static method approach\nclass Problem7506Solution:\n    @staticmethod\n    def zip_add_values_9(left, right):\n        return [a + b + 9 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_9([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7507,
    "title": "Problem 7507",
    "description": "Write a Python function called `zip_add_values_10` that must add parallel numbers plus 10. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_add_values_10([1, 2], [3, 4]) -> [14, 16]\n  zip_add_values_10([1], [2, 3]) -> [13]",
    "initialCode": "def zip_add_values_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_add_values_10(left, right):\n    return [a + b + 10 for a, b in zip(left, right)]\n\nprint(zip_add_values_10([1, 2], [3, 4]))  # Expected: [14, 16]\nprint(zip_add_values_10([1], [2, 3]))  # Expected: [13]\n\n# Example 2: named wrapper approach\ndef solve_problem_7507(left, right):\n    return zip_add_values_10(left, right)\n\n# Example 3: static method approach\nclass Problem7507Solution:\n    @staticmethod\n    def zip_add_values_10(left, right):\n        return [a + b + 10 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_add_values_10([1, 2], [3, 4])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_add_values_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7508,
    "title": "Problem 7508",
    "description": "Write a Python function called `zip_dictionary_1` that must build a dictionary from parallel inputs and add marker_1. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_1([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_1\": 1}\n  zip_dictionary_1([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_1\": 1}",
    "initialCode": "def zip_dictionary_1(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_1(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_1\"] = 1\n    return result\n\nprint(zip_dictionary_1([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_1\": 1}\nprint(zip_dictionary_1([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_1\": 1}\n\n# Example 2: named wrapper approach\ndef solve_problem_7508(keys, values):\n    return zip_dictionary_1(keys, values)\n\n# Example 3: static method approach\nclass Problem7508Solution:\n    @staticmethod\n    def zip_dictionary_1(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_1\"] = 1\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_1([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7509,
    "title": "Problem 7509",
    "description": "Write a Python function called `zip_dictionary_2` that must build a dictionary from parallel inputs and add marker_2. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_2([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_2\": 2}\n  zip_dictionary_2([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_2\": 2}",
    "initialCode": "def zip_dictionary_2(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_2(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_2\"] = 2\n    return result\n\nprint(zip_dictionary_2([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_2\": 2}\nprint(zip_dictionary_2([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_2\": 2}\n\n# Example 2: named wrapper approach\ndef solve_problem_7509(keys, values):\n    return zip_dictionary_2(keys, values)\n\n# Example 3: static method approach\nclass Problem7509Solution:\n    @staticmethod\n    def zip_dictionary_2(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_2\"] = 2\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_2([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7510,
    "title": "Problem 7510",
    "description": "Write a Python function called `zip_dictionary_3` that must build a dictionary from parallel inputs and add marker_3. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_3([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_3\": 3}\n  zip_dictionary_3([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_3\": 3}",
    "initialCode": "def zip_dictionary_3(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_3(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_3\"] = 3\n    return result\n\nprint(zip_dictionary_3([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_3\": 3}\nprint(zip_dictionary_3([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_3\": 3}\n\n# Example 2: named wrapper approach\ndef solve_problem_7510(keys, values):\n    return zip_dictionary_3(keys, values)\n\n# Example 3: static method approach\nclass Problem7510Solution:\n    @staticmethod\n    def zip_dictionary_3(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_3\"] = 3\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_3([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7511,
    "title": "Problem 7511",
    "description": "Write a Python function called `zip_dictionary_4` that must build a dictionary from parallel inputs and add marker_4. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_4([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_4\": 4}\n  zip_dictionary_4([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_4\": 4}",
    "initialCode": "def zip_dictionary_4(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_4(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_4\"] = 4\n    return result\n\nprint(zip_dictionary_4([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_4\": 4}\nprint(zip_dictionary_4([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_4\": 4}\n\n# Example 2: named wrapper approach\ndef solve_problem_7511(keys, values):\n    return zip_dictionary_4(keys, values)\n\n# Example 3: static method approach\nclass Problem7511Solution:\n    @staticmethod\n    def zip_dictionary_4(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_4\"] = 4\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_4([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7512,
    "title": "Problem 7512",
    "description": "Write a Python function called `zip_dictionary_5` that must build a dictionary from parallel inputs and add marker_5. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_5([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_5\": 5}\n  zip_dictionary_5([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_5\": 5}",
    "initialCode": "def zip_dictionary_5(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_5(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_5\"] = 5\n    return result\n\nprint(zip_dictionary_5([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_5\": 5}\nprint(zip_dictionary_5([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_5\": 5}\n\n# Example 2: named wrapper approach\ndef solve_problem_7512(keys, values):\n    return zip_dictionary_5(keys, values)\n\n# Example 3: static method approach\nclass Problem7512Solution:\n    @staticmethod\n    def zip_dictionary_5(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_5\"] = 5\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_5([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7513,
    "title": "Problem 7513",
    "description": "Write a Python function called `zip_dictionary_6` that must build a dictionary from parallel inputs and add marker_6. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_6([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_6\": 6}\n  zip_dictionary_6([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_6\": 6}",
    "initialCode": "def zip_dictionary_6(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_6(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_6\"] = 6\n    return result\n\nprint(zip_dictionary_6([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_6\": 6}\nprint(zip_dictionary_6([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_6\": 6}\n\n# Example 2: named wrapper approach\ndef solve_problem_7513(keys, values):\n    return zip_dictionary_6(keys, values)\n\n# Example 3: static method approach\nclass Problem7513Solution:\n    @staticmethod\n    def zip_dictionary_6(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_6\"] = 6\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_6([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7514,
    "title": "Problem 7514",
    "description": "Write a Python function called `zip_dictionary_7` that must build a dictionary from parallel inputs and add marker_7. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_7([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_7\": 7}\n  zip_dictionary_7([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_7\": 7}",
    "initialCode": "def zip_dictionary_7(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_7(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_7\"] = 7\n    return result\n\nprint(zip_dictionary_7([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_7\": 7}\nprint(zip_dictionary_7([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_7\": 7}\n\n# Example 2: named wrapper approach\ndef solve_problem_7514(keys, values):\n    return zip_dictionary_7(keys, values)\n\n# Example 3: static method approach\nclass Problem7514Solution:\n    @staticmethod\n    def zip_dictionary_7(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_7\"] = 7\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_7([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7515,
    "title": "Problem 7515",
    "description": "Write a Python function called `zip_dictionary_8` that must build a dictionary from parallel inputs and add marker_8. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_8([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_8\": 8}\n  zip_dictionary_8([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_8\": 8}",
    "initialCode": "def zip_dictionary_8(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_8(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_8\"] = 8\n    return result\n\nprint(zip_dictionary_8([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_8\": 8}\nprint(zip_dictionary_8([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_8\": 8}\n\n# Example 2: named wrapper approach\ndef solve_problem_7515(keys, values):\n    return zip_dictionary_8(keys, values)\n\n# Example 3: static method approach\nclass Problem7515Solution:\n    @staticmethod\n    def zip_dictionary_8(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_8\"] = 8\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_8([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7516,
    "title": "Problem 7516",
    "description": "Write a Python function called `zip_dictionary_9` that must build a dictionary from parallel inputs and add marker_9. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_9([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_9\": 9}\n  zip_dictionary_9([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_9\": 9}",
    "initialCode": "def zip_dictionary_9(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_9(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_9\"] = 9\n    return result\n\nprint(zip_dictionary_9([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_9\": 9}\nprint(zip_dictionary_9([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_9\": 9}\n\n# Example 2: named wrapper approach\ndef solve_problem_7516(keys, values):\n    return zip_dictionary_9(keys, values)\n\n# Example 3: static method approach\nclass Problem7516Solution:\n    @staticmethod\n    def zip_dictionary_9(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_9\"] = 9\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_9([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7517,
    "title": "Problem 7517",
    "description": "Write a Python function called `zip_dictionary_10` that must build a dictionary from parallel inputs and add marker_10. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_dictionary_10([\"a\", \"b\"], [1, 2]) -> {\"a\": 1, \"b\": 2, \"marker_10\": 10}\n  zip_dictionary_10([\"x\"], [5, 6]) -> {\"x\": 5, \"marker_10\": 10}",
    "initialCode": "def zip_dictionary_10(keys, values):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_dictionary_10(keys, values):\n    result = dict(zip(keys, values))\n    result[\"marker_10\"] = 10\n    return result\n\nprint(zip_dictionary_10([\"a\", \"b\"], [1, 2]))  # Expected: {\"a\": 1, \"b\": 2, \"marker_10\": 10}\nprint(zip_dictionary_10([\"x\"], [5, 6]))  # Expected: {\"x\": 5, \"marker_10\": 10}\n\n# Example 2: named wrapper approach\ndef solve_problem_7517(keys, values):\n    return zip_dictionary_10(keys, values)\n\n# Example 3: static method approach\nclass Problem7517Solution:\n    @staticmethod\n    def zip_dictionary_10(keys, values):\n        result = dict(zip(keys, values))\n        result[\"marker_10\"] = 10\n        return result\n\n# Example 4: assigned result approach\nresult = zip_dictionary_10([\"a\", \"b\"], [1, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_dictionary_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7518,
    "title": "Problem 7518",
    "description": "Write a Python function called `enumerate_zip_rows_1` that must return rank-name-score lists beginning at rank 1. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_1([\"A\", \"B\"], [9, 8]) -> [[1, \"A\", 9], [2, \"B\", 8]]\n  enumerate_zip_rows_1([\"X\"], [1, 2]) -> [[1, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_1(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_1(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=1)]\n\nprint(enumerate_zip_rows_1([\"A\", \"B\"], [9, 8]))  # Expected: [[1, \"A\", 9], [2, \"B\", 8]]\nprint(enumerate_zip_rows_1([\"X\"], [1, 2]))  # Expected: [[1, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7518(names, scores):\n    return enumerate_zip_rows_1(names, scores)\n\n# Example 3: static method approach\nclass Problem7518Solution:\n    @staticmethod\n    def enumerate_zip_rows_1(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=1)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_1([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7519,
    "title": "Problem 7519",
    "description": "Write a Python function called `enumerate_zip_rows_2` that must return rank-name-score lists beginning at rank 2. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_2([\"A\", \"B\"], [9, 8]) -> [[2, \"A\", 9], [3, \"B\", 8]]\n  enumerate_zip_rows_2([\"X\"], [1, 2]) -> [[2, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_2(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_2(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=2)]\n\nprint(enumerate_zip_rows_2([\"A\", \"B\"], [9, 8]))  # Expected: [[2, \"A\", 9], [3, \"B\", 8]]\nprint(enumerate_zip_rows_2([\"X\"], [1, 2]))  # Expected: [[2, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7519(names, scores):\n    return enumerate_zip_rows_2(names, scores)\n\n# Example 3: static method approach\nclass Problem7519Solution:\n    @staticmethod\n    def enumerate_zip_rows_2(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=2)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_2([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7520,
    "title": "Problem 7520",
    "description": "Write a Python function called `enumerate_zip_rows_3` that must return rank-name-score lists beginning at rank 3. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_3([\"A\", \"B\"], [9, 8]) -> [[3, \"A\", 9], [4, \"B\", 8]]\n  enumerate_zip_rows_3([\"X\"], [1, 2]) -> [[3, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_3(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_3(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=3)]\n\nprint(enumerate_zip_rows_3([\"A\", \"B\"], [9, 8]))  # Expected: [[3, \"A\", 9], [4, \"B\", 8]]\nprint(enumerate_zip_rows_3([\"X\"], [1, 2]))  # Expected: [[3, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7520(names, scores):\n    return enumerate_zip_rows_3(names, scores)\n\n# Example 3: static method approach\nclass Problem7520Solution:\n    @staticmethod\n    def enumerate_zip_rows_3(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=3)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_3([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7521,
    "title": "Problem 7521",
    "description": "Write a Python function called `enumerate_zip_rows_4` that must return rank-name-score lists beginning at rank 4. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_4([\"A\", \"B\"], [9, 8]) -> [[4, \"A\", 9], [5, \"B\", 8]]\n  enumerate_zip_rows_4([\"X\"], [1, 2]) -> [[4, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_4(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_4(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=4)]\n\nprint(enumerate_zip_rows_4([\"A\", \"B\"], [9, 8]))  # Expected: [[4, \"A\", 9], [5, \"B\", 8]]\nprint(enumerate_zip_rows_4([\"X\"], [1, 2]))  # Expected: [[4, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7521(names, scores):\n    return enumerate_zip_rows_4(names, scores)\n\n# Example 3: static method approach\nclass Problem7521Solution:\n    @staticmethod\n    def enumerate_zip_rows_4(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=4)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_4([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7522,
    "title": "Problem 7522",
    "description": "Write a Python function called `enumerate_zip_rows_5` that must return rank-name-score lists beginning at rank 5. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_5([\"A\", \"B\"], [9, 8]) -> [[5, \"A\", 9], [6, \"B\", 8]]\n  enumerate_zip_rows_5([\"X\"], [1, 2]) -> [[5, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_5(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_5(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=5)]\n\nprint(enumerate_zip_rows_5([\"A\", \"B\"], [9, 8]))  # Expected: [[5, \"A\", 9], [6, \"B\", 8]]\nprint(enumerate_zip_rows_5([\"X\"], [1, 2]))  # Expected: [[5, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7522(names, scores):\n    return enumerate_zip_rows_5(names, scores)\n\n# Example 3: static method approach\nclass Problem7522Solution:\n    @staticmethod\n    def enumerate_zip_rows_5(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=5)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_5([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7523,
    "title": "Problem 7523",
    "description": "Write a Python function called `enumerate_zip_rows_6` that must return rank-name-score lists beginning at rank 6. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_6([\"A\", \"B\"], [9, 8]) -> [[6, \"A\", 9], [7, \"B\", 8]]\n  enumerate_zip_rows_6([\"X\"], [1, 2]) -> [[6, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_6(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_6(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=6)]\n\nprint(enumerate_zip_rows_6([\"A\", \"B\"], [9, 8]))  # Expected: [[6, \"A\", 9], [7, \"B\", 8]]\nprint(enumerate_zip_rows_6([\"X\"], [1, 2]))  # Expected: [[6, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7523(names, scores):\n    return enumerate_zip_rows_6(names, scores)\n\n# Example 3: static method approach\nclass Problem7523Solution:\n    @staticmethod\n    def enumerate_zip_rows_6(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=6)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_6([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7524,
    "title": "Problem 7524",
    "description": "Write a Python function called `enumerate_zip_rows_7` that must return rank-name-score lists beginning at rank 7. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_7([\"A\", \"B\"], [9, 8]) -> [[7, \"A\", 9], [8, \"B\", 8]]\n  enumerate_zip_rows_7([\"X\"], [1, 2]) -> [[7, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_7(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_7(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=7)]\n\nprint(enumerate_zip_rows_7([\"A\", \"B\"], [9, 8]))  # Expected: [[7, \"A\", 9], [8, \"B\", 8]]\nprint(enumerate_zip_rows_7([\"X\"], [1, 2]))  # Expected: [[7, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7524(names, scores):\n    return enumerate_zip_rows_7(names, scores)\n\n# Example 3: static method approach\nclass Problem7524Solution:\n    @staticmethod\n    def enumerate_zip_rows_7(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=7)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_7([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7525,
    "title": "Problem 7525",
    "description": "Write a Python function called `enumerate_zip_rows_8` that must return rank-name-score lists beginning at rank 8. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_8([\"A\", \"B\"], [9, 8]) -> [[8, \"A\", 9], [9, \"B\", 8]]\n  enumerate_zip_rows_8([\"X\"], [1, 2]) -> [[8, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_8(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_8(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=8)]\n\nprint(enumerate_zip_rows_8([\"A\", \"B\"], [9, 8]))  # Expected: [[8, \"A\", 9], [9, \"B\", 8]]\nprint(enumerate_zip_rows_8([\"X\"], [1, 2]))  # Expected: [[8, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7525(names, scores):\n    return enumerate_zip_rows_8(names, scores)\n\n# Example 3: static method approach\nclass Problem7525Solution:\n    @staticmethod\n    def enumerate_zip_rows_8(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=8)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_8([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7526,
    "title": "Problem 7526",
    "description": "Write a Python function called `enumerate_zip_rows_9` that must return rank-name-score lists beginning at rank 9. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_9([\"A\", \"B\"], [9, 8]) -> [[9, \"A\", 9], [10, \"B\", 8]]\n  enumerate_zip_rows_9([\"X\"], [1, 2]) -> [[9, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_9(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_9(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=9)]\n\nprint(enumerate_zip_rows_9([\"A\", \"B\"], [9, 8]))  # Expected: [[9, \"A\", 9], [10, \"B\", 8]]\nprint(enumerate_zip_rows_9([\"X\"], [1, 2]))  # Expected: [[9, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7526(names, scores):\n    return enumerate_zip_rows_9(names, scores)\n\n# Example 3: static method approach\nclass Problem7526Solution:\n    @staticmethod\n    def enumerate_zip_rows_9(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=9)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_9([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7527,
    "title": "Problem 7527",
    "description": "Write a Python function called `enumerate_zip_rows_10` that must return rank-name-score lists beginning at rank 10. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  enumerate_zip_rows_10([\"A\", \"B\"], [9, 8]) -> [[10, \"A\", 9], [11, \"B\", 8]]\n  enumerate_zip_rows_10([\"X\"], [1, 2]) -> [[10, \"X\", 1]]",
    "initialCode": "def enumerate_zip_rows_10(names, scores):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef enumerate_zip_rows_10(names, scores):\n    return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=10)]\n\nprint(enumerate_zip_rows_10([\"A\", \"B\"], [9, 8]))  # Expected: [[10, \"A\", 9], [11, \"B\", 8]]\nprint(enumerate_zip_rows_10([\"X\"], [1, 2]))  # Expected: [[10, \"X\", 1]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7527(names, scores):\n    return enumerate_zip_rows_10(names, scores)\n\n# Example 3: static method approach\nclass Problem7527Solution:\n    @staticmethod\n    def enumerate_zip_rows_10(names, scores):\n        return [[rank, name, score] for rank, (name, score) in enumerate(zip(names, scores), start=10)]\n\n# Example 4: assigned result approach\nresult = enumerate_zip_rows_10([\"A\", \"B\"], [9, 8])\nprint(result)\n\n# Example 5: boundary case\nprint(enumerate_zip_rows_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7528,
    "title": "Problem 7528",
    "description": "Write a Python function called `zip_differences_1` that must return absolute parallel differences plus 1. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_1([1, 5], [4, 2]) -> [4, 4]\n  zip_differences_1([0], [0, 1]) -> [1]",
    "initialCode": "def zip_differences_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_1(left, right):\n    return [abs(a - b) + 1 for a, b in zip(left, right)]\n\nprint(zip_differences_1([1, 5], [4, 2]))  # Expected: [4, 4]\nprint(zip_differences_1([0], [0, 1]))  # Expected: [1]\n\n# Example 2: named wrapper approach\ndef solve_problem_7528(left, right):\n    return zip_differences_1(left, right)\n\n# Example 3: static method approach\nclass Problem7528Solution:\n    @staticmethod\n    def zip_differences_1(left, right):\n        return [abs(a - b) + 1 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_1([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7529,
    "title": "Problem 7529",
    "description": "Write a Python function called `zip_differences_2` that must return absolute parallel differences plus 2. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_2([1, 5], [4, 2]) -> [5, 5]\n  zip_differences_2([0], [0, 1]) -> [2]",
    "initialCode": "def zip_differences_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_2(left, right):\n    return [abs(a - b) + 2 for a, b in zip(left, right)]\n\nprint(zip_differences_2([1, 5], [4, 2]))  # Expected: [5, 5]\nprint(zip_differences_2([0], [0, 1]))  # Expected: [2]\n\n# Example 2: named wrapper approach\ndef solve_problem_7529(left, right):\n    return zip_differences_2(left, right)\n\n# Example 3: static method approach\nclass Problem7529Solution:\n    @staticmethod\n    def zip_differences_2(left, right):\n        return [abs(a - b) + 2 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_2([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7530,
    "title": "Problem 7530",
    "description": "Write a Python function called `zip_differences_3` that must return absolute parallel differences plus 3. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_3([1, 5], [4, 2]) -> [6, 6]\n  zip_differences_3([0], [0, 1]) -> [3]",
    "initialCode": "def zip_differences_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_3(left, right):\n    return [abs(a - b) + 3 for a, b in zip(left, right)]\n\nprint(zip_differences_3([1, 5], [4, 2]))  # Expected: [6, 6]\nprint(zip_differences_3([0], [0, 1]))  # Expected: [3]\n\n# Example 2: named wrapper approach\ndef solve_problem_7530(left, right):\n    return zip_differences_3(left, right)\n\n# Example 3: static method approach\nclass Problem7530Solution:\n    @staticmethod\n    def zip_differences_3(left, right):\n        return [abs(a - b) + 3 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_3([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7531,
    "title": "Problem 7531",
    "description": "Write a Python function called `zip_differences_4` that must return absolute parallel differences plus 4. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_4([1, 5], [4, 2]) -> [7, 7]\n  zip_differences_4([0], [0, 1]) -> [4]",
    "initialCode": "def zip_differences_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_4(left, right):\n    return [abs(a - b) + 4 for a, b in zip(left, right)]\n\nprint(zip_differences_4([1, 5], [4, 2]))  # Expected: [7, 7]\nprint(zip_differences_4([0], [0, 1]))  # Expected: [4]\n\n# Example 2: named wrapper approach\ndef solve_problem_7531(left, right):\n    return zip_differences_4(left, right)\n\n# Example 3: static method approach\nclass Problem7531Solution:\n    @staticmethod\n    def zip_differences_4(left, right):\n        return [abs(a - b) + 4 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_4([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7532,
    "title": "Problem 7532",
    "description": "Write a Python function called `zip_differences_5` that must return absolute parallel differences plus 5. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_5([1, 5], [4, 2]) -> [8, 8]\n  zip_differences_5([0], [0, 1]) -> [5]",
    "initialCode": "def zip_differences_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_5(left, right):\n    return [abs(a - b) + 5 for a, b in zip(left, right)]\n\nprint(zip_differences_5([1, 5], [4, 2]))  # Expected: [8, 8]\nprint(zip_differences_5([0], [0, 1]))  # Expected: [5]\n\n# Example 2: named wrapper approach\ndef solve_problem_7532(left, right):\n    return zip_differences_5(left, right)\n\n# Example 3: static method approach\nclass Problem7532Solution:\n    @staticmethod\n    def zip_differences_5(left, right):\n        return [abs(a - b) + 5 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_5([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7533,
    "title": "Problem 7533",
    "description": "Write a Python function called `zip_differences_6` that must return absolute parallel differences plus 6. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_6([1, 5], [4, 2]) -> [9, 9]\n  zip_differences_6([0], [0, 1]) -> [6]",
    "initialCode": "def zip_differences_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_6(left, right):\n    return [abs(a - b) + 6 for a, b in zip(left, right)]\n\nprint(zip_differences_6([1, 5], [4, 2]))  # Expected: [9, 9]\nprint(zip_differences_6([0], [0, 1]))  # Expected: [6]\n\n# Example 2: named wrapper approach\ndef solve_problem_7533(left, right):\n    return zip_differences_6(left, right)\n\n# Example 3: static method approach\nclass Problem7533Solution:\n    @staticmethod\n    def zip_differences_6(left, right):\n        return [abs(a - b) + 6 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_6([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7534,
    "title": "Problem 7534",
    "description": "Write a Python function called `zip_differences_7` that must return absolute parallel differences plus 7. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_7([1, 5], [4, 2]) -> [10, 10]\n  zip_differences_7([0], [0, 1]) -> [7]",
    "initialCode": "def zip_differences_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_7(left, right):\n    return [abs(a - b) + 7 for a, b in zip(left, right)]\n\nprint(zip_differences_7([1, 5], [4, 2]))  # Expected: [10, 10]\nprint(zip_differences_7([0], [0, 1]))  # Expected: [7]\n\n# Example 2: named wrapper approach\ndef solve_problem_7534(left, right):\n    return zip_differences_7(left, right)\n\n# Example 3: static method approach\nclass Problem7534Solution:\n    @staticmethod\n    def zip_differences_7(left, right):\n        return [abs(a - b) + 7 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_7([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7535,
    "title": "Problem 7535",
    "description": "Write a Python function called `zip_differences_8` that must return absolute parallel differences plus 8. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_8([1, 5], [4, 2]) -> [11, 11]\n  zip_differences_8([0], [0, 1]) -> [8]",
    "initialCode": "def zip_differences_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_8(left, right):\n    return [abs(a - b) + 8 for a, b in zip(left, right)]\n\nprint(zip_differences_8([1, 5], [4, 2]))  # Expected: [11, 11]\nprint(zip_differences_8([0], [0, 1]))  # Expected: [8]\n\n# Example 2: named wrapper approach\ndef solve_problem_7535(left, right):\n    return zip_differences_8(left, right)\n\n# Example 3: static method approach\nclass Problem7535Solution:\n    @staticmethod\n    def zip_differences_8(left, right):\n        return [abs(a - b) + 8 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_8([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7536,
    "title": "Problem 7536",
    "description": "Write a Python function called `zip_differences_9` that must return absolute parallel differences plus 9. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_9([1, 5], [4, 2]) -> [12, 12]\n  zip_differences_9([0], [0, 1]) -> [9]",
    "initialCode": "def zip_differences_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_9(left, right):\n    return [abs(a - b) + 9 for a, b in zip(left, right)]\n\nprint(zip_differences_9([1, 5], [4, 2]))  # Expected: [12, 12]\nprint(zip_differences_9([0], [0, 1]))  # Expected: [9]\n\n# Example 2: named wrapper approach\ndef solve_problem_7536(left, right):\n    return zip_differences_9(left, right)\n\n# Example 3: static method approach\nclass Problem7536Solution:\n    @staticmethod\n    def zip_differences_9(left, right):\n        return [abs(a - b) + 9 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_9([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7537,
    "title": "Problem 7537",
    "description": "Write a Python function called `zip_differences_10` that must return absolute parallel differences plus 10. Practice enumerate & zip.\nDifficulty: Intermediate.\nExamples:\n  zip_differences_10([1, 5], [4, 2]) -> [13, 13]\n  zip_differences_10([0], [0, 1]) -> [10]",
    "initialCode": "def zip_differences_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef zip_differences_10(left, right):\n    return [abs(a - b) + 10 for a, b in zip(left, right)]\n\nprint(zip_differences_10([1, 5], [4, 2]))  # Expected: [13, 13]\nprint(zip_differences_10([0], [0, 1]))  # Expected: [10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7537(left, right):\n    return zip_differences_10(left, right)\n\n# Example 3: static method approach\nclass Problem7537Solution:\n    @staticmethod\n    def zip_differences_10(left, right):\n        return [abs(a - b) + 10 for a, b in zip(left, right)]\n\n# Example 4: assigned result approach\nresult = zip_differences_10([1, 5], [4, 2])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_differences_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Intermediate"
  },
  {
    "id": 7538,
    "title": "Problem 7538",
    "description": "Write a Python function called `zip_longest_fill_1` that must zip all values into lists using 1 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_1([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 1]]\n  zip_longest_fill_1([1], [\"a\", \"b\"]) -> [[1, \"a\"], [1, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_1(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_1(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=1)]\n\nprint(zip_longest_fill_1([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 1]]\nprint(zip_longest_fill_1([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [1, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7538(left, right):\n    return zip_longest_fill_1(left, right)\n\n# Example 3: static method approach\nclass Problem7538Solution:\n    @staticmethod\n    def zip_longest_fill_1(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=1)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_1([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7539,
    "title": "Problem 7539",
    "description": "Write a Python function called `zip_longest_fill_2` that must zip all values into lists using 2 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_2([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 2]]\n  zip_longest_fill_2([1], [\"a\", \"b\"]) -> [[1, \"a\"], [2, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_2(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_2(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=2)]\n\nprint(zip_longest_fill_2([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 2]]\nprint(zip_longest_fill_2([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [2, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7539(left, right):\n    return zip_longest_fill_2(left, right)\n\n# Example 3: static method approach\nclass Problem7539Solution:\n    @staticmethod\n    def zip_longest_fill_2(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=2)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_2([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7540,
    "title": "Problem 7540",
    "description": "Write a Python function called `zip_longest_fill_3` that must zip all values into lists using 3 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_3([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 3]]\n  zip_longest_fill_3([1], [\"a\", \"b\"]) -> [[1, \"a\"], [3, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_3(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_3(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=3)]\n\nprint(zip_longest_fill_3([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 3]]\nprint(zip_longest_fill_3([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [3, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7540(left, right):\n    return zip_longest_fill_3(left, right)\n\n# Example 3: static method approach\nclass Problem7540Solution:\n    @staticmethod\n    def zip_longest_fill_3(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=3)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_3([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7541,
    "title": "Problem 7541",
    "description": "Write a Python function called `zip_longest_fill_4` that must zip all values into lists using 4 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_4([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 4]]\n  zip_longest_fill_4([1], [\"a\", \"b\"]) -> [[1, \"a\"], [4, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_4(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_4(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=4)]\n\nprint(zip_longest_fill_4([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 4]]\nprint(zip_longest_fill_4([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [4, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7541(left, right):\n    return zip_longest_fill_4(left, right)\n\n# Example 3: static method approach\nclass Problem7541Solution:\n    @staticmethod\n    def zip_longest_fill_4(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=4)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_4([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7542,
    "title": "Problem 7542",
    "description": "Write a Python function called `zip_longest_fill_5` that must zip all values into lists using 5 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_5([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 5]]\n  zip_longest_fill_5([1], [\"a\", \"b\"]) -> [[1, \"a\"], [5, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_5(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_5(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=5)]\n\nprint(zip_longest_fill_5([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 5]]\nprint(zip_longest_fill_5([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [5, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7542(left, right):\n    return zip_longest_fill_5(left, right)\n\n# Example 3: static method approach\nclass Problem7542Solution:\n    @staticmethod\n    def zip_longest_fill_5(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=5)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_5([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7543,
    "title": "Problem 7543",
    "description": "Write a Python function called `zip_longest_fill_6` that must zip all values into lists using 6 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_6([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 6]]\n  zip_longest_fill_6([1], [\"a\", \"b\"]) -> [[1, \"a\"], [6, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_6(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_6(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=6)]\n\nprint(zip_longest_fill_6([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 6]]\nprint(zip_longest_fill_6([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [6, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7543(left, right):\n    return zip_longest_fill_6(left, right)\n\n# Example 3: static method approach\nclass Problem7543Solution:\n    @staticmethod\n    def zip_longest_fill_6(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=6)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_6([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7544,
    "title": "Problem 7544",
    "description": "Write a Python function called `zip_longest_fill_7` that must zip all values into lists using 7 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_7([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 7]]\n  zip_longest_fill_7([1], [\"a\", \"b\"]) -> [[1, \"a\"], [7, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_7(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_7(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=7)]\n\nprint(zip_longest_fill_7([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 7]]\nprint(zip_longest_fill_7([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [7, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7544(left, right):\n    return zip_longest_fill_7(left, right)\n\n# Example 3: static method approach\nclass Problem7544Solution:\n    @staticmethod\n    def zip_longest_fill_7(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=7)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_7([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7545,
    "title": "Problem 7545",
    "description": "Write a Python function called `zip_longest_fill_8` that must zip all values into lists using 8 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_8([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 8]]\n  zip_longest_fill_8([1], [\"a\", \"b\"]) -> [[1, \"a\"], [8, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_8(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_8(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=8)]\n\nprint(zip_longest_fill_8([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 8]]\nprint(zip_longest_fill_8([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [8, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7545(left, right):\n    return zip_longest_fill_8(left, right)\n\n# Example 3: static method approach\nclass Problem7545Solution:\n    @staticmethod\n    def zip_longest_fill_8(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=8)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_8([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7546,
    "title": "Problem 7546",
    "description": "Write a Python function called `zip_longest_fill_9` that must zip all values into lists using 9 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_9([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 9]]\n  zip_longest_fill_9([1], [\"a\", \"b\"]) -> [[1, \"a\"], [9, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_9(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_9(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=9)]\n\nprint(zip_longest_fill_9([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 9]]\nprint(zip_longest_fill_9([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [9, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7546(left, right):\n    return zip_longest_fill_9(left, right)\n\n# Example 3: static method approach\nclass Problem7546Solution:\n    @staticmethod\n    def zip_longest_fill_9(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=9)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_9([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7547,
    "title": "Problem 7547",
    "description": "Write a Python function called `zip_longest_fill_10` that must zip all values into lists using 10 as the fill value. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  zip_longest_fill_10([1, 2], [\"a\"]) -> [[1, \"a\"], [2, 10]]\n  zip_longest_fill_10([1], [\"a\", \"b\"]) -> [[1, \"a\"], [10, \"b\"]]",
    "initialCode": "from itertools import zip_longest\n\ndef zip_longest_fill_10(left, right):\n    pass",
    "solution": "from itertools import zip_longest\n\n# Example 1: canonical function approach\ndef zip_longest_fill_10(left, right):\n    return [list(pair) for pair in zip_longest(left, right, fillvalue=10)]\n\nprint(zip_longest_fill_10([1, 2], [\"a\"]))  # Expected: [[1, \"a\"], [2, 10]]\nprint(zip_longest_fill_10([1], [\"a\", \"b\"]))  # Expected: [[1, \"a\"], [10, \"b\"]]\n\n# Example 2: named wrapper approach\ndef solve_problem_7547(left, right):\n    return zip_longest_fill_10(left, right)\n\n# Example 3: static method approach\nclass Problem7547Solution:\n    @staticmethod\n    def zip_longest_fill_10(left, right):\n        return [list(pair) for pair in zip_longest(left, right, fillvalue=10)]\n\n# Example 4: assigned result approach\nresult = zip_longest_fill_10([1, 2], [\"a\"])\nprint(result)\n\n# Example 5: boundary case\nprint(zip_longest_fill_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7548,
    "title": "Problem 7548",
    "description": "Write a Python function called `indexed_products_1` that must multiply parallel values and add their index plus 1. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_1([2, 3], [4, 5]) -> [9, 17]\n  indexed_products_1([1], [9, 8]) -> [10]",
    "initialCode": "def indexed_products_1(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_1(left, right):\n    return [a * b + index + 1 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_1([2, 3], [4, 5]))  # Expected: [9, 17]\nprint(indexed_products_1([1], [9, 8]))  # Expected: [10]\n\n# Example 2: named wrapper approach\ndef solve_problem_7548(left, right):\n    return indexed_products_1(left, right)\n\n# Example 3: static method approach\nclass Problem7548Solution:\n    @staticmethod\n    def indexed_products_1(left, right):\n        return [a * b + index + 1 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_1([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_1([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7549,
    "title": "Problem 7549",
    "description": "Write a Python function called `indexed_products_2` that must multiply parallel values and add their index plus 2. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_2([2, 3], [4, 5]) -> [10, 18]\n  indexed_products_2([1], [9, 8]) -> [11]",
    "initialCode": "def indexed_products_2(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_2(left, right):\n    return [a * b + index + 2 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_2([2, 3], [4, 5]))  # Expected: [10, 18]\nprint(indexed_products_2([1], [9, 8]))  # Expected: [11]\n\n# Example 2: named wrapper approach\ndef solve_problem_7549(left, right):\n    return indexed_products_2(left, right)\n\n# Example 3: static method approach\nclass Problem7549Solution:\n    @staticmethod\n    def indexed_products_2(left, right):\n        return [a * b + index + 2 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_2([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_2([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7550,
    "title": "Problem 7550",
    "description": "Write a Python function called `indexed_products_3` that must multiply parallel values and add their index plus 3. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_3([2, 3], [4, 5]) -> [11, 19]\n  indexed_products_3([1], [9, 8]) -> [12]",
    "initialCode": "def indexed_products_3(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_3(left, right):\n    return [a * b + index + 3 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_3([2, 3], [4, 5]))  # Expected: [11, 19]\nprint(indexed_products_3([1], [9, 8]))  # Expected: [12]\n\n# Example 2: named wrapper approach\ndef solve_problem_7550(left, right):\n    return indexed_products_3(left, right)\n\n# Example 3: static method approach\nclass Problem7550Solution:\n    @staticmethod\n    def indexed_products_3(left, right):\n        return [a * b + index + 3 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_3([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_3([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7551,
    "title": "Problem 7551",
    "description": "Write a Python function called `indexed_products_4` that must multiply parallel values and add their index plus 4. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_4([2, 3], [4, 5]) -> [12, 20]\n  indexed_products_4([1], [9, 8]) -> [13]",
    "initialCode": "def indexed_products_4(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_4(left, right):\n    return [a * b + index + 4 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_4([2, 3], [4, 5]))  # Expected: [12, 20]\nprint(indexed_products_4([1], [9, 8]))  # Expected: [13]\n\n# Example 2: named wrapper approach\ndef solve_problem_7551(left, right):\n    return indexed_products_4(left, right)\n\n# Example 3: static method approach\nclass Problem7551Solution:\n    @staticmethod\n    def indexed_products_4(left, right):\n        return [a * b + index + 4 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_4([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_4([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7552,
    "title": "Problem 7552",
    "description": "Write a Python function called `indexed_products_5` that must multiply parallel values and add their index plus 5. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_5([2, 3], [4, 5]) -> [13, 21]\n  indexed_products_5([1], [9, 8]) -> [14]",
    "initialCode": "def indexed_products_5(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_5(left, right):\n    return [a * b + index + 5 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_5([2, 3], [4, 5]))  # Expected: [13, 21]\nprint(indexed_products_5([1], [9, 8]))  # Expected: [14]\n\n# Example 2: named wrapper approach\ndef solve_problem_7552(left, right):\n    return indexed_products_5(left, right)\n\n# Example 3: static method approach\nclass Problem7552Solution:\n    @staticmethod\n    def indexed_products_5(left, right):\n        return [a * b + index + 5 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_5([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_5([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7553,
    "title": "Problem 7553",
    "description": "Write a Python function called `indexed_products_6` that must multiply parallel values and add their index plus 6. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_6([2, 3], [4, 5]) -> [14, 22]\n  indexed_products_6([1], [9, 8]) -> [15]",
    "initialCode": "def indexed_products_6(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_6(left, right):\n    return [a * b + index + 6 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_6([2, 3], [4, 5]))  # Expected: [14, 22]\nprint(indexed_products_6([1], [9, 8]))  # Expected: [15]\n\n# Example 2: named wrapper approach\ndef solve_problem_7553(left, right):\n    return indexed_products_6(left, right)\n\n# Example 3: static method approach\nclass Problem7553Solution:\n    @staticmethod\n    def indexed_products_6(left, right):\n        return [a * b + index + 6 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_6([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_6([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7554,
    "title": "Problem 7554",
    "description": "Write a Python function called `indexed_products_7` that must multiply parallel values and add their index plus 7. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_7([2, 3], [4, 5]) -> [15, 23]\n  indexed_products_7([1], [9, 8]) -> [16]",
    "initialCode": "def indexed_products_7(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_7(left, right):\n    return [a * b + index + 7 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_7([2, 3], [4, 5]))  # Expected: [15, 23]\nprint(indexed_products_7([1], [9, 8]))  # Expected: [16]\n\n# Example 2: named wrapper approach\ndef solve_problem_7554(left, right):\n    return indexed_products_7(left, right)\n\n# Example 3: static method approach\nclass Problem7554Solution:\n    @staticmethod\n    def indexed_products_7(left, right):\n        return [a * b + index + 7 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_7([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_7([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7555,
    "title": "Problem 7555",
    "description": "Write a Python function called `indexed_products_8` that must multiply parallel values and add their index plus 8. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_8([2, 3], [4, 5]) -> [16, 24]\n  indexed_products_8([1], [9, 8]) -> [17]",
    "initialCode": "def indexed_products_8(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_8(left, right):\n    return [a * b + index + 8 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_8([2, 3], [4, 5]))  # Expected: [16, 24]\nprint(indexed_products_8([1], [9, 8]))  # Expected: [17]\n\n# Example 2: named wrapper approach\ndef solve_problem_7555(left, right):\n    return indexed_products_8(left, right)\n\n# Example 3: static method approach\nclass Problem7555Solution:\n    @staticmethod\n    def indexed_products_8(left, right):\n        return [a * b + index + 8 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_8([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_8([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7556,
    "title": "Problem 7556",
    "description": "Write a Python function called `indexed_products_9` that must multiply parallel values and add their index plus 9. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_9([2, 3], [4, 5]) -> [17, 25]\n  indexed_products_9([1], [9, 8]) -> [18]",
    "initialCode": "def indexed_products_9(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_9(left, right):\n    return [a * b + index + 9 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_9([2, 3], [4, 5]))  # Expected: [17, 25]\nprint(indexed_products_9([1], [9, 8]))  # Expected: [18]\n\n# Example 2: named wrapper approach\ndef solve_problem_7556(left, right):\n    return indexed_products_9(left, right)\n\n# Example 3: static method approach\nclass Problem7556Solution:\n    @staticmethod\n    def indexed_products_9(left, right):\n        return [a * b + index + 9 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_9([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_9([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  },
  {
    "id": 7557,
    "title": "Problem 7557",
    "description": "Write a Python function called `indexed_products_10` that must multiply parallel values and add their index plus 10. Practice enumerate & zip.\nDifficulty: Expert.\nExamples:\n  indexed_products_10([2, 3], [4, 5]) -> [18, 26]\n  indexed_products_10([1], [9, 8]) -> [19]",
    "initialCode": "def indexed_products_10(left, right):\n    pass",
    "solution": "# Example 1: canonical function approach\ndef indexed_products_10(left, right):\n    return [a * b + index + 10 for index, (a, b) in enumerate(zip(left, right))]\n\nprint(indexed_products_10([2, 3], [4, 5]))  # Expected: [18, 26]\nprint(indexed_products_10([1], [9, 8]))  # Expected: [19]\n\n# Example 2: named wrapper approach\ndef solve_problem_7557(left, right):\n    return indexed_products_10(left, right)\n\n# Example 3: static method approach\nclass Problem7557Solution:\n    @staticmethod\n    def indexed_products_10(left, right):\n        return [a * b + index + 10 for index, (a, b) in enumerate(zip(left, right))]\n\n# Example 4: assigned result approach\nresult = indexed_products_10([2, 3], [4, 5])\nprint(result)\n\n# Example 5: boundary case\nprint(indexed_products_10([], []))",
    "hint": "Focus on enumerate start values, zip shortest-input behavior, tuple unpacking, indexes, and parallel values. Derive the behavior from the task instead of copying an example output.",
    "breakdown": "1. Identify every input type and the exact return type.\n2. Apply the required enumerate & zip rule.\n3. Trace intermediate values in execution order.\n4. Check empty, invalid, tied, or boundary inputs.\n5. Return a general result for all hidden tests.",
    "category": "Enumerate & Zip Difficult"
  }
];
