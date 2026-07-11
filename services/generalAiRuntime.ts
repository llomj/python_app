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
  executionTrace?: Array<{ line: number; variables: Record<string, string> }>;
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
  'abs', 'all', 'any', 'bool', 'dict', 'enumerate', 'float', 'int', 'len', 'list',
  'max', 'min', 'print', 'range', 'repr', 'reversed', 'round', 'set', 'sorted',
  'str', 'sum', 'tuple', 'type', 'zip', 'append', 'capitalize', 'clear', 'copy',
  'count', 'endswith', 'extend', 'find', 'get', 'index', 'insert', 'items', 'join',
  'keys', 'lower', 'pop', 'remove', 'replace', 'reverse', 'sort', 'split', 'startswith',
  'strip', 'update', 'upper', 'values',
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

export const buildGeneralAiRuntimeScript = (code: string): string => `
import ast, contextlib, io, json, traceback, sys, types
__general_ai_source = ${JSON.stringify(code)}
__general_ai_stdout = io.StringIO()
__general_ai_result = None
__general_ai_payload = {}
__general_ai_trace = []
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
    if frame.f_code.co_filename == "<general-ai>" and event == "line" and len(__general_ai_trace) < 80:
        __general_ai_trace.append({"line": frame.f_lineno, "variables": __general_ai_variables(frame.f_locals)})
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
  if (!result.ok) {
    return [
      fr ? '**Preuve d’exécution locale**' : '**Local runtime evidence**',
      `${fr ? 'Le code déclenche' : 'The code raises'} \`${result.errorType}\`${result.errorMessage ? `: ${result.errorMessage}` : ''}${result.errorLine ? ` ${fr ? 'à la ligne' : 'on line'} ${result.errorLine}` : ''}.`,
      result.variables && Object.keys(result.variables).length ? `**${fr ? 'Variables au moment de l’erreur' : 'Variables at failure'}**\n${Object.entries(result.variables).map(([name, value]) => `- \`${name}\` = \`${value}\``).join('\n')}` : '',
      result.stdout ? `${fr ? 'Sortie avant l’erreur' : 'Output before the error'}:\n\`\`\`text\n${result.stdout.trim()}\n\`\`\`` : '',
    ].filter(Boolean).join('\n\n');
  }
  return [
    fr ? '**Preuve d’exécution locale**' : '**Local runtime evidence**',
    result.stdout ? `${fr ? 'Sortie réelle' : 'Actual output'}:\n\`\`\`text\n${result.stdout.trim()}\n\`\`\`` : (fr ? 'Le code ne produit aucune sortie avec `print()`.' : 'The code produces no `print()` output.'),
    result.resultRepr ? `${fr ? 'Valeur de la dernière expression' : 'Final expression value'}: \`${result.resultRepr}\` (\`${result.resultType}\`)` : '',
    result.variables && Object.keys(result.variables).length ? `**${fr ? 'État final des variables' : 'Final variable state'}**\n${Object.entries(result.variables).map(([name, value]) => `- \`${name}\` = \`${value}\``).join('\n')}` : '',
    result.executionTrace?.length ? `**${fr ? 'Ordre d’exécution vérifié' : 'Verified execution order'}**\n${result.executionTrace.slice(-12).map((step, index) => `${index + 1}. ${fr ? 'ligne' : 'line'} ${step.line}${Object.keys(step.variables).length ? ` — ${Object.entries(step.variables).map(([name, value]) => `\`${name}=${value}\``).join(', ')}` : ''}`).join('\n')}` : '',
  ].filter(Boolean).join('\n\n');
};
