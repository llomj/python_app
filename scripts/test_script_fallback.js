const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');

function loadTsExports(fileName) {
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2020,
      jsx: ts.JsxEmit.React,
      esModuleInterop: true,
    },
    fileName,
  }).outputText;
  const sandbox = {
    exports: {},
    module: { exports: {} },
    require: request => {
      if (request === './graders') return loadTsExports('graders.ts');
      if (request === './exercises') return loadTsExports('exercises.ts');
      if (request === './types') return {};
      if (request === 'react') {
        return {
          __esModule: true,
          default: { createElement: () => null },
          useState: () => [null, () => {}],
          useEffect: () => {},
          useCallback: value => value,
          useRef: () => ({ current: null }),
          useMemo: value => value(),
        };
      }
      if (request === '@codemirror/view') {
        return {
          EditorView: {
            domEventHandlers: () => ({}),
            theme: () => ({}),
            lineWrapping: {},
          },
        };
      }
      if (request === '@codemirror/state') {
        return {
          EditorSelection: {},
        };
      }
      if (request === '@codemirror/autocomplete') {
        return {
          autocompletion: () => ({}),
          snippetCompletion: () => ({}),
        };
      }
      if (request === '@codemirror/lang-python') {
        return { python: () => ({}) };
      }
      if (request === '@codemirror/language') {
        return { indentUnit: { of: () => ({}) } };
      }
      if (request === '@uiw/react-codemirror') {
        return { __esModule: true, default: () => null };
      }
      return {};
    },
    localStorage: {
      getItem: () => null,
      setItem: () => {},
      removeItem: () => {},
    },
    window: {},
    navigator: {},
    console,
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

function runAutoGrade(script) {
  const result = spawnSync('python3', ['-c', `${script}\nprint(__auto_grader_json)\n`], {
    cwd: root,
    encoding: 'utf8',
    maxBuffer: 1024 * 1024 * 20,
    timeout: 30000,
  });
  if (result.error) throw result.error;
  if (result.status !== 0) {
    throw new Error(`Python grader exited ${result.status}: ${result.stderr}`);
  }
  const match = result.stdout.match(/({.*})\s*$/s);
  if (!match) {
    throw new Error(`Could not find grader JSON in output:\n${result.stdout}`);
  }
  return JSON.parse(match[1]);
}

const { buildAutoGradeScript } = loadTsExports('App.tsx');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const squareGrader = AUTO_GRADERS[8];
const sumMultiplyGrader = AUTO_GRADERS[118];
const closureGrader = AUTO_GRADERS[429];
const oopMethodGrader = AUTO_GRADERS[495];
const oopAttrsGrader = AUTO_GRADERS[496];
const printKwargsGrader = AUTO_GRADERS[1371];
const sumKwargsGrader = AUTO_GRADERS[1378];
const updateDictKwargsGrader = AUTO_GRADERS[1381];

const scriptAnswer = `
result = number ** 2
print(result)
`;
const scriptResult = runAutoGrade(buildAutoGradeScript(squareGrader, scriptAnswer));
if (!scriptResult.passed) {
  throw new Error(`Expected script answer to pass, got: ${JSON.stringify(scriptResult)}`);
}

const hardcodedAnswer = `
print(25)
`;
const hardcodedResult = runAutoGrade(buildAutoGradeScript(squareGrader, hardcodedAnswer));
if (hardcodedResult.passed) {
  throw new Error(`Expected hard-coded script answer to fail, got: ${JSON.stringify(hardcodedResult)}`);
}

const multiFunctionScriptAnswer = `
if function_name == "multiply":
    result = 1
    for item in lst:
        result *= item
else:
    result = sum(lst)
print(result)
`;
const multiFunctionResult = runAutoGrade(buildAutoGradeScript(sumMultiplyGrader, multiFunctionScriptAnswer));
if (!multiFunctionResult.passed) {
  throw new Error(`Expected multi-function script answer to pass, got: ${JSON.stringify(multiFunctionResult)}`);
}

const closureScriptAnswer = `
result = n * call_arg1
print(result)
`;
const closureScriptResult = runAutoGrade(buildAutoGradeScript(closureGrader, closureScriptAnswer));
if (!closureScriptResult.passed) {
  throw new Error(`Expected closure-style script answer to pass, got: ${JSON.stringify(closureScriptResult)}`);
}

const oopMethodScriptAnswer = `
if function_name == "Dog" and method_name == "speak":
    result = "Bark"
elif function_name == "Cat" and method_name == "speak":
    result = "Meow"
print(result)
`;
const oopMethodScriptResult = runAutoGrade(buildAutoGradeScript(oopMethodGrader, oopMethodScriptAnswer));
if (!oopMethodScriptResult.passed) {
  throw new Error(`Expected OOP method script answer to pass, got: ${JSON.stringify(oopMethodScriptResult)}`);
}

const oopAttrsScriptAnswer = `
result = {name: value for name, value in zip(attr_names, args)}
print(result)
`;
const oopAttrsScriptResult = runAutoGrade(buildAutoGradeScript(oopAttrsGrader, oopAttrsScriptAnswer));
if (!oopAttrsScriptResult.passed) {
  throw new Error(`Expected OOP attribute script answer to pass, got: ${JSON.stringify(oopAttrsScriptResult)}`);
}

const printKwargsScriptAnswer = `
print(kwargs)
`;
const printKwargsScriptResult = runAutoGrade(buildAutoGradeScript(printKwargsGrader, printKwargsScriptAnswer));
if (!printKwargsScriptResult.passed) {
  throw new Error(`Expected printed kwargs script answer to pass, got: ${JSON.stringify(printKwargsScriptResult)}`);
}

const sumKwargsScriptAnswer = `
result = sum(value for value in kwargs.values() if isinstance(value, (int, float)) and not isinstance(value, bool))
`;
const sumKwargsScriptResult = runAutoGrade(buildAutoGradeScript(sumKwargsGrader, sumKwargsScriptAnswer));
if (!sumKwargsScriptResult.passed) {
  throw new Error(`Expected numeric kwargs script answer to pass, got: ${JSON.stringify(sumKwargsScriptResult)}`);
}

const updateDictKwargsScriptAnswer = `
result = arg1.copy()
result.update(kwargs)
`;
const updateDictKwargsScriptResult = runAutoGrade(buildAutoGradeScript(updateDictKwargsGrader, updateDictKwargsScriptAnswer));
if (!updateDictKwargsScriptResult.passed) {
  throw new Error(`Expected dict/update kwargs script answer to pass, got: ${JSON.stringify(updateDictKwargsScriptResult)}`);
}

console.log('Script fallback smoke test passed.');
