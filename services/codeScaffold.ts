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
  if (!grader || grader.mode === 'script' || !grader.tests?.length) return initial;

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
