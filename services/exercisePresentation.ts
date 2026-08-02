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
const EXAMPLES_LINE = /^\s*(?:Examples?|Exemples?)\s*:/im;

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
