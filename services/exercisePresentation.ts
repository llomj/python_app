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

const DIFFICULTY_LINE = /^\s*(?:Difficulty|Difficulté)\s*:/im;
const EXAMPLES_LINE = /^\s*(?:Examples?|Exemples?)\s*:/im;

export const formatExerciseDescription = (
  description: string,
  difficulty: ExerciseDifficulty,
  language: 'en' | 'fr',
): string => {
  const clean = String(description || '').replace(/\r\n?/g, '\n').trim();
  if (!clean || DIFFICULTY_LINE.test(clean)) return clean;

  const label = language === 'fr'
    ? `Difficulté : ${DIFFICULTY_LABELS.fr[difficulty]}.`
    : `Difficulty: ${DIFFICULTY_LABELS.en[difficulty]}.`;
  const examples = clean.match(EXAMPLES_LINE);
  if (!examples || examples.index === undefined) return `${clean}\n${label}`;

  const before = clean.slice(0, examples.index).trimEnd();
  const after = clean.slice(examples.index).trimStart();
  return `${before}\n${label}\n${after}`;
};
