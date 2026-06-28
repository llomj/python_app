import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';

const hasFunctionDefinition = (code: string) => /\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(code);
const hasReturn = (code: string) => /\breturn\b/.test(code);
const hasPrint = (code: string) => /\bprint\s*\(/.test(code);
const hasInput = (code: string) => /\binput\s*\(/.test(code);

export const buildDiagnosticReview = (request: AiReviewRequest): AiReviewResult => {
    const code = request.userCode || '';
    const graderMessage = request.graderMessage || '';
    const notes: string[] = [];
    let confidence = 0.35;
    let verdict: AiReviewResult['verdict'] = 'unclear';

    if (request.graderPassed) {
        return {
            verdict: 'likely_correct',
            confidence: 0.99,
            explanation: 'The deterministic grader already passed this solution.',
            source: 'diagnostic',
        };
    }

    if (/Missing required source pattern|Missing required syntax/i.test(graderMessage)) {
        verdict = 'likely_incorrect';
        confidence = 0.82;
        notes.push('The grader failed because the problem requires specific syntax or a specific API call.');
    }

    if (/Could not find a callable|function/i.test(graderMessage) && !hasFunctionDefinition(code)) {
        verdict = 'likely_incorrect';
        confidence = Math.max(confidence, 0.8);
        notes.push('The answer does not define a function, but this problem appears to require one.');
    }

    if (/Expected .* got/i.test(graderMessage)) {
        verdict = verdict === 'likely_incorrect' ? verdict : 'unclear';
        confidence = Math.max(confidence, 0.55);
        notes.push('The code ran, but at least one hidden test produced a different result.');
    }

    if (hasPrint(code) && !hasReturn(code) && /Expected .* got/i.test(graderMessage)) {
        notes.push('The code prints output but may need to return a value from the required function.');
    }

    if (hasInput(code)) {
        notes.push('The code uses input(); the grader can test this only when the problem is configured as a script/input problem.');
    }

    if (!notes.length) {
        notes.push('The deterministic grader failed, but the diagnostic reviewer could not identify a single obvious cause.');
    }

    return {
        verdict,
        confidence,
        explanation: notes.join(' '),
        suggestedFix: 'Compare the required function name, return value, and edge cases against the problem statement.',
        source: 'diagnostic',
    };
};
