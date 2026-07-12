import type { AutoGrader } from '../graders';
import type { Exercise } from '../types';

type ProblemAiLanguage = 'en' | 'fr';

export interface ProblemAiTutorContext {
  exercise: Exercise;
  description: string;
  grader?: AutoGrader | null;
  language: ProblemAiLanguage;
  question?: string;
}

interface ConceptGuide {
  name: string;
  syntax: string;
  en: string;
  fr: string;
}

const CONCEPTS: Record<string, ConceptGuide> = {
  lambda: { name: 'lambda', syntax: 'lambda parameters: expression', en: 'A lambda is a small anonymous function containing one expression. Its expression runs when the lambda is called.', fr: 'Une lambda est une petite fonction anonyme contenant une seule expression. Son expression s’exécute lorsque la lambda est appelée.' },
  unpacking: { name: 'unpacking', syntax: 'function(*values)', en: 'Unpacking with `*` takes items from an iterable and supplies them as separate positional arguments.', fr: 'Le déballage avec `*` prend les éléments d’un itérable et les transmet comme arguments positionnels séparés.' },
  function: { name: 'function', syntax: 'def name(parameters):', en: 'A function is reusable code that receives arguments and can return a result.', fr: 'Une fonction est un bloc réutilisable qui reçoit des arguments et peut renvoyer un résultat.' },
  return: { name: 'return', syntax: 'return expression', en: '`return` sends a value from a function back to its caller; it does not display the value.', fr: '`return` renvoie une valeur de la fonction vers l’appelant ; il ne l’affiche pas.' },
  print: { name: 'print', syntax: 'print(value)', en: '`print()` displays a value in the output panel. It does not replace a required return value.', fr: '`print()` affiche une valeur dans la sortie. Il ne remplace pas une valeur de retour demandée.' },
  string: { name: 'string', syntax: 'text = "characters"', en: 'A string (`str`) is an immutable sequence of Unicode characters. String methods must be called on a string value.', fr: 'Une chaîne (`str`) est une séquence immuable de caractères Unicode. Les méthodes de chaîne doivent être appelées sur une chaîne.' },
  list: { name: 'list', syntax: '[item1, item2]', en: 'A list is an ordered, mutable collection addressed with zero-based indexes.', fr: 'Une liste est une collection ordonnée et modifiable dont les indices commencent à zéro.' },
  tuple: { name: 'tuple', syntax: '(item1, item2)', en: 'A tuple is an ordered, immutable collection that can be packed and unpacked.', fr: 'Un tuple est une collection ordonnée et immuable qui peut être regroupée et déballée.' },
  dictionary: { name: 'dictionary', syntax: '{key: value}', en: 'A dictionary maps unique hashable keys to values.', fr: 'Un dictionnaire associe des clés uniques et hachables à des valeurs.' },
  set: { name: 'set', syntax: '{item1, item2}', en: 'A set stores unique hashable values without positional indexes.', fr: 'Un ensemble stocke des valeurs hachables uniques sans indices positionnels.' },
  slicing: { name: 'slicing', syntax: 'sequence[start:stop:step]', en: 'Slicing selects part of a sequence. The stop position is excluded.', fr: 'Le découpage sélectionne une partie d’une séquence. La position de fin est exclue.' },
  subscript: { name: 'indexing', syntax: 'sequence[index]', en: 'Indexing reads one item by position, starting at index `0`.', fr: 'L’indexation lit un élément par sa position, en commençant à l’indice `0`.' },
  comprehension: { name: 'comprehension', syntax: '[expression for item in iterable if condition]', en: 'A comprehension builds a collection by transforming and optionally filtering iterable items.', fr: 'Une compréhension construit une collection en transformant et, éventuellement, en filtrant les éléments d’un itérable.' },
  generator: { name: 'generator expression', syntax: '(expression for item in iterable)', en: 'A generator expression produces values lazily, one at a time.', fr: 'Une expression génératrice produit les valeurs paresseusement, une par une.' },
  loop: { name: 'loop', syntax: 'for item in iterable:', en: 'A loop repeats its indented block for values from an iterable or while a condition remains true.', fr: 'Une boucle répète son bloc indenté pour les valeurs d’un itérable ou tant qu’une condition reste vraie.' },
  conditional: { name: 'condition', syntax: 'if condition:', en: 'A condition chooses which indented branch runs according to a Boolean expression.', fr: 'Une condition choisit le bloc indenté à exécuter selon une expression booléenne.' },
  class: { name: 'class', syntax: 'class Name:', en: 'A class defines the data and behavior shared by its instances.', fr: 'Une classe définit les données et le comportement partagés par ses instances.' },
  exception: { name: 'exception handling', syntax: 'try: ... except Error:', en: 'Exception handling runs recovery code only when a matching runtime error occurs.', fr: 'La gestion des exceptions exécute le code de récupération uniquement lorsqu’une erreur correspondante survient.' },
  context: { name: 'context manager', syntax: 'with resource as value:', en: 'A context manager guarantees setup and cleanup around an indented block.', fr: 'Un gestionnaire de contexte garantit la préparation et le nettoyage autour d’un bloc indenté.' },
  boolean: { name: 'Boolean expression', syntax: 'left and right', en: 'A Boolean expression evaluates to `True` or `False` and may combine comparisons with `and`, `or`, or `not`.', fr: 'Une expression booléenne produit `True` ou `False` et peut combiner des comparaisons avec `and`, `or` ou `not`.' },
};

const NODE_CONCEPT: Record<string, string> = {
  Assert: 'boolean', Attribute: 'function', BinOp: 'function', BoolOp: 'boolean', Call: 'function',
  ClassDef: 'class', Compare: 'conditional', Delete: 'dictionary', Dict: 'dictionary', DictComp: 'comprehension',
  For: 'loop', FunctionDef: 'function', GeneratorExp: 'generator', Global: 'function', Lambda: 'lambda',
  ListComp: 'comprehension', Nonlocal: 'function', Raise: 'exception', Set: 'set', SetComp: 'comprehension',
  Starred: 'unpacking', Subscript: 'subscript', Try: 'exception', Tuple: 'tuple', While: 'loop', With: 'context',
};

const NODE_REQUIREMENT: Record<string, [string, string]> = {
  Assert: ['Include an `assert` statement that checks a condition.', 'Incluez une instruction `assert` qui vérifie une condition.'],
  Attribute: ['Access or call an attribute with dot syntax.', 'Accédez à un attribut ou appelez-le avec la notation pointée.'],
  BinOp: ['Use the required arithmetic or binary operation.', 'Utilisez l’opération arithmétique ou binaire demandée.'],
  BoolOp: ['Combine conditions with a Boolean operator.', 'Combinez les conditions avec un opérateur booléen.'],
  Call: ['Call the required function or method.', 'Appelez la fonction ou méthode demandée.'],
  ClassDef: ['Define the required class with `class`.', 'Définissez la classe demandée avec `class`.'],
  Compare: ['Use a comparison that produces a Boolean result.', 'Utilisez une comparaison qui produit un résultat booléen.'],
  Delete: ['Delete the requested item with `del`.', 'Supprimez l’élément demandé avec `del`.'],
  Dict: ['Create or use a dictionary literal.', 'Créez ou utilisez un dictionnaire littéral.'],
  DictComp: ['Build the dictionary with a dictionary comprehension.', 'Construisez le dictionnaire avec une compréhension de dictionnaire.'],
  For: ['Use a `for` loop and indent its repeated body.', 'Utilisez une boucle `for` et indentez son bloc répété.'],
  FunctionDef: ['Define a named function with `def`.', 'Définissez une fonction nommée avec `def`.'],
  GeneratorExp: ['Use a generator expression inside parentheses.', 'Utilisez une expression génératrice entre parenthèses.'],
  Global: ['Declare the module-level name with `global` before assigning it.', 'Déclarez le nom de niveau module avec `global` avant de l’affecter.'],
  Lambda: ['Create an anonymous function with `lambda parameters: expression`.', 'Créez une fonction anonyme avec `lambda paramètres: expression`.'],
  ListComp: ['Build the list with a list comprehension.', 'Construisez la liste avec une compréhension de liste.'],
  Nonlocal: ['Use `nonlocal` to update a name from the enclosing function.', 'Utilisez `nonlocal` pour modifier un nom de la fonction englobante.'],
  Raise: ['Raise the requested exception explicitly.', 'Levez explicitement l’exception demandée.'],
  Set: ['Create or use a set literal.', 'Créez ou utilisez un ensemble littéral.'],
  SetComp: ['Build the set with a set comprehension.', 'Construisez l’ensemble avec une compréhension d’ensemble.'],
  Starred: ['Use starred unpacking (`*values`) so iterable items become separate values or arguments.', 'Utilisez le déballage étoilé (`*valeurs`) pour transformer les éléments d’un itérable en valeurs ou arguments séparés.'],
  Subscript: ['Access the required item with indexing or slicing.', 'Accédez à l’élément demandé par indexation ou découpage.'],
  Try: ['Use a `try`/`except` block for the requested runtime error.', 'Utilisez un bloc `try`/`except` pour l’erreur demandée.'],
  Tuple: ['Create, return, or unpack a tuple.', 'Créez, renvoyez ou déballez un tuple.'],
  While: ['Use a `while` loop whose condition eventually becomes false.', 'Utilisez une boucle `while` dont la condition finit par devenir fausse.'],
  With: ['Use a `with` block so the resource is cleaned up automatically.', 'Utilisez un bloc `with` pour que la ressource soit automatiquement nettoyée.'],
};

const OPERATOR_SYNTAX: Record<string, string> = {
  Add: '+', Sub: '-', Mult: '*', Div: '/', FloorDiv: '//', Mod: '%', Pow: '**',
  Eq: '==', NotEq: '!=', Lt: '<', LtE: '<=', Gt: '>', GtE: '>=', And: 'and', Or: 'or',
};

const CALL_REFERENCE: Record<string, [string, string, string]> = {
  all: ['all(iterable)', 'Returns `True` only when every item is truthy.', 'Renvoie `True` uniquement lorsque tous les éléments sont vrais.'],
  any: ['any(iterable)', 'Returns `True` when at least one item is truthy.', 'Renvoie `True` lorsqu’au moins un élément est vrai.'],
  append: ['list.append(value)', 'Adds one value to the end of a list and returns `None`.', 'Ajoute une valeur à la fin d’une liste et renvoie `None`.'],
  count: ['sequence.count(value)', 'Counts matching values in a sequence.', 'Compte les valeurs correspondantes dans une séquence.'],
  dict: ['dict(iterable_or_mapping)', 'Creates a dictionary from key-value data.', 'Crée un dictionnaire à partir de données clé-valeur.'],
  enumerate: ['enumerate(iterable, start=0)', 'Produces `(index, value)` pairs.', 'Produit des paires `(indice, valeur)`.'],
  filter: ['filter(function, iterable)', 'Keeps items for which the function returns a truthy value.', 'Conserve les éléments pour lesquels la fonction renvoie une valeur vraie.'],
  findall: ['re.findall(pattern, text)', 'Returns every non-overlapping regex match.', 'Renvoie toutes les correspondances non chevauchantes d’une expression régulière.'],
  float: ['float(value)', 'Converts a compatible value to a floating-point number.', 'Convertit une valeur compatible en nombre décimal.'],
  fullmatch: ['re.fullmatch(pattern, text)', 'Matches only when the complete string satisfies the regex.', 'Correspond uniquement lorsque toute la chaîne respecte l’expression régulière.'],
  get: ['mapping.get(key, default=None)', 'Reads a mapping value without raising `KeyError` for a missing key.', 'Lit une valeur sans lever `KeyError` lorsque la clé est absente.'],
  input: ['input(prompt="")', 'Reads user input and returns it as a string.', 'Lit la saisie utilisateur et la renvoie sous forme de chaîne.'],
  int: ['int(value)', 'Converts a compatible value to an integer.', 'Convertit une valeur compatible en entier.'],
  isalnum: ['text.isalnum()', 'String method. Returns `True` when the non-empty string contains only letters and digits.', 'Méthode de chaîne. Renvoie `True` lorsque la chaîne non vide contient uniquement des lettres et des chiffres.'],
  isalpha: ['text.isalpha()', 'String method. Returns `True` when the non-empty string contains only letters. Spaces, signs, and digits make it `False`.', 'Méthode de chaîne. Renvoie `True` lorsque la chaîne non vide contient uniquement des lettres. Les espaces, signes et chiffres donnent `False`.'],
  isdigit: ['text.isdigit()', 'String method. Returns `True` when the non-empty string contains only digit characters. A minus sign or decimal point makes it `False`.', 'Méthode de chaîne. Renvoie `True` lorsque la chaîne non vide contient uniquement des chiffres. Un signe moins ou un point décimal donne `False`.'],
  islower: ['text.islower()', 'String method. Checks whether all cased characters are lowercase.', 'Méthode de chaîne. Vérifie si tous les caractères alphabétiques sont en minuscules.'],
  isinstance: ['isinstance(object, type)', 'Checks whether an object has the specified type.', 'Vérifie si un objet possède le type indiqué.'],
  isupper: ['text.isupper()', 'String method. Checks whether all cased characters are uppercase.', 'Méthode de chaîne. Vérifie si tous les caractères alphabétiques sont en majuscules.'],
  items: ['mapping.items()', 'Provides `(key, value)` pairs from a mapping.', 'Fournit les paires `(clé, valeur)` d’un dictionnaire.'],
  join: ['separator.join(strings)', 'Combines strings with the separator between them.', 'Combine des chaînes en plaçant le séparateur entre elles.'],
  keys: ['mapping.keys()', 'Provides the keys from a mapping.', 'Fournit les clés d’un dictionnaire.'],
  len: ['len(collection)', 'Returns the number of items in a collection.', 'Renvoie le nombre d’éléments d’une collection.'],
  list: ['list(iterable)', 'Creates a mutable list from an iterable.', 'Crée une liste modifiable à partir d’un itérable.'],
  lower: ['text.lower()', 'Returns a lowercase copy of a string.', 'Renvoie une copie de la chaîne en minuscules.'],
  map: ['map(function, iterable)', 'Applies a function to each iterable item lazily.', 'Applique paresseusement une fonction à chaque élément d’un itérable.'],
  match: ['re.match(pattern, text)', 'Checks for a regex match at the beginning of a string.', 'Recherche une correspondance regex au début d’une chaîne.'],
  max: ['max(iterable)', 'Returns the largest item.', 'Renvoie le plus grand élément.'],
  min: ['min(iterable)', 'Returns the smallest item.', 'Renvoie le plus petit élément.'],
  next: ['next(iterator, default)', 'Reads the next iterator item or returns the optional default.', 'Lit l’élément suivant d’un itérateur ou renvoie la valeur par défaut facultative.'],
  open: ['open(path, mode="r")', 'Opens a file and returns a file object.', 'Ouvre un fichier et renvoie un objet fichier.'],
  pop: ['collection.pop(key_or_index)', 'Removes and returns one item.', 'Supprime et renvoie un élément.'],
  print: ['print(*values, sep=" ", end="\\n")', 'Displays values in the output panel and returns `None`.', 'Affiche des valeurs dans le panneau de sortie et renvoie `None`.'],
  range: ['range(start, stop, step)', 'Creates an integer sequence whose stop value is excluded.', 'Crée une séquence d’entiers dont la borne de fin est exclue.'],
  reduce: ['reduce(function, iterable)', 'Combines iterable items into one accumulated value.', 'Combine les éléments d’un itérable en une seule valeur accumulée.'],
  replace: ['text.replace(old, new)', 'Returns a copy with matching text replaced.', 'Renvoie une copie dans laquelle le texte correspondant est remplacé.'],
  search: ['re.search(pattern, text)', 'Finds the first regex match anywhere in a string.', 'Trouve la première correspondance regex dans une chaîne.'],
  set: ['set(iterable)', 'Creates a collection of unique hashable values.', 'Crée une collection de valeurs hachables uniques.'],
  setdefault: ['mapping.setdefault(key, default)', 'Returns a key’s value, inserting the default when the key is absent.', 'Renvoie la valeur d’une clé et insère la valeur par défaut si la clé est absente.'],
  sorted: ['sorted(iterable, key=None, reverse=False)', 'Returns a new sorted list without mutating the input.', 'Renvoie une nouvelle liste triée sans modifier l’entrée.'],
  split: ['text.split(separator=None)', 'Breaks a string into a list of parts.', 'Découpe une chaîne en une liste de parties.'],
  startswith: ['text.startswith(prefix)', 'String method. Checks whether text begins with the specified prefix.', 'Méthode de chaîne. Vérifie si le texte commence par le préfixe indiqué.'],
  str: ['str(value)', 'Converts a value to its string representation.', 'Convertit une valeur en représentation textuelle.'],
  strip: ['text.strip()', 'Returns a copy without leading or trailing whitespace.', 'Renvoie une copie sans espaces au début ni à la fin.'],
  sub: ['re.sub(pattern, replacement, text)', 'Replaces regex matches in a string.', 'Remplace les correspondances regex dans une chaîne.'],
  sum: ['sum(iterable, start=0)', 'Adds numeric iterable items and returns the total.', 'Additionne les éléments numériques d’un itérable et renvoie le total.'],
  tuple: ['tuple(iterable)', 'Creates an immutable ordered tuple.', 'Crée un tuple ordonné et immuable.'],
  type: ['type(object)', 'Returns the object’s runtime type.', 'Renvoie le type d’un objet à l’exécution.'],
  update: ['mapping.update(other)', 'Adds or replaces mapping entries in place.', 'Ajoute ou remplace les entrées d’un dictionnaire sur place.'],
  upper: ['text.upper()', 'Returns an uppercase copy of a string.', 'Renvoie une copie de la chaîne en majuscules.'],
  values: ['mapping.values()', 'Provides the values from a mapping.', 'Fournit les valeurs d’un dictionnaire.'],
  zip: ['zip(*iterables)', 'Pairs items from multiple iterables by position.', 'Associe par position les éléments de plusieurs itérables.'],
};

const STRING_METHODS = new Set([
  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
  'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
  'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
  'upper', 'zfill',
]);

const LIST_METHODS = new Set(['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']);

const DICT_METHODS = new Set(['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']);

const cleanPrompt = (description: string): string => {
  const first = description.split('\n').map(line => line.trim()).find(line => line && !/^examples?:/i.test(line)) || description.trim();
  return first.replace(/^(?:write|create|build|define|implement)\s+(?:a\s+)?python\s+(?:program|function|script)(?:\s+called\s+`?[A-Za-z_]\w*`?)?(?:\s+that|\s+which|\s+to)?\s+/i, '')
    .replace(/^(?:write|create|build|define|implement)\s+(?:a\s+)?python\s+(?:program|function|script)\s+to\s+/i, '')
    .replace(/^(?:write|create|build|define|implement)\s+/i, '')
    .replace(/^(?:écrivez|créez|construisez|définissez|implémentez)\s+(?:une?\s+)?(?:fonction|programme|script)\s+python\s+(?:appelée?\s+`?\w+`?\s+)?(?:qui\s+|pour\s+)?/i, '')
    .replace(/^(?:écrivez|créez|construisez|définissez|implémentez)\s+/i, '')
    .replace(/[.\s]+$/, '');
};

interface SolutionPatterns {
  hasLambda: boolean;
  hasUnpacking: boolean;
  hasComprehension: boolean;
  hasGenerator: boolean;
  hasLoop: boolean;
  hasConditional: boolean;
  hasClass: boolean;
  hasTryExcept: boolean;
  hasWith: boolean;
  hasComparison: boolean;
  hasFString: boolean;
}

interface SolutionAnalysis {
  snippet: string;
  calls: string[];
  receiverByMethod: Record<string, string>;
  patterns: SolutionPatterns;
}

type ProblemType = 'function-def' | 'script-output' | 'class-def';

const detectSolutionPatterns = (code: string): SolutionPatterns => {
  const stripped = code.replace(/#.*$/gm, '');
  return {
    hasLambda: /\blambda\s+\w+\s*:/.test(stripped),
    hasUnpacking: /\*\w+/.test(stripped),
    hasComprehension: /[[({]\s*(?:\w+\s*=\s*)?[^\]]*?\bfor\b\s+\w+\s+\bin\b/.test(stripped),
    hasGenerator: /\([^)]*?\bfor\b\s+\w+\s+\bin\b[^)]*?\)/.test(stripped) && !/[[{][^]*?\bfor\b/.test(stripped),
    hasLoop: /\b(?:for|while)\s+\w+\s+(?:in|:)/.test(stripped),
    hasConditional: /\bif\s+.+:\s*$|\belif\b|\belse\s*:/m.test(stripped),
    hasClass: /\bclass\s+\w+/.test(stripped),
    hasTryExcept: /\btry\s*:|\bexcept\b/.test(stripped),
    hasWith: /\bwith\s+\w+\s*(?:=\s*[^:]+)?\s*:/.test(stripped),
    hasComparison: /(?:==|!=|<=|>=|<|>)\s*(?:True|False|None|\d|['"])|(?:True|False|None|\d|['"])\s*(?:==|!=|<=|>=|<|>)/.test(stripped) || /\b(?:and|or|not)\b/.test(stripped),
    hasFString: /f['"]/.test(stripped),
  };
};

const analyzeCanonicalSolution = (exercise: Exercise, grader?: AutoGrader | null): SolutionAnalysis => {
  const lines = exercise.solution.split('\n');
  const startMarker = lines.findIndex(line => /^#\s*Using function approach/i.test(line.trim()));
  const start = startMarker >= 0 ? startMarker + 1 : 0;
  const selected: string[] = [];
  const topLevelDefinitions = new Set<string>();
  for (let index = start; index < lines.length; index += 1) {
    const line = lines[index];
    if (selected.some(item => item.trim()) && /^#\s*(?:Using|Script|Direct)\b/i.test(line.trim())) break;
    const definition = line.match(/^(?:def|class)\s+([A-Za-z_]\w*)/);
    if (definition && topLevelDefinitions.has(definition[1])) break;
    if (definition) topLevelDefinitions.add(definition[1]);
    if (/^#\s*Expected output/i.test(line.trim())) continue;
    selected.push(line.replace(/\s+#\s*(?:Expected.*|Convert .*|If .*|Update .*)$/i, ''));
    if (selected.filter(item => item.trim()).length >= 16) break;
  }
  const snippet = selected.join('\n').trim() || exercise.initialCode.trim();
  const functionNames = new Set(grader?.functionNames || []);
  const receiverByMethod: Record<string, string> = {};
  for (const match of snippet.matchAll(/\b([A-Za-z_]\w*)\.([A-Za-z_]\w*)\s*\(/g)) receiverByMethod[match[2]] = match[1];
  const calls = [...snippet.matchAll(/(?:\.\s*|\b)([A-Za-z_]\w*)\s*\(/g)]
    .map(match => match[1])
    .filter(name => !functionNames.has(name));
  return {
    snippet,
    calls: [...new Set(calls)].slice(0, 10),
    receiverByMethod,
    patterns: detectSolutionPatterns(snippet),
  };
};

const classifyProblemType = (grader: AutoGrader | null | undefined, patterns: SolutionPatterns): ProblemType => {
  if (patterns.hasClass) return 'class-def';
  if (grader?.mode === 'script' || (!grader?.functionNames?.length && !patterns.hasLambda && !patterns.hasClass)) return 'script-output';
  return 'function-def';
};

const receiverContract = (method: string, receiver: string, language: ProblemAiLanguage): string => {
  const fr = language === 'fr';
  if (STRING_METHODS.has(method)) return fr
    ? `Le récepteur \`${receiver}\` doit être une chaîne (\`str\`) car \`${method}()\` est une méthode de chaîne. Appelez-la avec la notation pointée : \`${receiver}.${method}()\`.`
    : `The receiver \`${receiver}\` must be a string (\`str\`) because \`${method}()\` is a string method. Call it with dot syntax: \`${receiver}.${method}()\`.`;
  if (LIST_METHODS.has(method)) return fr
    ? `Le récepteur \`${receiver}\` doit être une liste car \`${method}()\` est une méthode de liste.`
    : `The receiver \`${receiver}\` must be a list because \`${method}()\` is a list method.`;
  if (DICT_METHODS.has(method)) return fr
    ? `Le récepteur \`${receiver}\` doit être un dictionnaire car \`${method}()\` est une méthode de dictionnaire.`
    : `The receiver \`${receiver}\` must be a dictionary because \`${method}()\` is a dictionary method.`;
  return '';
};

const methodReference = (analysis: SolutionAnalysis, language: ProblemAiLanguage): string[] => analysis.calls.map(name => {
  const base = describeCall(name, language);
  const receiver = analysis.receiverByMethod[name];
  const contract = receiver ? receiverContract(name, receiver, language) : '';
  return contract ? `${base}\n  ${contract}` : base;
});

const explainSolutionLines = (analysis: SolutionAnalysis, language: ProblemAiLanguage): string[] => {
  const fr = language === 'fr';
  const p = analysis.patterns;
  return analysis.snippet.split('\n').map(line => line.trim()).filter(line => line && !line.startsWith('#')).slice(0, 12).map(line => {
    if (/lambda\s+\w+\s*:/.test(line)) return fr
      ? `\`${line}\` — crée une fonction anonyme (lambda) ; l'expression après \`:\` est renvoyée automatiquement.`
      : `\`${line}\` — creates an anonymous function (lambda); the expression after \`:\` is returned automatically.`;
    if (/\*\w+/.test(line) && /\(.*\*\w+/.test(line)) return fr
      ? `\`${line}\` — déballe un itérable avec \`*\` pour passer ses éléments comme arguments séparés.`
      : `\`${line}\` — unpacks an iterable with \`*\` to pass its items as separate arguments.`;
    if (/^def\s+/.test(line)) return fr ? `\`${line}\` — crée la fonction ; son corps attend un appel avant de s’exécuter.` : `\`${line}\` — defines the function; its body waits until the function is called.`;
    if (/^class\s+/.test(line)) return fr ? `\`${line}\` — définit la classe ; les méthodes sont des fonctions à l’intérieur de son bloc indenté.` : `\`${line}\` — defines the class; methods are functions inside its indented block.`;
    if (/^return\s+/.test(line)) {
      if (p.hasLambda) return fr
        ? `\`${line}\` — renvoie le résultat de l’appel de la lambda.`
        : `\`${line}\` — returns the result of calling the lambda.`;
      if (/\bor\b/.test(line)) return fr ? `\`${line}\` — évalue la condition gauche, puis la droite seulement si nécessaire, et renvoie le résultat booléen.` : `\`${line}\` — evaluates the left condition, evaluates the right only if needed, and returns the Boolean result.`;
      return fr ? `\`${line}\` — calcule l’expression puis renvoie sa valeur à l’appelant.` : `\`${line}\` — evaluates the expression and returns its value to the caller.`;
    }
    if (/^if\s+/.test(line)) return fr ? `\`${line}\` — évalue la condition et choisit le bloc indenté.` : `\`${line}\` — evaluates the condition and selects an indented branch.`;
    if (/^(?:for|while)\s+/.test(line)) return fr ? `\`${line}\` — démarre la répétition du bloc indenté.` : `\`${line}\` — begins repetition of the indented block.`;
    if (/^(?:import|from)\s+/.test(line)) return fr ? `\`${line}\` — charge le module ou le nom nécessaire.` : `\`${line}\` — loads the required module or name.`;
    if (/\s=\s/.test(line)) {
      if (/lambda\b/.test(line)) return fr
        ? `\`${line}\` — affecte la lambda à une variable pour pouvoir l’utiliser plus tard.`
        : `\`${line}\` — assigns the lambda to a variable for later use.`;
      if (/\*[A-Za-z_]/.test(line)) return fr
        ? `\`${line}\` — déballe l’itérable dans des variables séparées.`
        : `\`${line}\` — unpacks the iterable into separate variables.`;
      if (/f['"]/.test(line)) return fr
        ? `\`${line}\` — chaîne f-string avec expressions intégrées entre {} pour produire la sortie.`
        : `\`${line}\` — f-string with embedded expressions in {} to build the output.`;
      if (/\[.*for\b/.test(line) || /\{.*for\b/.test(line)) return fr
        ? `\`${line}\` — compréhension qui construit la collection par transformation et filtrage.`
        : `\`${line}\` — comprehension that builds the collection by transforming and filtering.`;
      const stringValue = /=\s*['"]/.test(line);
      return fr
        ? `\`${line}\` — crée ou met à jour la variable${stringValue ? ' avec une valeur de type chaîne (`str`)' : ''}.`
        : `\`${line}\` — creates or updates the variable${stringValue ? ' with a string (`str`) value' : ''}.`;
    }
    if (/^print\s*\(/.test(line)) return fr ? `\`${line}\` — affiche la valeur finale dans le panneau de sortie.` : `\`${line}\` — displays the final value in the output panel.`;
    if (/^@\w+/.test(line)) return fr ? `\`${line}\` — décorateur qui modifie le comportement de la définition suivante.` : `\`${line}\` — decorator that modifies the following definition's behavior.`;
    if (/^try\s*:/.test(line)) return fr ? `\`${line}\` — commence un bloc de protection contre les exceptions.` : `\`${line}\` — starts a block that guards against exceptions.`;
    if (/^except\b/.test(line)) return fr ? `\`${line}\` — attrape l’exception et exécute le code de récupération.` : `\`${line}\` — catches the exception and runs recovery code.`;
    if (/^with\s+/.test(line)) return fr ? `\`${line}\` — garantit le nettoyage automatique de la ressource.` : `\`${line}\` — guarantees automatic resource cleanup.`;
    return fr ? `\`${line}\` — exécute cette instruction dans l’ordre indiqué.` : `\`${line}\` — executes this statement in order.`;
  });
};

const concreteTests = (exercise: Exercise, grader: AutoGrader | null | undefined, language: ProblemAiLanguage): string[] => {
  const fr = language === 'fr';
  const functionName = grader?.functionNames?.[0];
  const parameterText = exercise.initialCode.match(/def\s+[A-Za-z_]\w*\s*\(([^)]*)\)/)?.[1];
  const declaredParameters = parameterText === undefined ? undefined : parameterText.split(',').map(value => value.trim()).filter(Boolean).length;
  const cases = [...(grader?.optionalTests || []), ...(grader?.tests || [])]
    .filter(test => test.expected !== null && test.expected !== undefined)
    .slice(0, 4);
  return cases.map(test => {
    const args = test.args.map(value => JSON.stringify(value)).join(', ');
    const call = functionName && (declaredParameters === undefined || test.args.length <= declaredParameters)
      ? `${functionName}(${args})`
      : test.args.length
        ? `${fr ? 'valeur(s) d’entrée' : 'input value(s)'}: ${args}`
        : (functionName ? `${functionName}()` : (fr ? 'entrée du script' : 'script input'));
    return `\`${call}\` → \`${JSON.stringify(test.expected)}\``;
  });
};

const valueType = (value: unknown, language: ProblemAiLanguage): string => {
  const fr = language === 'fr';
  if (Array.isArray(value)) return fr ? 'liste' : 'list';
  if (value === null) return fr ? 'aucune valeur fixe' : 'no fixed value';
  if (typeof value === 'string') return fr ? 'chaîne' : 'string';
  if (typeof value === 'number') return fr ? 'nombre' : 'number';
  if (typeof value === 'boolean') return fr ? 'booléen' : 'Boolean';
  if (typeof value === 'object') return fr ? 'dictionnaire/objet' : 'dictionary/object';
  return fr ? 'valeur' : 'value';
};

const addConcept = (target: string[], key: string) => {
  if (CONCEPTS[key] && !target.includes(key)) target.push(key);
};

const detectConcepts = (description: string, grader?: AutoGrader | null): string[] => {
  const lower = description.toLowerCase();
  const concepts: string[] = [];
  const promptPatterns: Array<[RegExp, string]> = [
    [/\blambda\b/, 'lambda'], [/\bunpack|starred|\*args\b/, 'unpacking'], [/\btuple\b/, 'tuple'],
    [/\bstring\b|\bstr\b|\bchaîne\b|\btexte\b/, 'string'], [/\blist\b|\bliste\b/, 'list'], [/\bdictionar|\bdict\b|\bdictionnaire\b/, 'dictionary'], [/\bset\b|\bensemble\b/, 'set'],
    [/\bslic|\bindex|\bdécoupage|\bindice/, 'slicing'], [/\bcomprehension\b|\bcompréhension\b/, 'comprehension'], [/\bgenerator\b|\bgénérateur/, 'generator'],
    [/\bfor loop|\bwhile loop|\bloop\b|\bboucle\b/, 'loop'], [/\bcondition|\bif\b/, 'conditional'],
    [/\bclass\b|\bclasse\b|\bobject-oriented|\boop\b|\bpoo\b/, 'class'], [/\bexception|\btry\b/, 'exception'],
    [/\breturn\b|\breturns?\b|\brenvoie\b|\bretourne\b/, 'return'], [/\bprint\b|example output|exemple de sortie/, 'print'], [/\bfunction\b|\bfonction\b/, 'function'],
  ];
  for (const [pattern, concept] of promptPatterns) if (pattern.test(lower)) addConcept(concepts, concept);
  for (const requirement of grader?.requiredNodePatterns || []) addConcept(concepts, NODE_CONCEPT[requirement.nodeType]);
  if (grader?.requiredUnpackPatterns?.length) addConcept(concepts, 'unpacking');
  if (grader?.requiredBoolOps?.length) addConcept(concepts, 'boolean');
  return concepts.slice(0, 7);
};

const promptOutputType = (description: string, language: ProblemAiLanguage): string | null => {
  const lower = description.toLowerCase();
  const fr = language === 'fr';
  if (/\b(?:true|false|boolean|booléen|vrai|faux)\b/.test(lower)) return fr ? 'booléen' : 'Boolean';
  if (/\b(?:returns?|renvoie|retourne)\s+(?:(?:a|an|the|new|une?|la|le|nouvelle?)\s+)?(?:list|liste)\b/.test(lower)) return fr ? 'liste' : 'list';
  if (/\b(?:returns?|renvoie|retourne)\s+(?:(?:a|an|the|new|une?|la|le|nouveau)\s+)?(?:dictionary|dict|dictionnaire)\b/.test(lower)) return fr ? 'dictionnaire' : 'dictionary';
  if (/\b(?:returns?|renvoie|retourne)\s+(?:(?:a|an|the|new|une?|la|le|nouveau)\s+)?tuple\b/.test(lower)) return 'tuple';
  if (/\b(?:returns?|renvoie|retourne)\s+(?:(?:a|an|the|new|une?|la|le|nouvel)\s+)?(?:set|ensemble)\b/.test(lower)) return fr ? 'ensemble' : 'set';
  if (/\b(?:returns?|renvoie|retourne)\s+(?:(?:a|an|the|new|une?|la|le|nouvelle?)\s+)?(?:string|str|chaîne|texte)\b/.test(lower)) return fr ? 'chaîne' : 'string';
  if (/\b(?:returns?|renvoie|retourne)\b[^.\n]*\b(?:number|integer|float|count|length|sum|minimum|maximum|average|nombre|entier|compte|longueur|somme|moyenne)\b/.test(lower)
    || /\b(?:add|sum|addition|somme|minimum|maximum)\b/.test(lower)) return fr ? 'nombre' : 'number';
  return null;
};

const describeCall = (name: string, language: ProblemAiLanguage): string => {
  const reference = CALL_REFERENCE[name];
  if (!reference) return language === 'fr' ? `\`${name}()\` — fonction ou méthode requise par cet exercice ; appelez-la avec les arguments décrits.` : `\`${name}()\` — a function or method required by this exercise; call it with the described arguments.`;
  return `\`${reference[0]}\` — ${reference[language === 'fr' ? 2 : 1]}`;
};

const inferContract = (description: string, grader: AutoGrader | null | undefined, language: ProblemAiLanguage): string[] => {
  const fr = language === 'fr';
  const firstTest = grader?.optionalTests?.find(test => test.args.length > 0)
    || grader?.tests?.find(test => test.args.length > 0)
    || grader?.tests?.[0];
  const explicitOutputType = promptOutputType(description, language);
  const names = grader?.functionNames?.filter(Boolean) || [];
  const lines: string[] = [];
  if (grader?.mode === 'script' || !names.length) {
    lines.push(fr ? 'Forme : script exécutable ; aucun nom de fonction précis n’est imposé.' : 'Form: executable script; no specific function name is required.');
  } else {
    lines.push(`${fr ? 'Fonction acceptée' : 'Accepted function'}: ${names.map(name => `\`${name}()\``).join(', ')}.`);
  }
  if (firstTest?.args?.length) {
    lines.push(`${fr ? 'Entrées testées' : 'Tested inputs'}: ${firstTest.args.map((arg, index) => `${index + 1}. ${valueType(arg, language)}`).join(' · ')}.`);
  } else if (/three numbers|trois nombres/i.test(description)) {
    lines.push(fr ? 'Entrée conceptuelle : trois nombres, généralement regroupés dans un tuple ou une liste avant le déballage.' : 'Conceptual input: three numbers, usually grouped in a tuple or list before unpacking.');
  }
  if (explicitOutputType) {
    lines.push(`${fr ? 'Type de résultat demandé par l’énoncé' : 'Result type stated by the prompt'}: ${explicitOutputType}.`);
  } else if (firstTest && firstTest.expected !== null && firstTest.expected !== undefined) {
    lines.push(`${fr ? 'Résultat attendu' : 'Expected result type'}: ${valueType(firstTest.expected, language)}.`);
  } else if (/add|sum|addition|somme/i.test(description)) {
    lines.push(fr ? 'Résultat : un nombre égal à la somme des entrées.' : 'Result: one number equal to the sum of the inputs.');
  } else {
    lines.push(fr ? 'Le résultat doit respecter le comportement décrit, pas seulement reproduire une valeur d’exemple.' : 'The result must satisfy the described behavior, not merely reproduce one example value.');
  }
  return lines;
};

const requiredSyntax = (grader: AutoGrader | null | undefined, language: ProblemAiLanguage, description = '', analysis?: SolutionAnalysis): string[] => {
  const frIndex = language === 'fr' ? 1 : 0;
  const lines: string[] = [];
  for (const requirement of grader?.requiredNodePatterns || []) {
    const description = NODE_REQUIREMENT[requirement.nodeType];
    if (description) lines.push(description[frIndex]);
  }
  for (const requirement of grader?.requiredUnpackPatterns || []) {
    lines.push(language === 'fr'
      ? `Déballez au moins ${requirement.targetCount} cible(s)${requirement.allowStarred ? ' avec une cible étoilée autorisée' : ''}.`
      : `Unpack at least ${requirement.targetCount} target(s)${requirement.allowStarred ? ' with a starred target allowed' : ''}.`);
  }
  const calls = [...(grader?.requiredCallPatterns || []), ...(grader?.requiredAnyCallPatterns || [])];
  for (const requirement of calls.slice(0, 6)) lines.push(describeCall(requirement.functionName, language));
  const userFunctionNames = new Set(grader?.functionNames || []);
  const promptCalls = [...description.matchAll(/(?:\.\s*|\b)([A-Za-z_]\w*)\s*\(\s*\)/g)]
    .map(match => match[1])
    .filter(name => !userFunctionNames.has(name));
  for (const name of [...new Set(promptCalls)].slice(0, 4)) lines.push(describeCall(name, language));
  const operators = [...(grader?.requiredAstOperators || []), ...(grader?.requiredBoolOps || [])]
    .map(operator => OPERATOR_SYNTAX[operator] || operator);
  if (operators.length) lines.push(`${language === 'fr' ? 'Opérateur(s) requis' : 'Required operator(s)'}: ${operators.map(value => `\`${value}\``).join(', ')}.`);
  for (const inheritance of grader?.requiredClassInheritance || []) {
    lines.push(`${language === 'fr' ? 'Héritage requis' : 'Required inheritance'}: \`class ${inheritance.className}(${inheritance.baseName})\`.`);
  }
  return [...new Set(lines)].slice(0, 10);
};

const buildSteps = (description: string, grader: AutoGrader | null | undefined, language: ProblemAiLanguage, analysis: SolutionAnalysis, concepts: string[] = []): string[] => {
  const fr = language === 'fr';
  const lower = description.toLowerCase();
  const steps: string[] = [];
  const hasLambda = concepts.includes('lambda') || /lambda/.test(lower);
  const hasUnpack = concepts.includes('unpacking') || /\bunpack|\*args|starred\b/.test(lower);
  if (analysis.calls.includes('isalpha') && analysis.calls.includes('isdigit') && grader?.requiredBoolOps?.includes('Or')) {
    return fr ? [
      'Définissez la fonction demandée et créez une variable texte contenant une chaîne (`str`).',
      'Évaluez `text.isalpha()` pour savoir si la chaîne non vide contient uniquement des lettres.',
      'Évaluez `text.isdigit()` pour savoir si la chaîne non vide contient uniquement des chiffres.',
      'Combinez les deux booléens avec `or` : `text.isalpha() or text.isdigit()`.',
      'Renvoyez ce booléen. Une chaîne mélangée comme `"abc123"` doit produire `False`.',
    ] : [
      'Define the requested function and create a text variable containing a string (`str`).',
      'Evaluate `text.isalpha()` to check whether the non-empty string contains only letters.',
      'Evaluate `text.isdigit()` to check whether the non-empty string contains only digit characters.',
      'Combine the two Booleans with `or`: `text.isalpha() or text.isdigit()`.',
      'Return that Boolean. A mixed string such as `"abc123"` must produce `False`.',
    ];
  }
  if (/three numbers|trois nombres/.test(lower) && hasLambda && hasUnpack) {
    return fr ? [
      'Regroupez trois nombres dans un tuple ou une liste, par exemple `valeurs = (2, 3, 4)`.',
      'Créez une lambda avec trois paramètres et une expression d\'addition : `lambda a, b, c: a + b + c`.',
      'Appelez la lambda avec `*valeurs`. L\'étoile distribue les trois éléments vers `a`, `b` et `c`.',
      'Affichez ou stockez le nombre renvoyé par cet appel.',
    ] : [
      'Group three numbers in a tuple or list, for example `values = (2, 3, 4)`.',
      'Create a lambda with three parameters and one addition expression: `lambda a, b, c: a + b + c`.',
      'Call the lambda with `*values`. The star distributes the three items to `a`, `b`, and `c`.',
      'Print or store the number returned by that call.',
    ];
  }
  if (hasLambda && hasUnpack) {
    return fr ? [
      'Créez une lambda avec le nombre de paramètres correspondant aux valeurs à traiter.',
      'Utilisez une expression à l\'intérieur de la lambda (après `:`) qui produit le résultat demandé.',
      'Regroupez les valeurs d\'entrée dans un tuple ou une liste.',
      'Appelez la lambda avec l\'opérateur `*` pour déballer le conteneur en arguments séparés.',
      'Récupérez la valeur renvoyée et traitez-la selon l\'énoncé.',
    ] : [
      'Create a lambda with one parameter for each value you need to process.',
      'Write an expression after `:` that computes the required result.',
      'Group the input values in a tuple or list.',
      'Call the lambda with `*` to unpack the container into separate arguments.',
      'Capture the returned value and handle it as the problem requires.',
    ];
  }
  if (hasLambda) {
    steps.push(fr ? 'Définissez une lambda avec la syntaxe `lambda paramètres: expression`.' : 'Define a lambda using `lambda parameters: expression`.');
    steps.push(fr ? 'L\'expression après `:` est automatiquement renvoyée — pas besoin de `return`.' : 'The expression after `:` is automatically returned — no `return` needed.');
    steps.push(fr ? 'Stockez la lambda dans une variable ou appelez-la directement avec `(lambda ...)(args)`.' : 'Store the lambda in a variable or call it directly with `(lambda ...)(args)`.');
  }
  if (hasUnpack) {
    steps.push(fr ? 'Utilisez `*conteneur` pour déballer les éléments d\'un itérable en arguments séparés.' : 'Use `*container` to unpack iterable items into separate arguments.');
    steps.push(fr ? 'Sans `*`, tout le conteneur est passé comme un seul argument.' : 'Without `*`, the entire container is passed as a single argument.');
  }
  if (!hasLambda && !hasUnpack) {
    const names = grader?.functionNames?.filter(Boolean) || [];
    if (names.length && grader?.mode !== 'script') steps.push(fr ? `Définissez \`${names[0]}()\` avec un paramètre pour chaque entrée décrite.` : `Define \`${names[0]}()\` with one parameter for each described input.`);
    else steps.push(fr ? 'Préparez les données d\'entrée avec des noms qui décrivent leur rôle.' : 'Prepare the input data with names that describe each value\'s role.');
  }
  for (const line of requiredSyntax(grader, language, description, analysis).slice(0, 4)) steps.push(line);
  steps.push(/\breturn|returns?\b|\brenvoie\b|\bretourne\b/i.test(description)
    ? (fr ? 'Renvoyez la valeur calculée avec `return`.' : 'Return the calculated value with `return`.')
    : (fr ? 'Produisez la sortie demandée avec `print()` ou l\'opération indiquée.' : 'Produce the requested output with `print()` or the stated operation.'));
  return [...new Set(steps)].slice(0, 7);
};

const commonMistakes = (concepts: string[], grader: AutoGrader | null | undefined, language: ProblemAiLanguage, analysis: SolutionAnalysis): string[] => {
  const fr = language === 'fr';
  const mistakes: string[] = [];
  if (concepts.includes('lambda')) mistakes.push(fr ? 'Une lambda contient une expression après `:` ; elle ne possède pas de bloc d’instructions indenté.' : 'A lambda has one expression after `:`; it does not have an indented statement block.');
  if (concepts.includes('unpacking')) mistakes.push(fr ? 'Sans `*`, le conteneur entier devient un seul argument au lieu de plusieurs arguments.' : 'Without `*`, the whole container becomes one argument instead of separate arguments.');
  if (concepts.includes('subscript') || concepts.includes('slicing')) mistakes.push(fr ? 'Les indices commencent à `0`, et la borne de fin d’un découpage est exclue.' : 'Indexes start at `0`, and a slice stop position is excluded.');
  if (concepts.includes('return')) mistakes.push(fr ? '`print()` affiche une valeur mais ne la renvoie pas à l’appelant.' : '`print()` displays a value but does not return it to the caller.');
  if (concepts.includes('loop')) mistakes.push(fr ? 'Le corps de la boucle doit être indenté ; une boucle `while` doit progresser vers son arrêt.' : 'The loop body must be indented; a `while` loop must progress toward termination.');
  if (analysis.calls.some(call => STRING_METHODS.has(call))) mistakes.push(fr ? 'N’appelez pas une méthode de chaîne sur un entier ou une liste : cela lève `AttributeError`. Le récepteur doit être de type `str`.' : 'Do not call a string method on an integer or list: that raises `AttributeError`. The receiver must be a `str`.');
  if (analysis.calls.includes('isalpha') || analysis.calls.includes('isdigit')) mistakes.push(fr ? 'Écrivez les parenthèses : `text.isalpha()` appelle la méthode, tandis que `text.isalpha` désigne seulement l’objet méthode.' : 'Include parentheses: `text.isalpha()` calls the method, while `text.isalpha` only refers to the method object.');
  if (analysis.calls.includes('isalpha') && analysis.calls.includes('isdigit')) mistakes.push(fr ? 'Utilisez `or`, pas `and` : une chaîne non vide ne peut pas être à la fois composée uniquement de lettres et uniquement de chiffres.' : 'Use `or`, not `and`: a non-empty string cannot be both letters-only and digits-only.');
  if (grader?.mode === 'script') mistakes.push(fr ? 'Ne définissez pas seulement une fonction inutilisée : le script doit exécuter l’opération demandée.' : 'Do not only define an unused function: the script must execute the requested operation.');
  return [...new Set(mistakes)].slice(0, 5);
};

const executionFlow = (analysis: SolutionAnalysis, language: ProblemAiLanguage): string[] => {
  const fr = language === 'fr';
  const p = analysis.patterns;
  if (analysis.calls.includes('isalpha') && analysis.calls.includes('isdigit')) return fr ? [
    'Python crée la fonction sans exécuter immédiatement son corps.',
    'Lors de l’appel, la variable `text` doit référencer une chaîne (`str`).',
    'Python appelle d’abord `text.isalpha()`.',
    'Si ce résultat est `True`, `or` s’arrête immédiatement. Sinon, Python appelle `text.isdigit()`.',
    'Le booléen final est renvoyé à l’appelant, puis peut être affiché avec `print()`.',
  ] : [
    'Python creates the function without immediately running its body.',
    'When called, `text` must refer to a string (`str`).',
    'Python calls `text.isalpha()` first.',
    'If that result is `True`, `or` short-circuits. Otherwise Python calls `text.isdigit()`.',
    'The final Boolean is returned to the caller and can then be displayed with `print()`.',
  ];
  if (p.hasLambda) {
    return fr ? [
      'Python rencontre la lambda et crée un objet fonction sans exécuter l\'expression.',
      'Lors de l\'appel, Python évalue d\'abord les arguments de gauche à droite.',
      'Les paramètres reçoivent les valeurs, puis l\'expression après `:` est évaluée.',
      p.hasUnpacking ? 'L\'opérateur `*` étend l\'itérable pour que chaque élément devienne un argument séparé.' : '',
      'Le résultat de l\'expression est renvoyé automatiquement — pas besoin de `return`.',
    ].filter(Boolean) : [
      'Python encounters the lambda and creates a function object without running the expression.',
      'When called, Python evaluates arguments left to right first.',
      'Parameters receive the values, then the expression after `:` is evaluated.',
      p.hasUnpacking ? 'The `*` operator expands the iterable so each item becomes a separate argument.' : '',
      'The expression result is returned automatically — no `return` needed.',
    ].filter(Boolean);
  }
  if (p.hasComprehension) {
    return fr ? [
      'Python évalue l\'itérable de la première clause `for`.',
      'La variable de boucle reçoit chaque élément.',
      'Les clauses `for` et filtres `if` suivants sont évalués de gauche à droite.',
      'Si les filtres passent, l\'expression de sortie est évaluée et le résultat est collecté dans la nouvelle structure.',
    ] : [
      'Python evaluates the first `for` clause\'s iterable.',
      'The loop variable is bound to each item.',
      'Later `for` clauses and `if` filters are evaluated left to right.',
      'When filters pass, the output expression is evaluated and collected into the new structure.',
    ];
  }
  if (p.hasClass) {
    return fr ? [
      'Python lit la définition de classe et crée un objet classe.',
      'Les méthodes définies avec `def` à l\'intérieur de la classe sont liées à cette classe.',
      'Lorsqu\'une méthode est appelée sur une instance, `self` reçoit automatiquement l\'instance.',
    ] : [
      'Python reads the class definition and creates a class object.',
      'Methods defined with `def` inside the class are bound to that class.',
      'When a method is called on an instance, `self` automatically receives the instance.',
    ];
  }
  return [fr
    ? 'Python crée d\'abord les valeurs et fonctions, évalue les arguments de gauche à droite, exécute l\'opération, puis transmet le résultat à `return`, `print()` ou à la variable cible.'
    : 'Python first creates values and functions, evaluates arguments from left to right, performs the operation, and sends the result to `return`, `print()`, or the target variable.'];
};

const alternativeApproaches = (analysis: SolutionAnalysis, language: ProblemAiLanguage): string[] => {
  const fr = language === 'fr';
  if (analysis.calls.includes('isalpha') && analysis.calls.includes('isdigit')) return fr ? [
    'Forme directe : `return text.isalpha() or text.isdigit()`.',
    'Forme pédagogique : stockez `letters_only = text.isalpha()` et `digits_only = text.isdigit()`, puis renvoyez `letters_only or digits_only`.',
    '`text.isalnum()` n’est pas équivalent : il accepte les mélanges comme `"abc123"`, qui doivent être refusés ici.',
  ] : [
    'Direct form: `return text.isalpha() or text.isdigit()`.',
    'Teaching form: store `letters_only = text.isalpha()` and `digits_only = text.isdigit()`, then return `letters_only or digits_only`.',
    '`text.isalnum()` is not equivalent: it accepts mixed text such as `"abc123"`, which this task must reject.',
  ];
  return [fr ? 'Vous pouvez utiliser des noms de variables différents tant que les types, les opérations et le résultat restent conformes.' : 'You may use different variable names as long as the types, operations, and result remain correct.'];
};

const problemTypeTag = (type: ProblemType, fr: boolean): string => ({
  'function-def': fr ? 'fonction à définir' : 'function to write',
  'script-output': fr ? 'script à produire' : 'script to write',
  'class-def': fr ? 'classe à définir' : 'class to write',
}[type]);

const codeCount = (analysis: SolutionAnalysis): number => {
  const nonEmpty = analysis.snippet.split('\n').filter(line => line.trim() && !line.startsWith('#')).length;
  return nonEmpty || 3;
};

const hasRelevantContent = (items: unknown[] | string | undefined | null): boolean => {
  if (!items) return false;
  if (Array.isArray(items)) return items.length > 0;
  return typeof items === 'string' && items.trim().length > 0;
};

export const buildProblemAiTutorAnswer = ({ exercise, description, grader, language }: ProblemAiTutorContext): string => {
  const fr = language === 'fr';
  const goal = cleanPrompt(description);
  const concepts = detectConcepts(description, grader);
  const analysis = analyzeCanonicalSolution(exercise, grader);
  const problemType = classifyProblemType(grader, analysis.patterns);
  const methods = methodReference(analysis, language);
  const syntax = requiredSyntax(grader, language, description, analysis);
  const steps = buildSteps(description, grader, language, analysis, concepts);
  const mistakes = commonMistakes(concepts, grader, language, analysis);
  const walkthrough = explainSolutionLines(analysis, language);
  const tests = concreteTests(exercise, grader, language);
  const definitions = concepts.map(key => {
    const concept = CONCEPTS[key];
    return `- **${concept.name}** — ${fr ? concept.fr : concept.en}\n  Syntax: \`${concept.syntax}\``;
  });
  const execution = steps.map((step, index) => `${index + 1}. ${step}`);
  const p = analysis.patterns;
  const sections: string[] = [];

  // 1 — type-aware intro
  const codelines = codeCount(analysis);
  const codeIntro = problemType === 'function-def'
    ? (fr ? `La solution de référence contient environ **${codelines} lignes** de code dans la définition de fonction.` : `The reference solution contains about **${codelines} lines** of code inside the function definition.`)
    : problemType === 'class-def'
      ? (fr ? `La solution de référence définit une classe avec environ **${codelines} lignes** de code.` : `The reference solution defines a class with about **${codelines} lines** of code.`)
      : (fr ? `La solution de référence contient environ **${codelines} lignes** de code en script.` : `The reference solution contains about **${codelines} lines** of script code.`);
  const patternTags = [
    p.hasLambda && (fr ? 'λ lambda' : 'λ lambda'),
    p.hasUnpacking && (fr ? '* déballage' : '* unpacking'),
    p.hasComprehension && (fr ? '⊔ compréhension' : '⊔ comprehension'),
    p.hasLoop && (fr ? '↻ boucle' : '↻ loop'),
    p.hasConditional && (fr ? '◆ condition' : '◆ condition'),
    p.hasClass && (fr ? '■ classe' : '■ class'),
    p.hasComparison && (fr ? '= comparaison' : '= comparison'),
  ].filter(Boolean);
  sections.push(
    `**1. ${fr ? 'Ce que demande exactement le problème' : 'What this problem asks'}**\n`
    + (fr ? '**Type**' : '**Type**') + `: ${problemTypeTag(problemType, fr)}.\n`
    + (fr ? '**Comportement demandé**' : '**Required behavior**') + `: ${goal}.\n`
    + codeIntro
    + (patternTags.length ? `\n${fr ? '**Constructions Python détectées**' : '**Python constructs detected**'}: ${patternTags.join(' · ')}.` : '')
  );

  // 2
  sections.push(`**2. ${fr ? 'Entrées et résultat' : 'Inputs and result'}**\n${inferContract(description, grader, language).map(line => `- ${line}`).join('\n')}`);

  // 3
  sections.push(`**3. ${fr ? 'Mots et concepts importants' : 'Key words and concepts'}**\n${definitions.length ? definitions.join('\n') : (fr ? '- Aucun concept spécial n\'est imposé ; concentrez-vous sur la transformation décrite.' : '- No special construct is required; focus on the transformation described.')}`);

  // 4 — skip if no methods referenced
  if (hasRelevantContent(methods)) {
    sections.push(`**4. ${fr ? 'Référence des méthodes et fonctions' : 'Method and function reference'}**\n${methods.map(line => `- ${line}`).join('\n')}`);
  }

  // 5 — skip if grader syntax empty
  if (hasRelevantContent(syntax)) {
    sections.push(`**5. ${fr ? 'Syntaxe que le correcteur recherche' : 'Syntax the grader requires'}**\n${syntax.map(line => `- ${line}`).join('\n')}`);
  }

  // 6 — reference code pattern
  sections.push(`**6. ${fr ? 'Modèle de code de référence' : 'Reference code pattern'}**\n\`\`\`python\n${analysis.snippet}\n\`\`\``);

  // 7 — step-by-step plan
  sections.push(`**7. ${fr ? 'Plan de construction' : 'Step-by-step plan'}**\n${execution.join('\n')}`);

  // 8 — line-by-line, skip if very generic
  if (hasRelevantContent(walkthrough)) {
    sections.push(`**8. ${fr ? 'Explication ligne par ligne' : 'Line-by-line explanation'}**\n${walkthrough.map((line, index) => `${index + 1}. ${line}`).join('\n')}`);
  }

  // 9
  sections.push(`**9. ${fr ? 'Ordre d\'exécution' : 'Execution flow'}**\n${executionFlow(analysis, language).map((line, index) => `${index + 1}. ${line}`).join('\n')}`);

  // 10
  if (hasRelevantContent(mistakes)) {
    sections.push(`**10. ${fr ? 'Erreurs fréquentes à éviter' : 'Common mistakes to avoid'}**\n${mistakes.map(line => `- ${line}`).join('\n')}`);
  }

  // 11
  if (hasRelevantContent(tests)) {
    sections.push(`**11. ${fr ? 'Cas de test concrets' : 'Concrete test cases'}**\n${tests.map(line => `- ${line}`).join('\n')}`);
  }

  // 12
  sections.push(`**12. ${fr ? 'Autres façons correctes de l\'écrire' : 'Other correct ways to write it'}**\n${alternativeApproaches(analysis, language).map(line => `- ${line}`).join('\n')}`);

  return sections.join('\n\n');
};
