import fs from 'node:fs';

const startId = 2081;
const exercises = [];
const graders = {};

const q = (value) => JSON.stringify(value);
const repr = (value) => {
  if (typeof value === 'string') return q(value);
  if (typeof value === 'boolean') return value ? 'True' : 'False';
  if (Array.isArray(value)) return `[${value.map(repr).join(', ')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.entries(value).map(([key, val]) => `${q(key)}: ${repr(val)}`).join(', ')}}`;
  }
  return String(value);
};

const tupleRepr = (items) => `(${items.map(repr).join(', ')}${items.length === 1 ? ',' : ''})`;

const cleanScript = (script) => script
  .replace(/^#\s*Script approach\s*\n/i, '')
  .trim();

const indent = (code, spaces = 4) => code
  .split('\n')
  .map((line) => (line ? `${' '.repeat(spaces)}${line}` : line))
  .join('\n');

const compactScript = (script) => {
  const body = cleanScript(script);
  const resultMatch = body.match(/^([\s\S]*?)\nresult\s*=\s*([^\n]+)\nprint\(result\)$/);
  if (resultMatch) {
    const setup = resultMatch[1].trim();
    const expression = resultMatch[2].trim();
    return `${setup ? `${setup}\n` : ''}print(${expression})`;
  }

  const assignmentPrintMatch = body.match(/^([A-Za-z_]\w*)\s*=\s*([^\n]+)\nprint\(\1\)$/);
  if (assignmentPrintMatch) {
    const [, name, value] = assignmentPrintMatch;
    return `${name} = ${value}\nprint(${name})`;
  }

  return body;
};

const commentedScript = (script) => cleanScript(script)
  .split('\n')
  .flatMap((line, index) => {
    const trimmed = line.trim();
    if (!trimmed) return [line];
    if (/^print\(/.test(trimmed)) return [`# Step ${index + 1}: display the final answer.`, line];
    if (/^if\b/.test(trimmed)) return [`# Step ${index + 1}: check the condition before printing.`, line];
    if (/=/.test(trimmed) && !/[=!<>]=/.test(trimmed)) return [`# Step ${index + 1}: store a value in a name.`, line];
    return [`# Step ${index + 1}: run this Python statement.`, line];
  })
  .join('\n');

const functionScript = (script) => {
  const body = cleanScript(script);
  const lines = body.split('\n');
  const printIndexes = lines
    .map((line, index) => (/^\s*print\(([\s\S]*)\)\s*$/.test(line) ? index : -1))
    .filter((index) => index >= 0);

  if (printIndexes.length === 1 && printIndexes[0] === lines.length - 1) {
    const expression = lines[lines.length - 1].trim().match(/^print\(([\s\S]*)\)$/)?.[1] ?? '';
    const setup = lines.slice(0, -1).join('\n').trim();
    const functionBody = `${setup ? `${setup}\n` : ''}return ${expression}`;
    return `def solve():\n${indent(functionBody)}\n\nprint(solve())`;
  }

  return `def solve():\n${indent(body)}\n\nsolve()`;
};

const manualScript = (script) => {
  const body = cleanScript(script);
  const singlePrint = body.match(/^print\(([\s\S]+)\)$/);
  if (singlePrint) {
    return `# Step 1: store the answer in a clear name.\nanswer = ${singlePrint[1]}\n# Step 2: display the answer.\nprint(answer)`;
  }
  return commentedScript(script);
};

const buildTeachingSolution = (script) => {
  const body = cleanScript(script);
  const functionBlock = `# Using function approach\n${functionScript(script)}`;
  const scriptBlock = `# Using script approach\n${body}`;
  const directBlock = `# Direct approach\n${compactScript(script)}`;
  const manualBlock = `# Manual step-by-step approach\n${manualScript(script)}`;
  return [functionBlock, scriptBlock, directBlock, manualBlock].join('\n\n');
};

const add = ({ title, description, initialCode, solution, hint, breakdown, expected, requiredNodePatterns = [], requiredCallPatterns = [] }) => {
  const id = startId + exercises.length;
  exercises.push({
    id,
    title: `Problem ${id}`,
    description,
    initialCode: initialCode ?? '# Write your code here\n',
    solution: buildTeachingSolution(solution),
    hint,
    breakdown,
    category: 'Atomic Beginner',
  });
  graders[id] = {
    functionNames: ['main'],
    mode: 'script',
    compare: 'printedOrReturn',
    ...(requiredNodePatterns.length ? { requiredNodePatterns } : {}),
    ...(requiredCallPatterns.length ? { requiredCallPatterns } : {}),
    tests: [{ args: [], expected }],
  };
};

const printCall = { functionName: 'print', minArgs: 1 };
const node = (nodeType, minCount = 1) => ({ nodeType, minCount });

const addPrintLiteral = (text, label) => add({
  title: `Print ${label}`,
  description: `Write a Python program that prints the text ${q(text)}.`,
  solution: `# Script approach\nprint(${q(text)})`,
  hint: 'Use print() and put text inside quotes.',
  breakdown: `1. Write print().\n2. Put ${q(text)} inside the parentheses.\n3. Run the code and check that the output is exactly ${q(text)}.`,
  expected: text,
  requiredCallPatterns: [printCall],
});

const addPrintNumber = (value) => add({
  title: `Print ${value}`,
  description: `Write a Python program that prints the number ${value}.`,
  solution: `# Script approach\nprint(${value})`,
  hint: 'Numbers do not need quotes.',
  breakdown: `1. Write print().\n2. Put the number ${value} inside the parentheses.\n3. The output should show ${value}.`,
  expected: value,
  requiredCallPatterns: [printCall],
});

const addStringVariable = (name, value) => add({
  description: `Create a variable called \`${name}\` and store the string ${q(value)} in it. Then print the variable.`,
  solution: `# Script approach\n${name} = ${q(value)}\nprint(${name})`,
  hint: 'Use variable_name = "text", then print the variable name.',
  breakdown: `1. Create the variable with ${name} = ${q(value)}.\n2. Print ${name} without quotes.\n3. The output should be ${q(value)}.`,
  expected: value,
  requiredNodePatterns: [node('Assign')],
  requiredCallPatterns: [printCall],
});

const addNumberVariable = (name, value) => add({
  description: `Create a variable called \`${name}\` and store the number ${value} in it. Then print the variable.`,
  solution: `# Script approach\n${name} = ${value}\nprint(${name})`,
  hint: 'Use variable_name = number, then print the variable name.',
  breakdown: `1. Create the variable with ${name} = ${value}.\n2. Print ${name} without quotes.\n3. The output should be ${value}.`,
  expected: value,
  requiredNodePatterns: [node('Assign')],
  requiredCallPatterns: [printCall],
});

const addBinaryMath = (a, op, b, word) => {
  const expression = `${a} ${op} ${b}`;
  const expected = op === '+' ? a + b : op === '-' ? a - b : op === '*' ? a * b : a / b;
  add({
    description: `Write a Python program that ${word} ${a} and ${b}, then prints the result.`,
    solution: `# Script approach\nresult = ${expression}\nprint(result)`,
    hint: `Use the ${op} operator and print the result.`,
    breakdown: `1. Calculate ${expression}.\n2. Store the answer in result.\n3. Print result.`,
    expected,
    requiredNodePatterns: [node('Assign'), node('BinOp')],
    requiredCallPatterns: [printCall],
  });
};

const addStringBuiltin = (text, fn, expected, wording) => add({
  description: `Write a Python program that ${wording} for the string ${q(text)}, then prints the result.`,
  solution: `# Script approach\ntext = ${q(text)}\nresult = ${fn === 'len' ? 'len(text)' : `text.${fn}()`}\nprint(result)`,
  hint: fn === 'len' ? 'Use len(text).' : `Use the string method .${fn}().`,
  breakdown: `1. Store ${q(text)} in a variable.\n2. Use ${fn === 'len' ? 'len(text)' : `text.${fn}()`}.\n3. Print the result.`,
  expected,
  requiredNodePatterns: [node('Assign')],
  requiredCallPatterns: [{ functionName: fn, minArgs: fn === 'len' ? 1 : 0 }, printCall],
});

const addListPrint = (items) => add({
  description: `Create a list containing ${items.map(repr).join(', ')}. Then print the list.`,
  solution: `# Script approach\nitems = ${repr(items)}\nprint(items)`,
  hint: 'Use square brackets [] to make a list.',
  breakdown: `1. Put the items inside square brackets.\n2. Store the list in a variable.\n3. Print the list.`,
  expected: items,
  requiredNodePatterns: [node('Assign'), node('List')],
  requiredCallPatterns: [printCall],
});

const addListIndex = (items, index, label) => add({
  description: `Create the list ${repr(items)}. Then print the ${label} item.`,
  solution: `# Script approach\nitems = ${repr(items)}\nprint(items[${index}])`,
  hint: 'List indexes start at 0. The first item is index 0.',
  breakdown: `1. Create the list.\n2. Use items[${index}] to access the ${label} item.\n3. Print that item.`,
  expected: items.at(index),
  requiredNodePatterns: [node('Assign'), node('List'), node('Subscript')],
  requiredCallPatterns: [printCall],
});

const addListLength = (items) => add({
  description: `Create the list ${repr(items)}. Then print how many items are in the list.`,
  solution: `# Script approach\nitems = ${repr(items)}\nprint(len(items))`,
  hint: 'Use len(items) to count list items.',
  breakdown: '1. Create the list.\n2. Use len(items) to count it.\n3. Print the count.',
  expected: items.length,
  requiredNodePatterns: [node('Assign'), node('List')],
  requiredCallPatterns: [{ functionName: 'len', minArgs: 1 }, printCall],
});

const addComparison = (a, op, b, expected) => add({
  description: `Create a comparison that checks whether ${a} ${op} ${b}. Print the Boolean result.`,
  solution: `# Script approach\nresult = ${a} ${op} ${b}\nprint(result)`,
  hint: 'A comparison creates True or False.',
  breakdown: `1. Compare ${a} and ${b} with ${op}.\n2. Store the Boolean in result.\n3. Print result.`,
  expected,
  requiredNodePatterns: [node('Assign'), node('Compare')],
  requiredCallPatterns: [printCall],
});

const addSimpleIf = (name, value, op, check, output) => add({
  description: `Create a variable called \`${name}\` with the value ${repr(value)}. If \`${name}\` ${op} ${repr(check)}, print ${q(output)}.`,
  solution: `# Script approach\n${name} = ${repr(value)}\nif ${name} ${op} ${repr(check)}:\n    print(${q(output)})`,
  hint: 'Use if, a colon, and an indented print line.',
  breakdown: `1. Create ${name}.\n2. Write the if condition.\n3. Put print(${q(output)}) on the indented line below the if.`,
  expected: output,
  requiredNodePatterns: [node('Assign'), node('If')],
  requiredCallPatterns: [printCall],
});

const addConversion = (value, fn, expected) => add({
  description: `Convert ${repr(value)} using \`${fn}()\`, then print the result.`,
  solution: `# Script approach\nvalue = ${repr(value)}\nresult = ${fn}(value)\nprint(result)`,
  hint: `Use ${fn}(value) to convert the value.`,
  breakdown: `1. Store the starting value.\n2. Convert it with ${fn}().\n3. Print the converted result.`,
  expected,
  requiredNodePatterns: [node('Assign')],
  requiredCallPatterns: [{ functionName: fn, minArgs: 1 }, printCall],
});

const addFString = (name, age) => add({
  description: `Create \`name = ${q(name)}\` and \`age = ${age}\`. Print the sentence ${q(`${name} is ${age}`)} using an f-string.`,
  solution: `# Script approach\nname = ${q(name)}\nage = ${age}\nprint(f"{name} is {age}")`,
  hint: 'Use f"text {variable}" to place values inside text.',
  breakdown: '1. Create the two variables.\n2. Put f before the string.\n3. Use braces around variable names inside the string.',
  expected: `${name} is ${age}`,
  requiredNodePatterns: [node('Assign', 2), node('JoinedStr')],
  requiredCallPatterns: [printCall],
});

const addDictLookup = (data, key) => add({
  description: `Create the dictionary ${repr(data)}. Then print the value for the key ${q(key)}.`,
  solution: `# Script approach\ndata = ${repr(data)}\nprint(data[${q(key)}])`,
  hint: 'Use square brackets with the key: data["key"].',
  breakdown: `1. Create the dictionary with curly braces.\n2. Use data[${q(key)}] to get the value.\n3. Print that value.`,
  expected: data[key],
  requiredNodePatterns: [node('Assign'), node('Dict'), node('Subscript')],
  requiredCallPatterns: [printCall],
});

const addTupleIndex = (items, index, label) => add({
  description: `Create the tuple ${tupleRepr(items)}. Then print the ${label} item.`,
  solution: `# Script approach\nitems = ${tupleRepr(items)}\nprint(items[${index}])`,
  hint: 'Tuples use parentheses. Indexing works like lists.',
  breakdown: `1. Create the tuple.\n2. Use items[${index}] to access the ${label} item.\n3. Print that item.`,
  expected: items.at(index),
  requiredNodePatterns: [node('Assign'), node('Tuple'), node('Subscript')],
  requiredCallPatterns: [printCall],
});

const addModulo = (a, b) => add({
  description: `Write a Python program that prints the remainder of ${a} divided by ${b}.`,
  solution: `# Script approach\nresult = ${a} % ${b}\nprint(result)`,
  hint: 'Use the % operator to get a remainder.',
  breakdown: `1. Use ${a} % ${b}.\n2. Store the answer in result.\n3. Print result.`,
  expected: a % b,
  requiredNodePatterns: [node('Assign'), node('BinOp')],
  requiredCallPatterns: [printCall],
});

const addMembership = (value, container, expected) => add({
  description: `Check whether ${repr(value)} is inside ${repr(container)}. Print the Boolean result.`,
  solution: `# Script approach\nitems = ${repr(container)}\nresult = ${repr(value)} in items\nprint(result)`,
  hint: 'Use the in keyword to check membership.',
  breakdown: `1. Create the container.\n2. Use ${repr(value)} in items.\n3. Print the Boolean result.`,
  expected,
  requiredNodePatterns: [node('Assign'), node('Compare')],
  requiredCallPatterns: [printCall],
});

const printTexts = [
  'Hello', 'Python', 'Code', 'Ready', 'Start', 'Learn', 'Practice', 'Debug', 'Run', 'Output',
  'Input', 'Variable', 'String', 'Number', 'List', 'True', 'False', 'Good job', 'Keep going', 'Done'
];
printTexts.forEach((text) => addPrintLiteral(text, text));

[0, 1, 2, 3, 4, 5, 7, 9, 10, 12, 15, 20, 25, 30, 42].forEach(addPrintNumber);

[
  ['name', 'Noll'], ['city', 'Paris'], ['pet', 'cat'], ['food', 'rice'], ['color', 'blue'],
  ['language', 'Python'], ['word', 'hello'], ['day', 'Monday'], ['tool', 'keyboard'], ['fruit', 'apple'],
  ['animal', 'dog'], ['school', 'code'], ['planet', 'Mars'], ['drink', 'water'], ['shape', 'circle'],
].forEach(([name, value]) => addStringVariable(name, value));

[
  ['age', 10], ['score', 5], ['level', 1], ['year', 2026], ['count', 3],
  ['price', 8], ['height', 12], ['speed', 6], ['points', 15], ['size', 4],
  ['total', 20], ['number', 7], ['rank', 2], ['steps', 9], ['coins', 11],
].forEach(([name, value]) => addNumberVariable(name, value));

[[1, 2], [2, 3], [4, 5], [10, 5], [7, 8], [6, 9], [11, 4], [12, 13], [20, 1], [30, 12],
 [3, 14], [15, 15], [18, 2], [21, 6], [100, 25]].forEach(([a, b]) => addBinaryMath(a, '+', b, 'adds'));

[[5, 2], [9, 4], [10, 3], [20, 5], [30, 10], [12, 7], [15, 6], [40, 8], [18, 9], [100, 1],
 [50, 25], [14, 11], [22, 2], [8, 3], [70, 30]].forEach(([a, b]) => addBinaryMath(a, '-', b, 'subtracts'));

[[2, 3], [4, 5], [6, 2], [7, 3], [8, 4], [9, 5], [10, 10], [3, 11], [12, 2], [5, 5],
 [13, 2], [15, 3], [20, 4], [25, 2], [30, 3]].forEach(([a, b]) => addBinaryMath(a, '*', b, 'multiplies'));

[[10, 2], [12, 3], [20, 4], [30, 5], [42, 6], [18, 2], [100, 10], [9, 3], [16, 4], [25, 5],
 [36, 6], [49, 7], [64, 8], [81, 9], [8, 2]].forEach(([a, b]) => addBinaryMath(a, '/', b, 'divides'));

[
  ['cat', 'len', 3, 'prints the length'], ['dog', 'len', 3, 'prints the length'], ['Python', 'len', 6, 'prints the length'],
  ['hello', 'upper', 'HELLO', 'changes it to uppercase'], ['code', 'upper', 'CODE', 'changes it to uppercase'],
  ['WORLD', 'lower', 'world', 'changes it to lowercase'], ['APPLE', 'lower', 'apple', 'changes it to lowercase'],
  ['python', 'capitalize', 'Python', 'capitalizes it'], ['banana', 'capitalize', 'Banana', 'capitalizes it'],
  ['  hi  ', 'strip', 'hi', 'removes spaces from both ends'], ['  cat', 'strip', 'cat', 'removes spaces from both ends'],
  ['blue car', 'title', 'Blue Car', 'title-cases it'], ['red ball', 'title', 'Red Ball', 'title-cases it'],
  ['hello', 'replace', 'heLLo', 'replaces lowercase l with uppercase L'],
  ['mississippi', 'count', 4, 'counts the letter s'],
].forEach(([text, fn, expected, wording]) => {
  if (fn === 'replace') {
    add({
      description: `Store the string ${q(text)}. Replace every "l" with "L", then print the result.`,
      solution: `# Script approach\ntext = ${q(text)}\nresult = text.replace("l", "L")\nprint(result)`,
      hint: 'Use text.replace("l", "L").',
      breakdown: '1. Store the string.\n2. Use replace() with old text and new text.\n3. Print the result.',
      expected,
      requiredNodePatterns: [node('Assign')],
      requiredCallPatterns: [{ functionName: 'replace', minArgs: 2 }, printCall],
    });
  } else if (fn === 'count') {
    add({
      description: `Store the string ${q(text)}. Count how many times "s" appears, then print the count.`,
      solution: `# Script approach\ntext = ${q(text)}\nresult = text.count("s")\nprint(result)`,
      hint: 'Use text.count("s").',
      breakdown: '1. Store the string.\n2. Use count() to count "s".\n3. Print the result.',
      expected,
      requiredNodePatterns: [node('Assign')],
      requiredCallPatterns: [{ functionName: 'count', minArgs: 1 }, printCall],
    });
  } else {
    addStringBuiltin(text, fn, expected, wording);
  }
});

[
  [1, 2, 3], [4, 5, 6], ['a', 'b', 'c'], ['red', 'blue'], [10, 20], ['cat', 'dog'],
  [0, 1], ['yes', 'no'], [7, 8, 9], ['x', 'y', 'z'], [100, 200], ['sun', 'moon'],
  [3, 1, 4], ['pen', 'book'], [5, 10, 15],
].forEach(addListPrint);

[
  [['apple', 'banana', 'cherry'], 0, 'first'], [['red', 'blue', 'green'], 0, 'first'], [[10, 20, 30], 0, 'first'],
  [['cat', 'dog', 'bird'], 1, 'second'], [['small', 'medium', 'large'], 1, 'second'], [[5, 6, 7], 1, 'second'],
  [['north', 'south', 'east'], 2, 'third'], [['a', 'b', 'c'], 2, 'third'], [[100, 200, 300], 2, 'third'],
  [['one', 'two', 'three'], -1, 'last'], [['morning', 'noon', 'night'], -1, 'last'], [[2, 4, 6], -1, 'last'],
  [['zero', 'one'], 0, 'first'], [['left', 'right'], -1, 'last'], [[9, 8], -1, 'last'],
].forEach(([items, index, label]) => addListIndex(items, index, label));

[
  [1, 2, 3], ['a', 'b'], ['cat', 'dog', 'bird', 'fish'], [10], [], ['red', 'blue', 'green'],
  [5, 6], ['one'], [0, 1, 2, 3], ['x', 'y', 'z', 'w'], [100, 200, 300], ['sun', 'moon'],
  [7, 8, 9, 10, 11], ['pen', 'book', 'bag'], [42],
].forEach(addListLength);

[
  [5, '>', 3, true], [2, '<', 1, false], [10, '==', 10, true], [7, '!=', 8, true], [4, '>=', 5, false],
  [6, '<=', 6, true], [9, '>', 12, false], [1, '<', 4, true], [3, '==', 4, false], [8, '!=', 8, false],
  [15, '>=', 10, true], [11, '<=', 2, false], [0, '==', 0, true], [20, '>', 19, true], [30, '<', 10, false],
].forEach(([a, op, b, expected]) => addComparison(a, op, b, expected));

[
  ['age', 18, '>=', 18, 'adult'], ['score', 90, '>=', 50, 'pass'], ['temperature', 30, '>', 25, 'hot'],
  ['count', 0, '==', 0, 'empty'], ['name', 'Noll', '==', 'Noll', 'match'], ['speed', 5, '<', 10, 'slow'],
  ['coins', 3, '!=', 0, 'has coins'], ['level', 1, '<=', 1, 'start'], ['points', 100, '>=', 100, 'max'],
  ['word', 'cat', '!=', 'dog', 'different'], ['size', 4, '>', 2, 'big'], ['tries', 1, '<', 3, 'try again'],
  ['light', 'green', '==', 'green', 'go'], ['number', 12, '>=', 10, 'two digits'], ['answer', 'yes', '==', 'yes', 'confirmed'],
].forEach(([name, value, op, check, output]) => addSimpleIf(name, value, op, check, output));

[
  ['5', 'int', 5], ['12', 'int', 12], ['0', 'int', 0], [7, 'str', '7'], [42, 'str', '42'],
  [3.5, 'str', '3.5'], ['2.5', 'float', 2.5], ['10', 'float', 10.0], [1, 'bool', true], [0, 'bool', false],
  ['', 'bool', false], ['hello', 'bool', true], [[1, 2], 'tuple', [1, 2]], ['abc', 'list', ['a', 'b', 'c']], [['a', 'b'], 'tuple', ['a', 'b']],
].forEach(([value, fn, expected]) => addConversion(value, fn, expected));

[
  ['Noll', 10], ['Ada', 12], ['Bo', 8], ['Mia', 7], ['Leo', 9], ['Zoe', 11], ['Kai', 6], ['Ivy', 13],
  ['Omar', 14], ['Lina', 15], ['Noah', 16], ['Emma', 5], ['Ava', 17], ['Eli', 18], ['Sara', 19],
].forEach(([name, age]) => addFString(name, age));

[
  [{ name: 'Noll', age: 10 }, 'name'], [{ name: 'Ada', age: 12 }, 'age'], [{ color: 'blue', size: 4 }, 'color'],
  [{ pet: 'cat', sound: 'meow' }, 'sound'], [{ fruit: 'apple', count: 3 }, 'count'], [{ city: 'Paris', country: 'France' }, 'city'],
  [{ day: 'Monday', number: 1 }, 'number'], [{ language: 'Python', level: 'beginner' }, 'language'],
  [{ book: 'code', pages: 20 }, 'pages'], [{ team: 'red', score: 5 }, 'score'], [{ x: 1, y: 2 }, 'x'],
  [{ first: 'A', second: 'B' }, 'second'], [{ hot: true, cold: false }, 'hot'], [{ open: 'yes', closed: 'no' }, 'closed'],
  [{ start: 0, end: 10 }, 'end'],
].forEach(([data, key]) => addDictLookup(data, key));

[
  [['red', 'green', 'blue'], 0, 'first'], [['red', 'green', 'blue'], 1, 'second'], [['red', 'green', 'blue'], 2, 'third'],
  [[1, 2, 3], 0, 'first'], [[1, 2, 3], 1, 'second'], [[1, 2, 3], -1, 'last'],
  [['cat', 'dog'], 0, 'first'], [['cat', 'dog'], -1, 'last'], [['yes', 'no', 'maybe'], -1, 'last'],
  [[10, 20, 30], -1, 'last'], [['north', 'south'], 1, 'second'], [['left', 'middle', 'right'], 1, 'second'],
  [['small', 'large'], 0, 'first'], [['day', 'night'], -1, 'last'], [[5, 10], 1, 'second'],
].forEach(([items, index, label]) => addTupleIndex(items, index, label));

[[5, 2], [7, 3], [10, 4], [12, 5], [15, 6], [20, 7], [21, 10], [30, 8], [42, 5], [99, 10],
 [100, 9], [17, 4], [25, 6], [64, 10], [81, 7]].forEach(([a, b]) => addModulo(a, b));

[
  ['a', ['a', 'b', 'c'], true], ['z', ['a', 'b', 'c'], false], [2, [1, 2, 3], true], [5, [1, 2, 3], false],
  ['cat', ['cat', 'dog'], true], ['bird', ['cat', 'dog'], false], ['red', ['red', 'blue'], true],
  ['green', ['red', 'blue'], false], ['p', 'python', true], ['z', 'python', false],
].forEach(([value, container, expected]) => addMembership(value, container, expected));

if (exercises.length !== 300) {
  throw new Error(`Expected 300 atomic beginner exercises, generated ${exercises.length}`);
}

const translateAtomicDescription = (description) => {
  let match = description.match(/^Write a Python program that prints the text "(.+)"\.$/);
  if (match) return `Écrivez un programme Python qui affiche le texte "${match[1]}".`;

  match = description.match(/^Write a Python program that prints the number (.+)\.$/);
  if (match) return `Écrivez un programme Python qui affiche le nombre ${match[1]}.`;

  match = description.match(/^Create a variable called `([^`]+)` and store the string "(.+)" in it\. Then print the variable\.$/);
  if (match) return `Créez une variable appelée \`${match[1]}\` et stockez-y la chaîne "${match[2]}". Ensuite, affichez la variable.`;

  match = description.match(/^Create a variable called `([^`]+)` and store the number (.+) in it\. Then print the variable\.$/);
  if (match) return `Créez une variable appelée \`${match[1]}\` et stockez-y le nombre ${match[2]}. Ensuite, affichez la variable.`;

  match = description.match(/^Write a Python program that (adds|subtracts|multiplies|divides) (.+) and (.+), then prints the result\.$/);
  if (match) {
    const verbs = { adds: 'additionne', subtracts: 'soustrait', multiplies: 'multiplie', divides: 'divise' };
    return `Écrivez un programme Python qui ${verbs[match[1]]} ${match[2]} et ${match[3]}, puis affiche le résultat.`;
  }

  match = description.match(/^Write a Python program that prints the length for the string "(.+)", then prints the result\.$/);
  if (match) return `Écrivez un programme Python qui affiche la longueur de la chaîne "${match[1]}", puis affiche le résultat.`;

  match = description.match(/^Write a Python program that changes it to uppercase for the string "(.+)", then prints the result\.$/);
  if (match) return `Écrivez un programme Python qui transforme la chaîne "${match[1]}" en majuscules, puis affiche le résultat.`;

  match = description.match(/^Write a Python program that changes it to lowercase for the string "(.+)", then prints the result\.$/);
  if (match) return `Écrivez un programme Python qui transforme la chaîne "${match[1]}" en minuscules, puis affiche le résultat.`;

  match = description.match(/^Write a Python program that capitalizes it for the string "(.+)", then prints the result\.$/);
  if (match) return `Écrivez un programme Python qui met la première lettre de la chaîne "${match[1]}" en majuscule, puis affiche le résultat.`;

  match = description.match(/^Write a Python program that removes spaces from both ends for the string "([\s\S]+)", then prints the result\.$/);
  if (match) return `Écrivez un programme Python qui supprime les espaces au début et à la fin de la chaîne "${match[1]}", puis affiche le résultat.`;

  match = description.match(/^Write a Python program that title-cases it for the string "(.+)", then prints the result\.$/);
  if (match) return `Écrivez un programme Python qui met chaque mot de la chaîne "${match[1]}" en forme titre, puis affiche le résultat.`;

  match = description.match(/^Store the string "(.+)"\. Replace every "l" with "L", then print the result\.$/);
  if (match) return `Stockez la chaîne "${match[1]}". Remplacez chaque "l" par "L", puis affichez le résultat.`;

  match = description.match(/^Store the string "(.+)"\. Count how many times "s" appears, then print the count\.$/);
  if (match) return `Stockez la chaîne "${match[1]}". Comptez combien de fois "s" apparaît, puis affichez le nombre.`;

  match = description.match(/^Create a list containing (.+)\. Then print the list\.$/);
  if (match) return `Créez une liste contenant ${match[1]}. Ensuite, affichez la liste.`;

  match = description.match(/^Create the list (.+)\. Then print the (first|second|third|last) item\.$/);
  if (match) {
    const labels = { first: 'premier', second: 'deuxième', third: 'troisième', last: 'dernier' };
    return `Créez la liste ${match[1]}. Ensuite, affichez le ${labels[match[2]]} élément.`;
  }

  match = description.match(/^Create the list (.+)\. Then print how many items are in the list\.$/);
  if (match) return `Créez la liste ${match[1]}. Ensuite, affichez combien d’éléments elle contient.`;

  match = description.match(/^Create a comparison that checks whether (.+) (>|<|==|!=|>=|<=) (.+)\. Print the Boolean result\.$/);
  if (match) return `Créez une comparaison qui vérifie si ${match[1]} ${match[2]} ${match[3]}. Affichez le résultat booléen.`;

  match = description.match(/^Create a variable called `([^`]+)` with the value (.+)\. If `([^`]+)` (>|<|==|!=|>=|<=) (.+), print "(.+)"\.$/);
  if (match) return `Créez une variable appelée \`${match[1]}\` avec la valeur ${match[2]}. Si \`${match[3]}\` ${match[4]} ${match[5]}, affichez "${match[6]}".`;

  match = description.match(/^Convert (.+) using `([^`]+)\(\)`, then print the result\.$/);
  if (match) return `Convertissez ${match[1]} avec \`${match[2]}()\`, puis affichez le résultat.`;

  match = description.match(/^Create `name = "(.+)"` and `age = (.+)`\. Print the sentence "(.+)" using an f-string\.$/);
  if (match) return `Créez \`name = "${match[1]}"\` et \`age = ${match[2]}\`. Affichez la phrase "${match[3]}" avec une f-string.`;

  match = description.match(/^Create the dictionary (.+)\. Then print the value for the key "(.+)"\.$/);
  if (match) return `Créez le dictionnaire ${match[1]}. Ensuite, affichez la valeur de la clé "${match[2]}".`;

  match = description.match(/^Create the tuple (.+)\. Then print the (first|second|third|last) item\.$/);
  if (match) {
    const labels = { first: 'premier', second: 'deuxième', third: 'troisième', last: 'dernier' };
    return `Créez le tuple ${match[1]}. Ensuite, affichez le ${labels[match[2]]} élément.`;
  }

  match = description.match(/^Write a Python program that prints the remainder of (.+) divided by (.+)\.$/);
  if (match) return `Écrivez un programme Python qui affiche le reste de ${match[1]} divisé par ${match[2]}.`;

  match = description.match(/^Check whether (.+) is inside (.+)\. Print the Boolean result\.$/);
  if (match) return `Vérifiez si ${match[1]} se trouve dans ${match[2]}. Affichez le résultat booléen.`;

  return description;
};

const frenchDescriptions = Object.fromEntries(
  exercises.map((exercise) => [exercise.id, translateAtomicDescription(exercise.description)])
);

const exerciseFile = `import type { Exercise } from './types';\n\nexport const ATOMIC_BEGINNER_EXERCISES: Exercise[] = ${JSON.stringify(exercises, null, 2)};\n`;

const graderFile = `import type { AutoGrader } from './graders';\n\nexport const ATOMIC_BEGINNER_GRADERS: Record<number, AutoGrader> = ${JSON.stringify(graders, null, 2)};\n`;

const frenchFile = `// Auto-generated French descriptions for atomic beginner exercises.\n// Do not edit manually; run scripts/generate_atomic_beginner.mjs.\n\nexport const ATOMIC_BEGINNER_EXERCISES_FR: Record<number, string> = ${JSON.stringify(frenchDescriptions, null, 2)};\n`;

fs.writeFileSync('atomicBeginnerExercises.ts', exerciseFile);
fs.writeFileSync('atomicBeginnerGraders.ts', graderFile);
fs.writeFileSync('atomicBeginnerExercisesFr.ts', frenchFile);
console.log(`Generated ${exercises.length} atomic beginner exercises (${startId}-${startId + exercises.length - 1}).`);
