const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const manifestPath = path.join(dist, 'offline-assets.json');

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap(entry => {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) return walk(absolute);
    if (absolute === manifestPath || entry.name.endsWith('.map')) return [];
    return [`./${path.relative(dist, absolute).split(path.sep).join('/')}`];
  });
}

const assets = ['./', ...walk(dist)].filter((asset, index, all) => all.indexOf(asset) === index).sort();
fs.writeFileSync(manifestPath, `${JSON.stringify({ version: 'v275', assets }, null, 2)}\n`);
console.log(`Generated offline manifest with ${assets.length} local assets.`);
