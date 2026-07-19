import type { AutoGrader } from './graders';
import type { Exercise } from './types';

export interface GeneratedFrenchExercise {
  description: string;
  hint: string;
  breakdown: string;
}

export interface CurriculumCatalog {
  exercises: Exercise[];
  graders: Record<number, AutoGrader>;
  exercisesFr: Record<number, string>;
  atomicBeginnerExercisesFr: Record<number, string>;
  whileLoopPracticeFr: Record<number, GeneratedFrenchExercise>;
  conceptExpansionFr: Record<number, GeneratedFrenchExercise>;
  advancedConceptFr: Record<number, GeneratedFrenchExercise>;
  foundationIntermediateFr: Record<number, GeneratedFrenchExercise>;
}

let curriculumPromise: Promise<CurriculumCatalog> | null = null;

export const preloadCurriculum = (): Promise<CurriculumCatalog> => {
  if (curriculumPromise) return curriculumPromise;

  curriculumPromise = Promise.all([
    import('./exercises'),
    import('./graders'),
    import('./services/exercisesFr'),
    import('./atomicBeginnerExercisesFr'),
    import('./services/whileLoopPracticeFr'),
    import('./services/conceptExpansionFr'),
    import('./services/advancedConceptFr'),
    import('./services/foundationIntermediateFr'),
  ]).then(([
    exercises,
    graders,
    exercisesFr,
    atomicBeginnerExercisesFr,
    whileLoopPracticeFr,
    conceptExpansionFr,
    advancedConceptFr,
    foundationIntermediateFr,
  ]) => ({
    exercises: exercises.EXERCISES,
    graders: graders.AUTO_GRADERS,
    exercisesFr: exercisesFr.EXERCISES_FR,
    atomicBeginnerExercisesFr: atomicBeginnerExercisesFr.ATOMIC_BEGINNER_EXERCISES_FR,
    whileLoopPracticeFr: whileLoopPracticeFr.WHILE_LOOP_PRACTICE_FR,
    conceptExpansionFr: conceptExpansionFr.CONCEPT_EXPANSION_FR,
    advancedConceptFr: advancedConceptFr.ADVANCED_CONCEPT_FR,
    foundationIntermediateFr: foundationIntermediateFr.FOUNDATION_INTERMEDIATE_FR,
  }));

  return curriculumPromise;
};
