export type AiCodeExplanationLanguage = 'en' | 'fr';

const MAX_SOURCE_LINES = 56;
const MAX_ANNOTATED_LINES = 340;

type PythonCall = {
    path: string;
    args: string[];
};

const PYTHON_BUILTINS: Record<string, { signature: string; purpose: string; purposeFr: string }> = {
    abs: { signature: 'abs(number)', purpose: 'returns the non-negative magnitude of a number', purposeFr: 'renvoie la magnitude non négative d’un nombre' },
    all: { signature: 'all(iterable)', purpose: 'returns True only when every item is truthy', purposeFr: 'renvoie True seulement si chaque élément est vrai' },
    any: { signature: 'any(iterable)', purpose: 'returns True when at least one item is truthy', purposeFr: 'renvoie True si au moins un élément est vrai' },
    bin: { signature: 'bin(integer)', purpose: 'returns the binary representation of an integer as text', purposeFr: 'renvoie la représentation binaire d’un entier sous forme de texte' },
    bool: { signature: 'bool(value=False)', purpose: 'converts a value to True or False', purposeFr: 'convertit une valeur en True ou False' },
    chr: { signature: 'chr(code_point)', purpose: 'returns the character represented by a Unicode code point', purposeFr: 'renvoie le caractère représenté par un point de code Unicode' },
    dict: { signature: 'dict(source=...)', purpose: 'creates a dictionary from key-value data', purposeFr: 'crée un dictionnaire à partir de données clé-valeur' },
    enumerate: { signature: 'enumerate(iterable, start=0)', purpose: 'pairs each item with a counter', purposeFr: 'associe chaque élément à un compteur' },
    filter: { signature: 'filter(function, iterable)', purpose: 'keeps items for which function(item) is truthy', purposeFr: 'conserve les éléments pour lesquels function(item) est vrai' },
    float: { signature: 'float(value=0)', purpose: 'converts a compatible value to a decimal number', purposeFr: 'convertit une valeur compatible en nombre décimal' },
    format: { signature: 'format(value, format_spec="")', purpose: 'formats a value according to a formatting specification', purposeFr: 'formate une valeur selon une spécification de formatage' },
    hex: { signature: 'hex(integer)', purpose: 'returns the hexadecimal representation of an integer as text', purposeFr: 'renvoie la représentation hexadécimale d’un entier sous forme de texte' },
    input: { signature: 'input(prompt="")', purpose: 'shows an optional prompt and returns the typed text as a string', purposeFr: 'affiche un message facultatif et renvoie le texte saisi comme chaîne' },
    int: { signature: 'int(value=0, base=10)', purpose: 'converts a compatible value to an integer', purposeFr: 'convertit une valeur compatible en entier' },
    isinstance: { signature: 'isinstance(object, classinfo)', purpose: 'checks whether an object belongs to a requested type', purposeFr: 'vérifie si un objet appartient au type demandé' },
    len: { signature: 'len(object)', purpose: 'returns the number of items', purposeFr: 'renvoie le nombre d’éléments' },
    list: { signature: 'list(iterable=())', purpose: 'consumes an iterable and collects its items in a list', purposeFr: 'parcourt un itérable et rassemble ses éléments dans une liste' },
    map: { signature: 'map(function, iterable, ...)', purpose: 'calls function(item) lazily for every item from the iterable', purposeFr: 'appelle function(item) progressivement pour chaque élément de l’itérable' },
    max: { signature: 'max(iterable, *, key=None)', purpose: 'returns the largest selected item', purposeFr: 'renvoie le plus grand élément sélectionné' },
    min: { signature: 'min(iterable, *, key=None)', purpose: 'returns the smallest selected item', purposeFr: 'renvoie le plus petit élément sélectionné' },
    ord: { signature: 'ord(character)', purpose: 'returns the Unicode code point of one character', purposeFr: 'renvoie le point de code Unicode d’un caractère' },
    pow: { signature: 'pow(base, exponent, modulus=None)', purpose: 'raises a base to an exponent, optionally using a modulus', purposeFr: 'élève une base à une puissance, avec un modulo facultatif' },
    print: { signature: 'print(*objects, sep=" ", end="\\n")', purpose: 'converts values to display text and writes them to the output', purposeFr: 'convertit les valeurs en texte et les écrit dans la sortie' },
    range: { signature: 'range(start, stop, step=1)', purpose: 'creates an integer sequence whose stop value is excluded', purposeFr: 'crée une séquence d’entiers dont la valeur stop est exclue' },
    repr: { signature: 'repr(object)', purpose: 'returns a developer-oriented text representation of an object', purposeFr: 'renvoie une représentation textuelle détaillée d’un objet' },
    reversed: { signature: 'reversed(sequence)', purpose: 'returns an iterator that reads a sequence from the end to the beginning', purposeFr: 'renvoie un itérateur qui lit une séquence de la fin vers le début' },
    round: { signature: 'round(number, ndigits=None)', purpose: 'rounds a number to the requested number of decimal places', purposeFr: 'arrondit un nombre au nombre demandé de décimales' },
    set: { signature: 'set(iterable=())', purpose: 'collects unique hashable items', purposeFr: 'rassemble des éléments hachables uniques' },
    sorted: { signature: 'sorted(iterable, *, key=None, reverse=False)', purpose: 'returns a new sorted list', purposeFr: 'renvoie une nouvelle liste triée' },
    str: { signature: 'str(object="")', purpose: 'converts a value to text', purposeFr: 'convertit une valeur en texte' },
    sum: { signature: 'sum(iterable, start=0)', purpose: 'adds the items to an optional starting value', purposeFr: 'additionne les éléments à une valeur initiale facultative' },
    tuple: { signature: 'tuple(iterable=())', purpose: 'collects items in an immutable tuple', purposeFr: 'rassemble les éléments dans un tuple immuable' },
    type: { signature: 'type(object)', purpose: 'returns the type of an object', purposeFr: 'renvoie le type d’un objet' },
    zip: { signature: 'zip(*iterables)', purpose: 'combines corresponding items from multiple iterables', purposeFr: 'combine les éléments correspondants de plusieurs itérables' },
};

const MODULE_PURPOSES: Record<string, [string, string]> = {
    collections: ['specialized container data types', 'des types de conteneurs spécialisés'],
    datetime: ['date and time types and operations', 'des types et opérations de date et d’heure'],
    functools: ['higher-order function tools', 'des outils pour fonctions d’ordre supérieur'],
    itertools: ['memory-efficient iterator tools', 'des outils d’itération économes en mémoire'],
    json: ['JSON encoding and decoding', 'l’encodage et le décodage JSON'],
    math: ['mathematical functions and constants', 'des fonctions et constantes mathématiques'],
    os: ['portable operating-system services', 'des services portables du système d’exploitation'],
    pathlib: ['object-oriented filesystem paths', 'des chemins de fichiers orientés objet'],
    random: ['pseudo-random selections and numbers', 'des sélections et nombres pseudo-aléatoires'],
    re: ['regular-expression matching', 'la recherche par expressions régulières'],
    statistics: ['statistical calculations', 'des calculs statistiques'],
    sys: ['Python interpreter and runtime information', 'des informations sur l’interpréteur et l’exécution Python'],
};

const METHOD_PURPOSES: Record<string, [string, string]> = {
    append: ['adds one item to the end of the existing list and returns None', 'ajoute un élément à la fin de la liste existante et renvoie None'],
    count: ['counts matching occurrences', 'compte les occurrences correspondantes'],
    get: ['reads a dictionary value and can supply a default when the key is absent', 'lit une valeur du dictionnaire et peut fournir une valeur par défaut si la clé manque'],
    items: ['returns a dynamic view of dictionary key-value pairs', 'renvoie une vue dynamique des paires clé-valeur du dictionnaire'],
    join: ['joins an iterable of strings using the owner string as the separator', 'joint un itérable de chaînes en utilisant la chaîne propriétaire comme séparateur'],
    lower: ['returns a lowercase copy of the string', 'renvoie une copie de la chaîne en minuscules'],
    now: ['creates a datetime value for the current local date and time', 'crée une valeur datetime contenant la date et l’heure locales actuelles'],
    replace: ['returns a copy with selected text replaced', 'renvoie une copie dans laquelle le texte choisi est remplacé'],
    sort: ['sorts the existing list in place and returns None', 'trie la liste existante sur place et renvoie None'],
    split: ['returns a list of substrings separated at the requested delimiter', 'renvoie une liste de sous-chaînes séparées au délimiteur demandé'],
    strip: ['returns a copy with surrounding whitespace or selected characters removed', 'renvoie une copie sans les espaces ou caractères choisis autour'],
    upper: ['returns an uppercase copy of the string', 'renvoie une copie de la chaîne en majuscules'],
    values: ['returns a dynamic view of dictionary values', 'renvoie une vue dynamique des valeurs du dictionnaire'],
};

const extractPythonCalls = (code: string): PythonCall[] => {
    const calls: PythonCall[] = [];
    const seen = new Set<string>();
    const callStart = /[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*/y;
    for (let index = 0; index < code.length; index += 1) {
        callStart.lastIndex = index;
        const match = callStart.exec(code);
        if (!match) continue;
        const path = match[0];
        let open = callStart.lastIndex;
        while (/\s/.test(code[open] || '')) open += 1;
        if (code[open] !== '(' || /\bdef\s+$/.test(code.slice(Math.max(0, index - 8), index))) {
            index = callStart.lastIndex - 1;
            continue;
        }
        let depth = 0;
        let quote = '';
        let escaped = false;
        let close = -1;
        for (let cursor = open; cursor < code.length; cursor += 1) {
            const char = code[cursor];
            if (quote) {
                if (escaped) escaped = false;
                else if (char === '\\') escaped = true;
                else if (char === quote) quote = '';
                continue;
            }
            if (char === "'" || char === '"') quote = char;
            else if (char === '(') depth += 1;
            else if (char === ')' && --depth === 0) {
                close = cursor;
                break;
            }
        }
        if (close < 0) continue;
        const args = splitTopLevel(code.slice(open + 1, close));
        const key = `${path}(${args.join(',')})`;
        if (!seen.has(key)) {
            calls.push({ path, args });
            seen.add(key);
        }
        index = callStart.lastIndex - 1;
    }
    return calls.slice(0, 10);
};

const primarySolutionCode = (solution: string) => {
    const lines = solution.trim().split('\n');
    const isApproachHeading = (line: string) => /^\s*#\s*(?:.*\bapproach\b|Alternative\b.*)/i.test(line);
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
    for (const line of lines) target.push(line ? `${indent}# ${line.replace(/`/g, '')}` : '');
};

const quotePythonString = (value: string) => `"${value.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;

const normalizeDisplayLine = (
    line: string,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    let normalized = line.replace(/\.split\(\s*(['"])(.*?)\1\s*\)/g, (_match, _quote, delimiter) => `.split(${quotePythonString(delimiter)})`);
    if (example && new RegExp(`\\b${example.name}\\s*\\(`).test(normalized)) {
        normalized = normalized.replace(
            new RegExp(`\\b${example.name}\\s*\\(([^\\n()]*(?:\\([^\\n()]*\\)[^\\n()]*)*)\\)`),
            (_match, rawArguments) => {
                const formattedArgs = splitTopLevel(rawArguments).map(arg => {
            const value = unquote(arg);
            return value === null ? arg : quotePythonString(value);
                });
                return `${example.name}(${formattedArgs.join(', ')})`;
            },
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

const displayTracedValue = (trace: TracedValue): string => {
    if (trace.type === 'float' && typeof trace.value === 'number' && Number.isInteger(trace.value)) {
        return `${trace.value.toFixed(1)}`;
    }
    return displayValue(trace.value);
};

const PARAMETER_PURPOSES: Record<string, [string, string]> = {
    part: ['the amount being compared with the total', 'la quantité comparée au total'],
    whole: ['the complete or total amount used as the reference', 'la quantité complète ou totale utilisée comme référence'],
    text: ['the input string the function will examine or transform', 'la chaîne d’entrée que la fonction va examiner ou transformer'],
    string: ['the input text the function will examine or transform', 'le texte d’entrée que la fonction va examiner ou transformer'],
    sentence: ['the sentence the function will process', 'la phrase que la fonction va traiter'],
    word: ['the word the function will process', 'le mot que la fonction va traiter'],
    number: ['the numeric input the function will calculate with', 'l’entrée numérique utilisée dans le calcul'],
    num: ['the numeric input the function will calculate with', 'l’entrée numérique utilisée dans le calcul'],
    numbers: ['the collection of numbers the function will process', 'la collection de nombres que la fonction va traiter'],
    values: ['the collection of input values the function will process', 'la collection de valeurs que la fonction va traiter'],
    items: ['the collection of items the function will process', 'la collection d’éléments que la fonction va traiter'],
    key: ['the dictionary key to find, create, or update', 'la clé de dictionnaire à trouver, créer ou modifier'],
    value: ['the value supplied for the requested operation', 'la valeur fournie pour l’opération demandée'],
    target: ['the value the function is trying to find or match', 'la valeur que la fonction cherche à trouver ou faire correspondre'],
    start: ['the starting value or position', 'la valeur ou position de départ'],
    stop: ['the stopping boundary, normally excluded by Python ranges and slices', 'la limite d’arrêt, normalement exclue par les plages et tranches Python'],
    end: ['the ending value or position', 'la valeur ou position de fin'],
    step: ['the amount by which the operation advances each time', 'la quantité de progression à chaque étape'],
    count: ['the number of repetitions or items requested', 'le nombre de répétitions ou d’éléments demandé'],
    index: ['the position used to access an item', 'la position utilisée pour accéder à un élément'],
    mapping: ['the dictionary-like object containing key-value pairs', 'l’objet de type dictionnaire contenant des paires clé-valeur'],
    dictionary: ['the dictionary containing key-value pairs', 'le dictionnaire contenant des paires clé-valeur'],
    records: ['the records the function will inspect or group', 'les enregistrements que la fonction va examiner ou regrouper'],
    delimiter: ['the separator used to split or join text', 'le séparateur utilisé pour découper ou joindre du texte'],
    separator: ['the text placed between items or used to split them', 'le texte placé entre les éléments ou utilisé pour les découper'],
};

const parameterPurpose = (
    parameter: string,
    problemDescription: string,
    language: AiCodeExplanationLanguage,
) => {
    const fr = language === 'fr';
    const normalized = parameter.toLowerCase().replace(/^_+|_+$/g, '');
    const direct = PARAMETER_PURPOSES[normalized];
    if (direct) return fr ? direct[1] : direct[0];
    if (/^(?:list|list\d+|array|sequence)$/.test(normalized)) return fr ? 'la séquence d’entrée que la fonction va traiter' : 'the input sequence the function will process';
    if (/^(?:dict|dic|data|lookup)$/.test(normalized)) return fr ? 'les données d’entrée organisées en paires clé-valeur' : 'the input data organized as key-value pairs';
    if (/^(?:func|function|callback|predicate)$/.test(normalized)) return fr ? 'la fonction que le code appellera sur d’autres valeurs' : 'the function the code will call with other values';
    if (/^(?:iterable|iterator)$/.test(normalized)) return fr ? 'la source d’éléments à parcourir' : 'the source of items to iterate over';
    const descriptionHasName = new RegExp(`\\b${parameter.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'i').test(problemDescription);
    if (descriptionHasName) return fr
        ? `la valeur d’entrée appelée ${parameter} dans l’énoncé du problème`
        : `the input value called ${parameter} in the problem statement`;
    return fr ? 'la valeur reçue à cette position lors de l’appel' : 'the value received at this argument position when the function is called';
};

const buildParameterLesson = (
    params: string[],
    example: ReturnType<typeof extractFunctionExample>,
    problemDescription: string,
    language: AiCodeExplanationLanguage,
) => {
    if (!params.length) return [];
    const fr = language === 'fr';
    const countLabel = params.length === 1
        ? (fr ? 'une' : 'one')
        : params.length === 2
            ? (fr ? 'deux' : 'two')
            : params.length === 3
                ? (fr ? 'trois' : 'three')
                : String(params.length);
    const lines = [
        fr
            ? `Elle reçoit ${countLabel} ${params.length === 1 ? 'valeur' : 'valeurs'} :`
            : `It takes ${countLabel} ${params.length === 1 ? 'value' : 'values'}:`,
    ];
    params.forEach((param, index) => {
        const rawArgument = example?.args[index];
        const traced = rawArgument ? inferExpression(rawArgument, new Map()) : null;
        const shownValue = traced?.known ? ` ${fr ? 'Dans l’exemple' : 'In the example'}: ${param} = ${displayTracedValue(traced)} (${traced.type}).` : '';
        lines.push(`${param} = ${parameterPurpose(param, problemDescription, language)}.${shownValue}`);
    });
    return lines;
};

const findEvaluationOperator = (expression: string) => {
    const precedenceGroups = [
        [' or '],
        [' and '],
        ['==', '!=', '>=', '<=', ' is ', ' in ', '>', '<'],
        ['+', '-'],
        ['//', '%', '*', '/'],
        ['**'],
    ];
    for (const operators of precedenceGroups) {
        const found = findTopLevelOperator(expression, operators);
        if (found) return found;
    }
    return null;
};

const buildConcreteExpressionWalkthrough = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    if (!example || example.args.length < example.params.length) return [];
    const returnExpression = code.match(/^\s*return\s+(.+)$/m)?.[1]?.trim();
    if (!returnExpression) return [];
    const fr = language === 'fr';
    const environment = new Map<string, TracedValue>();
    example.params.forEach((param, index) => {
        environment.set(param, inferExpression(example.args[index] || '', environment));
    });
    if ([...environment.values()].some(value => !value.known)) return [];

    const steps: string[] = [];
    const seen = new Set<string>();
    const addStep = (source: string, calculation: string, result: TracedValue, explanation: string) => {
        const key = `${source}|${calculation}`;
        if (seen.has(key)) return;
        seen.add(key);
        const number = seen.size;
        steps.push(
            fr ? `Étape ${number} : évaluer ${source}.` : `Step ${number}: evaluate ${source}.`,
            `${fr ? 'Calcul' : 'Calculation'}: ${calculation}`,
            `${fr ? 'Résultat et type' : 'Result and type'}: ${displayTracedValue(result)} (${result.type})`,
            `${fr ? 'Pourquoi' : 'Why'}: ${explanation}`,
            '',
        );
    };

    const evaluate = (rawExpression: string, depth = 0): TracedValue => {
        const expression = stripOuterParentheses(rawExpression.trim());
        if (depth > 12) return inferExpression(expression, environment);
        const operator = findEvaluationOperator(expression);
        if (operator) {
            const leftText = expression.slice(0, operator.index).trim();
            const rightText = expression.slice(operator.index + operator.operator.length).trim();
            const left = evaluate(leftText, depth + 1);
            const right = evaluate(rightText, depth + 1);
            const result = inferExpression(expression, environment);
            const operatorName = operator.operator.trim();
            const lesson = OPERATOR_LESSONS[operatorName];
            if (left.known && right.known && result.known) {
                addStep(
                    expression,
                    `${displayTracedValue(left)} ${operatorName} ${displayTracedValue(right)} = ${displayTracedValue(result)}`,
                    result,
                    lesson ? (fr ? lesson[1] : lesson[0]) : result.operation,
                );
            }
            return result;
        }

        const call = expression.match(/^([A-Za-z_][\w.]*)\((.*)\)$/s);
        if (call) {
            const rawArgs = splitTopLevel(call[2]);
            const args = rawArgs.map(argument => evaluate(argument.replace(/^\w+\s*=\s*/, ''), depth + 1));
            const result = inferExpression(expression, environment);
            const builtin = PYTHON_BUILTINS[call[1]];
            if (args.every(argument => argument.known) && result.known) {
                const renderedCall = `${call[1]}(${args.map(displayTracedValue).join(', ')})`;
                let explanation = builtin ? (fr ? builtin.purposeFr : builtin.purpose) : result.operation;
                if (call[1] === 'round' && rawArgs[1]) explanation += fr
                    ? ` Le deuxième argument ${rawArgs[1]} demande ${rawArgs[1]} chiffres après la virgule.`
                    : ` The second argument ${rawArgs[1]} requests ${rawArgs[1]} digits after the decimal point.`;
                addStep(expression, `${renderedCall} = ${displayTracedValue(result)}`, result, explanation);
            }
            return result;
        }

        const result = inferExpression(expression, environment);
        if (result.known && (/\[[^\]]+\]|\.[A-Za-z_]\w*\(/.test(expression))) {
            addStep(expression, `${expression} = ${displayTracedValue(result)}`, result, result.operation);
        }
        return result;
    };

    const finalResult = evaluate(returnExpression);
    if (!steps.length || !finalResult.known) return [];
    const percentageLesson = example.params.includes('part')
        && example.params.includes('whole')
        && /\bpart\s*\/\s*whole\b/.test(returnExpression)
        && /\*\s*100\b/.test(returnExpression)
        ? (fr ? [
            '',
            'La formule générale est :',
            '',
            'pourcentage = (partie / total) * 100',
            '',
            'Autre exemple : si 40 réponses sur 50 sont correctes :',
            '40 / 50 = 0.8',
            '0.8 * 100 = 80.0',
            'Donc 40 représente 80 % de 50.',
        ] : [
            '',
            'The general formula is:',
            '',
            'percentage = (part / whole) * 100',
            '',
            'Another example: if 40 answers out of 50 are correct:',
            '40 / 50 = 0.8',
            '0.8 * 100 = 80.0',
            'So 40 is 80% of 50.',
        ])
        : [];
    return [
        fr ? 'Calcul complet avec l’exemple affiché :' : 'Complete calculation with the shown example:',
        '',
        ...example.params.map(param => {
            const value = environment.get(param)!;
            return `${param} = ${displayTracedValue(value)} (${value.type})`;
        }),
        '',
        ...steps,
        fr
            ? `La fonction renvoie finalement ${displayTracedValue(finalResult)} (${finalResult.type}).`
            : `The function finally returns ${displayTracedValue(finalResult)} (${finalResult.type}).`,
        ...percentageLesson,
    ];
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

const stripInlinePythonComment = (line: string) => {
    let quote = '';
    let escaped = false;
    for (let index = 0; index < line.length; index += 1) {
        const char = line[index];
        if (quote) {
            if (escaped) escaped = false;
            else if (char === '\\') escaped = true;
            else if (char === quote) quote = '';
            continue;
        }
        if (char === "'" || char === '"') quote = char;
        else if (char === '#') return line.slice(0, index).trimEnd();
    }
    return line;
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
                const traced = knownValue(value, operation);
                const resultType = arithmetic.operator === '/' || left.type === 'float' || right.type === 'float'
                    ? 'float'
                    : traced.type;
                return { ...traced, type: resultType };
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
                    const traced = knownValue(Math.round(Number(values[0]) * factor) / factor, operation);
                    return { ...traced, type: args[0]?.type === 'float' ? 'float' : traced.type };
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

    return unknownValue('value', `Evaluate the exact expression ${expression} using the values currently bound to its names.`);
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
        .replace(/^Evaluate the exact expression (.+) using the values currently bound to its names\.$/, 'Évaluer exactement l’expression $1 avec les valeurs actuellement liées à ses noms.');
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
        const trimmed = stripInlinePythonComment(line).trim();
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
            ? `${destination} = ${displayTracedValue(trace)} (${trace.type})`
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

const buildCallableSemanticsLesson = (
    code: string,
    language: AiCodeExplanationLanguage,
) => {
    const fr = language === 'fr';
    const imports = new Map<string, { module: string; imported?: string }>();
    const definitions = new Map<string, { params: string[]; nested: boolean; parent?: string }>();
    const scopeByIndent: Array<{ indent: number; name: string }> = [];

    for (const line of code.split('\n')) {
        const trimmed = stripInlinePythonComment(line).trim();
        const importedModule = trimmed.match(/^import\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)(?:\s+as\s+([A-Za-z_]\w*))?/);
        if (importedModule) imports.set(importedModule[2] || importedModule[1].split('.')[0], { module: importedModule[1] });
        const importedName = trimmed.match(/^from\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)\s+import\s+([A-Za-z_]\w*)(?:\s+as\s+([A-Za-z_]\w*))?/);
        if (importedName) imports.set(importedName[3] || importedName[2], { module: importedName[1], imported: importedName[2] });

        const definition = trimmed.match(/^def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/);
        if (!definition) continue;
        const indent = line.length - line.trimStart().length;
        while (scopeByIndent.length && scopeByIndent[scopeByIndent.length - 1].indent >= indent) scopeByIndent.pop();
        const parent = scopeByIndent[scopeByIndent.length - 1]?.name;
        definitions.set(definition[1], {
            params: splitTopLevel(definition[2]).map(param => param.trim()).filter(Boolean),
            nested: Boolean(parent),
            parent,
        });
        scopeByIndent.push({ indent, name: definition[1] });
    }

    const calls = extractPythonCalls(code);
    if (!calls.length) return [];
    const lesson: string[] = [
        fr ? 'Détail des modules, fonctions et méthodes :' : 'Module, function, and method breakdown:',
        '',
    ];

    calls.forEach((call, index) => {
        const parts = call.path.split('.');
        const root = parts[0];
        const terminal = parts[parts.length - 1];
        const imported = imports.get(root);
        const local = definitions.get(root);
        const builtin = PYTHON_BUILTINS[root];
        lesson.push(`${index + 1}. ${call.path}(${call.args.join(', ')})`);

        if (call.path === 'datetime.datetime.now' && imported?.module === 'datetime') {
            lesson.push(
                fr
                    ? '`datetime` est le module importé : il fournit les outils de date et d’heure.'
                    : '`datetime` is the imported module: it provides date and time tools.',
                fr
                    ? '`datetime.datetime` est la classe `datetime` stockée dans ce module ; le second `datetime` n’est pas une méthode.'
                    : '`datetime.datetime` is the `datetime` class stored inside that module; the second `datetime` is not a method.',
                fr
                    ? '`now` est une méthode de classe de `datetime`. `now()` crée puis renvoie une nouvelle instance représentant la date et l’heure locales actuelles.'
                    : '`now` is a class method of the `datetime` class. `now()` creates and returns a new instance representing the current local date and time.',
                fr
                    ? 'Résolution de gauche à droite : trouver le module `datetime` → lire sa classe `datetime` → lire la méthode `now` → appeler `now()`.'
                    : 'Left-to-right resolution: find the `datetime` module → read its `datetime` class → read the `now` method → call `now()`.',
            );
        } else if (builtin && parts.length === 1) {
            lesson.push(
                fr ? `Fonction intégrée : ${builtin.signature}. Elle ${builtin.purposeFr}.` : `Built-in function: ${builtin.signature}. It ${builtin.purpose}.`,
            );
            if (root === 'map' || root === 'filter') {
                lesson.push(fr
                    ? 'Le premier argument est la fonction à appliquer ; le deuxième est l’itérable qui fournit les éléments. Le résultat est produit progressivement.'
                    : 'The first argument is the function to apply; the second is the iterable supplying items. Results are produced lazily.');
            } else if (root === 'sorted') {
                lesson.push(fr
                    ? 'L’itérable vient en premier ; `key=` et `reverse=` sont des options nommées évaluées ensuite.'
                    : 'The iterable comes first; `key=` and `reverse=` are named options evaluated afterward.');
            }
        } else if (local && parts.length === 1) {
            const signature = `${root}(${local.params.join(', ')})`;
            lesson.push(fr
                ? `${signature} est ${local.nested ? `une fonction imbriquée créée pendant l’appel de ${local.parent}` : 'une fonction définie par ce programme'}. Sa définition crée l’objet fonction ; son corps ne s’exécute qu’au moment de l’appel.`
                : `${signature} is ${local.nested ? `a nested helper created while ${local.parent} is running` : 'a function defined by this program'}. Its definition creates the function object; its body does not run until the call.`);
            lesson.push(fr
                ? `À l’appel, Python lie les arguments aux paramètres ${local.params.join(', ') || '(aucun)'}, exécute le corps indenté, puis ` + '`return` rend le contrôle et la valeur à l’appelant.'
                : `At the call, Python binds arguments to ${local.params.join(', ') || '(no parameters)'}, runs the indented body, then ` + '`return` sends control and the value back to the caller.');
        } else if (imported && parts.length === 1) {
            const modulePurpose = MODULE_PURPOSES[imported.module.split('.')[0]];
            lesson.push(fr
                ? `\`${root}\` est \`${imported.imported || imported.module}\` importé depuis le module \`${imported.module}\`${modulePurpose ? `, qui fournit ${modulePurpose[1]}` : ''}. L’appel exécute cet objet importé.`
                : `\`${root}\` is \`${imported.imported || imported.module}\` imported from the \`${imported.module}\` module${modulePurpose ? `, which provides ${modulePurpose[0]}` : ''}. The call executes that imported callable.`);
        } else if (parts.length > 1) {
            const methodPurpose = METHOD_PURPOSES[terminal];
            if (imported?.imported) {
                lesson.push(fr
                    ? `\`${root}\` est le nom local de \`${imported.imported}\`, importé depuis le module \`${imported.module}\`. C’est un membre du module, pas le module lui-même.`
                    : `\`${root}\` is the local name for \`${imported.imported}\`, imported from the \`${imported.module}\` module. It is a member of that module, not the module itself.`);
                if (imported.module === 'datetime' && imported.imported === 'datetime' && terminal === 'now') {
                    lesson.push(fr
                        ? `Ici, \`${root}\` est la classe \`datetime\` et \`${terminal}\` est sa méthode de classe, qui crée la date et l’heure locales actuelles.`
                        : `Here, \`${root}\` is the \`datetime\` class and \`${terminal}\` is its class method, which creates the current local date and time.`);
                } else {
                    lesson.push(fr
                        ? `Python résout ensuite l’attribut ou la méthode \`${parts.slice(1).join('.')}\` sur cet objet importé.`
                        : `Python then resolves the \`${parts.slice(1).join('.')}\` attribute or method on that imported object.`);
                }
            } else if (imported) {
                const modulePurpose = MODULE_PURPOSES[imported.module.split('.')[0]];
                lesson.push(fr
                    ? `\`${root}\` désigne le module importé \`${imported.module}\`${modulePurpose ? `, utilisé pour ${modulePurpose[1]}` : ''}.`
                    : `\`${root}\` refers to the imported \`${imported.module}\` module${modulePurpose ? `, used for ${modulePurpose[0]}` : ''}.`);
                lesson.push(fr
                    ? `Python lit ensuite \`${parts.slice(1).join('.')}\` dans ce module, puis appelle la fonction ou méthode finale \`${terminal}\`.`
                    : `Python then resolves \`${parts.slice(1).join('.')}\` from that module and calls the final \`${terminal}\` function or method.`);
            } else {
                lesson.push(fr
                    ? `Python évalue d’abord l’objet \`${parts.slice(0, -1).join('.')}\`, puis recherche sa méthode \`${terminal}\`.`
                    : `Python first evaluates the \`${parts.slice(0, -1).join('.')}\` object, then looks up its \`${terminal}\` method.`);
            }
            if (methodPurpose) lesson.push(fr ? `Cette méthode ${methodPurpose[1]}.` : `This method ${methodPurpose[0]}.`);
        } else {
            lesson.push(fr
                ? `\`${root}\` est résolu comme un objet appelable au moment de l’exécution.`
                : `\`${root}\` is resolved as a callable object at runtime.`);
        }

        const nestedArguments = call.args.filter(argument => /[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*\s*\(/.test(argument));
        lesson.push(fr
            ? `Ordre d’appel : Python résout d’abord \`${call.path}\`, puis évalue ${call.args.length ? `ses ${call.args.length} argument(s) de gauche à droite` : 'qu’il n’y a aucun argument'}, appelle la fonction, puis utilise sa valeur de retour.`
            : `Call order: Python resolves \`${call.path}\` first, then evaluates ${call.args.length ? `its ${call.args.length} argument(s) from left to right` : 'that there are no arguments'}, calls it, and then uses its return value.`);
        if (nestedArguments.length) lesson.push(fr
            ? `Appel imbriqué : ${nestedArguments.map(value => `\`${value}\``).join(', ')} doit finir avant que l’appel extérieur puisse commencer.`
            : `Nested call: ${nestedArguments.map(value => `\`${value}\``).join(', ')} must finish before the outer call can begin.`);
        lesson.push('');
    });

    return lesson;
};

const OPERATOR_LESSONS: Record<string, [string, string]> = {
    '+': ['adds the right operand to the left operand', 'additionne l’opérande de droite à celui de gauche'],
    '-': ['subtracts the right operand from the left operand', 'soustrait l’opérande de droite de celui de gauche'],
    '*': ['multiplies the two operands', 'multiplie les deux opérandes'],
    '/': ['performs true division and returns a floating-point result', 'effectue une division réelle et renvoie un résultat décimal'],
    '//': ['performs floor division: it divides and rounds the quotient down to the nearest integer', 'effectue une division entière : il divise puis arrondit le quotient vers le bas'],
    '%': ['returns the remainder left after division', 'renvoie le reste laissé par la division'],
    '**': ['raises the left operand to the power of the right operand', 'élève l’opérande de gauche à la puissance de celui de droite'],
    '==': ['tests whether the two values are equal', 'teste si les deux valeurs sont égales'],
    '!=': ['tests whether the two values are different', 'teste si les deux valeurs sont différentes'],
    '>': ['tests whether the left value is greater than the right value', 'teste si la valeur de gauche est supérieure à celle de droite'],
    '<': ['tests whether the left value is less than the right value', 'teste si la valeur de gauche est inférieure à celle de droite'],
    '>=': ['tests whether the left value is greater than or equal to the right value', 'teste si la valeur de gauche est supérieure ou égale à celle de droite'],
    '<=': ['tests whether the left value is less than or equal to the right value', 'teste si la valeur de gauche est inférieure ou égale à celle de droite'],
    'and': ['evaluates left to right and stops at the first falsy operand', 'évalue de gauche à droite et s’arrête au premier opérande faux'],
    'or': ['evaluates left to right and stops at the first truthy operand', 'évalue de gauche à droite et s’arrête au premier opérande vrai'],
    'in': ['tests whether the left value occurs inside the right container', 'teste si la valeur de gauche se trouve dans le conteneur de droite'],
    'not in': ['tests whether the left value does not occur inside the right container', 'teste si la valeur de gauche ne se trouve pas dans le conteneur de droite'],
    'is': ['tests object identity, not value equality', 'teste l’identité des objets, et non l’égalité de leurs valeurs'],
    'is not': ['tests that two references do not point to the same object', 'teste que deux références ne désignent pas le même objet'],
};

const expressionOperatorLessons = (
    expression: string,
    language: AiCodeExplanationLanguage,
) => {
    const fr = language === 'fr';
    const lessons: string[] = [];
    const addOperator = (operator: string) => {
        const lesson = OPERATOR_LESSONS[operator];
        if (!lesson || lessons.some(line => line.startsWith(`\`${operator}\``))) return;
        lessons.push(fr ? `\`${operator}\` ${lesson[1]}.` : `\`${operator}\` ${lesson[0]}.`);
    };
    const orderedOperators = ['is not', 'not in', '**', '//', '>=', '<=', '==', '!=', 'and', 'or', 'in', 'is', '%', '/', '*', '+', '-', '>', '<'];
    for (const operator of orderedOperators) {
        let pattern: RegExp;
        if (operator === '**') pattern = /(?<!\*)\*\*(?!\*)/;
        else if (operator === '*') pattern = /(?<!\*)\*(?!\*)/;
        else if (operator === '//') pattern = /(?<!\/)\/\/(?!\/)/;
        else if (operator === '/') pattern = /(?<!\/)\/(?!\/)/;
        else if (operator === '>') pattern = /(?<![=>])>(?!=)/;
        else if (operator === '<') pattern = /(?<![=<])<(?!=)/;
        else {
            const escaped = operator.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
            pattern = new RegExp(/^[a-z]/i.test(operator) ? `\\b${escaped}\\b` : escaped);
        }
        if (pattern.test(expression)) addOperator(operator);
    }
    if (/\bnot\s+/.test(expression) && !/\bnot\s+(?:in|is)\b/.test(expression)) {
        lessons.push(fr ? '`not` inverse la valeur de vérité obtenue.' : '`not` reverses the resulting truth value.');
    }
    if (/\[[^\]]*:[^\]]*\]/.test(expression)) {
        lessons.push(fr
            ? 'Une tranche `[début:fin:pas]` sélectionne une partie de la séquence ; la position `fin` est exclue.'
            : 'A `[start:stop:step]` slice selects part of the sequence; the `stop` position is excluded.');
    } else if (/\[[^\]]+\]/.test(expression)) {
        lessons.push(fr
            ? 'Les crochets évaluent l’indice ou la clé, puis récupèrent cet élément précis.'
            : 'The brackets evaluate the index or key and then retrieve that specific item.');
    }
    if (/\/\/\s*10\b/.test(expression)) {
        lessons.push(fr
            ? 'Pour un entier positif, la division entière par `10` supprime le dernier chiffre décimal : `482 // 10` donne `48`.'
            : 'For a positive integer, floor-dividing by `10` removes the final decimal digit: `482 // 10` gives `48`.');
    }
    if (/%\s*10\b/.test(expression)) {
        lessons.push(fr
            ? 'Pour un entier non négatif, `% 10` isole le dernier chiffre décimal : `482 % 10` donne `2`.'
            : 'For a non-negative integer, `% 10` extracts the final decimal digit: `482 % 10` gives `2`.');
    }
    return lessons;
};

const augmentedAssignmentExplanation = (
    target: string,
    operator: string,
    expression: string,
    language: AiCodeExplanationLanguage,
) => {
    const fr = language === 'fr';
    const binaryOperator = operator.slice(0, -1);
    return [
        fr
            ? `\`${target} ${operator} ${expression}\` est une affectation augmentée, forme abrégée de \`${target} = ${target} ${binaryOperator} ${expression}\`.`
            : `\`${target} ${operator} ${expression}\` is augmented assignment, shorthand for \`${target} = ${target} ${binaryOperator} ${expression}\`.`,
        fr
            ? `Python lit d’abord la valeur actuelle de \`${target}\`, évalue \`${expression}\`, applique \`${binaryOperator}\`, puis stocke le résultat dans \`${target}\`.`
            : `Python first reads the current value of \`${target}\`, evaluates \`${expression}\`, applies \`${binaryOperator}\`, and stores the result back in \`${target}\`.`,
        ...expressionOperatorLessons(`${target} ${binaryOperator} ${expression}`, language),
    ];
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
    const inlineCompound = trimmed.match(/^(if|elif|while)\s+(.+):\s*(\S.+)$/);
    if (inlineCompound) {
        return [
            ...lineExplanation(`${inlineCompound[1]} ${inlineCompound[2]}:`, language, example),
            ...(splitTopLevel(inlineCompound[3], ';').flatMap(statement => lineExplanation(statement, language, example))),
        ];
    }
    const inlineElse = trimmed.match(/^else\s*:\s*(\S.+)$/);
    if (inlineElse) {
        return [
            ...(fr ? ['Ce bloc s’exécute uniquement si les conditions précédentes étaient False.'] : ['This branch runs only when the preceding conditions were False.']),
            ...(splitTopLevel(inlineElse[1], ';').flatMap(statement => lineExplanation(statement, language, example))),
        ];
    }
    const simpleStatements = splitTopLevel(trimmed, ';');
    if (simpleStatements.length > 1) {
        return simpleStatements.flatMap(statement => lineExplanation(statement, language, example));
    }
    if (/^return\b/.test(trimmed)) {
        const expression = trimmed.replace(/^return\s*/, '');
        return [
            fr ? `Python évalue d’abord \`${expression || 'None'}\` ; return arrête ensuite cette fonction et renvoie cette valeur à l’appelant et au correcteur.` : `Python evaluates \`${expression || 'None'}\` first; return then stops this function and sends that value back to the caller and grader.`,
            ...expressionOperatorLessons(expression, language),
        ];
    }
    if (/^print\s*\(/.test(trimmed)) {
        return [fr ? 'print(...) appelle la fonction et affiche le résultat dans la sortie.' : 'print(...) calls the function and displays the result in the output panel.'];
    }
    const whileStatement = trimmed.match(/^while\s+(.+):$/);
    if (whileStatement) {
        return [
            fr
                ? `Avant chaque itération, Python réévalue \`${whileStatement[1]}\`. Si le résultat est True, le bloc indenté s’exécute ; s’il est False, la boucle s’arrête.`
                : `Before every iteration, Python reevaluates \`${whileStatement[1]}\`. If it is True, the indented body runs; if it is False, the loop stops.`,
            fr ? 'Une ligne du corps doit modifier l’état utilisé par la condition, sinon la boucle peut ne jamais se terminer.' : 'A line in the body must change the state used by the condition, or the loop may never terminate.',
            ...expressionOperatorLessons(whileStatement[1], language),
        ];
    }
    const forStatement = trimmed.match(/^for\s+(.+)\s+in\s+(.+):$/);
    if (forStatement) {
        return [
            fr ? `Python évalue \`${forStatement[2]}\` une fois, obtient un itérable, puis affecte chaque élément successif à \`${forStatement[1]}\`.` : `Python evaluates \`${forStatement[2]}\` once, obtains an iterable, and assigns each successive item to \`${forStatement[1]}\`.`,
            ...expressionOperatorLessons(forStatement[2], language),
        ];
    }
    const conditionStatement = trimmed.match(/^(if|elif)\s+(.+):$/);
    if (conditionStatement) {
        return [
            fr ? `Python évalue \`${conditionStatement[2]}\` comme un booléen. Le bloc indenté s’exécute seulement si cette condition est True.` : `Python evaluates \`${conditionStatement[2]}\` as a Boolean. The indented branch runs only when this condition is True.`,
            ...expressionOperatorLessons(conditionStatement[2], language),
        ];
    }
    if (/^else\s*:/.test(trimmed)) {
        return [fr ? 'Ce bloc s’exécute uniquement si les conditions précédentes de la même chaîne étaient toutes False.' : 'This branch runs only when every preceding condition in the same chain was False.'];
    }
    if (/^with\b/.test(trimmed)) {
        return [fr ? 'Le bloc `with` gère automatiquement l’ouverture et le nettoyage de la ressource.' : 'The `with` block automatically manages opening and cleaning up the resource.'];
    }
    if (/^try\s*:|^except\b/.test(trimmed)) {
        return [fr ? 'Ce bloc exécute une opération risquée et traite une erreur prévue.' : 'This block runs a risky operation and handles an expected error.'];
    }
    if (/^finally\s*:/.test(trimmed)) {
        return [fr ? 'Le bloc `finally` s’exécute après `try`, qu’une erreur ait été levée ou non, afin d’effectuer le nettoyage final.' : 'The `finally` block runs after `try` whether or not an exception occurred, so final cleanup always happens.'];
    }
    const decorator = trimmed.match(/^@([A-Za-z_][\w.]*)/);
    if (decorator) {
        return [fr ? `Le décorateur \`${decorator[1]}\` reçoit la fonction ou classe définie juste dessous et peut modifier ou enrichir son comportement.` : `The \`${decorator[1]}\` decorator receives the function or class defined immediately below and can modify or extend its behavior.`];
    }
    const matchStatement = trimmed.match(/^match\s+(.+):$/);
    if (matchStatement) {
        return [fr ? `Python évalue \`${matchStatement[1]}\` une fois, puis compare cette valeur aux motifs des blocs \`case\` dans l’ordre.` : `Python evaluates \`${matchStatement[1]}\` once, then compares that value with each \`case\` pattern in order.`];
    }
    const caseStatement = trimmed.match(/^case\s+(.+):$/);
    if (caseStatement) {
        return [fr ? `Ce bloc s’exécute si la valeur de \`match\` correspond au motif \`${caseStatement[1]}\`; les noms du motif reçoivent les parties correspondantes.` : `This branch runs if the \`match\` value fits the pattern \`${caseStatement[1]}\`; names in the pattern receive the matching parts.`];
    }
    const assertStatement = trimmed.match(/^assert\s+(.+?)(?:,\s*(.+))?$/);
    if (assertStatement) {
        return [fr ? `assert évalue \`${assertStatement[1]}\`. Si le résultat est False, Python lève AssertionError${assertStatement[2] ? ` avec le message ${assertStatement[2]}` : ''}.` : `assert evaluates \`${assertStatement[1]}\`. If it is False, Python raises AssertionError${assertStatement[2] ? ` with the message ${assertStatement[2]}` : ''}.`, ...expressionOperatorLessons(assertStatement[1], language)];
    }
    const scopeStatement = trimmed.match(/^(global|nonlocal)\s+(.+)$/);
    if (scopeStatement) {
        return [scopeStatement[1] === 'global'
            ? (fr ? `global indique que \`${scopeStatement[2]}\` désigne le nom défini au niveau du module, et non une nouvelle variable locale.` : `global says that \`${scopeStatement[2]}\` refers to the module-level name rather than creating a new local variable.`)
            : (fr ? `nonlocal indique que \`${scopeStatement[2]}\` désigne la variable de la fonction englobante la plus proche.` : `nonlocal says that \`${scopeStatement[2]}\` refers to the variable in the nearest enclosing function.`)];
    }
    const yieldStatement = trimmed.match(/^yield(?:\s+from)?\s*(.*)$/);
    if (yieldStatement) {
        return [fr ? `yield produit \`${yieldStatement[1] || 'None'}\`, suspend le générateur et conserve son état pour la prochaine reprise.` : `yield produces \`${yieldStatement[1] || 'None'}\`, pauses the generator, and preserves its state for the next request.`, ...expressionOperatorLessons(yieldStatement[1], language)];
    }
    const augmented = trimmed.match(/^(.+?)\s*(\+=|-=|\*=|\/=|\/\/=|%=|\*\*=)\s*(.+)$/);
    if (augmented) return augmentedAssignmentExplanation(augmented[1], augmented[2], augmented[3], language);
    const assignment = trimmed.match(/^(.+?)\s*=\s*(?!=)(.+)$/);
    if (assignment) {
        return [
            fr ? `Python évalue d’abord le côté droit \`${assignment[2]}\`, puis stocke le résultat dans \`${assignment[1]}\`.` : `Python evaluates the right-hand side \`${assignment[2]}\` first, then stores the result in \`${assignment[1]}\`.`,
            ...expressionOperatorLessons(assignment[2], language),
        ];
    }
    if (trimmed === 'break') return [fr ? 'break arrête immédiatement la boucle la plus proche ; Python reprend après cette boucle.' : 'break immediately stops the nearest loop; Python resumes after that loop.'];
    if (trimmed === 'continue') return [fr ? 'continue ignore le reste de cette itération et revient au test de la boucle.' : 'continue skips the rest of this iteration and returns to the loop test.'];
    if (trimmed === 'pass') {
        return [fr ? 'pass est seulement un emplacement vide ; il ne résout pas encore le problème.' : 'pass is only an empty placeholder; it does not solve the problem yet.'];
    }
    if (/^[\]}][,;]?$/.test(trimmed)) {
        return [fr ? 'Cette ligne ferme la collection commencée plus haut ; Python peut alors utiliser la valeur complète.' : 'This line closes the collection started above, so Python can now use the complete value.'];
    }
    const mappingEntry = trimmed.match(/^(.+?):\s*(.+),?$/);
    if (mappingEntry) {
        return [fr ? `Cette entrée associe la clé \`${mappingEntry[1]}\` à la valeur \`${mappingEntry[2].replace(/,$/, '')}\` dans le dictionnaire.` : `This dictionary entry maps the key \`${mappingEntry[1]}\` to the value \`${mappingEntry[2].replace(/,$/, '')}\`.`];
    }
    if (/^.+,$/.test(trimmed)) {
        return [fr ? `Cette ligne ajoute la valeur \`${trimmed.replace(/,$/, '')}\` à la collection en cours de construction.` : `This line adds the value \`${trimmed.replace(/,$/, '')}\` to the collection currently being built.`];
    }
    const methodCall = trimmed.match(/^(.+)\.([A-Za-z_]\w*)\((.*)\)$/);
    if (methodCall) {
        return [fr ? `Python évalue d’abord l’objet \`${methodCall[1]}\`, puis appelle sa méthode \`${methodCall[2]}\` avec ${methodCall[3] ? `les arguments \`${methodCall[3]}\`` : 'aucun argument'}.` : `Python first evaluates the object \`${methodCall[1]}\`, then calls its \`${methodCall[2]}\` method with ${methodCall[3] ? `the arguments \`${methodCall[3]}\`` : 'no arguments'}.`];
    }
    const functionCall = trimmed.match(/^([A-Za-z_]\w*)\((.*)\)$/);
    if (functionCall) {
        return [fr ? `Python trouve la fonction \`${functionCall[1]}\`, évalue ${functionCall[2] ? `les arguments \`${functionCall[2]}\` de gauche à droite` : 'cet appel sans argument'}, puis exécute son corps.` : `Python resolves the function \`${functionCall[1]}\`, evaluates ${functionCall[2] ? `the arguments \`${functionCall[2]}\` from left to right` : 'this call with no arguments'}, and then runs its body.`];
    }
    return [fr ? `Python exécute ici l’instruction exacte \`${trimmed}\`; sa valeur ou son effet alimente l’étape suivante du code.` : `Python executes the exact statement \`${trimmed}\` here; its value or side effect feeds the next step of this code.`];
};

const functionIntroduction = (
    code: string,
    functionName: string,
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
    const returnExpression = code.match(/^\s*return\s+(.+)$/m)?.[1]?.trim();
    if (returnExpression) {
        return fr
            ? `Cette ligne définit \`${functionName}(${params})\`. Lors de son appel, la fonction lie ses arguments aux paramètres puis calcule exactement \`${returnExpression}\`.`
            : `This line defines \`${functionName}(${params})\`. When called, the function binds its arguments to the parameters and then calculates exactly \`${returnExpression}\`.`;
    }
    return fr
        ? `Cette ligne définit \`${functionName}(${params})\` et les instructions indentées qui constituent son corps.`
        : `This line defines \`${functionName}(${params})\` and the indented statements that make up its body.`;
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

    const concreteWalkthrough = buildConcreteExpressionWalkthrough(code, language, example);
    if (concreteWalkthrough.length) add('', ...concreteWalkthrough);

    return comments;
};

const extractCallArgumentSets = (code: string, functionName: string) => {
    const results: string[][] = [];
    for (const line of code.split('\n')) {
        if (new RegExp(`^\\s*def\\s+${functionName}\\s*\\(`).test(line)) continue;
        let searchFrom = 0;
        while (searchFrom < line.length) {
            const marker = new RegExp(`\\b${functionName}\\s*\\(`).exec(line.slice(searchFrom));
            if (!marker) break;
            const openIndex = searchFrom + marker.index + marker[0].lastIndexOf('(');
            let depth = 0;
            let quote = '';
            let escaped = false;
            let closeIndex = -1;
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
                else if (char === ')' && --depth === 0) {
                    closeIndex = index;
                    break;
                }
            }
            if (closeIndex < 0) break;
            results.push(splitTopLevel(line.slice(openIndex + 1, closeIndex)));
            searchFrom = closeIndex + 1;
        }
    }
    return results;
};

const illustrativeArgumentScore = (args: string[]) => args.reduce((score, argument) => {
    const value = inferExpression(argument, new Map());
    if (!value.known) return score;
    if (typeof value.value === 'number') return score + Math.min(1000, Math.abs(value.value)) + (value.value !== 0 ? 25 : 0);
    if (typeof value.value === 'string') return score + value.value.length * 4;
    if (Array.isArray(value.value)) return score + value.value.length * 8;
    return score + 1;
}, 0);

const buildConcreteLoopWalkthrough = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    if (!example || !/\bwhile\b/.test(code)) return [];
    const fr = language === 'fr';
    const sourceLines = code.split('\n');
    const definitionIndex = sourceLines.findIndex(line => new RegExp(`^\\s*def\\s+${example.name}\\s*\\(`).test(line));
    if (definitionIndex < 0) return [];
    const definitionIndent = sourceLines[definitionIndex].length - sourceLines[definitionIndex].trimStart().length;
    let functionEnd = sourceLines.length;
    for (let index = definitionIndex + 1; index < sourceLines.length; index += 1) {
        if (!sourceLines[index].trim()) continue;
        const indent = sourceLines[index].length - sourceLines[index].trimStart().length;
        if (indent <= definitionIndent) {
            functionEnd = index;
            break;
        }
    }
    const functionLines = sourceLines.slice(definitionIndex + 1, functionEnd);
    const whileIndex = functionLines.findIndex(line => /^\s*while\s+.+:\s*$/.test(line));
    if (whileIndex < 0) return [];
    const whileLine = functionLines[whileIndex];
    const whileIndent = whileLine.length - whileLine.trimStart().length;
    const condition = whileLine.trim().replace(/^while\s+/, '').replace(/:\s*$/, '');
    let bodyEnd = functionLines.length;
    for (let index = whileIndex + 1; index < functionLines.length; index += 1) {
        if (!functionLines[index].trim()) continue;
        const indent = functionLines[index].length - functionLines[index].trimStart().length;
        if (indent <= whileIndent) {
            bodyEnd = index;
            break;
        }
    }
    const bodyLines = functionLines.slice(whileIndex + 1, bodyEnd);
    if (!bodyLines.length) return [];

    const argumentSets = extractCallArgumentSets(code, example.name)
        .filter(args => args.length >= example.params.length)
        .sort((left, right) => illustrativeArgumentScore(right) - illustrativeArgumentScore(left));
    const selectedArgs = argumentSets[0] || example.args;
    if (!selectedArgs.length) return [];
    const environment = new Map<string, TracedValue>();
    example.params.forEach((param, index) => environment.set(param, inferExpression(selectedArgs[index] || '', environment)));
    if ([...environment.values()].some(value => !value.known)) return [];

    const applyMutation = (trimmed: string) => {
        const augmented = trimmed.match(/^([A-Za-z_]\w*)\s*(\+=|-=|\*=|\/=|\/\/=|%=|\*\*=)\s*(.+)$/);
        if (augmented) {
            const [, target, operator, rightExpression] = augmented;
            const before = environment.get(target);
            const right = inferExpression(rightExpression, environment);
            const binaryOperator = operator.slice(0, -1);
            const after = inferExpression(`${target} ${binaryOperator} ${rightExpression}`, environment);
            if (!before?.known || !right.known || !after.known) return null;
            environment.set(target, after);
            return `${target} ${operator} ${rightExpression} → ${target} = ${displayValue(before.value)} ${binaryOperator} ${displayValue(right.value)} = ${displayValue(after.value)}`;
        }
        const assignment = trimmed.match(/^([A-Za-z_]\w*)\s*=\s*(?!=)(.+)$/);
        if (assignment) {
            const value = inferExpression(assignment[2], environment);
            if (!value.known) return null;
            environment.set(assignment[1], value);
            return `${assignment[1]} = ${assignment[2]} → ${displayValue(value.value)}`;
        }
        return null;
    };

    for (const line of functionLines.slice(0, whileIndex)) {
        const trimmed = stripInlinePythonComment(line).trim();
        if (!trimmed || /^(?:if|elif|else|return|pass)\b/.test(trimmed)) continue;
        applyMutation(trimmed);
    }

    const initialCondition = inferExpression(condition, environment);
    if (!initialCondition.known || !initialCondition.value) return [];
    const initialValues = [...environment.entries()]
        .filter(([name]) => !name.startsWith('@'))
        .map(([name, value]) => `${name} = ${displayValue(value.value)}`);
    const callLabel = `${example.name}(${selectedArgs.join(', ')})`;
    const walkthrough: string[] = [
        fr ? `Exemple pas à pas pour ${callLabel} :` : `Step-by-step example for ${callLabel}:`,
        '',
        fr ? 'Départ :' : 'Start:',
        ...initialValues,
        '',
    ];
    let iterations = 0;
    let terminated = false;
    while (iterations < 12) {
        const conditionValue = inferExpression(condition, environment);
        if (!conditionValue.known || !conditionValue.value) {
            terminated = Boolean(conditionValue.known);
            break;
        }
        iterations += 1;
        walkthrough.push(fr ? `Itération ${iterations} :` : `Loop ${iterations}:`);
        const inactiveIndents: number[] = [];
        let breakLoop = false;
        for (const line of bodyLines) {
            const indent = line.length - line.trimStart().length;
            while (inactiveIndents.length && indent <= inactiveIndents[inactiveIndents.length - 1]) inactiveIndents.pop();
            if (inactiveIndents.length) continue;
            const trimmed = stripInlinePythonComment(line).trim();
            if (!trimmed) continue;
            const branch = trimmed.match(/^if\s+(.+):$/);
            if (branch) {
                const value = inferExpression(branch[1], environment);
                walkthrough.push(
                    `${fr ? 'Opération' : 'Operation'}: ${branch[1]} → ${value.known ? displayValue(Boolean(value.value)) : fr ? 'valeur inconnue' : 'unknown value'}`,
                    `${fr ? 'Valeur intermédiaire et type' : 'Intermediate value and type'}: ${fr ? 'résultat de la condition' : 'condition result'} = ${value.known ? displayValue(Boolean(value.value)) : fr ? 'inconnu' : 'unknown'} (bool)`,
                );
                if (!value.known || !value.value) inactiveIndents.push(indent);
                continue;
            }
            if (trimmed === 'break') {
                walkthrough.push(fr ? 'break → arrêt immédiat de la boucle' : 'break → stop the loop immediately');
                breakLoop = true;
                break;
            }
            if (/^(?:continue|return)\b/.test(trimmed)) continue;
            const mutation = applyMutation(trimmed);
            if (mutation) {
                walkthrough.push(`${fr ? 'Opération' : 'Operation'}: ${mutation}`);
                const target = trimmed.match(/^([A-Za-z_]\w*)/)?.[1];
                const value = target ? environment.get(target) : null;
                if (target && value?.known) walkthrough.push(
                    `${fr ? 'Valeur intermédiaire et type' : 'Intermediate value and type'}: ${target} = ${displayValue(value.value)} (${value.type})`,
                );
            }
        }
        walkthrough.push('');
        if (breakLoop) {
            terminated = true;
            break;
        }
    }
    const finalCondition = inferExpression(condition, environment);
    if (finalCondition.known && !finalCondition.value) terminated = true;
    if (!terminated) {
        walkthrough.push(fr ? 'La trace est arrêtée après 12 itérations pour garder l’explication lisible.' : 'The trace stops after 12 iterations to keep the explanation readable.', '');
    } else {
        walkthrough.push(
            fr ? `La condition \`${condition}\` vaut maintenant False, donc la boucle s’arrête.` : `The condition \`${condition}\` is now False, so the while loop stops.`,
            '',
        );
    }
    const returnLine = functionLines.slice(bodyEnd).map(line => line.trim()).find(line => /^return\b/.test(line));
    if (returnLine) {
        const expression = returnLine.replace(/^return\s*/, '');
        const result = inferExpression(expression, environment);
        if (result.known) walkthrough.push(fr ? 'Résultat final :' : 'Final result:', displayValue(result.value), '');
    }
    const changedValues = initialValues
        .map(value => value.split(' = ')[0])
        .map(name => environment.get(name)?.known ? `${name}: ${initialValues.find(item => item.startsWith(`${name} = `))?.split(' = ').slice(1).join(' = ')} → ${displayValue(environment.get(name)?.value)}` : '')
        .filter(Boolean);
    if (changedValues.length) walkthrough.push(fr ? 'Trajet de l’état :' : 'State path:', ...changedValues);
    return walkthrough;
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
    const whileMatch = code.match(/while\s+(.+):/);
    if (whileMatch) {
        const steps: string[] = [];
        const initializers = [...code.matchAll(/^\s*([A-Za-z_]\w*)\s*=\s*(?!=)(.+)$/gm)]
            .filter(match => !match[0].includes('while '))
            .slice(0, 3)
            .map(match => `\`${match[1]} = ${match[2].trim()}\``);
        if (initializers.length) steps.push(fr
            ? `Initialiser l’état de départ avec ${initializers.join(', ')}.`
            : `Initialize the starting state with ${initializers.join(', ')}.`);
        steps.push(fr
            ? `Tester \`${whileMatch[1].trim()}\` avant chaque itération et continuer seulement pendant que cette condition est True.`
            : `Test \`${whileMatch[1].trim()}\` before every iteration and continue only while that condition is True.`);
        const mutations = [...code.matchAll(/^\s*([A-Za-z_]\w*)\s*(\+=|-=|\*=|\/=|\/\/=|%=|\*\*=)\s*(.+)$/gm)].slice(0, 4);
        for (const mutation of mutations) {
            const binaryOperator = mutation[2].slice(0, -1);
            steps.push(fr
                ? `Mettre à jour \`${mutation[1]}\` avec \`${mutation[1]} = ${mutation[1]} ${binaryOperator} ${mutation[3].trim()}\`.`
                : `Update \`${mutation[1]}\` using \`${mutation[1]} = ${mutation[1]} ${binaryOperator} ${mutation[3].trim()}\`.`);
        }
        if (/\/\/=\s*10\b/.test(code)) steps.push(fr
            ? 'Supprimer un chiffre décimal à droite à chaque division entière par 10.'
            : 'Remove one decimal digit from the right on every floor division by 10.');
        const returnedValues = [...code.matchAll(/^\s*return\s+(.+)$/gm)].map(match => match[1].trim());
        const returned = returnedValues[returnedValues.length - 1];
        if (returned) steps.push(fr ? `Renvoyer finalement \`${returned}\`.` : `Finally return \`${returned}\`.`);
        return steps.slice(0, 8);
    }
    const steps: string[] = [];
    if (/\.split\s*\(/.test(code)) steps.push(fr ? 'La chaîne est découpée en éléments séparés.' : 'The string is split into separate pieces.');
    if (/\bmap\s*\(\s*int\s*,/.test(code) || /\bint\s*\(/.test(code)) steps.push(fr ? 'Les morceaux numériques sont convertis du texte vers des entiers.' : 'Number-like pieces are converted from text into integers.');
    if (/\bmap\s*\(\s*float\s*,/.test(code) || /\bfloat\s*\(/.test(code)) steps.push(fr ? 'Les morceaux numériques sont convertis en nombres décimaux.' : 'Number-like pieces are converted into decimal numbers.');
    if (/\bfilter\s*\(|\bif\b/.test(code)) steps.push(fr ? 'Une condition décide quelles valeurs sont conservées.' : 'A condition decides which values are kept.');
    if (/\b(?:for|while)\b/.test(code)) steps.push(fr ? 'La boucle traite les valeurs dans l’ordre.' : 'The loop processes the values in order.');
    if (/\bsorted\s*\(|\.sort\s*\(/.test(code)) steps.push(fr ? 'Les valeurs sont placées dans l’ordre demandé.' : 'The values are placed in the required order.');
    if (/\blist\s*\(|\[[^\]]+\bfor\b/.test(code)) steps.push(fr ? 'Les résultats sont regroupés dans une liste.' : 'The results are collected into a list.');
    if (!steps.length) {
        const definition = code.match(/def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/);
        const returnExpression = code.match(/^\s*return\s+(.+)$/m)?.[1]?.trim();
        if (definition) steps.push(fr
            ? `Lier les arguments reçus aux paramètres ${definition[2].trim() || '(aucun)'}.`
            : `Bind the supplied arguments to the parameters ${definition[2].trim() || '(none)'}.`);
        if (returnExpression) {
            steps.push(fr
                ? `Évaluer précisément l’expression \`${returnExpression}\` en respectant les parenthèses et l’ordre des opérations.`
                : `Evaluate the exact expression \`${returnExpression}\` using its parentheses and Python's order of operations.`);
            steps.push(fr
                ? `Renvoyer le résultat de \`${returnExpression}\` à l’appelant.`
                : `Return the result of \`${returnExpression}\` to the caller.`);
        } else {
            const meaningfulLines = code.split('\n').map(line => stripInlinePythonComment(line).trim()).filter(Boolean).slice(0, 3);
            steps.push(fr
                ? `Exécuter dans l’ordre les instructions propres à cette solution : ${meaningfulLines.map(line => `\`${line}\``).join(', ')}.`
                : `Run this solution's specific statements in order: ${meaningfulLines.map(line => `\`${line}\``).join(', ')}.`);
        }
    }
    return steps.slice(0, 8);
};

export const buildDetailedCodeExplanation = (
    userCode: string,
    solution: string,
    language: AiCodeExplanationLanguage = 'en',
    problemDescription = '',
) => {
    const source = (isUsefulUserCode(userCode) ? userCode.trim() : primarySolutionCode(solution)).trim();
    const fr = language === 'fr';
    if (!source) {
        return fr
            ? 'Explication du code : aucun code n’est encore disponible. Écrivez ou exécutez une solution pour obtenir une explication ligne par ligne.'
            : 'Code explanation: No code is available yet. Write or run a solution to receive a line-by-line explanation.';
    }

    const baseExample = extractFunctionExample(source) || extractFunctionExample(primarySolutionCode(solution));
    const illustrativeArgs = baseExample
        ? extractCallArgumentSets(source, baseExample.name)
            .filter(args => args.length >= baseExample.params.length)
            .sort((left, right) => illustrativeArgumentScore(right) - illustrativeArgumentScore(left))[0]
        : undefined;
    const example = baseExample && illustrativeArgs ? { ...baseExample, args: illustrativeArgs } : baseExample;
    const annotated: string[] = [];
    const sourceLines = source.split('\n').slice(0, MAX_SOURCE_LINES);
    const expandedLesson = buildExpandedOperationLesson(source, language, example);
    let lessonInserted = false;

    for (const line of sourceLines) {
        const trimmed = stripInlinePythonComment(line).trim();
        if (!trimmed || trimmed.startsWith('#')) {
            if (annotated.length && annotated[annotated.length - 1] !== '') annotated.push('');
            continue;
        }
        const indent = line.match(/^\s*/)?.[0] || '';
        const definition = trimmed.match(/^def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*:/);
        if (definition) {
            const params = splitTopLevel(definition[2])
                .map(param => param.trim().replace(/^\*{1,2}/, '').split(/[:=]/)[0].trim())
                .filter(Boolean);
            addComment(annotated, indent, [
                functionIntroduction(source, definition[1], definition[2].trim(), language),
                '',
                ...buildParameterLesson(params, example, problemDescription, language),
            ]);
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
        }
        addComment(annotated, indent, lineExplanation(trimmed, language, example));
        annotated.push(normalizeDisplayLine(line, example));
    }

    if (!lessonInserted && expandedLesson.length) {
        annotated.push('');
        addComment(annotated, '', expandedLesson);
    }

    const callableLesson = buildCallableSemanticsLesson(source, language);
    if (callableLesson.length) {
        annotated.push('');
        annotated.push('');
        addComment(annotated, '', callableLesson);
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

    const loopWalkthrough = buildConcreteLoopWalkthrough(source, language, example);
    if (loopWalkthrough.length) {
        annotated.push('');
        annotated.push('');
        addComment(annotated, '', [
            fr ? 'Trajet complet des valeurs pour l’exemple affiché :' : 'Complete value path for the shown example:',
            '',
            ...loopWalkthrough,
        ]);
    }

    const concreteTraceIsComplete = loopWalkthrough.some(line => /^(?:Operation|Opération):/.test(line))
        && loopWalkthrough.some(line => /^(?:Intermediate value and type|Valeur intermédiaire et type):/.test(line));
    const executionTrace = concreteTraceIsComplete ? [] : buildUniversalExecutionTrace(source, language, example);
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
