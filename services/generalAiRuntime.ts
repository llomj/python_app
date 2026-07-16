export type GeneralAiRuntimeLanguage = 'en' | 'fr';

export interface GeneralAiRuntimeSafety {
  safe: boolean;
  reason: string;
  code: string;
}

export interface GeneralAiRuntimeResult {
  ok: boolean;
  stdout: string;
  resultRepr: string;
  resultType: string;
  errorType: string;
  errorMessage: string;
  errorLine?: number;
  variables?: Record<string, string>;
  executionTrace?: Array<{
    line: number;
    event?: 'call' | 'line' | 'return';
    function?: string;
    variables: Record<string, string>;
    changedVariables?: Record<string, string>;
    returnValue?: string;
  }>;
}

export interface GeneralAiTestResult {
  expression: string;
  passed: boolean;
  actual: string;
  expected: string;
  errorType: string;
  errorMessage: string;
  stdout: string;
  mismatchKind?: string;
  mismatchPath?: string;
  mismatchDetail?: string;
}

export interface GeneralAiTestRunResult {
  ok: boolean;
  tests: GeneralAiTestResult[];
  setupError: string;
}

export interface GeneralAiDoctestRunResult {
  ok: boolean;
  attempted: number;
  failed: number;
  report: string;
  setupError: string;
}

export interface GeneralAiAstAnalysisResult {
  ok: boolean;
  errorType: string;
  errorMessage: string;
  errorLine?: number;
  functions: Array<{ name: string; line: number; parameters: string[]; async: boolean; returns: number }>;
  classes: Array<{ name: string; line: number; bases: string[] }>;
  assignments: Array<{ line: number; targets: string[] }>;
  calls: Array<{ line: number; name: string }>;
  loops: Array<{ line: number; kind: string }>;
  branches: Array<{ line: number; kind: string }>;
  returns: Array<{ line: number; hasValue: boolean }>;
  mutations: Array<{ line: number; target: string; method: string }>;
  imports: Array<{ line: number; name: string }>;
  loadedNames: string[];
  storedNames: string[];
}

export const extractGeneralAiPythonCode = (question: string): string => {
  const fenced = question.match(/```(?:python)?\s*\n?([\s\S]*?)```/i);
  if (fenced) return fenced[1].trim();
  return question.split('\n')
    .filter(line => !/^\s*(?:explain|analyse|analyze|debug|what does|why does)\b/i.test(line))
    .join('\n')
    .trim();
};

const SAFE_CALLS = new Set([
  'abs', 'all', 'any', 'bool', 'bytearray', 'bytes', 'dict', 'enumerate', 'float',
  'frozenset', 'int', 'iter', 'len', 'list', 'max', 'memoryview', 'min', 'next',
  'print', 'range', 'repr', 'reversed', 'round', 'set', 'sorted', 'str', 'sum',
  'tuple', 'type', 'zip', 'append', 'capitalize', 'clear', 'close', 'copy', 'decode',
  'count', 'endswith', 'extend', 'find', 'get', 'index', 'insert', 'items', 'join',
  'keys', 'lower', 'pop', 'remove', 'replace', 'reverse', 'sort', 'split', 'startswith',
  'strip', 'send', 'throw', 'tobytes', 'update', 'upper', 'values', 'hex',
]);

export const assessGeneralAiRuntimeSafety = (question: string): GeneralAiRuntimeSafety => {
  const code = extractGeneralAiPythonCode(question);
  if (!code) return { safe: false, reason: 'No Python code was found.', code };
  if (code.length > 2400 || code.split('\n').length > 60) return { safe: false, reason: 'The snippet is too large for automatic execution.', code };
  if (/\b(?:import|from|input|open|exec|eval|compile|globals|locals|breakpoint|help|memoryview)\b|__/i.test(code)) {
    return { safe: false, reason: 'The snippet uses imports, I/O, dynamic execution, introspection, or dunder access.', code };
  }
  if (/^\s*(?:while|async|with|try)\b/m.test(code)) {
    return { safe: false, reason: 'Automatic runtime evidence rejects while loops, async code, context managers, and exception-control blocks.', code };
  }
  if (/\b\d{8,}\b|\*\s*\d{6,}|range\s*\([^)]*\d{7,}/.test(code)) {
    return { safe: false, reason: 'The snippet may allocate or compute too much data.', code };
  }
  for (const match of code.matchAll(/\brange\s*\(([^)]*)\)/g)) {
    const numericArguments = match[1].split(',').map(value => Number(value.trim()));
    if (numericArguments.every(Number.isFinite) && numericArguments.some(value => Math.abs(value) > 5000)) {
      return { safe: false, reason: 'A range() bound is too large for tutor execution.', code };
    }
  }
  const userCallables = new Set([...code.matchAll(/^\s*(?:def|class)\s+([A-Za-z_]\w*)/gm)].map(match => match[1]));
  const calls = [...code.matchAll(/\b([A-Za-z_]\w*)\s*\(/g)].map(match => match[1]);
  const unknownCall = calls.find(name => !SAFE_CALLS.has(name) && !userCallables.has(name));
  if (unknownCall) return { safe: false, reason: `Call to ${unknownCall}() is outside the safe runtime allowlist.`, code };
  return { safe: true, reason: 'Straight-line snippet uses only safe built-ins and expressions.', code };
};

export const assessGeneralAiTestSafety = (question: string): GeneralAiRuntimeSafety => {
  const base = assessGeneralAiRuntimeSafety(question);
  if (!base.safe) return base;
  const assertions = base.code.match(/^\s*assert\s+/gm) || [];
  if (!assertions.length) return { safe: false, reason: 'No assertions were found.', code: base.code };
  if (assertions.length > 20) return { safe: false, reason: 'A maximum of 20 assertions can run at once.', code: base.code };
  if ([...base.code.matchAll(/\b\d+(?:\.\d+)?\b/g)].some(match => Number(match[0]) > 5000)) {
    return { safe: false, reason: 'Test literals must not exceed 5000.', code: base.code };
  }
  const lines = base.code.split('\n');
  for (let index = 0; index < lines.length; index += 1) {
    const definition = lines[index].match(/^def\s+([A-Za-z_]\w*)\s*\([^\n]*\):/);
    if (!definition) continue;
    const body: string[] = [];
    for (let bodyIndex = index + 1; bodyIndex < lines.length; bodyIndex += 1) {
      if (!lines[bodyIndex].trim()) continue;
      if (!/^\s+/.test(lines[bodyIndex])) break;
      body.push(lines[bodyIndex]);
    }
    if (new RegExp(`\\b${definition[1]}\\s*\\(`).test(body.join('\n'))) {
      return { safe: false, reason: 'Recursive functions are not executed by the local test runner.', code: base.code };
    }
  }
  return { safe: true, reason: 'Assertions use the bounded local runtime policy.', code: base.code };
};

export const assessGeneralAiDoctestSafety = (question: string): GeneralAiRuntimeSafety => {
  const base = assessGeneralAiRuntimeSafety(question);
  if (!base.safe) return base;
  const examples = base.code.match(/^\s*>>>\s+/gm) || [];
  if (!examples.length) return { safe: false, reason: 'No doctest prompts were found.', code: base.code };
  if (examples.length > 20) return { safe: false, reason: 'A maximum of 20 doctest examples can run at once.', code: base.code };
  return { safe: true, reason: 'Doctest examples use the bounded local runtime policy.', code: base.code };
};

export const buildGeneralAiAstAnalysisScript = (code: string): string => `
import ast, json
__ast_source = ${JSON.stringify(code)}
__ast_payload = {
    "ok": False, "errorType": "", "errorMessage": "", "errorLine": None,
    "functions": [], "classes": [], "assignments": [], "calls": [],
    "loops": [], "branches": [], "returns": [], "mutations": [], "imports": [],
    "loadedNames": [], "storedNames": [],
}
try:
    __ast_tree = ast.parse(__ast_source, mode="exec")
    __ast_mutating_methods = {"append", "clear", "discard", "extend", "insert", "pop", "popitem", "remove", "reverse", "setdefault", "sort", "update", "add"}
    def __ast_name(node):
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            prefix = __ast_name(node.value)
            return f"{prefix}.{node.attr}" if prefix else node.attr
        if isinstance(node, ast.Subscript):
            return __ast_name(node.value)
        if isinstance(node, (ast.Tuple, ast.List)):
            return ", ".join(filter(None, (__ast_name(item) for item in node.elts)))
        return ""
    for __ast_node in ast.walk(__ast_tree):
        if isinstance(__ast_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            __ast_parameters = [arg.arg for arg in [*__ast_node.args.posonlyargs, *__ast_node.args.args, *__ast_node.args.kwonlyargs]]
            if __ast_node.args.vararg:
                __ast_parameters.append("*" + __ast_node.args.vararg.arg)
            if __ast_node.args.kwarg:
                __ast_parameters.append("**" + __ast_node.args.kwarg.arg)
            __ast_return_count = sum(isinstance(item, ast.Return) for item in ast.walk(__ast_node))
            __ast_payload["functions"].append({"name": __ast_node.name, "line": __ast_node.lineno, "parameters": __ast_parameters, "async": isinstance(__ast_node, ast.AsyncFunctionDef), "returns": __ast_return_count})
        elif isinstance(__ast_node, ast.ClassDef):
            __ast_payload["classes"].append({"name": __ast_node.name, "line": __ast_node.lineno, "bases": [__ast_name(base) for base in __ast_node.bases if __ast_name(base)]})
        elif isinstance(__ast_node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            __ast_targets = __ast_node.targets if isinstance(__ast_node, ast.Assign) else [__ast_node.target]
            __ast_payload["assignments"].append({"line": __ast_node.lineno, "targets": [__ast_name(target) for target in __ast_targets if __ast_name(target)]})
        elif isinstance(__ast_node, ast.Call):
            __ast_call_name = __ast_name(__ast_node.func)
            __ast_payload["calls"].append({"line": __ast_node.lineno, "name": __ast_call_name or "<expression>"})
            if isinstance(__ast_node.func, ast.Attribute) and __ast_node.func.attr in __ast_mutating_methods:
                __ast_payload["mutations"].append({"line": __ast_node.lineno, "target": __ast_name(__ast_node.func.value), "method": __ast_node.func.attr})
        elif isinstance(__ast_node, (ast.For, ast.AsyncFor, ast.While)):
            __ast_payload["loops"].append({"line": __ast_node.lineno, "kind": type(__ast_node).__name__})
        elif isinstance(__ast_node, (ast.If, ast.IfExp, ast.Match, ast.Try)):
            __ast_payload["branches"].append({"line": __ast_node.lineno, "kind": type(__ast_node).__name__})
        elif isinstance(__ast_node, ast.Return):
            __ast_payload["returns"].append({"line": __ast_node.lineno, "hasValue": __ast_node.value is not None})
        elif isinstance(__ast_node, (ast.Import, ast.ImportFrom)):
            if isinstance(__ast_node, ast.Import):
                __ast_names = [alias.name for alias in __ast_node.names]
            else:
                __ast_names = [f"{__ast_node.module or ''}.{alias.name}".strip(".") for alias in __ast_node.names]
            __ast_payload["imports"].extend({"line": __ast_node.lineno, "name": name} for name in __ast_names)
        elif isinstance(__ast_node, ast.Name):
            key = "storedNames" if isinstance(__ast_node.ctx, ast.Store) else "loadedNames" if isinstance(__ast_node.ctx, ast.Load) else None
            if key and __ast_node.id not in __ast_payload[key]:
                __ast_payload[key].append(__ast_node.id)
    for __ast_key in ("functions", "classes", "assignments", "calls", "loops", "branches", "returns", "mutations", "imports"):
        __ast_payload[__ast_key].sort(key=lambda item: (item["line"], item.get("name", "")))
    __ast_payload["ok"] = True
except SyntaxError as __ast_error:
    __ast_payload.update({"errorType": "SyntaxError", "errorMessage": __ast_error.msg, "errorLine": __ast_error.lineno})
except Exception as __ast_error:
    __ast_payload.update({"errorType": type(__ast_error).__name__, "errorMessage": str(__ast_error)})
json.dumps(__ast_payload)
`;

export const formatGeneralAiAstAnalysis = (result: GeneralAiAstAnalysisResult, language: GeneralAiRuntimeLanguage): string => {
  const fr = language === 'fr';
  if (!result.ok) {
    return `**${fr ? 'Analyse syntaxique Python' : 'Python syntax analysis'}**\n${result.errorType || 'SyntaxError'}${result.errorLine ? ` (${fr ? 'ligne' : 'line'} ${result.errorLine})` : ''}: ${result.errorMessage || (fr ? 'syntaxe invalide' : 'invalid syntax')}`;
  }
  const sections: string[] = [`**${fr ? 'Structure Python vérifiée (AST)' : 'Verified Python structure (AST)'}**`];
  if (result.functions.length) sections.push(`${fr ? 'Fonctions' : 'Functions'}:\n${result.functions.map(item => `- \`${item.async ? 'async ' : ''}${item.name}(${item.parameters.join(', ')})\` — ${fr ? 'ligne' : 'line'} ${item.line}; ${item.returns} ${fr ? 'instruction(s) return' : 'return statement(s)'}`).join('\n')}`);
  if (result.classes.length) sections.push(`${fr ? 'Classes' : 'Classes'}:\n${result.classes.map(item => `- \`${item.name}\` — ${fr ? 'ligne' : 'line'} ${item.line}${item.bases.length ? `; ${fr ? 'bases' : 'bases'}: ${item.bases.join(', ')}` : ''}`).join('\n')}`);
  if (result.assignments.length) sections.push(`${fr ? 'Affectations' : 'Assignments'}:\n${result.assignments.slice(0, 12).map(item => `- ${fr ? 'Ligne' : 'Line'} ${item.line}: \`${item.targets.join(', ') || '?'}\``).join('\n')}`);
  if (result.calls.length) sections.push(`${fr ? 'Appels' : 'Calls'}:\n${result.calls.slice(0, 16).map(item => `- ${fr ? 'Ligne' : 'Line'} ${item.line}: \`${item.name}()\``).join('\n')}`);
  if (result.loops.length || result.branches.length) sections.push(`${fr ? 'Flux de contrôle' : 'Control flow'}:\n${[...result.loops, ...result.branches].sort((a, b) => a.line - b.line).map(item => `- ${fr ? 'Ligne' : 'Line'} ${item.line}: ${item.kind}`).join('\n')}`);
  if (result.mutations.length) sections.push(`${fr ? 'Mutations détectées' : 'Detected mutations'}:\n${result.mutations.map(item => `- ${fr ? 'Ligne' : 'Line'} ${item.line}: \`${item.target}.${item.method}()\``).join('\n')}`);
  if (result.imports.length) sections.push(`${fr ? 'Importations (analysées, non exécutées)' : 'Imports (analyzed, not executed)'}:\n${result.imports.map(item => `- ${fr ? 'Ligne' : 'Line'} ${item.line}: \`${item.name}\``).join('\n')}`);
  if (result.storedNames.length || result.loadedNames.length) sections.push(`${fr ? 'Résolution des noms' : 'Name resolution'}:\n- ${fr ? 'Écrits' : 'Stored'}: ${result.storedNames.map(name => `\`${name}\``).join(', ') || '—'}\n- ${fr ? 'Lus' : 'Loaded'}: ${result.loadedNames.map(name => `\`${name}\``).join(', ') || '—'}`);
  return sections.join('\n\n');
};

export const buildGeneralAiTestRunnerScript = (code: string): string => `
import ast, contextlib, io, json
__test_source = ${JSON.stringify(code)}
__test_payload = {"ok": False, "tests": [], "setupError": ""}
try:
    __test_tree = ast.parse(__test_source, mode="exec")
    __test_assertions = [node for node in __test_tree.body if isinstance(node, ast.Assert)]
    __test_setup = ast.Module(body=[node for node in __test_tree.body if not isinstance(node, ast.Assert)], type_ignores=[])
    ast.fix_missing_locations(__test_setup)
    __test_namespace = {"__builtins__": __builtins__}
    exec(compile(__test_setup, "<general-ai-tests>", "exec"), __test_namespace, __test_namespace)
    for __test_node in __test_assertions:
        __test_stdout = io.StringIO()
        __test_item = {
            "expression": ast.get_source_segment(__test_source, __test_node.test) or "assert",
            "passed": False,
            "actual": "",
            "expected": "True",
            "errorType": "",
            "errorMessage": "",
            "stdout": "",
            "mismatchKind": "",
            "mismatchPath": "",
            "mismatchDetail": "",
        }
        try:
            if isinstance(__test_node.test, ast.Compare) and len(__test_node.test.ops) == 1 and isinstance(__test_node.test.ops[0], ast.Eq):
                __test_actual_node = ast.Expression(__test_node.test.left)
                __test_expected_node = ast.Expression(__test_node.test.comparators[0])
                ast.fix_missing_locations(__test_actual_node)
                ast.fix_missing_locations(__test_expected_node)
                with contextlib.redirect_stdout(__test_stdout):
                    __test_expected = eval(compile(__test_expected_node, "<general-ai-test-expected>", "eval"), __test_namespace, __test_namespace)
                    __test_item["expected"] = repr(__test_expected)
                    __test_actual = eval(compile(__test_actual_node, "<general-ai-test-actual>", "eval"), __test_namespace, __test_namespace)
                __test_item["passed"] = __test_actual == __test_expected
                __test_item["actual"] = repr(__test_actual)
                if not __test_item["passed"]:
                    if type(__test_actual) is not type(__test_expected):
                        __test_item["mismatchKind"] = "type"
                        __test_item["mismatchDetail"] = f"{type(__test_actual).__name__} != {type(__test_expected).__name__}"
                    elif isinstance(__test_actual, (int, float)) and not isinstance(__test_actual, bool):
                        __test_item["mismatchKind"] = "number"
                        __test_item["mismatchDetail"] = repr(__test_actual - __test_expected)
                    elif isinstance(__test_actual, (str, list, tuple)):
                        __test_item["mismatchKind"] = "sequence"
                        __test_item["mismatchDetail"] = f"length {len(__test_actual)} != {len(__test_expected)}"
                        for __test_index, (__test_left, __test_right) in enumerate(zip(__test_actual, __test_expected)):
                            if __test_left != __test_right:
                                __test_item["mismatchPath"] = f"[{__test_index}]"
                                __test_item["mismatchDetail"] = f"{repr(__test_left)} != {repr(__test_right)}"
                                break
                    elif isinstance(__test_actual, dict):
                        __test_missing = [repr(key) for key in __test_expected.keys() - __test_actual.keys()]
                        __test_extra = [repr(key) for key in __test_actual.keys() - __test_expected.keys()]
                        __test_different = [repr(key) for key in __test_actual.keys() & __test_expected.keys() if __test_actual[key] != __test_expected[key]]
                        __test_item["mismatchKind"] = "mapping"
                        __test_item["mismatchDetail"] = f"missing={__test_missing}; extra={__test_extra}; different={__test_different}"
                    elif isinstance(__test_actual, (set, frozenset)):
                        __test_item["mismatchKind"] = "set"
                        __test_item["mismatchDetail"] = f"missing={repr(__test_expected - __test_actual)}; extra={repr(__test_actual - __test_expected)}"
                    else:
                        __test_item["mismatchKind"] = "value"
                        __test_item["mismatchDetail"] = "values are not equal"
            else:
                __test_expression = ast.Expression(__test_node.test)
                ast.fix_missing_locations(__test_expression)
                with contextlib.redirect_stdout(__test_stdout):
                    __test_actual = eval(compile(__test_expression, "<general-ai-test-condition>", "eval"), __test_namespace, __test_namespace)
                __test_item["passed"] = bool(__test_actual)
                __test_item["actual"] = repr(__test_actual)
        except Exception as __test_error:
            __test_item["errorType"] = type(__test_error).__name__
            __test_item["errorMessage"] = str(__test_error)
        __test_item["stdout"] = __test_stdout.getvalue()
        __test_payload["tests"].append(__test_item)
    __test_payload["ok"] = True
except Exception as __test_setup_error:
    __test_payload["setupError"] = f"{type(__test_setup_error).__name__}: {__test_setup_error}"
json.dumps(__test_payload)
`;

export const buildGeneralAiDoctestRunnerScript = (code: string): string => `
import contextlib, doctest, io, json, types
__doctest_source = ${JSON.stringify(code)}
__doctest_payload = {"ok": False, "attempted": 0, "failed": 0, "report": "", "setupError": ""}
try:
    __doctest_module = types.ModuleType("general_ai_doctest")
    exec(compile(__doctest_source, "<general-ai-doctest>", "exec"), __doctest_module.__dict__, __doctest_module.__dict__)
    __doctest_finder = doctest.DocTestFinder(exclude_empty=True)
    __doctest_runner = doctest.DocTestRunner(optionflags=doctest.NORMALIZE_WHITESPACE)
    __doctest_output = io.StringIO()
    for __doctest_case in __doctest_finder.find(__doctest_module):
        __doctest_runner.run(__doctest_case, out=__doctest_output.write)
    with contextlib.redirect_stdout(__doctest_output):
        __doctest_summary = __doctest_runner.summarize(verbose=False)
    __doctest_payload.update({
        "ok": True,
        "attempted": __doctest_summary.attempted,
        "failed": __doctest_summary.failed,
        "report": __doctest_output.getvalue(),
    })
except Exception as __doctest_error:
    __doctest_payload["setupError"] = f"{type(__doctest_error).__name__}: {__doctest_error}"
json.dumps(__doctest_payload)
`;

export const formatGeneralAiDoctestResults = (result: GeneralAiDoctestRunResult, language: GeneralAiRuntimeLanguage): string => {
  const fr = language === 'fr';
  if (!result.ok) return `**${fr ? 'Exécution locale des doctests' : 'Local doctest execution'}**\n${fr ? 'Échec de préparation' : 'Setup failed'}: \`${result.setupError || 'unknown error'}\`.`;
  const passed = result.attempted - result.failed;
  return [
    `**${fr ? 'Résultats des doctests locaux' : 'Local doctest results'}: ${passed}/${result.attempted} ${fr ? 'réussis' : 'passed'}**`,
    result.report ? `${fr ? 'Rapport exact de Python' : 'Exact Python report'}:\n\`\`\`text\n${result.report.trim()}\n\`\`\`` : (fr ? 'Tous les exemples produisent la sortie attendue.' : 'Every example produced the expected output.'),
  ].join('\n\n');
};

export const formatGeneralAiTestResults = (result: GeneralAiTestRunResult, language: GeneralAiRuntimeLanguage): string => {
  const fr = language === 'fr';
  if (!result.ok) return `**${fr ? 'Exécution locale des tests' : 'Local test execution'}**\n${fr ? 'Échec de préparation' : 'Setup failed'}: \`${result.setupError || 'unknown error'}\`.`;
  const passed = result.tests.filter(test => test.passed).length;
  return [
    `**${fr ? 'Résultats des tests locaux' : 'Local test results'}: ${passed}/${result.tests.length} ${fr ? 'réussis' : 'passed'}**`,
    result.tests.map((test, index) => [
      `${index + 1}. ${test.passed ? '✓' : '✗'} \`${test.expression}\``,
      `${fr ? 'Attendu' : 'Expected'}: \`${test.expected}\``,
      `${fr ? 'Réel' : 'Actual'}: \`${test.actual || (test.errorType ? 'no value' : 'None')}\``,
      test.errorType ? `${fr ? 'Exception' : 'Exception'}: \`${test.errorType}: ${test.errorMessage}\`` : '',
      !test.passed && test.mismatchKind ? `${fr ? 'Diagnostic' : 'Diagnosis'}: ${
        test.mismatchKind === 'number'
          ? (fr ? `écart réel − attendu = \`${test.mismatchDetail}\`` : `actual − expected = \`${test.mismatchDetail}\``)
          : test.mismatchKind === 'sequence'
            ? `${test.mismatchPath ? `${fr ? 'première différence à' : 'first difference at'} \`${test.mismatchPath}\`: ` : ''}\`${test.mismatchDetail}\``
            : test.mismatchKind === 'type'
              ? `${fr ? 'types différents' : 'different types'}: \`${test.mismatchDetail}\``
              : `\`${test.mismatchDetail}\``
      }` : '',
      test.stdout ? `${fr ? 'Sortie' : 'Output'}:\n\`\`\`text\n${test.stdout.trim()}\n\`\`\`` : '',
    ].filter(Boolean).join('\n')).join('\n\n'),
  ].join('\n\n');
};

export const buildGeneralAiRuntimeScript = (code: string): string => `
import ast, contextlib, io, json, traceback, sys, types
__general_ai_source = ${JSON.stringify(code)}
__general_ai_stdout = io.StringIO()
__general_ai_result = None
__general_ai_payload = {}
__general_ai_trace = []
__general_ai_previous = {}
def __general_ai_repr(value):
    try:
        text = repr(value)
        return text if len(text) <= 200 else text[:197] + "..."
    except Exception:
        return "<unrepresentable>"
def __general_ai_variables(namespace):
    return {
        name: __general_ai_repr(value)
        for name, value in namespace.items()
        if not name.startswith("__") and not isinstance(value, (types.FunctionType, type, types.ModuleType))
    }
def __general_ai_tracer(frame, event, arg):
    if frame.f_code.co_filename == "<general-ai>" and event in ("call", "line", "return") and len(__general_ai_trace) < 120:
        variables = __general_ai_variables(frame.f_locals)
        frame_key = id(frame)
        previous = __general_ai_previous.get(frame_key, {})
        changed = {name: value for name, value in variables.items() if previous.get(name) != value}
        item = {
            "line": frame.f_lineno,
            "event": event,
            "function": frame.f_code.co_name,
            "variables": variables,
            "changedVariables": changed,
        }
        if event == "return":
            item["returnValue"] = __general_ai_repr(arg)
            __general_ai_previous.pop(frame_key, None)
        else:
            __general_ai_previous[frame_key] = variables
        __general_ai_trace.append(item)
    return __general_ai_tracer
try:
    __general_ai_tree = ast.parse(__general_ai_source, mode="exec")
    if __general_ai_tree.body and isinstance(__general_ai_tree.body[-1], ast.Expr):
        __general_ai_tree.body[-1] = ast.Assign(
            targets=[ast.Name(id="__general_ai_result", ctx=ast.Store())],
            value=__general_ai_tree.body[-1].value,
        )
        ast.fix_missing_locations(__general_ai_tree)
    with contextlib.redirect_stdout(__general_ai_stdout):
        __general_ai_namespace = {"__builtins__": __builtins__}
        sys.settrace(__general_ai_tracer)
        try:
            exec(compile(__general_ai_tree, "<general-ai>", "exec"), __general_ai_namespace, __general_ai_namespace)
        finally:
            sys.settrace(None)
    __general_ai_result = __general_ai_namespace.get("__general_ai_result")
    __general_ai_payload = {
        "ok": True,
        "stdout": __general_ai_stdout.getvalue(),
        "resultRepr": repr(__general_ai_result) if __general_ai_result is not None else "",
        "resultType": type(__general_ai_result).__name__ if __general_ai_result is not None else "NoneType",
        "errorType": "",
        "errorMessage": "",
        "errorLine": 0,
        "variables": __general_ai_variables(__general_ai_namespace),
        "executionTrace": __general_ai_trace,
    }
except Exception as __general_ai_error:
    sys.settrace(None)
    __general_ai_tb = traceback.extract_tb(__general_ai_error.__traceback__)
    __general_ai_line = next((frame.lineno for frame in reversed(__general_ai_tb) if frame.filename == "<general-ai>"), 0)
    __general_ai_payload = {
        "ok": False,
        "stdout": __general_ai_stdout.getvalue(),
        "resultRepr": "",
        "resultType": "",
        "errorType": type(__general_ai_error).__name__,
        "errorMessage": str(__general_ai_error),
        "errorLine": __general_ai_line,
        "variables": __general_ai_variables(locals().get("__general_ai_namespace", {})),
        "executionTrace": __general_ai_trace,
    }
json.dumps(__general_ai_payload)
`;

export const formatGeneralAiRuntimeEvidence = (result: GeneralAiRuntimeResult, language: GeneralAiRuntimeLanguage): string => {
  const fr = language === 'fr';
  const lineVisits = new Map<number, number>();
  const traceLines = result.executionTrace?.filter(step => !(step.function === '<module>' && step.event && step.event !== 'line')).slice(-24).map((step, index) => {
    const visits = (lineVisits.get(step.line) || 0) + 1;
    lineVisits.set(step.line, visits);
    const eventLabel = step.event === 'call' ? (fr ? 'appel' : 'call') : step.event === 'return' ? (fr ? 'retour' : 'return') : (fr ? 'ligne' : 'line');
    const functionLabel = step.function && step.function !== '<module>' ? ` \`${step.function}()\`` : '';
    const loopLabel = visits > 1 && step.event !== 'call' ? ` (${fr ? 'passage' : 'visit'} ${visits})` : '';
    const changes = step.changedVariables && Object.keys(step.changedVariables).length
      ? Object.entries(step.changedVariables).map(([name, value]) => `\`${name}=${value}\``).join(', ')
      : '';
    const returned = step.event === 'return' && step.returnValue !== undefined ? ` ${fr ? 'valeur' : 'value'}=\`${step.returnValue}\`` : '';
    const location = step.event === 'line'
      ? `${fr ? 'ligne' : 'line'} ${step.line}${functionLabel ? ` ${fr ? 'dans' : 'in'} ${functionLabel}` : ''}`
      : `${eventLabel}${functionLabel} — ${fr ? 'ligne' : 'line'} ${step.line}`;
    return `${index + 1}. ${location}${loopLabel}${changes ? ` — ${fr ? 'modifié' : 'changed'}: ${changes}` : ''}${returned}`;
  }) || [];
  if (!result.ok) {
    return [
      fr ? '**Preuve d’exécution locale**' : '**Local runtime evidence**',
      `${fr ? 'Le code déclenche' : 'The code raises'} \`${result.errorType}\`${result.errorMessage ? `: ${result.errorMessage}` : ''}${result.errorLine ? ` ${fr ? 'à la ligne' : 'on line'} ${result.errorLine}` : ''}.`,
      result.variables && Object.keys(result.variables).length ? `**${fr ? 'Variables au moment de l’erreur' : 'Variables at failure'}**\n${Object.entries(result.variables).map(([name, value]) => `- \`${name}\` = \`${value}\``).join('\n')}` : '',
      traceLines.length ? `**${fr ? 'Trace avant l’erreur' : 'Trace before failure'}**\n${traceLines.join('\n')}` : '',
      result.stdout ? `${fr ? 'Sortie avant l’erreur' : 'Output before the error'}:\n\`\`\`text\n${result.stdout.trim()}\n\`\`\`` : '',
    ].filter(Boolean).join('\n\n');
  }
  return [
    fr ? '**Preuve d’exécution locale**' : '**Local runtime evidence**',
    result.stdout ? `${fr ? 'Sortie réelle' : 'Actual output'}:\n\`\`\`text\n${result.stdout.trim()}\n\`\`\`` : (fr ? 'Le code ne produit aucune sortie avec `print()`.' : 'The code produces no `print()` output.'),
    result.resultRepr ? `${fr ? 'Valeur de la dernière expression' : 'Final expression value'}: \`${result.resultRepr}\` (\`${result.resultType}\`)` : '',
    result.variables && Object.keys(result.variables).length ? `**${fr ? 'État final des variables' : 'Final variable state'}**\n${Object.entries(result.variables).map(([name, value]) => `- \`${name}\` = \`${value}\``).join('\n')}` : '',
    traceLines.length ? `**${fr ? 'Débogage pas à pas vérifié' : 'Verified step-by-step debugging'}**\n${traceLines.join('\n')}` : '',
  ].filter(Boolean).join('\n\n');
};
