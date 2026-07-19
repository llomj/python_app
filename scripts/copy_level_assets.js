const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const assetPatterns = [
  /^level1_.*_codelogic\.py$/,
  /^level1_.*_requirements.*\.py$/,
  /^level1_.*_syntax\.py$/,
  /^level1_.*_fr\.py$/,
];

if (!fs.existsSync(dist)) {
  throw new Error('dist is missing; run the Vite build before copying level assets');
}

const assets = fs.readdirSync(root).filter(file => assetPatterns.some(pattern => pattern.test(file)));
for (const asset of assets) {
  fs.copyFileSync(path.join(root, asset), path.join(dist, asset));
}

console.log(`Copied ${assets.length} optional level assets.`);
