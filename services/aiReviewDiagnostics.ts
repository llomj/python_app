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

    if (request.graderPassed) {
        return {
            verdict: 'likely_correct',
            confidence: 0.99,
            explanation: 'The deterministic grader already passed this solution.',
            suggestedFix: 'No fix needed; the deterministic grader already accepted this solution.',
            source: 'diagnostic',
        };
    }

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

    if (hasInput(code)) {
        notes.push('The code uses input(); only script/input problems should ask for interactive input during grading.');
        fixes.push('If this is a function problem, accept parameters instead of calling input().');
    }

    if (!notes.length) {
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
