const fs = require('fs');
const path = require('path');

const source = fs.readFileSync(path.join(__dirname, '..', 'App.tsx'), 'utf8');
const failures = [];

const requirePattern = (pattern, message) => {
    if (!pattern.test(source)) failures.push(message);
};

const starCountsMatch = source.match(/const STAR_COUNTS = \[([^\]]+)\];/);
if (!starCountsMatch) {
    failures.push('STAR_COUNTS is missing.');
} else {
    const starCounts = starCountsMatch[1].split(',').map(value => Number(value.trim()));
    if (starCounts.some((count, index) => index > 0 && count <= starCounts[index - 1])) {
        failures.push('Every higher animal rank must add more falling stars.');
    }

    const masteryCount = Number(source.match(/const PYTHON_MASTERY_STAR_COUNT = (\d+);/)?.[1]);
    if (!masteryCount || masteryCount <= starCounts[starCounts.length - 1]) {
        failures.push('Python mastery must use more stars than the highest animal rank.');
    }
}

requirePattern(
    /successRate > 90 && userRank === RANKS\[RANKS\.length - 1\]/,
    'Python mastery must require an overall average above 90% and the top animal rank.',
);
requirePattern(
    /previous\.wins === 0 && currentStats\.success > 0 && rankIndex === 0/,
    'The first successful answer must celebrate mastery of Atom.',
);
requirePattern(
    /celebration\.kind === 'python' && resultSoundRef\.current/,
    'The mastery melody must be reserved for Python mastery.',
);
requirePattern(
    /You have mastered Python!/,
    'The Python mastery message is missing.',
);
requirePattern(
    /You have mastered[\s\S]{0,250}celebration\.rankName[\s\S]{0,100}level!/,
    'Animal celebrations must name the mastered level.',
);

console.log('Rank celebration audit');
console.log('Increasing animal star counts: checked');
console.log('Atom and named-rank milestones: checked');
console.log('Top-rank >90% Python mastery gate: checked');
console.log('Python mastery melody and enhanced stars: checked');

if (failures.length > 0) {
    failures.forEach(failure => console.error(`- ${failure}`));
    process.exit(1);
}

console.log('Result: passed');
