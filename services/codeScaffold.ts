import type { AutoGrader, AutoTestCase } from '../graders';
import type { Exercise } from '../types';

const pythonLiteral = (value: unknown): string => {
  if (value === null || value === undefined) return 'None';
  if (typeof value === 'boolean') return value ? 'True' : 'False';
  if (typeof value === 'number') {
    if (Number.isNaN(value)) return 'float("nan")';
    if (value === Infinity) return 'float("inf")';
    if (value === -Infinity) return 'float("-inf")';
    return String(value);
  }
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(pythonLiteral).join(', ')}]`;
  if (typeof value === 'object') {
    return `{${Object.entries(value as Record<string, unknown>)
      .map(([key, item]) => `${pythonLiteral(key)}: ${pythonLiteral(item)}`)
      .join(', ')}}`;
  }
  return 'None';
};

const inferParameterNames = (test: AutoTestCase): string[] => {
  const values = [...(test.args || [])];
  const used = new Map<string, number>();
  const names = values.map(value => {
    let base = Array.isArray(value) ? 'items'
      : value !== null && typeof value === 'object' ? 'dictionary'
        : typeof value === 'string' ? 'text'
          : typeof value === 'number' ? 'number'
            : typeof value === 'boolean' ? 'flag'
              : 'value';
    const count = (used.get(base) || 0) + 1;
    used.set(base, count);
    if (count > 1) base += count;
    return base;
  });
  (test.argExpressions || []).forEach((_, index) => names.push(`value${names.length + index + 1}`));
  (test.argFunctionNames || []).forEach(name => names.push(name));
  if (test.functionListArgNames?.length) names.unshift('functions');
  return names;
};

const buildArguments = (test: AutoTestCase): string[] => {
  const args = (test.args || []).map(pythonLiteral);
  args.push(...(test.argExpressions || []));
  args.push(...(test.argFunctionNames || []));
  if (test.functionListArgNames?.length) args.unshift(`[${test.functionListArgNames.join(', ')}]`);
  if (test.kwargs) {
    args.push(...Object.entries(test.kwargs).map(([key, value]) => `${key}=${pythonLiteral(value)}`));
  }
  return args;
};

const findTopLevelFunctions = (code: string) => [...code.matchAll(/^(async\s+)?def\s+([A-Za-z_]\w*)\s*\(([^\n]*)\)\s*(?:->[^:]*)?:/gm)]
  .map(match => ({ name: match[2], parameters: match[3], async: Boolean(match[1]) }));

const findClassNames = (code: string) => [...code.matchAll(/^class\s+([A-Za-z_]\w*)\b/gm)].map(match => match[1]);

const GENERIC_COMMENT_PATTERN = /^#\s*(?:(?:write|enter|add|type|put)\b.*|(?:your|the)\s+(?:code|solution)\s+here\.?|todo\b.*)$/i;

const isGenericStarter = (code: string): boolean => {
  const lines = code.trim().split('\n').map(line => line.trim()).filter(Boolean);
  return lines.length === 0 || lines.every(line => (
    /^(?:from\s+[A-Za-z_.]+\s+import\s+.+|import\s+[A-Za-z_., ]+)$/.test(line)
    || line === 'pass'
    || GENERIC_COMMENT_PATTERN.test(line)
  ));
};

const stripTrailingComment = (line: string): string => line.replace(/\s+#.*$/, '').trimEnd();

const isBalancedSingleLine = (line: string): boolean => {
  if (!line || /\\\s*$/.test(line)) return false;
  const withoutEscapes = line.replace(/\\./g, '');
  const count = (character: string) => [...withoutEscapes].filter(item => item === character).length;
  return count("'") % 2 === 0
    && count('"') % 2 === 0
    && count('(') === count(')')
    && count('[') === count(']')
    && count('{') === count('}');
};

interface RepresentativeCall {
  lines: string[];
  sourceIndex: number;
}

const findRepresentativeCall = (solution: string, name: string): RepresentativeCall | null => {
  const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const callPattern = new RegExp(`^(?!\\s*(?:def|class)\\b).*\\b${escaped}\\s*\\(`);
  const candidates = solution.split('\n')
    .map((source, sourceIndex) => ({ line: stripTrailingComment(source).trim(), sourceIndex, topLevel: source === source.trimStart() }))
    .filter(item => item.topLevel
      && callPattern.test(item.line)
      && /^(?:print\s*\(|assert\s+|[A-Za-z_]\w*\s*=|[A-Za-z_]\w*\s*\()/.test(item.line)
      && isBalancedSingleLine(item.line));
  const candidate = candidates.find(item => /^print\s*\(/.test(item.line))
    || candidates.find(item => /^assert\s+/.test(item.line))
    || candidates[0];
  if (!candidate) return null;
  if (/^print\s*\(/.test(candidate.line)) return { lines: [candidate.line], sourceIndex: candidate.sourceIndex };
  if (/^assert\s+/.test(candidate.line)) return { lines: [candidate.line, 'print("Assertion passed")'], sourceIndex: candidate.sourceIndex };
  const assignment = candidate.line.match(/^([A-Za-z_]\w*)\s*=\s*(.+)$/);
  if (assignment) return { lines: [candidate.line, `print(${assignment[1]})`], sourceIndex: candidate.sourceIndex };
  return { lines: [`print(${candidate.line})`], sourceIndex: candidate.sourceIndex };
};

const buildCallableStarterFromSolution = (exercise: Exercise, language: 'en' | 'fr'): string | null => {
  const match = exercise.solution.match(/^(async\s+)?def\s+([A-Za-z_]\w*)\s*\(([^\n]*)\)\s*(?:->\s*[^:]*)?:/m);
  if (!match) return null;
  const signature = match[0];
  const functionName = match[2];
  const call = findRepresentativeCall(exercise.solution, functionName);
  const imports = [...new Set(`${exercise.initialCode}\n${exercise.solution.slice(0, match.index || 0)}`.split('\n')
    .map(line => line.trim())
    .filter(line => /^(?:from\s+[A-Za-z_.]+\s+import\s+.+|import\s+[A-Za-z_., ]+)$/.test(line)))];
  const setup = call ? exercise.solution.split('\n')
    .slice(0, call.sourceIndex)
    .filter(line => line === line.trimStart() && isSafeSetupLine(line))
    .map(stripTrailingComment)
    .filter(line => !imports.includes(line.trim()))
    .slice(-6) : [];
  const todo = language === 'fr' ? 'écrivez uniquement la logique ici' : 'write only the logic here';
  return [
    ...imports,
    imports.length ? '' : null,
    signature,
    `    # TODO: ${todo}`,
    '    pass',
    setup.length || call ? '' : null,
    ...setup,
    ...(call?.lines || []),
  ].filter(line => line !== null).join('\n');
};

const isSafeSetupLine = (line: string): boolean => {
  const trimmed = stripTrailingComment(line).trim();
  if (/^(?:from\s+[A-Za-z_.]+\s+import\s+.+|import\s+[A-Za-z_., ]+)$/.test(trimmed)) return true;
  const assignment = trimmed.match(/^([A-Za-z_]\w*)\s*=\s*(.+)$/);
  if (!assignment) return false;
  const value = assignment[2].trim();
  return /^(?:None|True|False|-?\d+(?:\.\d+)?|[rubfRUBF]*["']|\[|\{|\()/.test(value) && isBalancedSingleLine(trimmed);
};

const buildScriptStarterFromSolution = (exercise: Exercise, language: 'en' | 'fr'): string => {
  const scriptSection = exercise.solution.match(/#\s*(?:Using\s+)?Script approach\s*\n([\s\S]*?)(?=\n\s*#\s*(?:Using|Direct|Function|Built-in|Manual)\b|$)/i)?.[1] || exercise.solution;
  const lines = scriptSection.split('\n');
  const setup = lines.filter(isSafeSetupLine).map(stripTrailingComment).slice(0, 6);
  const todo = language === 'fr' ? '# TODO: écrivez la logique demandée ici' : '# TODO: write the requested logic here';
  return [...setup, setup.length ? '' : null, todo, 'result = None', 'print(result)']
    .filter(line => line !== null)
    .join('\n');
};

const buildScriptStarter = (exercise: Exercise, language: 'en' | 'fr'): string => {
  const initial = exercise.initialCode.trimEnd();
  if (!isGenericStarter(initial)) return initial;
  return buildCallableStarterFromSolution(exercise, language) || buildScriptStarterFromSolution(exercise, language);
};

const hasExecutableCall = (code: string, name: string) => {
  const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return new RegExp(`^(?:print[ \\t]*\\()?[ \\t]*${escaped}[ \\t]*\\(`, 'm').test(code);
};

const ensureFunctionStarter = (exercise: Exercise, grader: AutoGrader, test: AutoTestCase, language: 'en' | 'fr') => {
  const initial = exercise.initialCode.trimEnd();
  const definitions = findTopLevelFunctions(initial);
  const preferredName = test.functionName || grader.functionNames.find(name => definitions.some(definition => definition.name === name));
  const existing = definitions.find(definition => definition.name === preferredName) || definitions[0];
  if (existing) return { code: initial, functionName: existing.name, async: existing.async };

  const functionName = test.functionName || grader.functionNames[0];
  if (!functionName) return null;
  const parameters = inferParameterNames(test).join(', ');
  return {
    code: `${initial && !/^#\s*Write (?:your|the) (?:code|solution) here\.?$/i.test(initial.trim()) ? `${initial}\n\n` : ''}def ${functionName}(${parameters}):\n    # TODO: ${language === 'fr' ? 'écrivez uniquement la logique ici' : 'write only the logic here'}\n    pass`,
    functionName,
    async: false,
  };
};

const buildCallLines = (code: string, grader: AutoGrader, test: AutoTestCase, functionName: string, isAsync: boolean) => {
  if (hasExecutableCall(code, functionName)) return [];
  const args = buildArguments(test);
  const call = `${functionName}(${args.join(', ')})`;
  const callMethodArgs = [
    ...(test.callMethodArgs || []).map(pythonLiteral),
    ...(test.callMethodArgExpressions || []),
  ];

  if (test.callMethod) {
    return [
      `example = ${call}`,
      `print(example.${test.callMethod}(${callMethodArgs.join(', ')}))`,
    ];
  }
  if (test.getAttrs?.length) {
    return [
      `example = ${call}`,
      ...test.getAttrs.map(attribute => `print(example.${attribute})`),
    ];
  }
  if (test.callReturnedWith) {
    return [`print(${call}(${test.callReturnedWith.map(pythonLiteral).join(', ')}))`];
  }
  if (isAsync) {
    return ['import asyncio', `print(asyncio.run(${call}))`];
  }
  return [`print(${call})`];
};

export const buildExerciseCodeScaffold = (exercise: Exercise, grader?: AutoGrader, language: 'en' | 'fr' = 'en'): string => {
  const initial = exercise.initialCode.trimEnd();
  if (!grader || grader.mode === 'script' || !grader.tests?.length) return buildScriptStarter(exercise, language);

  const test = grader.tests[0];
  const classNames = findClassNames(initial);
  const targetName = test.functionName || grader.functionNames.find(name => classNames.includes(name));
  if (targetName && classNames.includes(targetName)) {
    const lines = buildCallLines(initial, grader, test, targetName, false);
    const comment = language === 'fr'
      ? '# Essayez la structure fournie avec des arguments représentatifs.'
      : '# Try the supplied structure with representative arguments.';
    return lines.length ? `${initial}\n\n${comment}\n${lines.join('\n')}\n` : `${initial}\n`;
  }

  const starter = ensureFunctionStarter(exercise, grader, test, language);
  if (!starter) return initial;
  const lines = buildCallLines(starter.code, grader, test, starter.functionName, starter.async);
  if (!lines.length) return `${starter.code}\n`;
  const comment = language === 'fr'
    ? '# Exécutez la fonction avec des arguments représentatifs.'
    : '# Run the function with representative arguments.';
  return `${starter.code}\n\n${comment}\n${lines.join('\n')}\n`;
};

export const getExerciseEditorCode = (exercise: Exercise, scaffoldEnabled: boolean, grader?: AutoGrader, language: 'en' | 'fr' = 'en'): string => (
  scaffoldEnabled ? buildExerciseCodeScaffold(exercise, grader, language) : exercise.initialCode
);
