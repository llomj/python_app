export type GeneralAiTracebackLanguage = 'en' | 'fr';

interface TracebackFrame {
  file: string;
  line: number;
  functionName: string;
  source?: string;
}

export interface ParsedPythonTraceback {
  frames: TracebackFrame[];
  errorType: string;
  errorMessage: string;
  failingFrame: TracebackFrame | null;
  caretDetail: string;
}

const ERROR_LINE = /^([A-Za-z_][A-Za-z0-9_.]*(?:Error|Exception|Warning))(?::\s*(.*))?$/;

export const parsePythonTraceback = (text: string): ParsedPythonTraceback | null => {
  if (!/Traceback \(most recent call last\)|(^|\n)\s*File ".+", line \d+/i.test(text)) return null;
  const lines = text.split('\n');
  const frames: TracebackFrame[] = [];
  for (let index = 0; index < lines.length; index += 1) {
    const match = lines[index].match(/^\s*File "([^"]+)", line (\d+)(?:, in (.+))?\s*$/);
    if (!match) continue;
    const possibleSource = lines[index + 1]?.trim();
    frames.push({
      file: match[1],
      line: Number(match[2]),
      functionName: match[3]?.trim() || '<module>',
      source: possibleSource && !/^File |^[~^]+$/.test(possibleSource) ? possibleSource : undefined,
    });
  }
  let errorType = 'PythonError';
  let errorMessage = '';
  for (let index = lines.length - 1; index >= 0; index -= 1) {
    const match = lines[index].trim().match(ERROR_LINE);
    if (match) {
      errorType = match[1];
      errorMessage = match[2]?.trim() || '';
      break;
    }
  }
  const caretDetail = lines.find(line => /^\s*[~^]+\s*$/.test(line))?.trim() || '';
  return { frames, errorType, errorMessage, failingFrame: frames.at(-1) || null, caretDetail };
};

const likelyCause = (parsed: ParsedPythonTraceback, language: GeneralAiTracebackLanguage): string => {
  const detail = parsed.errorMessage;
  const causes: Record<string, [string, string]> = {
    SyntaxError: ['Python could not parse the statement. Check the marked token, missing punctuation, brackets, quotes, and assignment syntax.', 'Python ne peut pas analyser cette instruction. Vérifiez le jeton indiqué, la ponctuation, les crochets, les guillemets et la syntaxe d’affectation.'],
    IndentationError: ['A block has the wrong indentation. Use four spaces per level and do not mix tabs with spaces.', 'Un bloc possède une indentation incorrecte. Utilisez quatre espaces par niveau et ne mélangez pas tabulations et espaces.'],
    NameError: [`A name was used before it was defined or its spelling differs.${detail ? ` Python reported: ${detail}` : ''}`, `Un nom a été utilisé avant sa définition ou son orthographe diffère.${detail ? ` Python indique : ${detail}` : ''}`],
    TypeError: [`An operation received incompatible value types or an incorrect call signature.${detail ? ` Python reported: ${detail}` : ''}`, `Une opération a reçu des types incompatibles ou une signature d’appel incorrecte.${detail ? ` Python indique : ${detail}` : ''}`],
    KeyError: ['A dictionary lookup requested a key that is not present. Inspect the available keys or use `dict.get()` when absence is expected.', 'Une recherche dans un dictionnaire demande une clé absente. Vérifiez les clés disponibles ou utilisez `dict.get()` lorsque l’absence est normale.'],
    IndexError: ['A sequence index is outside its valid range. Compare the index with `len(sequence)` and remember that indexing starts at zero.', 'Un index se trouve hors des limites de la séquence. Comparez-le à `len(sequence)` et souvenez-vous que les index commencent à zéro.'],
    AttributeError: ['The object does not provide the requested attribute or method. Verify the object type and method spelling.', 'L’objet ne possède pas l’attribut ou la méthode demandé. Vérifiez son type et l’orthographe de la méthode.'],
    ValueError: ['The value has the right general type but an unacceptable content or range.', 'La valeur possède le bon type général, mais son contenu ou sa plage est invalide.'],
  };
  return (causes[parsed.errorType] || [
    'The final exception line identifies the failure. Inspect the last application frame and the values used there.',
    'La dernière ligne d’exception identifie l’échec. Vérifiez le dernier cadre de votre programme et les valeurs utilisées.',
  ])[language === 'fr' ? 1 : 0];
};

export const answerPythonTraceback = (text: string, language: GeneralAiTracebackLanguage): string | null => {
  const parsed = parsePythonTraceback(text);
  if (!parsed) return null;
  const fr = language === 'fr';
  const frames = parsed.frames.map((frame, index) => (
    `${index + 1}. \`${frame.file}:${frame.line}\` — \`${frame.functionName}\`${frame.source ? `\n   \`${frame.source}\`` : ''}`
  )).join('\n') || (fr ? 'Aucun cadre de fichier détecté.' : 'No file frames were detected.');
  const failing = parsed.failingFrame
    ? `\`${parsed.failingFrame.file}:${parsed.failingFrame.line}\` (${parsed.failingFrame.functionName})`
    : (fr ? 'ligne non détectée' : 'line not detected');
  return [
    fr ? '**1. Erreur exacte**' : '**1. Exact error**',
    `\`${parsed.errorType}\`${parsed.errorMessage ? `: ${parsed.errorMessage}` : ''}`,
    '',
    fr ? '**2. Pile d’appels**' : '**2. Call stack**',
    frames,
    '',
    fr ? '**3. Point d’échec**' : '**3. Failure point**',
    `${failing}${parsed.caretDetail ? `\n${fr ? 'Marqueur' : 'Marker'}: \`${parsed.caretDetail}\`` : ''}`,
    '',
    fr ? '**4. Cause probable**' : '**4. Likely cause**',
    likelyCause(parsed, language),
    '',
    fr ? '**5. Vérification suivante**' : '**5. Next check**',
    fr
      ? 'Vérifiez les valeurs et les types sur la ligne d’échec, corrigez cette première erreur, puis relancez le code car les erreurs suivantes peuvent en découler.'
      : 'Inspect the values and types on the failing line, fix this first error, then run again because later errors may be consequences of it.',
  ].join('\n');
};
