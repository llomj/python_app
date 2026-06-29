import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';

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
        return {
            verdict: 'likely_correct',
            confidence: 0.99,
            explanation: 'The deterministic grader already passed this solution.',
            suggestedFix: 'No fix needed; the deterministic grader already accepted this solution.',
            source: 'diagnostic',
        };
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

    return {
        verdict,
        confidence,
        explanation: notes.join(' '),
        suggestedFix: fixes.length
            ? [...new Set(fixes)].join(' ')
            : 'Compare the required function name, return value, and edge cases against the problem statement.',
        source: 'diagnostic',
    };
};
