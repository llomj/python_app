#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const app = fs.readFileSync(path.join(__dirname, '..', 'App.tsx'), 'utf8');
const entry = fs.readFileSync(path.join(__dirname, '..', 'index.tsx'), 'utf8');
const failures = [];

const requirePattern = (source, pattern, message) => {
    if (!pattern.test(source)) failures.push(message);
};

requirePattern(app, /const EXERCISE_POOL_CACHE = new Map<(?:ProblemMode|string), Exercise\[\]>/, 'Exercise pools must be cached.');
requirePattern(app, /statsPanelsVisible \? DIFFICULTY_MODES\.map/, 'Stats calculations must be deferred until their panel is visible.');
requirePattern(app, /const setProblemById = \(id: number\) => \{[\s\S]*?runGenerationRef\.current \+= 1;/, 'Changing problems must invalidate stale runs.');
requirePattern(app, /if \(!isCurrentRun\(\)\) return;/, 'Async run results must be discarded after Next changes the problem.');
requirePattern(app, /pythonRuntimeGenerationRef\.current === runGeneration/, 'A stale AI review must not unlock or overwrite a newer Python run.');
requirePattern(app, /__PY_EXECUTION_TIMEOUT__/, 'User Python execution must have a runaway-loop guard.');
requirePattern(app, /USER_CODE_TIMEOUT_CHECK_INTERVAL = 20/, 'The runaway-loop guard must check frequently enough for mobile Pyodide.');
requirePattern(app, /requestAnimationFrame\(\(\) => resolve\(\)\)/, 'The editor must paint as unlocked before optional AI fallback work.');
requirePattern(entry, /window\.__START_LOCAL_PYTHON__ = startLocalPython/, 'Python startup must begin from the mounted app instead of competing with the initial bundle.');
requirePattern(entry, /requestIdleCallback\(preload/, 'Optional curriculum preloading must wait for browser idle time.');

if (/Auto-download offline AI model on first launch/.test(app)) {
    failures.push('The optional offline AI model must not download automatically during startup.');
}

console.log('Runtime responsiveness audit');
console.log('Sequential startup: checked');
console.log('Optional AI remains opt-in: checked');
console.log('Exercise-pool caching: checked');
console.log('Deferred stats work: checked');
console.log('Stale run cancellation: checked');
console.log('Runaway Python guard: checked');

if (failures.length) {
    failures.forEach(failure => console.error(`- ${failure}`));
    process.exit(1);
}

console.log('Result: passed');
