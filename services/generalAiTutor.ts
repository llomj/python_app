import type { GeneralAiResponseMode } from './generalAiMode';
import {
  answerPythonBareOrFuzzyQuestion,
  answerPythonAtLevel,
  extractKnowledgeTerm,
  resolveFuzzyPythonTerm,
  resolvePythonKnowledge,
  searchPythonKnowledge,
  type KnowledgeLanguage,
  type PythonExplanationLevel,
} from './pythonKnowledge';

export type GeneralAiTutorMode = 'explain' | 'socratic' | 'debug' | 'compare' | 'quiz' | 'practice';

export interface TutorMasteryEntry {
  views: number;
  beginner: number;
  intermediate: number;
  expert: number;
  lastSeen: number;
}

export type TutorMasteryProfile = Record<string, TutorMasteryEntry>;

export interface TutorCodeCommand {
  handled: boolean;
  effectiveQuestion?: string;
  directAnswer?: string;
}

const TUTOR_SUBJECT_STOP_WORDS = new Set([
  'a', 'about', 'again', 'and', 'are', 'can', 'compare', 'define', 'describe', 'do',
  'does', 'explain', 'for', 'how', 'in', 'is', 'it', 'me', 'more', 'of', 'please',
  'show', 'tell', 'the', 'this', 'to', 'what', 'why', 'with',
  'de', 'des', 'encore', 'est', 'et', 'explique', 'la', 'le', 'les', 'moi', 'plus', 'quoi', 'un', 'une',
]);

export const parseTutorMasteryProfile = (raw: string | null): TutorMasteryProfile => {
  if (!raw) return {};
  try {
    const parsed = JSON.parse(raw);
    return parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed : {};
  } catch {
    return {};
  }
};

export const getTutorSubject = (question: string): string => {
  const direct = extractKnowledgeTerm(question);
  if (direct) {
    const fuzzy = resolveFuzzyPythonTerm(direct);
    if (fuzzy) return fuzzy.term;
    if (resolvePythonKnowledge(direct).record) return direct.toLowerCase();
  }
  const semantic = searchPythonKnowledge(question, 1)[0];
  if (semantic && semantic.score >= 12) return semantic.record.canonicalName.toLowerCase();
  const words = question.toLowerCase().match(/[a-z_][a-z0-9_.-]*/g) || [];
  for (const word of words) {
    if (TUTOR_SUBJECT_STOP_WORDS.has(word)) continue;
    const fuzzy = resolveFuzzyPythonTerm(word);
    if (fuzzy) return fuzzy.term;
  }
  return 'python';
};

export const inferTutorLevel = (
  question: string,
  profile: TutorMasteryProfile,
  selectedMode: GeneralAiResponseMode,
  adaptive: boolean,
): GeneralAiResponseMode => {
  if (!adaptive || selectedMode === 'examples') return selectedMode;
  if (/\b(?:simple|beginner|basic|plain language|d[eé]butant|facile|simplement)\b/i.test(question)) return 'simple';
  if (/\b(?:expert|internals?|implementation|complexity|big[- ]?o|bytecode|cpython|memory|protocol|expert|interne|complexit[eé]|m[eé]moire)\b/i.test(question)) return 'deep';
  if (/\b(?:intermediate|practical|workflow|common mistakes|interm[eé]diaire|pratique)\b/i.test(question)) return 'normal';
  const subject = getTutorSubject(question);
  const views = profile[subject]?.views || 0;
  if (views === 0) return 'simple';
  if (views < 4) return 'normal';
  return 'deep';
};

const responseLevel = (mode: GeneralAiResponseMode): PythonExplanationLevel => (
  mode === 'simple' ? 'beginner' : mode === 'deep' ? 'expert' : 'intermediate'
);

export const updateTutorMastery = (
  profile: TutorMasteryProfile,
  subject: string,
  mode: GeneralAiResponseMode,
): TutorMasteryProfile => {
  const level = responseLevel(mode);
  const current = profile[subject] || { views: 0, beginner: 0, intermediate: 0, expert: 0, lastSeen: 0 };
  return {
    ...profile,
    [subject]: {
      ...current,
      views: current.views + 1,
      [level]: current[level] + 1,
      lastSeen: Date.now(),
    },
  };
};

const fencedCode = (text: string): string => text.match(/```(?:python)?\s*\n?([\s\S]*?)```/i)?.[1]?.trim() || '';

export const resolveTutorCodeCommand = (
  question: string,
  previousAssistantAnswer: string,
  language: KnowledgeLanguage,
): TutorCodeCommand => {
  const code = fencedCode(previousAssistantAnswer);
  if (!code) return { handled: false };
  if (/^(?:run|execute|test) (?:this|that|it)|^(?:ex[eé]cute|lance|teste) (?:ceci|cela|ce code)$/i.test(question.trim())) {
    return { handled: true, effectiveQuestion: `Explain this code:\n\`\`\`python\n${code}\n\`\`\`` };
  }
  const lineMatch = question.match(/(?:explain|analyse|analyze|explique)\s+(?:line|ligne)\s+(\d+)/i);
  if (lineMatch) {
    const lineNumber = Number(lineMatch[1]);
    const lines = code.split('\n');
    const line = lines[lineNumber - 1];
    if (!line) {
      return {
        handled: true,
        directAnswer: language === 'fr'
          ? `Le bloc précédent contient ${lines.length} lignes ; la ligne ${lineNumber} n’existe pas.`
          : `The previous code block has ${lines.length} lines; line ${lineNumber} does not exist.`,
      };
    }
    return {
      handled: true,
      directAnswer: [
        `**${language === 'fr' ? `Ligne ${lineNumber}` : `Line ${lineNumber}`}**`,
        `\`\`\`python\n${line}\n\`\`\``,
        language === 'fr'
          ? 'Cette ligne doit être lue dans le contexte des valeurs créées par les lignes précédentes. Demandez « approfondis » pour analyser son type, son retour et ses effets.'
          : 'Read this line using the values created by earlier lines. Ask “go deeper” to analyze its types, return value, and side effects.',
      ].join('\n\n'),
    };
  }
  const changeMatch = question.match(/(?:change|replace|set|utilise|remplace|change)\s+(?:the\s+)?(?:input|value|entr[eé]e|valeur)(?:\s+to|\s+par|\s+avec)?\s+(.+)$/i);
  if (changeMatch) {
    const replacement = changeMatch[1].trim();
    const lines = code.split('\n');
    const assignmentIndex = lines.findIndex(line => /^\s*[A-Za-z_]\w*\s*=/.test(line));
    if (assignmentIndex < 0) return { handled: false };
    lines[assignmentIndex] = lines[assignmentIndex].replace(/^(\s*[A-Za-z_]\w*\s*=\s*).+$/, `$1${replacement}`);
    const changedCode = lines.join('\n');
    return { handled: true, effectiveQuestion: `Explain this code:\n\`\`\`python\n${changedCode}\n\`\`\`` };
  }
  return { handled: false };
};

export const answerTutorMode = (
  question: string,
  mode: GeneralAiTutorMode,
  responseMode: GeneralAiResponseMode,
  language: KnowledgeLanguage,
): string | null => {
  const specializedQuestion = /\b(?:difference between|compare|versus|vs\.?|documentation|official docs?|how many|number of|when was|what version|how can i|what should i use|Traceback|Error:)\b/i.test(question)
    || /```|(^|\n)\s*(?:def |class |print\(|[A-Za-z_]\w*\s*=)/m.test(question);
  const subject = getTutorSubject(question);
  const resolution = resolvePythonKnowledge(subject);
  const record = resolution.record;
  const fr = language === 'fr';
  if (mode === 'debug') {
    if (/```|Traceback|(^|\n)\s*(?:def |class |print\(|[A-Za-z_]\w*\s*=)/m.test(question)) return null;
    return fr
      ? '**Mode débogage**\n\nCollez le code, la sortie réelle et le traceback complet. Je suivrai les lignes, les types et l’ordre d’exécution sans deviner.'
      : '**Debug mode**\n\nPaste the code, actual output, and complete traceback. I will trace the lines, types, and execution order without guessing.';
  }
  if (mode === 'compare') {
    if (/\bdifference between\s+.+\s+and\s+.+|\bcompare\s+.+\s+(?:with|to|and)\s+.+|.+\s+(?:vs\.?|versus)\s+.+|\bdiff[eé]rence entre\s+.+\s+et\s+.+/i.test(question)) return null;
    return fr
      ? '**Mode comparaison**\n\nIndiquez deux concepts, par exemple `list vs tuple` ou `sort vs sorted`.'
      : '**Compare mode**\n\nName two concepts, for example `list vs tuple` or `sort vs sorted`.';
  }
  if (!record) return null;
  if (mode === 'socratic') {
    return [
      `**${fr ? 'Mode socratique' : 'Socratic mode'}: ${record.canonicalName}**`,
      fr ? 'Je ne donne pas immédiatement la réponse. Utilisez ces indices :' : 'I will not reveal the answer immediately. Use these hints:',
      `1. ${fr ? 'Identifiez son type' : 'Identify its kind'}: \`${record.kind}\`.`,
      `2. ${fr ? 'Observez sa syntaxe' : 'Inspect its syntax'}: \`${record.signature}\`.`,
      `3. ${fr ? 'Demandez-vous si l’objet original change' : 'Ask whether the original object changes'}.`,
      fr ? 'Votre réponse : que pensez-vous que ce code renvoie ou modifie ?' : 'Your turn: what do you think this code returns or changes?',
    ].join('\n\n');
  }
  if (mode === 'quiz') {
    const example = record.examples[0]?.code || record.signature;
    return [
      `**${fr ? 'Quiz adaptatif' : 'Adaptive quiz'}: ${record.canonicalName}**`,
      fr ? 'Sans exécuter le code, prédisez la sortie, le type renvoyé et si une valeur existante est modifiée.' : 'Without running the code, predict the output, return type, and whether an existing value is mutated.',
      `\`\`\`python\n${example}\n\`\`\``,
      fr ? 'Répondez avec votre raisonnement ; je vérifierai chaque étape.' : 'Reply with your reasoning and I will check each step.',
    ].join('\n\n');
  }
  if (mode === 'practice') {
    return [
      `**${fr ? 'Exercice ciblé' : 'Targeted practice'}: ${record.canonicalName}**`,
      fr ? `Créez un petit programme qui utilise \`${record.signature}\` avec vos propres valeurs.` : `Create a small program using \`${record.signature}\` with your own values.`,
      fr ? 'Contraintes : affichez le résultat, testez un cas normal et un cas limite, puis demandez-moi de vérifier votre code.' : 'Requirements: print the result, test one normal case and one edge case, then ask me to check your code.',
      fr ? 'Je donnerai d’abord un indice, puis une solution seulement si vous la demandez.' : 'I will give a hint first and only show a solution if you request it.',
    ].join('\n\n');
  }
  if (mode === 'explain' && responseMode !== 'examples' && !specializedQuestion) {
    const fuzzyBare = answerPythonBareOrFuzzyQuestion(question, language);
    if (fuzzyBare && resolveFuzzyPythonTerm(question)?.distance) return fuzzyBare;
    return answerPythonAtLevel(question, language, responseLevel(responseMode));
  }
  return null;
};
