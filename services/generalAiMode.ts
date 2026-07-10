import { AiLanguage } from './aiLocalization';

export type GeneralAiResponseMode = 'simple' | 'normal' | 'deep' | 'examples';

type ComposeGeneralAiAnswerOptions = {
    answer: string;
    topic: string;
    mode: GeneralAiResponseMode;
    language: AiLanguage;
    examples?: string;
    relatedConcepts?: string[];
    followUps?: string;
};

export const getGeneralAiModeInstruction = (mode: GeneralAiResponseMode, language: AiLanguage): string => {
    if (language === 'fr') {
        switch (mode) {
            case 'simple': return 'Réponse SIMPLE : 2 à 4 phrases courtes, une définition claire et un seul petit exemple.';
            case 'normal': return 'Réponse NORMALE : définition, fonctionnement en étapes, exemple et erreur fréquente.';
            case 'deep': return 'Réponse APPROFONDIE : mécanisme interne, ordre d’exécution, cas limites, compromis, erreurs fréquentes et plusieurs exemples.';
            case 'examples': return 'Réponse EXEMPLES : privilégie plusieurs exemples Python progressifs, chacun brièvement expliqué.';
        }
    }
    switch (mode) {
        case 'simple': return 'SIMPLE response: 2-4 short sentences, one clear definition, and one tiny example.';
        case 'normal': return 'NORMAL response: definition, step-by-step workflow, example, and common mistake.';
        case 'deep': return 'DEEP response: internal mechanics, execution order, edge cases, tradeoffs, common mistakes, and multiple examples.';
        case 'examples': return 'EXAMPLES response: prioritize several progressive Python examples, each with a short explanation.';
    }
};

export const composeGeneralAiAnswer = ({
    answer,
    topic,
    mode,
    language,
    examples = '',
    relatedConcepts = [],
    followUps = '',
}: ComposeGeneralAiAnswerOptions): string => {
    if (mode === 'simple') {
        return [answer, language === 'fr'
            ? `**À retenir**\nConcentrez-vous d’abord sur le rôle de ${topic}, puis sur sa syntaxe.`
            : `**Key point**\nFocus first on what ${topic} does, then on its syntax.`]
            .filter(Boolean)
            .join('\n\n');
    }

    if (mode === 'examples') {
        return [
            answer,
            language === 'fr' ? '**Exemples progressifs**' : '**Progressive examples**',
            examples,
            language === 'fr'
                ? '**Comment les lire**\n1. Repérez la valeur de départ.\n2. Suivez l’opération.\n3. Vérifiez la valeur affichée ou renvoyée.'
                : '**How to read them**\n1. Find the starting value.\n2. Follow the operation.\n3. Check the printed or returned value.',
            followUps,
        ].filter(Boolean).join('\n\n');
    }

    const workflow = language === 'fr'
        ? `**Déroulement**\n1. Identifiez les données de départ.\n2. Appliquez la syntaxe de ${topic}.\n3. Vérifiez si l’opération modifie l’objet ou crée une nouvelle valeur.\n4. Utilisez \`return\` ou \`print()\` selon le but.`
        : `**Workflow**\n1. Identify the starting data.\n2. Apply the ${topic} syntax.\n3. Check whether the operation mutates the object or creates a new value.\n4. Use \`return\` or \`print()\` for the intended result.`;
    const mistakes = language === 'fr'
        ? '**Erreurs fréquentes**\n- Copier un exemple sans comprendre sa logique.\n- Confondre une valeur affichée avec une valeur renvoyée.\n- Utiliser une méthode sur le mauvais type de données.'
        : '**Common mistakes**\n- Copying an example without understanding its logic.\n- Confusing a printed value with a returned value.\n- Calling a method on the wrong data type.';

    if (mode === 'normal') {
        return [answer, workflow, mistakes, followUps].filter(Boolean).join('\n\n');
    }

    const related = relatedConcepts.length
        ? `${language === 'fr' ? '**Concepts liés**' : '**Related concepts**'}\n${relatedConcepts.map((item, index) => `${index + 1}. ${item}`).join('\n')}`
        : '';
    const deep = language === 'fr'
        ? '**Analyse approfondie**\n- Identifiez le type exact de chaque objet.\n- Suivez l’ordre d’évaluation des expressions et des appels.\n- Vérifiez la mutabilité, la portée des variables et la valeur de retour.\n- Testez les entrées vides, les valeurs limites et les types incorrects.\n- Comparez lisibilité, coût mémoire et temps d’exécution lorsque plusieurs approches existent.'
        : '**In-depth analysis**\n- Identify the exact type of every object.\n- Follow expression and call evaluation order.\n- Check mutability, variable scope, and return value.\n- Test empty input, boundary values, and incorrect types.\n- Compare readability, memory cost, and runtime when several approaches exist.';
    return [answer, workflow, deep, related, mistakes, examples, followUps].filter(Boolean).join('\n\n');
};
