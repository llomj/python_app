export type AiCodeExplanationLanguage = 'en' | 'fr';

const MAX_SOURCE_LINES = 24;
const MAX_ANNOTATED_LINES = 180;

const primarySolutionCode = (solution: string) => {
    const lines = solution.trim().split('\n');
    const start = lines.findIndex(line => /^\s*(?:def|class|from\s+|import\s+)/.test(line));
    const selected = start >= 0 ? lines.slice(start) : lines;
    const result: string[] = [];

    for (const line of selected) {
        if (result.length && /^#\s*(?:Using|Script|Direct|Built|Manual|Alternative)\b/i.test(line.trim())) break;
        if (
            result.length
            && line.trim()
            && !/^\s/.test(line)
            && /^(?:def|class)\s+/.test(line)
            && result.some(existing => /^(?:def|class)\s+/.test(existing.trim()))
        ) break;
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
    const calls = [...code.matchAll(new RegExp(`\\b${name}\\s*\\(([^\\n()]*(?:\\([^\\n()]*\\)[^\\n()]*)*)\\)`, 'g'))];
    const call = calls.find(match => {
        const prefix = code.slice(Math.max(0, (match.index || 0) - 5), match.index || 0);
        return !/\bdef\s*$/.test(prefix) && match[1].trim();
    });
    const args = call?.[1]
        .split(/,(?=(?:[^'"]|'[^']*'|"[^"]*")*$)/)
        .map(arg => arg.trim())
        .filter(Boolean) || [];
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
    for (const line of lines) target.push(line ? `${indent}# ${line}` : `${indent}#`);
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

    const summary = transformationSummary(source, language, example);
    annotated.push('');
    annotated.push('');
    addComment(annotated, '', [
        fr ? 'Cette solution effectue les étapes suivantes :' : 'So this function is doing these things:',
        '',
        ...summary.map((step, index) => `${index + 1}. ${step}`),
    ]);

    const bounded = annotated.slice(0, MAX_ANNOTATED_LINES).join('\n').trim();
    const intro = fr
        ? 'Explication du code : voici le code réel expliqué à l’endroit où chaque opération se produit. Les commentaires montrent les types, les valeurs intermédiaires et le trajet vers le résultat.'
        : 'Code explanation: Here is the actual code explained where each operation happens. The comments show the data types, intermediate values, and path to the final result.';
    return `${intro}\n\`\`\`python\n${bounded}\n\`\`\``;
};
