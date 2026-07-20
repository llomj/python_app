const fs = require('fs');
const path = require('path');

const app = fs.readFileSync(path.join(__dirname, '..', 'App.tsx'), 'utf8');
const theme = fs.readFileSync(path.join(__dirname, '..', 'editorTheme.ts'), 'utf8');
const failures = [];

const requirePattern = (source, pattern, message) => {
    if (!pattern.test(source)) failures.push(message);
};

requirePattern(
    app,
    /const pythonCompletionSource = useCallback\([\s\S]*?pythonCompletionOptionsRef\.current[\s\S]*?\}, \[\]\);/,
    'Autocomplete must use a stable callback backed by the current completion-options ref.',
);
requirePattern(
    app,
    /autocompletion\(\{ override: \[pythonCompletionSource\] \}\)/,
    'Autocomplete must use one deduplicated completion source.',
);
requirePattern(
    app,
    /setFiles\(currentFiles => currentFiles\.map\(\(file, index\) => \([\s\S]*?\{ \.\.\.file, content: val \}/,
    'Editor changes must update file content immutably.',
);
requirePattern(
    app,
    /event\.repeat[\s\S]*?__backspaceHoldDelay = undefined[\s\S]*?__backspaceHoldTimer = undefined/,
    'Native key-repeat must cancel the synthetic Backspace loop.',
);
requirePattern(
    app,
    /stableEditorInputAttributes[\s\S]*?autocorrect: 'off'[\s\S]*?spellcheck: 'false'/,
    'The code editor must disable mobile autocorrection and spellcheck.',
);
requirePattern(
    app,
    /keyboardRestoreTimerRef\.current = window\.setTimeout\([\s\S]*?180\);/,
    'Keyboard viewport restoration must use one debounced correction.',
);
requirePattern(
    theme,
    /fontVariantLigatures: "none"[\s\S]*?\.cm-cursor, \.cm-dropCursor[\s\S]*?borderLeftWidth: "2px"/,
    'The editor theme must use stable character metrics and an explicit caret.',
);

if (/longPressTimerRef|addEventListener\('touchstart', startLongPress/.test(app)) {
    failures.push('Custom touch long-press handling must not compete with native mobile caret placement.');
}

const editorExtensions = app.match(/const editorExtensions = useMemo\(\(\) => \[([\s\S]*?)\n    \], \[([^\]]*)\]\);/);
if (!editorExtensions || /\bfiles\b/.test(editorExtensions[2])) {
    failures.push('CodeMirror extensions must not be recreated when file text changes.');
}

console.log('Editor stability audit');
console.log('Stable autocomplete extension: checked');
console.log('Immutable editor updates: checked');
console.log('Native mobile caret and key repeat: checked');
console.log('Debounced keyboard viewport handling: checked');
console.log('Explicit stable caret styling: checked');

if (failures.length > 0) {
    failures.forEach(failure => console.error(`- ${failure}`));
    process.exit(1);
}

console.log('Result: passed');
