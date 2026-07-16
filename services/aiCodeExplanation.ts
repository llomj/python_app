export type AiCodeExplanationLanguage = 'en' | 'fr';

const MAX_SOURCE_LINES = 24;
const MAX_ANNOTATED_LINES = 110;

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
                ? `Cette fonction reçoit ${params ? `les données \`${params}\`` : 'aucun argument'} et regroupe la logique de la solution.`
                : `This function receives ${params ? `the input data \`${params}\`` : 'no arguments'} and groups the solution logic.`,
            example?.args.length
                ? (fr ? `Exemple d'appel : ${example.name}(${example.args.join(', ')})` : `Example call: ${example.name}(${example.args.join(', ')})`)
                : '',
        ].filter(Boolean);
    }
    if (/^class\s+/.test(trimmed)) {
        return [fr ? 'Cette classe définit un nouveau type d’objet et regroupe ses données et ses méthodes.' : 'This class defines a new object type and groups its data and methods.'];
    }
    if (/^(?:from|import)\s+/.test(trimmed)) {
        return [fr ? 'Cette ligne charge un outil Python utilisé plus bas dans le programme.' : 'This line loads a Python tool used later in the program.'];
    }
    if (/^return\b/.test(trimmed)) {
        return [fr ? '`return` renvoie le résultat final à l’appelant et au correcteur.' : '`return` sends the final result back to the caller and grader.'];
    }
    if (/^print\s*\(/.test(trimmed)) {
        return [fr ? '`print(...)` appelle ou évalue son contenu, puis affiche le résultat dans la sortie.' : '`print(...)` calls or evaluates its contents, then displays the result in the output panel.'];
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
        return [fr ? '`pass` est seulement un emplacement vide ; il ne résout pas encore le problème.' : '`pass` is only an empty placeholder; it does not solve the problem yet.'];
    }
    return [fr ? 'Python exécute cette instruction à cet endroit du programme.' : 'Python executes this statement at this point in the program.'];
};

const operationComments = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    const comments: string[] = [];
    const add = (...lines: string[]) => comments.push(...lines.filter(Boolean));
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
                ? `\`${variable}.split(${JSON.stringify(delimiter)})\` découpe une grande chaîne chaque fois qu’il trouve ${JSON.stringify(delimiter)}.`
                : `\`${variable}.split(${JSON.stringify(delimiter)})\` splits one large string wherever it finds ${JSON.stringify(delimiter)}.`,
        );
        if (textValue !== null) {
            const pieces = textValue.split(delimiter);
            add(
                '',
                fr ? `Avant : ${JSON.stringify(textValue)}` : `Before: ${JSON.stringify(textValue)}`,
                fr ? `Après split : ${pythonList(pieces)}` : `After split: ${pythonList(pieces)}`,
                fr ? 'Les éléments obtenus sont encore des chaînes de caractères.' : 'The resulting items are still strings.',
            );
        }
    }

    const mapMatch = code.match(/\bmap\(\s*([A-Za-z_]\w*)\s*,/);
    if (mapMatch) {
        const converter = mapMatch[1];
        add(
            '',
            fr
                ? `\`map(${converter}, ...)\` applique \`${converter}()\` à chaque élément, un par un.`
                : `\`map(${converter}, ...)\` applies \`${converter}()\` to every item, one at a time.`,
        );
        if (converter === 'int' && splitMatch) {
            const rawValue = argumentByParam.get(splitMatch[1]);
            const textValue = rawValue ? unquote(rawValue) : null;
            if (textValue !== null) {
                const pieces = textValue.split(splitMatch[3]);
                const converted = pieces.map(piece => Number.parseInt(piece, 10)).filter(value => Number.isFinite(value));
                add(
                    ...pieces.slice(0, 5).map((piece, index) => `int(${JSON.stringify(piece)}) -> ${converted[index]}`),
                    fr ? 'La différence importante : `"10"` est du texte, tandis que `10` est un entier.' : 'The important difference: `"10"` is text, while `10` is an integer.',
                );
            }
        }
    }

    if (/\blist\s*\(/.test(code)) {
        add(
            '',
            fr ? '`list(...)` collecte les valeurs produites dans une vraie liste réutilisable.' : '`list(...)` collects the produced values into a real, reusable list.',
        );
    }
    if (/\bfilter\s*\(/.test(code)) add('', fr ? '`filter(...)` conserve seulement les éléments pour lesquels le test est vrai.' : '`filter(...)` keeps only the items whose test is true.');
    if (/\bsorted\s*\(/.test(code)) add('', fr ? '`sorted(...)` crée une nouvelle liste triée sans modifier l’original.' : '`sorted(...)` creates a new sorted list without changing the original.');
    if (/\bsum\s*\(/.test(code)) add('', fr ? '`sum(...)` additionne toutes les valeurs numériques de l’itérable.' : '`sum(...)` adds every numeric value from the iterable.');
    if (/\blen\s*\(/.test(code)) add('', fr ? '`len(...)` compte le nombre d’éléments.' : '`len(...)` counts how many items are present.');
    if (/\brange\s*\(/.test(code)) add('', fr ? '`range(...)` produit une suite de nombres utilisée généralement par une boucle.' : '`range(...)` produces a number sequence, usually for a loop.');
    if (/\[[^\]]*:[^\]]*\]/.test(code)) add('', fr ? 'La syntaxe `[début:fin:pas]` extrait une tranche ; la position `fin` est exclue.' : 'The `[start:stop:step]` syntax extracts a slice; the `stop` position is excluded.');
    if (/\[-1\]/.test(code)) add('', fr ? '`[-1]` sélectionne le dernier élément de la séquence.' : '`[-1]` selects the final item in the sequence.');
    if (/\[[^\]]+\bfor\b[^\]]+\bin\b[^\]]+\]/.test(code)) add('', fr ? 'La compréhension de liste construit une nouvelle liste en transformant chaque élément.' : 'The list comprehension builds a new list by transforming each item.');
    if (/\.\s*(?:append|extend|insert|remove|pop|sort|reverse)\s*\(/.test(code)) add('', fr ? 'Cette méthode modifie directement la liste existante.' : 'This method changes the existing list directly.');
    if (/\.\s*(?:get|keys|values|items)\s*\(/.test(code)) add('', fr ? 'Cette méthode lit une partie précise du dictionnaire : clés, valeurs ou paires clé-valeur.' : 'This method reads a specific view of the dictionary: keys, values, or key-value pairs.');
    if (/\blambda\b/.test(code)) add('', fr ? '`lambda` crée une petite fonction anonyme dont l’expression devient automatiquement le résultat.' : '`lambda` creates a small anonymous function whose expression automatically becomes its result.');

    return comments;
};

const transformationSummary = (
    code: string,
    language: AiCodeExplanationLanguage,
    example: ReturnType<typeof extractFunctionExample>,
) => {
    const fr = language === 'fr';
    const steps: string[] = [];
    if (example?.args.length) steps.push(fr ? `Les arguments ${example.args.join(', ')} entrent dans \`${example.name}()\`.` : `The arguments ${example.args.join(', ')} enter \`${example.name}()\`.`);
    if (/\.split\s*\(/.test(code)) steps.push(fr ? 'La chaîne est découpée en éléments séparés.' : 'The string is split into separate pieces.');
    if (/\bmap\s*\(\s*int\s*,/.test(code) || /\bint\s*\(/.test(code)) steps.push(fr ? 'Les morceaux numériques sont convertis du texte vers des entiers.' : 'Number-like pieces are converted from text into integers.');
    if (/\bmap\s*\(\s*float\s*,/.test(code) || /\bfloat\s*\(/.test(code)) steps.push(fr ? 'Les morceaux numériques sont convertis en nombres décimaux.' : 'Number-like pieces are converted into decimal numbers.');
    if (/\bfilter\s*\(|\bif\b/.test(code)) steps.push(fr ? 'Une condition décide quelles valeurs sont conservées.' : 'A condition decides which values are kept.');
    if (/\b(?:for|while)\b/.test(code)) steps.push(fr ? 'La boucle traite les valeurs dans l’ordre.' : 'The loop processes the values in order.');
    if (/\bsorted\s*\(|\.sort\s*\(/.test(code)) steps.push(fr ? 'Les valeurs sont placées dans l’ordre demandé.' : 'The values are placed in the required order.');
    if (/\blist\s*\(|\[[^\]]+\bfor\b/.test(code)) steps.push(fr ? 'Les résultats sont regroupés dans une liste.' : 'The results are collected into a list.');
    if (/\breturn\b/.test(code)) steps.push(fr ? 'La fonction renvoie le résultat final.' : 'The function returns the final result.');
    if (/\bprint\s*\(/.test(code)) steps.push(fr ? '`print()` affiche le résultat visible.' : '`print()` displays the visible result.');
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

    for (const line of sourceLines) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith('#')) {
            if (annotated.length && annotated[annotated.length - 1] !== '') annotated.push('');
            continue;
        }
        const indent = line.match(/^\s*/)?.[0] || '';
        addComment(annotated, indent, lineExplanation(trimmed, language, example));
        annotated.push(line);
    }

    const operations = operationComments(source, language, example);
    if (operations.length) {
        annotated.push('');
        addComment(annotated, '', [
            fr ? 'Transformation des données, étape par étape :' : 'Data transformation, step by step:',
            ...operations,
        ]);
    }

    const summary = transformationSummary(source, language, example);
    annotated.push('');
    addComment(annotated, '', [
        fr ? 'Résumé du déroulement :' : 'Workflow summary:',
        ...summary.map((step, index) => `${index + 1}. ${step}`),
    ]);

    const bounded = annotated.slice(0, MAX_ANNOTATED_LINES).join('\n').trim();
    const intro = fr
        ? 'Explication du code : voici le code réel expliqué à l’endroit où chaque opération se produit. Les commentaires montrent les types, les valeurs intermédiaires et le trajet vers le résultat.'
        : 'Code explanation: Here is the actual code explained where each operation happens. The comments show the data types, intermediate values, and path to the final result.';
    return `${intro}\n\`\`\`python\n${bounded}\n\`\`\``;
};
