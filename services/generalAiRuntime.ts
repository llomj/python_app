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
  if (code.length > 1200 || code.split('\n').length > 30) return { safe: false, reason: 'The snippet is too large for automatic execution.', code };
  if (/\b(?:import|from|input|open|exec|eval|compile|globals|locals|breakpoint|help|memoryview)\b|__/i.test(code)) {
    return { safe: false, reason: 'The snippet uses imports, I/O, dynamic execution, introspection, or dunder access.', code };
  }
  if (/^\s*(?:for|while|def|class|async|with|try)\b/m.test(code)) {
    return { safe: false, reason: 'Automatic runtime evidence is limited to straight-line snippets without loops, functions, classes, or context managers.', code };
  }
  if (/\b\d{8,}\b|\*\s*\d{6,}|range\s*\([^)]*\d{7,}/.test(code)) {
    return { safe: false, reason: 'The snippet may allocate or compute too much data.', code };
  }
  const calls = [...code.matchAll(/\b([A-Za-z_]\w*)\s*\(/g)].map(match => match[1]);
  const unknownCall = calls.find(name => !SAFE_CALLS.has(name));
  if (unknownCall) return { safe: false, reason: `Call to ${unknownCall}() is outside the safe runtime allowlist.`, code };
  return { safe: true, reason: 'Straight-line snippet uses only safe built-ins and expressions.', code };
};

export const buildGeneralAiRuntimeScript = (code: string): string => `
import ast, contextlib, io, json, traceback
__general_ai_source = ${JSON.stringify(code)}
__general_ai_stdout = io.StringIO()
__general_ai_result = None
__general_ai_payload = {}
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
        exec(compile(__general_ai_tree, "<general-ai>", "exec"), __general_ai_namespace, __general_ai_namespace)
    __general_ai_result = __general_ai_namespace.get("__general_ai_result")
    __general_ai_payload = {
        "ok": True,
        "stdout": __general_ai_stdout.getvalue(),
        "resultRepr": repr(__general_ai_result) if __general_ai_result is not None else "",
        "resultType": type(__general_ai_result).__name__ if __general_ai_result is not None else "NoneType",
        "errorType": "",
        "errorMessage": "",
    }
except Exception as __general_ai_error:
    __general_ai_payload = {
        "ok": False,
        "stdout": __general_ai_stdout.getvalue(),
        "resultRepr": "",
        "resultType": "",
        "errorType": type(__general_ai_error).__name__,
        "errorMessage": str(__general_ai_error),
    }
json.dumps(__general_ai_payload)
`;

export const formatGeneralAiRuntimeEvidence = (result: GeneralAiRuntimeResult, language: GeneralAiRuntimeLanguage): string => {
  const fr = language === 'fr';
  if (!result.ok) {
    return [
      fr ? '**Preuve d’exécution locale**' : '**Local runtime evidence**',
      `${fr ? 'Le code déclenche' : 'The code raises'} \`${result.errorType}\`${result.errorMessage ? `: ${result.errorMessage}` : ''}.`,
      result.stdout ? `${fr ? 'Sortie avant l’erreur' : 'Output before the error'}:\n\`\`\`text\n${result.stdout.trim()}\n\`\`\`` : '',
    ].filter(Boolean).join('\n\n');
  }
  return [
    fr ? '**Preuve d’exécution locale**' : '**Local runtime evidence**',
    result.stdout ? `${fr ? 'Sortie réelle' : 'Actual output'}:\n\`\`\`text\n${result.stdout.trim()}\n\`\`\`` : (fr ? 'Le code ne produit aucune sortie avec `print()`.' : 'The code produces no `print()` output.'),
    result.resultRepr ? `${fr ? 'Valeur de la dernière expression' : 'Final expression value'}: \`${result.resultRepr}\` (\`${result.resultType}\`)` : '',
  ].filter(Boolean).join('\n\n');
};
