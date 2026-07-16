export type AiCodeExplanationLanguage = 'en' | 'fr';

const MAX_SOURCE_LINES = 56;
const MAX_ANNOTATED_LINES = 260;

const primarySolutionCode = (solution: string) => {
    const lines = solution.trim().split('\n');
    const isApproachHeading = (line: string) => /^\s*#\s*(?:Using|Script|Direct|Built|Manual|Alternative)\b/i.test(line);
    const functionHeading = lines.findIndex(line => /^\s*#\s*Using function approach\b/i.test(line));
    const leadingImports = lines
        .slice(0, functionHeading >= 0 ? functionHeading : lines.length)
        .filter(line => /^\s*(?:from\s+\S+\s+import\s+|import\s+)/.test(line));

    if (functionHeading >= 0) {
        const section: string[] = [];
        for (let index = functionHeading + 1; index < lines.length; index += 1) {
            if (isApproachHeading(lines[index])) break;
            section.push(lines[index]);
            if (leadingImports.length + section.length >= MAX_SOURCE_LINES) break;
        }
        return [...leadingImports, ...(leadingImports.length ? [''] : []), ...section].join('\n').trim();
    }


    const firstApproachHeading = lines.findIndex(isApproachHeading);
    if (firstApproachHeading >= 0) {
        const imports = lines
            .slice(0, firstApproachHeading)
            .filter(line => /^\s*(?:from\s+\S+\s+import\s+|import\s+)/.test(line));
        const section: string[] = [];
        for (let index = firstApproachHeading + 1; index < lines.length; index += 1) {
            if (isApproachHeading(lines[index])) break;
            section.push(lines[index]);
            if (imports.length + section.length >= MAX_SOURCE_LINES) break;
        }
        return [...imports, ...(imports.length ? [''] : []), ...section].join('\n').trim();
    }

    const start = lines.findIndex(line => /^\s*(?:def|class|from\s+|import\s+|[A-Za-z_]\w*\s*=|print\s*\()/.test(line));
    const selected = start >= 0 ? lines.slice(start) : lines;
    const result: string[] = [];
    for (const line of selected) {
        if (result.length && isApproachHeading(line)) break;
        result.push(line);
        if (result.length >= MAX_SOURCE_LINES) break;
    }
    return result.join('\n').trim();
};

const isUsefulUserCode = (code: string) => {
    const meaningful = code
        .split('\n')
        .map(line => line.trim())
        .filter(line => line && !line.startsWith('#'));
    return meaningful.length > 0 && !meaningful.every(line => line === 'pass');
};

const extractFunctionExample = (code: string) => {
    const definition = code.match(/\bdef\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/);
    if (!definition) return null;
    const [, name, rawParams] = definition;
    const params = rawParams
        .split(',')
        .map(param => param.trim().replace(/^\*{1,2}/, '').split(/[:=]/)[0].trim())
        .filter(Boolean);
    let rawArguments = '';
    for (const line of code.split('\n')) {
        if (new RegExp(`^\\s*def\\s+${name}\\s*\\(`).test(line)) continue;
        const marker = new RegExp(`\\b${name}\\s*\\(`).exec(line);
        if (!marker) continue;
        const openIndex = marker.index + marker[0].lastIndexOf('(');
        let depth = 0;
        let quote = '';
        let escaped = false;
        for (let index = openIndex; index < line.length; index += 1) {
            const char = line[index];
            if (quote) {
                if (escaped) escaped = false;
                else if (char === '\\') escaped = true;
                else if (char === quote) quote = '';
                continue;
            }
            if (char === "'" || char === '"') quote = char;
            else if (char === '(') depth += 1;
            else if (char === ')') {
                depth -= 1;
                if (depth === 0) {
                    rawArguments = line.slice(openIndex + 1, index).trim();
                    break;
                }
            }
        }
        if (rawArguments) break;
    }
    const args = splitTopLevel(rawArguments);
    return { name, params, args };
};

const unquote = (value: string) => {
    const trimmed = value.trim();
    if (
        trimmed.length >= 2
        && ((trimmed.startsWith("'") && trimmed.endsWith("'")) || (trimmed.startsWith('"') && trimmed.endsWith('"')))
    ) {
        return trimmed.slice(1, -1);
    }
    return null;
};

const pythonList = (values: string[]) => `[${values.map(value => JSON.stringify(value)).join(', ')}]`;

const addComment = (target: string[], indent: string, lines: string[]) => {
    for (const line of lines) target.push(line ? `${indent}# ${line}` : '');
};

const quotePythonString = (value: string) => `"${value.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;

const normalizeDisplayLine = (
    line: string,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    let normalized = line.replace(/\.split\(\s*(['"])(.*?)\1\s*\)/g, (_match, _quote, delimiter) => `.split(${quotePythonString(delimiter)})`);
    if (example?.args.length && new RegExp(`\\b${example.name}\\s*\\(`).test(normalized)) {
        const formattedArgs = example.args.map(arg => {
            const value = unquote(arg);
            return value === null ? arg : quotePythonString(value);
        });
        normalized = normalized.replace(
            new RegExp(`\\b${example.name}\\s*\\(([^\\n()]*(?:\\([^\\n()]*\\)[^\\n()]*)*)\\)`),
            `${example.name}(${formattedArgs.join(', ')})`,
        );
    }
    return normalized;
};

type TracedValue = {
    known: boolean;
    value?: unknown;
    type: string;
    operation: string;
};

const unknownValue = (type = 'value', operation = 'Python evaluates the expression at runtime.'): TracedValue => ({
    known: false,
    type,
    operation,
});

const knownValue = (value: unknown, operation: string): TracedValue => {
    let type = typeof value;
    if (value === null) type = 'NoneType';
    else if (Array.isArray(value)) type = 'list';
    else if (value instanceof Set) type = 'set';
    else if (value && typeof value === 'object') type = 'dict';
    else if (type === 'number') type = Number.isInteger(value) ? 'int' : 'float';
    else if (type === 'string') type = 'str';
    else if (type === 'boolean') type = 'bool';
    return { known: true, value, type, operation };
};

const displayValue = (value: unknown): string => {
    if (value === null) return 'None';
    if (typeof value === 'string') return quotePythonString(value);
    if (typeof value === 'boolean') return value ? 'True' : 'False';
    if (value instanceof Set) return `{${[...value].map(displayValue).join(', ')}}`;
    if (Array.isArray(value)) return `[${value.map(displayValue).join(', ')}]`;
    if (value && typeof value === 'object') {
        return `{${Object.entries(value as Record<string, unknown>).map(([key, item]) => `${quotePythonString(key)}: ${displayValue(item)}`).join(', ')}}`;
    }
    return String(value);
};

const splitTopLevel = (text: string, delimiter = ','): string[] => {
    const parts: string[] = [];
    let start = 0;
    let depth = 0;
    let quote = '';
    let escaped = false;
    for (let index = 0; index < text.length; index += 1) {
        const char = text[index];
        if (quote) {
            if (escaped) escaped = false;
            else if (char === '\\') escaped = true;
            else if (char === quote) quote = '';
            continue;
        }
        if (char === "'" || char === '"') quote = char;
        else if ('([{'.includes(char)) depth += 1;
        else if (')]}'.includes(char)) depth -= 1;
        else if (depth === 0 && text.startsWith(delimiter, index)) {
            parts.push(text.slice(start, index).trim());
            start = index + delimiter.length;
            index += delimiter.length - 1;
        }
    }
    parts.push(text.slice(start).trim());
    return parts.filter(Boolean);
};

const stripOuterParentheses = (expression: string) => {
    let text = expression.trim();
    while (text.startsWith('(') && text.endsWith(')')) {
        let depth = 0;
        let closesAtEnd = false;
        for (let index = 0; index < text.length; index += 1) {
            if (text[index] === '(') depth += 1;
            if (text[index] === ')') depth -= 1;
            if (depth === 0) {
                closesAtEnd = index === text.length - 1;
                break;
            }
        }
        if (!closesAtEnd) break;
        text = text.slice(1, -1).trim();
    }
    return text;
};

const findTopLevelOperator = (expression: string, operators: string[]) => {
    let depth = 0;
    let quote = '';
    let escaped = false;
    for (let index = expression.length - 1; index >= 0; index -= 1) {
        const char = expression[index];
        if (quote) {
            if (escaped) escaped = false;
            else if (char === '\\') escaped = true;
            else if (char === quote) quote = '';
            continue;
        }
        if (char === "'" || char === '"') quote = char;
        else if (')]}'.includes(char)) depth += 1;
        else if ('([{'.includes(char)) depth -= 1;
        if (depth !== 0 || quote) continue;
        for (const operator of operators) {
            const start = index - operator.length + 1;
            if (start < 0 || expression.slice(start, index + 1) !== operator) continue;
            const before = expression[start - 1] || ' ';
            const after = expression[index + 1] || ' ';
            if (/^[a-z]+$/i.test(operator) && (/\w/.test(before) || /\w/.test(after))) continue;
            if ((operator === '+' || operator === '-') && start === 0) continue;
            return { index: start, operator };
        }
    }
    return null;
};

const inferExpression = (
    rawExpression: string,
    environment: Map<string, TracedValue>,
    depth = 0,
): TracedValue => {
    if (depth > 10) return unknownValue();
    const expression = stripOuterParentheses(rawExpression.replace(/\s+#.*$/, '').trim());
    if (!expression) return unknownValue();

    if (/^(?:None|True|False)$/.test(expression)) {
        return knownValue(expression === 'None' ? null : expression === 'True', 'Read the literal value directly.');
    }
    if (/^-?\d+(?:\.\d+)?$/.test(expression)) {
        return knownValue(Number(expression), 'Read the numeric literal directly.');
    }
    const stringMatch = expression.match(/^(?:[rubf]{0,2})(['"])([\s\S]*)\1$/i);
    if (stringMatch && !/^f/i.test(expression)) {
        return knownValue(stringMatch[2].replace(/\\n/g, '\n').replace(/\\t/g, '\t'), 'Read the string literal as text.');
    }
    if (/^f(['"])[\s\S]*\1$/i.test(expression)) {
        return unknownValue('str', 'Evaluate each expression inside {...}, convert it to text, and insert it into the formatted string.');
    }
    if (/^not\s+/.test(expression)) {
        const operand = inferExpression(expression.replace(/^not\s+/, ''), environment, depth + 1);
        return operand.known
            ? knownValue(!operand.value, 'Evaluate the operand, convert it to truth, then invert that bool with not.')
            : unknownValue('bool', 'Evaluate the operand, convert it to truth, then invert that bool with not.');
    }
    if (/^[A-Za-z_]\w*$/.test(expression)) {
        return environment.get(expression) || unknownValue('value', `Read the current value stored in ${expression}.`);
    }
    if (/^lambda\b/.test(expression)) return unknownValue('function', 'Create an anonymous function object; its body runs only when called.');

    if (expression.startsWith('[') && expression.endsWith(']')) {
        const body = expression.slice(1, -1).trim();
        if (/\bfor\b/.test(body)) return unknownValue('list', 'Run the list-comprehension expression for each selected item and collect the results.');
        const items = splitTopLevel(body).map(item => inferExpression(item, environment, depth + 1));
        return items.every(item => item.known)
            ? knownValue(items.map(item => item.value), 'Evaluate each item from left to right and collect them in a list.')
            : unknownValue('list', 'Evaluate each item from left to right and collect them in a list.');
    }
    if (expression.startsWith('{') && expression.endsWith('}')) {
        const body = expression.slice(1, -1).trim();
        if (/\bfor\b/.test(body)) return unknownValue(body.includes(':') ? 'dict' : 'set', 'Run the comprehension and collect each generated item.');
        if (!body) return knownValue({}, 'Create an empty dictionary.');
        const items = splitTopLevel(body);
        if (items.every(item => item.includes(':'))) {
            const result: Record<string, unknown> = {};
            let allKnown = true;
            for (const item of items) {
                const pair = splitTopLevel(item, ':');
                const key = inferExpression(pair[0] || '', environment, depth + 1);
                const value = inferExpression(pair.slice(1).join(':') || '', environment, depth + 1);
                if (!key.known || !value.known) allKnown = false;
                else result[String(key.value)] = value.value;
            }
            return allKnown ? knownValue(result, 'Evaluate every key-value pair and build a dictionary.') : unknownValue('dict', 'Evaluate every key-value pair and build a dictionary.');
        }
        const values = items.map(item => inferExpression(item, environment, depth + 1));
        return values.every(item => item.known)
            ? knownValue(new Set(values.map(item => item.value)), 'Evaluate the unique items and build a set.')
            : unknownValue('set', 'Evaluate the unique items and build a set.');
    }
    if (expression.startsWith('(') && expression.endsWith(')') && expression.includes(',')) {
        const items = splitTopLevel(expression.slice(1, -1)).map(item => inferExpression(item, environment, depth + 1));
        return items.every(item => item.known)
            ? { ...knownValue(items.map(item => item.value), 'Evaluate each item and pack the results into a tuple.'), type: 'tuple' }
            : unknownValue('tuple', 'Evaluate each item and pack the results into a tuple.');
    }

    const booleanOperator = findTopLevelOperator(expression, [' or ', ' and ']);
    if (booleanOperator) {
        const left = inferExpression(expression.slice(0, booleanOperator.index), environment, depth + 1);
        const right = inferExpression(expression.slice(booleanOperator.index + booleanOperator.operator.length), environment, depth + 1);
        if (left.known && right.known) {
            const value = booleanOperator.operator.trim() === 'or' ? (left.value || right.value) : (left.value && right.value);
            return knownValue(value, `Evaluate the left side first, then short-circuit ${booleanOperator.operator.trim()} when possible.`);
        }
        return unknownValue('bool', `Evaluate the left side first, then short-circuit ${booleanOperator.operator.trim()} when possible.`);
    }

    const comparison = findTopLevelOperator(expression, ['==', '!=', '>=', '<=', ' is ', ' in ', '>', '<']);
    if (comparison) {
        const left = inferExpression(expression.slice(0, comparison.index), environment, depth + 1);
        const right = inferExpression(expression.slice(comparison.index + comparison.operator.length), environment, depth + 1);
        if (left.known && right.known) {
            const operator = comparison.operator.trim();
            let value = false;
            if (operator === '==') value = left.value === right.value;
            else if (operator === '!=') value = left.value !== right.value;
            else if (operator === '>') value = (left.value as number) > (right.value as number);
            else if (operator === '<') value = (left.value as number) < (right.value as number);
            else if (operator === '>=') value = (left.value as number) >= (right.value as number);
            else if (operator === '<=') value = (left.value as number) <= (right.value as number);
            else if (operator === 'is') value = left.value === right.value;
            else if (operator === 'in') value = Array.isArray(right.value) ? right.value.includes(left.value) : String(right.value).includes(String(left.value));
            return knownValue(value, `Compare the two evaluated operands with ${operator}; comparisons produce bool.`);
        }
        return unknownValue('bool', `Compare the two evaluated operands with ${comparison.operator.trim()}; comparisons produce bool.`);
    }

    const arithmetic = findTopLevelOperator(expression, ['**', '//', '%', '+', '-', '*', '/']);
    if (arithmetic) {
        const left = inferExpression(expression.slice(0, arithmetic.index), environment, depth + 1);
        const right = inferExpression(expression.slice(arithmetic.index + arithmetic.operator.length), environment, depth + 1);
        const operation = `Evaluate both operands, then apply ${arithmetic.operator}.`;
        if (left.known && right.known) {
            try {
                let value: unknown;
                if (arithmetic.operator === '+') value = (left.value as number) + (right.value as number);
                else if (arithmetic.operator === '-') value = (left.value as number) - (right.value as number);
                else if (arithmetic.operator === '*') value = typeof left.value === 'string' ? left.value.repeat(Number(right.value)) : (left.value as number) * (right.value as number);
                else if (arithmetic.operator === '/') value = (left.value as number) / (right.value as number);
                else if (arithmetic.operator === '//') value = Math.floor((left.value as number) / (right.value as number));
                else if (arithmetic.operator === '%') value = (left.value as number) % (right.value as number);
                else value = (left.value as number) ** (right.value as number);
                return knownValue(value, operation);
            } catch { /* Keep the conservative inferred type below. */ }
        }
        return unknownValue(arithmetic.operator === '/' ? 'float' : left.type === 'str' ? 'str' : 'number', operation);
    }

    const method = expression.match(/^((?:[A-Za-z_]\w*|[A-Za-z_]\w*\([^()]*\))(?:\[[^\]]+\])?)\.([A-Za-z_]\w*)\((.*)\)$/s);
    if (method) {
        const target = inferExpression(method[1], environment, depth + 1);
        const args = splitTopLevel(method[3]).map(arg => inferExpression(arg, environment, depth + 1));
        const name = method[2];
        const operation = `Evaluate ${method[1]}, then call its .${name}() method.`;
        if (target.known && args.every(arg => arg.known)) {
            const value = target.value;
            const rawArgs = args.map(arg => arg.value);
            try {
                if (typeof value === 'string') {
                    if (name === 'split') return knownValue(value.split(String(rawArgs[0] ?? ' ')), operation);
                    if (name === 'rsplit') {
                        const delimiter = String(rawArgs[0] ?? ' ');
                        const pieces = value.split(delimiter);
                        const count = Number(rawArgs[1] ?? -1);
                        return knownValue(count < 0 || pieces.length <= count + 1 ? pieces : [pieces.slice(0, pieces.length - count).join(delimiter), ...pieces.slice(-count)], operation);
                    }
                    if (name === 'join' && Array.isArray(rawArgs[0])) return knownValue(rawArgs[0].join(value), operation);
                    if (name === 'count') return knownValue(value.split(String(rawArgs[0])).length - 1, operation);
                    if (name === 'lower') return knownValue(value.toLowerCase(), operation);
                    if (name === 'upper') return knownValue(value.toUpperCase(), operation);
                    if (name === 'strip') return knownValue(value.trim(), operation);
                    if (name === 'replace') return knownValue(value.split(String(rawArgs[0])).join(String(rawArgs[1] ?? '')), operation);
                    if (name === 'isdigit') return knownValue(/^\d+$/.test(value), operation);
                    if (name === 'isalpha') return knownValue(/^[A-Za-z]+$/.test(value), operation);
                    if (name === 'isalnum') return knownValue(/^[A-Za-z0-9]+$/.test(value), operation);
                    if (name === 'startswith') return knownValue(value.startsWith(String(rawArgs[0])), operation);
                    if (name === 'endswith') return knownValue(value.endsWith(String(rawArgs[0])), operation);
                }
                if (value && typeof value === 'object' && !Array.isArray(value)) {
                    const record = value as Record<string, unknown>;
                    if (name === 'get') return knownValue(record[String(rawArgs[0])] ?? rawArgs[1] ?? null, operation);
                    if (name === 'keys') return knownValue(Object.keys(record), operation);
                    if (name === 'values') return knownValue(Object.values(record), operation);
                    if (name === 'items') return knownValue(Object.entries(record), operation);
                }
                if (Array.isArray(value) && name === 'count') return knownValue(value.filter(item => item === rawArgs[0]).length, operation);
                if (Array.isArray(value) && name === 'copy') return knownValue([...value], operation);
            } catch { /* Keep the conservative method return type below. */ }
        }
        const booleanMethods = /^(?:isdigit|isalpha|isalnum|islower|isupper|isspace|startswith|endswith)$/;
        const listMethods = /^(?:split|rsplit|keys|values|items|copy)$/;
        const mutatingMethods = /^(?:append|extend|insert|remove|sort|reverse|update|add|discard)$/;
        return unknownValue(booleanMethods.test(name) ? 'bool' : listMethods.test(name) ? 'list' : mutatingMethods.test(name) ? 'NoneType' : 'value', operation);
    }

    const call = expression.match(/^([A-Za-z_][\w.]*)\((.*)\)$/s);
    if (call) {
        const name = call[1];
        const args = splitTopLevel(call[2]).map(arg => inferExpression(arg.replace(/^\w+\s*=\s*/, ''), environment, depth + 1));
        const operation = `Evaluate the arguments from left to right, then call ${name}().`;
        const functionModel = environment.get(`@function:${name}`);
        if (functionModel?.known && functionModel.value && typeof functionModel.value === 'object') {
            const model = functionModel.value as { params: string[]; expression: string };
            const callEnvironment = new Map(environment);
            model.params.forEach((param, index) => {
                if (args[index]) callEnvironment.set(param, args[index]);
            });
            const result = inferExpression(model.expression, callEnvironment, depth + 1);
            return {
                ...result,
                operation: `${operation} Substitute this call's arguments into the function body and evaluate its return expression.`,
            };
        }
        const inferredFunctionReturn = environment.get(`@return:${name}`);
        if (inferredFunctionReturn) {
            return {
                ...inferredFunctionReturn,
                operation: `${operation} The function body produces the traced return value.`,
            };
        }
        if (args.every(arg => arg.known)) {
            const values = args.map(arg => arg.value);
            try {
                if (name === 'str') return knownValue(String(values[0]), operation);
                if (name === 'int') return knownValue(Number.parseInt(String(values[0]), 10), operation);
                if (name === 'float') return knownValue(Number.parseFloat(String(values[0])), operation);
                if (name === 'bool') return knownValue(Boolean(values[0]), operation);
                if (name === 'len' && values[0] != null) return knownValue((values[0] as { length?: number }).length ?? Object.keys(values[0] as object).length, operation);
                if (name === 'sum' && Array.isArray(values[0])) return knownValue(values[0].reduce((total: number, item) => total + Number(item), Number(values[1] || 0)), operation);
                if (name === 'min' && Array.isArray(values[0])) return knownValue(Math.min(...values[0].map(Number)), operation);
                if (name === 'max' && Array.isArray(values[0])) return knownValue(Math.max(...values[0].map(Number)), operation);
                if (name === 'abs') return knownValue(Math.abs(Number(values[0])), operation);
                if (name === 'round') {
                    const places = Number(values[1] || 0);
                    const factor = 10 ** places;
                    return knownValue(Math.round(Number(values[0]) * factor) / factor, operation);
                }
                if (name === 'pow') return knownValue(Number(values[0]) ** Number(values[1]), operation);
                if (name === 'list') return knownValue(Array.isArray(values[0]) ? [...values[0]] : [...String(values[0] ?? '')], operation);
                if (name === 'tuple') return { ...knownValue(Array.isArray(values[0]) ? [...values[0]] : [values[0]], operation), type: 'tuple' };
                if (name === 'set') return knownValue(new Set(Array.isArray(values[0]) ? values[0] : String(values[0] ?? '')), operation);
                if (name === 'sorted' && Array.isArray(values[0])) return knownValue([...values[0]].sort(), operation);
                if (name === 'all' && Array.isArray(values[0])) return knownValue(values[0].every(Boolean), operation);
                if (name === 'any' && Array.isArray(values[0])) return knownValue(values[0].some(Boolean), operation);
            } catch { /* Keep the inferred call type below. */ }
        }
        const knownTypes: Record<string, string> = {
            str: 'str', int: 'int', float: 'float', bool: 'bool', len: 'int', sum: 'number', min: 'value', max: 'value',
            abs: 'number', round: 'number', pow: 'number', list: 'list', tuple: 'tuple', set: 'set', dict: 'dict',
            sorted: 'list', range: 'range', enumerate: 'enumerate', zip: 'zip', map: 'map iterator', filter: 'filter iterator',
            all: 'bool', any: 'bool', print: 'NoneType', input: 'str',
        };
        return unknownValue(knownTypes[name] || 'value', operation);
    }

    const index = expression.match(/^([A-Za-z_]\w*)\[([^\]]+)\]$/);
    if (index) {
        const target = environment.get(index[1]);
        const accessor = index[2].trim();
        if (target?.known) {
            if (accessor.includes(':')) {
                const parts = accessor.split(':').map(item => item.trim() ? inferExpression(item.trim(), environment, depth + 1) : knownValue(undefined, 'Use the default slice boundary.'));
                if (typeof target.value === 'string' || Array.isArray(target.value)) {
                    const sequence = target.value as string | unknown[];
                    if (parts.every(part => part.known)) {
                        const start = parts[0]?.value as number | undefined;
                        const stop = parts[1]?.value as number | undefined;
                        const step = parts[2]?.value as number | undefined;
                        if (step === -1) return knownValue(typeof sequence === 'string' ? sequence.split('').reverse().join('') : [...sequence].reverse(), 'Apply the slice from start to stop using the requested step.');
                        if (step === undefined || step === 1) return knownValue(sequence.slice(start, stop), 'Apply the slice; the stop position is excluded.');
                    }
                }
            } else {
                const key = inferExpression(accessor, environment, depth + 1);
                if (key.known) {
                    const value = target.value as Record<string, unknown> | unknown[] | string;
                    const numericKey = Number(key.value);
                    const resolvedKey = numericKey < 0 && (typeof value === 'string' || Array.isArray(value)) ? value.length + numericKey : key.value as never;
                    return knownValue((value as never)[resolvedKey], 'Evaluate the index/key and retrieve that one item.');
                }
            }
        }
        return unknownValue(accessor.includes(':') ? target?.type || 'sequence' : 'item', accessor.includes(':') ? 'Apply the slice to create a selected subsequence.' : 'Use the index or key to retrieve one item.');
    }

    return unknownValue('value', 'Evaluate this Python expression using the current variables.');
};

const localizedTraceText = (text: string, language: AiCodeExplanationLanguage) => {
    if (language === 'en') return text;
    return text
        .replace('Read the literal value directly.', 'Lire directement la valeur littérale.')
        .replace('Read the numeric literal directly.', 'Lire directement le nombre littéral.')
        .replace('Read the string literal as text.', 'Lire directement la chaîne comme texte.')
        .replace(/^Read the current value stored in (.+)\.$/, 'Lire la valeur actuelle stockée dans $1.')
        .replace('Evaluate both operands, then apply', 'Évaluer les deux opérandes, puis appliquer')
        .replace(/^Evaluate the arguments from left to right, then call (.+)\.$/, 'Évaluer les arguments de gauche à droite, puis appeler $1.')
        .replace(/^Evaluate (.+), then call its (.+) method\.$/, 'Évaluer $1, puis appeler sa méthode $2.')
        .replace('Evaluate each item from left to right and collect them in a list.', 'Évaluer chaque élément de gauche à droite et les rassembler dans une liste.')
        .replace('Evaluate every key-value pair and build a dictionary.', 'Évaluer chaque paire clé-valeur et construire un dictionnaire.')
        .replace('Use the index or key to retrieve one item.', 'Utiliser l’indice ou la clé pour récupérer un élément.')
        .replace('Apply the slice to create a selected subsequence.', 'Appliquer la tranche pour créer une sous-séquence.')
        .replace('Python evaluates the expression at runtime.', 'Python évalue cette expression pendant l’exécution.')
        .replace('Evaluate this Python expression using the current variables.', 'Évaluer cette expression Python avec les variables actuelles.');
};

const buildUniversalExecutionTrace = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    const environment = new Map<string, TracedValue>();
    for (const line of code.split('\n')) {
        if (/^\s/.test(line)) continue;
        const assignment = line.trim().replace(/\s+#.*$/, '').match(/^([A-Za-z_]\w*)\s*=\s*(.+)$/s);
        if (!assignment) continue;
        const value = inferExpression(assignment[2], environment);
        if (value.known) environment.set(assignment[1], value);
    }
    example?.params.forEach((param, index) => {
        const argument = example.args[index];
        if (argument) environment.set(param, inferExpression(argument, environment));
    });
    const steps: string[] = [];
    let stepNumber = 0;
    let currentFunction = '';
    let currentFunctionParams: string[] = [];
    const lines = code.split('\n').slice(0, MAX_SOURCE_LINES);

    lines.forEach((line, index) => {
        const trimmed = line.trim().replace(/\s+#.*$/, '');
        if (!trimmed) return;
        const definition = trimmed.match(/^def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/);
        if (definition) {
            currentFunction = definition[1];
            currentFunctionParams = splitTopLevel(definition[2]).map(param => param.trim().replace(/^\*{1,2}/, '').split(/[:=]/)[0].trim()).filter(Boolean);
            return;
        }
        if (!/^\s/.test(line) && !/^(?:@|def\b|class\b)/.test(trimmed)) {
            currentFunction = '';
            currentFunctionParams = [];
        }
        if (/^(?:class|from\s+|import\s+|global\b|nonlocal\b|pass$)/.test(trimmed)) return;
        let label = trimmed;
        let trace: TracedValue | null = null;
        let destination = '';

        const assignment = trimmed.match(/^([A-Za-z_]\w*)\s*=\s*(.+)$/s);
        const unpacking = !assignment && trimmed.match(/^([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)+)\s*=\s*(.+)$/s);
        const targetAssignment = !assignment && !unpacking && trimmed.match(/^((?:self\.)?[A-Za-z_]\w*(?:\[[^\]]+\]|\.[A-Za-z_]\w*)+)\s*=\s*(?!=)(.+)$/s);
        const augmentedAssignment = !assignment && !unpacking && !targetAssignment && trimmed.match(/^(.+?)\s*(\+=|-=|\*=|\/=|\/\/=|%=|\*\*=)\s*(.+)$/s);
        if (assignment) {
            destination = assignment[1];
            trace = inferExpression(assignment[2], environment);
            environment.set(destination, trace);
        } else if (unpacking) {
            trace = inferExpression(unpacking[2], environment);
            const names = unpacking[1].split(',').map(name => name.trim());
            if (trace.known && Array.isArray(trace.value)) names.forEach((name, itemIndex) => environment.set(name, knownValue(trace!.value![itemIndex], 'Unpack the matching item by position.')));
            else names.forEach(name => environment.set(name, unknownValue('item', 'Unpack the matching item by position.')));
            destination = names.join(', ');
        } else if (targetAssignment) {
            destination = targetAssignment[1];
            trace = inferExpression(targetAssignment[2], environment);
            trace = { ...trace, operation: `Evaluate the right-hand expression, then store it at ${destination}.` };
        } else if (augmentedAssignment) {
            destination = augmentedAssignment[1];
            trace = inferExpression(`${augmentedAssignment[1]} ${augmentedAssignment[2].slice(0, -1)} ${augmentedAssignment[3]}`, environment);
            if (/^[A-Za-z_]\w*$/.test(destination)) environment.set(destination, trace);
            trace = { ...trace, operation: `Read ${destination}, apply ${augmentedAssignment[2].slice(0, -1)}, then store the updated value back in the same place.` };
        } else if (/^return\b/.test(trimmed)) {
            label = trimmed.replace(/^return\s*/, '');
            trace = inferExpression(label, environment);
            destination = fr ? 'valeur renvoyée' : 'returned value';
            if (currentFunction) {
                environment.set(`@return:${currentFunction}`, trace);
                environment.set(`@function:${currentFunction}`, knownValue({ params: currentFunctionParams, expression: label }, 'Store the function return expression for its later calls.'));
            }
        } else if (/^print\s*\(/.test(trimmed)) {
            const printedExpression = trimmed.replace(/^print\s*\(/, '').replace(/\)\s*$/, '');
            const printedItems = splitTopLevel(printedExpression).map(item => inferExpression(item, environment));
            trace = printedItems.length === 1
                ? { ...printedItems[0], operation: `Evaluate the value, convert it to display text, then write it to the output panel.` }
                : printedItems.every(item => item.known)
                    ? { ...knownValue(printedItems.map(item => displayValue(item.value)).join(' '), 'Evaluate every print argument from left to right, separate them with spaces, and display them.'), type: 'display text' }
                    : unknownValue('display text', 'Evaluate every print argument from left to right, separate them with spaces, and display them.');
            destination = fr ? 'sortie affichée' : 'printed output';
        } else if (/^(?:if|elif|while)\b/.test(trimmed)) {
            const condition = trimmed.replace(/^(?:if|elif|while)\s+/, '').replace(/:\s*$/, '');
            trace = inferExpression(condition, environment);
            destination = fr ? 'résultat de la condition' : 'condition result';
        } else if (/^for\b/.test(trimmed)) {
            const iterable = trimmed.match(/\bin\s+(.+):$/)?.[1] || '';
            trace = inferExpression(iterable, environment);
            destination = fr ? 'itérable de la boucle' : 'loop iterable';
        } else if (/^yield\b/.test(trimmed)) {
            const yielded = trimmed.replace(/^yield(?:\s+from)?\s*/, '');
            trace = inferExpression(yielded, environment);
            destination = fr ? 'valeur produite' : 'yielded value';
            trace = { ...trace, operation: 'Pause the generator, send this value to its caller, and preserve local state for the next iteration.' };
        } else if (/^(?:raise|assert|del)\b/.test(trimmed)) {
            const keyword = trimmed.match(/^\w+/)?.[0] || 'statement';
            trace = unknownValue(keyword === 'assert' ? 'bool check' : 'control-flow effect', `${keyword} changes normal execution: it checks, raises, or removes the named value.`);
            destination = fr ? 'effet de contrôle' : 'control-flow effect';
        } else if (/^(?:with|try|except|finally)\b/.test(trimmed)) {
            trace = unknownValue('control-flow block', 'Enter the protected block and follow its resource-management or error-handling rules.');
            destination = fr ? 'bloc de contrôle' : 'control-flow block';
        } else if (/\.[A-Za-z_]\w*\s*\(/.test(trimmed)) {
            trace = inferExpression(trimmed, environment);
            destination = fr ? 'effet de la méthode' : 'method effect';
        } else if (/^[A-Za-z_][\w.]*\s*\(/.test(trimmed)) {
            trace = inferExpression(trimmed, environment);
            destination = fr ? 'résultat de l’appel' : 'call result';
        }

        if (!trace) return;
        const result = trace.known
            ? `${destination} = ${displayValue(trace.value)} (${trace.type})`
            : `${destination}: ${trace.type}${fr ? ' déterminé pendant l’exécution' : ' determined at runtime'}`;
        stepNumber += 1;
        steps.push(
            `${fr ? 'Étape' : 'Step'} ${stepNumber} — ${fr ? 'ligne' : 'line'} ${index + 1}: ${label}`,
            `${fr ? 'Opération' : 'Operation'}: ${localizedTraceText(trace.operation, language)}`,
            `${fr ? 'Valeur intermédiaire et type' : 'Intermediate value and type'}: ${result}`,
            '',
        );
    });
    return steps.slice(0, 18 * 4);
};

const lineExplanation = (
    trimmed: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    const definition = trimmed.match(/^def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*:/);
    if (definition) {
        const params = definition[2].trim();
        return [
            fr
                ? `Cette fonction reçoit ${params ? `les données ${params}` : 'aucun argument'}.`
                : `This function takes ${params ? `the input ${params}` : 'no arguments'}.`,
        ].filter(Boolean);
    }
    if (/^class\s+/.test(trimmed)) {
        return [fr ? 'Cette classe définit un nouveau type d’objet et regroupe ses données et ses méthodes.' : 'This class defines a new object type and groups its data and methods.'];
    }
    if (/^(?:from|import)\s+/.test(trimmed)) {
        return [fr ? 'Cette ligne charge un outil Python utilisé plus bas dans le programme.' : 'This line loads a Python tool used later in the program.'];
    }
    if (/^return\b/.test(trimmed)) {
        return [fr ? 'return renvoie le résultat final à l’appelant et au correcteur.' : 'return sends the final result back to the caller and grader.'];
    }
    if (/^print\s*\(/.test(trimmed)) {
        return [fr ? 'print(...) appelle la fonction et affiche le résultat dans la sortie.' : 'print(...) calls the function and displays the result in the output panel.'];
    }
    if (/^(?:for|while)\b/.test(trimmed)) {
        return [fr ? 'Cette boucle répète le bloc indenté ; les lignes décalées dessous appartiennent à la boucle.' : 'This loop repeats the indented block; the shifted lines below belong to the loop.'];
    }
    if (/^(?:if|elif|else)\b/.test(trimmed)) {
        return [fr ? 'Cette condition choisit quelle branche indentée doit s’exécuter.' : 'This condition chooses which indented branch should run.'];
    }
    if (/^with\b/.test(trimmed)) {
        return [fr ? 'Le bloc `with` gère automatiquement l’ouverture et le nettoyage de la ressource.' : 'The `with` block automatically manages opening and cleaning up the resource.'];
    }
    if (/^try\s*:|^except\b/.test(trimmed)) {
        return [fr ? 'Ce bloc exécute une opération risquée et traite une erreur prévue.' : 'This block runs a risky operation and handles an expected error.'];
    }
    if (/^[A-Za-z_]\w*\s*=/.test(trimmed)) {
        const name = trimmed.match(/^([A-Za-z_]\w*)/)?.[1] || 'value';
        return [fr ? `Cette ligne calcule une valeur et la conserve dans la variable \`${name}\`.` : `This line calculates a value and stores it in the variable \`${name}\`.`];
    }
    if (trimmed === 'pass') {
        return [fr ? 'pass est seulement un emplacement vide ; il ne résout pas encore le problème.' : 'pass is only an empty placeholder; it does not solve the problem yet.'];
    }
    return [fr ? 'Python exécute cette instruction à cet endroit du programme.' : 'Python executes this statement at this point in the program.'];
};

const functionIntroduction = (
    code: string,
    params: string,
    language: AiCodeExplanationLanguage,
) => {
    const fr = language === 'fr';
    const splitDelimiter = code.match(/\.split\(\s*(['"])(.*?)\1\s*\)/)?.[2];
    if (splitDelimiter !== undefined && /\bmap\s*\(\s*int\s*,/.test(code)) {
        const separator = splitDelimiter === ','
            ? (fr ? 'des virgules' : 'commas')
            : (fr ? `le séparateur ${quotePythonString(splitDelimiter)}` : `the ${quotePythonString(splitDelimiter)} delimiter`);
        return fr
            ? `Cette fonction prend une chaîne contenant des nombres séparés par ${separator}.`
            : `This function takes one string containing numbers separated by ${separator}.`;
    }
    if (/\.split\s*\(/.test(code)) {
        return fr
            ? 'Cette fonction prend une chaîne et la découpe en plusieurs parties.'
            : 'This function takes one string and splits it into separate parts.';
    }
    if (/\b(?:for|while)\b/.test(code)) {
        return fr
            ? `Cette fonction traite ${params || 'les données reçues'} étape par étape avec une boucle.`
            : `This function processes ${params || 'its input data'} step by step with a loop.`;
    }
    if (/\bif\b/.test(code)) {
        return fr
            ? `Cette fonction examine ${params || 'les données reçues'} et choisit un résultat selon une condition.`
            : `This function checks ${params || 'its input data'} and chooses a result using a condition.`;
    }
    return fr
        ? `Cette fonction reçoit ${params || 'les données nécessaires'} et renvoie le résultat demandé.`
        : `This function takes ${params || 'the required input data'} and returns the requested result.`;
};

const buildExpandedOperationLesson = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    const comments: string[] = [];
    const add = (...lines: string[]) => comments.push(...lines);
    const argumentByParam = new Map<string, string>();
    example?.params.forEach((param, index) => {
        if (example.args[index]) argumentByParam.set(param, example.args[index]);
    });

    const splitMatch = code.match(/([A-Za-z_]\w*)\.split\(\s*(['"])(.*?)\2\s*\)/);
    if (splitMatch) {
        const [, variable, , delimiter] = splitMatch;
        const rawValue = argumentByParam.get(variable);
        const textValue = rawValue ? unquote(rawValue) : null;
        add(
            fr
                ? `${variable}.split(${quotePythonString(delimiter)}) découpe la grande chaîne chaque fois qu’il trouve ${quotePythonString(delimiter)}.`
                : `${variable}.split(${quotePythonString(delimiter)}) splits the one big string wherever it finds ${quotePythonString(delimiter)}.`,
        );
        if (textValue !== null) {
            const pieces = textValue.split(delimiter);
            add(
                '',
                fr ? 'Cela transforme :' : 'This changes:',
                quotePythonString(textValue),
                '',
                fr ? 'en :' : 'into:',
                pythonList(pieces),
                '',
                fr ? 'Important :' : 'Important:',
                fr ? 'Ces éléments sont encore des chaînes, pas des entiers.' : 'These are still strings, not integers.',
            );
        }
    }

    const mapMatch = code.match(/\bmap\(\s*([A-Za-z_]\w*)\s*,/);
    if (mapMatch) {
        const converter = mapMatch[1];
        add(
            '',
            fr
                ? `map(${converter}, ...) applique ${converter}() à chaque élément.`
                : `map(${converter}, ...) applies ${converter}() to every item.`,
        );
        if (converter === 'int' && splitMatch) {
            const rawValue = argumentByParam.get(splitMatch[1]);
            const textValue = rawValue ? unquote(rawValue) : null;
            if (textValue !== null) {
                const pieces = textValue.split(splitMatch[3]);
                const converted = pieces.map(piece => Number.parseInt(piece, 10)).filter(value => Number.isFinite(value));
                add(
                    '',
                    ...pieces.slice(0, 5).map((piece, index) => `int(${JSON.stringify(piece)}) -> ${converted[index]}`),
                    '',
                    fr
                        ? 'Ainsi map() convertit chaque chaîne ressemblant à un nombre en véritable entier.'
                        : 'So map() is converting each number-like string into a real integer.',
                );
            }
        }
    }

    if (/\blist\s*\(/.test(code)) {
        add(
            '',
            fr ? 'list(...) rassemble tous les entiers convertis dans une seule liste.' : 'list(...) collects all the converted integers into one list.',
        );
    }
    if (/\bfilter\s*\(/.test(code)) add('', fr ? 'filter(...) teste chaque élément et conserve seulement ceux dont le résultat est vrai.' : 'filter(...) tests every item and keeps only the ones whose result is true.');
    if (/\bsorted\s*\(/.test(code)) add('', fr ? 'sorted(...) lit toutes les valeurs et crée une nouvelle liste triée sans modifier l’original.' : 'sorted(...) reads all the values and creates a new sorted list without changing the original.');
    if (/\bsum\s*\(/.test(code)) add('', fr ? 'sum(...) parcourt les valeurs numériques et les additionne pour produire un total.' : 'sum(...) walks through the numeric values and adds them to produce one total.');
    if (/\blen\s*\(/.test(code)) add('', fr ? 'len(...) compte le nombre d’éléments et renvoie ce nombre comme entier.' : 'len(...) counts the items and returns that count as an integer.');
    if (/\brange\s*\(/.test(code)) add('', fr ? 'range(...) produit les nombres que la boucle traitera, dans l’ordre.' : 'range(...) produces the numbers that the loop will process, in order.');
    if (/\[[^\]]*:[^\]]*\]/.test(code)) add('', fr ? 'La syntaxe [début:fin:pas] extrait une tranche ; la position fin est exclue.' : 'The [start:stop:step] syntax extracts a slice; the stop position is excluded.');
    if (/\[-1\]/.test(code)) add('', fr ? '[-1] sélectionne le dernier élément de la séquence.' : '[-1] selects the final item in the sequence.');
    if (/\[[^\]]+\bfor\b[^\]]+\bin\b[^\]]+\]/.test(code)) add('', fr ? 'La compréhension de liste construit une nouvelle liste en transformant chaque élément.' : 'The list comprehension builds a new list by transforming each item.');
    if (/\.\s*(?:append|extend|insert|remove|pop|sort|reverse)\s*\(/.test(code)) add('', fr ? 'Cette méthode modifie directement la liste existante.' : 'This method changes the existing list directly.');
    if (/\.\s*(?:get|keys|values|items)\s*\(/.test(code)) add('', fr ? 'Cette méthode lit une partie précise du dictionnaire : clés, valeurs ou paires clé-valeur.' : 'This method reads a specific view of the dictionary: keys, values, or key-value pairs.');
    if (/\blambda\b/.test(code)) add('', fr ? 'lambda crée une petite fonction anonyme dont l’expression devient automatiquement le résultat.' : 'lambda creates a small anonymous function whose expression automatically becomes its result.');

    return comments;
};

const buildConcreteTransformation = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    const lines: string[] = [];
    const argumentByParam = new Map<string, string>();
    example?.params.forEach((param, index) => {
        if (example.args[index]) argumentByParam.set(param, example.args[index]);
    });
    const splitMatch = code.match(/([A-Za-z_]\w*)\.split\(\s*(['"])(.*?)\2\s*\)/);
    const mapMatch = code.match(/\bmap\(\s*([A-Za-z_]\w*)\s*,/);
    if (!splitMatch) return lines;

    const rawValue = argumentByParam.get(splitMatch[1]);
    const textValue = rawValue ? unquote(rawValue) : null;
    if (textValue === null) return lines;
    const delimiter = splitMatch[3];
    const pieces = textValue.split(delimiter);
    const converted = mapMatch?.[1] === 'int'
        ? pieces.map(piece => Number.parseInt(piece, 10))
        : mapMatch?.[1] === 'float'
            ? pieces.map(piece => Number.parseFloat(piece))
            : [];

    lines.push(
        fr ? 'La transformation complète ressemble à ceci :' : 'The full transformation looks like this:',
        '',
        quotePythonString(textValue),
        '',
        `       ${fr ? '↓' : '↓'} ${splitMatch[1]}.split(${quotePythonString(delimiter)})`,
        '',
        pythonList(pieces),
    );
    if (mapMatch) {
        lines.push('', `       ↓ map(${mapMatch[1]}, ...)`, '');
        lines.push(converted.length ? converted.join(', ') : fr ? 'valeurs transformées' : 'transformed values');
    }
    if (/\blist\s*\(/.test(code)) {
        lines.push('', '       ↓ list(...)', '');
        lines.push(converted.length ? `[${converted.join(', ')}]` : fr ? 'liste finale' : 'final list');
    }
    return lines;
};

const buildTypeContrast = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    if (!/\bmap\s*\(\s*int\s*,/.test(code)) return [];
    const splitMatch = code.match(/([A-Za-z_]\w*)\.split\(\s*(['"])(.*?)\2\s*\)/);
    const rawValue = splitMatch && example
        ? example.args[example.params.indexOf(splitMatch[1])]
        : '';
    const textValue = rawValue ? unquote(rawValue) : null;
    const sample = textValue?.split(splitMatch?.[3] || ',')[0] || '10';
    const numeric = Number.parseInt(sample, 10);
    if (!Number.isFinite(numeric)) return [];
    return fr
        ? [
            'La différence importante est :',
            '',
            `${quotePythonString(sample)} est une chaîne.`,
            `${numeric} est un entier.`,
            '',
            'Une chaîne est du texte :',
            `${quotePythonString(sample)} + ${quotePythonString(sample)} donne ${quotePythonString(sample + sample)}`,
            '',
            'Un entier est un nombre :',
            `${numeric} + ${numeric} donne ${numeric + numeric}`,
        ]
        : [
            'The important difference is:',
            '',
            `${quotePythonString(sample)} is a string.`,
            `${numeric} is an integer.`,
            '',
            'A string is text:',
            `${quotePythonString(sample)} + ${quotePythonString(sample)} gives ${quotePythonString(sample + sample)}`,
            '',
            'An integer is a number:',
            `${numeric} + ${numeric} gives ${numeric + numeric}`,
        ];
};

const transformationSummary = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    if (/\.split\s*\(/.test(code) && /\bmap\s*\(\s*int\s*,/.test(code) && /\blist\s*\(/.test(code)) {
        return fr
            ? [
                'Découper une chaîne en morceaux séparés.',
                'Convertir chaque morceau de chaîne en entier.',
                'Rassembler ces entiers dans une liste.',
            ]
            : [
                'Splitting one string into separate pieces.',
                'Converting each piece from a string into an integer.',
                'Collecting those integers into a list.',
            ];
    }
    const steps: string[] = [];
    if (/\.split\s*\(/.test(code)) steps.push(fr ? 'La chaîne est découpée en éléments séparés.' : 'The string is split into separate pieces.');
    if (/\bmap\s*\(\s*int\s*,/.test(code) || /\bint\s*\(/.test(code)) steps.push(fr ? 'Les morceaux numériques sont convertis du texte vers des entiers.' : 'Number-like pieces are converted from text into integers.');
    if (/\bmap\s*\(\s*float\s*,/.test(code) || /\bfloat\s*\(/.test(code)) steps.push(fr ? 'Les morceaux numériques sont convertis en nombres décimaux.' : 'Number-like pieces are converted into decimal numbers.');
    if (/\bfilter\s*\(|\bif\b/.test(code)) steps.push(fr ? 'Une condition décide quelles valeurs sont conservées.' : 'A condition decides which values are kept.');
    if (/\b(?:for|while)\b/.test(code)) steps.push(fr ? 'La boucle traite les valeurs dans l’ordre.' : 'The loop processes the values in order.');
    if (/\bsorted\s*\(|\.sort\s*\(/.test(code)) steps.push(fr ? 'Les valeurs sont placées dans l’ordre demandé.' : 'The values are placed in the required order.');
    if (/\blist\s*\(|\[[^\]]+\bfor\b/.test(code)) steps.push(fr ? 'Les résultats sont regroupés dans une liste.' : 'The results are collected into a list.');
    if (!steps.length) steps.push(fr ? 'Python exécute les lignes de haut en bas et produit le résultat final.' : 'Python runs the lines from top to bottom and produces the final result.');
    return steps.slice(0, 8);
};

export const buildDetailedCodeExplanation = (
    userCode: string,
    solution: string,
    language: AiCodeExplanationLanguage = 'en',
) => {
    const source = (isUsefulUserCode(userCode) ? userCode.trim() : primarySolutionCode(solution)).trim();
    const fr = language === 'fr';
    if (!source) {
        return fr
            ? 'Explication du code : aucun code n’est encore disponible. Écrivez ou exécutez une solution pour obtenir une explication ligne par ligne.'
            : 'Code explanation: No code is available yet. Write or run a solution to receive a line-by-line explanation.';
    }

    const example = extractFunctionExample(source) || extractFunctionExample(primarySolutionCode(solution));
    const annotated: string[] = [];
    const sourceLines = source.split('\n').slice(0, MAX_SOURCE_LINES);
    const expandedLesson = buildExpandedOperationLesson(source, language, example);
    let lessonInserted = false;

    for (const line of sourceLines) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith('#')) {
            if (annotated.length && annotated[annotated.length - 1] !== '') annotated.push('');
            continue;
        }
        const indent = line.match(/^\s*/)?.[0] || '';
        const definition = trimmed.match(/^def\s+[A-Za-z_]\w*\s*\(([^)]*)\)\s*:/);
        if (definition) {
            addComment(annotated, indent, [functionIntroduction(source, definition[1].trim(), language)]);
            annotated.push(line);
            if (example?.args.length) {
                const formattedArgs = example.args.map(arg => {
                    const unquoted = unquote(arg);
                    return unquoted === null ? arg : quotePythonString(unquoted);
                });
                annotated.push('');
                addComment(annotated, `${indent}    `, [
                    fr ? 'Exemple d’entrée :' : 'Example input:',
                    formattedArgs.join(', '),
                    '',
                ]);
            }
            continue;
        }
        if (!lessonInserted && /^return\b/.test(trimmed) && expandedLesson.length) {
            addComment(annotated, indent, expandedLesson);
            annotated.push('');
            lessonInserted = true;
        } else if (!/^print\s*\(/.test(trimmed) || !example) {
            addComment(annotated, indent, lineExplanation(trimmed, language, example));
        }
        annotated.push(normalizeDisplayLine(line, example));
    }

    if (!lessonInserted && expandedLesson.length) {
        annotated.push('');
        addComment(annotated, '', expandedLesson);
    }

    const concreteTransformation = buildConcreteTransformation(source, language, example);
    if (concreteTransformation.length) {
        annotated.push('');
        annotated.push('');
        addComment(annotated, '', concreteTransformation);
    }

    const typeContrast = buildTypeContrast(source, language, example);
    if (typeContrast.length) {
        annotated.push('');
        annotated.push('');
        addComment(annotated, '', typeContrast);
    }

    const executionTrace = buildUniversalExecutionTrace(source, language, example);
    if (executionTrace.length) {
        annotated.push('');
        annotated.push('');
        addComment(annotated, '', [
            fr
                ? 'Trajet complet des valeurs pour l’exemple affiché :'
                : 'Complete value path for the shown example:',
            '',
            ...executionTrace,
        ]);
    }

    const summary = transformationSummary(source, language, example);
    annotated.push('');
    annotated.push('');
    addComment(annotated, '', [
        fr ? 'Cette solution effectue les étapes suivantes :' : 'So this function is doing these things:',
        '',
        ...summary.map((step, index) => `${index + 1}. ${step}`),
    ]);

    const compacted = annotated.filter((line, index) => line !== '' || annotated[index - 1] !== '');
    const bounded = compacted.slice(0, MAX_ANNOTATED_LINES).join('\n').trim();
    const intro = fr
        ? 'Explication du code : voici le code réel expliqué à l’endroit où chaque opération se produit. Les commentaires montrent les types, les valeurs intermédiaires et le trajet vers le résultat.'
        : 'Code explanation: Here is the actual code explained where each operation happens. The comments show the data types, intermediate values, and path to the final result.';
    return `${intro}\n\`\`\`python\n${bounded}\n\`\`\``;
};
