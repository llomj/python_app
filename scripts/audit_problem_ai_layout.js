#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(root, 'App.tsx'), 'utf8');
const css = fs.readFileSync(path.join(root, 'styles', 'tailwind.css'), 'utf8');
const failures = [];

for (const marker of [
  'data-problem-ai-panel',
  'data-problem-ai-scroll',
  'data-problem-ai-message',
  'data-problem-ai-content',
  'data-problem-ai-code',
]) {
  if (!app.includes(marker)) failures.push(`App.tsx is missing ${marker}`);
  if (!css.includes(`[${marker}]`)) failures.push(`Problem AI containment CSS is missing [${marker}]`);
}

for (const rule of [
  'overflow-x: hidden',
  'overscroll-behavior-x: none',
  'touch-action: pan-y',
  'overflow-wrap: anywhere',
  'word-break: break-word',
]) {
  if (!css.includes(rule)) failures.push(`Problem AI containment CSS is missing ${rule}`);
}

if (!/data-problem-ai-scroll[^>]*overflow-y-auto[^>]*overflow-x-hidden/.test(app)) {
  failures.push('Problem AI conversation must scroll vertically and hide horizontal overflow');
}
if (!/grid-cols-\[28px_minmax\(0,1fr\)\]/.test(app)) {
  failures.push('Problem AI response grid must use a shrinkable minmax(0, 1fr) content column');
}
if (!/data-problem-ai-code[\s\S]{0,1000}EditorView\.lineWrapping/.test(app)) {
  failures.push('Problem AI code blocks must retain CodeMirror line wrapping');
}

console.log('Problem AI layout audit');
console.log('Horizontal containment layers: 5');
console.log('Vertical-only touch scrolling: checked');
console.log('Long text and code wrapping: checked');

if (failures.length) {
  for (const failure of failures) console.error(`- ${failure}`);
  process.exitCode = 1;
} else {
  console.log('Result: passed');
}
