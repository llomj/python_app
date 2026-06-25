import React, { useState, useEffect, useCallback, useRef, useMemo } from 'react';
import {
    Settings,
    Book,
    Lightbulb,
    Bot,
    CheckCircle,
    XCircle,
    RotateCcw,
    Play,
    SkipForward,
    Plus,
    Minus,
    Pencil,
    FileCode,
    AlertTriangle,
    Key,
    ExternalLink,
    Loader2,
    Trash2,
    Zap,
    Copy,
    Check,
    MousePointer2,
    ArrowUpRight,
    RefreshCw,
    Info,
    SlidersHorizontal,
    Volume2,
    Vibrate,
    X,
    ChevronDown,
    ChevronUp,
    Bookmark
} from 'lucide-react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { indentUnit } from '@codemirror/language';
import { autocompletion, snippetCompletion, CompletionContext, Completion } from '@codemirror/autocomplete';
import { EditorView } from '@codemirror/view';
import { EditorSelection } from '@codemirror/state';
import { EXERCISES } from './exercises';
import { Exercise, Stats } from './types';
import { getAiHint } from './services/geminiService';
import { customPythonTheme } from './editorTheme';
import { AUTO_GRADERS, AutoGrader } from './graders';

// Fixed: Removed local AIStudio interface definition as it conflicts with environment-provided types.

declare global {
    interface Window {
        __PYODIDE_INSTANCE__: any;
        __PYODIDE_INIT_LOCK__: boolean;
        loadPyodide: any;
        APP_VERSION?: string;
    }
}

interface ProjectFile {
    name: string;
    content: string;
}

interface AutoGradeResult {
    passed: boolean;
    message: string;
    functionName?: string;
}

type OutputStatus = 'idle' | 'running' | 'win' | 'fail' | 'info';
type DifficultyMode = 'normal' | 'beginner' | 'intermediate' | 'expert' | 'legend';
type StatsByMode = Record<DifficultyMode, Stats>;

const DIFFICULTY_MODES: Array<{ id: DifficultyMode; label: string; description: string }> = [
    { id: 'normal', label: 'Normal', description: 'All problems mixed' },
    { id: 'beginner', label: 'Beginner', description: 'Simple functions, strings, lists' },
    { id: 'intermediate', label: 'Intermediate', description: 'Loops, dictionaries, patterns' },
    { id: 'expert', label: 'Expert', description: 'Nested data, constraints, algorithms' },
    { id: 'legend', label: 'Legend', description: 'Recursion, OOP, files, advanced modules' }
];

const getDifficultyLabel = (mode: DifficultyMode) => DIFFICULTY_MODES.find(item => item.id === mode)?.label ?? 'Normal';

const getSavedDifficultyMode = (): DifficultyMode => {
    const savedMode = localStorage.getItem('python_difficulty_mode') as DifficultyMode | null;
    return savedMode && DIFFICULTY_MODES.some(mode => mode.id === savedMode) ? savedMode : 'normal';
};

const scoreExerciseDifficulty = (exercise: Exercise): number => {
    const text = `${exercise.title} ${exercise.description} ${exercise.initialCode} ${exercise.solution}`.toLowerCase();
    let score = 0;

    const addIf = (pattern: RegExp, value: number) => {
        if (pattern.test(text)) score += value;
    };

    addIf(/\b(add|sum|subtract|multiply|divide|square|cube|even|odd|positive|negative|uppercase|lowercase|capitalize|reverse string|greet|hello)\b/, -2);
    addIf(/\b(return their sum|returns their sum|two numbers|single number|one number|string as input|integer as input)\b/, -1);
    addIf(/\b(list|array|string|loop|for each|iterate|count|filter|map|sort|search)\b/, 2);
    addIf(/\b(dictionary|dict|set|tuple|key-value|frequency|histogram|group|unique|duplicate)\b/, 4);
    addIf(/\b(nested|matrix|2d|grid|list of lists|dictionary of|list of dictionaries|flatten|transpose)\b/, 6);
    addIf(/\b(recursion|recursive|memoization|dynamic programming|backtracking|permutation|combination|graph|tree|binary search|shortest path)\b/, 10);
    addIf(/\b(class|object|inheritance|polymorphism|encapsulation|dataclass|decorator|generator|yield|context manager|async|await|thread|subprocess)\b/, 9);
    addIf(/\b(file|csv|json|configparser|sqlite|database|api|request|beautifulsoup|pandas|numpy|regex|regular expression|re\.)\b/, 8);
    addIf(/\b(lambda|partial|reduce|zip\(|enumerate\(|comprehension)\b/, 4);
    addIf(/\b(without|do not use|don't use|no built[- ]?in|not use|constraint|efficient|optimize|performance|large)\b/, 4);
    addIf(/\b(pattern|pyramid|triangle|hourglass|checkerboard|hollow)\b/, 3);
    addIf(/\b(factorial|prime|fibonacci|gcd|lcm|palindrome|anagram|pangram)\b/, 3);

    const functionCount = (exercise.initialCode.match(/\bdef\s+/g) || []).length;
    const solutionLines = exercise.solution.split('\n').filter(line => line.trim()).length;
    const loopCount = (exercise.solution.match(/\b(for|while)\b/g) || []).length;
    const branchCount = (exercise.solution.match(/\b(if|elif|else)\b/g) || []).length;
    const importCount = (exercise.solution.match(/^\s*import\s+|^\s*from\s+/gm) || []).length;
    const classCount = (exercise.solution.match(/\bclass\s+/g) || []).length;

    score += Math.max(0, functionCount - 1) * 2;
    score += Math.min(10, Math.floor(solutionLines / 8));
    score += loopCount * 2;
    score += branchCount;
    score += importCount * 3;
    score += classCount * 8;
    if (exercise.description.length > 180) score += 2;
    if (exercise.description.length > 320) score += 3;

    return Math.max(0, score);
};

const deleteBackwardOnce = (view: EditorView) => {
    const changes = view.state.changeByRange((range) => {
        if (!range.empty) {
            return {
                changes: { from: range.from, to: range.to, insert: '' },
                range: EditorSelection.cursor(range.from)
            };
        }

        if (range.from === 0) {
            return { changes: [], range };
        }

        const previous = view.state.doc.lineAt(range.from).from === range.from ? range.from - 1 : range.from - 1;
        return {
            changes: { from: previous, to: range.from, insert: '' },
            range: EditorSelection.cursor(previous)
        };
    });

    if (!changes.changes.empty) {
        view.dispatch(changes, { scrollIntoView: true, userEvent: 'delete.backward' });
    }
};

const holdBackspaceExtension = EditorView.domEventHandlers({
    keydown(event, view) {
        if (event.key !== 'Backspace' || event.metaKey || event.ctrlKey || event.altKey) return false;
        const dom = view.dom as HTMLElement & { __backspaceHoldTimer?: number; __backspaceHoldDelay?: number };

        if (dom.__backspaceHoldDelay || dom.__backspaceHoldTimer) return false;

        dom.__backspaceHoldDelay = window.setTimeout(() => {
            deleteBackwardOnce(view);
            dom.__backspaceHoldTimer = window.setInterval(() => deleteBackwardOnce(view), 55);
        }, 260);

        return false;
    },
    keyup(event, view) {
        if (event.key !== 'Backspace') return false;
        const dom = view.dom as HTMLElement & { __backspaceHoldTimer?: number; __backspaceHoldDelay?: number };

        if (dom.__backspaceHoldDelay) {
            window.clearTimeout(dom.__backspaceHoldDelay);
            dom.__backspaceHoldDelay = undefined;
        }
        if (dom.__backspaceHoldTimer) {
            window.clearInterval(dom.__backspaceHoldTimer);
            dom.__backspaceHoldTimer = undefined;
        }

        return false;
    },
    blur(_event, view) {
        const dom = view.dom as HTMLElement & { __backspaceHoldTimer?: number; __backspaceHoldDelay?: number };

        if (dom.__backspaceHoldDelay) {
            window.clearTimeout(dom.__backspaceHoldDelay);
            dom.__backspaceHoldDelay = undefined;
        }
        if (dom.__backspaceHoldTimer) {
            window.clearInterval(dom.__backspaceHoldTimer);
            dom.__backspaceHoldTimer = undefined;
        }

        return false;
    }
});

const EMPTY_STATS: Stats = { shots: 0, success: 0, failed: 0 };

const createEmptyStatsByMode = (): StatsByMode => ({
    normal: { ...EMPTY_STATS },
    beginner: { ...EMPTY_STATS },
    intermediate: { ...EMPTY_STATS },
    expert: { ...EMPTY_STATS },
    legend: { ...EMPTY_STATS }
});

const isStats = (value: unknown): value is Stats => {
    const item = value as Stats;
    return Boolean(item && typeof item.shots === 'number' && typeof item.success === 'number' && typeof item.failed === 'number');
};

const loadStatsByMode = (): StatsByMode => {
    const emptyStats = createEmptyStatsByMode();
    const savedStats = localStorage.getItem('python_mastery_stats');
    if (!savedStats) return emptyStats;

    try {
        const parsed = JSON.parse(savedStats);
        if (isStats(parsed)) {
            return { ...emptyStats, normal: parsed };
        }

        const merged = { ...emptyStats };
        for (const mode of DIFFICULTY_MODES) {
            if (isStats(parsed?.[mode.id])) {
                merged[mode.id] = parsed[mode.id];
            }
        }
        return merged;
    } catch {
        return emptyStats;
    }
};

const classifyExerciseDifficulty = (exercise: Exercise): Exclude<DifficultyMode, 'normal'> => {
    const score = scoreExerciseDifficulty(exercise);

    if (score > 24) return 'legend';
    if (score > 13) return 'expert';
    if (score > 5) return 'intermediate';
    return 'beginner';
};

const getExerciseById = (id: number | null): Exercise | null => {
    if (!id) return null;
    return EXERCISES.find(item => item.id === id) ?? null;
};

const getExercisePoolForMode = (mode: DifficultyMode): Exercise[] => {
    if (mode === 'normal') return EXERCISES;
    const pool = EXERCISES.filter(item => classifyExerciseDifficulty(item) === mode);
    return pool.length > 0 ? pool : EXERCISES;
};

const getRandomExerciseForMode = (mode: DifficultyMode, excludeId?: number): Exercise => {
    const pool = getExercisePoolForMode(mode);
    const candidates = pool.length > 1 && excludeId ? pool.filter(item => item.id !== excludeId) : pool;
    return candidates[Math.floor(Math.random() * candidates.length)] ?? EXERCISES[0];
};

const getInitialExercise = (): Exercise => {
    const savedMode = getSavedDifficultyMode();
    const savedId = Number(localStorage.getItem('python_current_problem_id'));
    const savedExercise = getExerciseById(Number.isFinite(savedId) ? savedId : null);

    if (savedExercise && (savedMode === 'normal' || classifyExerciseDifficulty(savedExercise) === savedMode)) {
        return savedExercise;
    }

    return getRandomExerciseForMode(savedMode);
};

const buildAutoGradeScript = (grader: AutoGrader, sourceCode = '', sourceName = 'main.py') => `
import json
import math
import sys
import io
import builtins
import inspect
import re
import ast
import types

__auto_grader_spec = json.loads(${JSON.stringify(JSON.stringify(grader))})
__auto_grader_source = ${JSON.stringify(sourceCode)}
__auto_grader_source_name = ${JSON.stringify(sourceName)}

def __auto_grader_jsonable(value):
    try:
        json.dumps(value)
        return value
    except Exception:
        return repr(value)

def __auto_grader_normalize(value):
    if hasattr(value, "isoformat") and callable(value.isoformat):
        try:
            return value.isoformat()
        except Exception:
            pass
    if type(value).__name__ in ("dict_keys", "dict_values", "dict_items"):
        return [__auto_grader_normalize(item) for item in value]
    if hasattr(value, "__iter__") and hasattr(value, "__next__"):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, tuple):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, list):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, set):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): __auto_grader_normalize(item) for key, item in value.items()}
    return value

def __auto_grader_numbers(value):
    return [float(match) for match in re.findall(r"-?\\d+(?:\\.\\d+)?", str(value))]

def __auto_grader_maybe_literal(value):
    if not isinstance(value, str):
        return value
    text = value.strip()
    if not text:
        return value
    try:
        return ast.literal_eval(text)
    except Exception:
        return value

def __auto_grader_clean_text(value):
    return "\\n".join(line.rstrip() for line in str(value).strip().splitlines())

def __auto_grader_compact_pattern(value):
    return "\\n".join(re.sub(r"[ \\t]+", "", line) for line in __auto_grader_clean_text(value).splitlines())

def __auto_grader_same(actual, expected, compare):
    actual = __auto_grader_normalize(actual)
    expected = __auto_grader_normalize(expected)
    if isinstance(actual, str) and isinstance(expected, (list, dict, tuple, set)):
        actual = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
    if compare == "float":
        try:
            return math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-9)
        except Exception:
            return False
    if compare == "printedOrReturn":
        actual_text = __auto_grader_clean_text(actual)
        expected_text = __auto_grader_clean_text(expected)
        return (
            actual == expected
            or actual_text == expected_text
            or expected_text in actual_text
            or __auto_grader_compact_pattern(actual_text) == __auto_grader_compact_pattern(expected_text)
        )
    if compare == "numberRange":
        numbers = __auto_grader_numbers(actual)
        if not numbers or not isinstance(expected, list) or len(expected) != 2:
            return False
        value = numbers[-1]
        return float(expected[0]) <= value <= float(expected[1])
    if compare == "length":
        try:
            return len(str(actual)) == int(expected)
        except Exception:
            return False
    if compare == "unorderedList":
        try:
            actual = __auto_grader_maybe_literal(actual)
            expected = __auto_grader_maybe_literal(expected)
            return sorted(list(actual)) == sorted(list(expected))
        except Exception:
            return False
    if compare == "unorderedWords":
        try:
            actual = __auto_grader_maybe_literal(actual)
            expected = __auto_grader_maybe_literal(expected)
            if isinstance(actual, str):
                actual = actual.split()
            if isinstance(expected, str):
                expected = expected.split()
            return sorted(list(actual)) == sorted(list(expected))
        except Exception:
            return False
    if compare == "numberList":
        try:
            actual_numbers = __auto_grader_numbers(actual)
            expected_numbers = [float(item) for item in expected]
            return actual_numbers == expected_numbers
        except Exception:
            return False
    if compare == "dictUnorderedLists":
        actual = __auto_grader_maybe_literal(actual)
        expected = __auto_grader_maybe_literal(expected)
        if not isinstance(actual, dict) or not isinstance(expected, dict):
            return False
        if set(actual.keys()) != set(expected.keys()):
            return False
        try:
            for key in expected:
                if sorted(list(actual[key])) != sorted(list(expected[key])):
                    return False
            return True
        except Exception:
            return False
    if compare == "letterCounts":
        if isinstance(actual, dict):
            upper = actual.get("upper", actual.get("uppercase"))
            lower = actual.get("lower", actual.get("lowercase"))
            return upper == expected.get("upper") and lower == expected.get("lower")
        if isinstance(actual, (list, tuple)) and len(actual) == 2:
            return list(actual) in ([expected.get("upper"), expected.get("lower")], [expected.get("lower"), expected.get("upper")])
        text = str(actual).lower()
        lower_match = re.search(r"lower\\D+(\\d+)", text)
        upper_match = re.search(r"upper\\D+(\\d+)", text)
        return bool(lower_match and upper_match and int(lower_match.group(1)) == expected.get("lower") and int(upper_match.group(1)) == expected.get("upper"))
    if compare == "vowelConsonantCounts":
        if isinstance(actual, dict):
            vowels = actual.get("vowels", actual.get("vowel"))
            consonants = actual.get("consonants", actual.get("consonant"))
            return vowels == expected.get("vowels") and consonants == expected.get("consonants")
        if isinstance(actual, (list, tuple)) and len(actual) == 2:
            return list(actual) == [expected.get("vowels"), expected.get("consonants")]
        text = str(actual).lower()
        vowel_match = re.search(r"vowels?\\D+(\\d+)", text)
        consonant_match = re.search(r"consonants?\\D+(\\d+)", text)
        return bool(vowel_match and consonant_match and int(vowel_match.group(1)) == expected.get("vowels") and int(consonant_match.group(1)) == expected.get("consonants"))
    return actual == expected

def __auto_grader_accepts_args(candidate, args):
    try:
        inspect.signature(candidate).bind(*args)
        return True
    except Exception:
        return False

def __auto_grader_find_callable(function_names, args, required_name=None):
    names = [required_name] if required_name else function_names
    for name in names:
        candidate = globals().get(name)
        if callable(candidate) and __auto_grader_accepts_args(candidate, args):
            return name, candidate
    return None, None

def __auto_grader_run():
    if __auto_grader_spec.get("mode") == "script":
        return __auto_grader_run_script()

    function_names = __auto_grader_spec.get("functionNames", [])
    compare = __auto_grader_spec.get("compare", "exact")
    tests = __auto_grader_spec.get("tests", [])
    first_args = tests[0].get("args", []) if tests else []
    if tests and tests[0].get("argFunctionNames"):
        first_args = first_args + [None] * len(tests[0].get("argFunctionNames", []))
    if tests and tests[0].get("functionListArgNames"):
        first_args = [None] + first_args
    target_name, target = __auto_grader_find_callable(function_names, first_args)

    if target is None:
        return {
            "passed": False,
            "message": "Missing function. Expected one of: " + ", ".join(function_names)
        }

    for index, case in enumerate(__auto_grader_spec.get("tests", []), start=1):
        args = case.get("args", [])
        arg_function_names = case.get("argFunctionNames", [])
        function_list_arg_names = case.get("functionListArgNames")
        expected = case.get("expected")
        call_returned_with = case.get("callReturnedWith")
        call_method = case.get("callMethod")
        call_method_args = case.get("callMethodArgs", [])
        get_attrs = case.get("getAttrs")
        expected_exception = case.get("expectedException")
        input_values = list(case.get("inputValues", []))
        label = case.get("label") or ("test " + str(index))
        required_name = case.get("functionName")
        case_target_name = target_name
        case_target = target
        resolved_args = list(args)
        if function_list_arg_names is not None:
            function_list = []
            for function_name in function_list_arg_names:
                function = globals().get(function_name)
                if not callable(function):
                    return {
                        "passed": False,
                        "functionName": case_target_name,
                        "message": f"{label} missing helper function {function_name}()."
                    }
                function_list.append(function)
            resolved_args = [function_list] + resolved_args
        for arg_function_name in arg_function_names:
            arg_function = globals().get(arg_function_name)
            if not callable(arg_function):
                return {
                    "passed": False,
                    "functionName": case_target_name,
                    "message": f"{label} missing helper function {arg_function_name}()."
                }
            resolved_args.append(arg_function)
        if required_name:
            case_target_name, case_target = __auto_grader_find_callable(function_names, resolved_args, required_name)
            if case_target is None:
                return {
                    "passed": False,
                    "message": f"{label} missing required function {required_name}()."
                }
        old_stdout = sys.stdout
        old_input = builtins.input
        sys.stdout = io.StringIO()
        input_iter = iter(input_values)
        builtins.input = lambda prompt='': next(input_iter)
        try:
            returned = case_target(*resolved_args)
            if call_returned_with is not None:
                if not callable(returned):
                    return {
                        "passed": False,
                        "functionName": case_target_name,
                        "message": f"{label} expected {case_target_name}() to return a callable function."
                    }
                returned = returned(*call_returned_with)
            if call_method is not None:
                method = getattr(returned, call_method, None)
                if not callable(method):
                    return {
                        "passed": False,
                        "functionName": case_target_name,
                        "message": f"{label} expected returned object to have method {call_method}()."
                    }
                returned = method(*call_method_args)
            if get_attrs is not None:
                returned = {name: getattr(returned, name, None) for name in get_attrs}
            printed = sys.stdout.getvalue().strip()
        except Exception as exc:
            if expected_exception and type(exc).__name__ == expected_exception:
                continue
            return {
                "passed": False,
                "functionName": case_target_name,
                "message": f"{label} raised {type(exc).__name__}: {exc}"
            }
        finally:
            sys.stdout = old_stdout
            builtins.input = old_input

        if expected_exception:
            return {
                "passed": False,
                "functionName": case_target_name,
                "message": f"{label} expected {expected_exception} to be raised."
            }

        returned_ok = __auto_grader_same(returned, expected, compare)
        printed_ok = bool(printed) and __auto_grader_same(printed, expected, compare)
        if not printed_ok and compare == "printedOrReturn":
            printed_ok = __auto_grader_same(printed, expected, "printedOrReturn")
        if not returned_ok and not printed_ok:
            actual = printed if printed else returned
            return {
                "passed": False,
                "functionName": case_target_name,
                "message": (
                    f"{label} failed for args={args}. "
                    f"Expected {expected!r}, got {__auto_grader_jsonable(actual)!r}."
                )
            }

    return {
        "passed": True,
        "functionName": target_name,
        "message": f"All {len(__auto_grader_spec.get('tests', []))} tests passed using {target_name}()."
    }

def __auto_grader_run_script():
    compare = __auto_grader_spec.get("compare", "printedOrReturn")
    tests = __auto_grader_spec.get("tests", [])
    compiled = compile(__auto_grader_source, __auto_grader_source_name, "exec")

    for index, case in enumerate(tests, start=1):
        expected = case.get("expected")
        input_values = list(case.get("inputValues", []))
        random_values = list(case.get("randomValues", []))
        label = case.get("label") or ("test " + str(index))

        old_stdout = sys.stdout
        old_input = builtins.input
        old_random = None
        sys.stdout = io.StringIO()
        input_iter = iter(input_values)
        random_iter = iter(random_values)

        def __script_input(prompt=""):
            try:
                return next(input_iter)
            except StopIteration:
                raise Exception("No test input left for input().")

        builtins.input = __script_input
        try:
            import random
            old_random = random.randint
            if random_values:
                def __script_randint(_start, _end):
                    try:
                        return next(random_iter)
                    except StopIteration:
                        return random_values[-1]
                random.randint = __script_randint

            namespace = {"__name__": "__main__"}
            exec(compiled, namespace)
            printed = sys.stdout.getvalue().strip()
        except Exception as exc:
            return {
                "passed": False,
                "message": f"{label} raised {type(exc).__name__}: {exc}"
            }
        finally:
            if old_random is not None:
                try:
                    import random
                    random.randint = old_random
                except Exception:
                    pass
            sys.stdout = old_stdout
            builtins.input = old_input

        if not __auto_grader_same(printed, expected, compare):
            return {
                "passed": False,
                "message": (
                    f"{label} failed. "
                    f"Expected output {expected!r}, got {__auto_grader_jsonable(printed)!r}."
                )
            }

    return {
        "passed": True,
        "message": f"All {len(tests)} script tests passed."
    }

__auto_grader_result = __auto_grader_run()
__auto_grader_json = json.dumps(__auto_grader_result)
`;

// CHEAT TAB - Python Examples Only
const CHEAT_CONTENT = `# Python Cheat Sheet - Templates & Examples
import collections
from collections import Counter
import datetime
from functools import reduce
import math
import os
from pathlib import Path
import random
import string
import re
import time
from urllib.parse import parse_qs

# Dictionary Example
def main(dic):
    return len(dic)
    
dic = {"apple": 1, "orange": 33}
print(main(dic))

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Dictionary with target
def main(dic, target):
    return dic.get(target)

dic = {"apple": 1, "orange": 33, "mango": 5}
target = "orange"
main(dic, target)

# Two dictionaries
def main(dic1, dic2):
    return {**dic1, **dic2}

dic1 = {"apple": 1, "orange": 33}
dic2 = {"storm": 11, "sky": 36}
main(dic1, dic2)

# List of dictionaries
lst_dic = [
    {"name": "Jon", "age": 67},
    {"name": "mike", "age": 55},
    {"name": "dilly", "age": 23}
]

# Nested list
nested_lst = [[1,2,3], [4,5,6], [7,8,9]]

# List of tuples
lst_tuples = [(55,7), (2,4), (27,23)]

# Keyword arguments
def main(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

main(a=1, b=2, c="hot", d="cold")

# Helper function pattern
def helper(x):
    return x * 2

def main():
    result = helper(5)
    return result

main()
`;

// GLOSSARY TAB - Complete Python Glossary
const GLOSSARY_CONTENT = `#glossary python 
"""
PYTHON GLOSSARY - COMPREHENSIVE REFERENCE
==========================================

A
---

**all()** - all(iterable)
    Returns True if all elements in the iterable are truthy, otherwise False.
    Example: all([True, True, False]) returns False

**any()** - any(iterable)
    Returns True if any element in the iterable is truthy, otherwise False.
    Example: any([False, False, True]) returns True

**Argument**
    A value passed to a function or method when it is called. An argument can be an expression, 
    a value, or even another function call. Arguments are assigned to parameters when the function executes.

**Assert** - assert expression, message
    A debugging aid that tests a condition. If the condition is False, it raises an AssertionError 
    with an optional message. Used to catch programming errors early.

**Attribute**
    A value associated with an object. Attributes are accessed using dot notation (object.attribute).
    Can be data attributes (variables) or method attributes (functions).

B
---

**Built-in Function**
    Functions that are always available in Python without needing to import them.
    Examples: print(), len(), range(), type(), str(), int(), float(), list(), dict(), set(), tuple()

**Built-in Scope (B in LEGB)**
    The outermost scope containing Python's built-in names (like print, len, etc.).
    Always checked last in the LEGB lookup order.

C
---

**Class** - Class_name: attribute
    A blueprint for creating objects. Defines attributes and methods that all instances of the class will have.
    Example: class Person: pass

**Class Object** - obj = ClassName()
    An instance of a class. Created by calling the class like a function.
    Example: person = Person() creates a Person object

**Closure**
    A function that has access to variables from its enclosing (outer) scope even after the outer 
    function has finished executing. Closures "remember" the environment in which they were created.

**Comprehension**
    A concise way to create collections (lists, dictionaries, sets) using a single expression.
    1. List comprehension: [expression for item in iterable if condition]
    2. Dictionary comprehension: {key: value for item in iterable if condition}
    3. Set comprehension: {value for item in iterable if condition}
    4. Generator expression: (expression for variable in iterable)

**Constant**
    A variable that is intended not to be changed after its initial assignment. 
    In Python, constants are typically written in UPPER_CASE by convention (though not enforced).

**Constructor**
    A special method (__init__) that is automatically called when an object is created.
    Used to initialize the object's attributes.

D
---

**Decorator**
    A function that modifies or extends the behavior of another function without permanently modifying it.
    Applied using the @decorator_name syntax above a function definition.

**Dictionary (dict)**
    An unordered, mutable collection of key-value pairs. Keys must be hashable (immutable).
    Example: {"name": "Alice", "age": 30}

**Docstring**
    A string literal that appears as the first statement in a function, class, or module.
    Used to document code and accessible via the __doc__ attribute.

E
---

**Enclosing Scope (E in LEGB)**
    The scope of an outer function that contains a nested function. Variables from the enclosing 
    scope are accessible to the inner function, forming closures.

**Enclosing Variable**
    A variable defined in an outer (enclosing) function that is accessible to an inner function.
    Part of how closures work in Python.

**Exception**
    An error that occurs during program execution. Can be caught and handled using try/except blocks.
    Examples: ValueError, TypeError, IndexError, KeyError, AttributeError

**Expression**
    A piece of code that evaluates to a value. Can be a simple value, a variable, or a combination 
    of operators and values. Examples: 2 + 2, name = "Sam", len([1, 2, 3])

F
---

**Filter** - filter(function, iterable)
    Returns an iterator containing only the elements from the iterable for which the function 
    returns True. Example: filter(lambda x: x > 0, [-1, 0, 1, 2]) returns [1, 2]

**Function**
    A block of code that performs a specific task. Defined using the def keyword.
    Can accept parameters and return values. Syntax: function_name(arguments)

**Function Call**
    The act of executing a function by using its name followed by parentheses.
    Example: print("Hello") calls the print function

G
---

**Generator**
    A special type of iterator that generates values on-the-fly using the yield keyword.
    More memory-efficient than lists for large sequences. Created using generator functions or expressions.

**Generator Expression**
    A compact way to create a generator. Syntax: (expression for variable in iterable)
    Similar to list comprehension but uses parentheses and returns a generator object.

**Global Variable**
    A variable defined outside of any function, accessible from anywhere in the program.
    To modify a global variable inside a function, use the global keyword.

**Global Scope (G in LEGB)**
    The module-level scope where global variables are defined. Checked third in the LEGB lookup order.

I
---

**Immutable**
    An object whose value cannot be changed after it is created. Examples: int, float, str, tuple, frozenset.
    Operations on immutable objects create new objects rather than modifying existing ones.

**Import**
    The process of bringing code from one module into another. Syntax: import module_name
    or from module_name import function_name

**Inheritance**
    A mechanism where a class (child/subclass) can inherit attributes and methods from another class (parent/superclass).
    Promotes code reuse and establishes relationships between classes.

**Instance**
    An individual object created from a class. Each instance has its own set of attributes.

**Instance Method**
    A method that operates on an instance of a class. Takes self as the first parameter.

**Instance Variable**
    A variable that belongs to a specific instance of a class. Each instance has its own copy.

**isinstance()** - isinstance(expression, classinfo)
    Returns True if the object is an instance of the specified class or a subclass thereof.
    Example: isinstance(5, int) returns True

**Iterable**
    An object that can be iterated over (used in a for loop). Must implement the __iter__() method.
    Examples: lists, tuples, strings, dictionaries, sets, file objects

**Iteration**
    The process of repeating a set of instructions for a specified number of times or until a 
    certain condition is met. Often done using for loops or while loops.

**Iterator**
    An object that allows you to iterate over a sequence, accessing its elements one at a time 
    without loading the entire collection into memory. Implements __iter__() and __next__() methods.
    More memory-efficient than loading entire sequences.

K
---

**Key (in dictionaries)**
    The first element in a key-value pair in a dictionary. Keys must be hashable (immutable).
    Used to access the corresponding value. Example: dict["key"] returns the value

**Keyword Argument**
    An argument passed to a function using the parameter name. Allows arguments to be passed 
    in any order. Example: function(name="Alice", age=30)

**kwargs** - **kwargs
    A special parameter that collects all keyword arguments into a dictionary.
    The double asterisk (**) unpacks keyword arguments.

L
---

**Lambda**
    An anonymous function defined using the lambda keyword. Syntax: lambda argument: expression
    Used for simple, one-line functions. Example: lambda x: x * 2

**List**
    An ordered, mutable collection of items. Items can be of any type and can be duplicated.
    Example: [1, 2, 3, "hello", True]

**List Comprehension**
    A concise way to create lists. Syntax: [expression for item in iterable if condition]
    More readable and often faster than equivalent for loops.

**Local Scope (L in LEGB)**
    The innermost scope, typically inside a function. Variables defined here are local to that function.
    Checked first in the LEGB lookup order.

**Local Variable**
    A variable defined within a function or block of code, only accessible within that scope.
    Takes precedence over variables with the same name in outer scopes.

M
---

**Map** - map(function, iterable)
    Returns an iterator that applies the function to every item in the iterable.
    Example: map(str.upper, ["hello", "world"]) returns ["HELLO", "WORLD"]

**Max** - max(expression, [default])
    Returns the largest item in an iterable or the largest of two or more arguments.
    Example: max([1, 5, 3]) returns 5

**Method**
    A function that belongs to an object. Called using dot notation: object.method(arguments)
    Methods can be instance methods, class methods, or static methods.

**Min** - min(expression, [default])
    Returns the smallest item in an iterable or the smallest of two or more arguments.
    Example: min([1, 5, 3]) returns 1

**Module**
    A file containing Python code (functions, classes, variables). Can be imported into other programs.
    Example: math, os, datetime, random

**Mutable**
    An object whose value can be changed after it is created. Examples: list, dict, set.
    Mutable objects can be modified in-place.

N
---

**Next** - next(iterable, [default])
    Returns the next item from an iterator. Raises StopIteration when exhausted, 
    or returns default if provided. Example: next(iter([1, 2, 3])) returns 1

**None**
    A special constant representing the absence of a value. The only value of the NoneType.
    Used to indicate that a variable has no value assigned.

O
---

**Object**
    An instance of a class. Everything in Python is an object, including numbers, strings, functions, and classes.
    Objects are self-contained units that combine data (attributes) and behavior (methods).
    Example: class Person(name, age): pass creates a Person class that can be instantiated into objects

**Operator**
    A symbol that performs an operation on one or more operands. Examples: +, -, *, /, ==, !=, <, >, and, or, not

P
---

**Parameter**
    An input variable defined in a function's definition. When the function is called, arguments 
    are passed and assigned to these parameters. Example: def add(a, b): where a and b are parameters

**Perfect Number**
    A positive integer that is equal to the sum of its proper divisors (excluding itself).
    Example: 6 = 1 + 2 + 3, so 6 is a perfect number

**Pop** - pop([index])
    Removes and returns an item from a list at the specified index (default is the last item).
    Example: [1, 2, 3].pop() returns 3 and the list becomes [1, 2]

**Property**
    A special kind of method that is accessed like an attribute. Defined using the @property decorator.
    Allows controlled access to instance variables.

R
---

**Range**
    A built-in function that generates a sequence of numbers. Syntax: range(start, stop, step)
    Returns an immutable sequence type. Example: range(5) generates 0, 1, 2, 3, 4

**Return**
    A statement that exits a function and optionally returns a value to the caller.
    If no value is specified, returns None.

S
---

**Scope**
    A region of code where variables are defined and accessible. Python uses LEGB (Local, Enclosing, Global, Built-in) 
    to determine which variable to use. Scopes help prevent naming conflicts and manage variable lifetimes.

**Set**
    An unordered, mutable collection of unique elements. No duplicates allowed.
    Example: {1, 2, 3, 4}

**Set Comprehension**
    A concise way to create sets. Syntax: {value for item in iterable if condition}
    Similar to list comprehension but creates a set instead.

**Sorted** - sorted(iterable, key=None, reverse=False)
    Returns a new sorted list from the items in the iterable. Does not modify the original.
    key parameter specifies a function to extract a comparison key. reverse=True sorts in descending order.
    Example: sorted([3, 1, 2]) returns [1, 2, 3]

**Statement**
    A line of code that performs an action. Unlike expressions, statements don't necessarily return a value.
    Examples: if, for, while, def, class, import, return, pass

**String (str)**
    An immutable sequence of characters. Can be created using single, double, or triple quotes.
    Example: "Hello, World!" or 'Python' or """Multi-line string"""

**Subclass**
    A class that inherits from another class (superclass). Also called a child class or derived class.

**Superclass**
    A class that is inherited by another class. Also called a parent class or base class.

**Syntax**
    The set of rules that define how Python code must be written. Syntax errors occur when code 
    doesn't follow these rules and prevent the program from running.

T
---

**Tuple**
    An ordered, immutable collection of objects. Used to store groups of related data.
    Created using parentheses: (1, 2, 3) or just commas: 1, 2, 3
    Example: coordinates = (10, 20)

**Type**
    The category or class of a value. Determines what operations can be performed on it.
    Examples: int, float, str, list, dict, bool, NoneType

**Type Hinting**
    A feature that allows you to indicate the expected types of function parameters and return values.
    Example: def add(a: int, b: int) -> int:

V
---

**Variable**
    A container that holds a value. Created by assigning a value to a name using the = operator.
    Variables can hold different types of data: numbers, strings, lists, objects, etc.
    Example: name = "Alice" or count = 42

**Variable Scope**
    The region of code where a variable is accessible. Determined by where the variable is defined.
    See: Local Scope, Global Scope, Enclosing Scope

Z
---

**Zip** - zip([iterable1], [iterable2], [iterable3], ...)
    Combines multiple iterables element-wise into tuples. Returns an iterator of tuples.
    Example: zip([1, 2], ['a', 'b']) returns [(1, 'a'), (2, 'b')]
    Stops when the shortest iterable is exhausted.

LEGB RULE - SCOPE RESOLUTION ORDER
==================================
Python finds names by searching in this order:

    • L = Local (inner function) - Variables defined inside the current function
    • E = Enclosing (closures) - Variables from outer functions that contain the current function
    • G = Global (module) - Variables defined at the module level
    • B = Builtins - Python's built-in names (print, len, etc.)

This order ensures that local variables take precedence over global ones, and allows closures 
to access variables from their enclosing functions.

"""
`;

// REGEX TAB - Regular Expressions Reference
const REGEX_CONTENT = `#regular expressions
"""
**Character Classes**

* \`a-z\`: Matches any lowercase letter
* \`A-Z\`: Matches any uppercase letter
* \`0-9\`: Matches any digit
* \`[a-zA-Z]\`: Matches any letter (both lowercase and uppercase)
* \`[0-9]\`: Matches any digit
* \`\\d\`: Matches any digit
* \`\\w\`: Matches any word character (alphanumeric plus underscore)
* \`\\s\`: Matches any whitespace character

**Special Characters**

* \`.\`: Matches any single character
* \`^\`: Matches the start of a string
* \`$\`: Matches the end of a string
* \`*\`: Matches 0 or more of the preceding character
* \`+\`: Matches 1 or more of the preceding character
* \`?\`: Matches 0 or 1 of the preceding character
* \`{n, m}\`: Matches between n and m of the preceding character
* \`{n,}\`: Matches at least n of the preceding character
* \`{, m}\`: Matches at most m of the preceding character

**Quantifiers**

* \`*\`: Matches 0 or more of the preceding character
* \`+\`: Matches 1 or more of the preceding character
* \`?\`: Matches 0 or 1 of the preceding character
* \`{n, m}\`: Matches between n and m of the preceding character
* \`{n,}\`: Matches at least n of the preceding character
* \`{, m}\`: Matches at most m of the preceding character

**Groups and Capturing**

* \`(\` and \`)\`: Used to group parts of a pattern together
* \`\\1\`, \`\\2\`, etc.: Refer to the capturing groups in the pattern

**Escaping**

* \`\\\`: Escapes special characters
* \`\\b\`: Matches a word boundary

Here are some examples of regex patterns:

* \`\\d{4}-\\d{2}-\\d{2}\`: Matches a date in the format DD-MM-YYYY
* \`[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\`: Matches an email address
* \`\\d{3}-\\d{3}-\\d{4}\`: Matches a credit card number
* \`[a-zA-Z]+ [a-zA-Z]+, [A-Z]{2}\`: Matches a full name
* \`\\d{1,3}\\.\\d{3,5}/\\d{4}\`: Matches a phone number

These are just a few examples of the many patterns you can use in regex. The specific patterns you use will depend on the problem you're trying to solve.

Do you have a specific problem you'd like me to help you solve using regex?
"""
`;

const PYTHON_KEYWORDS = [
    'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
    'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'True', 'try', 'while', 'with', 'yield'
];

const PYTHON_BUILTINS = [
    'abs', 'all', 'any', 'append', 'bool', 'breakpoint', 'callable', 'chr', 'classmethod',
    'clear', 'copy', 'count', 'dict', 'dir', 'divmod', 'enumerate', 'extend', 'filter',
    'float', 'format', 'get', 'hasattr', 'hex', 'index', 'input', 'insert', 'int', 'isinstance',
    'issubclass', 'items', 'join', 'keys', 'len', 'list', 'lower', 'map', 'max', 'min',
    'next', 'open', 'ord', 'pop', 'pow', 'print', 'property', 'range', 'remove', 'replace',
    'reverse', 'reversed', 'round', 'set', 'slice', 'sorted', 'split', 'staticmethod', 'str',
    'sum', 'super', 'tuple', 'type', 'upper', 'update', 'values', 'zip'
];

function CopyButton({ text }: { text: string }) {
    const [copied, setCopied] = useState(false);
    return (
        <button
            onClick={async () => {
                try {
                    await navigator.clipboard.writeText(text);
                    setCopied(true);
                    setTimeout(() => setCopied(false), 2000);
                } catch { /* ignore */ }
            }}
            className="flex items-center gap-1 text-[10px] text-gray-400 hover:text-[#4ade80] transition-colors"
            title="Copy to clipboard"
        >
            {copied ? <Check size={12} className="text-[#4ade80]" /> : <Copy size={12} />}
            {copied ? 'Copied' : 'Copy'}
        </button>
    );
}

const BASE_PYTHON_COMPLETIONS: Completion[] = [
    snippetCompletion("print(${0})", { label: "print", detail: "built-in function", type: "function" }),
    snippetCompletion("def ${name}(${args}):\n    ${0}", { label: "def", detail: "define function", type: "keyword" }),
    snippetCompletion("for ${item} in ${iterable}:\n    ${0}", { label: "for", detail: "for loop", type: "keyword" }),
    snippetCompletion("if ${condition}:\n    ${0}", { label: "if", detail: "if statement", type: "keyword" }),
    snippetCompletion("class ${Name}:\n    def __init__(self${args}):\n        ${0}", { label: "class", detail: "define class", type: "keyword" }),
    ...PYTHON_KEYWORDS.map((label) => ({ label, type: 'keyword' as const })),
    ...PYTHON_BUILTINS.map((label) => ({ label, type: 'function' as const, detail: 'built-in' }))
];


const pythonSnippets = (context: CompletionContext) => {
    const word = context.matchBefore(/\w*/);
    if (!word || (word.from === word.to && !context.explicit)) return null;

    return {
        from: word.from,
        options: [
            snippetCompletion("print(${0})", { label: "print", detail: "built-in function", type: "function" }),
            snippetCompletion("def ${name}(${args}):\n    ${0}", { label: "def", detail: "define function", type: "keyword" }),
        ]
    };
};

const App: React.FC = () => {
    const initialExercise = useMemo(() => getInitialExercise(), []);
    const [exercise, setExercise] = useState<Exercise>(initialExercise);
    const [files, setFiles] = useState<ProjectFile[]>([{ name: 'main.py', content: initialExercise.initialCode }]);
    const [activeFileIndex, setActiveFileIndex] = useState(0);
    const [isEditingFileName, setIsEditingFileName] = useState(false);
    const [newName, setNewName] = useState('');

    const [output, setOutput] = useState('Run code to see output...');
    const [outputStatus, setOutputStatus] = useState<OutputStatus>('idle');
    const [pendingNextProblem, setPendingNextProblem] = useState(false);
    const [stdinValues, setStdinValues] = useState<string[]>([]);
    const [stdinDraft, setStdinDraft] = useState('');
    const [waitingForInput, setWaitingForInput] = useState(false);
    const [inputPrompt, setInputPrompt] = useState('');
    const [isRunning, setIsRunning] = useState(false);
    const [statsByMode, setStatsByMode] = useState<StatsByMode>(() => loadStatsByMode());
    const [pyodide, setPyodide] = useState<any>(null);
    const [bootStage, setBootStage] = useState<'loading' | 'ready' | 'launched'>('loading');
    const [bootLog, setBootLog] = useState<string>('Handshaking...');
    const [loadTime, setLoadTime] = useState<number>(0);
    const [isInFrame, setIsInFrame] = useState(false);
    const [showModal, setShowModal] = useState<'none' | 'instructions' | 'hint' | 'solution' | 'settings' | 'api_key' | 'restart_confirm' | 'problem_full'>('none');
    const [modalTab, setModalTab] = useState<'how' | 'cheat' | 'glossary' | 'regex'>('how');
    const [solutionTab, setSolutionTab] = useState<'code' | 'logic' | 'requirements'>('code');
    const [aiHintText, setAiHintText] = useState<string>('');
    const [copyFeedback, setCopyFeedback] = useState(false);
    const [apiKey, setApiKey] = useState<string>(() => {
        return localStorage.getItem('gemini_api_key') || '';
    });
    const [difficultyMode, setDifficultyMode] = useState<DifficultyMode>(() => getSavedDifficultyMode());
    const [keyboardHaptics, setKeyboardHaptics] = useState(() => localStorage.getItem('python_keyboard_haptics') === 'true');
    const [keyboardSound, setKeyboardSound] = useState(() => localStorage.getItem('python_keyboard_sound') === 'true');
    const [isOutputExpanded, setIsOutputExpanded] = useState(false);
    const [showActionPanel, setShowActionPanel] = useState(false);
    const [outputHeight, setOutputHeight] = useState(85);
    const [logicContent, setLogicContent] = useState<string>('');
    const [requirementsContent, setRequirementsContent] = useState<string>('');
    const [resetConfirmArmed, setResetConfirmArmed] = useState(false);
    const [contextMenu, setContextMenu] = useState<{ x: number; y: number } | null>(null);

    // Saved problems state
    interface SavedProblem {
        exerciseId: number;
        description: string;
        initialCode: string;
        solution: string;
        savedAt: string;
        mastered: boolean;
    }
    const [savedProblems, setSavedProblems] = useState<SavedProblem[]>(() => {
        try {
            const raw = localStorage.getItem('python_mastery_saved_problems');
            return raw ? JSON.parse(raw) : [];
        } catch {
            return [];
        }
    });

    useEffect(() => {
        localStorage.setItem('python_mastery_saved_problems', JSON.stringify(savedProblems));
    }, [savedProblems]);

    const isProblemSaved = (id: number) => savedProblems.some(p => p.exerciseId === id);

    const saveCurrentProblem = () => {
        if (isProblemSaved(exercise.id)) return;
        const newProblem: SavedProblem = {
            exerciseId: exercise.id,
            description: exercise.description,
            initialCode: exercise.initialCode,
            solution: exercise.solution,
            savedAt: new Date().toISOString(),
            mastered: false,
        };
        setSavedProblems(prev => [...prev, newProblem]);
    };

    const deleteSavedProblem = (id: number) => {
        setSavedProblems(prev => prev.filter(p => p.exerciseId !== id));
    };

    const markSavedProblemMastered = (id: number) => {
        setSavedProblems(prev =>
            prev.map(p => (p.exerciseId === id ? { ...p, mastered: true } : p))
        );
    };

    const loadSavedProblem = (problem: SavedProblem) => {
        const ex = EXERCISES[problem.exerciseId - 1];
        if (ex) {
            setExercise(ex);
            setFiles([{ name: 'main.py', content: problem.initialCode }]);
            setActiveFileIndex(0);
            setOutput('Run code to see output...');
            setOutputStatus('idle');
            setPendingNextProblem(false);
            setAiHintText('');
            setShowModal('none');
        }
    };

    const mainScrollRef = useRef<HTMLDivElement>(null);
    const editorShellRef = useRef<HTMLDivElement>(null);
    const activeEditorViewRef = useRef<EditorView | null>(null);
    const stdinValuesRef = useRef<string[]>([]);
    const keyboardHapticsRef = useRef(keyboardHaptics);
    const keyboardSoundRef = useRef(keyboardSound);
    const keyboardAudioRef = useRef<AudioContext | null>(null);
    const lastKeyboardFeedbackRef = useRef(0);
    const keyboardMainScrollRef = useRef<number | null>(null);
    const keyboardRestoreTimersRef = useRef<number[]>([]);
    const deleteHoldDelayRef = useRef<number | null>(null);
    const deleteHoldTimerRef = useRef<number | null>(null);
    const longPressTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
    const outputRef = useRef<HTMLDivElement>(null);
    const headerRef = useRef<HTMLDivElement>(null);
    const problemPanelRef = useRef<HTMLDivElement>(null);
    const problemDescriptionRef = useRef<HTMLDivElement>(null);
    const [headerHeight, setHeaderHeight] = useState(265);
    const [problemPanelHeight, setProblemPanelHeight] = useState(200);
    const editorToolbarTop = Math.max(headerHeight + 4, 270);
    const editorContentTop = editorToolbarTop + 54;
    const runButtonLabel = 'RUN';
    const runButtonClass = 'ml-1 flex items-center gap-1.5 px-3 py-1 rounded-lg font-bold text-xs bg-[#22c55e1a] border border-[#22c55e4d] text-[#22c55e]';
    const selectedModeLabel = getDifficultyLabel(difficultyMode);
    const currentStats = statsByMode[difficultyMode] ?? EMPTY_STATS;
    const modeExerciseCount = useMemo(() => {
        return getExercisePoolForMode(difficultyMode).length;
    }, [difficultyMode]);

    useEffect(() => {
        keyboardHapticsRef.current = keyboardHaptics;
        localStorage.setItem('python_keyboard_haptics', String(keyboardHaptics));
    }, [keyboardHaptics]);

    useEffect(() => {
        keyboardSoundRef.current = keyboardSound;
        localStorage.setItem('python_keyboard_sound', String(keyboardSound));
    }, [keyboardSound]);

    const playKeyboardFeedback = useCallback(() => {
        const now = performance.now();
        if (now - lastKeyboardFeedbackRef.current < 28) return;
        lastKeyboardFeedbackRef.current = now;

        if (keyboardHapticsRef.current && 'vibrate' in navigator) {
            navigator.vibrate(8);
        }

        if (!keyboardSoundRef.current) return;
        try {
            const AudioCtor = window.AudioContext || (window as any).webkitAudioContext;
            if (!AudioCtor) return;
            const audio = keyboardAudioRef.current ?? new AudioCtor();
            keyboardAudioRef.current = audio;
            if (audio.state === 'suspended') audio.resume();
            const oscillator = audio.createOscillator();
            const gain = audio.createGain();
            oscillator.type = 'triangle';
            oscillator.frequency.value = 880;
            gain.gain.setValueAtTime(0.0001, audio.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.035, audio.currentTime + 0.006);
            gain.gain.exponentialRampToValueAtTime(0.0001, audio.currentTime + 0.035);
            oscillator.connect(gain);
            gain.connect(audio.destination);
            oscillator.start();
            oscillator.stop(audio.currentTime + 0.04);
        } catch {
            // Audio feedback is optional and may be blocked by the browser.
        }
    }, []);

    const preserveEditorKeyboardPosition = useCallback(() => {
        const mainScroller = mainScrollRef.current;
        if (!mainScroller) return;

        if (keyboardMainScrollRef.current === null) {
            keyboardMainScrollRef.current = mainScroller.scrollTop;
        }

        const targetScrollTop = keyboardMainScrollRef.current;
        const restore = () => {
            mainScroller.scrollTop = targetScrollTop;
            if (window.scrollY !== 0) window.scrollTo(0, 0);
        };

        restore();
        window.requestAnimationFrame(restore);
        keyboardRestoreTimersRef.current.forEach(timer => window.clearTimeout(timer));
        keyboardRestoreTimersRef.current = [60, 140, 280, 520].map(delay => window.setTimeout(restore, delay));
    }, []);

    useEffect(() => {
        setIsInFrame(window.self !== window.top);

        const bootEl = document.getElementById('boot');
        if (bootEl) {
            setTimeout(() => { bootEl.style.opacity = '0'; }, 500);
            setTimeout(() => { bootEl.style.display = 'none'; }, 1000);
        }
    }, []);

    useEffect(() => {
        const updateHeaderHeight = () => {
            if (headerRef.current) {
                // Use getBoundingClientRect for more accurate measurement
                // This includes padding and border, which is what we want for positioning
                const rect = headerRef.current.getBoundingClientRect();
                setHeaderHeight(rect.bottom);
            }
        };
        const updateProblemPanelHeight = () => {
            if (problemPanelRef.current) {
                const height = problemPanelRef.current.getBoundingClientRect().height;
                setProblemPanelHeight(height);
            }
        };
        // Immediate update
        updateHeaderHeight();
        updateProblemPanelHeight();
        // Update after a short delay to ensure DOM is ready
        const timeoutId1 = setTimeout(() => {
            updateHeaderHeight();
            updateProblemPanelHeight();
        }, 50);
        const timeoutId2 = setTimeout(() => {
            updateHeaderHeight();
            updateProblemPanelHeight();
        }, 200);
        const handleResize = () => {
            updateHeaderHeight();
            updateProblemPanelHeight();
        };
        window.addEventListener('resize', handleResize);

        // Use ResizeObserver to watch for content changes
        let headerObserver: ResizeObserver | null = null;
        let problemObserver: ResizeObserver | null = null;
        if (headerRef.current && typeof ResizeObserver !== 'undefined') {
            headerObserver = new ResizeObserver(() => {
                updateHeaderHeight();
            });
            headerObserver.observe(headerRef.current);
        }
        if (problemPanelRef.current && typeof ResizeObserver !== 'undefined') {
            problemObserver = new ResizeObserver(() => {
                updateProblemPanelHeight();
            });
            problemObserver.observe(problemPanelRef.current);
        }

        return () => {
            clearTimeout(timeoutId1);
            clearTimeout(timeoutId2);
            window.removeEventListener('resize', handleResize);
            if (headerObserver) {
                headerObserver.disconnect();
            }
            if (problemObserver) {
                problemObserver.disconnect();
            }
        };
    }, [exercise, bootStage]);

    // Removed problematic useEffect - inline styles now properly set in JSX to allow scrolling
    // maxHeight: '300px' and overflowY: 'auto' are set directly in the style prop

    useEffect(() => {
        if (bootStage !== 'launched') return;
        const editorShell = editorShellRef.current;
        if (!editorShell) return;

        const handleEditorFocus = () => {
            keyboardMainScrollRef.current = mainScrollRef.current?.scrollTop ?? 0;
            preserveEditorKeyboardPosition();
        };

        const handleEditorBlur = () => {
            window.setTimeout(() => {
                keyboardMainScrollRef.current = null;
            }, 650);
        };

        const handleViewportChange = () => {
            if (!editorShell.contains(document.activeElement)) return;
            preserveEditorKeyboardPosition();
        };

        editorShell.addEventListener('focusin', handleEditorFocus);
        editorShell.addEventListener('focusout', handleEditorBlur);
        window.visualViewport?.addEventListener('resize', handleViewportChange);
        window.visualViewport?.addEventListener('scroll', handleViewportChange);

        return () => {
            editorShell.removeEventListener('focusin', handleEditorFocus);
            editorShell.removeEventListener('focusout', handleEditorBlur);
            window.visualViewport?.removeEventListener('resize', handleViewportChange);
            window.visualViewport?.removeEventListener('scroll', handleViewportChange);
            keyboardRestoreTimersRef.current.forEach(timer => window.clearTimeout(timer));
            keyboardRestoreTimersRef.current = [];
        };
    }, [bootStage, preserveEditorKeyboardPosition]);

    useEffect(() => {
        localStorage.setItem('python_mastery_stats', JSON.stringify(statsByMode));
    }, [statsByMode]);

    useEffect(() => {
        localStorage.setItem('python_current_problem_id', String(exercise.id));
    }, [exercise.id]);

    // Auto-scroll output to bottom when new output is added
    useEffect(() => {
        if (outputRef.current && output !== 'Run code to see output...') {
            outputRef.current.scrollTop = outputRef.current.scrollHeight;
        }
    }, [output]);

    // After run completes, keep the editor below the fixed file toolbar.
    useEffect(() => {
        if (!isRunning && mainScrollRef.current && output !== 'Run code to see output...') {
            const scrollContainer = mainScrollRef.current;
            const editorPanel = editorShellRef.current?.closest('[data-editor-panel]');
            if (!(editorPanel instanceof HTMLElement)) return;

            const toolbarBottom = editorToolbarTop + 54;
            const panelTop = editorPanel.getBoundingClientRect().top;
            if (panelTop < toolbarBottom + 8) {
                scrollContainer.scrollTop -= toolbarBottom + 8 - panelTop;
            }
        }
    }, [isRunning, output, editorToolbarTop]);

    useEffect(() => {
        return () => {
            stopEditorDeleteHold();
        };
    }, []);

    useEffect(() => {
        if (bootStage !== 'launched') return;
        const mainScroller = mainScrollRef.current;
        if (!mainScroller) return;

        const resetScroll = () => {
            mainScroller.scrollTop = 0;
        };

        resetScroll();
        const frameId = window.requestAnimationFrame(resetScroll);
        const timeoutId = window.setTimeout(resetScroll, 120);

        return () => {
            window.cancelAnimationFrame(frameId);
            window.clearTimeout(timeoutId);
        };
    }, [bootStage, exercise.id]);

    useEffect(() => {
        const mainScroller = mainScrollRef.current;
        const editorShell = editorShellRef.current;
        if (!mainScroller || !editorShell) return;

        let editorScroller: HTMLElement | null = null;
        let lastTouchY = 0;

        const attachTouchBridge = () => {
            const candidate = editorShell.querySelector('.cm-scroller');
            if (!(candidate instanceof HTMLElement)) return;
            editorScroller = candidate;

            const handleTouchStart = (event: TouchEvent) => {
                if (event.touches.length !== 1) return;
                lastTouchY = event.touches[0].clientY;
            };

            const handleTouchMove = (event: TouchEvent) => {
                if (!editorScroller || event.touches.length !== 1) return;

                const currentY = event.touches[0].clientY;
                const deltaY = currentY - lastTouchY;
                lastTouchY = currentY;

                const editorMaxScroll = editorScroller.scrollHeight - editorScroller.clientHeight;
                const editorCannotScroll = editorMaxScroll <= 1;
                const atTop = editorScroller.scrollTop <= 0;
                const atBottom = editorScroller.scrollTop >= editorMaxScroll - 1;

                if (editorCannotScroll || (deltaY > 0 && atTop) || (deltaY < 0 && atBottom)) {
                    mainScroller.scrollTop -= deltaY;
                    event.preventDefault();
                }
            };

            editorScroller.addEventListener('touchstart', handleTouchStart, { passive: true });
            editorScroller.addEventListener('touchmove', handleTouchMove, { passive: false });

            return () => {
                editorScroller?.removeEventListener('touchstart', handleTouchStart);
                editorScroller?.removeEventListener('touchmove', handleTouchMove);
            };
        };

        const detach = attachTouchBridge();
        if (detach) return detach;

        const retryId = window.setTimeout(() => {
            const lateDetach = attachTouchBridge();
            if (lateDetach) {
                cleanup = lateDetach;
            }
        }, 50);

        let cleanup = () => {};
        return () => {
            window.clearTimeout(retryId);
            cleanup();
        };
    }, [activeFileIndex, files.length, bootStage]);

    useEffect(() => {
        if (bootStage !== 'launched') return;
        const mainScroller = mainScrollRef.current;
        const overlay = headerRef.current;
        if (!mainScroller || !overlay) return;

        let lastTouchY = 0;

        const handleTouchStart = (event: TouchEvent) => {
            if (event.touches.length !== 1) return;
            lastTouchY = event.touches[0].clientY;
        };

        const handleTouchMove = (event: TouchEvent) => {
            if (event.touches.length !== 1) return;

            const currentY = event.touches[0].clientY;
            const deltaY = currentY - lastTouchY;
            lastTouchY = currentY;

            mainScroller.scrollTop -= deltaY;
            event.preventDefault();
        };

        overlay.addEventListener('touchstart', handleTouchStart, { passive: true, capture: true });
        overlay.addEventListener('touchmove', handleTouchMove, { passive: false, capture: true });

        return () => {
            overlay.removeEventListener('touchstart', handleTouchStart, true);
            overlay.removeEventListener('touchmove', handleTouchMove, true);
        };
    }, [bootStage]);

    useEffect(() => {
        let interval: any;
        if (bootStage === 'loading') {
            interval = setInterval(() => {
                setLoadTime(prev => {
                    const next = prev + 1;
                    if (next === 3) setBootLog('Network verified...');
                    if (next === 8) setBootLog('Streaming binaries...');
                    if (next === 15) setBootLog('Extracting modules...');
                    if (next === 25) setBootLog('Finalizing compile...');
                    return next;
                });
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [bootStage]);

    useEffect(() => {
        async function initPyodide() {
            if (window.__PYODIDE_INSTANCE__) {
                setPyodide(window.__PYODIDE_INSTANCE__);
                setBootStage('ready');
                return;
            }

            if (window.__PYODIDE_INIT_LOCK__) return;
            window.__PYODIDE_INIT_LOCK__ = true;

            try {
                setBootLog('Fetching interpreter...');

                let retries = 0;
                while (typeof window.loadPyodide === 'undefined' && retries < 120) {
                    await new Promise(r => setTimeout(r, 500));
                    retries++;
                }

                if (typeof window.loadPyodide === 'undefined') {
                    throw new Error("WASM source unavailable. Please refresh.");
                }

                const py = await window.loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/"
                });

                await py.loadPackage([]);
                window.__PYODIDE_INSTANCE__ = py;
                setPyodide(py);
                setBootStage('ready');
            } catch (err: any) {
                console.error("Pyodide error:", err);
                setBootLog(`Error: ${err.message || 'Engine Fail'}`);
                window.__PYODIDE_INIT_LOCK__ = false;
            }
        }
        initPyodide();
    }, []);

    const handleLaunch = () => {
        setBootStage('launched');
    };

    const forceResetCache = async () => {
        if (window.localStorage) window.localStorage.clear();
        if (window.caches) {
            const keys = await window.caches.keys();
            await Promise.all(keys.map(k => window.caches.delete(k)));
        }
        window.location.reload();
    };

    const forceRefreshToNewest = async () => {
        if (navigator.serviceWorker) {
            const regs = await navigator.serviceWorker.getRegistrations();
            await Promise.all(regs.map(r => r.unregister()));
        }
        if (window.caches) {
            const keys = await window.caches.keys();
            await Promise.all(keys.map(k => window.caches.delete(k)));
        }
        window.location.reload(true);
    };

    const handleCopyLink = () => {
        const url = window.location.href;
        navigator.clipboard.writeText(url);
        setCopyFeedback(true);
        setTimeout(() => setCopyFeedback(false), 2000);
    };

    const setProblemById = (id: number) => {
        const ex = getExerciseById(id) ?? EXERCISES[0];
        setExercise(ex);
        localStorage.setItem('python_current_problem_id', String(ex.id));
        setFiles([{ name: 'main.py', content: ex.initialCode }]);
        setActiveFileIndex(0);
        setOutput('Run code to see output...');
        setOutputStatus('idle');
        setPendingNextProblem(false);
        setStdinValues([]);
        stdinValuesRef.current = [];
        setStdinDraft('');
        setWaitingForInput(false);
        setInputPrompt('');
        setAiHintText('');
    };

    const loadRandomExercise = useCallback((mode: DifficultyMode = difficultyMode) => {
        const randomExercise = getRandomExerciseForMode(mode, exercise.id);
        setProblemById(randomExercise.id);
    }, [difficultyMode, exercise.id]);

    const handleDifficultyModeSelect = (mode: DifficultyMode) => {
        setDifficultyMode(mode);
        localStorage.setItem('python_difficulty_mode', mode);
        const nextExercise = getRandomExerciseForMode(mode, exercise.id);
        setProblemById(nextExercise.id);
    };

    const updateCurrentModeStats = (result: 'success' | 'failed') => {
        setStatsByMode(prev => {
            const modeStats = prev[difficultyMode] ?? EMPTY_STATS;
            return {
                ...prev,
                [difficultyMode]: {
                    ...modeStats,
                    shots: modeStats.shots + 1,
                    success: modeStats.success + (result === 'success' ? 1 : 0),
                    failed: modeStats.failed + (result === 'failed' ? 1 : 0)
                }
            };
        });
    };

    const handleRestartProgress = () => {
        setStatsByMode(createEmptyStatsByMode());
        loadRandomExercise();
        setResetConfirmArmed(false);
        setShowModal('none');
    };

    const runCode = async () => {
        if (isRunning) return;
        if (!pyodide) return;
        const autoGrader = AUTO_GRADERS[exercise.id];
        setIsRunning(true);
        setOutputStatus('running');
        setOutput('Executing...');
        setWaitingForInput(false);
        setInputPrompt('');
        setPendingNextProblem(false);
        try {
            // Write all files to the virtual filesystem
            files.forEach(file => {
                const pathParts = file.name.split('/').filter(Boolean);
                if (pathParts.length > 1) {
                    let currentPath = '';
                    pathParts.slice(0, -1).forEach(part => {
                        currentPath = currentPath ? `${currentPath}/${part}` : part;
                        try {
                            pyodide.FS.mkdir(currentPath);
                        } catch {
                            // Directory already exists.
                        }
                    });
                }
                pyodide.FS.writeFile(file.name, file.content);
            });

            // Clear user-defined modules from sys.modules to ensure fresh imports
            const userModules = files.map(f => f.name.replace('.py', ''));
            const clearModulesCode = `
import sys
import importlib
import io
import builtins

# Ensure current directory is in path (crucial for imports)
if '.' not in sys.path:
    sys.path.insert(0, '.')

for mod in ${JSON.stringify(userModules)}:
    if mod in sys.modules:
        del sys.modules[mod]

importlib.invalidate_caches()
sys.stdout = io.StringIO()
__app_input_values = list(${JSON.stringify(stdinValuesRef.current)})
def __app_input(prompt=""):
    print(prompt, end="")
    if not __app_input_values:
        raise Exception("__PY_INPUT_REQUIRED__" + str(prompt))
    value = __app_input_values.pop(0)
    print(value)
    return value
builtins.input = __app_input
`;
            pyodide.runPython(clearModulesCode);

            const activeFile = files[activeFileIndex];
            let stdout = '';
            if (autoGrader?.mode !== 'script') {
                // CRITICAL FIX: Use exec with filename context so imports work
                const code = `exec(compile(${JSON.stringify(activeFile.content)}, ${JSON.stringify(activeFile.name)}, 'exec'))`;
                await pyodide.runPythonAsync(code);
                stdout = pyodide.runPython("sys.stdout.getvalue()");
            }
            const userOutput = stdout?.trim() ? `Program output:\n${stdout.trim()}\n\n` : '';
            stdinValuesRef.current = [];
            setStdinValues([]);

            if (autoGrader) {
                pyodide.runPython(`
import builtins
builtins.input = lambda prompt='': (_ for _ in ()).throw(Exception("__AUTO_GRADER_INPUT_UNAVAILABLE__" + str(prompt)))
`);
                pyodide.runPython(buildAutoGradeScript(autoGrader, activeFile.content, activeFile.name));
                const gradeResult = JSON.parse(pyodide.runPython("__auto_grader_json")) as AutoGradeResult;

                if (gradeResult.passed) {
                    updateCurrentModeStats('success');
                    setOutputStatus('win');
                    setPendingNextProblem(true);
                    setOutput(`${userOutput}AUTO WIN\n${gradeResult.message}\n\nUse the Next button in the problem panel for another problem.`);
                } else {
                    updateCurrentModeStats('failed');
                    setOutputStatus('fail');
                    setPendingNextProblem(true);
                    setOutput(`${userOutput}AUTO FAILED\n${gradeResult.message}\n\nFix your code and press RUN again, or use the Next button in the problem panel.`);
                }
            } else {
                setOutputStatus('info');
                setOutput(`${stdout || 'Success (No output).'}\n\nNo auto-grader yet for Problem ${exercise.id}. Use WIN/FAILED manually.`);
            }
        } catch (err: any) {
            const errorMessage = String(err?.message || err || '');
            const inputMarker = '__PY_INPUT_REQUIRED__';
            if (errorMessage.includes(inputMarker)) {
                const prompt = errorMessage.split(inputMarker).pop()?.trim() || 'Input required';
                const stdout = pyodide.runPython("sys.stdout.getvalue()");
                setOutputStatus('info');
                setWaitingForInput(true);
                setInputPrompt(prompt);
                setOutput(`${stdout || ''}\nWaiting for input${prompt ? `: ${prompt}` : ''}`);
                return;
            }
            const stdout = pyodide.runPython("sys.stdout.getvalue()");
            const userOutput = stdout?.trim() ? `Program output:\n${stdout.trim()}\n\n` : '';
            stdinValuesRef.current = [];
            setStdinValues([]);
            if (autoGrader) {
                updateCurrentModeStats('failed');
                setOutputStatus('fail');
                setPendingNextProblem(true);
                setOutput(`${userOutput}AUTO FAILED\n${errorMessage}\n\nFix your code and press RUN again, or use the Next button in the problem panel.`);
            } else {
                setOutputStatus('fail');
                setOutput(`${userOutput}${errorMessage}`);
            }
        } finally {
            setIsRunning(false);
        }
    };

    const submitInputValue = () => {
        const nextValues = [...stdinValuesRef.current, stdinDraft];
        stdinValuesRef.current = nextValues;
        setStdinValues(nextValues);
        setStdinDraft('');
        setWaitingForInput(false);
        setInputPrompt('');
        setOutput(prev => `${prev}\n${stdinDraft}`);
        setTimeout(() => {
            runCode();
        }, 0);
    };

    const addFile = () => {
        const name = `file_${files.length + 1}.py`;
        setFiles([...files, { name, content: '# New module\n' }]);
        setActiveFileIndex(files.length);
    };

    const removeFile = () => {
        if (files.length <= 1) return;
        const newFiles = files.filter((_, i) => i !== activeFileIndex);
        setFiles(newFiles);
        setActiveFileIndex(Math.max(0, activeFileIndex - 1));
    };

    const startRenaming = () => {
        setNewName(files[activeFileIndex].name);
        setIsEditingFileName(true);
    };

    const finishRenaming = () => {
        if (!newName.trim()) return setIsEditingFileName(false);
        const updatedFiles = [...files];
        updatedFiles[activeFileIndex].name = newName.endsWith('.py') ? newName : `${newName}.py`;
        setFiles(updatedFiles);
        setIsEditingFileName(false);
    };

    const updateActiveContent = (val: string) => {
        const updatedFiles = [...files];
        updatedFiles[activeFileIndex].content = val;
        setFiles(updatedFiles);
        if (pendingNextProblem) setPendingNextProblem(false);
    };

    const handleMarkSuccess = () => {
        updateCurrentModeStats('success');
        loadRandomExercise();
    };

    const handleMarkFailed = () => {
        updateCurrentModeStats('failed');
        loadRandomExercise();
    };

    const handleAiHint = async () => {
        if (!apiKey || apiKey.trim() === '') {
            setShowModal('api_key');
            return;
        }
        setShowModal('hint');
        if (!aiHintText) {
            setAiHintText('Asking Gemini...');
            const hint = await getAiHint(exercise.description, files[activeFileIndex].content, apiKey);
            setAiHintText(hint);
        }
    };

    // Helper function to extract a specific problem's content from file text
    const extractProblemContent = (fileContent: string, problemId: number): string => {
        // Pattern to match both formats: """ \nProblem: X (requirements) and """ \nProblem X: (codelogic)
        const problemMarker = new RegExp(`"""\\s*Problem\\s*:?\\s*${problemId}\\b`, 'm');
        const match = fileContent.match(problemMarker);

        if (!match) {
            return '';
        }

        const startIndex = match.index || 0;

        // Find the end - look for the next problem marker
        const remainingContent = fileContent.substring(startIndex);
        const nextProblemPattern = new RegExp(`"""\\s*Problem\\s*:?\\s*\\d+\\b`, 'm');

        // Find all potential next problems, but skip the current one
        let endIndex = remainingContent.length;
        let searchStart = match[0].length;

        // Look for next problem after the current one
        while (searchStart < remainingContent.length) {
            const nextMatch = remainingContent.substring(searchStart).match(nextProblemPattern);
            if (!nextMatch) {
                break;
            }

            const nextProblemNum = nextMatch[0].match(/\d+/);
            if (nextProblemNum && parseInt(nextProblemNum[0]) !== problemId) {
                endIndex = searchStart + (nextMatch.index || 0);
                break;
            }

            searchStart += (nextMatch.index || 0) + nextMatch[0].length;
        }

        return remainingContent.substring(0, endIndex).trim();
    };

    const loadSolutionFiles = useCallback(async (exerciseId: number) => {
        // Determine which file set contains this problem
        let filePrefix: number;
        if (exerciseId <= 500) {
            filePrefix = 500;
        } else if (exerciseId <= 1000) {
            filePrefix = 1000;
        } else if (exerciseId <= 1500) {
            filePrefix = 1500;
        } else if (exerciseId <= 2000) {
            filePrefix = 2000;
        } else {
            setLogicContent('');
            setRequirementsContent('');
            return;
        }

        try {
            const logicFile = `level1_${filePrefix}_codelogic.py`;
            const reqFile1 = `level1_${filePrefix}_requirements.py`;
            const reqFile2 = `level1_${filePrefix}_requirements..py`;

            // Fetch and parse logic file
            try {
                // Handle GitHub Pages subdirectory
                const isGitHubPages = window.location.hostname === 'llomj.github.io';
                const basePath = isGitHubPages ? '/python_app' : '';
                const logicResponse = await fetch(`${basePath}/${logicFile}`);
                if (logicResponse.ok) {
                    const logicText = await logicResponse.text();
                    const problemLogic = extractProblemContent(logicText, exerciseId);
                    setLogicContent(problemLogic || '');
                } else {
                    setLogicContent('');
                    console.warn(`Logic file not found: ${logicFile}`);
                }
            } catch (err) {
                setLogicContent('');
                console.warn(`Error loading logic file: ${err.message}`);
            }

            // Fetch and parse requirements file (try both variations)
            try {
                // Handle GitHub Pages subdirectory
                const isGitHubPages = window.location.hostname === 'llomj.github.io';
                const basePath = isGitHubPages ? '/python_app' : '';
                let reqResponse = await fetch(`${basePath}/${reqFile1}`);
                if (!reqResponse.ok) {
                    reqResponse = await fetch(`${basePath}/${reqFile2}`);
                }
                if (reqResponse.ok) {
                    const reqText = await reqResponse.text();
                    const problemReq = extractProblemContent(reqText, exerciseId);
                    setRequirementsContent(problemReq || '');
                } else {
                    setRequirementsContent('');
                    console.warn(`Requirements file not found: ${reqFile1} or ${reqFile2}`);
                }
            } catch (err) {
                setRequirementsContent('');
                console.warn(`Error loading requirements file: ${err.message}`);
            }
        } catch (err) {
            console.error('Error loading solution files:', err);
            setLogicContent('');
            setRequirementsContent('');
        }
    }, []);

    useEffect(() => {
        if (showModal === 'solution') {
            loadSolutionFiles(exercise.id);
        }
    }, [showModal, exercise.id, loadSolutionFiles]);

    const rate = currentStats.shots > 0 ? ((currentStats.success / currentStats.shots) * 100).toFixed(2) : '0.00';

    const pythonCompletionSource = useMemo(() => {
        const symbolMap = new Map<string, Completion>();

        for (const completion of BASE_PYTHON_COMPLETIONS) {
            symbolMap.set(completion.label, completion);
        }

        const addSymbol = (label: string, detail: string, type: Completion['type']) => {
            if (!label || symbolMap.has(label)) return;
            symbolMap.set(label, { label, detail, type });
        };

        for (const file of files) {
            const matches = file.content.match(/\b[A-Za-z_][A-Za-z0-9_]*\b/g) || [];
            for (const match of matches) {
                if (!PYTHON_KEYWORDS.includes(match)) {
                    addSymbol(match, 'file symbol', 'variable');
                }
            }

            const defMatches = file.content.matchAll(/\bdef\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)/g);
            for (const [, fnName, rawArgs] of defMatches) {
                addSymbol(fnName, 'function in project', 'function');
                for (const arg of rawArgs.split(',')) {
                    const cleanedArg = arg.trim().replace(/=.*/, '').replace(/:.*/, '');
                    if (cleanedArg && cleanedArg !== 'self' && cleanedArg !== 'cls') {
                        addSymbol(cleanedArg, 'parameter', 'variable');
                    }
                }
            }

            const classMatches = file.content.matchAll(/\bclass\s+([A-Za-z_][A-Za-z0-9_]*)/g);
            for (const [, className] of classMatches) {
                addSymbol(className, 'class in project', 'class');
            }
        }

        const completions = Array.from(symbolMap.values()).sort((a, b) => a.label.localeCompare(b.label));

        return (context: CompletionContext) => {
            const word = context.matchBefore(/[A-Za-z_][A-Za-z0-9_]*/);
            if (!word && !context.explicit) return null;

            const currentText = word?.text ?? '';
            const from = word?.from ?? context.pos;
            const options = completions
                .filter((completion) => completion.label.toLowerCase().startsWith(currentText.toLowerCase()))
                .slice(0, 200);

            return { from, options };
        };
    }, [files]);
    const toggleOutputHeight = () => {
        const nextExpanded = !isOutputExpanded;
        setIsOutputExpanded(nextExpanded);
        setOutputHeight(nextExpanded ? 320 : 85);
    };

    const stopEditorDeleteHold = () => {
        if (deleteHoldDelayRef.current !== null) {
            window.clearTimeout(deleteHoldDelayRef.current);
            deleteHoldDelayRef.current = null;
        }
        if (deleteHoldTimerRef.current !== null) {
            window.clearInterval(deleteHoldTimerRef.current);
            deleteHoldTimerRef.current = null;
        }
    };

    const deleteFromActiveEditor = () => {
        const view = activeEditorViewRef.current;
        if (!view) return;
        const mainScrollTop = mainScrollRef.current?.scrollTop ?? 0;
        const editorScrollTop = view.scrollDOM.scrollTop;
        const editorScrollLeft = view.scrollDOM.scrollLeft;
        deleteBackwardOnce(view);
        view.scrollDOM.scrollTop = editorScrollTop;
        view.scrollDOM.scrollLeft = editorScrollLeft;
        if (mainScrollRef.current) mainScrollRef.current.scrollTop = mainScrollTop;
        window.requestAnimationFrame(() => {
            view.scrollDOM.scrollTop = editorScrollTop;
            view.scrollDOM.scrollLeft = editorScrollLeft;
            if (mainScrollRef.current) mainScrollRef.current.scrollTop = mainScrollTop;
        });
        if (pendingNextProblem) setPendingNextProblem(false);
    };

    const startEditorDeleteHold = (event: React.PointerEvent<HTMLButtonElement>) => {
        event.preventDefault();
        event.currentTarget.blur();
        try {
            event.currentTarget.setPointerCapture(event.pointerId);
        } catch {
            // Some browsers do not allow pointer capture after preventDefault.
        }
        stopEditorDeleteHold();
        deleteFromActiveEditor();
        deleteHoldDelayRef.current = window.setTimeout(() => {
            deleteHoldTimerRef.current = window.setInterval(deleteFromActiveEditor, 55);
        }, 240);
    };

    const editorExtensions = useMemo(() => [
        python(),
        indentUnit.of("    "),
        holdBackspaceExtension,
        autocompletion({ override: [pythonCompletionSource, pythonSnippets] }),
        EditorView.lineWrapping,
        ...customPythonTheme
    ], [pythonCompletionSource]);

    if (bootStage !== 'launched') {
        return (
            <div className="fixed inset-0 z-[100] bg-[#040b16] flex flex-col items-center justify-start pt-16 p-8 text-center text-white overflow-y-auto animate-in fade-in duration-500">
                <div className="relative mb-8 flex-shrink-0">
                    <div className="absolute inset-0 bg-[#3b82f6]/20 blur-3xl rounded-full animate-pulse"></div>
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" className={`w-20 h-20 relative z-10 ${bootStage === 'loading' ? 'animate-bounce' : 'scale-110'}`} alt="Python" />
                </div>

                {bootStage === 'loading' ? (
                    <>
                        <Loader2 className="animate-spin text-[#3b82f6] mb-4" size={40} />
                        <h1 className="text-2xl font-black tracking-tighter mb-2 italic uppercase">Starting Engine...</h1>
                        <p className="text-[#3b82f6] text-[10px] font-mono tracking-widest mb-6 uppercase animate-pulse">{bootLog}</p>
                        <p className="text-gray-400 text-[11px] max-w-xs leading-relaxed mb-8">Caching Standard Library (20MB) for offline use.</p>
                        <div className="flex flex-col gap-3 w-full max-w-xs animate-in slide-in-from-bottom-4">
                            <button onClick={() => window.location.reload()} className="w-full bg-[#1d2d44] text-white py-4 rounded-2xl font-black text-[10px] uppercase border border-white/5 flex items-center justify-center gap-2"><RefreshCw size={14} /> Refresh</button>
                            <button onClick={forceResetCache} className="w-full bg-red-500/10 border border-red-500/20 text-red-500 py-4 rounded-2xl font-black text-[10px] uppercase flex items-center justify-center gap-2"><Trash2 size={14} /> Wipe Cache</button>
                        </div>
                    </>
                ) : (
                    <div className="animate-in fade-in zoom-in duration-500 flex flex-col items-center flex-shrink-0">
                        <h1 className="text-3xl font-black tracking-tighter mb-2 text-[#3b82f6]">LOCAL ENGINE READY</h1>
                        <p className="text-gray-400 text-xs mb-6 uppercase tracking-widest font-bold">Standard Library Loaded</p>
                        <button onClick={handleLaunch} className="mt-4 bg-[#3b82f6] text-white px-10 py-4 rounded-2xl font-black text-lg shadow-[0_0_40px_rgba(59,130,246,0.3)] active:scale-95 transition-all flex items-center gap-2"><Zap size={20} fill="currentColor" /> ENTER EDITOR</button>
                    </div>
                )}

                {isInFrame && (
                    <div className="mt-10 w-full max-w-sm">
                        <div className="bg-[#112240] border-2 border-dashed border-[#3b82f6]/30 p-6 rounded-[2rem] text-left shadow-2xl">
                            <h3 className="text-[#3b82f6] font-black text-xs uppercase mb-4">iPhone Preview</h3>
                            <button onClick={handleCopyLink} className={`w-full py-2.5 rounded-lg font-bold text-[10px] flex items-center justify-center gap-2 transition-all ${copyFeedback ? 'bg-[#22c55e] text-white' : 'bg-[#1d2d44] text-gray-300'}`}>
                                {copyFeedback ? <Check size={14} /> : <Copy size={14} />} {copyFeedback ? 'LINK COPIED' : 'COPY URL'}
                            </button>
                        </div>
                    </div>
                )}
            </div>
        );
    }

    return (
        <div
            className="h-screen bg-[#040b16] text-white flex flex-col max-w-2xl mx-auto overflow-hidden animate-in fade-in duration-700 relative"
        >
            <div
                ref={headerRef}
                className="fixed left-1/2 z-20 w-full max-w-2xl -translate-x-1/2 bg-[#040b16]"
                style={{
                    top: 0,
                    backgroundColor: 'rgba(4, 11, 22, 0.18)',
                    pointerEvents: 'none',
                    paddingTop: 'max(0.75rem, calc(env(safe-area-inset-top) + 0.75rem))',
                    paddingLeft: 'max(1rem, calc(var(--safe-area-inset-left, 0px) + 1rem))',
                    paddingRight: 'max(1rem, calc(var(--safe-area-inset-right, 0px) + 1rem))',
                    paddingBottom: '0.75rem'
                }}
            >
                <div className="flex items-center justify-center mb-3">
                    <div className="flex gap-3 sm:gap-5 items-center bg-[#0a1628] border border-[#1d2d44] px-3 py-2 rounded-full shadow-lg text-[10px] sm:text-xs font-black tracking-tight" style={{ pointerEvents: 'auto' }}>
                        <button onClick={() => setShowModal('api_key')} className="text-gray-400 hover:text-[#3b82f6] transition-all bg-[#050c18] p-1.5 rounded-full border border-[#1d2d44]" title="API key settings"><Key size={14} /></button>
                        <div className="flex items-center"><span className="text-[#3b82f6] mr-1 uppercase">Count:</span><span>{currentStats.shots}</span></div>
                        <div className="flex items-center"><span className="text-[#22c55e] mr-1 uppercase">Wins:</span><span>{currentStats.success}</span></div>
                        <div className="flex items-center"><span className="text-[#ef4444] mr-1 uppercase">Fail:</span><span>{currentStats.failed}</span></div>
                        <div className="flex items-center border-l border-[#1d2d44] pl-3 ml-1"><span className="text-[#f59e0b] mr-1 uppercase">Rate:</span><span>{rate}%</span></div>
                        <button onClick={() => setShowModal('settings')} className="text-gray-400 hover:text-[#3b82f6] transition-all bg-[#050c18] p-1.5 rounded-full border border-[#1d2d44]" title="Settings"><Settings size={14} /></button>
                    </div>
                </div>

                <div
                    ref={problemPanelRef}
                    className="bg-[#0a1628] rounded-xl border border-[#1d2d44] shadow-2xl overflow-hidden"
                    style={{
                        minHeight: '120px',
                        backgroundColor: 'rgba(8, 18, 34, 0.30)',
                        backdropFilter: 'blur(6px)',
                        WebkitBackdropFilter: 'blur(6px)',
                        borderColor: 'rgba(88, 118, 160, 0.35)',
                        pointerEvents: 'none'
                    }}
                >
                    <div className="flex items-center justify-between gap-3 px-4 pt-4 pb-2">
                        <h2 className="text-lg font-bold text-white m-0">Problem {exercise.id}</h2>
                        <div className="flex items-center gap-2">
                            <button
                                onClick={saveCurrentProblem}
                                title={isProblemSaved(exercise.id) ? 'Saved' : 'Save problem'}
                                style={{
                                    backgroundColor: isProblemSaved(exercise.id) ? 'rgba(59, 130, 246, 0.15)' : 'transparent',
                                    border: '1px solid #1d2d44',
                                    borderRadius: '0.5rem',
                                    padding: '0.25rem 0.5rem',
                                    color: '#3b82f6',
                                    cursor: 'pointer',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '0.25rem',
                                    fontSize: '0.75rem',
                                    flexShrink: 0,
                                    pointerEvents: 'auto',
                                    opacity: isProblemSaved(exercise.id) ? 1 : 0.7,
                                    transition: 'all 0.2s ease'
                                }}
                            >
                                <Bookmark size={14} fill={isProblemSaved(exercise.id) ? 'currentColor' : 'none'} />
                                <span>{isProblemSaved(exercise.id) ? 'Saved' : 'Save'}</span>
                            </button>
                            <button
                                onClick={() => {
                                    setPendingNextProblem(false);
                                    loadRandomExercise();
                                }}
                                style={{
                                    backgroundColor: 'transparent',
                                    border: '1px solid #1d2d44',
                                    borderRadius: '0.5rem',
                                    padding: '0.25rem 0.5rem',
                                    color: '#3b82f6',
                                    cursor: 'pointer',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '0.25rem',
                                    fontSize: '0.75rem',
                                    flexShrink: 0,
                                    pointerEvents: 'auto'
                                }}
                                title="Load next problem"
                            >
                                <SkipForward size={14} />
                                <span>Next</span>
                            </button>
                            <button
                                onClick={() => setShowModal('problem_full')}
                                style={{
                                    backgroundColor: 'transparent',
                                    border: '1px solid #1d2d44',
                                    borderRadius: '0.5rem',
                                    padding: '0.25rem 0.5rem',
                                    color: '#3b82f6',
                                    cursor: 'pointer',
                                    display: 'flex',
                                    alignItems: 'center',
                                    gap: '0.25rem',
                                    fontSize: '0.75rem',
                                    flexShrink: 0,
                                    pointerEvents: 'auto'
                                }}
                            >
                                <ExternalLink size={14} />
                                <span>View Full</span>
                            </button>
                        </div>
                    </div>
                    <pre
                        data-problem-description
                        className="problem-description-scroll"
                        id={`problem-desc-${exercise.id}`}
                        ref={problemDescriptionRef}
                        style={{
                            color: '#d1d5db',
                            fontSize: '0.875rem',
                            lineHeight: '1.75',
                            whiteSpace: 'pre-wrap',
                            wordWrap: 'break-word',
                            overflowWrap: 'break-word',
                            maxHeight: '28vh',
                            minHeight: '84px',
                            overflowY: 'auto',
                            overflowX: 'hidden',
                            padding: '0.5rem 1rem 1rem',
                            margin: 0,
                            fontFamily: 'inherit',
                            textOverflow: 'clip',
                            display: 'block',
                            WebkitLineClamp: 'unset',
                            lineClamp: 'unset',
                            width: '100%',
                            WebkitOverflowScrolling: 'touch',
                            touchAction: 'pan-y',
                            overscrollBehavior: 'contain'
                        }}
                    >
                        {exercise.description}
                    </pre>
                </div>
            </div>

            <div
                className="fixed left-1/2 z-[110] w-full max-w-2xl -translate-x-1/2 px-4"
                style={{
                    top: `${editorToolbarTop}px`,
                    pointerEvents: 'none'
                }}
            >
                <div
                    className="flex items-center justify-between rounded-xl border border-[#5f7fa6] bg-[#0d1b2a] p-2 shadow-2xl shadow-black/40"
                    style={{ pointerEvents: 'auto' }}
                >
                    <div className="flex items-center gap-2 overflow-hidden">
                        <button onClick={startRenaming} className="p-1 hover:bg-[#1d2d44] rounded-full text-gray-400"><Pencil size={14} /></button>
                        {isEditingFileName ? (
                            <input autoFocus value={newName} onChange={(e) => setNewName(e.target.value)} onBlur={finishRenaming} onKeyDown={(e) => e.key === 'Enter' && finishRenaming()} className="bg-[#112240] text-sm border border-[#3b82f6] rounded px-2 py-0.5 outline-none text-white w-24" />
                        ) : (
                            <span className="text-sm font-bold text-gray-300 font-mono truncate max-w-[100px]">{files[activeFileIndex].name}</span>
                        )}
                    </div>
                    <div className="flex items-center gap-1">
                        <button onClick={addFile} className="p-1.5 hover:bg-[#1d2d44] rounded-full text-[#22c55e]"><Plus size={18} /></button>
                        <button onClick={removeFile} disabled={files.length <= 1} className="p-1.5 hover:bg-[#1d2d44] rounded-full text-[#ef4444] disabled:opacity-30"><Minus size={18} /></button>
                        <button
                            onPointerDown={startEditorDeleteHold}
                            onPointerUp={stopEditorDeleteHold}
                            onPointerCancel={stopEditorDeleteHold}
                            onPointerLeave={stopEditorDeleteHold}
                            onContextMenu={(event) => event.preventDefault()}
                            className="select-none px-2 py-1 rounded-lg border border-[#22c55e]/40 bg-[#22c55e]/10 text-[#22c55e] text-sm font-black active:scale-95"
                            style={{ touchAction: 'none' }}
                            title="Hold to delete"
                        >
                            &lt;
                        </button>
                        <button onClick={runCode} disabled={isRunning} className={runButtonClass}>
                            {isRunning ? <Loader2 size={12} className="animate-spin" /> : <Play size={12} fill="currentColor" />} {runButtonLabel}
                        </button>
                    </div>
                </div>
            </div>

            <div
                ref={mainScrollRef}
                className="flex-1 overflow-y-auto overflow-x-hidden px-4"
                style={{
                    paddingTop: `${editorContentTop}px`,
                    paddingBottom: `max(16rem, calc(env(safe-area-inset-bottom) + ${Math.max(headerHeight + problemPanelHeight + 300, 620)}px))`,
                    scrollPaddingTop: `${editorContentTop}px`,
                    WebkitOverflowScrolling: 'touch',
                    overscrollBehaviorY: 'contain'
                }}
            >
                <div
                    data-editor-panel
                    className="mb-28 bg-[#0a1628] rounded-xl flex flex-col shadow-2xl border border-[#5f7fa6] overflow-hidden"
                    style={{ scrollMarginTop: `${editorContentTop + 12}px` }}
                >
                    <div
                        className="hidden"
                    >
                        <div className="flex items-center gap-2 overflow-hidden">
                            <button onClick={startRenaming} className="p-1 hover:bg-[#1d2d44] rounded-full text-gray-400"><Pencil size={14} /></button>
                            {isEditingFileName ? (
                                <input autoFocus value={newName} onChange={(e) => setNewName(e.target.value)} onBlur={finishRenaming} onKeyDown={(e) => e.key === 'Enter' && finishRenaming()} className="bg-[#112240] text-sm border border-[#3b82f6] rounded px-2 py-0.5 outline-none text-white w-24" />
                            ) : (
                                <span className="text-sm font-bold text-gray-300 font-mono truncate max-w-[100px]">{files[activeFileIndex].name}</span>
                            )}
                        </div>
                        <div className="flex items-center gap-1">
                            <button onClick={addFile} className="p-1.5 hover:bg-[#1d2d44] rounded-full text-[#22c55e]"><Plus size={18} /></button>
                            <button onClick={removeFile} disabled={files.length <= 1} className="p-1.5 hover:bg-[#1d2d44] rounded-full text-[#ef4444] disabled:opacity-30"><Minus size={18} /></button>
                            <button onClick={runCode} disabled={isRunning} className={runButtonClass}>
                                {isRunning ? <Loader2 size={12} className="animate-spin" /> : <Play size={12} fill="currentColor" />} {runButtonLabel}
                            </button>
                        </div>
                    </div>
                    <div
                        className="flex bg-[#0a1628] border-b border-[#1d2d44] overflow-x-auto no-scrollbar"
                        style={{ position: 'sticky', top: 0, zIndex: 50 }}
                    >
                        {files.map((f, idx) => (
                            <button key={idx} onClick={() => setActiveFileIndex(idx)} className={`px-4 py-1.5 text-[10px] font-bold tracking-wider transition-all border-r border-[#1d2d44] whitespace-nowrap ${activeFileIndex === idx ? 'bg-[#050c18] text-[#3b82f6] border-b-2 border-b-[#3b82f6]' : 'text-gray-500'}`}>
                                {f.name}
                            </button>
                        ))}
                    </div>
                    <div ref={editorShellRef} className="flex-grow bg-[#050c18] relative border-b border-[#5f7fa6]" style={{ minHeight: '320px', scrollMarginTop: `${editorContentTop}px` }}>
                        <CodeMirror
                            value={files[activeFileIndex].content} height="320px" extensions={editorExtensions} onChange={updateActiveContent}
                            onCreateEditor={(view) => {
                                activeEditorViewRef.current = view;
                                const dom = view.contentDOM;
                                const startLongPress = (e: MouseEvent | TouchEvent) => {
                                    const pos = 'touches' in e ? { x: e.touches[0].clientX, y: e.touches[0].clientY } : { x: e.clientX, y: e.clientY };
                                    longPressTimerRef.current = setTimeout(() => {
                                        setContextMenu({ x: pos.x, y: pos.y });
                                    }, 500);
                                };
                                const cancelLongPress = () => {
                                    if (longPressTimerRef.current) {
                                        clearTimeout(longPressTimerRef.current);
                                        longPressTimerRef.current = null;
                                    }
                                };
                                const handleKeyboardFeedback = (event: KeyboardEvent) => {
                                    if (event.metaKey || event.ctrlKey || event.altKey) return;
                                    if (event.key.length === 1 || event.key === 'Enter' || event.key === 'Backspace' || event.key === 'Tab') {
                                        playKeyboardFeedback();
                                    }
                                };
                                dom.addEventListener('mousedown', startLongPress);
                                dom.addEventListener('touchstart', startLongPress, { passive: true });
                                dom.addEventListener('mouseup', cancelLongPress);
                                dom.addEventListener('touchend', cancelLongPress);
                                dom.addEventListener('touchmove', cancelLongPress);
                                dom.addEventListener('mousemove', cancelLongPress);
                                dom.addEventListener('keydown', handleKeyboardFeedback);
                            }}
                            basicSetup={{ lineNumbers: true, autocompletion: true, bracketMatching: true, closeBrackets: true, indentOnInput: true }}
                        />
                        {contextMenu && (
                            <>
                                <div className="fixed inset-0 z-30" onClick={() => setContextMenu(null)} />
                                <div className="fixed z-40 bg-[#0a1628] border border-[#1d2d44] rounded-lg shadow-2xl py-1 min-w-[160px]" style={{ left: contextMenu.x, top: contextMenu.y }}>
                                    <button onClick={() => { const v = activeEditorViewRef.current; if (v) { v.dispatch({ selection: { anchor: 0, head: v.state.doc.length } }); v.focus(); } setContextMenu(null); }} className="w-full text-left px-4 py-2 text-xs text-white hover:bg-[#1d2d44] transition-colors flex items-center gap-2">
                                        <MousePointer2 size={12} /> Select All
                                    </button>
                                    <button onClick={() => { const v = activeEditorViewRef.current; if (v) { navigator.clipboard.writeText(v.state.sliceDoc(0, v.state.doc.length)); } setContextMenu(null); }} className="w-full text-left px-4 py-2 text-xs text-white hover:bg-[#1d2d44] transition-colors flex items-center gap-2">
                                        <Copy size={12} /> Copy All
                                    </button>
                                    <button onClick={() => { const v = activeEditorViewRef.current; if (v) { v.dispatch({ changes: { from: 0, to: v.state.doc.length } }); v.focus(); } setContextMenu(null); }} className="w-full text-left px-4 py-2 text-xs text-white hover:bg-[#1d2d44] transition-colors flex items-center gap-2">
                                        <Trash2 size={12} /> Delete All
                                    </button>
                                </div>
                            </>
                        )}
                    </div>
                    <div className="bg-[#0a1628] flex-shrink-0">
                        <div className="flex items-center justify-between px-2 py-1 border-b border-[#1d2d44]">
                            <span className="text-xs font-bold text-gray-400 uppercase tracking-wider">Output</span>
                            <button
                                onClick={toggleOutputHeight}
                                className="text-gray-400 hover:text-[#3b82f6] transition-all px-2 py-1 flex items-center gap-1 text-[11px] font-bold"
                                title={isOutputExpanded ? "Collapse" : "Expand"}
                            >
                                <span>{isOutputExpanded ? 'Smaller' : 'Larger'}</span>
                                {isOutputExpanded ? <ChevronDown size={14} /> : <ChevronUp size={14} />}
                            </button>
                        </div>
                        <div
                            ref={outputRef}
                            className="overflow-y-auto px-2 py-2"
                            style={{
                                height: `${outputHeight}px`,
                                minHeight: '85px',
                                maxHeight: '55vh',
                                border: outputStatus === 'win'
                                    ? '2px solid rgba(34, 197, 94, 0.75)'
                                    : outputStatus === 'fail'
                                        ? '2px solid rgba(239, 68, 68, 0.75)'
                                        : outputStatus === 'info'
                                            ? '1px solid rgba(59, 130, 246, 0.55)'
                                            : '1px solid rgba(95, 127, 166, 0.25)',
                                borderRadius: '0.75rem',
                                backgroundColor: outputStatus === 'win'
                                    ? 'rgba(12, 45, 28, 0.45)'
                                    : outputStatus === 'fail'
                                        ? 'rgba(64, 15, 20, 0.45)'
                                        : outputStatus === 'running'
                                            ? 'rgba(30, 41, 59, 0.45)'
                                            : 'rgba(5, 12, 24, 0.45)',
                                boxShadow: outputStatus === 'win'
                                    ? '0 0 22px rgba(34, 197, 94, 0.18)'
                                    : outputStatus === 'fail'
                                        ? '0 0 22px rgba(239, 68, 68, 0.18)'
                                        : 'none',
                                transition: 'max-height 0.2s ease, height 0.2s ease',
                                WebkitOverflowScrolling: 'touch',
                                touchAction: 'pan-y',
                                overscrollBehavior: 'contain',
                                overflowY: 'scroll'
                            }}
                        >
                            <pre className="text-[10px] font-mono text-[#4ade80] whitespace-pre-wrap select-text break-words">{output}</pre>
                        </div>
                        {waitingForInput && (
                            <div className="mt-2 flex items-center gap-2 rounded-xl border border-[#3b82f6]/40 bg-[#071225]/90 px-2 py-2">
                                <span className="min-w-0 flex-1 truncate text-[10px] font-bold uppercase tracking-[0.12em] text-[#93c5fd]">
                                    {inputPrompt || 'Input'}
                                </span>
                                <input
                                    value={stdinDraft}
                                    onChange={(event) => setStdinDraft(event.target.value)}
                                    onKeyDown={(event) => {
                                        if (event.key === 'Enter') {
                                            event.preventDefault();
                                            submitInputValue();
                                        }
                                    }}
                                    autoFocus
                                    className="min-w-0 flex-[2] rounded-lg border border-[#1d2d44] bg-[#050c18] px-2 py-1 text-xs text-white outline-none focus:border-[#3b82f6]"
                                    placeholder="Type input value..."
                                />
                                <button
                                    onClick={submitInputValue}
                                    className="rounded-lg border border-[#22c55e]/40 bg-[#22c55e]/10 px-3 py-1 text-xs font-black text-[#22c55e]"
                                >
                                    Send
                                </button>
                            </div>
                        )}
                        <div className="border-t border-[#1d2d44] bg-[#071225]">
                            <button
                                onClick={() => setShowActionPanel(prev => !prev)}
                                className="w-full flex items-center justify-center gap-2 px-3 py-2 text-[11px] font-black uppercase tracking-[0.18em] text-gray-300 hover:text-[#3b82f6] transition-colors"
                            >
                                <span>{showActionPanel ? 'Hide Tools' : 'Show Tools'}</span>
                                {showActionPanel ? <ChevronDown size={14} /> : <ChevronUp size={14} />}
                            </button>
                            {showActionPanel && (
                                <div className="flex justify-center gap-2 sm:gap-3 px-2 pb-3 animate-in fade-in slide-in-from-top-1 duration-200">
                                    <ActionButton icon={<Book size={16} />} color="rgba(245, 158, 11, 0.15)" borderColor="rgba(245, 158, 11, 0.3)" iconColor="#f59e0b" description="Info" onClick={() => { setShowModal('instructions'); setModalTab('how'); }} />
                                    <ActionButton icon={<Lightbulb size={16} />} color="rgba(59, 130, 246, 0.15)" borderColor="rgba(59, 130, 246, 0.3)" iconColor="#3b82f6" description="Sol" onClick={() => setShowModal('solution')} />
                                    <ActionButton icon={<Bot size={16} />} color="rgba(139, 92, 246, 0.15)" borderColor="rgba(139, 92, 246, 0.3)" iconColor="#8b5cf6" description="AI" onClick={handleAiHint} />
                                    <ActionButton icon={<CheckCircle size={16} />} color="rgba(34, 197, 94, 0.15)" borderColor="rgba(34, 197, 94, 0.3)" iconColor="#22c55e" description="Win" onClick={handleMarkSuccess} />
                                    <ActionButton icon={<XCircle size={16} />} color="rgba(239, 68, 68, 0.15)" borderColor="rgba(239, 68, 68, 0.3)" iconColor="#ef4444" description="Failed" onClick={handleMarkFailed} />
                                    <ActionButton icon={<RotateCcw size={16} />} color="rgba(249, 115, 22, 0.15)" borderColor="rgba(249, 115, 22, 0.3)" iconColor="#f97316" description="Reset" onClick={() => { setResetConfirmArmed(false); setShowModal('restart_confirm'); }} />
                                </div>
                            )}
                        </div>
                        <div className="h-2 flex-shrink-0 border-t border-[#5f7fa6] bg-[#13233a]" />
                    </div>
                </div>
            </div>

            {/* Fixed footer - centered version button */}
            <div className="fixed bottom-0 left-1/2 -translate-x-1/2 w-full max-w-2xl z-20 bg-[#040b16] border-t border-[#1d2d44] py-2 px-4" style={{ paddingBottom: 'max(0.5rem, env(safe-area-inset-bottom))' }}>
                <div className="relative flex items-center justify-center">
                    <button onClick={forceRefreshToNewest} className="flex items-center gap-2 text-gray-400 hover:text-[#3b82f6] transition-colors px-3 py-2 rounded-full border border-[#1d2d44] bg-[#0a1628] hover:border-[#3b82f6]/50" title="Refresh to newest version">
                        <RefreshCw size={18} />
                        <span className="text-xs font-bold tracking-tight">{typeof window !== 'undefined' && (window as any).APP_VERSION || 'PythonV2'}</span>
                        <span className="rounded-full border border-[#3b82f6]/35 bg-[#3b82f6]/10 px-2 py-0.5 text-[10px] font-black uppercase tracking-[0.14em] text-[#93c5fd]">{selectedModeLabel}</span>
                    </button>
                </div>
            </div>

            {showModal !== 'none' && (
                <div
                    className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 z-[120] animate-in fade-in duration-200"
                    style={{
                        paddingTop: 'max(1rem, calc(env(safe-area-inset-top) + 1rem))',
                        paddingBottom: 'max(1rem, calc(env(safe-area-inset-bottom) + 1rem))',
                        paddingLeft: 'max(1rem, calc(env(safe-area-inset-left) + 1rem))',
                        paddingRight: 'max(1rem, calc(env(safe-area-inset-right) + 1rem))'
                    }}
                >
                    <div
                        className="rounded-3xl p-4 sm:p-6 max-w-4xl w-full border border-[#1d2d44] shadow-2xl relative flex flex-col overflow-hidden"
                        style={{
                            backgroundColor: showModal === 'settings' ? 'rgba(17, 34, 64, 0.20)' : '#112240',
                            backdropFilter: showModal === 'settings' ? 'blur(18px)' : undefined,
                            WebkitBackdropFilter: showModal === 'settings' ? 'blur(18px)' : undefined,
                            height: 'calc(100dvh - 2rem - env(safe-area-inset-top) - env(safe-area-inset-bottom))',
                            maxHeight: 'calc(100dvh - 2rem - env(safe-area-inset-top) - env(safe-area-inset-bottom))'
                        }}
                    >
                        <button onClick={() => setShowModal('none')} className="absolute top-4 right-4 text-gray-400 z-10"><X size={24} /></button>
                        {showModal === 'instructions' && (
                            <div className="flex flex-col h-full">
                                <div className="flex gap-4 mb-4 border-b border-[#1d2d44]">
                                    <TabButton active={modalTab === 'how'} onClick={() => setModalTab('how')} label="Guide" />
                                    <TabButton active={modalTab === 'cheat'} onClick={() => setModalTab('cheat')} label="Cheat" />
                                    <TabButton active={modalTab === 'glossary'} onClick={() => setModalTab('glossary')} label="Glossary" />
                                    <TabButton active={modalTab === 'regex'} onClick={() => setModalTab('regex')} label="Regex" />
                                </div>
                                <div className="overflow-y-auto text-xs text-gray-300 space-y-4 flex-grow">
                                    {modalTab === 'how' && <p className="select-text">For full offline mode, add to <b>Home Screen</b>. Python logic is executed locally.</p>}
                                    {modalTab === 'cheat' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44]">
                                            <CodeMirror
                                                value={CHEAT_CONTENT}
                                                height="400px"
                                                readOnly={true}
                                                extensions={[python(), ...customPythonTheme]}
                                                basicSetup={{ lineNumbers: false, foldGutter: false }}
                                            />
                                        </div>
                                    )}
                                    {modalTab === 'glossary' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-auto h-[400px] p-4 border border-[#1d2d44]">
                                            <pre className="text-[#4ade80] font-mono text-xs whitespace-pre-wrap select-text m-0">{GLOSSARY_CONTENT}</pre>
                                        </div>
                                    )}
                                    {modalTab === 'regex' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44]">
                                            <CodeMirror
                                                value={REGEX_CONTENT}
                                                height="400px"
                                                readOnly={true}
                                                extensions={[python(), ...customPythonTheme]}
                                                basicSetup={{ lineNumbers: false, foldGutter: false }}
                                            />
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                        {showModal === 'solution' && (
                            <div className="flex flex-col h-full overflow-hidden">
                                <div className="flex gap-4 mb-4 border-b border-[#1d2d44] mx-1 mt-1">
                                    <TabButton active={solutionTab === 'code'} onClick={() => setSolutionTab('code')} label="Solution" />
                                    <TabButton active={solutionTab === 'logic'} onClick={() => setSolutionTab('logic')} label="Logic" />
                                    <TabButton active={solutionTab === 'requirements'} onClick={() => setSolutionTab('requirements')} label="Requirements" />
                                </div>
                                <div className="flex-grow overflow-y-auto">
                                    {solutionTab === 'code' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={exercise.solution} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={exercise.solution} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...customPythonTheme]} />
                                            </div>
                                        </div>
                                    )}
                                    {solutionTab === 'logic' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={logicContent || ''} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                {logicContent ? (
                                                    <CodeMirror value={logicContent} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...customPythonTheme]} />
                                                ) : (
                                                    <div className="p-8 text-center text-gray-500 text-sm">
                                                        Searching logic documentation...
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    )}
                                    {solutionTab === 'requirements' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={requirementsContent || ''} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                {requirementsContent ? (
                                                    <CodeMirror value={requirementsContent} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...customPythonTheme]} />
                                                ) : (
                                                    <div className="p-8 text-center text-gray-500 text-sm">
                                                        Searching requirements...
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                        {showModal === 'hint' && (
                            <div className="flex flex-col">
                                <h2 className="text-lg font-bold mb-3 text-[#8b5cf6]">AI Analysis</h2>
                                <div className="bg-[#0d1b2a] p-3 rounded-xl border border-[#1d2d44] text-gray-200 italic mb-3 text-xs">{aiHintText}</div>
                            </div>
                        )}
                        {showModal === 'settings' && (
                            <div className="flex h-full min-h-0 flex-col py-2">
                                <h2 className="mb-4 flex-shrink-0 text-center text-lg font-bold">Settings</h2>
                                <div className="min-h-0 flex-1 overflow-y-auto overscroll-contain pr-1 pb-8">

                                <div className="mb-6">
                                    <label className="block text-sm font-bold mb-2 text-gray-200">
                                        Problem Mode
                                    </label>
                                    <div className="grid grid-cols-1 gap-2">
                                        {DIFFICULTY_MODES.map(mode => {
                                            const isSelected = difficultyMode === mode.id;
                                            return (
                                                <button
                                                    key={mode.id}
                                                    onClick={() => handleDifficultyModeSelect(mode.id)}
                                                    className={`w-full rounded-xl border px-3 py-2 text-left transition-all ${isSelected ? 'border-[#3b82f6] bg-[#3b82f6]/25 text-white' : 'border-[#1d2d44] bg-[#071225]/70 text-gray-300 hover:border-[#3b82f6]/50'}`}
                                                >
                                                    <span className="flex items-center justify-between gap-3">
                                                        <span className="text-xs font-black uppercase tracking-[0.16em]">{mode.label}</span>
                                                        {isSelected && <Check size={14} className="text-[#93c5fd]" />}
                                                    </span>
                                                    <span className="mt-1 block text-[10px] text-gray-400">{mode.description}</span>
                                                </button>
                                            );
                                        })}
                                    </div>
                                    <p className="mt-2 text-[10px] text-gray-300">
                                        Current mode has {modeExerciseCount} matching problems. Normal mode uses all problems.
                                    </p>
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-gray-200">Stats By Mode</h3>
                                    <div className="space-y-2">
                                        {DIFFICULTY_MODES.map(mode => {
                                            const modeStats = statsByMode[mode.id] ?? EMPTY_STATS;
                                            const modeRate = modeStats.shots > 0 ? ((modeStats.success / modeStats.shots) * 100).toFixed(0) : '0';
                                            return (
                                                <div key={mode.id} className="flex items-center justify-between gap-3 text-[11px] text-gray-300">
                                                    <span className="font-bold uppercase tracking-[0.12em] text-gray-200">{mode.label}</span>
                                                    <span className="font-mono">S:{modeStats.shots} W:{modeStats.success} F:{modeStats.failed} R:{modeRate}%</span>
                                                </div>
                                            );
                                        })}
                                    </div>
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 flex items-center gap-2 text-xs font-black uppercase tracking-[0.16em] text-gray-200">
                                        <SlidersHorizontal size={14} className="text-[#3b82f6]" />
                                        Customize
                                    </h3>
                                    <div className="grid grid-cols-2 gap-2">
                                        <button
                                            onClick={() => setKeyboardHaptics(prev => !prev)}
                                            className={`rounded-xl border px-3 py-3 text-left transition-all ${keyboardHaptics ? 'border-[#22c55e]/60 bg-[#22c55e]/15 text-white' : 'border-[#1d2d44] bg-[#050c18]/70 text-gray-400'}`}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <Vibrate size={15} className={keyboardHaptics ? 'text-[#22c55e]' : 'text-gray-500'} />
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]">{keyboardHaptics ? 'On' : 'Off'}</span>
                                            </span>
                                            <span className="block text-xs font-bold">Haptic</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">Tiny vibration while typing.</span>
                                        </button>
                                        <button
                                            onClick={() => setKeyboardSound(prev => !prev)}
                                            className={`rounded-xl border px-3 py-3 text-left transition-all ${keyboardSound ? 'border-[#22c55e]/60 bg-[#22c55e]/15 text-white' : 'border-[#1d2d44] bg-[#050c18]/70 text-gray-400'}`}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <Volume2 size={15} className={keyboardSound ? 'text-[#22c55e]' : 'text-gray-500'} />
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]">{keyboardSound ? 'On' : 'Off'}</span>
                                            </span>
                                            <span className="block text-xs font-bold">Sound</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">Soft key click in editor.</span>
                                        </button>
                                    </div>
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-gray-200 flex items-center gap-2">
                                        <Bookmark size={14} className="text-[#3b82f6]" /> Saved Problems
                                    </h3>
                                    {savedProblems.length === 0 ? (
                                        <p className="text-[11px] text-gray-400 italic">No saved problems yet. Press Save on any problem to add it here.</p>
                                    ) : (
                                        <div className="space-y-2 max-h-[240px] overflow-y-auto pr-1">
                                            {savedProblems.map(problem => (
                                                <div
                                                    key={problem.exerciseId}
                                                    className="flex items-center justify-between gap-2 rounded-lg border border-[#1d2d44] bg-[#050c18] px-3 py-2"
                                                >
                                                    <button
                                                        onClick={() => loadSavedProblem(problem)}
                                                        className="flex-1 text-left min-w-0"
                                                    >
                                                        <span className="text-[11px] font-bold text-gray-200 block truncate">
                                                            Problem {problem.exerciseId}
                                                            {problem.mastered && (
                                                                <span className="ml-2 text-[10px] text-[#22c55e] font-black uppercase tracking-wider">Mastered</span>
                                                            )}
                                                        </span>
                                                        <span className="text-[10px] text-gray-400 block truncate">
                                                            {problem.description.split('\n')[0]}
                                                        </span>
                                                    </button>
                                                    <div className="flex items-center gap-1 flex-shrink-0">
                                                        {!problem.mastered && (
                                                            <button
                                                                onClick={() => markSavedProblemMastered(problem.exerciseId)}
                                                                title="Mark as mastered"
                                                                className="p-1.5 rounded-md hover:bg-[#22c55e]/20 text-[#22c55e] transition-colors"
                                                            >
                                                                <CheckCircle size={14} />
                                                            </button>
                                                        )}
                                                        <button
                                                            onClick={() => deleteSavedProblem(problem.exerciseId)}
                                                            title="Remove"
                                                            className="p-1.5 rounded-md hover:bg-red-500/20 text-red-500 transition-colors"
                                                        >
                                                            <Trash2 size={14} />
                                                        </button>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>

                                </div>
                                <button onClick={() => { setResetConfirmArmed(false); setShowModal('restart_confirm'); }} className="w-full flex-shrink-0 border border-red-500/30 text-red-500 py-3 rounded-xl hover:bg-red-500/10 transition-colors">Reset Progress</button>
                            </div>
                        )}
                        {showModal === 'api_key' && (
                            <div className="py-2">
                                <h2 className="text-lg font-bold mb-4 text-center">API Key</h2>
                                <div className="mb-6">
                                    <label className="block text-sm font-bold mb-2 text-gray-300">
                                        <Key size={14} className="inline mr-1" /> Gemini API Key
                                    </label>
                                    <input
                                        type="text"
                                        value={apiKey}
                                        onChange={(e) => setApiKey(e.target.value)}
                                        placeholder="Paste your API key here..."
                                        className="w-full bg-[#0d1b2a] border border-[#1d2d44] text-white px-4 py-3 rounded-xl text-sm font-mono focus:outline-none focus:border-[#3b82f6] transition-colors"
                                    />
                                    <p className="text-[10px] text-gray-400 mt-2 leading-relaxed">
                                        Get your API key from{' '}
                                        <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noreferrer" className="text-[#3b82f6] underline inline-flex items-center gap-0.5">
                                            Google AI Studio <ExternalLink size={10} />
                                        </a>
                                    </p>
                                </div>
                                <button
                                    onClick={() => {
                                        localStorage.setItem('gemini_api_key', apiKey);
                                        setShowModal('none');
                                    }}
                                    className="w-full bg-[#3b82f6] text-white font-bold py-4 rounded-xl flex items-center justify-center gap-2 hover:bg-[#3b82f6]/90 transition-colors"
                                >
                                    <Check size={18} /> Save API Key
                                </button>
                            </div>
                        )}
                        {showModal === 'restart_confirm' && (
                            <div className="text-center py-4">
                                <h2 className="text-lg font-bold mb-2">{resetConfirmArmed ? 'Final Warning' : 'Clear Stats?'}</h2>
                                <p className="text-xs text-gray-300 mb-4 leading-relaxed">
                                    {resetConfirmArmed
                                        ? 'This will permanently reset shots, wins, fails, and rate for every mode. This cannot be undone.'
                                        : 'Resetting clears progress stats for Normal, Beginner, Intermediate, Expert, and Legend. Press Reset Now once more to confirm.'}
                                </p>
                                <button
                                    onClick={() => {
                                        if (resetConfirmArmed) {
                                            handleRestartProgress();
                                            return;
                                        }
                                        setResetConfirmArmed(true);
                                    }}
                                    className={`w-full py-4 rounded-xl font-bold mb-3 ${resetConfirmArmed ? 'bg-red-600 text-white' : 'bg-red-500/20 text-red-300 border border-red-500/40'}`}
                                >
                                    {resetConfirmArmed ? 'Yes, Reset Everything' : 'Reset Now'}
                                </button>
                                <button onClick={() => { setResetConfirmArmed(false); setShowModal('none'); }} className="w-full bg-[#1d2d44] py-4 rounded-xl">Cancel</button>
                            </div>
                        )}
                        {showModal === 'problem_full' && (
                            <div className="flex flex-col h-full overflow-hidden">
                                <h2 className="text-lg font-bold mb-3 text-[#3b82f6]">Problem {exercise.id} - Full Description</h2>
                                <div
                                    className="bg-[#0d1b2a] p-4 rounded-xl border border-[#1d2d44] text-gray-200 text-sm leading-relaxed whitespace-pre-wrap break-words overflow-y-auto flex-grow"
                                    style={{
                                        maxHeight: '60vh',
                                        minHeight: '200px',
                                        overflowY: 'auto',
                                        overflowX: 'hidden'
                                    }}
                                >
                                    <pre style={{
                                        margin: 0,
                                        padding: 0,
                                        fontFamily: 'inherit',
                                        whiteSpace: 'pre-wrap',
                                        wordWrap: 'break-word',
                                        overflowWrap: 'break-word'
                                    }}>
                                        {exercise.description}
                                    </pre>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

const ActionButton: React.FC<{ icon: React.ReactNode, color: string, borderColor: string, iconColor: string, description: string, onClick: () => void }> = ({ icon, color, borderColor, iconColor, description, onClick }) => (
    <button onClick={onClick} style={{ backgroundColor: color, borderColor: borderColor, color: iconColor, pointerEvents: 'auto' }} className="w-[42px] h-[42px] rounded-full flex flex-col items-center justify-center shadow-lg active:scale-90 transition-all border border-white/5">
        {icon}
        <span className="text-[6px] font-bold mt-0.5 uppercase tracking-tighter">{description}</span>
    </button>
);

const TabButton: React.FC<{ active: boolean, onClick: () => void, label: string }> = ({ active: isActive, onClick, label }) => (
    <button onClick={onClick} className={`pb-2 px-1 font-bold transition-all text-xs ${isActive ? 'text-white border-b-2 border-[#3b82f6]' : 'text-gray-500'}`}>{label}</button>
);

const X = ({ size, className }: { size: number, className?: string }) => (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M18 6 6 18" /><path d="m6 6 12 12" /></svg>
);

export default App;
