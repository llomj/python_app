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

const gradeDecisionStart = app.indexOf('if (gradeResult.passed) {');
const deterministicFailureStart = app.indexOf("} else {\n                    updateCurrentModeStats('failed');", gradeDecisionStart);
const deterministicFailureEnd = app.indexOf("\n            } else {\n                setOutputStatus('info');", deterministicFailureStart);
const deterministicFailureBranch = deterministicFailureStart >= 0 && deterministicFailureEnd > deterministicFailureStart
    ? app.slice(deterministicFailureStart, deterministicFailureEnd)
    : '';

if (!deterministicFailureBranch) failures.push('The deterministic grader failure branch must remain auditable.');
if (/updateCurrentModeStats\('success'\)|setOutputStatus\('win'\)|playResultFeedback\('win'\)/.test(deterministicFailureBranch)) {
    failures.push('AI review must not convert a deterministic grader failure into a win.');
}
if (!/updateCurrentModeStats\('failed'\)[\s\S]*setOutputStatus\('fail'\)/.test(deterministicFailureBranch)) {
    failures.push('A deterministic grader failure must record a failed attempt and show red failure output.');
}

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
console.log('Deterministic failure remains failed after AI review: checked');

if (failures.length) {
    failures.forEach(failure => console.error(`- ${failure}`));
    process.exit(1);
}

console.log('Result: passed');
