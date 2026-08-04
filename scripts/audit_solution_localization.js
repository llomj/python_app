#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(root, 'App.tsx'), 'utf8');
const translations = fs.readFileSync(path.join(root, 'services/translations.ts'), 'utf8');
const failures = [];

const modesBlock = app.slice(app.indexOf('const PYTHON_CONCEPT_MODES'), app.indexOf('interface ConceptDocGuide'));
const modeIds = [...modesBlock.matchAll(/id:\s*'(concept:[^']+)'/g)].map(match => match[1]);
const overrides = {
  'concept:for_loops': 'concept.forLoops',
  'concept:while_loops': 'concept.whileLoops',
  'concept:input_output': 'concept.inputOutput',
  'concept:type_conversion': 'concept.typeConversion',
};

for (const modeId of modeIds) {
  const key = overrides[modeId] ?? modeId.replace(':', '.');
  for (const suffix of ['', 'Desc']) {
    const fullKey = `${key}${suffix}`;
    const escaped = fullKey.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const occurrences = translations.match(new RegExp(`'${escaped}'`, 'g'))?.length ?? 0;
    if (occurrences !== 2) failures.push(`${modeId}: expected English and French records for ${fullKey}, found ${occurrences}`);
  }
}

const requiredSource = [
  "SYNTAXE: 'SYNTAX'",
  "'VUE D’ENSEMBLE': 'OVERVIEW'",
  "'EXPLICATION SIMPLE': 'SIMPLE EXPLANATION'",
  "'EXPLICATION INTERMÉDIAIRE': 'INTERMEDIATE EXPLANATION'",
  "'EXPLICATION APPROFONDIE': 'IN-DEPTH EXPLANATION'",
  "EXEMPLES: 'EXAMPLES'",
  "'OPÉRATIONS COURANTES': 'COMMON OPERATIONS'",
  "formatDocSectionTitle(section.title, lang)",
  "getConceptDoc(difficultyMode, appLang)",
  'lang={appLang}',
  "label={getModeLabel(selectedConceptMode.id, appLang)}",
  "Une boucle while vérifie sa condition avant chaque itération.",
  "Une boucle while répète un bloc tant que sa condition reste vraie.",
];

for (const marker of requiredSource) {
  if (!app.includes(marker)) failures.push(`missing localization marker: ${marker}`);
}

if (app.includes('const CONCEPT_DOCS:')) failures.push('concept documents are still prebuilt in one language');
if ((app.match(/<SyntaxDocumentationPanel[^>]+lang=\{appLang\}/g) ?? []).length !== 2) failures.push('syntax and concept panels must both receive the active language');

console.log('Solution localization audit');
console.log(`Concept modes checked: ${modeIds.length}`);
console.log('English/French section headings: checked');
console.log('Language-reactive syntax and concept documents: checked');
console.log('French while-loop reference: checked');
if (failures.length) {
  failures.forEach(failure => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log('Result: passed');
}
