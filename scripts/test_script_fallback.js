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
      if (request === './atomicBeginnerExercises') return loadTsExports('atomicBeginnerExercises.ts');
      if (request === './atomicBeginnerGraders') return loadTsExports('atomicBeginnerGraders.ts');
      if (request === './whileLoopPracticeExercises') return loadTsExports('whileLoopPracticeExercises.ts');
      if (request === './whileLoopPracticeGraders') return loadTsExports('whileLoopPracticeGraders.ts');
      if (request === './conceptExpansionExercises') return loadTsExports('conceptExpansionExercises.ts');
      if (request === './conceptExpansionGraders') return loadTsExports('conceptExpansionGraders.ts');
      if (request === './advancedConceptExercises') return loadTsExports('advancedConceptExercises.ts');
      if (request === './advancedConceptGraders') return loadTsExports('advancedConceptGraders.ts');
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
const setExpressionGrader = AUTO_GRADERS[1761];
const lambdaExpressionGrader = AUTO_GRADERS[1972];
const writeFileGrader = AUTO_GRADERS[1765];
const composeHelperGrader = AUTO_GRADERS[598];
const mapWithIndexHelperGrader = AUTO_GRADERS[601];
const composeListHelperGrader = AUTO_GRADERS[604];
const stackMutationGrader = AUTO_GRADERS[1576];
const dictItemMutationGrader = AUTO_GRADERS[1622];
const listDeleteMutationGrader = AUTO_GRADERS[1623];
const methodExpressionGrader = AUTO_GRADERS[1574];
const mixedExceptionGrader = AUTO_GRADERS[944];
const attrExceptionGrader = AUTO_GRADERS[1571];
const pureExceptionGrader = AUTO_GRADERS[948];
const addKeyValuePairGrader = AUTO_GRADERS[797];
const countDigitGrader = AUTO_GRADERS[550];
const sumValuesGrader = AUTO_GRADERS[1211];

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

const setExpressionScriptAnswer = `
result = arg1 | arg2
`;
const setExpressionScriptResult = runAutoGrade(buildAutoGradeScript(setExpressionGrader, setExpressionScriptAnswer));
if (!setExpressionScriptResult.passed) {
  throw new Error(`Expected set expression script answer to pass, got: ${JSON.stringify(setExpressionScriptResult)}`);
}

const lambdaExpressionScriptAnswer = `
result = [item for item in lst if arg2(item)]
`;
const lambdaExpressionScriptResult = runAutoGrade(buildAutoGradeScript(lambdaExpressionGrader, lambdaExpressionScriptAnswer));
if (!lambdaExpressionScriptResult.passed) {
  throw new Error(`Expected lambda expression script answer to pass, got: ${JSON.stringify(lambdaExpressionScriptResult)}`);
}

const writeFileScriptAnswer = `
with open(arg1, "w", encoding="utf-8") as handle:
    handle.write(arg2)
`;
const writeFileScriptResult = runAutoGrade(buildAutoGradeScript(writeFileGrader, writeFileScriptAnswer));
if (!writeFileScriptResult.passed) {
  throw new Error(`Expected file-output script answer to pass, got: ${JSON.stringify(writeFileScriptResult)}`);
}

const composeHelperScriptAnswer = `
result = arg2(arg1(call_arg1))
`;
const composeHelperScriptResult = runAutoGrade(buildAutoGradeScript(composeHelperGrader, composeHelperScriptAnswer));
if (!composeHelperScriptResult.passed) {
  throw new Error(`Expected compose helper script answer to pass, got: ${JSON.stringify(composeHelperScriptResult)}`);
}

const mapWithIndexHelperScriptAnswer = `
result = [arg2(index, value) for index, value in enumerate(arg1)]
`;
const mapWithIndexHelperScriptResult = runAutoGrade(buildAutoGradeScript(mapWithIndexHelperGrader, mapWithIndexHelperScriptAnswer));
if (!mapWithIndexHelperScriptResult.passed) {
  throw new Error(`Expected map-with-index helper script answer to pass, got: ${JSON.stringify(mapWithIndexHelperScriptResult)}`);
}

const composeListHelperScriptAnswer = `
result = arg2
for func in arg1:
    result = func(result)
`;
const composeListHelperScriptResult = runAutoGrade(buildAutoGradeScript(composeListHelperGrader, composeListHelperScriptAnswer));
if (!composeListHelperScriptResult.passed) {
  throw new Error(`Expected compose-list helper script answer to pass, got: ${JSON.stringify(composeListHelperScriptResult)}`);
}

const stackMutationScriptAnswer = `
result = len(set_attrs.get("items", []))
`;
const stackMutationScriptResult = runAutoGrade(buildAutoGradeScript(stackMutationGrader, stackMutationScriptAnswer));
if (!stackMutationScriptResult.passed) {
  throw new Error(`Expected stack mutation script answer to pass, got: ${JSON.stringify(stackMutationScriptResult)}`);
}

const dictItemMutationScriptAnswer = `
store = {}
for spec in set_items:
    store[spec["key"]] = spec["value"]
result = store[method_arg1]
`;
const dictItemMutationScriptResult = runAutoGrade(buildAutoGradeScript(dictItemMutationGrader, dictItemMutationScriptAnswer));
if (!dictItemMutationScriptResult.passed) {
  throw new Error(`Expected dict item mutation script answer to pass, got: ${JSON.stringify(dictItemMutationScriptResult)}`);
}

const listDeleteMutationScriptAnswer = `
values = arg1.copy()
for index in sorted(delete_items, reverse=True):
    del values[index]
result = {"items": values}
`;
const listDeleteMutationScriptResult = runAutoGrade(buildAutoGradeScript(listDeleteMutationGrader, listDeleteMutationScriptAnswer));
if (!listDeleteMutationScriptResult.passed) {
  throw new Error(`Expected list delete mutation script answer to pass, got: ${JSON.stringify(listDeleteMutationScriptResult)}`);
}

const methodExpressionScriptAnswer = `
result = args == method_expression_args[0]
`;
const methodExpressionScriptResult = runAutoGrade(buildAutoGradeScript(methodExpressionGrader, methodExpressionScriptAnswer));
if (!methodExpressionScriptResult.passed) {
  throw new Error(`Expected method-expression script answer to pass, got: ${JSON.stringify(methodExpressionScriptResult)}`);
}

const mixedExceptionScriptAnswer = `
class NegativeNumberError(Exception):
    pass

if number < 0:
    raise NegativeNumberError("negative")
`;
const mixedExceptionScriptResult = runAutoGrade(buildAutoGradeScript(mixedExceptionGrader, mixedExceptionScriptAnswer));
if (!mixedExceptionScriptResult.passed) {
  throw new Error(`Expected mixed exception script answer to pass, got: ${JSON.stringify(mixedExceptionScriptResult)}`);
}

const attrExceptionScriptAnswer = `
if set_attrs.get("celsius", 0) < -273.15:
    raise ValueError("temperature below absolute zero")
result = set_attrs if set_attrs else None
`;
const attrExceptionScriptResult = runAutoGrade(buildAutoGradeScript(attrExceptionGrader, attrExceptionScriptAnswer));
if (!attrExceptionScriptResult.passed) {
  throw new Error(`Expected attribute exception script answer to pass, got: ${JSON.stringify(attrExceptionScriptResult)}`);
}

const pureExceptionScriptAnswer = `
raise RecursionError("fake")
`;
const pureExceptionScriptResult = runAutoGrade(buildAutoGradeScript(pureExceptionGrader, pureExceptionScriptAnswer));
if (pureExceptionScriptResult.passed) {
  throw new Error(`Expected pure exception-only script answer to stay blocked, got: ${JSON.stringify(pureExceptionScriptResult)}`);
}

const addKeyValuePairAnswer = `
def add_key_value_pair(dic):
    dic["c"] = 88
    return dic
`;
const addKeyValuePairResult = runAutoGrade(buildAutoGradeScript(addKeyValuePairGrader, addKeyValuePairAnswer));
if (!addKeyValuePairResult.passed) {
  throw new Error(`Expected add-key-value answer with arbitrary new pair to pass, got: ${JSON.stringify(addKeyValuePairResult)}`);
}

const addKeyValuePairNoop = `
def add_key_value_pair(dic):
    return dic
`;
const addKeyValuePairNoopResult = runAutoGrade(buildAutoGradeScript(addKeyValuePairGrader, addKeyValuePairNoop));
if (addKeyValuePairNoopResult.passed) {
  throw new Error(`Expected add-key-value no-op answer to fail, got: ${JSON.stringify(addKeyValuePairNoopResult)}`);
}

const addKeyValuePairInvalid = `
def add_key_value_pair(dic):
    return dic["c"] = 88
`;
const addKeyValuePairInvalidResult = runAutoGrade(buildAutoGradeScript(addKeyValuePairGrader, addKeyValuePairInvalid));
if (addKeyValuePairInvalidResult.passed) {
  throw new Error(`Expected invalid assignment-in-return answer to fail, got: ${JSON.stringify(addKeyValuePairInvalidResult)}`);
}

const countDigitAlternative = `
def count_digit(num, digit):
    return str(num).count(str(digit))

num = 15443674
print(count_digit(num, 4))
`;
const countDigitAlternativeResult = runAutoGrade(buildAutoGradeScript(countDigitGrader, countDigitAlternative));
if (!countDigitAlternativeResult.passed) {
  throw new Error(`Expected the two-argument count_digit solution to pass, got: ${JSON.stringify(countDigitAlternativeResult)}`);
}

const sumValuesAlternative = `
def sum_values():
    dic = {"a": 1, "b": 3}
    return sum(dic.values())

print(sum_values())
`;
const sumValuesAlternativeResult = runAutoGrade(buildAutoGradeScript(sumValuesGrader, sumValuesAlternative));
if (!sumValuesAlternativeResult.passed) {
  throw new Error(`Expected guarded fixed-data alternatives to pass, got: ${JSON.stringify(sumValuesAlternativeResult)}`);
}

const sumValuesWrongOperation = `
def sum_values():
    dic = {"a": 1, "b": 3}
    return len(dic)
`;
const sumValuesWrongOperationResult = runAutoGrade(buildAutoGradeScript(sumValuesGrader, sumValuesWrongOperation));
if (sumValuesWrongOperationResult.passed) {
  throw new Error(`Expected a fixed-data answer missing sum()/values() to fail, got: ${JSON.stringify(sumValuesWrongOperationResult)}`);
}

console.log('Script fallback smoke test passed.');
