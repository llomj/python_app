#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const write = process.argv.includes('--write');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'problem-description-repair-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'entry.cjs');

const pythonValue = value => {
  if (value === null) return 'None';
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(pythonValue).join(', ')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.entries(value).map(([key, item]) => `${pythonValue(key)}: ${pythonValue(item)}`).join(', ')}}`;
  }
  return String(value);
};

const hasRepeatedExampleLines = description => {
  const section = String(description).split(/\n(?:Examples?|Exemples?)\s*:\s*\n/i).slice(1).join('\n');
  if (!section) return false;
  const counts = new Map();
  for (const line of section.split('\n').map(item => item.trim()).filter(Boolean)) {
    counts.set(line, (counts.get(line) || 0) + 1);
  }
  return [...counts.values()].some(count => count > 1);
};

const examplesFromGrader = grader => {
  if (!grader?.tests?.length) return [];
  const functionName = grader.functionNames?.find(name => name !== 'main') || grader.functionNames?.[0];
  return grader.tests.slice(0, 3).flatMap(test => {
    if (test.expected === undefined) return [];
    if (functionName && grader.mode !== 'script' && Array.isArray(test.args)) {
      return [`  ${(test.functionName || functionName)}(${test.args.map(pythonValue).join(', ')}) → ${pythonValue(test.expected)}`];
    }
    const inputs = Array.isArray(test.inputValues) && test.inputValues.length
      ? test.inputValues.map(pythonValue).join(', ')
      : null;
    return [`  ${inputs ? `input ${inputs}` : 'program output'} → ${pythonValue(test.expected)}`];
  });
};

const DESCRIPTION_OVERRIDES = new Map([
  [221, 'Write a Python function called `print_hollow_square` that takes a side length and prints a hollow square made of stars. The first and last rows are full; middle rows contain a star at each edge.\nExamples:\n  print_hollow_square(5) → "*****\\n*   *\\n*   *\\n*   *\\n*****"\n  print_hollow_square(3) → "***\\n* *\\n***"'],
  [227, 'Write a Python function called `print_zigzag` that takes a row count and prints an alternating zigzag pattern of stars.\nExamples:\n  print_zigzag(5) → "*       * \\n  *       \\n*       * \\n  *       \\n*       *"\n  print_zigzag(3) → "*   *\\n  *\\n*   *"'],
  [228, 'Write a Python function called `print_cross` that takes an odd row count and prints an X-shaped cross made of stars.\nExamples:\n  print_cross(5) → "*   *\\n * * \\n  *  \\n * * \\n*   *"\n  print_cross(3) → "* *\\n * \\n* *"'],
  [114, 'Define a function `max_of_three()` that takes three numbers and returns the largest one.\nExamples:\n  max_of_three(1, 5, 3) → 5\n  max_of_three(-10, -2, -5) → -2\n  max_of_three(7, 7, 1) → 7'],
  [224, 'Write a Python program to print a triangle pattern of letters, adding one repeated letter on each row.\nExamples:\n  triangle_pattern(5) → "A\\nB B\\nC C C\\nD D D D\\nE E E E E"\n  triangle_pattern(3) → "A\\nB B\\nC C C"'],
  [265, 'Write a Python function called `euclidean_distance` that takes two coordinate lists and returns the Euclidean distance between them using `zip()` and `math.sqrt()`.\nExamples:\n  euclidean_distance([3, 4], [6, 8]) → 5\n  euclidean_distance([0, 0], [3, 4]) → 5'],
  [297, 'Write a Python program to find the sum of all elements in a list using a `while` loop.\nExamples:\n  sum_elements([1, 2, 3, 4, 5]) → 15\n  sum_elements([]) → 0\n  sum_elements([-2, 5]) → 3'],
  [576, 'Write a Python function called `number_lst` that takes a non-empty list of numbers and returns its smallest value using `functools.reduce()`.\nExamples:\n  number_lst([3, 1, 4, 1, 5]) → 1\n  number_lst([9, -2, 4]) → -2'],
  [841, 'Write a Python program that reads a starting integer and uses a while loop to print a countdown from that integer to 0, including both endpoints.\nExamples:\n  Input: 4 → Output: "4\\n3\\n2\\n1\\n0"\n  Input: 0 → Output: "0"'],
  [842, 'Write a Python program that repeatedly reads integers, adds the non-negative values, and prints the total when a negative integer is entered. Use a while loop.\nExamples:\n  Input: 4, 6, 2, -1 → Output: 12\n  Input: -5 → Output: 0'],
  [1191, 'Write a Python function called `calculate_gcd` that takes two integers and returns their greatest common divisor using `math.gcd()`.\nExamples:\n  calculate_gcd(12, 8) → 4\n  calculate_gcd(48, 180) → 12'],
  [1192, "Write a Python function called `rename_file` that takes an old file name and a new file name, then renames the file using `os.rename()`.\nExamples:\n  rename_file('old_file.txt', 'new_file.txt') → {'new_file.txt':'renamed content','old_file.txt':null}\n  rename_file('source_note.txt', 'target_note.txt') → {'target_note.txt':'second rename','source_note.txt':null}"],
  [1614, 'Write a Python comparison function called `compare` for use with `functools.cmp_to_key()`. Return a negative number when the first value is greater, a positive number when it is smaller, and 0 when equal.\nExamples:\n  compare(5, 3) → -2\n  compare(2, 5) → 3\n  compare(4, 4) → 0'],
  [1616, "Write a Python function called `process_scores` that accepts a `Dict[str, int]` and returns the sum of all score values.\nExamples:\n  process_scores({'Alice':85,'Bob':90}) → 175\n  process_scores({'A':1,'B':2,'C':3}) → 6"],
  [1618, 'Write a Python function called `apply_operation` that takes two integers and a `Callable[[int, int], int]`, then returns the result of calling that operation with the integers.\nExamples:\n  apply_operation(5, 3, lambda a, b: a * b) → 15\n  apply_operation(5, 3, lambda a, b: a + b) → 8'],
  [1622, 'Write a Python class called `MyDict` that implements `__setitem__` and `__getitem__` so values can be assigned and retrieved with square brackets.\nExamples:\n  obj = MyDict(); obj["key"] = "value"; obj["key"] → "value"\n  obj = MyDict(); obj["count"] = 3; obj["count"] → 3'],
  [1888, 'Write a Python function called `calculate_distance` that takes two points as four coordinates and returns their Euclidean distance using `math.sqrt()`.\nExamples:\n  calculate_distance(0, 0, 3, 4) → 5\n  calculate_distance(1, 1, 4, 5) → 5'],
  [1969, 'Write a Python function called `calculate_quadratic_roots` that takes coefficients `a`, `b`, and `c`, returns both real roots using the quadratic formula, and returns `None` when there are no real roots.\nExamples:\n  calculate_quadratic_roots(1, -5, 6) → [3, 2]\n  calculate_quadratic_roots(1, 0, 1) → None'],
]);

fs.writeFileSync(entry, [
  `export { EXERCISES } from ${JSON.stringify(path.join(root, 'exercises.ts'))};`,
  `export { AUTO_GRADERS } from ${JSON.stringify(path.join(root, 'graders.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const { EXERCISES, AUTO_GRADERS } = require(bundle);
  let source = fs.readFileSync(path.join(root, 'exercises.ts'), 'utf8');
  let repaired = 0;

  for (const exercise of EXERCISES) {
    const override = DESCRIPTION_OVERRIDES.get(exercise.id);
    const repeatedExamples = exercise.id <= 2000 && hasRepeatedExampleLines(exercise.description);
    if (!override && !repeatedExamples) continue;
    const examples = repeatedExamples ? examplesFromGrader(AUTO_GRADERS[exercise.id]) : [];
    if (!override && !examples.length) continue;
    const task = exercise.description.split(/\n(?:Examples?|Exemples?)\s*:/i)[0].trim();
    const replacement = override || `${task}\nExamples:\n${examples.join('\n')}`;
    if (replacement === exercise.description) continue;
    const before = `\"description\": ${JSON.stringify(exercise.description)}`;
    const after = `\"description\": ${JSON.stringify(replacement)}`;
    if (!source.includes(before)) throw new Error(`Could not locate description for problem ${exercise.id}`);
    source = source.replace(before, after);
    repaired += 1;
  }

  console.log(`Problem descriptions requiring repair: ${repaired}`);
  if (write) {
    fs.writeFileSync(path.join(root, 'exercises.ts'), source);
    console.log('exercises.ts updated.');
  } else {
    console.log('Dry run only. Add --write to apply repairs.');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
