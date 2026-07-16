import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';
import { localizeAiText } from './aiLocalization';
import { buildDetailedCodeExplanation } from './aiCodeExplanation';

const hasFunctionDefinition = (code: string) => /\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(code);
const hasReturn = (code: string) => /\breturn\b/.test(code);
const hasPrint = (code: string) => /\bprint\s*\(/.test(code);
const hasInput = (code: string) => /\binput\s*\(/.test(code);

const extractRequiredFunctionName = (text: string) => {
    const patterns = [
        /function\s+called\s+`?([A-Za-z_][A-Za-z0-9_]*)`?/i,
        /called\s+`?([A-Za-z_][A-Za-z0-9_]*)`?/i,
        /define\s+(?:a\s+)?function\s+`?([A-Za-z_][A-Za-z0-9_]*)`?/i,
        /def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(/i,
    ];
    for (const pattern of patterns) {
        const match = text.match(pattern);
        if (match?.[1]) return match[1];
    }
    return '';
};

const extractExpectedGot = (message: string) => {
    const match = message.match(/(?:for args=([^.]*)\.\s*)?Expected(?: output)? (.*?), got (.*?)\.$/i);
    if (!match) return null;
    return {
        args: match[1]?.trim() || '',
        expected: match[2]?.trim() || '',
        actual: match[3]?.trim() || '',
    };
};

const extractRaisedError = (message: string) => {
    const match = message.match(/(?:Test \d+|Case \d+|Input \d+)?\s*raised\s+([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$/i);
    if (!match) return null;
    return {
        errorType: match[1],
        detail: match[2]?.trim() || '',
    };
};

const extractExpectedFunctionNames = (message: string) => {
    const match = message.match(/Expected one of:\s*([A-Za-z0-9_,\s]+)/i);
    if (!match?.[1]) return [];
    return match[1]
        .split(',')
        .map(name => name.trim())
        .filter(Boolean);
};

const extractDefinedFunctions = (code: string) => {
    const functions: Array<{ name: string; params: string[] }> = [];
    const pattern = /\bdef\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)/g;
    let match: RegExpExecArray | null;
    while ((match = pattern.exec(code)) !== null) {
        const params = match[2]
            .split(',')
            .map(param => param.trim())
            .filter(Boolean);
        functions.push({ name: match[1], params });
    }
    return functions;
};

const getFirstGraderArgsLength = (graderSpec: unknown) => {
    const tests = (graderSpec as { tests?: Array<{ args?: unknown[] }> })?.tests;
    if (!Array.isArray(tests) || !tests.length) return null;
    const args = tests[0]?.args;
    return Array.isArray(args) ? args.length : null;
};

const graderUsesInputValues = (graderSpec: unknown) => {
    const tests = (graderSpec as { tests?: Array<{ inputValues?: unknown[] }> })?.tests;
    return Array.isArray(tests) && tests.some(test => Array.isArray(test?.inputValues) && test.inputValues.length > 0);
};

const hasForLoop = (code: string) => /\bfor\s+/.test(code);
const hasWhileLoop = (code: string) => /\bwhile\s+/.test(code);
const hasConditional = (code: string) => /\b(if|elif|else)\b/.test(code);
const hasImport = (code: string) => /^\s*(import|from)\s+/m.test(code);
const hasAssignment = (code: string) => /[^=]=[^=]/.test(code);
const extractVariableNames = (code: string) => {
    const names = new Set<string>();
    const patterns = [
        /(?:\b(?:for|in|not|and|or|is|if|elif|else|while|return|def|class|import|from|as|pass|break|continue|with|try|except|finally)\b)|(['"`])/g,
    ];
    const variablePattern = /\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=/g;
    let match;
    while ((match = variablePattern.exec(code)) !== null) {
        names.add(match[1]);
    }
    return names;
};

const extractKeyPhrases = (text: string) => {
    const phrases: string[] = [];
    const patterns = [
        /Write a Python(?:ic)? (?:way|program) to ([^.]+)/gi,
        /Create a function(?: called)? `?([A-Za-z_][A-Za-z0-9_]*)`?/gi,
        /define\s+(?:a\s+)?function(?: called)? `?([A-Za-z_][A-Za-z0-9_]*)`?/gi,
    ];
    for (const pattern of patterns) {
        const matches = text.matchAll(pattern);
        for (const m of matches) {
            phrases.push(m[1].toLowerCase());
        }
    }
    return phrases;
};

const extractRequiredSyntax = (text: string) => {
    const patterns: Array<{ regex: RegExp; label: string }> = [
        { regex: /`list\.extend\(\)`|list\.extend|\.extend\(/i, label: '.extend()' },
        { regex: /`list\.append\(\)`|list\.append|\.append\(/i, label: '.append()' },
        { regex: /`list\.index\(\)`|list\.index|\.index\(/i, label: '.index()' },
        { regex: /`list\.sort\(\)`|list\.sort|\.sort\(/i, label: '.sort()' },
        { regex: /`list\.reverse\(\)`|list\.reverse|\.reverse\(/i, label: '.reverse()' },
        { regex: /`list\.pop\(\)`|list\.pop|\.pop\(/i, label: '.pop()' },
        { regex: /`list\.remove\(\)`|list\.remove|\.remove\(/i, label: '.remove()' },
        { regex: /`list\.insert\(\)`|list\.insert|\.insert\(/i, label: '.insert()' },
        { regex: /`list\.copy\(\)`|list\.copy|\.copy\(/i, label: '.copy()' },
        { regex: /`list\.clear\(\)`|list\.clear|\.clear\(/i, label: '.clear()' },
        { regex: /`dict\.(?:get|keys|values|items)\(\)`|dict\.(?:get|keys|values|items)\(/i, label: 'dict method' },
        { regex: /`str\.(?:join|split|replace|strip|find)\(\)`|str\.(?:join|split|replace|strip|find)\(/i, label: 'string method' },
        { regex: /`set`|`frozenset`/i, label: 'set/frozenset' },
        { regex: /slicing/i, label: 'slicing' },
        { regex: /comprehension/i, label: 'comprehension' },
        { regex: /lambda/i, label: 'lambda' },
        { regex: /decorator/i, label: 'decorator' },
        { regex: /generator/i, label: 'generator' },
        { regex: /recursion/i, label: 'recursion' },
    ];
    return patterns.filter(p => p.regex.test(text)).map(p => p.label);
};

const getLineText = (code: string, lineNumber: number | null) => {
    if (!lineNumber || lineNumber < 1) return '';
    return code.split('\n')[lineNumber - 1]?.trim() || '';
};

const findReturnAssignmentLine = (code: string) => {
    return code
        .split('\n')
        .map((line, index) => ({ line: line.trim(), number: index + 1 }))
        .find(item => /^return\b/.test(item.line) && /=(?!=)/.test(item.line) && !/[!<>]=/.test(item.line));
};

const extractErrorLineNumber = (message: string) => {
    const match = message.match(/line\s+(\d+)/i);
    return match ? Number(match[1]) : null;
};

const detectLikelySyntaxIssue = (code: string, message: string) => {
    const lineNumber = extractErrorLineNumber(message);
    const lineText = getLineText(code, lineNumber);
    const lineHint = lineNumber ? ` on line ${lineNumber}${lineText ? `: \`${lineText}\`` : ''}` : '';

    if (/IndentationError|unexpected indent|expected an indented block|unindent does not match/i.test(message)) {
        return `Specific issue: indentation is wrong${lineHint}. Python uses indentation to decide what belongs inside a function, loop, or if-block.`;
    }
    if (/TabError/i.test(message)) {
        return `Specific issue: tabs and spaces are mixed${lineHint}. Use spaces consistently for indentation.`;
    }
    if (/forgot a comma|perhaps you forgot a comma/i.test(message)) {
        return `Specific issue: Python thinks a comma is missing${lineHint}. Check lists, tuples, function arguments, and dictionary entries around that line.`;
    }
    if (/invalid syntax|SyntaxError/i.test(message)) {
        const returnAssignmentLine = findReturnAssignmentLine(code);
        if (returnAssignmentLine) {
            return `Specific issue: invalid assignment inside a return statement on line ${returnAssignmentLine.number}: \`${returnAssignmentLine.line}\`. Python cannot do \`return x = value\`; assign first, then return the changed object.`;
        }
        const missingColonLine = code
            .split('\n')
            .map((line, index) => ({ line: line.trim(), number: index + 1 }))
            .find(item => /^(def|if|elif|else|for|while|try|except|finally|with|class)\b/.test(item.line) && !item.line.endsWith(':'));
        if (missingColonLine) {
            return `Specific issue: missing colon \`:\` on line ${missingColonLine.number}: \`${missingColonLine.line}\`. Lines that start blocks, like \`def\`, \`if\`, \`for\`, and \`while\`, must end with \`:\`.`;
        }
        const bracketBalance = {
            round: (code.match(/\(/g) || []).length - (code.match(/\)/g) || []).length,
            square: (code.match(/\[/g) || []).length - (code.match(/\]/g) || []).length,
            curly: (code.match(/\{/g) || []).length - (code.match(/\}/g) || []).length,
        };
        if (bracketBalance.round || bracketBalance.square || bracketBalance.curly) {
            return `Specific issue: brackets do not balance${lineHint}. Check that every \`(\`, \`[\`, or \`{\` has the matching closing bracket.`;
        }
        return `Specific issue: invalid Python syntax${lineHint}. Check punctuation first: commas, colons, quotes, and brackets.`;
    }
    return '';
};

const summarizeSpecificIssue = (
    request: AiReviewRequest,
    expectedGot: ReturnType<typeof extractExpectedGot>,
    raisedError: ReturnType<typeof extractRaisedError>,
    expectedFunctionNames: string[],
) => {
    const code = request.userCode || '';
    const message = request.graderMessage || '';
    if (request.graderPassed) {
        return 'Specific issue: none detected. The grader accepted the output/return value for this problem.';
    }

    const syntaxIssue = detectLikelySyntaxIssue(code, message);
    if (syntaxIssue) return syntaxIssue;

    if (expectedGot) {
        return expectedGot.args
            ? `Specific issue: output mismatch for ${expectedGot.args}. Expected \`${expectedGot.expected}\`, but the code produced \`${expectedGot.actual}\`.`
            : `Specific issue: output mismatch. Expected \`${expectedGot.expected}\`, but the code produced \`${expectedGot.actual}\`.`;
    }

    if (/Missing required source pattern|Missing required syntax/i.test(message)) {
        return `Specific issue: the required method/syntax is missing. ${message}`;
    }

    if (/Could not find a callable|Missing function/i.test(message)) {
        if (expectedFunctionNames.length) {
            return `Specific issue: wrong or missing function name. The grader is looking for \`${expectedFunctionNames.join('()` or `')}()\`.`;
        }
        const required = extractRequiredFunctionName(`${request.title}\n${request.description}`);
        return required
            ? `Specific issue: wrong or missing function name. The prompt expects \`${required}()\`.`
            : 'Specific issue: the grader could not find the function it needs to call.';
    }

    const nameError = message.match(/NameError:\s*name ['"]([^'"]+)['"] is not defined/i);
    if (nameError?.[1]) {
        return `Specific issue: variable/function \`${nameError[1]}\` is used before it is defined. Check spelling and make sure it is assigned before use.`;
    }

    const attributeError = message.match(/AttributeError:\s*['"]?([^'"]+)['"]? object has no attribute ['"]([^'"]+)['"]/i);
    if (attributeError?.[2]) {
        return `Specific issue: wrong method/property name \`.${attributeError[2]}\`. That object does not provide this method, so check the required method spelling/type.`;
    }

    if (/TypeError/i.test(message)) {
        if (/missing .* positional argument/i.test(message)) {
            return `Specific issue: function parameters do not match how the grader calls the function. ${message}`;
        }
        if (/takes .* positional argument/i.test(message)) {
            return `Specific issue: wrong number of function arguments. ${message}`;
        }
        if (/unsupported operand|not supported between/i.test(message)) {
            return `Specific issue: wrong data type for an operation. ${message}`;
        }
        return `Specific issue: type error. ${message}`;
    }

    if (raisedError) {
        return `Specific issue: runtime error \`${raisedError.errorType}\`${raisedError.detail ? `: \`${raisedError.detail}\`` : ''}.`;
    }

    if (/\bpass\b/.test(code)) {
        return 'Specific issue: the code still contains `pass`, so the required logic has not been written yet.';
    }

    return message && !/Run has not been pressed/i.test(message)
        ? `Specific issue: the grader rejected the answer with this message: \`${message}\`.`
        : 'Specific issue: not checked yet. Press `RUN` first so the review can identify the exact problem.';
};

const summarizeProblemRequirement = (
    request: AiReviewRequest,
    expectedGot?: ReturnType<typeof extractExpectedGot>,
    raisedError?: ReturnType<typeof extractRaisedError>,
    expectedFunctionNames: string[] = [],
) => {
    const description = (request.description || request.title || '').replace(/\s+/g, ' ').trim();
    const conciseDescription = description.length > 220 ? `${description.slice(0, 220)}...` : description;
    const issue = summarizeSpecificIssue(request, expectedGot || null, raisedError || null, expectedFunctionNames);
    return `${conciseDescription} ${issue}`;
};

const describeCodeLine = (line: string) => {
    if (/^from\s+/.test(line) || /^import\s+/.test(line)) return 'imports a module';
    if (/^def\s+/.test(line)) return 'defines the function the grader will call';
    if (line === 'pass') return 'is only a placeholder and does not implement or return anything';
    if (/^return\b/.test(line)) return 'returns a value to the grader';
    if (/^print\s*\(/.test(line)) return 'prints output to the console';
    if (/\binput\s*\(/.test(line)) return 'asks the user for interactive input';
    if (/=/.test(line) && !/[=!<>]=/.test(line)) return 'assigns a value';
    if (/^(if|elif|else)\b/.test(line)) return 'branches based on a condition';
    if (/^(for|while)\b/.test(line)) return 'loops over values';
    return 'runs this statement';
};

const explainPythonConcepts = (code: string) => {
    const explanations: string[] = [];
    const seen = new Set<string>();
    const add = (key: string, text: string) => {
        if (seen.has(key)) return;
        seen.add(key);
        explanations.push(text);
    };

    if (/\[[^\]\n]*\]/.test(code)) {
        add('list-literal', '`[...]` can create a list, or when it appears after a value like `name[...]` it indexes/slices that sequence.');
    }
    if (/\[[^\]\n]*:-?\d+[^\]\n]*\]|\[[^\]\n]*-?\d+:[^\]\n]*\]|\[[^\]\n]*:[^\]\n]*:[^\]\n]*\]/.test(code)) {
        add('slice', '`sequence[start:stop:step]` is slicing: `start` is where to begin, `stop` is excluded, and `step` controls how far to move each time.');
    }
    if (/\[-1\]/.test(code)) {
        add('negative-index', '`[-1]` means the last item in a string, list, or tuple. `[-2]` would mean the second-last item.');
    }
    if (/\[::-1\]/.test(code)) {
        add('reverse-slice', '`[::-1]` means take the whole sequence with a step of `-1`, so it reverses a string/list/tuple.');
    }
    if (/\[[^\]\n]*\bfor\b[^\]\n]*\bin\b[^\]\n]*\]/.test(code)) {
        add('list-comprehension', '`[expression for item in iterable]` is a list comprehension. It builds a new list by running the expression once for each item.');
    }
    if (/\{[^}\n]*:[^}\n]*\}/.test(code)) {
        add('dict-literal', '`{key: value}` creates a dictionary. Dictionaries store lookup pairs, so `data[key]` retrieves the value for that key.');
    }
    if (/\{[^}\n]*\bfor\b[^}\n]*\bin\b[^}\n]*\}/.test(code)) {
        add('dict-comprehension', '`{key: value for item in iterable}` is a dictionary comprehension. It builds a dictionary by looping and creating key/value pairs.');
    }
    if (/\{[^}:{}\n]*(?:,\s*[^}:{}\n]+)+\}/.test(code)) {
        add('set-literal', '`{a, b, c}` creates a set when there are no `key: value` pairs. Sets store unique values and are useful for membership checks.');
    }
    if (/\([^)\n]*\bfor\b[^)\n]*\bin\b[^)\n]*\)/.test(code)) {
        add('generator', '`(expression for item in iterable)` is a generator expression. It produces values lazily instead of building a full list immediately.');
    }
    if (/\blambda\b/.test(code)) {
        add('lambda', '`lambda` creates a small anonymous function, often used as a `key=` function for sorting or filtering.');
    }
    if (/\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(code)) {
        add('def', '`def name(...):` defines a function. Python records the function first; the indented body runs later when the function is called.');
    }
    if (/\breturn\b/.test(code)) {
        add('return', '`return` sends a value back to the caller/grader. Code after `return` in the same block usually will not run.');
    }
    if (/\bprint\s*\(/.test(code)) {
        add('print', '`print(...)` displays text in the output panel. It does not return that value to the grader unless the problem is output-based.');
    }
    if (/\binput\s*\(/.test(code)) {
        add('input', '`input(...)` pauses for user text and returns that text as a string. Convert it with `int()` or `float()` when numbers are needed.');
    }
    if (/\bfor\s+/.test(code)) {
        add('for', '`for item in iterable:` repeats the indented block once for each item in the iterable.');
    }
    if (/\bwhile\s+/.test(code)) {
        add('while', '`while condition:` repeats while the condition stays true. The loop must update something or it can run forever.');
    }
    if (/\bif\s+/.test(code)) {
        add('if', '`if` checks a condition. `elif` checks another condition, and `else` runs when the earlier conditions are false.');
    }
    if (/\bwith\s+/.test(code)) {
        add('with', '`with` opens a context safely, such as a file. Python automatically runs cleanup when the block finishes.');
    }
    if (/\btry\s*:/.test(code)) {
        add('try', '`try` runs code that might fail. `except` catches selected errors so the program can handle them.');
    }
    if (/==|!=|<=|>=|<|>/.test(code)) {
        add('comparison', 'Comparison operators like `==`, `!=`, `<`, and `>` produce `True` or `False` and are commonly used in `if` or `while` logic.');
    }
    if (/\bis\b|\bis not\b/.test(code)) {
        add('identity', '`is` checks object identity, meaning whether two names point to the exact same object. Use `==` when you want value equality.');
    }
    if (/%/.test(code)) {
        add('modulo', '`%` is modulo. It returns the remainder, so `number % 2 == 0` checks whether a number is even.');
    }
    if (/\*\*/.test(code)) {
        add('power', '`**` is exponentiation. For example, `number ** 2` squares a number.');
    }
    if (/\/\//.test(code)) {
        add('floor-division', '`//` is floor division. It divides and rounds down to an integer-like result.');
    }

    const builtinExplanations: Array<[RegExp, string, string]> = [
        [/\blen\s*\(/, 'len', '`len(x)` returns how many items are in a string, list, tuple, dict, or other sized object.'],
        [/\brange\s*\(/, 'range', '`range(...)` creates a sequence of numbers, often used by `for` loops.'],
        [/\bsum\s*\(/, 'sum', '`sum(iterable)` adds numeric values together.'],
        [/\bmax\s*\(/, 'max', '`max(iterable)` returns the largest value. With `key=`, it chooses the item whose key value is largest.'],
        [/\bmin\s*\(/, 'min', '`min(iterable)` returns the smallest value. With `key=`, it chooses the item whose key value is smallest.'],
        [/\bsorted\s*\(/, 'sorted', '`sorted(iterable)` returns a new sorted list and does not mutate the original object.'],
        [/\bmap\s*\(/, 'map', '`map(function, iterable)` applies a function to every item and returns an iterator.'],
        [/\bfilter\s*\(/, 'filter', '`filter(function, iterable)` keeps only items where the function returns truthy.'],
        [/\bzip\s*\(/, 'zip', '`zip(a, b)` pairs items from multiple iterables by position.'],
        [/\benumerate\s*\(/, 'enumerate', '`enumerate(iterable)` gives `(index, value)` pairs while looping.'],
        [/\bstr\s*\(/, 'str', '`str(x)` converts a value to text.'],
        [/\bint\s*\(/, 'int', '`int(x)` converts text or a number to an integer.'],
        [/\bfloat\s*\(/, 'float', '`float(x)` converts text or a number to a decimal number.'],
        [/\blist\s*\(/, 'list', '`list(x)` converts an iterable into a list.'],
        [/\bdict\s*\(/, 'dict', '`dict(...)` creates a dictionary or converts key/value pairs into a dictionary.'],
        [/\bset\s*\(/, 'set', '`set(x)` creates a collection of unique values.'],
        [/\bbool\s*\(/, 'bool', '`bool(x)` converts a value to `True` or `False`. Empty values are usually `False`.'],
        [/\babs\s*\(/, 'abs', '`abs(x)` returns the positive distance from zero.'],
        [/\bround\s*\(/, 'round', '`round(x, n)` rounds a number, optionally to `n` decimal places.'],
    ];

    for (const [regex, key, text] of builtinExplanations) {
        if (regex.test(code)) add(key, text);
    }

    const methodExplanations: Array<[RegExp, string, string]> = [
        [/\.\s*append\s*\(/, 'append', '`.append(x)` adds one item to the end of a list and mutates that list.'],
        [/\.\s*extend\s*\(/, 'extend', '`.extend(items)` adds each item from another iterable to the end of a list.'],
        [/\.\s*pop\s*\(/, 'pop', '`.pop()` removes and returns an item. On lists it defaults to the last item; on dicts it removes a key.'],
        [/\.\s*remove\s*\(/, 'remove', '`.remove(x)` removes the first matching value from a list.'],
        [/\.\s*sort\s*\(/, 'sort', '`.sort()` sorts a list in place and returns `None`.'],
        [/\.\s*split\s*\(/, 'split', '`.split(...)` breaks a string into a list of smaller strings.'],
        [/\.\s*join\s*\(/, 'join', '`separator.join(items)` combines strings with the separator between them.'],
        [/\.\s*strip\s*\(/, 'strip', '`.strip()` removes whitespace from the start and end of a string.'],
        [/\.\s*replace\s*\(/, 'replace', '`.replace(old, new)` returns text with matching parts changed.'],
        [/\.\s*lower\s*\(/, 'lower', '`.lower()` returns lowercase text.'],
        [/\.\s*upper\s*\(/, 'upper', '`.upper()` returns uppercase text.'],
        [/\.\s*items\s*\(/, 'items', '`.items()` on a dictionary gives `(key, value)` pairs for looping.'],
        [/\.\s*keys\s*\(/, 'keys', '`.keys()` on a dictionary gives its keys.'],
        [/\.\s*values\s*\(/, 'values', '`.values()` on a dictionary gives its values.'],
        [/\.\s*get\s*\(/, 'get', '`.get(key, default)` reads a dictionary key without crashing if the key is missing.'],
        [/\.\s*read_text\s*\(/, 'read_text', '`Path(...).read_text()` reads a whole text file and returns its content as a string.'],
        [/\.\s*write_text\s*\(/, 'write_text', '`Path(...).write_text(text)` writes text to a file and returns the number of characters written.'],
        [/\.\s*glob\s*\(/, 'glob', '`Path(...).glob(pattern)` finds paths matching a filename pattern such as `*.py`.'],
    ];

    for (const [regex, key, text] of methodExplanations) {
        if (regex.test(code)) add(key, text);
    }

    if (/\bjson\.dump\s*\(/.test(code)) add('json-dump', '`json.dump(data, file)` writes a Python object into an open file as JSON text.');
    if (/\bjson\.load\s*\(/.test(code)) add('json-load', '`json.load(file)` reads JSON text from an open file and converts it back to Python data.');
    if (/\bre\.(?:findall|search|match|fullmatch|sub)\s*\(/.test(code)) add('regex', '`re` functions use regular expressions. They match patterns in strings instead of only exact text.');

    return explanations;
};

const summarizeCodeExplanation = (userCode: string, solution: string) => {
    return buildDetailedCodeExplanation(userCode, solution, 'en');
};

const conciseOutput = (value: string | undefined, fallback = 'No visible output') => {
    const text = String(value || '').trim();
    if (!text) return fallback;
    return text.length > 180 ? `${text.slice(0, 180)}...` : text;
};

const summarizeOutputAnalysis = (
    request: AiReviewRequest,
    expectedGot: ReturnType<typeof extractExpectedGot>,
    raisedError: ReturnType<typeof extractRaisedError>,
) => {
    const visibleOutput = conciseOutput(request.programOutput);

    if (request.graderPassed) {
        return `Output analysis: Correct. The grader accepted this answer. User output: \`${visibleOutput}\`. This means the final \`return\` value or printed output matched the tests for this problem.`;
    }

    if (expectedGot) {
        const caseText = expectedGot.args ? ` For ${expectedGot.args},` : '';
        return `Output analysis: Incorrect.${caseText} expected \`${expectedGot.expected}\`, but the user output/result was \`${expectedGot.actual}\`. The code is close only if the approach is right, but the final value does not match what the problem requires. Fix the line that creates the final \`return\` value or printed output, then rerun.`;
    }

    if (raisedError) {
        return `Output analysis: Incorrect. The code did not produce a valid final answer because it crashed with \`${raisedError.errorType}\`${raisedError.detail ? `: \`${raisedError.detail}\`` : ''}. Fix that runtime error first, then check the output again.`;
    }

    const message = conciseOutput(request.graderMessage, 'The grader did not return a detailed mismatch.');
    if (/Run has not been pressed/i.test(message)) {
        return `Output analysis: Not checked yet. Press \`RUN\` first so the app can compare the user output against this problem's grader.`;
    }

    return `Output analysis: Incorrect. User output: \`${visibleOutput}\`. Grader message: \`${message}\`. The answer did not satisfy the tests, so inspect the final \`return\` or \`print\` and compare it with the problem requirement.`;
};

const extractPrimarySolutionLines = (solution: string) => {
    const lines = solution.trim().split('\n');
    const imports = lines.filter(line => /^\s*(?:from|import)\s+/.test(line)).slice(0, 4);
    const firstDefIndex = lines.findIndex(line => /^\s*def\s+/.test(line));
    if (firstDefIndex >= 0) {
        const block: string[] = [];
        for (let index = firstDefIndex; index < lines.length; index += 1) {
            const line = lines[index];
            if (index > firstDefIndex && line.trim() && !/^\s/.test(line)) {
                break;
            }
            if (!/^\s*#/.test(line)) {
                block.push(line);
            }
        }
        return [...imports, ...block].filter((line, index, arr) => line.trim() || (index > 0 && arr[index - 1].trim()));
    }
    return lines.filter(line => !/^\s*#/.test(line)).slice(0, 12);
};

const summarizeCodeLines = (code: string) => {
    const lines = code.split('\n');
    const importantLines = lines
        .map((line, index) => ({ line: line.trim(), number: index + 1 }))
        .filter(item => item.line && !item.line.startsWith('#'))
        .slice(0, 8);

    if (!importantLines.length) {
        return 'Code inspection: the editor is empty, so there are no lines to grade yet.';
    }

    return `Line-by-line code inspection: ${importantLines.map(item => `line ${item.number} \`${item.line}\` ${describeCodeLine(item.line)}`).join('; ')}.`;
};

const summarizeExpectedWorkflow = (solution: string) => {
    const primaryLines = extractPrimarySolutionLines(solution)
        .map(line => line.trim())
        .filter(Boolean)
        .slice(0, 8);

    if (!primaryLines.length) return '';

    const hasNestedFunction = primaryLines.some((line, index) => index > 0 && /^\s+def\s+/.test(line));
    const workflow = primaryLines.map((line, index) => {
        if (/^def\s+/.test(line)) return `step ${index + 1}: \`${line}\` builds the function boundary and defines what the grader can call`;
        if (/^from\s+|^import\s+/.test(line)) return `step ${index + 1}: \`${line}\` loads the tool/module needed before the function runs`;
        if (/=/.test(line) && !/[=!<>]=/.test(line)) return `step ${index + 1}: \`${line}\` creates an intermediate value used by the later return/output`;
        if (/^return\b/.test(line)) return `step ${index + 1}: \`${line}\` sends the final value back to the grader`;
        if (/^print\s*\(/.test(line)) return `step ${index + 1}: \`${line}\` displays the final value`;
        return `step ${index + 1}: \`${line}\` is part of the required execution flow`;
    });

    const closureNote = hasNestedFunction
        ? ' Function workflow note: because this solution defines a function inside another function, the inner function can close over values from the outer scope; that is the closure relationship.'
        : ' Function workflow note: execution starts outside the function, but the function body only runs when the grader or script calls it.';

    return `Expected solution workflow: ${workflow.join('; ')}.${closureNote}`;
};

const visibleSolutionFix = (request: AiReviewRequest) => {
    const solution = (request.visibleSolution || '').trim();
    if (!solution) return '';

    const concise = extractPrimarySolutionLines(solution).join('\n').trim();
    return concise ? `Use this structure for this exact problem:\n\`\`\`python\n${concise}\n\`\`\`` : '';
};

const describeCodeLineFr = (line: string) => {
    if (/^\s*(?:from|import)\s+/.test(line)) return 'importe un module';
    if (/^\s*def\s+/.test(line)) return 'définit la fonction que le correcteur peut appeler';
    if (/^\s*pass\s*$/.test(line)) return 'est seulement un emplacement vide et ne réalise aucun calcul';
    if (/^\s*return\b/.test(line)) return 'renvoie une valeur au correcteur';
    if (/^\s*print\s*\(/.test(line)) return 'affiche une valeur dans la sortie';
    if (/\binput\s*\(/.test(line)) return 'demande une entrée interactive';
    if (/^\s*(?:if|elif|else)\b/.test(line)) return 'choisit une branche selon une condition';
    if (/^\s*(?:for|while)\b/.test(line)) return 'répète un bloc de code';
    if (/=/.test(line) && !/[=!<>]=/.test(line)) return 'affecte ou calcule une valeur';
    return 'exécute cette instruction';
};

const buildFrenchDiagnosticReview = (
    request: AiReviewRequest,
    verdict: AiReviewResult['verdict'],
    confidence: number,
    expectedGot: ReturnType<typeof extractExpectedGot>,
    raisedError: ReturnType<typeof extractRaisedError>,
    requiredFunctionName: string,
): AiReviewResult => {
    const code = request.userCode || '';
    const importantLines = code.split('\n')
        .map((line, index) => ({ text: line.trim(), number: index + 1 }))
        .filter(item => item.text && !item.text.startsWith('#'))
        .slice(0, 10);
    const codeCheck = importantLines.length
        ? importantLines.map(item => `Ligne ${item.number} : \`${item.text}\` ${describeCodeLineFr(item.text)}.`).join('\n')
        : 'L’éditeur est vide : aucune ligne ne peut encore être vérifiée.';

    let outputAnalysis: string;
    if (request.graderPassed) {
        outputAnalysis = `Correcte. Le correcteur a accepté la réponse${request.programOutput?.trim() ? ` et la sortie visible est \`${request.programOutput.trim().slice(0, 180)}\`` : ''}.`;
    } else if (expectedGot) {
        outputAnalysis = `${expectedGot.args ? `Pour ${expectedGot.args}, ` : ''}le correcteur attendait \`${expectedGot.expected}\`, mais le code a produit \`${expectedGot.actual}\`.`;
    } else if (raisedError) {
        outputAnalysis = `Le code s’est arrêté avec \`${raisedError.errorType}\`${raisedError.detail ? ` : \`${raisedError.detail}\`` : ''}. Cette erreur doit être corrigée avant de vérifier le résultat final.`;
    } else {
        outputAnalysis = `Le correcteur n’a pas accepté cette réponse. ${localizeAiText(request.graderMessage || 'Aucun détail supplémentaire.', 'fr')}`;
    }

    const codeExplanation = buildDetailedCodeExplanation(code, request.visibleSolution || '', 'fr');

    const solutionLines = extractPrimarySolutionLines(request.visibleSolution || '')
        .map(line => line.trim())
        .filter(Boolean)
        .slice(0, 7);
    const workflow = solutionLines.length
        ? solutionLines.map((line, index) => `Étape ${index + 1} : \`${line}\` ${describeCodeLineFr(line)}.`).join('\n')
        : 'Identifiez les entrées demandées, appliquez l’opération décrite, puis renvoyez ou affichez exactement le type de résultat demandé.';

    let suggestedFix = 'Comparez le nom de la fonction, ses paramètres, la valeur renvoyée et les cas limites avec l’énoncé, puis relancez le code.';
    if (!code.trim()) suggestedFix = 'Écrivez d’abord une solution dans l’éditeur, puis relancez la révision.';
    else if (/\bpass\b/.test(code)) suggestedFix = 'Remplacez `pass` par la logique demandée et ajoutez la valeur finale avec `return` ou `print()` selon l’énoncé.';
    else if (expectedGot?.actual === 'None' && hasFunctionDefinition(code) && !hasReturn(code)) suggestedFix = 'La fonction renvoie `None`. Remplacez le `print()` final par `return`, ou ajoutez un `return` dans chaque branche.';
    else if (raisedError) suggestedFix = `Corrigez d’abord l’erreur \`${raisedError.errorType}\`, puis exécutez à nouveau le code.`;
    else if (requiredFunctionName && !new RegExp(`\\bdef\\s+${requiredFunctionName}\\s*\\(`).test(code)) suggestedFix = `Définissez la fonction demandée avec le nom exact \`${requiredFunctionName}\`.`;

    return {
        verdict,
        confidence,
        explanation: [
            `1. Exigence du problème\n${request.description || request.title}`,
            `2. Vérification ligne par ligne\n${codeCheck}`,
            `3. Analyse de la sortie\n${outputAnalysis}`,
            `4. ${codeExplanation}`,
            `5. Déroulement de la solution\n${workflow}`,
            `6. Point à corriger\n${suggestedFix}`,
        ].join('\n\n'),
        suggestedFix,
        source: 'diagnostic',
    };
};

const buildCodeComparisonReview = (userCode: string, solution: string, description: string): { notes: string[]; fixes: string[] } => {
    const notes: string[] = [];
    const fixes: string[] = [];

    if (!userCode.trim()) {
        notes.push('The editor is empty. Write your Python code before pressing AI Review.');
        fixes.push('Type your solution in the code editor, then press AI Review again to get feedback.');
        return { notes, fixes };
    }

    const userFns = extractDefinedFunctions(userCode);
    const solutionFns = extractDefinedFunctions(solution);
    const userVars = extractVariableNames(userCode);
    const solutionVars = extractVariableNames(solution);

    if (userFns.length === 0 && solutionFns.length > 0) {
        notes.push(`The problem expects you to define a function (${solutionFns.map(f => `${f.name}()`).join(', ')}), but your code does not define any functions.`);
        fixes.push(`Start by defining a function: def ${solutionFns[0].name}(...): and put your logic inside it.`);
    } else if (userFns.length > 0 && solutionFns.length > 0) {
        const solutionFnNames = new Set(solutionFns.map(f => f.name));
        const missingFns = solutionFns.filter(f => !userFns.some(u => u.name === f.name));
        if (missingFns.length > 0) {
            notes.push(`Your code is missing a function named ${missingFns.map(f => `'${f.name}()'`).join(', ')} that the problem expects.`);
            fixes.push(`Define a function called ${missingFns[0].name} with the correct parameters.`);
        }
        for (const userFn of userFns) {
            const matchSol = solutionFns.find(s => s.name === userFn.name);
            if (matchSol && userFn.params.length !== matchSol.params.length) {
                notes.push(`Your function '${userFn.name}' takes ${userFn.params.length} parameter${userFn.params.length === 1 ? '' : 's'} (${userFn.params.join(', ') || 'none'}), but it should take ${matchSol.params.length} parameter${matchSol.params.length === 1 ? '' : 's'} (${matchSol.params.join(', ') || 'none'}).`);
                fixes.push(`Change 'def ${userFn.name}(${userFn.params.join(', ')})' to 'def ${userFn.name}(${matchSol.params.join(', ')})'.`);
            }
        }
    }

    const descLower = description.toLowerCase();
    const reqPrint = /print/i.test(descLower);
    const reqReturn = /return/i.test(descLower);

    const userPrints = hasPrint(userCode);
    const userReturns = hasReturn(userCode);
    const solPrints = hasPrint(solution);
    const solReturns = hasReturn(solution);

    if (solReturns && !userReturns && userPrints) {
        notes.push('The solution uses return to produce a value, but your code only prints output. The grader may expect a return value instead of printed output.');
        fixes.push('Change print() to return so the function can be tested programmatically.');
    }

    if (solPrints && !userPrints && !solReturns) {
        notes.push('The solution uses print() to show output, but your code does not print anything.');
        fixes.push('Add a print() statement to display the result.');
    }

    const solLoops = hasForLoop(solution) || hasWhileLoop(solution);
    const userLoops = hasForLoop(userCode) || hasWhileLoop(userCode);
    if (solLoops && !userLoops) {
        notes.push('The solution uses a loop, but your code does not. The problem may require iterating over data.');
        fixes.push('Add a for or while loop to process the data.');
    }

    const solConditionals = hasConditional(solution);
    const userConditionals = hasConditional(userCode);
    if (solConditionals && !userConditionals) {
        notes.push('The solution uses conditionals (if/else), but your code does not. The problem may require branching logic.');
        fixes.push('Add if/else statements to handle different cases.');
    }

    const solImports = hasImport(solution);
    const userImports = hasImport(userCode);
    if (solImports && !userImports && solImports) {
        const solutionImports = (solution.match(/^\s*(?:import|from)\s+\S+/gm) || []).join('; ');
        notes.push(`The solution imports modules: ${solutionImports}. You may be missing a required import.`);
        fixes.push(`Add: ${solutionImports}`);
    }

    const missingVars: string[] = [];
    for (const solVar of solutionVars) {
        if (!userVars.has(solVar) && !/^(i|j|n|x|result|item|key|value|count|total|num|val|temp)$/.test(solVar)) {
            missingVars.push(solVar);
        }
    }
    if (missingVars.length > 0 && missingVars.length <= 5) {
        const likelyExpected = missingVars.filter(v => new RegExp(`\\b${v}\\b`, 'i').test(description));
        if (likelyExpected.length > 0) {
            notes.push(`The problem description mentions '${likelyExpected.join(', ')}', but your code does not define or use these variables.`);
            fixes.push(`Initialize and use ${likelyExpected.map(v => `'${v}'`).join(', ')} in your solution.`);
        }
    }

    const descPhrases = extractKeyPhrases(description);
    for (const phrase of descPhrases) {
        if (phrase.length > 3 && !userCode.toLowerCase().includes(phrase)) {
            const keywords = phrase.split(/\s+/);
            const solMatching = keywords.some(k => k.length > 3 && solution.toLowerCase().includes(k));
            if (solMatching) {
                notes.push(`The problem mentions '${phrase}', but your code does not use that approach. The solution uses concepts related to: ${phrase}.`);
                break;
            }
        }
    }

    const requiredSyntax = extractRequiredSyntax(description);
    for (const syntax of requiredSyntax) {
        const escapedSyntax = syntax.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        if (!new RegExp(escapedSyntax, 'i').test(userCode)) {
            const solutionUsesIt = new RegExp(escapedSyntax, 'i').test(solution);
            if (solutionUsesIt) {
                notes.push(`The problem asks you to use ${syntax}, but your code does not contain ${syntax}. The solution uses ${syntax} to solve it.`);
                fixes.push(`Use ${syntax} in your code as required by the problem statement.`);
            }
        }
    }

    return { notes, fixes };
};

export const buildDiagnosticReview = (request: AiReviewRequest): AiReviewResult => {
    const code = request.userCode || '';
    const graderMessage = request.graderMessage || '';
    const problemText = `${request.title || ''}\n${request.description || ''}`;
    const requiredFunctionName = extractRequiredFunctionName(problemText);
    const expectedGot = extractExpectedGot(graderMessage);
    const raisedError = extractRaisedError(graderMessage);
    const expectedFunctionNames = extractExpectedFunctionNames(graderMessage);
    const definedFunctions = extractDefinedFunctions(code);
    const firstGraderArgsLength = getFirstGraderArgsLength(request.graderSpec);
    const usesInputValues = graderUsesInputValues(request.graderSpec);
    const notes: string[] = [];
    const fixes: string[] = [];
    let confidence = 0.35;
    let verdict: AiReviewResult['verdict'] = 'unclear';

    const hasUsefulGraderMessage = graderMessage &&
        graderMessage !== 'Run has not been pressed for this code yet.' &&
        graderMessage !== 'Run has not been pressed for this code yet' &&
        !/running a custom auto-grader|run has not been pressed/i.test(graderMessage) &&
        graderMessage !== '';

    if (request.graderPassed) {
        const expectedWorkflow = request.visibleSolution ? summarizeExpectedWorkflow(request.visibleSolution) : '';
        const codeExplanation = summarizeCodeExplanation(code, request.visibleSolution || '');
        const outputAnalysis = summarizeOutputAnalysis(request, expectedGot, raisedError);
        return {
            verdict: 'likely_correct',
            confidence: 0.99,
            explanation: `Problem requirement: ${summarizeProblemRequirement(request, expectedGot, raisedError, expectedFunctionNames)} ${summarizeCodeLines(code)} ${outputAnalysis} ${codeExplanation} ${expectedWorkflow} Execution order: Python reads imports and function definitions first; the function body runs only when called; the final \`return\` or printed output is what the grader checks. The deterministic grader passed this exact code, so the submitted behavior matches the hidden tests for this problem.`,
            suggestedFix: 'No fix needed; the deterministic grader already accepted this solution.',
            source: 'diagnostic',
        };
    }

    if (request.description || request.title) {
        notes.push(`Problem requirement: ${summarizeProblemRequirement(request, expectedGot, raisedError, expectedFunctionNames)}`);
    }

    notes.push(summarizeCodeLines(code));
    notes.push(summarizeOutputAnalysis(request, expectedGot, raisedError));
    notes.push(summarizeCodeExplanation(code, request.visibleSolution || ''));

    if (request.visibleSolution) {
        const expectedWorkflow = summarizeExpectedWorkflow(request.visibleSolution);
        if (expectedWorkflow) {
            notes.push(expectedWorkflow);
            notes.push('Execution order: Python loads imports first, records function definitions next, then runs the function body only when the grader or script calls it. Intermediate assignments prepare values; the final return/output is what decides whether the answer passes.');
        }
    }

    if (/\bpass\b/.test(code)) {
        verdict = 'likely_incorrect';
        confidence = Math.max(confidence, 0.86);
        notes.push('The code still contains pass, so the required function body is blank. A function that reaches pass returns None, which cannot satisfy a problem that asks for a computed result.');
        fixes.push(visibleSolutionFix(request) || 'Replace pass with the actual logic and return the required result from the function.');
    }

    if (hasUsefulGraderMessage) {
        if (/Missing required source pattern|Missing required syntax/i.test(graderMessage)) {
            verdict = 'likely_incorrect';
            confidence = 0.82;
            notes.push(`This answer is missing syntax required by this problem: ${graderMessage}`);
            fixes.push('Use the exact syntax/API requested in the problem statement.');
        }

        if (/Could not find a callable|function/i.test(graderMessage) && !hasFunctionDefinition(code)) {
            verdict = 'likely_incorrect';
            confidence = Math.max(confidence, 0.8);
            notes.push(requiredFunctionName
                ? `This problem expects a function named ${requiredFunctionName}(), but the submitted code does not define a callable function with that name.`
                : 'This problem expects a function, but the submitted code does not define a callable function.');
            fixes.push(requiredFunctionName
                ? `Start with def ${requiredFunctionName}(...): and return the required value.`
                : 'Define the required function and return the required value.');
        }

        if (/Missing function|Could not find a callable/i.test(graderMessage) && expectedFunctionNames.length && hasFunctionDefinition(code)) {
            const matchingDefinition = definedFunctions.find(fn => expectedFunctionNames.includes(fn.name));
            if (matchingDefinition && firstGraderArgsLength !== null && matchingDefinition.params.length !== firstGraderArgsLength) {
                verdict = 'likely_incorrect';
                confidence = Math.max(confidence, 0.88);
                notes.push(`The function name ${matchingDefinition.name} is present, but the signature does not match the grader. The grader calls ${matchingDefinition.name}() with ${firstGraderArgsLength} argument${firstGraderArgsLength === 1 ? '' : 's'}, while the code defines ${matchingDefinition.name}(${matchingDefinition.params.join(', ') || ''}).`);
                if (usesInputValues) {
                    notes.push('This grader supplies test input through input(), so this specific problem is configured like an input-based function even though the wording may sound like a parameter-based function.');
                }
                fixes.push(firstGraderArgsLength === 0
                    ? `For this grader, define ${matchingDefinition.name}() with no parameters and read the provided values using input(), or fix the problem/grader data if the prompt should require parameters.`
                    : `Change the function signature so ${matchingDefinition.name} accepts ${firstGraderArgsLength} argument${firstGraderArgsLength === 1 ? '' : 's'}.`);
            } else if (!matchingDefinition) {
                verdict = 'likely_incorrect';
                confidence = Math.max(confidence, 0.82);
                notes.push(`The grader is looking for ${expectedFunctionNames.join(' or ')}(), but the submitted function names are ${definedFunctions.map(fn => fn.name).join(', ') || 'none'}.`);
                fixes.push(`Rename the function to ${expectedFunctionNames[0]}.`);
            }
        }

        if (expectedGot) {
            verdict = verdict === 'likely_incorrect' ? verdict : 'unclear';
            confidence = Math.max(confidence, 0.68);
            notes.push(expectedGot.args
                ? `For ${expectedGot.args}, the grader expected ${expectedGot.expected}, but your code produced ${expectedGot.actual}.`
                : `The grader expected ${expectedGot.expected}, but your code produced ${expectedGot.actual}.`);
            fixes.push('Trace that exact case by hand and make the function return the expected value.');
        }

        if (expectedGot?.actual === 'None' && hasFunctionDefinition(code) && !hasReturn(code)) {
            verdict = 'likely_incorrect';
            confidence = Math.max(confidence, 0.85);
            notes.push('The function returned None, which usually means it ended without a return statement.');
            fixes.push('Replace print-only logic with return, or add a return on every branch.');
        } else if (hasPrint(code) && !hasReturn(code) && expectedGot) {
            notes.push('The code prints output, but this problem appears to require returning a value from the function.');
            fixes.push('Return the value from the function instead of only printing it.');
        }

        if (requiredFunctionName && hasFunctionDefinition(code) && !new RegExp(`\\bdef\\s+${requiredFunctionName}\\s*\\(`).test(code)) {
            verdict = 'likely_incorrect';
            confidence = Math.max(confidence, 0.78);
            notes.push(`The problem asks for ${requiredFunctionName}(), but the submitted function name appears to be different.`);
            fixes.push(`Rename the function to ${requiredFunctionName}.`);
        }

        if (raisedError) {
            verdict = 'likely_incorrect';
            confidence = Math.max(confidence, 0.82);
            notes.push(`The code crashes during grading with ${raisedError.errorType}${raisedError.detail ? `: ${raisedError.detail}` : ''}.`);
            fixes.push(`Fix the ${raisedError.errorType} before checking the final answer.`);
        }

        if (/Cannot access|before initialization|ReferenceError|TypeError|SyntaxError|NameError/i.test(graderMessage) && !raisedError) {
            verdict = 'likely_incorrect';
            confidence = Math.max(confidence, 0.82);
            notes.push(`The grader/run system reported this concrete failure: ${graderMessage}`);
            const returnAssignmentLine = findReturnAssignmentLine(code);
            fixes.push(
                returnAssignmentLine
                    ? 'Split the assignment and return into separate lines, for example: `dic["c"] = 88` on one line, then `return dic` on the next line.'
                    : visibleSolutionFix(request) || 'Fix the runtime error first, then rerun so the grader can compare the actual return value/output.'
            );
        }
    }

    if (hasInput(code)) {
        notes.push('The code uses input(); only script/input problems should ask for interactive input during grading.');
        fixes.push('If this is a function problem, accept parameters instead of calling input().');
    }

    if (!notes.length && request.visibleSolution) {
        const comparison = buildCodeComparisonReview(code, request.visibleSolution, request.description || request.title);
        if (comparison.notes.length > 0) {
            verdict = 'likely_incorrect';
            confidence = 0.7;
            notes.push(...comparison.notes);
            fixes.push(...comparison.fixes);
        } else if (code.trim()) {
            notes.push('Your code structure is similar to the expected solution, but the grader rejected it. Check for subtle differences in logic, edge cases, or exact output format.');
            fixes.push('Compare your output format, variable names, and edge case handling against the problem statement.');
        } else {
            notes.push(`The grader rejected this answer for this problem: ${request.description || request.title || graderMessage}`);
            fixes.push('Compare the submitted code against the exact function name, inputs, return value, and edge cases in the prompt.');
        }
    } else if (!notes.length) {
        notes.push(`The grader rejected this answer for this problem: ${request.description || request.title || graderMessage}`);
        fixes.push('Compare the submitted code against the exact function name, inputs, return value, and edge cases in the prompt.');
    }

    if (request.language === 'fr') {
        return buildFrenchDiagnosticReview(request, verdict, confidence, expectedGot, raisedError, requiredFunctionName);
    }

    const explanation = notes.join(' ');
    const suggestedFix = fixes.length
        ? [...new Set(fixes)].join(' ')
        : 'Compare the required function name, return value, and edge cases against the problem statement.';

    return {
        verdict,
        confidence,
        explanation: localizeAiText(explanation, request.language || 'en'),
        suggestedFix: localizeAiText(suggestedFix, request.language || 'en'),
        source: 'diagnostic',
    };
};
