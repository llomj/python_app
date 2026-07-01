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

def is_simple_case(case):
    special_keys = {
        "inputValues", "setupRemove", "setupDirs", "setupFiles", "setupSymlinks",
        "permissionDeniedPaths", "getFiles", "randomValues", "randomFloatValues",
        "randomChoiceValues", "randomSampleValues", "randomShuffleValues",
        "callReturnedWith", "callMethod", "callMethodArgs", "callMethodArgExpressions",
        "getAttrs", "setAttrs", "deleteAttrs", "setItems", "deleteItems",
        "argExpressions", "argFunctionNames", "functionListArgNames",
        "expectedException", "kwargs", "functionName"
    }
    return not any(case.get(key) for key in special_keys)

def is_generated_input_case(case):
    if case.get("args", []) != []:
        return False
    if not case.get("inputValues"):
        return False
    special_keys = {
        "setupRemove", "setupDirs", "setupFiles", "setupSymlinks",
        "permissionDeniedPaths", "getFiles", "randomValues", "randomFloatValues",
        "randomChoiceValues", "randomSampleValues", "randomShuffleValues",
        "callReturnedWith", "callMethod", "callMethodArgs", "callMethodArgExpressions",
        "getAttrs", "setAttrs", "deleteAttrs", "setItems", "deleteItems",
        "argExpressions", "argFunctionNames", "functionListArgNames",
        "expectedException", "kwargs", "functionName"
    }
    return not any(case.get(key) for key in special_keys)

def input_generated_cases(function_names, tests):
    if not tests or not all(is_generated_input_case(case) for case in tests):
        return []
    name_set = set(function_names)
    first_inputs = tests[0].get("inputValues", [])
    first_expected = tests[0].get("expected")
    cases = []
    def add(input_values, expected, label):
        cases.append({"args": [], "inputValues": input_values, "expected": expected, "label": label})

    if "area_rectangle" in name_set and len(first_inputs) == 2:
        add(["7", "2"], "14.0", "generated input: rectangle area")
        add(["3.5", "2"], "7.0", "generated input: decimal rectangle area")
    elif "even_odd" in name_set:
        add(["12"], "Number is even", "generated input: even number")
        add(["13"], "Number is odd", "generated input: odd number")
    elif "fibonacci_series" in name_set:
        add(["7"], "0 1 1 2 3 5", "generated input: fibonacci series")
    elif name_set & {"max_number", "max_of_three", "max_of_list"}:
        add(["5 -1 0"], "5", "generated input: maximum with negatives")
    elif "is_palindrome" in name_set:
        add(["level"], True, "generated input: palindrome true")
        add(["python"], False, "generated input: palindrome false")
    elif "count_vowels" in name_set:
        add(["Education"], "5", "generated input: vowel count")
        add(["rhythm"], "0", "generated input: no vowels")
    elif "factorial" in name_set:
        add(["6"], "720", "generated input: factorial")
        add(["1"], "1", "generated input: factorial one")
    elif "sum_of_all_numbers" in name_set:
        if first_inputs and isinstance(first_inputs[0], str) and " " in first_inputs[0]:
            add(["1 2 -3"], "0", "generated input: list sum")
        else:
            add(["4"], "10", "generated input: range sum")
    elif "is_leap_year" in name_set:
        add(["2400"], True, "generated input: leap year century")
        add(["2100"], False, "generated input: non-leap century")
    elif "length_string" in name_set:
        add(["hello world"], "11", "generated input: string length")
    elif name_set & {"are_anagrams", "pal"}:
        add(["triangle", "integral"], True, "generated input: anagram true")
        add(["python", "typhonx"], False, "generated input: anagram false")
    elif "decimal_to_binary" in name_set:
        add(["6"], "110", "generated input: binary conversion")
    elif "square_root" in name_set:
        add(["25"], "5", "generated input: square root")
    elif name_set & {"digits_string", "sum_digits"}:
        if first_inputs and isinstance(first_inputs[0], str) and " " in first_inputs[0]:
            add(["4 5 6"], "15", "generated input: spaced digit sum")
        else:
            add(["1234"], "10", "generated input: digit sum")
    elif name_set & {"sum_of_odd_numbers", "sum_of_all_odd", "sum_of_odd"}:
        add(["10 15 20 25"], "40", "generated input: odd sum")
        add(["2 4"], "0", "generated input: no odd numbers")
    elif name_set & {"remove_duplicates", "remove_duplicate"} and isinstance(first_expected, list):
        add(["mississippi"], ["m", "i", "s", "p"], "generated input: unique characters")
    elif "int_str" in name_set:
        add(["7 8 9"], ["7", "8", "9"], "generated input: string split")
    elif name_set & {"type_smallest_biggest", "small_big"}:
        add(["3 -2 10"], [-2, 3, 10], "generated input: numeric sort")
    elif name_set & {"common", "intersection"}:
        add(["red blue green", "green red gold"], ["red", "green"], "generated input: intersection")
    elif name_set & {"find_last_element", "find_second_last_element"}:
        add(["red blue green"], "blue", "generated input: second last item")
    elif "third_largest" in name_set:
        add(["9 1 5 7"], "5", "generated input: third largest")
    elif name_set & {"find_min", "find_min_num"}:
        add(["5 2 9 -1"], "-1", "generated input: minimum")
    elif "largest_element" in name_set:
        add(["cat elephant dog"], "elephant", "generated input: longest word")
    elif "second_largest_element" in name_set:
        add(["cat elephant zebra dog"], "zebra", "generated input: second longest word")
    elif "centimeters_inches" in name_set:
        add(["20"], [7.873, 7.875], "generated input: centimeters to inches")
    elif "find_min_max" in name_set:
        add(["5 -1 0"], [-1, 5], "generated input: min max")
    elif "remove_vowels" in name_set:
        add(["Beautiful"], "Btfl", "generated input: remove vowels")
    elif "group_by_first_letter" in name_set:
        add(["ant ape bee"], "{'a': ['ant', 'ape'], 'b': ['bee']}", "generated input: group words")
    elif "second_largest_number" in name_set:
        if isinstance(first_expected, str) and "Not enough" in first_expected:
            add(["9 9 2 5"], "5", "generated input: second largest unique")
            add(["4 4"], "Not enough unique numbers", "generated input: insufficient unique numbers")
        else:
            add(["9 1 5 7"], "7", "generated input: second largest")
    elif "greet" in name_set:
        add(["Ada"], "Hello, Ada!", "generated input: greeting")
    elif "count_occurrences" in name_set:
        add(["abracadabra", "a"], "The character 'a' occurs 5 times.", "generated input: character count")
        add(["banana", "aa"], "Please enter exactly one character.", "generated input: invalid character count")
    return cases

def metamorphic_cases(function_names, tests):
    if not tests or not all(is_simple_case(case) for case in tests):
        return []
    first_args = tests[0].get("args", [])
    name_set = set(function_names)
    first_expected = tests[0].get("expected")
    if len(first_args) == 2:
        left, right = first_args
        if name_set & {"add_numbers", "add_number", "add_num"} and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in [left, right]):
            return [([7, -2], 5), ([1.5, 2.25], 3.75)]
        if "merge_lists" in name_set and isinstance(left, list) and isinstance(right, list):
            return [([[1, 4], [2, 3]], [1, 2, 3, 4]), ([[], [2]], [2])]
        if "sum_of_2_lst" in name_set and isinstance(left, list) and isinstance(right, list):
            return [([[1, 2], [3, 4]], [4, 6]), ([[-1, 5], [1, -2]], [0, 3])]
        if name_set & {"maxium_element_wise", "maximum_element_wise"} and isinstance(left, list) and isinstance(right, list):
            return [([[1, 5], [2, 4]], [2, 5]), ([[10, -1], [3, 9]], [10, 9])]
        if "euclidean_distance" in name_set and isinstance(left, list) and isinstance(right, list):
            return [([[0, 0], [6, 8]], 10), ([[3, 4], [6, 8]], 5)]
        if "is_anagram" in name_set and isinstance(left, str) and isinstance(right, str):
            return [(["Listen", "Silent"], True), (["hello", "world"], False)]
        if "common_char" in name_set and isinstance(left, str) and isinstance(right, str):
            return [(["abc", "bcd"], ["b", "c"]), (["abc", "xyz"], [])]
        if "common_keys_max_values" in name_set and isinstance(left, dict) and isinstance(right, dict):
            return [([{"a": 1, "b": 5}, {"b": 3, "c": 2}], {"b": 5}), ([{"x": 1}, {"y": 2}], {})]
        if "gcd" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([48, 18], 6), ([17, 13], 1)]
        if "calculate_gcd" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([84, 30], 6), ([17, 13], 1)]
        if "lcm" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([12, 18], 36), ([5, 7], 35)]
        if "sum_of_squares" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in [left, right]):
            return [([3, 4], 25), ([1, 2], 5)]
        if "sum_of_primes" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([1, 20], 77), ([20, 30], 52)]
        if name_set & {"calculate_sum", "sum_of_two"} and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in [left, right]):
            return [([7, -2], 5), ([1.5, 2.25], 3.75)]
        if "sort_dicts_by_key" in name_set and isinstance(left, list) and isinstance(right, str):
            return [([[{"name": "B", "score": 2}, {"name": "A", "score": 5}], "name"], [{"name": "A", "score": 5}, {"name": "B", "score": 2}])]
        if "length_of_value" in name_set and isinstance(left, list) and isinstance(right, str):
            return [([[{"code": "zz"}, {"code": "a"}, {"code": "mmmm"}], "code"], [{"code": "a"}, {"code": "zz"}, {"code": "mmmm"}])]
        if "find_person" in name_set and isinstance(left, list) and isinstance(right, str):
            return [([[{"name": "Ann"}, {"name": "Christopher"}], "name"], {"name": "Christopher"})]
        if "longest_string_letter" in name_set and isinstance(left, list) and isinstance(right, str):
            return [([["sun", "moon", "star"], "n"], "moon"), ([["apple", "grape", "date"], "e"], "apple")]
        if "count_floating_numbers" in name_set and isinstance(left, list):
            return [([[1.1, 1.1, 2.2], 1.1], 2), ([[1, 2, 3], 4], 0)]
        if "calculate_integers" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in [left, right]):
            return [([8, 4], [32, 12, 2]), ([7, 2], [14, 9, 3.5])]
        if "calculate_percentage" in name_set and isinstance(left, list) and isinstance(right, (int, float)) and not isinstance(right, bool):
            return [([[40, 80, 100], 200], [20, 40, 50]), ([[3, 6], 12], [25, 50])]
        if "example_function" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in [left, right]):
            return [([2, 9], "The sum of 2 and 9 is 11"), ([-3, 5], "The sum of -3 and 5 is 2")]
        return []
    if len(first_args) == 3:
        if "max_of_three" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([10, 25, 15], 25), ([-10, -2, -5], -2)]
        if "find_minimum" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([10, -2, 5], -2), ([3, 3, 8], 3)]
        return []
    if len(first_args) != 1:
        return []
    sample = first_args[0]
    if name_set & {"calculate_square", "cal_square"} and isinstance(sample, (int, float)) and not isinstance(sample, bool):
        return [([7], 49), ([-3], 9)]
    if "is_even" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([12], True), ([13], False)]
    if "is_odd" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([12], False), ([13], True)]
    if "reverse_string" in name_set and isinstance(sample, str):
        return [(["abc def"], "fed cba"), (["Python"], "nohtyP")]
    if "reverse" in name_set and isinstance(sample, str):
        return [(["abc def"], "fed cba"), ([""], "")]
    if name_set & {"reverse_words", "reverse_word"} and isinstance(sample, str):
        return [(["one two three"], "three two one"), (["solo"], "solo")]
    if "remove_vowels" in name_set and isinstance(sample, str):
        return [(["Beautiful"], "Btfl"), (["rhythm"], "rhythm")]
    if "find_vowels" in name_set and isinstance(sample, str):
        return [(["Python"], ["o"]), (["AEIOUxyz"], ["A", "E", "I", "O", "U"])]
    if "count_vowels" in name_set and isinstance(sample, str):
        if isinstance(first_expected, dict):
            return [
                (["AEIOUxyz"], {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}),
                (["rhythm"], {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0})
            ]
        return [(["AEIOUxyz"], 5), (["rhythm"], 0)]
    if (name_set & {"find_max", "find_min", "find_minimum", "calculate_sum", "cal_sum", "sum_of_list"}) and isinstance(sample, list):
        if "find_max" in name_set:
            return [([[9, -2, 4]], 9), ([[0]], 0)]
        if name_set & {"find_min", "find_minimum"}:
            return [([[9, -2, 4]], -2), ([[0]], 0)]
        if name_set & {"calculate_sum", "cal_sum", "sum_of_list"}:
            return [([[9, -2, 4]], 11), ([[]], 0)]
    if "find_min_max" in name_set and isinstance(sample, list):
        return [([[5, -2, 10]], [-2, 10]), ([[7]], [7, 7])]
    if "l_s" in name_set and isinstance(sample, list):
        return [([[5, -1, 0]], [5, -1]), ([[7]], [7, 7])]
    if name_set & {"largest_smallest", "smallest_largest", "smallest_biggest"} and isinstance(sample, list):
        if isinstance(first_expected, list) and len(first_expected) == len(sample):
            expected_desc = first_expected == sorted(first_expected, reverse=True)
            return [([[5, -1, 0]], [5, 0, -1] if expected_desc else [-1, 0, 5])]
        if isinstance(first_expected, list) and len(first_expected) == 2:
            return [([[5, -1, 0]], [-1, 5]), ([[7]], [7, 7])]
    if "seconded_largest_number" in name_set and isinstance(sample, list):
        return [([[10, 5, 8, 3, 12]], 10), ([[7, 7, 3]], 7)]
    if "fourth_largest_number" in name_set and isinstance(sample, list):
        return [([[10, 5, 8, 3, 12, 7]], 7)]
    if "smallest_and_third" in name_set and isinstance(sample, list):
        return [([[5, 9, 2, 7, 11, 3]], [2, 7])]
    if name_set & {"calculate_average", "cal_average", "find_average", "find_average_lst"} and isinstance(sample, list):
        return [([[2, 4, 9]], 5), ([[-2, 2, 6]], 2)]
    if "average" in name_set and isinstance(sample, list):
        return [([[2, 4, 9]], 5), ([[]], 0)]
    if name_set & {"square_list", "square_lst", "square_elements"} and isinstance(sample, list):
        return [([[3, -2, 0]], [9, 4, 0]), ([[]], [])]
    if name_set & {"square_numbers"} and isinstance(sample, list):
        return [([[3, -2, 0]], [9, 4, 0]), ([[]], [])]
    if "square_roots" in name_set and isinstance(sample, list):
        return [([[4, 9, 16]], [2, 3, 4]), ([[1, 25]], [1, 5])]
    if name_set & {"ascending_order_numbers", "sort_list", "sort_lst"} and isinstance(sample, list):
        return [([[5, -1, 0]], [-1, 0, 5]), ([[]], [])]
    if "big_small" in name_set and isinstance(sample, list):
        return [([["4", "10", "2"]], ["10", "4", "2"])]
    if name_set & {"reverse_list", "reverse_lst"} and isinstance(sample, list):
        return [([[1, 2, 3, 4]], [4, 3, 2, 1]), ([["a", "b"]], ["b", "a"])]
    if "reverse_strings" in name_set and isinstance(sample, list):
        return [([["hello", "ab"]], ["olleh", "ba"])]
    if "strip_whitespace" in name_set and isinstance(sample, list):
        return [([["  a", "b  "]], ["a", "b"])]
    if "number_and_square" in name_set and isinstance(sample, list):
        return [([[3, -2, 0]], [[3, 9], [-2, 4], [0, 0]])]
    if name_set & {"remove_duplicates", "remove_duplicate"} and isinstance(sample, list):
        if any("case_insensitive" in name for name in name_set):
            return [([["Apple", "apple", "BANANA", "banana", "Cherry"]], ["Apple", "BANANA", "Cherry"])]
        return [([[3, 1, 3, 2, 1]], [3, 1, 2]), ([["a", "b", "a"]], ["a", "b"])]
    if "has_duplicates" in name_set and isinstance(sample, list):
        return [([[1, 2, 1]], True), ([[1, 2, 3]], False)]
    if "filter_even_numbers" in name_set and isinstance(sample, list):
        return [([[1, 2, 3, 4]], [1, 3]), ([[2, 4]], [])]
    if "filter_odd_numbers" in name_set and isinstance(sample, list):
        if isinstance(first_expected, list) and all(isinstance(value, int) and value % 2 != 0 for value in first_expected):
            return [([[1, 2, 3, 4]], [1, 3]), ([[2, 4, 7]], [7])]
        return [([[1, 2, 3, 4]], [2, 4]), ([[1, 3]], [])]
    if "filter_palindromes" in name_set and isinstance(sample, list):
        return [([["madam", "hello", "noon"]], ["madam", "noon"])]
    if "filter_prime" in name_set and isinstance(sample, list):
        return [([[1, 2, 3, 4, 5]], [2, 3, 5])]
    if "sum_odd_indexed_elements" in name_set and isinstance(sample, list):
        return [([[1, 2, 3, 4, 5, 6]], 12), ([[10, 20, 30]], 20)]
    if "sort_tuples_by_second" in name_set and isinstance(sample, list):
        return [([[["a", 3], ["b", 1], ["c", 2]]], [["b", 1], ["c", 2], ["a", 3]])]
    if "lst_of_tuples" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and all(isinstance(value, list) for value in first_expected):
        return [([[[4, "x"], [-1, "y"], [-3, "z"]]], [[-1, "y"], [-3, "z"], [4, "x"]])]
    if "earliest_date" in name_set and isinstance(sample, list):
        return [([["2025-05-01", "2024-12-31", "2025-01-01"]], "2024-12-31")]
    if "sort_dates" in name_set and isinstance(sample, list):
        return [([["2025-05-01", "2024-12-31", "2025-01-01"]], ["2024-12-31", "2025-01-01", "2025-05-01"])]
    if "sort_strings_alphabetically" in name_set and isinstance(sample, list):
        return [([["zebra", "Ant", "bee"]], ["Ant", "bee", "zebra"])]
    if "lst_tuples" in name_set and isinstance(sample, list) and isinstance(first_expected, list):
        return [([[[2, 1], [1, 9], [1, 2]]], [[1, 2], [1, 9], [2, 1]])]
    if "lst_of_numbers" in name_set and isinstance(sample, list) and isinstance(first_expected, list):
        return [([[9, 8, 9, 7, 7, 7]], [8, 9, 9, 7, 7, 7])]
    if "lst_names" in name_set and isinstance(sample, list):
        return [([["Charlotte", "Al", "Zoe"]], ["Al", "Zoe", "Charlotte"])]
    if "temperture" in name_set and isinstance(sample, list):
        return [([[12, -5, 30]], [-5, 12, 30])]
    if "last_letter" in name_set and isinstance(sample, list):
        return [([["dog", "banana", "apple"]], ["banana", "apple", "dog"])]
    if "sort_by_hire_date" in name_set and isinstance(sample, list):
        return [([ [["Nia", "2024-01-05"], ["Oli", "2020-09-10"], ["Paz", "2022-03-01"]] ], [["Oli", "2020-09-10"], ["Paz", "2022-03-01"], ["Nia", "2024-01-05"]])]
    if "lst_of_sentences" in name_set and isinstance(sample, list):
        return [([["tiny", "a much longer line", "medium text"]], ["tiny", "medium text", "a much longer line"])]
    if "frequency_first_letter" in name_set and isinstance(sample, list):
        return [([["ape", "ant", "bee", "cat", "cow"]], ["bee", "ape", "ant", "cat", "cow"])]
    if "reverse_order" in name_set and isinstance(sample, list):
        return []
    if "sort_scores" in name_set and isinstance(sample, list):
        return [([[12, -7, 0, 5]], [-7, 0, 5, 12])]
    if "sort_emails" in name_set and isinstance(sample, list):
        return [([["z@beta.com", "a@alpha.com", "m@gamma.com"]], ["a@alpha.com", "z@beta.com", "m@gamma.com"])]
    if name_set & {"sort_cities_by_population", "sort_students_by_grades", "sort_books_by_year"} and isinstance(sample, list):
        return [([ [["High", 99], ["Low", 10], ["Mid", 50]] ], [["Low", 10], ["Mid", 50], ["High", 99]])]
    if "sort_movies_by_release_date" in name_set and isinstance(sample, list):
        return [([[{"title": "Late", "release_date": "2025"}, {"title": "Early", "release_date": "1995"}, {"title": "Middle", "release_date": "2010"}]], [{"title": "Early", "release_date": "1995"}, {"title": "Middle", "release_date": "2010"}, {"title": "Late", "release_date": "2025"}])]
    if "sort_sentences_by_unique_words" in name_set and isinstance(sample, list):
        return [([["red red red", "red blue", "red blue green"]], ["red red red", "red blue", "red blue green"])]
    if "lst_words" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and first_expected == [str(value)[::-1] for value in sample]:
        return [([["codex", "AI"]], ["xedoc", "IA"])]
    if "lst_integers" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and all(value in ("Even", "Odd") for value in first_expected):
        return [([[10, -3, 0]], ["Even", "Odd", "Even"])]
    if "negate_booleans" in name_set and isinstance(sample, list):
        return [([[True, True, False]], [False, False, True])]
    if "lst_sentence" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and all(isinstance(value, str) for value in first_expected):
        if any(" " in str(value) for value in sample):
            return [([["a b", " spaced text "]], ["ab", "spacedtext"])]
        return [([["codex", "pYTHON"]], ["Codex", "Python"])]
    if "factorial_lst" in name_set and isinstance(sample, list):
        return [([[0, 4, 6]], [1, 24, 720])]
    if "reverse_words_in_sentences" in name_set and isinstance(sample, list):
        return [([["codex app", "learn python"]], ["xedoc ppa", "nrael nohtyp"])]
    if "square_floats" in name_set and isinstance(sample, list):
        return [([[1.5, -3.0, 0]], [2.25, 9.0, 0])]
    if "lst_squares_and_cubes" in name_set and isinstance(sample, list):
        return [([[-3, 4]], [[9, -27], [16, 64]])]
    if "calculate_square_roots" in name_set and isinstance(sample, list):
        return [([[36, 49, 81]], [6, 7, 9])]
    if name_set & {"remove_spaces", "remove_space"} and isinstance(sample, str):
        return [(["a b  c"], "abc"), ([" no spaces "], "nospaces")]
    if "vowels_consonates" in name_set and isinstance(sample, str):
        return [(["codex ai"], {"vowels": 4, "consonants": 3}), (["rhythm"], {"vowels": 0, "consonants": 6})]
    if "get_surname" in name_set and isinstance(sample, str):
        return [(["Ada Lovelace"], "Lovelace"), (["Grace Brewster Hopper"], "Hopper")]
    if "capitalize_words" in name_set and isinstance(sample, str):
        return [(["hello world"], "Hello World"), (["python code"], "Python Code")]
    if "capitalize_words" in name_set and isinstance(sample, list):
        return [([["alpha", "bETA"]], ["Alpha", "Beta"])]
    if "count_words" in name_set and isinstance(sample, str):
        if isinstance(first_expected, dict):
            return [(["One two one"], {"one": 2, "two": 1}), (["solo"], {"solo": 1})]
        return [(["one two  three"], 3), (["solo"], 1)]
    if "alphabetically_ordered" in name_set and isinstance(sample, str):
        return [(["banana apple cherry"], "apple banana cherry"), (["zebra cat dog"], "cat dog zebra")]
    if "correct" in name_set and isinstance(sample, str):
        return [(["Hello.World"], "Hello. World"), (["This  is ok"], "This is ok")]
    if name_set & {"remove_duplicates", "remove_duplicate"} and isinstance(sample, str):
        if isinstance(first_expected, str):
            return [(["banana"], "ban"), (["abc"], "abc")]
        if isinstance(first_expected, list) and " " in sample:
            sample_unique_words = []
            for word in sample.split():
                if word not in sample_unique_words:
                    sample_unique_words.append(word)
            if first_expected == sample_unique_words:
                return [(["hot cold hot warm cold"], ["hot", "cold", "warm"])]
            return [(["hot cold hot warm cold"], ["hot", "cold"])]
        if isinstance(first_expected, list):
            return [(["banana"], ["b", "a", "n"]), (["abc"], ["a", "b", "c"])]
    if "count_uppercase" in name_set and isinstance(sample, str):
        return [(["ABC xyz"], 3), (["none"], 0)]
    if "factorial" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([0], 1), ([6], 720)]
    if "factorial_while" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([0], 1), ([6], 720)]
    if "factorial_recursive" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([6], 720), ([3], 6)]
    if "is_palindrome" in name_set and isinstance(sample, str):
        return [(["racecar"], True), (["python"], False)]
    if "is_palindrome" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([12321], True), ([12345], False)]
    if "palindromes" in name_set and isinstance(sample, str):
        return [(["level"], True), (["python"], False)]
    if "is_prime" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([29], True), ([21], False)]
    if "prime_factors" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([84], [2, 2, 3, 7]), ([13], [13])]
    if "is_perfect_square" in name_set and "is_perfect_number" not in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([25], True), ([26], False)]
    if "is_perfect_number" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([28], True), ([12], False)]
    if "reverse_number" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([1200], 21), ([987], 789)]
    if "sum_of_digits" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([1234], 10), ([9001], 10)]
    if "is_armstrong" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([153], True), ([123], False)]
    if "fibonacci" in name_set and isinstance(sample, int) and isinstance(first_expected, list):
        return [([5], [0, 1, 1, 2, 3]), ([2], [0, 1])]
    if "fibonacci" in name_set and isinstance(sample, int) and isinstance(first_expected, int):
        return [([6], 8), ([8], 21)]
    if "fibonacci_sequence" in name_set and isinstance(sample, int):
        return [([6], "0\n1\n1\n2\n3\n5"), ([2], "0\n1")]
    if "sum_n" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([7], 28), ([1], 1)]
    if "print_reverse" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], "4\n3\n2\n1"), ([1], "1")]
    if "square_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], [0, 1, 4, 9]), ([1], [0])]
    if "fibonacci_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([8], [0, 1, 1, 2, 3, 5, 8]), ([1], [0, 1, 1])]
    if "even_number_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([8], [2, 4, 6, 8]), ([1], [])]
    if "square_even_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([8], [4, 16, 36, 64]), ([1], [])]
    if "prime_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], [2, 3, 5, 7]), ([1], [2])]
    if "factorial_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], [1, 2, 6, 24]), ([1], [1])]
    if "square_number_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], [1, 4, 9, 16]), ([1], [1])]
    if "even_fibonacci_generator" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], [0, 2, 8, 34]), ([1], [0])]
    if "check_even_odd" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([12], "Even"), ([13], "Odd")]
    if "prime_numbers_up_to_n" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([20], [2, 3, 5, 7, 11, 13, 17, 19]), ([2], [2])]
    if "even_and_greater_than_10" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([14], True), ([10], False)]
    if "is_perfect_square_and_armstrong" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([1], True), ([153], False), ([16], False)]
    if name_set & {"sum_even_indices", "all_odd_numbers"} and isinstance(sample, list):
        if "sum_even_indices" in name_set:
            return [([[10, 20, 30, 40, 50]], 90), ([[]], 0)]
        if "all_odd_numbers" in name_set:
            return [([[10, 15, 20, 25]], 40), ([[2, 4]], 0)]
    if "is_even_index_sum" in name_set and isinstance(sample, list):
        return [([[2, 1, 4]], True), ([[1, 10, 2]], False)]
    if name_set & {"largest_element", "max_in_list"} and isinstance(sample, list):
        return [([[5, -1, 0]], 5), ([[7]], 7)]
    if name_set & {"max_of_three", "max_of_list"} and isinstance(sample, list):
        return [([[5, -1, 0]], 5), ([[7]], 7)]
    if "sum_elements" in name_set and isinstance(sample, list):
        return [([[1, 2, 3]], 6), ([[]], 0)]
    if "list_sum" in name_set and isinstance(sample, list):
        return [([[1, 2, -3]], 0), ([[10]], 10)]
    if "sum_numbers" in name_set and isinstance(sample, list):
        return [([[1, 2, -3]], 0), ([[10]], 10)]
    if "get_middle_element" in name_set and isinstance(sample, list):
        return [([[9, 8, 7, 6, 5]], 7), ([[1, 2]], 2)]
    if "find_longest_word" in name_set and isinstance(sample, list):
        if isinstance(first_expected, int):
            return [([["cat", "elephant", "dog"]], 8), ([["a", "abc", "def"]], 3)]
        return [([["cat", "elephant", "dog"]], "elephant"), ([["a", "abc", "def"]], "abc")]
    if name_set & {"longest_word"} and isinstance(sample, list):
        return [([["cat", "elephant", "dog"]], "elephant"), ([["a", "abc", "def"]], "abc")]
    if "longest_string" in name_set and isinstance(sample, list):
        return [([["cat", "elephant", "dog"]], "elephant"), ([["aa", "bbb", "cc"]], "bbb")]
    if "min_len" in name_set and isinstance(sample, list):
        return [([["long", "to", "a"]], "a"), ([["bbb", "cc"]], "cc")]
    if "find_max_and_index" in name_set and isinstance(sample, list):
        return [([[10, 20, 30, 25]], [2, 30]), ([[5, 3, 9]], [2, 9])]
    if "max_value_key" in name_set and isinstance(sample, dict):
        return [([{"a": 1, "b": 5}], "b"), ([{}], None)]
    if "max_key" in name_set and isinstance(sample, dict):
        return [([{"2": "x", "10": "y", "3": "z"}], "10")]
    if "key_max" in name_set and isinstance(sample, dict):
        return [([{"alpha": 1, "zulu": 2, "mid": 3}], "zulu")]
    if "reverse_keys" in name_set and isinstance(sample, dict):
        return [([{"first": 1, "second": 2, "third": 3}], ["third", "second", "first"])]
    if (name_set & {"palindromic_keys", "palindrome_keys"}) and isinstance(sample, dict):
        return [([{"level": 1, "code": 2, "radar": 3}], ["level", "radar"])]
    if "merge_list_of_dicts" in name_set and isinstance(sample, list):
        return [([[{"a": 1}, {"a": 2, "b": 3}]], {"a": 2, "b": 3})]
    if "remove_duplicates_from_values" in name_set and isinstance(sample, dict):
        return [([{"a": [1, 1, 2], "b": ["x", "x"]}], {"a": [1, 2], "b": ["x"]})]
    if "average_values" in name_set and isinstance(sample, list):
        return [([[{"a": 2}, {"a": 4, "b": 10}]], {"a": 3, "b": 10})]
    if "average_values" in name_set and isinstance(sample, dict):
        return [([{"a": 2, "b": 4, "c": 9}], 5)]
    if name_set & {"average_of_list"} and isinstance(sample, list):
        return [([[2, 4, 9]], 5), ([[-2, 2, 6]], 2)]
    if "total" in name_set and isinstance(sample, list):
        return [([[2, -3, 4]], [3, -24]), ([[]], [0, 1])]
    if name_set & {"check_even"} and isinstance(sample, int) and not isinstance(sample, bool):
        return [([12], True), ([13], False)]
    if name_set & {"even_or_odd"} and isinstance(sample, int) and not isinstance(sample, bool):
        if isinstance(first_expected, str) and str(sample) in first_expected:
            return [([12], "12 is even"), ([13], "13 is odd")]
        return [([12], "Even"), ([13], "Odd")]
    if "check_prime" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([29], True), ([21], False)]
    if "calculate_factorial" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([0], 1), ([6], 720)]
    if "check_palindrome" in name_set and isinstance(sample, str):
        return [(["racecar"], True), (["python"], False)]
    if name_set & {"is_sorted", "check_sorted"} and isinstance(sample, list):
        return [([[1, 2, 3]], True), ([[1, 3, 2]], False)]
    if "min_max" in name_set and isinstance(sample, list):
        return [([[5, -2, 10]], [-2, 10]), ([[7]], [7, 7])]
    if "generate_squares" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], [1, 4, 9, 16]), ([1], [1])]
    if "calculate_square_root" in name_set and isinstance(sample, (int, float)) and not isinstance(sample, bool):
        return [([25], 5), ([2.25], 1.5)]
    if "perimeter_of_square" in name_set and isinstance(sample, (int, float)) and not isinstance(sample, bool):
        return [([7], 28), ([2.5], 10)]
    if "square_of_number" in name_set and isinstance(sample, (int, float)) and not isinstance(sample, bool):
        return [([7], 49), ([-3], 9)]
    if "closest_to_zero" in name_set and isinstance(sample, list):
        return [([[-8, -3, 5, 2]], 2), ([[4, -1, 9]], -1)]
    if "print_odd_index_elements" in name_set and isinstance(sample, list):
        return [([["a", "b", "c", "d"]], "b\nd"), ([["x", "y"]], "y")]
    if "index_element_if_vowel" in name_set and isinstance(sample, list):
        return [([["apple", "berry", "orange"]], [[0, "apple"], [2, "orange"]]), ([["egg", "fish"]], [[0, "egg"]])]
    if "print_index_squared" in name_set and isinstance(sample, list):
        return [([[2, -3]], "Index: 0, Squared: 4\nIndex: 1, Squared: 9")]
    if "replace_based_on_index" in name_set and isinstance(sample, list):
        return [([["a", "b", "c"]], ["Even", "Odd", "Even"]), ([[1, 2]], ["Even", "Odd"])]
    if "enumerate_lst" in name_set and isinstance(sample, list) and isinstance(first_expected, str) and "index" not in first_expected.lower():
        return [([["a", "b", "c", "d", "e"]], "0 a\n2 c\n4 e")]
    if name_set & {"sort_strings_by_length", "len_lst"} and isinstance(sample, list):
        return [([["aaaa", "b", "cc"]], ["b", "cc", "aaaa"])]
    if "sort_list_descending" in name_set and isinstance(sample, list):
        return [([[5, -1, 0]], [5, 0, -1]), ([[1, 2, 3]], [3, 2, 1])]
    if "sort_by_absolute_value" in name_set and isinstance(sample, list):
        return [([[-10, 1, -3, 2]], [1, 2, -3, -10])]
    if "sort_complex_numbers" in name_set and isinstance(sample, list):
        return [([[-3, 1, 2]], [1, 2, -3])]
    if "sort_fractions" in name_set and isinstance(sample, list):
        return [([[0.75, 0.125, 0.5]], [0.125, 0.5, 0.75])]
    if name_set & {"sort_tuples_by_sum", "sum_of_tuple"} and isinstance(sample, list):
        return [([[[5, 5], [1, 1], [3, 0]]], [[1, 1], [3, 0], [5, 5]])]
    if "sort_points_by_distance" in name_set and isinstance(sample, list):
        return [([[[3, 4], [0, 0], [1, 1]]], [[0, 0], [1, 1], [3, 4]])]
    if "sort_words_by_distinct_letters" in name_set and isinstance(sample, list):
        return [([["a", "ab", "abc"]], ["a", "ab", "abc"])]
    if name_set & {"sort_by_vowel_count", "sort_words_by_vowel_count"} and isinstance(sample, list):
        return [([["sky", "tree", "audio"]], ["sky", "tree", "audio"])]
    if name_set & {"sort_strings_by_last_character", "list_of_strings_lst"} and isinstance(sample, list):
        return [([["ab", "aa", "ac"]], ["aa", "ab", "ac"])]
    if "sort_number_uppercases" in name_set and isinstance(sample, list):
        return [([["ABC", "aB", "plain"]], ["plain", "aB", "ABC"])]
    if "find_highest_ascii_word" in name_set and isinstance(sample, list):
        return [([["aa", "bb", "cc", "uu"]], "uu")]
    if "filter_string" in name_set and isinstance(sample, list):
        return [([["a", "ab", "abc"]], ["abc"]), ([["one", "four", "two"]], ["one", "two"])]
    if "max_string_alpha" in name_set and isinstance(sample, list):
        return [([["zebra", "yak", "ant"]], "zebra")]
    if "reverse" in name_set and isinstance(sample, list):
        return [([[1, 2, 3, 4]], [4, 3, 2, 1]), ([["a", "b"]], ["b", "a"])]
    if "floating_point" in name_set and isinstance(sample, list):
        return [([[2.6, 1.2, 3.8]], [1.2, 2.6, 3.8])]
    if "first_element_decending_order" in name_set and isinstance(sample, list):
        return [([[[10, "a"], [5, "b"], [20, "c"]]], [[20, "c"], [10, "a"], [5, "b"]])]
    if "number_of_consonants" in name_set and isinstance(sample, list):
        if isinstance(first_expected, str):
            return [([["aeiou", "cat", "sky"]], "aeiou")]
        return [([["ai", "cat", "strength"]], ["ai", "cat", "strength"])]
    if "min_string" in name_set and isinstance(sample, list):
        return [([["long", "to", "a"]], "a"), ([["bbb", "cc"]], "cc")]
    if "main" in name_set and isinstance(sample, list):
        if isinstance(first_expected, list) and all(isinstance(value, int) for value in first_expected):
            return [([[10, 11, 12, 13], 3], [12, 10, 13, 11])]
    if "sort_by_year" in name_set and isinstance(sample, list):
        return [([["1999-12-31", "2024-01-01", "2001-06-15"]], ["1999-12-31", "2001-06-15", "2024-01-01"])]
    if "sort_by_a_count" in name_set and isinstance(sample, list):
        return [([["bbb", "atlas", "aardvark"]], ["bbb", "atlas", "aardvark"])]
    if "sort_by_first_element_desc" in name_set and isinstance(sample, list):
        return [([[[10, "a"], [5, "b"], [20, "c"]]], [[20, "c"], [10, "a"], [5, "b"]])]
    if "sort_by_length" in name_set and isinstance(sample, list):
        return [([["aaaa", "b", "cc"]], ["b", "cc", "aaaa"])]
    if "sum_of_elements" in name_set and isinstance(sample, list):
        return [([[10, -2, 5]], 13)]
    if "sum_of_even" in name_set and isinstance(sample, list):
        return [([[2, 8, 9]], 10), ([[1, 3]], 0)]
    if "create_square_root_tuples" in name_set and isinstance(sample, list):
        return [([[25, 36]], [[25, 5], [36, 6]])]
    if "average_of_odds" in name_set and isinstance(sample, list):
        return [([[1, 3, 8, 10]], 2), ([[2, 4, 9]], 9)]
    if "square_odd_numbers" in name_set and isinstance(sample, list):
        return [([[1, 2, 7]], [1, 49]), ([[2, 4]], [])]
    if "sum_of_cubes" in name_set and isinstance(sample, list):
        return [([[2, -3]], -19), ([[]], 0)]
    if "consecutive_pair_sum" in name_set and isinstance(sample, list):
        return [([[5, 1, 4]], [6, 5]), ([[9]], [])]
    if "odd_filter_generator" in name_set and isinstance(sample, list):
        return [([[1, 2, 8, 9]], [2, 8]), ([[1, 3]], [])]
    if "cumulative_sum_generator" in name_set and isinstance(sample, list):
        return [([[5, -2, 1]], [5, 3, 4])]
    if "reverse_list_generator" in name_set and isinstance(sample, list):
        return [([[1, 2, 3, 4]], [4, 3, 2, 1]), ([["a", "b"]], ["b", "a"])]
    if "sum_with_index_generator" in name_set and isinstance(sample, list):
        return [([[5, 5, 5]], [5, 6, 7])]
    if "palindrome_generator" in name_set and isinstance(sample, list):
        return [([["noon", "python", "madam"]], ["noon", "madam"])]
    if "even_index_generator" in name_set and isinstance(sample, list):
        return [([["a", "b", "c", "d"]], ["a", "c"])]
    if name_set & {"sort_sqaure", "sqaure_numbers_lst"} and isinstance(sample, list):
        return [([[-3, 2, -1]], [-1, 2, -3]), ([[0, -4, 1]], [0, 1, -4])]
    if "length_of_first_element" in name_set and isinstance(sample, list):
        return [([[["aa", 1], ["b", 2], ["cccc", 3]]], [["b", 2], ["aa", 1], ["cccc", 3]])]
    if "number_of_spaces" in name_set and isinstance(sample, list):
        return [([["two spaces here", "one space", "zero"]], ["zero", "one space", "two spaces here"])]
    if "most_vowels" in name_set and isinstance(sample, list):
        return [([["sky", "audio", "tree"]], "audio")]
    if "sort_lst_integers" in name_set and isinstance(sample, list):
        return [([[-10, 3, 200, -4]], [3, -4, -10, 200])]
    if "sort_tuples_by_difference" in name_set and isinstance(sample, list):
        return [([[[5, 5], [2, 8], [9, 7]]], [[5, 5], [9, 7], [2, 8]])]
    if "sort_strings_by_ascii" in name_set and isinstance(sample, list):
        return [([["zoo", "ant", "Dog"]], ["Dog", "ant", "zoo"])]
    if "sort_lists_by_sum" in name_set and isinstance(sample, list):
        return [([[[5], [1, 1, 1], [2, 2]]], [[1, 1, 1], [2, 2], [5]])]
    if "sort_files_by_extension" in name_set and isinstance(sample, list):
        return [([["a.zip", "b.csv", "c.txt"]], ["b.csv", "c.txt", "a.zip"])]
    if "sort_second_letter" in name_set and isinstance(sample, list):
        return [([["za", "ab", "cc"]], ["za", "ab", "cc"])]
    if name_set & {"people_age", "sort_people_by_age"} and isinstance(sample, list):
        return [([[{"name": "Old", "age": 80}, {"name": "Young", "age": 10}]], [{"name": "Young", "age": 10}, {"name": "Old", "age": 80}])]
    if "sort_by_binary_representation" in name_set and isinstance(sample, list):
        return [([[8, 5, 1]], [1, 8, 5])]
    if "sort_keys_by_value" in name_set and isinstance(sample, dict):
        return [([{"a": 3, "b": 1, "c": 2}], ["b", "c", "a"])]
    if (name_set & {"name_age", "sports_by_popularity"}) and isinstance(sample, dict):
        return [([{"middle": 50, "young": 5, "old": 90}], ["young", "middle", "old"])]
    if (name_set & {"sorted_students_grades", "movies", "sorted_movie_titles"}) and isinstance(sample, dict):
        return [([{"zeta": 1, "alpha": 2, "mid": 3}], ["alpha", "mid", "zeta"])]
    if "students_grades" in name_set and isinstance(sample, dict) and isinstance(first_expected, str):
        return [([{"zeta": 1, "alpha": 2, "mid": 3}], "alpha\nmid\nzeta")]
    if "colors_hex" in name_set and isinstance(sample, dict):
        return [([{"first": 1, "second": 2, "third": 3}], ["third", "second", "first"])]
    if "sort_dic" in name_set and isinstance(sample, dict):
        sorted_by_key = dict(sorted(sample.items(), key=lambda item: item[0]))
        if first_expected == sorted_by_key:
            return [([{"z": 1, "a": 2, "m": 3}], {"a": 2, "m": 3, "z": 1})]
        sorted_by_value_desc = dict(sorted(sample.items(), key=lambda item: item[1], reverse=True))
        if first_expected == sorted_by_value_desc:
            return [([{"low": 1, "high": 9, "mid": 5}], {"high": 9, "mid": 5, "low": 1})]
    if "remove_duplicates_values" in name_set and isinstance(sample, dict):
        return [([{"a": 1, "b": 2, "c": 1, "d": 3}], {"a": 1, "b": 2, "d": 3})]
    if "largest_value" in name_set and isinstance(sample, dict):
        return [([{"low": 1, "high": 9, "mid": 5}], "high")]
    if "smallest_value" in name_set and isinstance(sample, dict):
        return [([{"low": 1, "high": 9, "mid": 5}], "low")]
    if "sort_fractions_by_decimal" in name_set and isinstance(sample, list):
        return [([[10, 2, 6]], [2, 6, 10])]
    if "count_spaces" in name_set and isinstance(sample, str):
        return [(["hello world python"], 2), (["nospaces"], 0)]
    if "even_length_word_generator" in name_set and isinstance(sample, str):
        return [(["one four six seven"], ["four"]), (["to be or not"], ["to", "be", "or"])]
    if "fibonacci_up_to_n" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([8], "0 1 1 2 3 5 8"), ([1], "0 1 1")]
    if "get_middle_char" in name_set and isinstance(sample, str):
        return [(["abcde"], "c"), (["abcdef"], "d")]
    if "get_first_word" in name_set and isinstance(sample, str):
        return [(["alpha beta gamma"], "alpha")]
    if "get_last_word" in name_set and isinstance(sample, str):
        return [(["alpha beta gamma"], "gamma")]
    if "count_characters" in name_set and isinstance(sample, str) and isinstance(first_expected, int):
        return [(["a b c"], 3), ([" spaced text "], 10)]
    if "filters_even_numbers" in name_set and isinstance(sample, list):
        return [([[1, 3, 8, 10]], [8, 10])]
    if "palindromes" in name_set and isinstance(sample, list):
        return [([["noon", "python", "madam"]], ["noon", "madam"])]
    if "sum_of_lst" in name_set and isinstance(sample, list):
        if first_expected == math.prod(sample):
            return [([[2, 5, 3]], 30)]
        return [([[-2, 5, 7]], 10)]
    if "capitalize_string" in name_set and isinstance(sample, list):
        return [([["python", "CODE"]], ["Python", "Code"])]
    if "number_lst" in name_set and isinstance(sample, list):
        return [([[9, -2, 4]], -2)]
    if "lst_numbers" in name_set and isinstance(sample, list) and isinstance(first_expected, (int, float)) and not isinstance(first_expected, bool):
        return [([[2, 4]], 20)]
    if "apply_lsts" in name_set and isinstance(sample, list):
        return [([[2, 3, 6]], [9])]
    if "sum_nested_list" in name_set and isinstance(sample, list):
        return [([[[10], [-2, 3]]], 11)]
    if "fibonacci_n_numbers" in name_set and isinstance(sample, int):
        return [([6], [0, 1, 1, 2, 3, 5]), ([3], [0, 1, 1])]
    if "lst_string" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and all(isinstance(value, int) for value in first_expected):
        return [([["aei", "sky"]], [3, 0])]
    if "sum_even_numbers" in name_set and isinstance(sample, list):
        return [([[2, 8, 9]], 10)]
    if "lst_num" in name_set and isinstance(sample, list):
        return [([[5, -2, 1]], [5, 3, 4])]
    if "filter_primes" in name_set and isinstance(sample, list):
        return [([[8, 9, 10, 11, 12, 13]], [11, 13])]
    if "sort_string_len" in name_set and isinstance(sample, list):
        return [([["aa", "b", "cccc"]], ["b", "aa", "cccc"])]
    if "lst_tuples_second" in name_set and isinstance(sample, list):
        return [([[[1, 3], [2, 1], [3, 2]]], [[2, 1], [3, 2], [1, 3]])]
    if "sort_last_names" in name_set and isinstance(sample, list):
        return [([["Ada Lovelace", "Grace Hopper"]], ["Grace Hopper", "Ada Lovelace"])]
    if "sort_ignore_case" in name_set and isinstance(sample, list):
        return [([["Zoo", "ant", "Bee"]], ["ant", "Bee", "Zoo"])]
    if "list_floats" in name_set and isinstance(sample, list):
        return [([[0.5, -1.2, 2]], [2, 0.5, -1.2])]
    if "lst_words" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and first_expected == sorted(sample, key=lambda word: sum(1 for char in str(word).lower() if char in "aeiou")):
        return [([["sky", "tree", "audio"]], ["sky", "tree", "audio"])]
    if "lst_integers" in name_set and isinstance(sample, list) and isinstance(first_expected, list) and first_expected == sorted(sample, key=lambda value: sum(int(digit) for digit in str(abs(value)))):
        return [([[5666, 566, 56, 6]], [6, 56, 566, 5666])]
    if "lst_products" in name_set and isinstance(sample, list):
        return [([[{"name": "X", "price": 3}, {"name": "Y", "price": 1}]], [{"name": "Y", "price": 1}, {"name": "X", "price": 3}])]
    return []

def named_metamorphic_cases(function_names, tests):
    if not tests:
        return []
    normalized_cases = []
    for case in tests:
        if not case.get("functionName"):
            return []
        simple_copy = {key: value for key, value in case.items() if key != "functionName"}
        if not is_simple_case(simple_copy):
            return []
        normalized_cases.append(case)
    name_set = set(function_names)
    cases = []
    def add(function_name, args, expected):
        if function_name in name_set:
            cases.append({"functionName": function_name, "args": args, "expected": expected, "label": "generated helper metamorphic"})
    if name_set >= {"sum_list", "add"}:
        add("sum_list", [[10, -3, 5]], 12)
        add("add", [-4, 9], 5)
    if name_set >= {"is_even", "filter_even_numbers"}:
        add("filter_even_numbers", [[0, 1, 8, 9, 10]], [0, 8, 10])
        add("is_even", [12], True)
    if name_set >= {"word_list", "capitalize_first_letter"}:
        add("word_list", [["alpha", "bETA"]], ["Alpha", "Beta"])
        add("capitalize_first_letter", ["codex"], "Codex")
    if name_set >= {"lst_numbers", "find_max"}:
        add("lst_numbers", [[-9, -2, -5]], -2)
        add("find_max", [[3, 99, 1]], 99)
    if name_set >= {"string_lst", "reverse_string"}:
        add("string_lst", [["codex", "app"]], ["xedoc", "ppa"])
        add("reverse_string", ["level"], "level")
    if name_set >= {"lst_words", "count_vowels"}:
        add("lst_words", [["sky", "queue", "tree"]], "queue")
        add("count_vowels", ["rhythm"], 0)
    if name_set >= {"lst_of_word", "is_palindrome"}:
        add("lst_of_word", [["noon", "code", "radar"]], ["noon", "radar"])
        add("is_palindrome", ["level"], True)
    if name_set >= {"lst_numbers", "sqaure_number"}:
        add("lst_numbers", [[-3, 0, 4]], [9, 0, 16])
        add("sqaure_number", [-5], 25)
    if name_set >= {"find_gcd", "gcd_of_pairs"}:
        add("find_gcd", [84, 30], 6)
        add("gcd_of_pairs", [[[21, 14], [17, 13]]], [7, 1])
    if name_set >= {"lst_words", "sort_lst"}:
        add("lst_words", [[3, 1, 2], ["b", "a"]], [[1, 2, 3], ["a", "b"]])
        add("sort_lst", [["z", "a", "m"]], ["a", "m", "z"])
    if name_set >= {"lst_sites", "remove_duplicates"}:
        add("lst_sites", [["x", "y", "x", "z"]], ["x", "y", "z"])
        add("remove_duplicates", [[3, 3, 2, 1, 2]], [3, 2, 1])
    if name_set >= {"filter_primes", "is_prime"}:
        add("filter_primes", [[0, 1, 2, 13, 15]], [2, 13])
        add("is_prime", [13], True)
    if name_set >= {"lst_of_numbers", "calculate_factorial"}:
        add("lst_of_numbers", [[0, 3, 6]], [1, 6, 720])
        add("calculate_factorial", [0], 1)
    if name_set >= {"sort_dict_by_value", "get_value"}:
        add("sort_dict_by_value", [{"b": 2, "a": 1, "c": 3}], {"a": 1, "b": 2, "c": 3})
        add("get_value", [["name", 42]], 42)
    if name_set >= {"main", "generate_fibonacci"}:
        add("generate_fibonacci", [5], [0, 1, 1, 2, 3])
        add("main", [4], [0, 1, 1, 2])
    if name_set >= {"main", "calculate_average"}:
        add("calculate_average", [[2, 4, 9]], 5)
        add("main", [[2, 4], [10, 20, 30]], [3, 20])
    if name_set >= {"main", "remove_whitespace"}:
        add("remove_whitespace", [" a b c "], "abc")
        add("main", [" spaced text "], "spacedtext")
    if name_set >= {"main", "check_even_odd"}:
        add("main", [[0, 1, 2]], ["Even", "Odd", "Even"])
        add("check_even_odd", [9], "Odd")
    if name_set >= {"main", "sum_of_list"}:
        add("main", [[-2, 5, 7]], 10)
        add("sum_of_list", [[]], 0)
    if name_set >= {"main", "merge_sorted_lists"}:
        add("merge_sorted_lists", [[5, 1], [4, 2]], [1, 2, 4, 5])
        add("main", [[10, 0], [5, -1]], [-1, 0, 5, 10])
    if name_set >= {"main", "get_even_numbers"}:
        add("main", [[0, 1, 8, 9, 10]], [0, 8, 10])
        add("get_even_numbers", [12], True)
    if name_set >= {"main", "sort_values", "sort_key"}:
        add("main", [{"low": 1, "high": 9, "mid": 5}], {"low": 1, "mid": 5, "high": 9})
        add("sort_key", [["item", 42]], 42)
    if name_set >= {"main", "square_odd_number_generator"}:
        add("main", [6], [1, 9, 25])
        add("square_odd_number_generator", [9], [1, 9, 25, 49, 81])
    return cases

def run_metamorphic_tests(target, function_names, tests, compare):
    for args, expected in metamorphic_cases(function_names, tests):
        if not accepts_args(target, args):
            continue
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            returned = target(*args)
            printed = sys.stdout.getvalue().strip()
        except BaseException:
            return False
        finally:
            sys.stdout = old_stdout
        returned_ok = same(returned, expected, compare)
        printed_ok = bool(printed) and same(printed, expected, compare)
        if not printed_ok and returned is None:
            printed_ok = bool(printed) and same(printed, expected, "printedOrReturn")
        if not returned_ok and not printed_ok:
            return False
    return True

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
    if source_requirements_ok(source, grader):
        for solution in runnable_variants(source):
            last_solution = solution
            try:
                with time_limit(1.0):
                    if run_function_script_tests(solution, grader, tests, compare):
                        return True, "", solution
                last_error = "grader mismatch"
            except BaseException as exc:
                last_error = f"script fallback raised {type(exc).__name__}: {exc}"
                continue
    return False, last_error, last_solution

def function_script_test_cases(function_names, tests):
    cases = list(tests) + input_generated_cases(function_names, tests)
    cases += named_metamorphic_cases(function_names, tests)
    for args, expected in metamorphic_cases(function_names, tests):
        cases.append({"args": args, "expected": expected, "label": "generated script fallback"})
    return cases

def is_function_script_case(case):
    blocked_keys = set()
    return not any(case.get(key) for key in blocked_keys)

def script_helper_function(name):
    if name == "add_one":
        return lambda value: value + 1
    if name == "multiply_by_two":
        return lambda value: value * 2
    if name == "example_func":
        return lambda index, value: index * value
    return None

def script_method_expression_args(expression):
    parsed = ast.parse(expression, mode="eval").body
    if not isinstance(parsed, ast.Call):
        raise ValueError("method expression must be a call")
    return [ast.literal_eval(arg) for arg in parsed.args]

def script_namespace_for_args(args, required_name=None, call_args=None, method_name=None, method_args=None, attr_names=None, kwargs=None, expression_args=None, get_files=None, helper_functions=None, set_attrs=None, delete_attrs=None, set_items=None, delete_items=None, method_expression_args=None):
    call_args = list(call_args or [])
    method_args = list(method_args or [])
    attr_names = list(attr_names or [])
    kwargs = dict(kwargs or {})
    expression_args = list(expression_args or [])
    get_files = list(get_files or [])
    helper_functions = dict(helper_functions or {})
    set_attrs = dict(set_attrs or {})
    delete_attrs = list(delete_attrs or [])
    set_items = list(set_items or [])
    delete_items = list(delete_items or [])
    method_expression_args = list(method_expression_args or [])
    namespace = {
        "__name__": "__main__",
        "re": re,
        "math": math,
        "json": json,
        "args": list(args),
        "arguments": list(args),
        "inputs": list(args),
        "call_args": call_args,
        "call_arguments": call_args,
        "method_name": method_name,
        "call_method": method_name,
        "method_args": method_args,
        "method_arguments": method_args,
        "attr_names": attr_names,
        "attribute_names": attr_names,
        "kwargs": kwargs,
        "keyword_args": kwargs,
        "keywords": kwargs,
        "kw": kwargs,
        "expression_args": expression_args,
        "expr_args": expression_args,
        "get_files": get_files,
        "file_names": get_files,
        "helper_functions": helper_functions,
        "helpers": helper_functions,
        "set_attrs": set_attrs,
        "delete_attrs": delete_attrs,
        "set_items": set_items,
        "delete_items": delete_items,
        "method_expression_args": method_expression_args,
        "method_expr_args": method_expression_args,
        "function_name": required_name,
        "required_function_name": required_name,
        "target_name": required_name,
    }
    for index, value in enumerate(args, start=1):
        namespace[f"arg{index}"] = value
    for name, value in zip(["a", "b", "c", "d", "x", "y", "z"], args):
        namespace[name] = value
    for index, value in enumerate(call_args, start=1):
        namespace[f"call_arg{index}"] = value
    for index, value in enumerate(method_args, start=1):
        namespace[f"method_arg{index}"] = value
    for index, value in enumerate(expression_args, start=1):
        namespace[f"expression_arg{index}"] = value
        namespace[f"expr_arg{index}"] = value
    if args:
        first = args[0]
        namespace.update({
            "n": first,
            "num": first,
            "number": first,
            "value": first,
            "item": first,
        })
        if isinstance(first, list):
            namespace.update({"lst": first, "list": first, "numbers": first, "items": first, "data": first})
        if isinstance(first, str):
            namespace.update({"s": first, "string": first, "text": first, "word": first})
        if isinstance(first, dict):
            namespace.update({"dct": first, "dict": first, "dictionary": first})
    if call_args:
        namespace.update({"call_value": call_args[0], "inner_value": call_args[0], "suffix": call_args[0]})
    if method_args:
        namespace.update({"method_value": method_args[0]})
    for key, value in kwargs.items():
        if isinstance(key, str) and key.isidentifier() and not key.startswith("__") and key not in namespace:
            namespace[key] = value
    for key, value in helper_functions.items():
        if isinstance(key, str) and key.isidentifier() and not key.startswith("__") and key not in namespace:
            namespace[key] = value
    return namespace

def read_case_files(file_names):
    files = {}
    for file_name in file_names:
        try:
            with open(file_name, "r", encoding="utf-8") as result_file:
                files[file_name] = result_file.read()
        except FileNotFoundError:
            files[file_name] = None
    return files

def script_result_matches(namespace, printed, expected, compare):
    if expected is None and not printed and not any(name in namespace for name in ["result", "answer", "output", "final", "res", "solution"]):
        return True
    if printed and (same(printed, expected, compare) or same(printed, expected, "printedOrReturn")):
        return True
    result_names = ["result", "answer", "output", "total", "count", "value", "final", "res", "solution"]
    for name in result_names:
        if name in namespace and (same(namespace[name], expected, compare) or same(namespace[name], expected, "printedOrReturn")):
            return True
    return False

def run_function_script_tests(solution, grader, tests, compare):
    function_names = grader.get("functionNames", [])
    test_cases = function_script_test_cases(function_names, tests)
    if not test_cases or not all(is_function_script_case(case) for case in test_cases):
        return False
    if all(case.get("expectedException") for case in test_cases):
        return False
    compiled = compile(solution, "<solution>", "exec")
    for case in test_cases:
        expected = case.get("expected")
        if has_hardcoded_expected_output(solution, expected):
            return False
        expected_exception = case.get("expectedException")
        args = list(case.get("args", []))
        expression_args = [eval(expression, {"math": math, "re": re, "json": json}) for expression in case.get("argExpressions", [])]
        args = args + expression_args
        helper_names = list(case.get("argFunctionNames", []))
        helper_functions = {name: script_helper_function(name) for name in helper_names}
        function_list_names = list(case.get("functionListArgNames", []))
        function_list = [script_helper_function(name) for name in function_list_names]
        if any(function is None for function in helper_functions.values()) or any(function is None for function in function_list):
            return False
        if function_list_names:
            args = [function_list] + args
        args = args + [helper_functions[name] for name in helper_names]
        call_args = list(case.get("callReturnedWith", []))
        method_name = case.get("callMethod")
        method_args = list(case.get("callMethodArgs", []))
        attr_names = list(case.get("getAttrs", []))
        kwargs = dict(case.get("kwargs", {}))
        get_files = list(case.get("getFiles", []))
        set_attrs = dict(case.get("setAttrs", {}))
        delete_attrs = list(case.get("deleteAttrs", []))
        set_items = list(case.get("setItems", []))
        delete_items = list(case.get("deleteItems", []))
        method_expression_args = [script_method_expression_args(expression) for expression in case.get("callMethodArgExpressions", [])]
        input_values = iter(list(case.get("inputValues", [])))
        old_stdout = sys.stdout
        old_input = builtins.input
        old_open = builtins.open
        old_cwd = os.getcwd()
        old_random = {}
        with tempfile.TemporaryDirectory() as temp_dir:
            sys.stdout = io.StringIO()
            printed = ""
            file_result = None
            exception_name = None
            builtins.input = lambda prompt='': next(input_values)
            denied = set(case.get("permissionDeniedPaths", []))
            def guarded_open(file, *open_args, **open_kwargs):
                if str(file) in denied:
                    raise PermissionError("Permission denied")
                return old_open(file, *open_args, **open_kwargs)
            try:
                os.chdir(temp_dir)
                setup_case(case)
                install_random(case, old_random)
                if denied:
                    builtins.open = guarded_open
                namespace = script_namespace_for_args(args, case.get("functionName"), call_args, method_name, method_args, attr_names, kwargs, expression_args, get_files, helper_functions, set_attrs, delete_attrs, set_items, delete_items, method_expression_args)
                exec(compiled, namespace)
                printed = sys.stdout.getvalue().strip()
                file_result = read_case_files(get_files) if get_files else None
            except BaseException as exc:
                printed = sys.stdout.getvalue().strip()
                exception_name = type(exc).__name__
            finally:
                restore_random(old_random)
                os.chdir(old_cwd)
                sys.stdout = old_stdout
                builtins.input = old_input
                builtins.open = old_open
        if expected_exception:
            if exception_name != expected_exception:
                return False
            continue
        if exception_name:
            return False
        file_ok = get_files and same(file_result, expected, compare)
        if not file_ok and not script_result_matches(namespace, printed, expected, compare):
            return False
    return True

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
    test_cases = list(tests) + input_generated_cases(function_names, tests) + named_metamorphic_cases(function_names, tests)
    for index, case in enumerate(test_cases, start=1):
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
    if not run_metamorphic_tests(target, function_names, tests, compare):
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
