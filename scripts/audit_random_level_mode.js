#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(root, 'App.tsx'), 'utf8');
const translations = fs.readFileSync(path.join(root, 'services/translations.ts'), 'utf8');
const failures = [];

const difficultyModesMatch = app.match(/const DIFFICULTY_MODES:[\s\S]*?= \[([\s\S]*?)\n\];/);
const difficultyModeOrder = [...(difficultyModesMatch?.[1] || '').matchAll(/id: '([^']+)'/g)].map(match => match[1]);
const expectedDifficultyModeOrder = ['atomic_beginner', 'beginner', 'normal', 'intermediate', 'expert', 'legend'];
if (JSON.stringify(difficultyModeOrder) !== JSON.stringify(expectedDifficultyModeOrder)) {
  failures.push(`problem mode order must be ${expectedDifficultyModeOrder.join(', ')}`);
}

const requiredAppMarkers = [
  "const [randomLevelPickerOpen, setRandomLevelPickerOpen]",
  "const [randomLevelPracticeEnabled, setRandomLevelPracticeEnabled]",
  "const handleRandomLevelSelect = (mode: Extract<DifficultyMode, 'beginner' | 'intermediate' | 'expert'>)",
  "getRandomExerciseForMode(mode, exercise.id)",
  "localStorage.setItem('python_random_level_practice', 'true')",
  "localStorage.setItem('python_difficulty_mode', mode)",
  "(['beginner', 'intermediate', 'expert'] as const).map",
  "onClick={handleStandardExerciseMode}",
  "onClick={handleCodeScaffoldToggle}",
  "onClick={handlePlainIdeMode}",
  "t('settings.randomLevelHelp', appLang)",
];

for (const marker of requiredAppMarkers) {
  if (!app.includes(marker)) failures.push(`missing implementation marker: ${marker}`);
}

for (const key of ['settings.randomLevel', 'settings.randomLevelDesc', 'settings.randomLevelHelp', 'settings.chooseRandomLevel']) {
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const occurrences = translations.match(new RegExp(`'${escaped}'`, 'g'))?.length ?? 0;
  if (occurrences !== 2) failures.push(`${key}: expected English and French translations, found ${occurrences}`);
}

const modePanelStart = app.indexOf('{modeSectionOpen && (');
const modePanelEnd = app.indexOf("{soundsSectionOpen && (", modePanelStart);
const modePanel = app.slice(modePanelStart, modePanelEnd);
const orderedMarkers = [
  'onClick={handleStandardExerciseMode}',
  "t('settings.randomLevel', appLang)",
  'onClick={handleCodeScaffoldToggle}',
  'onClick={handlePlainIdeMode}',
];
let previousIndex = -1;
for (const marker of orderedMarkers) {
  const index = modePanel.indexOf(marker);
  if (index < 0 || index <= previousIndex) failures.push(`mode card order is incorrect at ${marker}`);
  previousIndex = index;
}

console.log('Random-by-level mode audit');
console.log('Four-card order: Play, Random by Level, Code Scaffold, Plain IDE');
console.log('Problem mode order: Beginner, Easy, Normal, Intermediate, Expert, Legend');
console.log('Difficulty pools: Easy, Intermediate, Expert');
console.log('English/French explanation: checked');
console.log('Persistent Next randomization: checked');
if (failures.length) {
  failures.forEach(failure => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log('Result: passed');
}
