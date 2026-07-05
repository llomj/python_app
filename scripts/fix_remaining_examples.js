const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'exercises.ts'), 'utf8');

/* ── field locator ── */
function findField(src, fromIdx, fieldName) {
  const re = new RegExp(`"${fieldName}":\\s*"`, 'g');
  re.lastIndex = fromIdx;
  const m = re.exec(src);
  if (!m) return null;
  const valStart = m.index + m[0].length;
  let i = valStart;
  while (i < src.length) {
    if (src[i] === '\\') { i += 2; continue; }
    if (src[i] === '"') break;
    i++;
  }
  return i < src.length ? { valueStart: valStart, valueEnd: i } : null;
}

function replaceField(src, info, newVal) {
  const escaped = newVal
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\n/g, '\\n');
  return src.slice(0, info.valueStart) + escaped + src.slice(info.valueEnd);
}

/* ── fixes ── */
const fixes = {
  // P265: euclidean_distance(5,5) -> euclidean_distance([3,4], [6,8]) -> 5
  265: {
    description: 'Write a Python program to calculate the Euclidean distance between two points in 2D space using `zip()`.\\nExamples:\\n  euclidean_distance([3, 4], [6, 8]) → 5\\n  euclidean_distance([0, 0], [3, 4]) → 5',
    breakdown: '1. Define `euclidean_distance(point1, point2)` with parameters `point1`, `point2`.\\n2. Use `zip(point1, point2)` to pair corresponding coordinates from each point.\\n3. For each pair, calculate the squared difference and sum them.\\n4. Apply `math.sqrt()` to the sum to get the Euclidean distance.\\n5. Return the result.',
    hint: 'Remember that `zip()` pairs elements positionally: `zip([x1,y1], [x2,y2])` gives `[(x1,x2), (y1,y2)]`.\\nUse `math.sqrt()` on the sum of squared differences.\\nThe distance between (0,0) and (3,4) is 5.0.',
  },
  // P576: min_number(5,5) -> min_number([3,1,4,1,5]) -> 1
  576: {
    description: 'Find Minimum: Write a function that finds the minimum number in a list using reduce().\\nExamples:\\n  min_number([3, 1, 4, 1, 5]) → 1\\n  min_number([9, -2, 4]) → -2',
    breakdown: '1. Define the `min_number` function with one parameter: a list of numbers.\\n2. Use `functools.reduce()` with a lambda that returns the smaller of two values.\\n3. The lambda should compare `a` and `b` and return `a if a < b else b`.\\n4. Return the result of `reduce()`.',
    hint: '`from functools import reduce` is required.\\nThe lambda for `reduce()` should compare two values and return the smaller one.',
  },
  // P842: solve(5,5) -> script with input loop
  842: {
    description: 'Write a Python program to keep asking the user for positive numbers and print the sum when a negative number is entered using a while loop.\\nExamples:\\n  Input: 4, 6, 2, -1 → Output: 12\\n  Input: -5 → Output: 0',
    breakdown: '1. Initialize a variable `total` to 0 before the loop.\\n2. Use a `while True` loop that keeps asking for input.\\n3. Convert each input to an integer.\\n4. If the number is negative, break out of the loop and print `total`.\\n5. Otherwise, add the number to `total`.',
    hint: 'Use `int(input())` to get an integer from the user.\\nBreak the loop when a negative number is entered, then print the accumulated sum.\\nInitialize the sum variable to 0 before the loop starts.',
  },
  // P1191: calculate_gcd(5,5) -> calculate_gcd(12, 8) -> 4
  1191: {
    description: 'Write a Python program to use the `math` module to calculate the greatest common divisor (GCD) of two numbers.\\nExamples:\\n  calculate_gcd(12, 8) → 4\\n  calculate_gcd(48, 180) → 12',
    breakdown: '1. Import the `math` module.\\n2. Define a function `calculate_gcd` that takes two numbers as parameters.\\n3. Call `math.gcd(a, b)` inside the function.\\n4. Return the result.',
    hint: '`math.gcd()` returns the greatest common divisor of two integers.\\nNo need to implement Euclid\'s algorithm manually — `math.gcd()` does it for you.',
  },
  // P1192: rename_file('hello','hello') -> rename_file with different filenames
  1192: {
    description: 'Write a Python program to use the `os` module to rename a file.\\nExamples:\\n  rename_file("old_file.txt", "new_file.txt") → file renamed\\n  rename_file("source_note.txt", "target_note.txt") → file renamed',
    breakdown: '1. Import the `os` module.\\n2. Define a function `rename_file` that takes `old_name` and `new_name` as parameters.\\n3. Call `os.rename(old_name, new_name)` to rename the file.\\n4. The function does not need to return anything.',
    hint: '`os.rename(src, dst)` renames a file from `src` to `dst`.\\nThe destination should not already exist (or it will be overwritten on some systems).',
  },
  // P1614: compare(5,5) -> compare(5, 3) -> -2
  1614: {
    description: 'Write a Pythonic way to use `functools.cmp_to_key()` to convert an old-style comparison function to a key function.\\nExamples:\\n  compare(5, 3) → -2\\n  compare(2, 5) → 3\\n  compare(4, 4) → 0',
    breakdown: '1. Define a comparison function that takes two values and returns a negative, zero, or positive number (old-style cmp).\\n2. Use `cmp_to_key(compare_function)` to convert it to a key function.\\n3. Pass the result to `sorted()` as the `key` parameter.\\n4. Return the sorted result.',
    hint: '`cmp_to_key()` is imported from `functools`.\\nOld-style cmp returns a negative number if `a < b`, 0 if equal, positive if `a > b`.',
  },
  // P1616: process_scores('hello','hello') -> process_scores with dict
  1616: {
    description: 'Write a Python program using `typing.Dict` to specify a function parameter that accepts a dictionary with string keys and integer values.\\nExamples:\\n  process_scores({"Alice": 85, "Bob": 90}) → 175\\n  process_scores({"A": 1, "B": 2, "C": 3}) → 6',
    breakdown: '1. Import `Dict` from `typing`.\\n2. Define a function with a parameter typed as `Dict[str, int]`.\\n3. Sum all the dictionary values using `sum(d.values())`.\\n4. Return the total sum.',
    hint: 'Use `from typing import Dict` to import the type hint.\\nAdd the type hint to the parameter: `def process_scores(scores: Dict[str, int]):`\\n`sum(d.values())` adds all values in the dictionary.',
  },
  // P1618: apply_operation(5,5,5,5,5) -> apply_operation(5, 3) -> 15
  1618: {
    description: 'Write a Python program using `typing.Callable` to specify a function parameter that accepts a callable.\\nExamples:\\n  apply_operation(5, 3, lambda a, b: a * b) → 15\\n  apply_operation(5, 3, lambda a, b: a + b) → 8',
    breakdown: '1. Import `Callable` from `typing`.\\n2. Define a function that takes two numbers and a callable parameter.\\n3. The callable parameter should be typed as `Callable[[int, int], int]`.\\n4. Call the callable with the two numbers and return the result.',
    hint: 'Use `from typing import Callable`.\\nThe type hint for a function that takes two ints and returns an int is `Callable[[int, int], int]`.',
  },
  // P1622: __setitem__(5,5) -> proper class example
  1622: {
    description: 'Write a Python class implementing `__setitem__` magic method to enable item assignment.\\nExamples:\\n  obj = MyDict(); obj["key"] = "value"; print(obj["key"]) → value\\n  obj["count"] = 3; print(obj["count"]) → 3',
    breakdown: '1. Define a class `MyDict` with an `__init__` method that initializes an internal dictionary.\\n2. Implement `__setitem__(self, key, value)` to store items in the internal dict.\\n3. Implement `__getitem__(self, key)` to retrieve items from the internal dict.\\n4. Return the value from `__getitem__`.',
    hint: '`__setitem__` is called when you write `obj[key] = value`.\\n`__getitem__` is called when you read `obj[key]`.\\nUse a regular dictionary internally to store the key-value pairs.',
  },
  // P1888: calculate_distance(5,5,5,5) -> calculate_distance(0, 0, 3, 4) -> 5
  1888: {
    description: 'Write a Python function called `calculate_distance` that takes two points (x1, y1) and (x2, y2) and returns the Euclidean distance between them.\\nExamples:\\n  calculate_distance(0, 0, 3, 4) → 5.0\\n  calculate_distance(1, 1, 4, 5) → 5.0',
    breakdown: '1. Define a function `calculate_distance` with four parameters: `x1, y1, x2, y2`.\\n2. Calculate the squared differences: `(x2 - x1)**2 + (y2 - y1)**2`.\\n3. Use `math.sqrt()` to get the distance.\\n4. Return the result.',
    hint: 'Use `math.sqrt()` to compute the square root.\\nThe distance between (0,0) and (3,4) is 5.0 from the formula sqrt((3-0)^2 + (4-0)^2).',
  },
  // P1969: calculate_quadratic_roots(5,5,5) -> calculate_quadratic_roots(1, -5, 6) -> (3.0, 2.0)
  1969: {
    description: 'Write a Python function called `calculate_quadratic_roots` that takes coefficients a, b, c and returns the roots of ax^2 + bx + c = 0 as a tuple (or None if no real roots).\\nExamples:\\n  calculate_quadratic_roots(1, -5, 6) → (3.0, 2.0)\\n  calculate_quadratic_roots(1, 0, 1) → None',
    breakdown: '1. Define `calculate_quadratic_roots(a, b, c)` with three coefficients.\\n2. Calculate the discriminant: `d = b**2 - 4*a*c`.\\n3. If `d < 0`, return `None` (no real roots).\\n4. Otherwise, compute roots: `((-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a))`.\\n5. Return the tuple of roots.',
    hint: 'Use `math.sqrt()` for the square root.\\nIf the discriminant is negative, there are no real roots — return `None`.\\nUse the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a',
  },
};

/* ── apply fixes ── */
let result = source;
let applied = 0;

for (const [idStr, fields] of Object.entries(fixes)) {
  const id = Number(idStr);
  const startIdx = result.indexOf(`"id": ${id},`);
  if (startIdx === -1) { console.log('P' + id + ': not found'); continue; }

  let blockStart = startIdx;
  let depth = 0;
  while (blockStart >= 0) {
    if (result[blockStart] === '}') depth++;
    if (result[blockStart] === '{') { depth--; if (depth < 0) break; }
    blockStart--;
  }
  if (blockStart < 0) { console.log('P' + id + ': block not found'); continue; }

  let blockEnd = startIdx;
  depth = 0;
  let inStr = false, quoteCh = '', esc = false;
  while (blockEnd < result.length) {
    const ch = result[blockEnd];
    if (inStr) {
      if (esc) esc = false;
      else if (ch === '\\') esc = true;
      else if (ch === quoteCh) inStr = false;
      blockEnd++; continue;
    }
    if (ch === '"' || ch === "'") { inStr = true; quoteCh = ch; blockEnd++; continue; }
    if (ch === '{') depth++;
    if (ch === '}') { depth--; if (depth < 0) { blockEnd++; break; } }
    blockEnd++;
  }

  // Get the block
  let block = result.slice(blockStart, blockEnd);

  if (fields.description) {
    const info = findField(block, 0, 'description');
    if (info) block = replaceField(block, info, fields.description);
  }
  if (fields.breakdown) {
    const info = findField(block, 0, 'breakdown');
    if (info) block = replaceField(block, info, fields.breakdown);
  }
  if (fields.hint) {
    const info = findField(block, 0, 'hint');
    if (info) block = replaceField(block, info, fields.hint);
  }

  result = result.slice(0, blockStart) + block + result.slice(blockEnd);
  applied++;
  console.log('P' + id + ': fixed');
}

fs.writeFileSync(path.join(root, 'exercises.ts'), result);
console.log('\\nFixed ' + applied + ' problems');
