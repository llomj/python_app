const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const manifestPath = path.join(dist, 'offline-assets.json');
const failures = [];

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) return walk(absolute);
    return [`./${path.relative(dist, absolute).split(path.sep).join('/')}`];
  });
}

const requiredAssets = [
  './index.html',
  './manifest.json',
  './python-icon.svg',
  './sw.js',
  './tailwind.generated.css',
  './pyodide/pyodide.js',
  './pyodide/pyodide.asm.js',
  './pyodide/pyodide.asm.wasm',
  './pyodide/pyodide-lock.json',
  './pyodide/python_stdlib.zip',
];

if (!fs.existsSync(manifestPath)) {
  failures.push('offline-assets.json is missing');
} else {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const serviceWorker = fs.readFileSync(path.join(dist, 'sw.js'), 'utf8');
  const workerVersion = serviceWorker.match(/CACHE_VERSION\s*=\s*['"]([^'"]+)/)?.[1];
  if (!workerVersion || workerVersion !== manifest.version) {
    failures.push(`service worker version ${workerVersion || 'missing'} does not match manifest ${manifest.version}`);
  }
  const listed = new Set(manifest.assets || []);
  for (const asset of requiredAssets) {
    const absolute = path.join(dist, asset.replace(/^\.\//, ''));
    if (!fs.existsSync(absolute)) failures.push(`${asset} is missing from dist`);
    if (!listed.has(asset)) failures.push(`${asset} is missing from the offline manifest`);
  }
  for (const asset of listed) {
    if (asset === './') continue;
    const absolute = path.join(dist, asset.replace(/^\.\//, ''));
    if (!fs.existsSync(absolute)) failures.push(`manifest references missing asset ${asset}`);
  }
}

const emittedText = walk(dist)
  .filter(asset => /\.(?:css|html|js|json)$/.test(asset) && !asset.startsWith('./pyodide/'))
  .map(asset => fs.readFileSync(path.join(dist, asset.replace(/^\.\//, '')), 'utf8'))
  .join('\n');
const forbiddenRuntimeUrls = [
  /https?:\/\/cdn\.tailwindcss\.com/i,
  /https?:\/\/cdn\.jsdelivr\.net\/pyodide/i,
  /https?:\/\/cdn\.jsdelivr\.net\/gh\/devicons/i,
  /https?:\/\/esm\.sh\//i,
];
if (forbiddenRuntimeUrls.some(pattern => pattern.test(emittedText))) {
  failures.push('the emitted application still references a mandatory runtime CDN');
}

const minimumSizes = {
  './pyodide/pyodide.asm.wasm': 5_000_000,
  './pyodide/python_stdlib.zip': 1_000_000,
  './tailwind.generated.css': 10_000,
};
for (const [asset, minimum] of Object.entries(minimumSizes)) {
  const size = fs.statSync(path.join(dist, asset.replace(/^\.\//, ''))).size;
  if (size < minimum) failures.push(`${asset} is unexpectedly small (${size} bytes)`);
}

console.log('Offline production audit');
console.log(`Required local assets: ${requiredAssets.length}`);
console.log(`Failures: ${failures.length}`);
if (failures.length) {
  failures.forEach(failure => console.error(failure));
  process.exit(1);
}
