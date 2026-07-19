const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');
const htmlPath = path.join(dist, 'index.html');
const failures = [];

const readAsset = relativeAsset => {
  const assetPath = path.join(dist, relativeAsset);
  if (!fs.existsSync(assetPath)) {
    failures.push(`production asset is missing: ${relativeAsset}`);
    return null;
  }
  return {
    path: assetPath,
    size: fs.statSync(assetPath).size,
    source: fs.readFileSync(assetPath, 'utf8'),
  };
};

if (!fs.existsSync(htmlPath)) {
  failures.push('dist/index.html is missing');
} else {
  const html = fs.readFileSync(htmlPath, 'utf8');
  const entryMatch = html.match(/<script[^>]+type="module"[^>]+src="([^"]+)"/i);
  if (!entryMatch) {
    failures.push('could not find the production module entry');
  } else {
    const relativeEntry = entryMatch[1].replace(/^\.\//, '').replace(/^\//, '');
    const entry = readAsset(relativeEntry);
    if (entry) {
      console.log(`Initial module: ${relativeEntry} (${entry.size} bytes)`);
      if (entry.size > 500_000) failures.push(`initial module is too large (${entry.size} bytes)`);

      const appName = entry.source.match(/import\(["']\.\/(App-[^"']+\.js)/)?.[1];
      const curriculumLoaderName = entry.source.match(/import\(["']\.\/(curriculumLoader-[^"']+\.js)/)?.[1];
      if (!appName) failures.push('application code is not loaded as a separate startup chunk');
      if (!curriculumLoaderName) failures.push('curriculum preload is missing from the startup entry');

      const app = appName ? readAsset(`assets/${appName}`) : null;
      if (app) {
        console.log(`Editor module: assets/${appName} (${app.size} bytes)`);
        if (app.size > 5_000_000) failures.push(`editor module is too large (${app.size} bytes)`);
        if (!/import\(["']\.\/webLlmReviewer-[^"']+\.js/.test(app.source)) {
          failures.push('optional WebLLM reviewer is not dynamically imported');
        }
        if (/Problem 5657/.test(app.source)) failures.push('exercise records leaked into the editor module');
      }

      const curriculumLoader = curriculumLoaderName ? readAsset(`assets/${curriculumLoaderName}`) : null;
      if (curriculumLoader) {
        console.log(`Curriculum loader: assets/${curriculumLoaderName} (${curriculumLoader.size} bytes)`);
        if (curriculumLoader.size > 50_000) failures.push(`curriculum loader is unexpectedly large (${curriculumLoader.size} bytes)`);
        if (!/import\(["']\.\/exercises-[^"']+\.js/.test(curriculumLoader.source)) failures.push('exercise catalog is not dynamically imported');
        if (!/import\(["']\.\/graders-[^"']+\.js/.test(curriculumLoader.source)) failures.push('grader catalog is not dynamically imported');
      }
    }
  }
}

console.log('Startup bundle audit');
console.log(`Failures: ${failures.length}`);
if (failures.length) {
  failures.forEach(failure => console.error(failure));
  process.exit(1);
}
