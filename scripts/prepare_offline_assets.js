const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const source = path.join(root, 'node_modules', 'pyodide');
const destination = path.join(root, 'public', 'pyodide');
const files = [
  'pyodide-lock.json',
  'pyodide.asm.js',
  'pyodide.asm.wasm',
  'pyodide.js',
  'python_stdlib.zip',
];

if (!fs.existsSync(source)) {
  throw new Error('Pyodide dependency is missing. Run npm install before building.');
}

fs.rmSync(destination, { recursive: true, force: true });
fs.mkdirSync(destination, { recursive: true });
for (const file of files) {
  fs.copyFileSync(path.join(source, file), path.join(destination, file));
}

console.log(`Prepared ${files.length} local Pyodide runtime assets.`);
