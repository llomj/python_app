export type ExerciseDifficulty = 'atomic_beginner' | 'beginner' | 'intermediate' | 'expert' | 'legend';

const DIFFICULTY_LABELS: Record<'en' | 'fr', Record<ExerciseDifficulty, string>> = {
  en: {
    atomic_beginner: 'Beginner',
    beginner: 'Easy',
    intermediate: 'Intermediate',
    expert: 'Expert',
    legend: 'Legend',
  },
  fr: {
    atomic_beginner: 'Débutant',
    beginner: 'Facile',
    intermediate: 'Intermédiaire',
    expert: 'Expert',
    legend: 'Légende',
  },
};

const DIFFICULTY_LINE = /^\s*(?:Difficulty|Difficulté)\s*:[^\n]*$/i;
const EXAMPLES_LINE = /^\s*(?:Examples?|Example output|Exemples?|Exemple de sortie)\s*:/im;

export interface ExerciseDescriptionSections {
  task: string;
  difficulty: string;
  examples: string;
}

export const formatExerciseDescription = (
  description: string,
  difficulty: ExerciseDifficulty,
  language: 'en' | 'fr',
): string => {
  const clean = String(description || '').replace(/\r\n?/g, '\n').trim();
  if (!clean) return clean;

  const body = clean
    .split('\n')
    .filter(line => !DIFFICULTY_LINE.test(line))
    .join('\n')
    .trim();

  const label = language === 'fr'
    ? `Difficulté : ${DIFFICULTY_LABELS.fr[difficulty]}.`
    : `Difficulty: ${DIFFICULTY_LABELS.en[difficulty]}.`;
  const examples = body.match(EXAMPLES_LINE);
  if (!examples || examples.index === undefined) return `${body}\n\n${label}`;

  const before = body.slice(0, examples.index).trimEnd();
  const after = body.slice(examples.index).trimStart();
  return `${before}\n\n${label}\n\n${after}`;
};

export const splitExerciseDescription = (description: string): ExerciseDescriptionSections => {
  const lines = String(description || '').replace(/\r\n?/g, '\n').trim().split('\n');
  const difficultyIndex = lines.findIndex(line => DIFFICULTY_LINE.test(line));
  const examplesIndex = lines.findIndex(line => EXAMPLES_LINE.test(line));
  const taskEndCandidates = [difficultyIndex, examplesIndex].filter(index => index >= 0);
  const taskEnd = taskEndCandidates.length ? Math.min(...taskEndCandidates) : lines.length;

  return {
    task: lines.slice(0, taskEnd).join('\n').trim(),
    difficulty: difficultyIndex >= 0 ? lines[difficultyIndex].trim() : '',
    examples: examplesIndex >= 0 ? lines.slice(examplesIndex).join('\n').trim() : '',
  };
};
