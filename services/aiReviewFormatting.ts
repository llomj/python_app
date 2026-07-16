export const splitAiReviewSteps = (text: string) => {
    const codeFences: string[] = [];
    const protectedText = text.replace(/```(?:python|py)?\s*[\s\S]*?```/gi, fence => {
        const token = `@@AI_CODE_FENCE_${codeFences.length}@@`;
        codeFences.push(fence);
        return token;
    });
    const restoreCodeFences = (value: string) => value.replace(/@@AI_CODE_FENCE_(\d+)@@/g, (_match, index) => codeFences[Number(index)] || '');
    const normalized = protectedText
        .replace(/\n\s*---\s*\n/g, '\n\n')
        .replace(/\s+(?=(?:Problem requirement|Line-by-line code inspection|Code inspection|Output analysis|Code explanation|Syntax explanation|Concept explanation|Expected solution workflow|Function workflow|Execution order|Order of operation|The code still contains|The grader\/run system|The local model response|Specific built-in analysis|Built-in analysis|Suggested fix):)/g, '\n\n')
        .replace(/\s+(?=The deterministic grader|A function that reaches|If this is|For this grader)/g, '\n\n')
        .trim();

    const explicitSections = normalized
        .split(/\n\s*\n+/)
        .map(section => section.trim())
        .filter(Boolean);

    if (explicitSections.length > 1) {
        return explicitSections
            .map(section => restoreCodeFences(section.replace(/^\d+[.)]\s*/, '').trim()))
            .filter(section => !/^(Specific built-in analysis|Built-in analysis):?$/i.test(section));
    }

    const sentenceSections = normalized
        .split(/(?<=[.!?])\s+(?=[A-Z])/)
        .map(section => section.trim())
        .filter(Boolean);

    return (sentenceSections.length > 1 ? sentenceSections : [normalized]).map(restoreCodeFences);
};
