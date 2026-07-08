const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const writeMode = process.argv.includes('--write');
const forceExamples = process.argv.includes('--force-examples');

function loadTsExports(fileName) {
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020, esModuleInterop: true },
    fileName,
  }).outputText;
  const sandbox = {
    exports: {},
    module: { exports: {} },
    require: (specifier) => {
      if (specifier === './atomicBeginnerExercises') return loadTsExports('atomicBeginnerExercises.ts');
      if (specifier === './atomicBeginnerGraders') return loadTsExports('atomicBeginnerGraders.ts');
      return {};
    },
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

/* ── helpers for formatting JSON-safe values ── */

function jsonEscape(str) {
  return str
    .replace(/\\/g, '\\\\')
    .replace(/"/g, '\\"')
    .replace(/\n/g, '\\n')
    .replace(/\r/g, '\\r')
    .replace(/\t/g, '\\t');
}

/* ── helpers for generating examples from test data ── */

function formatArg(arg) {
  if (typeof arg === 'string') return `'${arg}'`;
  if (Array.isArray(arg)) return `[${arg.map(formatArg).join(', ')}]`;
  if (arg === null) return 'None';
  if (arg === true) return 'True';
  if (arg === false) return 'False';
  if (typeof arg === 'object') return JSON.stringify(arg).replace(/"/g, "'");
  return String(arg);
}

function formatExpected(val) {
  if (typeof val === 'string') return `'${val}'`;
  if (Array.isArray(val)) return `[${val.map(formatExpected).join(', ')}]`;
  if (val === null) return 'None';
  if (val === true) return 'True';
  if (val === false) return 'False';
  if (typeof val === 'object') return JSON.stringify(val).replace(/"/g, "'");
  return String(val);
}

function generateExamples(functionName, testCases) {
  const cases = Array.isArray(testCases) ? testCases.slice(0, 3) : [];
  if (!cases.length) return [];
  return cases.map(tc => {
    if (Array.isArray(tc.inputValues) && tc.inputValues.length > 0) {
      const inputs = tc.inputValues.map(formatExpected).join(', ');
      const arrow = tc.expected !== undefined ? `\u2192 ${formatExpected(tc.expected)}` : '\u2192 shown output';
      return `  input ${inputs} ${arrow}`;
    }
    const args = Array.isArray(tc.args) ? tc.args.map(formatArg).join(', ') : '';
    const arrow = tc.expected !== undefined ? `\u2192 ${formatExpected(tc.expected)}` : '\u2192 ?';
    const name = tc.functionName || functionName;
    return `  ${name}(${args}) ${arrow}`;
  });
}

function examplesNeedFix(description) {
  const lines = description.split('\n');
  const exampleLines = lines.filter(l => /\u2192/.test(l) || /->/.test(l));
  if (exampleLines.length === 0) return true;
  const lowerDescription = description.toLowerCase();
  const expectsNumericData = /\b(integer|integers|number|numbers|numeric|float|floats)\b/.test(lowerDescription);
  const expectsListData = /\blist\b/.test(lowerDescription);
  const genericWordLiteral = /^['"]?(hello|world|python|test|example|sample)['"]?$/i;
  for (const line of exampleLines) {
    if (/(?:\u2192|->)\s*\?/.test(line)) return true;
    const match = line.match(/\(([^)]+)\)/);
    if (!match) continue;
    const args = match[1].split(',').map(a => a.trim());
    // All args identical (get_substring('hello','hello','hello'))
    const uniqueArgs = new Set(args);
    if (uniqueArgs.size === 1 && args.length > 1) return true;
    // Single number where a list/collection is expected
    if (args.length === 1 && /^\d+$/.test(args[0])) return true;
    if (args.some(arg => genericWordLiteral.test(arg))) return true;
    if (expectsNumericData && args.some(arg => /^['"][A-Za-z_]+['"]$/.test(arg))) return true;
    if (expectsListData && args.length === 1 && /^['"][^'"]*['"]$/.test(args[0])) return true;
    // Function name mismatch
    const fnMatch = line.match(/^  (\w+)\(/);
    if (fnMatch) {
      const descMatch = description.match(/function called `(\w+)`/);
      if (descMatch && fnMatch[1] !== descMatch[1]) return true;
    }
    // Likely mismatched args (a string where int expected based on param names)
    const firstParamMatch = description.match(/takes a string.*?(\w+) and returns/);
    if (firstParamMatch) {
      // Description suggests ordered params but example re-uses same literal for all
      const hasLiteralsMatch = args.every(a => a.startsWith("'") && a.endsWith("'"));
      if (hasLiteralsMatch && args.length >= 3) return true;
    }
  }
  return false;
}

/* Locate a JSON string value by field name, returning offsets. */
function findFieldValue(source, searchFrom, fieldName) {
  const fieldRegex = new RegExp(`"${fieldName}":\\s*"`, 'g');
  fieldRegex.lastIndex = searchFrom;
  const match = fieldRegex.exec(source);
  if (!match) return null;

  const valStart = match.index + match[0].length;
  let i = valStart;
  while (i < source.length) {
    if (source[i] === '\\') { i += 2; continue; }
    if (source[i] === '"') break;
    i++;
  }
  if (i >= source.length) return null;
  return {
    start: match.index,
    valueStart: valStart,
    valueEnd: i,
  };
}

/* Replace a JSON string field's value, properly escaping. */
function replaceFieldValue(source, fieldInfo, newValue) {
  const escaped = jsonEscape(newValue);
  const before = source.slice(0, fieldInfo.valueStart);
  const after = source.slice(fieldInfo.valueEnd);
  return before + escaped + after;
}

/* ── content generation ── */

function generateBreakdown(functionName, params, description) {
  const desc = description.toLowerCase();
  const steps = [];

  const paramList = params.map(p => `\`${p}\``).join(', ');
  steps.push(`Define \`${functionName}(${params.join(', ')})\` with parameters ${paramList}.`);

  if (/substring|slice.*(?:from|extract)/.test(desc)) {
    steps.push(`Use slicing: \`text[start:end]\` extracts characters from index \`start\` up to (not including) \`end\`.`);
  } else if (/\bmap\(\)/.test(desc) && /string.*number|string.*integer|integers/.test(desc) && /list/.test(desc)) {
    steps.push(`Use \`map(int, strings)\` to convert each numeric string into an integer without writing a manual loop.`);
    steps.push(`Wrap the map object with \`list(...)\` so the function returns a real list of integers.`);
  } else if (/\bmap\(\)/.test(desc) && /square/.test(desc) && /list/.test(desc)) {
    steps.push(`Use \`map()\` with a helper or lambda that returns \`x ** 2\` for each number.`);
    steps.push(`Wrap the map object with \`list(...)\` so the result is a list of squared numbers.`);
  } else if (/\bmap\(\)/.test(desc) && /length/.test(desc) && /string/.test(desc)) {
    steps.push(`Use \`map(len, strings)\` to apply \`len()\` to every string in the list.`);
    steps.push(`Wrap the map object with \`list(...)\` so the result is a list of lengths.`);
  } else if (/replace.*char|substitute/.test(desc)) {
    steps.push(`Call \`text.replace(old\\_char, new\\_char)\` — returns a new string with all occurrences replaced.`);
  } else if (/remove.*char|delete.*char/.test(desc)) {
    steps.push(`Call \`text.replace(char, '')\` — replaces target char with empty string, effectively removing it.`);
  } else if (/reverse/.test(desc)) {
    steps.push(`Use slicing \`[::-1]\` to reverse the sequence.`);
  } else if (/len(?:gth)?/.test(desc)) {
    steps.push(`Call \`len()\` on the input to get the number of elements.`);
  } else if (/\b(?:check|test|return).*(?:if|whether).*(?:is in|in the list|contain|present|exist|member)\b/.test(desc)) {
    steps.push(`Use \`element in my\\_list\` to test membership — returns \`True\` or \`False\`.`);
  } else if (/\bindex\b.*\b(?:first|occurrence|position)\b/.test(desc)) {
    steps.push(`Check \`if element in my\\_list\` first to avoid \`ValueError\`, then use \`.index(element)\` to find the position.`);
    steps.push(`If not found, return \`-1\`.`);
  } else if (/\bhow many\b[\s\S]*?\b(?:time|appear)\w*\b|\bfrequency\b|\bhow many\b[\s\S]*?\boccurrence\b/.test(desc)) {
    steps.push(`Call \`.count(element)\` on the list to count occurrences directly.`);
  } else if (/even|odd/.test(desc)) {
    const even = /even/.test(desc);
    const condition = even ? 'x % 2 == 0' : 'x % 2 != 0';
    steps.push(`Use a list comprehension: \`[x for x in numbers if ${condition}]\` to filter ${even ? 'even' : 'odd'} numbers.`);
  } else if (/sum|add|total/.test(desc) && !/\btwo\b/.test(desc)) {
    steps.push(`Use \`sum()\` on the input list to add all values together.`);
  } else if (/multiply|product/.test(desc) && !/\btwo\b/.test(desc)) {
    steps.push(`Iterate through the list and multiply values together, starting with \`1\`.`);
  } else if (/max|largest|biggest/.test(desc)) {
    steps.push(`Call \`max()\` on the input to find the largest value.`);
  } else if (/min|smallest/.test(desc)) {
    steps.push(`Call \`min()\` on the input to find the smallest value.`);
  } else if (/capitalize/.test(desc)) {
    steps.push(`Use \`.capitalize()\` to make the first letter uppercase and the rest lowercase.`);
  } else if (/upper/.test(desc)) {
    steps.push(`Use \`.upper()\` to convert all characters to uppercase.`);
  } else if (/lower/.test(desc)) {
    steps.push(`Use \`.lower()\` to convert all characters to lowercase.`);
  } else if (/square|pow|power|exponent/.test(desc)) {
    steps.push(`Use \`**\` operator or \`pow()\` to perform exponentiation.`);
  } else if (/palindrome/.test(desc)) {
    steps.push(`Compare the input to its reverse: \`text == text[::-1]\`.`);
  } else if (/prime/.test(desc)) {
    steps.push(`Check divisors from \`2\` to \`sqrt(n)\` — if none divide evenly, it is prime.`);
  } else if (/sort|sorted/.test(desc)) {
    steps.push(`Call \`sorted()\` on the input to get a new sorted list.`);
  } else if (/set|union|intersection|difference/.test(desc)) {
    steps.push(`Convert lists to sets with \`set()\`, perform operations, convert back if needed.`);
  } else if (/\b(?:count|number of)\s+vowel|vowel\s+count/.test(desc)) {
    steps.push(`Iterate through each character and check if it is a vowel (\`aeiou\`) using \`in\` operator.`);
    steps.push(`Use a counter variable or \`sum()\` with a generator expression.`);
  } else if (/\b(?:count|number of)\s+word|word\s+count/.test(desc)) {
    steps.push(`Use \`.split()\` to break the string into words, then call \`len()\` on the resulting list.`);
  } else if (/\b(?:count|occurrence|frequency|appear)\b/.test(desc)) {
    steps.push(`Use \`.count()\` on the sequence to count how many times each element appears.`);
    steps.push(`Or use a \`collections.Counter\` object to count all elements at once.`);
  } else if (/double|twice|each.*\b(?:2|two)\b/.test(desc)) {
    steps.push(`Use a list comprehension: \`[x * 2 for x in input_list]\` to double each element.`);
  } else if (/square\s+root|sqrt/.test(desc)) {
    steps.push(`Use \`math.sqrt()\` to compute the square root of a number.`);
  } else if (/random|randint|choice|shuffle/.test(desc)) {
    steps.push(`Import \`random\` and use \`random.randint()\`, \`random.choice()\`, or \`random.shuffle()\` as needed.`);
  } else if (/\barea\b|perimeter|circumference/.test(desc)) {
    steps.push(`Apply the appropriate geometric formula using the input dimensions.`);
  } else if (/dictionary|dict/.test(desc)) {
    steps.push(`Iterate with \`.items()\` to access both keys and values when building the result.`);
  } else if (/class\s/.test(desc) || /inherit/.test(desc)) {
    steps.push(`Define a parent class with base behavior, then create child classes that extend or override methods.`);
  } else if (/generator|yield/.test(desc)) {
    steps.push(`Use \`yield\` instead of \`return\` to produce values lazily one at a time as the generator is iterated.`);
  } else if (/kwargs|keyword.*arg/.test(desc)) {
    steps.push(`Access the keyword arguments dictionary with \`.items()\` and iterate to process each key-value pair.`);
  } else if (/args|positional.*arg|unpack/.test(desc)) {
    steps.push(`Use \`*args\` to accept variable positional arguments as a tuple, then iterate over them.`);
  } else if (/file.*(?:read|write|open|creat|exist)/.test(desc)) {
    steps.push(`Use \`open()\` with the appropriate mode (\`'r'\` for read, \`'w'\` for write) inside a \`with\` statement for automatic closing.`);
  } else if (/thread|parallel|concurrent/.test(desc)) {
    steps.push(`Import the \`threading\` module, create \`Thread\` objects, start them, and join to wait for completion.`);
  } else if (/except|error|raise|try/.test(desc)) {
    steps.push(`Wrap the risky operation in a \`try\` block and catch specific exceptions with \`except\` handlers.`);
  } else if (/regex|regular expression|re\./.test(desc)) {
    steps.push(`Use \`re.match()\` or \`re.search()\` with a pattern to test or extract portions of the input.`);
  } else {
    steps.push(`Perform the required operation on the input parameter(s) as described in the prompt.`);
  }

  steps.push(`Return the result using \`return\`.`);
  return steps;
}

function generateHint(functionName, params, description) {
  const desc = description.toLowerCase();
  const hints = [];

  if (/substring|slice/.test(desc) && /string|text/.test(desc)) {
    hints.push('Slicing with `text[start:end]` does NOT include the character at index `end`.');
    hints.push('Python slicing is forgiving: if `end` exceeds the string length, no error occurs.');
  } else if (/\bmap\(\)/.test(desc) && /string.*number|string.*integer|integers/.test(desc) && /list/.test(desc)) {
    hints.push('Use `list(map(int, strings))` — `map()` applies `int` to each item, and `list()` materializes the result.');
  } else if (/\bmap\(\)/.test(desc) && /square/.test(desc) && /list/.test(desc)) {
    hints.push('With `map()`, pass a function such as `lambda x: x ** 2`, then convert the result with `list()`.');
  } else if (/\bmap\(\)/.test(desc) && /length/.test(desc) && /string/.test(desc)) {
    hints.push('Use `list(map(len, strings))` to get one length for each string.');
  } else if (/replace.*char(?:acter)?/.test(desc)) {
    hints.push('`.replace()` returns a NEW string — it does NOT modify the original.');
    hints.push('Only exact character matches are replaced; case matters.');
  } else if (/remove.*char(?:acter)?/.test(desc)) {
    hints.push('`str.replace(old, empty_string)` removes ALL occurrences of `old`, not just the first one.');
  } else if (/reverse/.test(desc)) {
    hints.push('`[::-1]` works on both strings and lists for reversal.');
    if (/list/.test(desc) && !/string/.test(desc)) hints.push('`.reverse()` modifies the list in-place and returns `None` — prefer slicing.');
    if (/string/.test(desc)) hints.push('Strings have no `.reverse()` method — use `[::-1]`.');
  } else if (/len(?:gth)?/.test(desc)) {
    hints.push('`len()` works on any iterable — no loop needed.');
  } else if (/\b(?:check|test|return).*(?:if|whether).*(?:is in|in the list|contain|present|exist|member)\b/.test(desc)) {
    hints.push('The `in` operator already returns a boolean — return it directly, no `if` wrapping needed.');
  } else if (/\bhow many\b[\s\S]*?\b(?:time|appear)\w*\b|\bfrequency\b|\bhow many\b[\s\S]*?\boccurrence\b/.test(desc)) {
    hints.push('`.count(element)` returns 0 if the element never appears — no need for a manual check.');
  } else if (/\bindex\b.*\b(?:first|occurrence|position)\b/.test(desc)) {
    hints.push('`my_list.index(element)` raises `ValueError` if not found — guard with `in` first when -1 is required.');
  } else if (/(?:even|odd)\s+number/.test(desc) || /filter (?:even|odd)/.test(desc) || /only the (?:even|odd)/.test(desc)) {
    hints.push('Use `x % 2 == 0` to check if a number is even; `x % 2 != 0` for odd.');
  } else if (/palindrome/.test(desc)) {
    hints.push('`text == text[::-1]` is the simplest palindrome check.');
  } else if (/anagram/.test(desc)) {
    hints.push('`sorted(s1) == sorted(s2)` is the simplest anagram check.');
  } else if (/sort(?:ed)?/.test(desc)) {
    hints.push('`.sort()` sorts in-place (returns `None`); `sorted()` returns a new list.');
  } else if (/prime/.test(desc)) {
    hints.push('Numbers less than 2 are not prime. Only check divisors up to `sqrt(n)`.');
  } else if (/factorial/.test(desc)) {
    hints.push('`n! = n * (n-1) * (n-2) * ... * 1` — use a loop or `math.factorial()`.');
  } else if (/capitalize/.test(desc)) {
    hints.push('`.capitalize()` makes the first letter uppercase and the rest lowercase.');
  } else if (/upper(?:case)?/.test(desc)) {
    hints.push('`.upper()` converts all characters to uppercase.');
  } else if (/lower(?:case)?/.test(desc)) {
    hints.push('`.lower()` converts all characters to lowercase.');
  } else if (/inherit|class\s/.test(desc)) {
    hints.push('A child class inherits all methods from its parent — only override what needs different behavior.');
    hints.push('Use `super().__init__()` in the child to call the parent constructor.');
  } else if (/generator|yield/.test(desc)) {
    hints.push('Generators use `yield` to produce values and `next()` or a `for` loop to consume them.');
    hints.push('A generator function returns a generator object (lazy iterator), not the values themselves.');
  } else if (/kwargs/.test(desc)) {
    hints.push('`**kwargs` collects extra keyword arguments into a dictionary inside the function.');
    hints.push('Use `kwargs.items()` to iterate over the collected key-value pairs.');
  } else if (/args/.test(desc)) {
    hints.push('`*args` collects extra positional arguments into a tuple.');
  } else if (/random/.test(desc)) {
    hints.push('`random.randint(a, b)` returns a random integer between a and b inclusive.');
    hints.push('`random.choice(seq)` picks a random element from a sequence.');
  } else if (/sqrt|square\s+root/.test(desc)) {
    hints.push('`math.sqrt(x)` returns the square root as a float.');
    hints.push('For integer square roots, use `int(math.sqrt(x))`.');
  } else if (/vowel/.test(desc)) {
    hints.push('Check if each character is in the set `"aeiouAEIOU"` using the `in` operator.');
  } else if (/double/.test(desc) && !/double.*sort|double.*list/.test(desc)) {
    hints.push('A list comprehension `[x * 2 for x in lst]` doubles each element cleanly.');
  } else if (/file/.test(desc)) {
    hints.push('Always use `with open(...) as f:` to ensure files are properly closed after reading/writing.');
  } else {
    hints.push('Carefully identify what the problem asks for: input type, output type, and the operation.');
  }

  if (params.length >= 3) {
    hints.push('Parameter ORDER matters — match exactly to the function signature.');
  }
  if (desc.includes('return')) {
    hints.push('Use `return` to send the result back — `print()` alone will not satisfy a function problem.');
  }
  if (desc.includes('print') && !desc.includes('return')) {
    hints.push('Use `print()` to display the output as shown in the examples.');
  }

  return hints.slice(0, 6);
}

/* ── main ── */

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');

let source = fs.readFileSync(path.join(root, 'exercises.ts'), 'utf8');

let fixCount = 0;
let exampleFixCount = 0;
let breakdownFixCount = 0;
let hintFixCount = 0;

for (const ex of EXERCISES) {
  const grader = AUTO_GRADERS[ex.id];
  const allCode = ex.initialCode || '';
  // Search all lines for function/class definitions
  const fnMatch = allCode.match(/def\s+(\w+)\s*\(([^)]*)\)/);
  const classMatch = !fnMatch ? allCode.match(/class\s+(\w+)/) : null;
  // Script mode: no func/class definition anywhere in initialCode
  const isScriptMode = !fnMatch && !classMatch && allCode.trim().length > 0;
  
  if (!fnMatch && !classMatch && !isScriptMode) continue;

  const graderFunctionNames = Array.isArray(grader?.functionNames) ? grader.functionNames : [];
  const preferredGraderFunction = graderFunctionNames.find(name => name !== 'main') || graderFunctionNames[0];
  const functionName = preferredGraderFunction || (fnMatch ? fnMatch[1] : (classMatch ? classMatch[1] : 'solve'));
  const params = fnMatch ? fnMatch[2].split(',').map(p => p.trim()).filter(Boolean) : [];
  const description = ex.description || '';

  // Find the exercise block anchor
  const idSearch = `"id": ${ex.id},`;
  const anchor = source.indexOf(idSearch);
  if (anchor === -1) continue;

  // Search backward to find the block opening `{`
  let blockStart = anchor;
  let depth = 0;
  while (blockStart >= 0) {
    if (source[blockStart] === '}') depth++;
    if (source[blockStart] === '{') { depth--; if (depth < 0) break; }
    blockStart--;
  }
  if (blockStart < 0) continue;

  // Search forward to find the block closing `}`
  let blockEnd = anchor;
  depth = 0;
  let inStr = false, quoteCh = '', esc = false;
  while (blockEnd < source.length) {
    const ch = source[blockEnd];
    if (inStr) {
      if (esc) esc = false;
      else if (ch === '\\') esc = true;
      else if (ch === quoteCh) inStr = false;
      blockEnd++; continue;
    }
    if (ch === '"' || ch === "'") { inStr = true; quoteCh = ch; blockEnd++; continue; }
    if (ch === '{') depth++;
    if (ch === '}') { depth--; if (depth < 0) { blockEnd++; if (source[blockEnd] === ',') blockEnd++; break; } }
    blockEnd++;
  }

  const oldBlock = source.slice(blockStart, blockEnd);
  let newBlock = oldBlock;
  let blockChanged = false;

  // ── Fix description examples ──
  if ((forceExamples || examplesNeedFix(description)) && grader && Array.isArray(grader.tests) && fnMatch) {
    const newExamples = generateExamples(functionName, grader.tests);
    if (newExamples.length) {
      const lines = description.split('\n');
      const nonExampleLines = lines.filter(l => !/\u2192/.test(l) && !/->/.test(l));
      const newDesc = nonExampleLines.join('\n') + '\n' + newExamples.join('\n');

      const descInfo = findFieldValue(newBlock, 0, 'description');
      if (descInfo) {
        newBlock = replaceFieldValue(newBlock, descInfo, newDesc);
        blockChanged = true;
        exampleFixCount++;
      }
    }
  }

  // ── Fix generic breakdown ──
  const hasGoodBreakdown = ex.breakdown && ex.breakdown.trim().length > 0
    && !ex.breakdown.includes('What is')
    && !ex.breakdown.includes('A **')
    && !ex.breakdown.includes('Apply the operation')
    && !ex.breakdown.includes('Perform the required operation');

  if (!hasGoodBreakdown) {
    const steps = generateBreakdown(functionName, params, description);
    if (steps.length) {
      const newBreakdown = steps.map((s, i) => `${i + 1}. ${s}`).join('\n');
      const bdInfo = findFieldValue(newBlock, 0, 'breakdown');
      if (bdInfo) {
        newBlock = replaceFieldValue(newBlock, bdInfo, newBreakdown);
        blockChanged = true;
        breakdownFixCount++;
      }
    }
  }

  // ── Fix generic hint ──
  if (!ex.hint || /check the description for requirements/i.test(ex.hint.trim()) || /Carefully identify what the problem asks for/.test(ex.hint)) {
    const hints = generateHint(functionName, params, description);
    if (hints.length) {
      const hintStr = hints.join('\n');
      const hInfo = findFieldValue(newBlock, 0, 'hint');
      if (hInfo) {
        newBlock = replaceFieldValue(newBlock, hInfo, hintStr);
        blockChanged = true;
        hintFixCount++;
      }
    }
  }

  if (blockChanged) {
    source = source.slice(0, blockStart) + newBlock + source.slice(blockEnd);
    fixCount++;
  }
}

console.log(`Fixed total: ${fixCount} problems`);
console.log(`  Examples fixed: ${exampleFixCount}`);
console.log(`  Breakdowns fixed: ${breakdownFixCount}`);
console.log(`  Hints fixed: ${hintFixCount}`);
console.log(`  Unfixed: ${EXERCISES.length - fixCount}`);

if (!writeMode) {
  console.log('\nDry run only. Re-run with --write to apply fixes to exercises.ts.');
  process.exit(0);
}

fs.writeFileSync(path.join(root, 'exercises.ts'), source);
console.log('exercises.ts updated.');
