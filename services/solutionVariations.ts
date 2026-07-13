import type { AutoGrader } from '../graders';
import { INVALID_SOLUTION_SECTION_INDEXES } from './solutionSectionManifest';
import { SOLUTION_REFERENCE_OVERRIDES } from './solutionReferenceOverrides';
import { INVALID_SOLUTION_BODY_KEYS } from './solutionBehaviorManifest';
import { GENERATED_SOLUTION_ALTERNATIVES } from './generatedSolutionAlternatives';

interface SolutionSection {
    heading: string;
    body: string;
    index: number;
}

const HEADING_PATTERN = /^#\s*(?:[-=]+\s*)?(Using|Approach|Method|Version|Script|Direct|Built|Manual|Alternative|Try|Another|Equivalent|Convert|Modify|Consider|Nested|Advanced|Callable|Example|Reference)\b/i;

const normalizeCode = (code: string) => code
    .replace(/#.*$/gm, '')
    .replace(/\s+/g, ' ')
    .trim();

export const solutionBodyKey = (code: string): string => {
    const normalized = normalizeCode(code);
    let hash = 0x811c9dc5;
    for (let index = 0; index < normalized.length; index += 1) {
        hash ^= normalized.charCodeAt(index);
        hash = Math.imul(hash, 0x01000193);
    }
    return (hash >>> 0).toString(16).padStart(8, '0');
};

const parseSections = (solution: string): { prefix: string; sections: SolutionSection[] } => {
    const prefix: string[] = [];
    const sections: SolutionSection[] = [];
    let current: SolutionSection | null = null;

    for (const line of solution.split('\n')) {
        if (HEADING_PATTERN.test(line)) {
            if (current) sections.push({ ...current, body: current.body.trim() });
            current = { heading: line.trim(), body: '', index: sections.length };
            continue;
        }
        if (current) current.body += `${current.body ? '\n' : ''}${line}`;
        else prefix.push(line);
    }
    if (current) sections.push({ ...current, body: current.body.trim() });

    if (sections.length === 0) {
        sections.push({ heading: '# Reference approach', body: solution.trim(), index: 0 });
    }
    return { prefix: prefix.join('\n').trim(), sections };
};

const splitRepeatedCallableDefinitions = (
    section: SolutionSection,
    grader?: AutoGrader,
): SolutionSection[] => {
    if (!grader || grader.functionNames.length === 0) return [section];
    const names = new Set(grader.functionNames);
    const lines = section.body.split('\n');
    const definitions = lines.flatMap((line, lineIndex) => {
        const match = line.match(/^(?:async\s+)?(?:def|class)\s+([A-Za-z_]\w*)\b/);
        return match && names.has(match[1]) ? [{ lineIndex, name: match[1] }] : [];
    });
    const counts = new Map<string, number>();
    for (const definition of definitions) counts.set(definition.name, (counts.get(definition.name) ?? 0) + 1);
    const repeatedName = [...counts.entries()].sort((left, right) => right[1] - left[1])[0];
    if (!repeatedName || repeatedName[1] < 2) return [section];

    const starts = definitions.filter(definition => definition.name === repeatedName[0]).map(definition => definition.lineIndex);
    return starts.map((start, subIndex) => {
        const end = starts[subIndex + 1] ?? lines.length;
        const segment = lines.slice(start, end);
        const techniqueComment = segment
            .slice(1, 6)
            .map(line => line.trim())
            .find(line => /^#\s*Using\b/i.test(line));
        return {
            heading: techniqueComment ?? (subIndex === 0 ? section.heading : `# Alternative implementation ${subIndex + 1}`),
            body: [subIndex === 0 ? lines.slice(0, start).join('\n').trim() : '', segment.join('\n').trim()]
                .filter(Boolean)
                .join('\n'),
            index: section.index,
        };
    });
};

const requiredSyntaxScore = (body: string, grader?: AutoGrader): number => {
    if (!grader) return 0;
    let score = 0;
    const nodeChecks: Record<string, RegExp> = {
        For: /\bfor\b/,
        While: /\bwhile\b/,
        Lambda: /\blambda\b/,
        FunctionDef: /\bdef\s+[A-Za-z_]\w*\s*\(/,
        AsyncFunctionDef: /\basync\s+def\b/,
        ClassDef: /\bclass\s+[A-Za-z_]\w*/,
        ListComp: /\[[^\n]*\bfor\b[^\n]*\]/,
        SetComp: /\{[^\n]*\bfor\b[^\n]*\}/,
        DictComp: /\{[^\n]*:[^\n]*\bfor\b[^\n]*\}/,
        GeneratorExp: /\([^\n]*\bfor\b[^\n]*\)/,
        Try: /\btry\s*:/,
        With: /\bwith\b/,
        Match: /\bmatch\b/,
    };

    for (const requirement of grader.requiredNodePatterns ?? []) {
        const pattern = nodeChecks[requirement.nodeType];
        if (pattern?.test(body)) score += 8;
    }
    const callRequirements = [
        ...(grader.requiredCallPatterns ?? []),
        ...(grader.requiredAnyCallPatterns ?? []),
    ];
    for (const requirement of callRequirements) {
        const escaped = requirement.functionName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        if (new RegExp(`(?:\\.|\\b)${escaped}\\s*\\(`).test(body)) score += 5;
    }
    if ((grader.requiredUnpackPatterns?.length ?? 0) > 0 && /(?:^|[,([])\s*\*[A-Za-z_]\w*/m.test(body)) score += 8;
    if ((grader.requiredBoolOps ?? []).includes('And') && /\band\b/.test(body)) score += 4;
    if ((grader.requiredBoolOps ?? []).includes('Or') && /\bor\b/.test(body)) score += 4;
    return score;
};

const definesRequestedCallable = (body: string, grader?: AutoGrader): boolean => {
    if (!grader || grader.mode === 'script' || grader.functionNames.length === 0) return true;
    return grader.functionNames.some(name => {
        const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        return new RegExp(`\\b(?:def|class)\\s+${escaped}\\b|^\\s*${escaped}\\s*=`, 'm').test(body);
    });
};

const indent = (code: string, spaces: number) => {
    const padding = ' '.repeat(spaces);
    return code.split('\n').map(line => line ? `${padding}${line}` : '').join('\n');
};

const makeNestedVariation = (body: string) => [
    '# Nested function approach (intermediate)',
    'def run_solution():',
    indent(body, 4),
    '',
    'run_solution()',
].join('\n');

const makeClassVariation = (body: string, exerciseId: number) => [
    '# Callable class approach (advanced)',
    `class Exercise${exerciseId}Solution:`,
    '    @staticmethod',
    '    def run():',
    indent(body, 8),
    '',
    `Exercise${exerciseId}Solution.run()`,
].join('\n');

/**
 * Produces a compact set of distinct examples without mutating the canonical
 * solution used by the grader and Problem AI.
 */
export const buildSolutionVariations = (
    solution: string,
    exerciseId: number,
    grader?: AutoGrader,
): string => {
    const generatedAlternatives = GENERATED_SOLUTION_ALTERNATIVES[exerciseId];
    if (!SOLUTION_REFERENCE_OVERRIDES[exerciseId] && generatedAlternatives?.length >= 3) {
        return generatedAlternatives.slice(0, 4).map((alternative, index) => [
            `# Example ${index + 1}: ${index === 0 ? 'simplest reference' : alternative.heading.replace(/^#\s*/, '')}`,
            alternative.body,
        ].join('\n')).join('\n\n');
    }
    const effectiveSolution = SOLUTION_REFERENCE_OVERRIDES[exerciseId] ?? solution;
    const { prefix, sections } = parseSections(effectiveSolution);
    const invalidIndexes = new Set(SOLUTION_REFERENCE_OVERRIDES[exerciseId]
        ? []
        : (INVALID_SOLUTION_SECTION_INDEXES[exerciseId] ?? []));
    const invalidBodyKeys = new Set(INVALID_SOLUTION_BODY_KEYS[exerciseId] ?? []);
    const expandedSections = sections.flatMap(section => splitRepeatedCallableDefinitions(section, grader));
    const syntaxSafeSections = expandedSections.filter(section => (
        section.body.trim()
        && !invalidIndexes.has(section.index)
        && definesRequestedCallable(section.body, grader)
    ));
    const ranked = syntaxSafeSections
        .filter(section => (
            !invalidBodyKeys.has(solutionBodyKey(section.body))
        ))
        .map(section => ({ ...section, score: requiredSyntaxScore(section.body, grader) }))
        .sort((left, right) => right.score - left.score || left.index - right.index);
    const safeFallback = syntaxSafeSections[0];
    const reference = ranked[0] ?? (safeFallback
        ? { ...safeFallback, score: requiredSyntaxScore(safeFallback.body, grader) }
        : { heading: '# Reference approach', body: solution.trim(), index: 0, score: 0 });
    const requiredScore = reference.score;
    const selected: SolutionSection[] = [];
    const seen = new Set<string>();

    if (ranked.length === 0 && safeFallback) {
        selected.push(safeFallback);
        seen.add(normalizeCode(safeFallback.body));
    }

    for (const section of ranked) {
        if (selected.length >= 4) break;
        if (requiredScore > 0 && section.score < requiredScore) continue;
        const normalized = normalizeCode(section.body);
        if (!normalized || seen.has(normalized)) continue;
        seen.add(normalized);
        selected.push(section);
    }

    const referenceBody = [prefix, reference.body].filter(Boolean).join('\n\n');
    const rendered = selected.map((section, index) => [
        `# Example ${index + 1}: ${index === 0 ? 'simplest reference' : section.heading.replace(/^#\s*/, '')}`,
        index === 0 ? referenceBody : section.body,
    ].join('\n'));

    if (rendered.length < 3) rendered.push(makeNestedVariation(referenceBody));
    if (rendered.length < 3) rendered.push(makeClassVariation(referenceBody, exerciseId));

    return rendered.slice(0, 4).join('\n\n');
};

export const countDistinctSolutionVariations = (solution: string): number => {
    const { sections } = parseSections(solution);
    return new Set(sections.map(section => normalizeCode(section.body)).filter(Boolean)).size;
};
