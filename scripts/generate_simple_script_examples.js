const fs = require('fs');
const os = require('os');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const cache = new Map();

function resolveLocalModule(specifier) {
  const candidates = [specifier, `${specifier}.ts`, path.join(specifier, 'index.ts')];
  return candidates.find(candidate => fs.existsSync(path.join(root, candidate))) || null;
}

function loadTsExports(fileName) {
  if (cache.has(fileName)) return cache.get(fileName).exports;
  const compiled = ts.transpileModule(fs.readFileSync(path.join(root, fileName), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020 },
    fileName,
  }).outputText;
  const module = { exports: {} };
  cache.set(fileName, module);
  vm.runInNewContext(compiled, {
    module,
    exports: module.exports,
    require: specifier => {
      const resolved = resolveLocalModule(path.normalize(path.join(path.dirname(fileName), specifier)));
      return resolved ? loadTsExports(resolved) : {};
    },
  }, { filename: fileName });
  return module.exports;
}

function isLiteralValue(value) {
  if (value === null || ['string', 'number', 'boolean'].includes(typeof value)) return true;
  if (Array.isArray(value)) return value.every(isLiteralValue);
  return Boolean(value) && typeof value === 'object'
    && Object.entries(value).every(([key, item]) => typeof key === 'string' && isLiteralValue(item));
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const { GENERATED_SOLUTION_ALTERNATIVES } = loadTsExports('services/generatedSolutionAlternatives.ts');
const { SOLUTION_REFERENCE_OVERRIDES } = loadTsExports('services/solutionReferenceOverrides.ts');

function sourceSections(solution) {
  const heading = /^#\s*(?:[-=]+\s*)?(Using|Approach|Method|Version|Script|Direct|Built|Manual|Alternative|Try|Another|Equivalent|Convert|Modify|Consider|Nested|Advanced|Callable|Example|Reference)\b/i;
  const sections = [];
  let current = [];
  for (const line of solution.split('\n')) {
    if (heading.test(line)) {
      if (current.some(item => item.trim())) sections.push({ body: current.join('\n').trim() });
      current = [];
    } else {
      current.push(line);
    }
  }
  if (current.some(item => item.trim())) sections.push({ body: current.join('\n').trim() });
  return sections;
}

const records = EXERCISES.flatMap(exercise => {
  const grader = AUTO_GRADERS[exercise.id];
  const alternatives = GENERATED_SOLUTION_ALTERNATIVES[exercise.id] || [];
  if (!grader || alternatives.length < 3) return [];
  if (grader.mode === 'script') {
    const canonicalSections = sourceSections(SOLUTION_REFERENCE_OVERRIDES[exercise.id] || exercise.solution);
    return [{ id: exercise.id, mode: 'script', alternatives: [...canonicalSections, ...alternatives] }];
  }
  const test = [...(grader.optionalTests || []), ...(grader.tests || [])]
    .find(item => Array.isArray(item.args) && item.args.every(isLiteralValue)
      && isLiteralValue(item.kwargs || {}) && !item.inputValues?.length
      && !item.setupFiles && !item.setupDirs && !item.randomValues
      && !item.randomFloatValues && !item.randomChoiceValues
      && !item.randomSampleValues && !item.randomShuffleValues);
  if (!test) return [];
  return [{
    id: exercise.id,
    mode: 'function',
    names: grader.functionNames,
    args: test.args,
    kwargs: test.kwargs || {},
    alternatives,
  }];
});

const converter = String.raw`
import ast, contextlib, io, json, signal, sys

SAFE_IMPORTS = {'bisect', 'collections', 'decimal', 'fractions', 'functools', 'heapq',
                'itertools', 'math', 'operator', 're', 'statistics', 'string'}
BLOCKED_CALLS = {'breakpoint', 'compile', 'eval', 'exec', 'exit', 'input', 'open', 'quit', '__import__'}

class Timeout(Exception):
    pass

def timeout_handler(_signum, _frame):
    raise Timeout()

def literal_node(value):
    if isinstance(value, dict):
        return ast.Dict([literal_node(key) for key in value], [literal_node(item) for item in value.values()])
    if isinstance(value, list):
        return ast.List([literal_node(item) for item in value], ast.Load())
    return ast.Constant(value)

def has_blocked_construct(function):
    for node in ast.walk(function):
        if node is function:
            continue
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda,
                             ast.Yield, ast.YieldFrom, ast.Await, ast.Global, ast.Nonlocal)):
            return True
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS:
                return True
            if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                if node.func.value.id in {'os', 'pathlib', 'random', 'secrets', 'subprocess', 'sys'}:
                    return True
    return False

def safe_prefix(module, function, all_function_names):
    prefix = []
    for node in module.body:
        if node is function:
            break
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            modules = {alias.name.split('.')[0] for alias in node.names} if isinstance(node, ast.Import) else {(node.module or '').split('.')[0]}
            if modules and modules <= SAFE_IMPORTS:
                prefix.append(node)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            try:
                ast.literal_eval(value)
                prefix.append(node)
            except Exception:
                pass
    called_names = {node.func.id for node in ast.walk(function) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)}
    if called_names & (all_function_names - {function.name}):
        return None
    return prefix

def bind_parameters(function, args, kwargs):
    positional = [*function.args.posonlyargs, *function.args.args]
    if len(args) > len(positional) and not function.args.vararg:
        return None
    values = {}
    consumed_positional = min(len(args), len(positional))
    for parameter, value in zip(positional, args[:consumed_positional]):
        values[parameter.arg] = value
    for key, value in kwargs.items():
        if key in values:
            return None
        values[key] = value
    defaults = [None] * (len(positional) - len(function.args.defaults)) + list(function.args.defaults)
    assignments = []
    for parameter, default in zip(positional, defaults):
        if parameter.arg in values:
            value = literal_node(values[parameter.arg])
        elif default is not None:
            value = default
        else:
            return None
        assignments.append(ast.Assign([ast.Name(parameter.arg, ast.Store())], value))
    if function.args.vararg:
        assignments.append(ast.Assign(
            [ast.Name(function.args.vararg.arg, ast.Store())],
            ast.Tuple([literal_node(value) for value in args[consumed_positional:]], ast.Load()),
        ))
    consumed_names = {parameter.arg for parameter in positional}
    for parameter, default in zip(function.args.kwonlyargs, function.args.kw_defaults):
        if parameter.arg in kwargs:
            value = literal_node(kwargs[parameter.arg])
            consumed_names.add(parameter.arg)
        elif default is not None:
            value = default
        else:
            return None
        assignments.append(ast.Assign([ast.Name(parameter.arg, ast.Store())], value))
    remaining_kwargs = {key: value for key, value in kwargs.items() if key not in consumed_names}
    if function.args.kwarg:
        assignments.append(ast.Assign([ast.Name(function.args.kwarg.arg, ast.Store())], literal_node(remaining_kwargs)))
    elif remaining_kwargs:
        return None
    return assignments

def convert_function(record, body):
    module = ast.parse(body)
    functions = [node for node in module.body if isinstance(node, ast.FunctionDef)]
    function = next((node for name in record['names'] for node in functions if node.name == name), None)
    if not function or function.decorator_list or has_blocked_construct(function):
        return None
    returns = [node for node in ast.walk(function) if isinstance(node, ast.Return)]
    if len(returns) != 1 or not isinstance(function.body[-1], ast.Return):
        return None
    if any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == function.name for node in ast.walk(function)):
        return None
    prefix = safe_prefix(module, function, {node.name for node in functions})
    assignments = bind_parameters(function, record['args'], record['kwargs'])
    if prefix is None or assignments is None:
        return None
    result_expression = function.body[-1].value or ast.Constant(None)
    script = ast.Module([*prefix, *assignments, *function.body[:-1], ast.Assign([ast.Name('__script_result', ast.Store())], result_expression)], [])
    ast.fix_missing_locations(script)

    original_module = ast.Module([*prefix, function], [])
    ast.fix_missing_locations(original_module)
    original_namespace = {}
    script_namespace = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(original_module, '<reference>', 'exec'), original_namespace)
        expected = original_namespace[function.name](*record['args'], **record['kwargs'])
        exec(compile(script, '<script>', 'exec'), script_namespace)
    actual = script_namespace['__script_result']
    if type(actual) is not type(expected) or actual != expected:
        return None
    script.body[-1] = ast.Expr(ast.Call(ast.Name('print', ast.Load()), [result_expression], []))
    ast.fix_missing_locations(script)
    return ast.unparse(script)

def direct_script(body):
    module = ast.parse(body)
    if any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda,
                             ast.Yield, ast.YieldFrom, ast.Await)) for node in ast.walk(module)):
        return None
    if any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS for node in ast.walk(module)):
        return None
    compile(module, '<direct-script>', 'exec')
    return ast.unparse(module)

signal.signal(signal.SIGALRM, timeout_handler)
for line in sys.stdin:
    record = json.loads(line)
    result = None
    try:
        signal.alarm(1)
        for alternative in record['alternatives']:
            result = direct_script(alternative['body']) if record['mode'] == 'script' else convert_function(record, alternative['body'])
            if result:
                break
    except Exception:
        result = None
    finally:
        signal.alarm(0)
    if result:
        print(json.dumps({'id': record['id'], 'body': result}))
`;

const converted = spawnSync('python3', ['-c', converter], {
  input: records.map(record => JSON.stringify(record)).join('\n'),
  cwd: root,
  encoding: 'utf8',
  maxBuffer: 50 * 1024 * 1024,
  timeout: 300000,
});
if (converted.error) throw converted.error;
if (converted.status !== 0) throw new Error(converted.stderr);

const convertedItems = converted.stdout.trim().split('\n').filter(Boolean).map(line => JSON.parse(line));
const nativeItems = convertedItems.filter(item => AUTO_GRADERS[item.id]?.mode === 'script');
const temporaryDirectory = fs.mkdtempSync(path.join(os.tmpdir(), 'simple-script-examples-'));
const candidateFile = path.join(temporaryDirectory, 'candidates.json');
const resultsFile = path.join(temporaryDirectory, 'results.json');
fs.writeFileSync(candidateFile, JSON.stringify(nativeItems.map((item, index) => ({
  id: item.id,
  candidateId: String(index),
  solution: item.body,
  behaviorOnly: true,
}))));
const validation = spawnSync(process.execPath, [
  path.join(root, 'scripts/validate_graders.js'),
  `--candidate-file=${candidateFile}`,
  `--results-file=${resultsFile}`,
  `--max-failures=${nativeItems.length}`,
], { cwd: root, encoding: 'utf8', maxBuffer: 50 * 1024 * 1024, timeout: 300000 });
if (validation.error) throw validation.error;
if (validation.status !== 0) throw new Error(validation.stderr || validation.stdout);
const nativeResults = JSON.parse(fs.readFileSync(resultsFile, 'utf8'));
const passingNativeIds = new Set(nativeResults
  .filter(result => result.passed)
  .map(result => nativeItems[Number(result.candidateId)]?.id));
fs.rmSync(temporaryDirectory, { recursive: true, force: true });

const acceptedItems = convertedItems.filter(item => (
  AUTO_GRADERS[item.id]?.mode !== 'script' || passingNativeIds.has(item.id)
));
const scripts = Object.fromEntries(acceptedItems.map(item => [item.id, item.body]));
const output = [
  '// Generated by scripts/generate_simple_script_examples.js.',
  '// Each entry is a compile-checked, definition-free script; converted function examples are behavior-checked.',
  `export const GENERATED_SIMPLE_SCRIPT_EXAMPLES: Readonly<Record<number, string>> = ${JSON.stringify(scripts, null, 2)};`,
  '',
].join('\n');
fs.writeFileSync(path.join(root, 'services/generatedSimpleScriptExamples.ts'), output);
console.log(`Generated simple script examples for ${Object.keys(scripts).length}/${EXERCISES.length} exercises (${passingNativeIds.size}/${nativeItems.length} native scripts passed full grader validation).`);
