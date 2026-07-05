const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'exercises.ts'), 'utf8');

function findField(src, fromIdx, fieldName) {
  const re = new RegExp(`"${fieldName}":\\s*"`, 'g');
  re.lastIndex = fromIdx;
  const m = re.exec(src);
  if (!m) return null;
  const valStart = m.index + m[0].length;
  let i = valStart, esc = false;
  while (i < src.length) {
    if (src[i] === '\\' && !esc) { esc = true; i++; continue; }
    if (esc) { esc = false; i++; continue; }
    if (src[i] === '"') break;
    i++;
  }
  return i < src.length ? { valueStart: valStart, valueEnd: i } : null;
}

function replaceField(src, info, newVal) {
  const escaped = newVal.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n');
  return src.slice(0, info.valueStart) + escaped + src.slice(info.valueEnd);
}

function getBlockBounds(src, id) {
  const startIdx = src.indexOf(`"id": ${id},`);
  if (startIdx === -1) return null;
  let blockStart = startIdx, depth = 0;
  while (blockStart >= 0) {
    if (src[blockStart] === '}') depth++;
    if (src[blockStart] === '{') { depth--; if (depth < 0) break; }
    blockStart--;
  }
  if (blockStart < 0) return null;
  let blockEnd = startIdx, inStr = false, quoteCh = '', esc = false;
  depth = 0;
  while (blockEnd < src.length) {
    const ch = src[blockEnd];
    if (inStr) {
      if (esc) esc = false;
      else if (ch === '\\') esc = true;
      else if (ch === quoteCh) inStr = false;
      blockEnd++; continue;
    }
    if (ch === '"' || ch === "'") { inStr = true; quoteCh = ch; blockEnd++; continue; }
    if (ch === '{') depth++;
    if (ch === '}') { depth--; if (depth < 0) { blockEnd++; if (src[blockEnd] === ',') blockEnd++; break; } }
    blockEnd++;
  }
  return { start: blockStart, end: blockEnd };
}

const fixes = {
  72: {
    desc: `Write a Python program to check if a given string is a valid email address. Prompt the user to enter an email address.\nExamples:\n  is_valid_email("test@example.com") \u2192 True\n  is_valid_email("invalid") \u2192 False`,
    breakdown: `1. Define \`is_valid_email(email)\` with a parameter \`email\`.\n2. Use \`re.match()\` with a regex pattern like \`r"[\\w.-]+@[\\w.-]+\\.\\w+$"\` to match valid email format.\n3. Return \`True\` if the pattern matches, \`False\` otherwise.`,
    hint: `Use \`re.match()\` with an email regex pattern — it returns a match object or \`None\`.\nA basic email pattern: \`r"[\\w.-]+@[\\w.-]+\\.\\w+$"\`.\n\`re.match()\` returns a match object (truthy) on success, \`None\` (falsy) on failure.`,
  },
  82: {
    desc: `Write a Python program to find the area of a circle. Prompt the user to enter the radius.\nExamples:\n  calculate_circle_area(5) \u2192 78.54\n  calculate_circle_area(7) \u2192 153.94`,
    breakdown: `1. Define \`calculate_circle_area(radius)\` with a parameter \`radius\`.\n2. Use \`math.pi * radius ** 2\` to calculate the area of the circle.\n3. Return the result rounded to 2 decimal places if needed.`,
    hint: `Area of a circle = \u03c0 \u00d7 r\u00b2.\nUse \`math.pi\` for the value of \u03c0.\nRound large float results with \`round(result, 2)\` for display.`,
  },
  112: {
    desc: `Write a Python program to generate all possible permutations of a given string.\nExamples:\n  generate_permutations("AB") \u2192 ["AB", "BA"]\n  generate_permutations("ABC") \u2192 ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]`,
    breakdown: `1. Import \`permutations\` from \`itertools\`.\n2. Define \`generate_permutations(string)\` with a parameter \`string\`.\n3. Use \`permutations(string)\` to generate all permutations, then join each tuple back into a string.\n4. Return the list of permutation strings.`,
    hint: `\`itertools.permutations()\` returns tuples of characters — use \`"".join(p)\` to convert each tuple to a string.\nWrap the result in \`list()\` to materialize all permutations.`,
  },
  131: {
    desc: `Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the maximum using reduce().\nExamples:\n  max_in_list([3, 1, 4, 1, 5]) \u2192 5\n  max_in_list([9, -2, 4]) \u2192 9`,
    breakdown: `1. Import \`reduce\` from \`functools\`.\n2. Define a helper function \`max_func(a, b)\` that returns \`a if a > b else b\`.\n3. Define \`max_in_list(lst)\` that calls \`reduce(max_func, lst)\`.\n4. Return the result of \`reduce()\`.`,
    hint: `\`reduce()\` applies a function cumulatively.\nDefine a helper \`max_func(a, b)\` that returns the larger of two values.\n\`reduce(max_func, lst)\` reduces the list to the single largest element.`,
  },
  510: {
    desc: `Create a base class Plant with a method grow(). Create a derived class Flower that overrides the grow() method.\nExamples:\n  plant = Plant(); plant.grow() \u2192 "Plant is growing"\n  flower = Flower(); flower.grow() \u2192 "Flower is blooming"`,
    breakdown: `1. Define a base class \`Plant\` with a \`grow()\` method that returns a base message.\n2. Define a derived class \`Flower(Plant)\` that inherits from \`Plant\`.\n3. Override the \`grow()\` method in \`Flower\` to return a different message.\n4. Instantiate both classes and call their \`grow()\` methods.`,
    hint: `Inheritance: \`class Child(Parent):\` creates a child class.\nOverriding: define a method with the same name in the child class.\nThe child class inherits all parent methods that are not overridden.`,
  },
  574: {
    desc: `Product of List: Write a function that computes the product of a list of numbers using reduce().\nExamples:\n  sum_of_lst([1, 2, 3, 4]) \u2192 24\n  sum_of_lst([2, 5, 3]) \u2192 30`,
    breakdown: `1. Import \`reduce\` from \`functools\`.\n2. Define a helper function \`multiply(x, y)\` that returns \`x * y\`.\n3. Define \`sum_of_lst(lst)\` that calls \`reduce(multiply, lst)\`.\n4. Return the result of \`reduce()\`.`,
    hint: `Despite the name \`sum_of_lst\`, this problem computes the PRODUCT, not the sum.\n\`reduce(multiply, lst)\` multiplies all elements together.\nUse a helper \`multiply(x, y)\` that returns \`x * y\`.`,
  },
  603: {
    desc: `Average of List: Write a function that calculates the average of a list of numbers using reduce().\nExamples:\n  average([1, 2, 3, 4, 5]) \u2192 3.0\n  average([]) \u2192 0`,
    breakdown: `1. Import \`reduce\` from \`functools\`.\n2. Define \`add(x, y)\` helper and use \`len()\` for the count.\n3. Define \`average(lst)\` — handle empty list (return 0), then use \`reduce(add, lst) / len(lst)\`.\n4. Return the calculated average.`,
    hint: `Handle the empty list case first — return 0.\nUse \`reduce(add, lst) / len(lst)\` for the average.\nDefine \`add(x, y)\` as a helper function for \`reduce()\`.`,
  },
  1400: {
    desc: `Write a Python function that accepts **kwargs and returns only those key-value pairs where the key is uppercase.\nExamples:\n  uppercase_keys_only(Name="Alice", age=30) \u2192 {"Name": "Alice"}\n  uppercase_keys_only(KEY="value", other=42) \u2192 {"KEY": "value"}`,
    breakdown: `1. Define \`uppercase_keys_only(**kwargs)\` with \`**kwargs\` parameter.\n2. Use a dictionary comprehension: \`{k: v for k, v in kwargs.items() if k.isupper()}\`.\n3. Return the filtered dictionary containing only uppercase-key items.`,
    hint: `\`**kwargs\` collects all keyword arguments into a dictionary.\nUse \`k.isupper()\` to check if a key is entirely uppercase.\nA dictionary comprehension with an \`if\` clause filters the kwargs.`,
  },
};

let result = source;
let applied = 0;

for (const [idStr, fields] of Object.entries(fixes)) {
  const id = Number(idStr);
  const bounds = getBlockBounds(result, id);
  if (!bounds) { console.log(`P${id}: not found`); continue; }
  let block = result.slice(bounds.start, bounds.end);

  if (fields.desc) {
    const info = findField(block, 0, 'description');
    if (info) block = replaceField(block, info, fields.desc);
  }
  if (fields.breakdown) {
    const info = findField(block, 0, 'breakdown');
    if (info) block = replaceField(block, info, fields.breakdown);
  }
  if (fields.hint) {
    const info = findField(block, 0, 'hint');
    if (info) block = replaceField(block, info, fields.hint);
  }

  result = result.slice(0, bounds.start) + block + result.slice(bounds.end);
  applied++;
  console.log(`P${id}: fixed`);
}

fs.writeFileSync(path.join(root, 'exercises.ts'), result);
console.log(`\nFixed ${applied} problems`);
