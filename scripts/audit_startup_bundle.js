const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const htmlPath = path.join(dist, 'index.html');
const failures = [];

if (!fs.existsSync(htmlPath)) {
  failures.push('dist/index.html is missing');
} else {
  const html = fs.readFileSync(htmlPath, 'utf8');
  const entryMatch = html.match(/<script[^>]+type="module"[^>]+src="([^"]+)"/i);
  if (!entryMatch) {
    failures.push('could not find the production module entry');
  } else {
    const relativeEntry = entryMatch[1].replace(/^\.\//, '').replace(/^\//, '');
    const entryPath = path.join(dist, relativeEntry);
    if (!fs.existsSync(entryPath)) {
      failures.push(`production module entry is missing: ${relativeEntry}`);
    } else {
      const entrySize = fs.statSync(entryPath).size;
      const entrySource = fs.readFileSync(entryPath, 'utf8');
      console.log(`Initial module: ${relativeEntry} (${entrySize} bytes)`);
      if (entrySize > 500_000) failures.push(`initial module is too large (${entrySize} bytes)`);
      if (!/import\(["']\.\/[^)]+\)/.test(entrySource)) failures.push('application code is not loaded as a separate startup chunk');
    }
  }
}

console.log('Startup bundle audit');
console.log(`Failures: ${failures.length}`);
if (failures.length) {
  failures.forEach(failure => console.error(failure));
  process.exit(1);
}
