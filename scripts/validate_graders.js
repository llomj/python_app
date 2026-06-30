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
      esModuleInterop: true,
    },
    fileName,
  }).outputText;
  const sandbox = {
    exports: {},
    module: { exports: {} },
    require: () => ({}),
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');

const exerciseIds = EXERCISES.map(exercise => exercise.id);
const uniqueExerciseIds = new Set(exerciseIds);
const duplicateExerciseIds = exerciseIds.filter((id, index) => exerciseIds.indexOf(id) !== index);
const graderIds = Object.keys(AUTO_GRADERS).map(Number);
const missingGraders = exerciseIds.filter(id => !AUTO_GRADERS[id]);
const orphanGraders = graderIds.filter(id => !uniqueExerciseIds.has(id));

if (duplicateExerciseIds.length || missingGraders.length || orphanGraders.length) {
  if (duplicateExerciseIds.length) {
    console.error(`Duplicate exercise IDs: ${[...new Set(duplicateExerciseIds)].join(', ')}`);
  }
  if (missingGraders.length) {
    console.error(`Exercises missing graders: ${missingGraders.join(', ')}`);
  }
  if (orphanGraders.length) {
    console.error(`Graders without matching exercises: ${orphanGraders.join(', ')}`);
  }
  process.exit(1);
}

const validator = String.raw`
import ast
import builtins
import contextlib
import io
import inspect
import json
import math
import os
import random
import re
import shutil
import signal
import sys
import tempfile

payload = json.load(sys.stdin)

class SolutionTimeout(Exception):
    pass

@contextlib.contextmanager
def time_limit(seconds):
    def handler(_signum, _frame):
        raise SolutionTimeout(f"solution exceeded {seconds}s")
    old_handler = signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)

def jsonable(value):
    try:
        json.dumps(value)
        return value
    except Exception:
        return repr(value)

def normalize(value):
    if hasattr(value, "isoformat") and callable(value.isoformat):
        try:
            return value.isoformat()
        except Exception:
            pass
    if isinstance(value, os.PathLike):
        return str(value)
    if type(value).__name__ in ("dict_keys", "dict_values", "dict_items"):
        return [normalize(item) for item in value]
    if hasattr(value, "__iter__") and hasattr(value, "__next__"):
        return [normalize(item) for item in value]
    if isinstance(value, tuple):
        return [normalize(item) for item in value]
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, set):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): normalize(item) for key, item in value.items()}
    return value

def numbers(value):
    return [float(match) for match in re.findall(r"-?\d+(?:\.\d+)?", str(value))]

def maybe_literal(value):
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text:
        return value
    try:
        return ast.literal_eval(text)
    except Exception:
        pass
    try:
        return json.loads(text)
    except Exception:
        return value

def clean_text(value):
    return "\n".join(line.rstrip() for line in str(value).strip().splitlines())

def compact_pattern(value):
    return "\n".join(re.sub(r"[ \t]+", "", line) for line in clean_text(value).splitlines())

def meaningful_text_matches(actual_text, expected):
    actual_text = clean_text(actual_text)
    expected_value = normalize(maybe_literal(expected))
    expected_text = clean_text(expected)
    lines = [line.strip() for line in actual_text.splitlines() if line.strip()]
    if not lines:
        return False

    candidates = []
    for line in lines:
        candidates.append(line)
        for separator in (":", "=", "->"):
            if separator in line:
                candidates.append(line.rsplit(separator, 1)[-1].strip())
        tokens = re.findall(r"True|False|-?\d+(?:\.\d+)?|['\"][^'\"]+['\"]", line, re.IGNORECASE)
        if tokens:
            last_token = tokens[-1]
            candidates.append(last_token if isinstance(last_token, str) else str(last_token))

    for candidate in candidates:
        if values_equivalent(candidate, expected_value):
            return True
        if expected_text and clean_text(candidate).lower() == expected_text.lower():
            return True

    last_line = lines[-1]
    if isinstance(expected_value, bool):
        bool_tokens = re.findall(r"\b(true|false)\b", last_line, re.IGNORECASE)
        return bool(bool_tokens and (bool_tokens[-1].lower() == str(expected_value).lower()))
    if isinstance(expected_value, (int, float)) and not isinstance(expected_value, bool):
        found_numbers = numbers(last_line)
        if found_numbers:
            try:
                return math.isclose(float(found_numbers[-1]), float(expected_value), rel_tol=1e-9, abs_tol=1e-9)
            except Exception:
                return False
    if isinstance(expected_value, str) and expected_value:
        return expected_value.lower() in actual_text.lower()
    return False

def values_equivalent(actual, expected):
    actual = normalize(maybe_literal(actual))
    expected = normalize(maybe_literal(expected))
    if actual == expected:
        return True
    if isinstance(actual, str) and isinstance(expected, str):
        return clean_text(actual) == clean_text(expected)
    if isinstance(actual, (int, float)) or isinstance(expected, (int, float)):
        try:
            return math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-9)
        except Exception:
            pass
    if isinstance(actual, str) and isinstance(expected, bool):
        return actual.strip().lower() == str(expected).lower()
    if isinstance(expected, str) and isinstance(actual, bool):
        return expected.strip().lower() == str(actual).lower()
    return False

def repair_generated_string_newlines(source):
    repaired = []
    quote = None
    triple = False
    escaped = False
    in_comment = False
    i = 0
    while i < len(source):
        char = source[i]
        if in_comment:
            repaired.append(char)
            if char == "\n":
                in_comment = False
            i += 1
            continue
        if quote is None:
            if char == "#":
                in_comment = True
                repaired.append(char)
                i += 1
                continue
            if char in ("'", '"'):
                quote = char
                triple = source[i:i + 3] == char * 3
                if triple:
                    repaired.append(source[i:i + 3])
                    i += 3
                    continue
            repaired.append(char)
            i += 1
            continue
        if triple:
            if source[i:i + 3] == quote * 3:
                repaired.append(source[i:i + 3])
                i += 3
                quote = None
                triple = False
                escaped = False
                continue
            repaired.append(char)
            i += 1
            continue
        if escaped:
            repaired.append(char)
            escaped = False
            i += 1
            continue
        if char == "\\":
            repaired.append(char)
            escaped = True
            i += 1
            continue
        if char == quote:
            repaired.append(char)
            quote = None
            i += 1
            continue
        if char == "\n":
            repaired.append("\\n")
            i += 1
            continue
        repaired.append(char)
        i += 1
    return "".join(repaired)

def has_executable_ast(source):
    try:
        return bool(ast.parse(source).body)
    except SyntaxError:
        return False

def same(actual, expected, compare):
    if compare == "typeName":
        return type(actual).__name__ == expected
    actual = normalize(actual)
    expected = normalize(expected)
    if isinstance(actual, str) and isinstance(expected, (list, dict, tuple, set)):
        actual = normalize(maybe_literal(actual))
    if compare == "float":
        try:
            return math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-9)
        except Exception:
            return False
    if compare == "printedOrReturn":
        actual_text = clean_text(actual)
        expected_text = clean_text(expected)
        actual_lines = [line.strip() for line in actual_text.splitlines() if line.strip()]
        return values_equivalent(actual, expected) or actual_text == expected_text or expected_text in actual_text or compact_pattern(actual_text) == compact_pattern(expected_text) or any(values_equivalent(line, expected) for line in actual_lines) or meaningful_text_matches(actual_text, expected)
    if compare == "numberRange":
        found = numbers(actual)
        if not found or not isinstance(expected, list) or len(expected) != 2:
            return False
        return float(expected[0]) <= found[-1] <= float(expected[1])
    if compare == "setPop":
        if not isinstance(expected, list):
            return False
        lines = clean_text(actual).splitlines()
        if len(lines) < 2:
            return False
        try:
            removed_values = numbers(lines[0])
            remaining = maybe_literal(lines[1])
            if len(removed_values) != 1:
                return False
            removed = int(removed_values[0])
            expected_set = set(expected)
            return removed in expected_set and set(remaining) == expected_set - {removed}
        except Exception:
            return False
    if compare == "length":
        try:
            return len(str(actual)) == int(expected)
        except Exception:
            return False
    if compare == "unorderedList":
        try:
            return sorted(list(maybe_literal(actual))) == sorted(list(maybe_literal(expected)))
        except Exception:
            return False
    if compare == "unorderedWords":
        try:
            actual = maybe_literal(actual)
            expected = maybe_literal(expected)
            if isinstance(actual, str):
                actual = actual.split()
            if isinstance(expected, str):
                expected = expected.split()
            return sorted(list(actual)) == sorted(list(expected))
        except Exception:
            return False
    if compare == "numberList":
        try:
            return numbers(actual) == [float(item) for item in expected]
        except Exception:
            return False
    if compare == "dictUnorderedLists":
        actual = maybe_literal(actual)
        expected = maybe_literal(expected)
        if not isinstance(actual, dict) or not isinstance(expected, dict) or set(actual.keys()) != set(expected.keys()):
            return False
        try:
            return all(sorted(list(actual[key])) == sorted(list(expected[key])) for key in expected)
        except Exception:
            return False
    if compare == "letterCounts":
        if isinstance(actual, dict):
            return actual.get("upper", actual.get("uppercase")) == expected.get("upper") and actual.get("lower", actual.get("lowercase")) == expected.get("lower")
        if isinstance(actual, (list, tuple)) and len(actual) == 2:
            return list(actual) in ([expected.get("upper"), expected.get("lower")], [expected.get("lower"), expected.get("upper")])
        text = str(actual).lower()
        lower_match = re.search(r"lower\D+(\d+)", text)
        upper_match = re.search(r"upper\D+(\d+)", text)
        return bool(lower_match and upper_match and int(lower_match.group(1)) == expected.get("lower") and int(upper_match.group(1)) == expected.get("upper"))
    if compare == "vowelConsonantCounts":
        if isinstance(actual, dict):
            return actual.get("vowels", actual.get("vowel")) == expected.get("vowels") and actual.get("consonants", actual.get("consonant")) == expected.get("consonants")
        if isinstance(actual, (list, tuple)) and len(actual) == 2:
            return list(actual) == [expected.get("vowels"), expected.get("consonants")]
        text = str(actual).lower()
        vowel_match = re.search(r"vowels?\D+(\d+)", text)
        consonant_match = re.search(r"consonants?\D+(\d+)", text)
        return bool(vowel_match and consonant_match and int(vowel_match.group(1)) == expected.get("vowels") and int(consonant_match.group(1)) == expected.get("consonants"))
    return actual == expected

def runnable_variants(source, prefer_markers=False):
    markers = [
        "\n\n# Wrapped in function",
        "\n\n# Using ",
        "\n\n# Adding ",
        "\n\n# With ",
        "\n\n# Alternative",
        "\n\n# Script approach",
        "\n\n# Direct approach",
    ]
    candidates = [] if prefer_markers else [source]
    marker_positions = sorted(
        (source.index(marker), marker)
        for marker in markers
        if marker in source
    )
    for _position, marker in marker_positions:
        candidates.append(source.split(marker, 1)[0])
    candidates.append(source)
    lines = source.splitlines()
    for i in range(len(lines), 0, -1):
        candidates.append("\n".join(lines[:i]))
    seen = set()
    for candidate in candidates:
        candidate = candidate.strip() + "\n"
        candidate = repair_generated_string_newlines(candidate)
        if candidate in seen:
            continue
        seen.add(candidate)
        try:
            compile(candidate, "<solution>", "exec")
            if not has_executable_ast(candidate):
                continue
            yield candidate
        except SyntaxError:
            continue

def runnable_prefix(source, prefer_markers=False):
    for candidate in runnable_variants(source, prefer_markers):
        return candidate
    return source

def declarations_only(source):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source
    allowed = (
        ast.Import,
        ast.ImportFrom,
        ast.FunctionDef,
        ast.AsyncFunctionDef,
        ast.ClassDef,
    )
    tree.body = [node for node in tree.body if isinstance(node, allowed)]
    ast.fix_missing_locations(tree)
    try:
        return ast.unparse(tree) + "\n"
    except Exception:
        return source

def declarations_first_defs(source):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source
    kept = []
    seen = set()
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            kept.append(node)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name not in seen:
            seen.add(node.name)
            kept.append(node)
    tree.body = kept
    ast.fix_missing_locations(tree)
    try:
        return ast.unparse(tree) + "\n"
    except Exception:
        return source

def declaration_variants(source):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return [source]
    allowed = (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
    declaration_nodes = [node for node in tree.body if isinstance(node, allowed)]
    variants = []
    for end in range(1, len(declaration_nodes) + 1):
        variant_tree = ast.Module(body=declaration_nodes[:end], type_ignores=[])
        ast.fix_missing_locations(variant_tree)
        try:
            variants.append(ast.unparse(variant_tree) + "\n")
        except Exception:
            pass
    final = declarations_only(source)
    variants.append(final)
    seen = set()
    unique = []
    for variant in variants:
        if variant not in seen:
            seen.add(variant)
            unique.append(variant)
    return unique or [source]

def call_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None

def source_requirements_ok(source, grader):
    call_patterns = grader.get("requiredCallPatterns", [])
    node_patterns = grader.get("requiredNodePatterns", [])
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
    all_nodes = list(ast.walk(tree))
    tests = grader.get("tests", [])
    needs_input = any(case.get("inputValues") for case in tests)
    if needs_input and not any(call_name(call.func) == "input" for call in calls):
        return False
    random_call_names = {"randint", "randrange", "random", "uniform", "choice", "sample", "shuffle", "choices"}
    needs_random = any(
        case.get("randomValues") or
        case.get("randomFloatValues") or
        case.get("randomChoiceValues") or
        case.get("randomSampleValues") or
        case.get("randomShuffleValues")
        for case in tests
    )
    if needs_random and not any(call_name(call.func) in random_call_names for call in calls):
        return False
    if not call_patterns and not node_patterns:
        return True
    for pattern in call_patterns:
        function_name = pattern.get("functionName")
        keyword = pattern.get("keyword")
        min_args = pattern.get("minArgs")
        matched = False
        for call in calls:
            if call_name(call.func) != function_name:
                continue
            if keyword and not any(item.arg == keyword for item in call.keywords):
                continue
            if min_args is not None and len(call.args) < int(min_args):
                continue
            matched = True
            break
        if not matched:
            return False
    for pattern in node_patterns:
        node_type = pattern.get("nodeType")
        min_count = int(pattern.get("minCount", 1))
        count = sum(1 for node in all_nodes if type(node).__name__ == node_type)
        if count < min_count:
            return False
    return True

def has_hardcoded_expected_output(source, expected):
    if not isinstance(expected, str):
        return False
    expected_text = clean_text(expected)
    if len(expected_text) < 20 or "\n" not in expected_text:
        return False
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    expected_compact = compact_pattern(expected_text)
    expected_lines = [
        compact_pattern(line)
        for line in expected_text.splitlines()
        if line.strip()
    ]
    literal_lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            literal_text = clean_text(node.value)
            if literal_text == expected_text or compact_pattern(literal_text) == expected_compact:
                return True
            for literal_line in literal_text.splitlines():
                if literal_line.strip():
                    literal_lines.add(compact_pattern(literal_line))
    if len(expected_lines) >= 8 and literal_lines:
        matched_lines = sum(1 for line in expected_lines if line in literal_lines)
        if matched_lines >= 8 and matched_lines / len(expected_lines) >= 0.8:
            return True
    return False

def accepts_args(candidate, args, kwargs=None):
    try:
        inspect.signature(candidate).bind(*args, **(kwargs or {}))
        return True
    except Exception:
        return False

def is_user_function(namespace, name, candidate):
    if name.startswith("__"):
        return False
    if inspect.isclass(candidate) or inspect.ismodule(candidate):
        return False
    if not callable(candidate):
        return False
    return inspect.isfunction(candidate) and getattr(candidate, "__globals__", None) is namespace

def find_callable(namespace, function_names, args, required_name=None, kwargs=None):
    names = [required_name] if required_name else function_names
    for name in names:
        candidate = namespace.get(name)
        if callable(candidate) and accepts_args(candidate, args, kwargs):
            return name, candidate
    if required_name:
        return None, None
    fallback_matches = []
    for name, candidate in namespace.items():
        if name in function_names:
            continue
        if not is_user_function(namespace, name, candidate):
            continue
        if accepts_args(candidate, args, kwargs):
            fallback_matches.append((name, candidate))
    if len(fallback_matches) == 1:
        return fallback_matches[0]
    return None, None

def run_grader(source, grader):
    compare = grader.get("compare", "exact")
    tests = grader.get("tests", [])
    if grader.get("mode") == "script":
        with tempfile.TemporaryDirectory() as temp_dir:
            old_cwd = os.getcwd()
            try:
                os.chdir(temp_dir)
                last_solution = ""
                for solution in runnable_variants(source, prefer_markers=True):
                    last_solution = solution
                    if not source_requirements_ok(solution, grader):
                        continue
                    with time_limit(1.0):
                        if run_script_tests(solution, tests, compare):
                            return True, "", solution
                return False, "grader mismatch", last_solution
            finally:
                os.chdir(old_cwd)
    last_error = ""
    last_solution = ""
    for solution in runnable_variants(source):
        for candidate_solution in declaration_variants(solution):
            if not source_requirements_ok(candidate_solution, grader):
                continue
            namespace = {"__name__": "__main__", "re": re, "math": math, "json": json}
            old_stdout = sys.stdout
            old_input = builtins.input
            with tempfile.TemporaryDirectory() as temp_dir:
                old_cwd = os.getcwd()
                try:
                    os.chdir(temp_dir)
                    sys.stdout = io.StringIO()
                    try:
                        with time_limit(1.0):
                            exec(compile(candidate_solution, "<solution>", "exec"), namespace)
                    except BaseException as exc:
                        last_error = f"solution setup raised {type(exc).__name__}: {exc}"
                        last_solution = candidate_solution
                        continue
                    finally:
                        sys.stdout = old_stdout
                    try:
                        with time_limit(1.0):
                            if run_function_tests(namespace, grader, tests, compare):
                                return True, "", candidate_solution
                            last_error = "grader mismatch"
                            last_solution = candidate_solution
                    except BaseException as exc:
                        last_error = f"grader raised {type(exc).__name__}: {exc}"
                        last_solution = candidate_solution
                        continue
                finally:
                    os.chdir(old_cwd)
                    sys.stdout = old_stdout
                    builtins.input = old_input
    return False, last_error, last_solution

def run_script_tests(solution, tests, compare):
    compiled = compile(solution, "<solution>", "exec")
    for index, case in enumerate(tests, start=1):
        expected = case.get("expected")
        if has_hardcoded_expected_output(solution, expected):
            return False
        input_values = iter(list(case.get("inputValues", [])))
        old_stdout = sys.stdout
        old_input = builtins.input
        old_open = builtins.open
        old_cwd = os.getcwd()
        old_random = {}
        sys.stdout = io.StringIO()
        builtins.input = lambda prompt='': next(input_values)
        denied = set(case.get("permissionDeniedPaths", []))
        def guarded_open(file, *args, **kwargs):
            if str(file) in denied:
                raise PermissionError("Permission denied")
            return old_open(file, *args, **kwargs)
        try:
            setup_case(case)
            install_random(case, old_random)
            if denied:
                builtins.open = guarded_open
            exec(compiled, {"__name__": "__main__", "re": re, "math": math, "json": json})
            printed = sys.stdout.getvalue().strip()
        except BaseException as exc:
            return False
        finally:
            restore_random(old_random)
            os.chdir(old_cwd)
            sys.stdout = old_stdout
            builtins.input = old_input
            builtins.open = old_open
        if not same(printed, expected, compare):
            return False
    return True

def setup_case(case):
    for path_name in case.get("setupRemove", []):
        if os.path.islink(path_name) or os.path.isfile(path_name):
            os.remove(path_name)
        elif os.path.isdir(path_name):
            shutil.rmtree(path_name)
    for dir_name in case.get("setupDirs", []):
        os.makedirs(dir_name, exist_ok=True)
    for file_name, file_content in case.get("setupFiles", {}).items():
        dir_name = os.path.dirname(file_name)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(file_name, "w", encoding="utf-8") as setup_file:
            setup_file.write(file_content)
    for link_name, target_name in case.get("setupSymlinks", {}).items():
        dir_name = os.path.dirname(link_name)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        if os.path.lexists(link_name):
            os.remove(link_name)
        os.symlink(target_name, link_name)

def install_random(case, old_random):
    for name in ("randint", "randrange", "random", "uniform", "choice", "sample", "shuffle", "choices"):
        old_random[name] = getattr(random, name)
    values = iter(case.get("randomValues", []))
    float_values = iter(case.get("randomFloatValues", []))
    choice_values = iter(case.get("randomChoiceValues", []))
    sample_values = iter(case.get("randomSampleValues", []))
    shuffle_values = iter(case.get("randomShuffleValues", []))
    if case.get("randomValues"):
        fallback = case["randomValues"][-1]
        random.randint = lambda _start, _end: next(values, fallback)
        random.randrange = lambda *_args: random.randint(0, 0)
    if case.get("randomFloatValues"):
        fallback = case["randomFloatValues"][-1]
        random.random = lambda: next(float_values, fallback)
        random.uniform = lambda _start, _end: random.random()
    if case.get("randomChoiceValues"):
        fallback = case["randomChoiceValues"][-1]
        random.choice = lambda _items: next(choice_values, fallback)
        random.choices = lambda _items, *args, **kwargs: [next(choice_values, fallback) for _ in range(kwargs.get("k", 1))]
    if case.get("randomSampleValues"):
        fallback = case["randomSampleValues"][-1]
        random.sample = lambda _items, _count: list(next(sample_values, fallback))
    if case.get("randomShuffleValues"):
        fallback = case["randomShuffleValues"][-1]
        def shuffle(items):
            items[:] = list(next(shuffle_values, fallback))
        random.shuffle = shuffle

def restore_random(old_random):
    for name, method in old_random.items():
        setattr(random, name, method)

def run_function_tests(namespace, grader, tests, compare):
    function_names = grader.get("functionNames", [])
    first_args = tests[0].get("args", []) if tests else []
    first_kwargs = tests[0].get("kwargs", {}) if tests else {}
    if tests and tests[0].get("argFunctionNames"):
        first_args = first_args + [None] * len(tests[0].get("argFunctionNames", []))
    if tests and tests[0].get("argExpressions"):
        first_args = first_args + [None] * len(tests[0].get("argExpressions", []))
    if tests and tests[0].get("functionListArgNames"):
        first_args = [None] + first_args
    target_name, target = find_callable(namespace, function_names, first_args, kwargs=first_kwargs)
    if target is None:
        return False
    for index, case in enumerate(tests, start=1):
        args = list(case.get("args", []))
        kwargs = case.get("kwargs", {})
        expected = case.get("expected")
        required_name = case.get("functionName")
        if case.get("functionListArgNames") is not None:
            args = [[namespace[name] for name in case.get("functionListArgNames")]] + args
        for name in case.get("argFunctionNames", []):
            args.append(namespace[name])
        for expression in case.get("argExpressions", []):
            args.append(eval(expression, namespace))
        case_target_name, case_target = target_name, target
        if required_name:
            case_target_name, case_target = find_callable(namespace, function_names, args, required_name, kwargs)
            if case_target is None:
                return False
        old_stdout = sys.stdout
        old_input = builtins.input
        old_open = builtins.open
        old_cwd = os.getcwd()
        sys.stdout = io.StringIO()
        input_iter = iter(case.get("inputValues", []))
        builtins.input = lambda prompt='': next(input_iter)
        denied = set(case.get("permissionDeniedPaths", []))
        def guarded_open(file, *open_args, **open_kwargs):
            if str(file) in denied:
                raise PermissionError("Permission denied")
            return old_open(file, *open_args, **open_kwargs)
        try:
            setup_case(case)
            if denied:
                builtins.open = guarded_open
            returned = case_target(*args, **kwargs)
            if case.get("callReturnedWith") is not None:
                returned = returned(*case.get("callReturnedWith"))
            for attr_name, attr_value in case.get("setAttrs", {}).items():
                setattr(returned, attr_name, attr_value)
            for attr_name in case.get("deleteAttrs", []):
                delattr(returned, attr_name)
            for item_spec in case.get("setItems", []):
                returned[item_spec.get("key")] = item_spec.get("value")
            for item_key in case.get("deleteItems", []):
                del returned[item_key]
            if case.get("callMethod") is not None:
                method = getattr(returned, case.get("callMethod"))
                method_args = list(case.get("callMethodArgs", []))
                for expression in case.get("callMethodArgExpressions", []):
                    method_args.append(eval(expression, namespace))
                returned = method(*method_args)
            if case.get("getAttrs") is not None:
                returned = {name: getattr(returned, name, None) for name in case.get("getAttrs")}
            if case.get("getFiles") is not None:
                returned = {}
                for file_name in case.get("getFiles"):
                    try:
                        with open(file_name, "r", encoding="utf-8") as result_file:
                            returned[file_name] = result_file.read()
                    except FileNotFoundError:
                        returned[file_name] = None
            printed = sys.stdout.getvalue().strip()
        except BaseException as exc:
            if case.get("expectedException") == type(exc).__name__:
                continue
            return False
        finally:
            os.chdir(old_cwd)
            sys.stdout = old_stdout
            builtins.input = old_input
            builtins.open = old_open
        if case.get("expectedException"):
            return False
        returned_ok = same(returned, expected, compare)
        printed_ok = bool(printed) and same(printed, expected, compare)
        if not printed_ok and returned is None:
            printed_ok = bool(printed) and same(printed, expected, "printedOrReturn")
        if not returned_ok and not printed_ok:
            return False
    return True

results = []
for exercise in payload["exercises"]:
    grader = payload["graders"].get(str(exercise["id"]))
    if not grader:
        continue
    try:
        passed, error, selected = run_grader(exercise.get("solution", ""), grader)
    except BaseException as exc:
        passed, error, selected = False, f"validator raised {type(exc).__name__}: {exc}", ""
    results.append({
        "id": exercise["id"],
        "passed": bool(passed),
        "error": error,
        "selectedLines": len(selected.splitlines()) if selected else 0
    })

print(json.dumps(results))
`;

const payload = JSON.stringify({ exercises: EXERCISES, graders: AUTO_GRADERS });
const result = spawnSync('python3', ['-c', validator], {
  input: payload,
  encoding: 'utf8',
  maxBuffer: 1024 * 1024 * 20,
  timeout: 300000,
});

if (result.error) {
  throw result.error;
}

if (result.status !== 0) {
  process.stderr.write(result.stderr);
  process.exit(result.status);
}

const results = JSON.parse(result.stdout);
const failures = results.filter(item => !item.passed);
const maxFailuresArg = process.argv.find(arg => arg.startsWith('--max-failures='));
const maxFailures = maxFailuresArg ? Number(maxFailuresArg.split('=')[1]) : 0;

if (!Number.isFinite(maxFailures)) {
  console.error(`Invalid --max-failures value: ${maxFailuresArg}`);
  process.exit(1);
}

console.log(`Validated ${results.length} exercise solutions against graders.`);
console.log(`Passed: ${results.length - failures.length}`);
console.log(`Failed: ${failures.length}`);

if (failures.length) {
  console.log('First failures:');
  for (const failure of failures.slice(0, 80)) {
    console.log(`${failure.id}: ${failure.error || 'grader mismatch'} (${failure.selectedLines} selected lines)`);
  }
  if (failures.length > maxFailures) {
    console.error(`Validation failed: ${failures.length} failures exceeds max ${maxFailures}.`);
    process.exitCode = 1;
  } else {
    console.log(`Validation failure baseline accepted: ${failures.length}/${maxFailures}.`);
  }
}
