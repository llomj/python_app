export type GeneralAiIntent =
  | 'traceback'
  | 'code_explanation'
  | 'output_prediction'
  | 'interactive_debug'
  | 'test_generation'
  | 'code_quality'
  | 'code_comparison'
  | 'complexity_analysis'
  | 'module_project'
  | 'misconception'
  | 'learning_progress'
  | 'version_compatibility'
  | 'function_contract'
  | 'test_execution'
  | 'doctest_execution'
  | 'learning_path'
  | 'contract_search'
  | 'comparison'
  | 'count'
  | 'creation'
  | 'version'
  | 'quiz'
  | 'examples'
  | 'error_help'
  | 'documentation'
  | 'purpose'
  | 'relationships'
  | 'definition'
  | 'mechanism'
  | 'refactoring'
  | 'best_practices'
  | 'async_await'
  | 'type_hints'
  | 'performance'
  | 'debugging'
  | 'what_if'
  | 'library_help'
  | 'design_rationale'
  | 'formatting'
  | 'data_structure'
  | 'import_help'
  | 'code_review'
  | 'package_advice'
  | 'pep8'
  | 'comparison_reference'
  | 'project_structure'
  | 'testing'
  | 'cli'
  | 'string_methods'
  | 'list_methods'
  | 'dict_methods'
  | 'file_io_patterns'
  | 'logging'
  | 'env_guide'
  | 'tooling'
  | 'concurrency'
  | 'http_api'
  | 'database'
  | 'serialization'
  | 'datetime'
  | 'profiling'
  | 'packaging'
  | 'functional'
  | 'security'
  | 'context_manager'
  | 'unknown';

export interface GeneralAiIntentResult {
  intent: GeneralAiIntent;
  confidence: number;
  reason: string;
}

const containsCode = (question: string): boolean => (
  /```(?:python)?/i.test(question)
  || /(^|\n)\s*(?:def |class |for |while |if |from |import |return |yield |print\(|[A-Za-z_]\w*\s*=)/m.test(question)
);

export const classifyGeneralAiIntent = (question: string): GeneralAiIntentResult => {
  const value = question.trim();
  const lower = value.toLowerCase();
  if (/traceback \(most recent call last\)|(^|\n)\s*file ".+", line \d+/i.test(value)) {
    return { intent: 'traceback', confidence: 1, reason: 'Python traceback frames detected' };
  }
  if (containsCode(value) && /\b(?:what (?:does|will) (?:this )?(?:print|output|return)|predict (?:the )?output|trace (?:this|the code)|que va (?:afficher|renvoyer)|pr[eé]dis la sortie)\b/i.test(value)) {
    return { intent: 'output_prediction', confidence: 0.99, reason: 'Python code and output-prediction request detected' };
  }
  if (containsCode(value) && /\b(?:step through|debug step|trace execution|show variable changes|loop iterations|pas à pas|trace l['’]exécution|changements? de variables?|itérations? de boucle)\b/i.test(value)) {
    return { intent: 'interactive_debug', confidence: 0.99, reason: 'Interactive execution-trace request detected' };
  }
  if (/\b(?:how (?:to|do (?:i|you)|can (?:i|you)) .{0,40} debug|debugging (?:tips?|strateg|technique|approach)|how to use pdb|breakpoint|debugg\b.{0,20}(?:python|code))\b/i.test(value)) {
    return { intent: 'debugging', confidence: 0.96, reason: 'Debugging strategy request detected' };
  }
  if ((value.match(/```(?:python)?/gi) || []).length >= 2 && /\b(?:compare|comparison|versus|vs\.?|which (?:code|solution|approach)|better solution|comparaison|quelle solution|meilleure solution)\b/i.test(value)) {
    return { intent: 'code_comparison', confidence: 0.99, reason: 'Two Python snippets and a comparison request detected' };
  }
  if (containsCode(value) && /\b(?:time complexity|space complexity|big[- ]?o|complexity|runtime cost|memory cost|complexit[eé]|notation grand o|co[uû]t temporel|co[uû]t m[eé]moire)(?=\s|[?:.,]|$)/i.test(value)) {
    return { intent: 'complexity_analysis', confidence: 0.99, reason: 'Algorithm complexity request detected' };
  }
  if (/\b(?:performance|speed.?up|fast(?:er)?|optimize?|optimis.|bottleneck|slow)\b.{0,30}\b(?:python|code|function|loop|script)\b/i.test(value)) {
    return { intent: 'performance', confidence: 0.95, reason: 'Performance optimization request detected' };
  }
  if (containsCode(value) && /\b(?:function contract|analy[sz]e (?:the )?contract|parameters?,? returns?|input.?output contract|preconditions?|postconditions?|contrat (?:de la )?fonction|analyse le contrat|param[eè]tres?,? retours?|pr[eé]conditions?|postconditions?)\b/i.test(value)) {
    return { intent: 'function_contract', confidence: 0.99, reason: 'Function contract analysis request detected' };
  }
  if (containsCode(value) && /(?:doctests?|tests? de documentation|exemples? >>>)/i.test(value) && /(?:>>>|doctests?)/i.test(value)) {
    return { intent: 'doctest_execution', confidence: 0.99, reason: 'Bounded local doctest request detected' };
  }
  if (containsCode(value) && /\b(?:run|execute|check|verify|lance|ex[eé]cute|v[eé]rifie).{0,20}\b(?:tests?|assertions?)\b/i.test(value)) {
    return { intent: 'test_execution', confidence: 0.99, reason: 'Bounded local assertion-test request detected' };
  }
  if (/\b(?:modules?|imports?|packages?|multi[- ]?file|project structure|circular import|relative import|absolute import|__init__|__main__|fichiers? multiples?|structure (?:du |de )?projet|importation circulaire|importation relative|paquets?)\b/i.test(value)) {
    return { intent: 'module_project', confidence: 0.97, reason: 'Python module, import, package, or multi-file request detected' };
  }
  if (/\b(?:my progress|learning progress|progress report|weak areas?|strengths?|what should i revise|mastery report|mes progr[eè]s|rapport de progression|points? faibles?|points? forts?|que dois-je r[eé]viser|bilan d['’]apprentissage)\b/i.test(value)) {
    return { intent: 'learning_progress', confidence: 0.99, reason: 'Personal learning-progress request detected' };
  }
  if (containsCode(value) && /\b(?:minimum python version|python version compatibility|will this (?:work|run)|compatible with python|requires? python|support python|version minimale de python|compatibilit[eé].*python|compatible (?:avec|sous) python|fonctionne(?:ra)? (?:avec|sous) python|n[eé]cessite python|prend en charge python)\b/i.test(value)) {
    return { intent: 'version_compatibility', confidence: 0.99, reason: 'Code-level Python version compatibility request detected' };
  }
  if (/\b(?:misconception|what am i misunderstanding|common mistake|conceptual error|malentendu|qu['’]est-ce que je comprends mal|erreur de compr[eé]hension)\b/i.test(value)
    || (containsCode(value) && /\b(?:returns? none|unexpected behavior|comportement inattendu)\b/i.test(value))) {
    return { intent: 'misconception', confidence: 0.97, reason: 'Python misconception-diagnosis request detected' };
  }
  if (containsCode(value) && /\b(?:generate|create|write|suggest|show|make|g[eé]n[eè]re|cr[eé]e|[eé]cris|propose|montre).{0,25}\b(?:tests?|test cases?|edge cases?|cas de test|cas limites?)\b/i.test(value)) {
    return { intent: 'test_generation', confidence: 0.99, reason: 'Test-case generation request detected' };
  }
  if (containsCode(value) && /\b(?:review|quality|readability|pythonic|pep\s*8|performance|security|improve|refactor|qualit[eé]|lisibilit[eé]|am[eé]liore|refactorise)\b/i.test(value)) {
    return { intent: 'code_quality', confidence: 0.98, reason: 'Python code and quality-review request detected' };
  }
  if (/\b(?:refactor|rewrite|clean.?up|clean.?code|restructure|simplif)(?:\s+(?:this|the|my|function|code|class))?\b/i.test(value)) {
    return { intent: 'refactoring', confidence: 0.96, reason: 'Code refactoring request detected' };
  }
  if (/\b(?:what (?:if|happens?|would|when)|what happens (?:when|if)|scenario|imagine|suppose)\b/i.test(value)
    && /\b(?:modif|mutat|append|remove|delete|change|loop|iterat|add|insert|while|infinite)\b/i.test(value)) {
    return { intent: 'what_if', confidence: 0.94, reason: 'What-if scenario simulation request detected' };
  }
  if (/\b(?:how (?:do|can|to)\s+use\s+(?:the\s+)?|usage of|example of using|guide to using|how to work with)\b/i.test(value)
    && /\b(?:requests?|json|pathlib|re|regex|datetime|subprocess|os\.|sys|itertools|collections|random|math|string|typing)\b/i.test(value)) {
    return { intent: 'library_help', confidence: 0.95, reason: 'Standard-library usage request detected' };
  }
  if (/\b(?:why (?:does|is|was|did|would|are)|design (?:choice|decision|rationale)|reason (?:behind|for)|rationale)\b/i.test(value)
    && /\b(?:python|list|tuple|dict|str|int|print|sort|join|map|filter|lambda|return|none|null|immutable|mutable)\b/i.test(value)) {
    return { intent: 'design_rationale', confidence: 0.93, reason: 'Python design-rationale request detected' };
  }
  if (/\b(?:async|await|coroutine|asyncio|asynchronous)\b/i.test(value)
    && !/\b(?:modules?|imports?|packages?)\b/i.test(value)) {
    return { intent: 'async_await', confidence: 0.96, reason: 'Async/await request detected' };
  }
  if (/\b(?:learning path|roadmap|study plan|what should i learn|parcours|feuille de route|plan d['’][eé]tude)\b/i.test(lower)) {
    return { intent: 'learning_path', confidence: 0.97, reason: 'Structured learning-path request detected' };
  }
  if (/\b(?:find|which|show|list|search|trouve|quels?|montre|liste|cherche)\b/i.test(lower)
    && /\b(?:methods?|functions?|m[eé]thodes?|fonctions?)\b/i.test(lower)
    && /\b(?:return|accept|iterable|mutat|modify|in place|remove|delete|sort|copy|none|renvoie|accepte|modifie|supprime|trie|copie)\b/i.test(lower)) {
    return { intent: 'contract_search', confidence: 0.96, reason: 'API contract search detected' };
  }
  if (containsCode(value) && /explain|analyse|analyze|debug|why|output|code|ligne|erreur/i.test(value)) {
    return { intent: 'code_explanation', confidence: 0.98, reason: 'Python code and an analysis request detected' };
  }
  if (/\b(?:difference between|compare|versus|vs\.?|diff[eé]rence entre|compar(?:e|er))\b/i.test(lower)) {
    return { intent: 'comparison', confidence: 0.98, reason: 'Comparison phrasing detected' };
  }
  if (/\b(?:format.*(?:string|chaîne|str)|f.?string|%-formatting|printf|template.*string|which.*format|diff(?:érence|erence).*format)\b/i.test(lower)
    && (/\bf["']/i.test(value) || /\.format\b|%[sdfer%]|Template\b/i.test(value))) {
    return { intent: 'formatting', confidence: 0.95, reason: 'String formatting comparison request detected' };
  }
  if (/\b(?:which (?:data )?structure|list vs|tuple vs|set vs|dict vs|when to use|should i use|what (?:data )?structure|quelle structure|liste ou|tuple ou|set ou|dict ou)\b/i.test(lower)) {
    return { intent: 'data_structure', confidence: 0.94, reason: 'Data structure choice request detected' };
  }
  if (/\b(?:import|sys\.path|__init__|circular import|module.*not found|import.*error|package.*structure|importlib)\b/i.test(lower)
    && /\b(?:how|what|why|can'?t|not|problem|error|fix|solve|résoudre|problème|erreur)\b/i.test(lower)) {
    return { intent: 'import_help', confidence: 0.93, reason: 'Import system help request detected' };
  }
  if (/\b(?:review|audit|revise|code review|review.*code|check my code)\b/i.test(lower)
    && containsCode(value)) {
    return { intent: 'code_review', confidence: 0.96, reason: 'Code review request detected' };
  }
  if (/\b(?:type (?:hint|annotation)|typing\b|mypy|type.?safe)\b/i.test(lower)) {
    return { intent: 'type_hints', confidence: 0.96, reason: 'Type hints request detected' };
  }
  if (/\b(?:string.*method|str\.\w+\(|\.upper|\.lower|\.strip|\.split|\.join|\.replace|\.find)\b/i.test(lower) && !/\b(?:format|Template)\b/i.test(lower)) {
    return { intent: 'string_methods', confidence: 0.93, reason: 'String methods reference request detected' };
  }
  if (/\b(?:list.*method|\.append|\.extend|\.insert|\.remove|\.pop|\.sort|\.reverse)\b/i.test(lower)) {
    return { intent: 'list_methods', confidence: 0.93, reason: 'List methods reference request detected' };
  }
  if (/\b(?:dict.*method|\.get|\.keys|\.values|\.items|\.setdefault|\.popitem)\b/i.test(lower)) {
    return { intent: 'dict_methods', confidence: 0.93, reason: 'Dict methods reference request detected' };
  }
  if (/\b(?:file.?io|file.?read|file.?write|open.*file|encoding|binary.*file|text.*file|StringIO|BytesIO|tempfile)\b/i.test(lower)) {
    return { intent: 'file_io_patterns', confidence: 0.93, reason: 'File I/O patterns request detected' };
  }
  if (/\b(?:logging|logger|log.*config|handler|formatter|basicConfig)\b/i.test(lower)) {
    return { intent: 'logging', confidence: 0.94, reason: 'Logging patterns request detected' };
  }
  if (/\b(?:venv|virtual.?env|virtual environment|conda|poetry|pipenv|environnement virtuel|gestionnaire de paquets|package manager|requirements\.txt|install.*package)\b/i.test(lower)) {
    return { intent: 'env_guide', confidence: 0.95, reason: 'Environment management request detected' };
  }
  if (/\b(?:pdb|debug(?:ger|ging)|breakpoint|linter|lint|ruff|flake8|mypy|type.?check|black|formatter|code.?style|vs.?code|ide|outil de débogage|formateur)\b/i.test(lower)) {
    return { intent: 'tooling', confidence: 0.94, reason: 'Tooling/debugging request detected' };
  }
  if (/\b(?:threading|multiprocessing|gil|race.?condition|deadlock|thread.?safe|parallelis|concurrent\.futures|executor|pool|concurrence)\b/i.test(lower)) {
    return { intent: 'concurrency', confidence: 0.94, reason: 'Concurrency / parallel request detected' };
  }
  if (/\b(?:http|requests?|httpx|api|rest|endpoint|session|retry|pagination|webhook|resp\.json|resp\.text|status_code)\b/i.test(lower)) {
    return { intent: 'http_api', confidence: 0.93, reason: 'HTTP / API request detected' };
  }
  if (/\b(?:sql(?:ite|alchemy)?|database|orm|query|migration|connection.?pool|cursor|insert|select|from.*where|db\.|alembic)\b/i.test(lower)) {
    return { intent: 'database', confidence: 0.94, reason: 'Database / SQL request detected' };
  }
  if (/\b(?:serialize|deserialize|json|pickle|msgpack|yaml|marshal|encode.*object|decode.*object|dump.*load)\b/i.test(lower)) {
    return { intent: 'serialization', confidence: 0.93, reason: 'Serialization request detected' };
  }
  if (/\b(?:datetime|date.*time|timezone|strftime|strptime|timedelta|dateutil|pytz|tzinfo)\b/i.test(lower)) {
    return { intent: 'datetime', confidence: 0.94, reason: 'Date/time request detected' };
  }
  if (/\b(?:profile|profiler|cprofile|timeit|benchmark|optimize|bottleneck|memory.?usage|cpu.?time|perf_counter)\b/i.test(lower)) {
    return { intent: 'profiling', confidence: 0.93, reason: 'Performance profiling request detected' };
  }
  if (/\b(?:publish|distribute|pypi|setuptools|wheel|egg|twine|package.*build|upload.*pip|pip.*publish|distribution.*python)\b/i.test(lower)) {
    return { intent: 'packaging', confidence: 0.94, reason: 'Python packaging / distribution request detected' };
  }
  if (/\b(?:itertools|functools|map.*filter|filter.*map|reduce.*list|partial|compose|operator\.\w+|curry|pure.?function)\b/i.test(lower)) {
    return { intent: 'functional', confidence: 0.93, reason: 'Functional programming request detected' };
  }
  if (/\b(?:security|hash|encrypt|sanitize|injection|sql.*inject|secret|env.*var(?:iable)?|token|password.*safe)\b/i.test(lower)) {
    return { intent: 'security', confidence: 0.93, reason: 'Security / safe-patterns request detected' };
  }
  if (/\b(?:context.?manager|with.*statement|contextlib|contextvar|exitstack|@contextmanager|__enter__|__exit__)\b/i.test(lower)) {
    return { intent: 'context_manager', confidence: 0.94, reason: 'Context manager request detected' };
  }
  if (/\b(?:project structure|folder structure|how to structure|how to organize|project layout|src layout|structure du projet)\b/i.test(lower)) {
    return { intent: 'project_structure', confidence: 0.96, reason: 'Project structure request detected' };
  }
  if (/\b(?:pytest|unit.?test|how to test|write.*test|test.*pattern|testing.*fixture|parametrize|mock|tester|test.*écrire)\b/i.test(lower)) {
    return { intent: 'testing', confidence: 0.94, reason: 'Testing/testing patterns request detected' };
  }
  if (/\b(?:CLI|command.?line|if __name__|argparse|sys\.argv|entry.?point|console.?script|point d['’]entr[eé]e|ligne de commande)\b/i.test(lower)) {
    return { intent: 'cli', confidence: 0.94, reason: 'CLI/command-line patterns request detected' };
  }
  if (/\b(?:best (?:library|package|tool|framework)|recommend.*(?:library|package|framework)|what.*(?:library|package|tool).*use|which.*library|quel.*(?:biblioth[eè]que|module|paquet))\b/i.test(lower)) {
    return { intent: 'package_advice', confidence: 0.95, reason: 'Package/library recommendation request detected' };
  }
  if (/\b(?:pep.?8|style guide|naming conventions?|import order|line length|docstring convention)\b/i.test(lower)) {
    return { intent: 'pep8', confidence: 0.96, reason: 'PEP 8 / style guide request detected' };
  }
  if (/\b(?:is vs ==|== vs is|copy vs deepcopy|deepcopy vs copy|str vs repr|repr vs str|classmethod vs staticmethod|staticmethod vs classmethod|new vs init|init vs new|eq vs hash)\b/i.test(lower)) {
    return { intent: 'comparison_reference', confidence: 0.97, reason: 'Specific Python comparison reference request detected' };
  }
  if (/\b(?:best pract|recommended way|pythonic way|proper way|correct way)\b/i.test(lower)) {
    return { intent: 'best_practices', confidence: 0.96, reason: 'Best practices request detected' };
  }
  if (/\b(?:how can i|what should i use|which (?:method|function|type|tool)|best way to|comment (?:puis-je|faire)(?:\s+pour)?|que dois-je utiliser)\b/i.test(lower)) {
    return { intent: 'purpose', confidence: 0.95, reason: 'Purpose-based tool request detected' };
  }
  if (/\b(?:how many|number of|count of|combien|nombre de)\b/i.test(lower)) {
    return { intent: 'count', confidence: 0.96, reason: 'Count request detected' };
  }
  if (/\b(?:how (?:do|can|would) (?:i|you)|how to|comment)\b/i.test(lower)
    && /\b(?:create|make|write|build|define|start|use|cr[eé]er|faire|[eé]crire|d[eé]finir|utiliser)\b/i.test(lower)) {
    return { intent: 'creation', confidence: 0.94, reason: 'How-to creation request detected' };
  }
  if (/\b(?:what version|which version|when was|introduced|added in|deprecated|version|quelle version|ajout[eé]|introduit)\b/i.test(lower)) {
    return { intent: 'version', confidence: 0.94, reason: 'Version request detected' };
  }
  if (/\b(?:quiz|test me|practice me|check my understanding|interroge-moi|teste-moi)\b/i.test(lower)) {
    return { intent: 'quiz', confidence: 0.96, reason: 'Quiz request detected' };
  }
  if (/\b(?:examples?|show me|another example|exemples?|montre-moi)\b/i.test(lower)) {
    return { intent: 'examples', confidence: 0.88, reason: 'Example request detected' };
  }
  if (/\b(?:documentation|official docs?|reference|docs? for|documentation officielle|r[eé]f[eé]rence)\b/i.test(lower)) {
    return { intent: 'documentation', confidence: 0.94, reason: 'Documentation request detected' };
  }
  if (/\b(?:related concepts?|concepts? (?:are )?related|what next|learn next|connected to|goes with|concepts? li[eé]s?|apprendre ensuite)\b/i.test(lower)) {
    return { intent: 'relationships', confidence: 0.92, reason: 'Concept relationship request detected' };
  }
  if (/\b(?:syntaxerror|typeerror|nameerror|valueerror|keyerror|indexerror|indentationerror|attributeerror|exception|error|erreur)\b/i.test(lower)) {
    return { intent: 'error_help', confidence: 0.91, reason: 'Python error name or error request detected' };
  }
  if (/^how\s+(?:does|do|is|are)\s+.+\bwork(?:s|ing)?\b/i.test(value)
    || /\bhow\s+(?:does|do|is|are)\s+.+\b(?:internally|under the hood|behind the scenes|mechanism)\b/i.test(value)) {
    return { intent: 'mechanism', confidence: 0.96, reason: 'How-does-it-work mechanism request detected' };
  }
  if (/^(?:please\s+)?(?:what(?:'s|\s+is|\s+are|\s+does)|define|describe|explain|tell me about|tell me what|qu['’]est-ce que|d[eé]finis?|explique|d[eé]cris)\b/i.test(value)
    || /^(?:(?:can|could|would)\s+you\s+(?:explain|tell me about|describe|define)|do\s+you\s+know\s+(?:what|how)|i\s+(?:want\s+(?:to\s+)?(?:know|understand|learn)|'?m\s+(?:confused about|curious about|wondering)|'?d\s+like\s+to\s+(?:know|understand)))\b/i.test(value)
    || /^remind\s+me\s+(what|about)\b/i.test(value)
    || value.split(/\s+/).length <= 4) {
    return { intent: 'definition', confidence: 0.82, reason: 'Definition or short concept query detected' };
  }
  if (containsCode(value)) {
    return { intent: 'code_explanation', confidence: 0.76, reason: 'Python code detected' };
  }
  return { intent: 'unknown', confidence: 0.35, reason: 'No reliable Python intent matched' };
};

export const shouldClarifyGeneralAiQuestion = (question: string): boolean => {
  const value = question.trim();
  if (!value) return true;
  if (/^(?:it|this|that|more|why|how|yes|no|cela|ça|pourquoi|comment)[?.!]*$/i.test(value)) return true;
  return classifyGeneralAiIntent(value).intent === 'unknown' && value.split(/\s+/).length < 3;
};
