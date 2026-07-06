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
    FileText,
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
    Bookmark,
    Terminal
} from 'lucide-react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { indentUnit } from '@codemirror/language';
import { autocompletion, snippetCompletion, CompletionContext, Completion } from '@codemirror/autocomplete';
import { EditorView } from '@codemirror/view';
import { EditorSelection } from '@codemirror/state';
import { EXERCISES } from './exercises';
import { Exercise, Stats } from './types';
import { AiReviewRequest, AiReviewResult, OfflineAiStatus } from './aiReviewTypes';
import { DEFAULT_OFFLINE_AI_STATE, answerProblemQuestionWithAvailableAi, downloadOfflineAiModel, loadOfflineAiState, removeOfflineAiModel, reviewWithAvailableAi, saveOfflineAiState } from './services/offlineAiReviewer';
import { buildDiagnosticReview } from './services/aiReviewDiagnostics';
import { createCustomPythonTheme, DEFAULT_EDITOR_COLORS, EditorColorSettings } from './editorTheme';
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
    output?: string;
}

interface ProblemAiMessage {
    id: number;
    role: 'user' | 'assistant';
    text: string;
    source?: 'built_in' | 'offline' | 'user';
}

const AI_AUTO_WIN_MIN_CONFIDENCE = 0.75;
const AI_AUTO_WIN_MODEL_SOURCES: ReadonlySet<AiReviewResult['source']> = new Set(['offline_model', 'ollama', 'gemini']);

const isAiAutoWinReview = (review: AiReviewResult) => (
    AI_AUTO_WIN_MODEL_SOURCES.has(review.source) &&
    review.verdict === 'likely_correct' &&
    review.confidence >= AI_AUTO_WIN_MIN_CONFIDENCE
);

const formatAiReviewHintText = (review: AiReviewResult) => (
    `${review.verdict.replace('_', ' ').toUpperCase()}\n\n${review.explanation}${review.suggestedFix ? `\n\nSuggested fix: ${review.suggestedFix}` : ''}`
);

const getOfflineAiStatusLabel = (status: OfflineAiStatus) => {
    switch (status) {
        case 'failed':
            return 'model unavailable';
        case 'unsupported':
            return 'unsupported here';
        case 'not_installed':
            return 'not installed';
        default:
            return status;
    }
};

const getAiReviewSourceLabel = (source: AiReviewResult['source']) => {
    switch (source) {
        case 'offline_model':
            return 'offline model';
        case 'gemini':
            return 'Gemini AI';
        case 'ollama':
            return 'local AI (Ollama)';
        case 'diagnostic':
            return 'built-in offline';
        default:
            return source;
    }
};

const getOfflineAiProgressLabel = (status: OfflineAiStatus, progress: number) => {
    if (status === 'ready') return '100%';
    if (status === 'downloading') {
        const percent = Math.max(0, Math.min(99, Math.round((progress || 0) * 100)));
        return percent > 0 ? `${percent}%` : 'starting...';
    }
    return '0%';
};

const getOfflineAiElapsedLabel = (startedAt?: number, now = Date.now()) => {
    if (!startedAt) return '';
    const elapsedSeconds = Math.max(0, Math.floor((now - startedAt) / 1000));
    const minutes = Math.floor(elapsedSeconds / 60);
    const seconds = elapsedSeconds % 60;
    return minutes > 0 ? `${minutes}m ${seconds}s` : `${seconds}s`;
};

const AI_REVIEW_UI_TIMEOUT_MS = 55000;

const withAiReviewTimeout = async <T,>(promise: Promise<T>): Promise<T> => {
    let timeoutId: ReturnType<typeof setTimeout> | undefined;
    const timeout = new Promise<never>((_, reject) => {
        timeoutId = setTimeout(() => reject(new Error('AI review timed out.')), AI_REVIEW_UI_TIMEOUT_MS);
    });
    try {
        return await Promise.race([promise, timeout]);
    } finally {
        if (timeoutId) clearTimeout(timeoutId);
    }
};

type OutputStatus = 'idle' | 'running' | 'win' | 'fail' | 'info';
type DifficultyMode = 'normal' | 'beginner' | 'intermediate' | 'expert' | 'legend';
type StatsByMode = Record<DifficultyMode, Stats>;
type CustomizeModalTab = 'count' | 'ide' | 'tools' | 'panels';

interface CountRowColorSettings {
    background: string;
    border: string;
    count: string;
    wins: string;
    fail: string;
    rate: string;
    value: string;
    icon: string;
    iconBackground: string;
}

interface PanelColorSettings {
    background: string;
    border: string;
    alpha: number;
}

interface ToolPanelColorSettings {
    panelBackground: string;
    panelBorder: string;
    toggleBackground: string;
    toggleText: string;
    footerText: string;
    fileText: string;
    panelLabelText: string;
    info: string;
    solution: string;
    ai: string;
    custom: string;
    win: string;
    failed: string;
    reset: string;
}

const DEFAULT_COUNT_ROW_COLORS: CountRowColorSettings = {
    background: '#0a1628',
    border: '#1d2d44',
    count: '#3b82f6',
    wins: '#22c55e',
    fail: '#FF1900',
    rate: '#FF9700',
    value: '#ffffff',
    icon: '#9ca3af',
    iconBackground: '#050c18',
};

const DEFAULT_PANEL_COLORS: PanelColorSettings = {
    background: '#0f1f3d',
    border: '#5876a0',
    alpha: 40,
};

const DEFAULT_TOOL_PANEL_COLORS: ToolPanelColorSettings = {
    panelBackground: '#071225',
    panelBorder: '#1d2d44',
    toggleBackground: '#071225',
    toggleText: '#d1d5db',
    footerText: '#9ca3af',
    fileText: '#d1d5db',
    panelLabelText: '#9ca3af',
    info: '#FF9700',
    solution: '#3b82f6',
    ai: '#3b82f6',
    custom: '#3b82f6',
    win: '#22c55e',
    failed: '#FF1900',
    reset: '#FF9700',
};

const loadToolPanelColorSettings = () => {
    const settings = loadColorSettings('python_tool_panel_colors', DEFAULT_TOOL_PANEL_COLORS);
    try {
        const migrationKey = 'python_tool_panel_colors_v195_migrated';
        if (localStorage.getItem(migrationKey) !== 'true') {
            localStorage.setItem(migrationKey, 'true');
            return {
                ...settings,
                ai: settings.ai === '#8b5cf6' ? DEFAULT_TOOL_PANEL_COLORS.ai : settings.ai,
                custom: settings.custom === '#14b8a6' ? DEFAULT_TOOL_PANEL_COLORS.custom : settings.custom,
            };
        }
    } catch {
        // Keep loaded settings if storage migration is unavailable.
    }
    return settings;
};

const sanitizeHexColor = (value: unknown, fallback: string) => {
    return typeof value === 'string' && /^#[0-9a-fA-F]{6}$/.test(value) ? value : fallback;
};

const hexToRgba = (hex: string, alpha: number) => {
    const normalized = sanitizeHexColor(hex, '#ffffff').slice(1);
    const value = Number.parseInt(normalized, 16);
    const red = (value >> 16) & 255;
    const green = (value >> 8) & 255;
    const blue = value & 255;
    return `rgba(${red}, ${green}, ${blue}, ${alpha})`;
};

const loadColorSettings = <T extends Record<string, string>>(storageKey: string, defaults: T): T => {
    try {
        const parsed = JSON.parse(localStorage.getItem(storageKey) || '{}');
        return Object.fromEntries(
            Object.entries(defaults).map(([key, value]) => [key, sanitizeHexColor(parsed?.[key], value)])
        ) as T;
    } catch {
        return defaults;
    }
};

const loadPanelColorSettings = (): PanelColorSettings => {
    try {
        const raw = localStorage.getItem('python_panel_colors');
        if (!raw) return DEFAULT_PANEL_COLORS;
        const parsed = JSON.parse(raw);
        const migrationKey = 'python_panel_colors_v2_migrated';
        if (localStorage.getItem(migrationKey) !== 'true') {
            localStorage.setItem(migrationKey, 'true');
            if (sanitizeHexColor(parsed.background, '') === '#081222') {
                parsed.background = DEFAULT_PANEL_COLORS.background;
            }
        }
        return {
            background: sanitizeHexColor(parsed.background, DEFAULT_PANEL_COLORS.background),
            border: sanitizeHexColor(parsed.border, DEFAULT_PANEL_COLORS.border),
            alpha: typeof parsed.alpha === 'number' ? Math.max(0, Math.min(100, parsed.alpha)) : DEFAULT_PANEL_COLORS.alpha,
        };
    } catch {
        return DEFAULT_PANEL_COLORS;
    }
};

const DIFFICULTY_MODES: Array<{ id: DifficultyMode; label: string; description: string }> = [
    { id: 'normal', label: 'Normal', description: 'All problems mixed' },
    { id: 'beginner', label: 'Beginner', description: 'Simple functions, strings, lists' },
    { id: 'intermediate', label: 'Intermediate', description: 'Loops, dictionaries, patterns' },
    { id: 'expert', label: 'Expert', description: 'Nested data, constraints, algorithms' },
    { id: 'legend', label: 'Legend', description: 'Recursion, OOP, files, advanced modules' }
];

const getDifficultyLabel = (mode: DifficultyMode) => DIFFICULTY_MODES.find(item => item.id === mode)?.label ?? 'Normal';

// Ranking system
interface Rank {
    name: string;
    icon: string;
    minScore: number;
}

const RANKS: Rank[] = [
    { name: 'Plankton', icon: '🦠', minScore: 0 },
    { name: 'Shrimp', icon: '🦐', minScore: 5 },
    { name: 'Crab', icon: '🦀', minScore: 15 },
    { name: 'Small Fish', icon: '🐟', minScore: 35 },
    { name: 'Octopus', icon: '🐙', minScore: 70 },
    { name: 'Seal', icon: '🦭', minScore: 120 },
    { name: 'Dolphin', icon: '🐬', minScore: 200 },
    { name: 'Shark', icon: '🦈', minScore: 350 },
    { name: 'Whale', icon: '🐋', minScore: 500 },
    { name: 'God Whale', icon: '👑🐋', minScore: 750 },
];

const getUserRank = (statsByMode: StatsByMode): Rank => {
    const totalShots = Object.values(statsByMode).reduce((sum, s) => sum + s.shots, 0);
    const totalWins = Object.values(statsByMode).reduce((sum, s) => sum + s.success, 0);
    const winRate = totalShots > 0 ? (totalWins / totalShots) * 100 : 0;
    const score = totalShots * (winRate / 100);

    let currentRank = RANKS[0];
    for (const rank of RANKS) {
        if (score >= rank.minScore) {
            currentRank = rank;
        } else {
            break;
        }
    }
    return currentRank;
};

const getModeRank = (stats: Stats): Rank => {
    const winRate = stats.shots > 0 ? (stats.success / stats.shots) * 100 : 0;
    const score = stats.shots * (winRate / 100);
    let currentRank = RANKS[0];
    for (const rank of RANKS) {
        if (score >= rank.minScore) {
            currentRank = rank;
        } else {
            break;
        }
    }
    return currentRank;
};

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

export const buildAutoGradeScript = (grader: AutoGrader, sourceCode = '', sourceName = 'main.py') => `
import json
import math
import sys
import io
import builtins
import inspect
import re
import ast
import types
import os
import shutil
import tempfile

__auto_grader_spec = json.loads(${JSON.stringify(JSON.stringify(grader))})
__auto_grader_source = ${JSON.stringify(sourceCode)}
__auto_grader_source_name = ${JSON.stringify(sourceName)}
__auto_grader_project_root = os.getcwd()

def __auto_grader_jsonable(value):
    try:
        json.dumps(value)
        return value
    except Exception:
        return repr(value)

def __auto_grader_normalize(value):
    if value is None:
        return "None"
    if isinstance(value, bytes):
        try:
            return value.decode('utf-8')
        except Exception:
            return str(value)
    if isinstance(value, bytearray):
        try:
            return value.decode('utf-8')
        except Exception:
            return str(value)
    if type(value).__name__ == "Decimal":
        try:
            return float(value)
        except Exception:
            return str(value)
    if type(value).__name__ == "Fraction":
        try:
            return float(value)
        except Exception:
            return str(value)
    if isinstance(value, complex):
        return str(value)
    if hasattr(value, "isoformat") and callable(value.isoformat):
        try:
            return value.isoformat()
        except Exception:
            pass
    if isinstance(value, os.PathLike):
        return str(value)
    if type(value).__name__ in ("dict_keys", "dict_values", "dict_items"):
        return [__auto_grader_normalize(item) for item in value]
    if hasattr(value, "__iter__") and hasattr(value, "__next__"):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, tuple):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, list):
        return [__auto_grader_normalize(item) for item in value]
    if isinstance(value, set):
        return sorted([__auto_grader_normalize(item) for item in value], key=str)
    if isinstance(value, frozenset):
        return sorted([__auto_grader_normalize(item) for item in value], key=str)
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
    if text == "True":
        return True
    if text == "False":
        return False
    if text == "None":
        return None
    try:
        return ast.literal_eval(text)
    except Exception:
        pass
    try:
        return json.loads(text)
    except Exception:
        pass
    try:
        return json.loads(text.replace("'", '"'))
    except Exception:
        pass
    try:
        if text.startswith("(") and text.endswith(")"):
            return ast.literal_eval(text)
    except Exception:
        pass
    return value

def __auto_grader_values_equivalent(actual, expected):
    actual = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
    expected = __auto_grader_normalize(__auto_grader_maybe_literal(expected))
    if actual == expected:
        return True
    if isinstance(actual, str) and isinstance(expected, str):
        if __auto_grader_clean_text(actual) == __auto_grader_clean_text(expected):
            return True
        if __auto_grader_deep_normalize(actual) == __auto_grader_deep_normalize(expected):
            return True
    if isinstance(actual, (int, float)) or isinstance(expected, (int, float)):
        try:
            return math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-9)
        except Exception:
            pass
    if isinstance(actual, str) and isinstance(expected, bool):
        return actual.strip().lower() == str(expected).lower()
    if isinstance(expected, str) and isinstance(actual, bool):
        return expected.strip().lower() == str(actual).lower()
    if isinstance(actual, set) and isinstance(expected, set):
        return actual == expected
    if isinstance(actual, (list, tuple)) and isinstance(expected, (list, tuple)):
        if len(actual) == len(expected):
            return all(__auto_grader_values_equivalent(a, e) for a, e in zip(actual, expected))
        if set(str(x) for x in actual) == set(str(x) for x in expected):
            return True
    if isinstance(actual, dict) and isinstance(expected, dict):
        if set(actual.keys()) == set(expected.keys()):
            return all(__auto_grader_values_equivalent(actual[k], expected[k]) for k in expected)
    return False

def __auto_grader_declarations_only(source):
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
        return ast.unparse(tree) + "\\n"
    except Exception:
        return source

def __auto_grader_load_function_namespace():
    source = __auto_grader_declarations_only(__auto_grader_source)
    exec(compile(source, __auto_grader_source_name, "exec"), globals())

def __auto_grader_call_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None

def __auto_grader_check_source_requirements():
    call_patterns = __auto_grader_spec.get("requiredCallPatterns", [])
    node_patterns = __auto_grader_spec.get("requiredNodePatterns", [])
    inheritance_patterns = __auto_grader_spec.get("requiredClassInheritance", [])
    bool_ops = __auto_grader_spec.get("requiredBoolOps", [])
    ast_operators = __auto_grader_spec.get("requiredAstOperators", [])
    unpack_patterns = __auto_grader_spec.get("requiredUnpackPatterns", [])
    try:
        tree = ast.parse(__auto_grader_source)
    except SyntaxError as exc:
        return f"Could not inspect source syntax: {exc}"
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
    all_nodes = list(ast.walk(tree))
    tests = __auto_grader_spec.get("tests", [])
    needs_input = any(case.get("inputValues") for case in tests)
    if needs_input and not any(__auto_grader_call_name(call.func) == "input" for call in calls):
        return "Missing required input(): this problem must read the supplied test input instead of using fixed values."
    random_call_names = {"randint", "randrange", "random", "uniform", "choice", "sample", "shuffle", "choices"}
    needs_random = any(
        case.get("randomValues") or
        case.get("randomFloatValues") or
        case.get("randomChoiceValues") or
        case.get("randomSampleValues") or
        case.get("randomShuffleValues")
        for case in tests
    )
    if needs_random and not any(__auto_grader_call_name(call.func) in random_call_names for call in calls):
        return "Missing required random call: this problem must use the supplied random behavior instead of a fixed value."
    if not call_patterns and not node_patterns and not inheritance_patterns and not bool_ops and not ast_operators and not unpack_patterns:
        return None
    for pattern in call_patterns:
        function_name = pattern.get("functionName")
        keyword = pattern.get("keyword")
        min_args = pattern.get("minArgs")
        matched = False
        for call in calls:
            if __auto_grader_call_name(call.func) != function_name:
                continue
            if keyword and not any(item.arg == keyword for item in call.keywords):
                continue
            if min_args is not None and len(call.args) < int(min_args):
                continue
            matched = True
            break
        if not matched:
            detail = function_name + "()"
            if keyword:
                detail += f" with {keyword}="
            if min_args is not None:
                detail += f" with at least {min_args} positional arguments"
            return "Missing required source pattern: " + detail
    for pattern in node_patterns:
        node_type = pattern.get("nodeType")
        min_count = int(pattern.get("minCount", 1))
        count = sum(1 for node in all_nodes if type(node).__name__ == node_type)
        if count < min_count:
            return f"Missing required syntax: at least {min_count} {node_type} node(s)"
    class_defs = {node.name: node for node in all_nodes if isinstance(node, ast.ClassDef)}
    for pattern in inheritance_patterns:
        class_name = pattern.get("className")
        base_name = pattern.get("baseName")
        class_node = class_defs.get(class_name)
        if not class_node:
            return f"Missing required class: {class_name}"
        base_names = {__auto_grader_call_name(base) for base in class_node.bases}
        if base_name not in base_names:
            return f"Missing required inheritance: {class_name} must inherit from {base_name}"
    present_bool_ops = {type(node.op).__name__ for node in all_nodes if isinstance(node, ast.BoolOp)}
    for required in bool_ops:
        if required not in present_bool_ops:
            return f"Missing required boolean operator: {required}"
    present_operators = set()
    for node in all_nodes:
        if isinstance(node, ast.BinOp):
            present_operators.add(type(node.op).__name__)
        elif isinstance(node, ast.UnaryOp):
            present_operators.add(type(node.op).__name__)
        elif isinstance(node, ast.Compare):
            present_operators.update(type(op).__name__ for op in node.ops)
        elif isinstance(node, ast.AugAssign):
            present_operators.add(type(node.op).__name__)
    for required in ast_operators:
        if required not in present_operators:
            return f"Missing required operator: {required}"
    unpack_error = __auto_grader_unpack_patterns_error(tree, unpack_patterns)
    if unpack_error:
        return unpack_error
    return None

def __auto_grader_unpack_patterns_error(tree, patterns):
    if not patterns:
        return None
    list_names = set()
    tuple_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, (ast.List, ast.Tuple)):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if isinstance(node.value, ast.List):
                        list_names.add(target.id)
                    else:
                        tuple_names.add(target.id)
    assigns = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]
    for pattern in patterns:
        target_count = int(pattern.get("targetCount", 0))
        source_type = pattern.get("sourceType", "Any")
        allow_starred = bool(pattern.get("allowStarred", False))
        matched = False
        for assign in assigns:
            for target in assign.targets:
                if not isinstance(target, (ast.Tuple, ast.List)):
                    continue
                if len(target.elts) != target_count:
                    continue
                has_starred = any(isinstance(elt, ast.Starred) for elt in target.elts)
                if has_starred and not allow_starred:
                    continue
                value = assign.value
                if source_type == "Any":
                    matched = True
                elif source_type == "List":
                    matched = isinstance(value, ast.List) or (isinstance(value, ast.Name) and value.id in list_names) or (isinstance(value, ast.Call) and __auto_grader_call_name(value.func) == "list")
                elif source_type == "Tuple":
                    matched = isinstance(value, ast.Tuple) or (isinstance(value, ast.Name) and value.id in tuple_names) or (isinstance(value, ast.Call) and __auto_grader_call_name(value.func) == "tuple")
                if matched:
                    break
            if matched:
                break
        if not matched:
            source_label = source_type.lower() if source_type != "Any" else "sequence"
            starred_label = " with starred unpacking" if allow_starred else ""
            return f"Missing required unpacking: unpack a {source_label} into {target_count} variables{starred_label}."
    return None

def __auto_grader_hardcoded_expected_error(expected):
    if not isinstance(expected, str):
        return None
    expected_text = __auto_grader_clean_text(expected)
    if len(expected_text) < 20 or "\\n" not in expected_text:
        return None
    try:
        tree = ast.parse(__auto_grader_source)
    except SyntaxError:
        return None
    expected_compact = __auto_grader_compact_pattern(expected_text)
    expected_lines = [
        __auto_grader_compact_pattern(line)
        for line in expected_text.splitlines()
        if line.strip()
    ]
    literal_lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            literal_text = __auto_grader_clean_text(node.value)
            if literal_text == expected_text or __auto_grader_compact_pattern(literal_text) == expected_compact:
                return "Hard-coded output detected: build the result with the required logic instead of pasting the expected output."
            for literal_line in literal_text.splitlines():
                if literal_line.strip():
                    literal_lines.add(__auto_grader_compact_pattern(literal_line))
    if len(expected_lines) >= 8 and literal_lines:
        matched_lines = sum(1 for line in expected_lines if line in literal_lines)
        if matched_lines >= 8 and matched_lines / len(expected_lines) >= 0.8:
            return "Hard-coded output lines detected: generate the output with Python logic instead of printing the expected lines one by one."
    return None

def __auto_grader_clean_text(value):
    return "\\n".join(line.rstrip() for line in str(value).strip().splitlines())

def __auto_grader_deep_normalize(value):
    text = __auto_grader_clean_text(value)
    if not text:
        return text
    lines = []
    for line in text.splitlines():
        if not line.strip():
            continue
        normalized = line
        normalized = normalized.replace('"', "'")
        normalized = re.sub(r'\\btrue\\b', 'True', normalized, flags=re.IGNORECASE)
        normalized = re.sub(r'\\bfalse\\b', 'False', normalized, flags=re.IGNORECASE)
        normalized = re.sub(r'\\bnone\\b', 'None', normalized, flags=re.IGNORECASE)
        normalized = re.sub(r'(?<![\\w.])\\d+\\.0+(?![\\w.])', lambda m: str(int(float(m.group()))), normalized)
        normalized = re.sub(r'(?<![\\w.])\\d+\\.0(?=[^\\d]|$)', lambda m: str(int(float(m.group()))), normalized)
        normalized = re.sub(r'\\s+', ' ', normalized).strip()
        normalized = normalized.rstrip('.,;:')
        lines.append(normalized)
    return "\\n".join(lines)

def __auto_grader_compact_pattern(value):
    return "\\n".join(re.sub(r"[ \\t]+", "", line) for line in __auto_grader_clean_text(value).splitlines())

def __auto_grader_meaningful_text_matches(actual_text, expected):
    actual_text = __auto_grader_clean_text(actual_text)
    expected_value = __auto_grader_normalize(__auto_grader_maybe_literal(expected))
    expected_text = __auto_grader_clean_text(expected)
    lines = [line.strip() for line in actual_text.splitlines() if line.strip()]
    if not lines:
        return False

    candidates = []
    for line in lines:
        candidates.append(line)
        for separator in (":", "=", "->", "=>", "|", "is", "was"):
            if separator in line:
                candidates.append(line.rsplit(separator, 1)[-1].strip())
        tokens = re.findall(r"True|False|-?\\d+(?:\\.\\d+)?|['\\\"][^'\\\"]+['\\\"]", line, re.IGNORECASE)
        if tokens:
            for token in tokens:
                candidates.append(token if isinstance(token, str) else str(token))
            candidates.append(tokens[-1] if isinstance(tokens[-1], str) else str(tokens[-1]))

    for candidate in candidates:
        if __auto_grader_values_equivalent(candidate, expected_value):
            return True
        if expected_text and __auto_grader_clean_text(candidate).lower() == expected_text.lower():
            return True
        if __auto_grader_deep_normalize(candidate) == __auto_grader_deep_normalize(expected):
            return True

    last_line = lines[-1]
    if isinstance(expected_value, bool):
        bool_tokens = re.findall(r"\\b(true|false)\\b", last_line, re.IGNORECASE)
        return bool(bool_tokens and (bool_tokens[-1].lower() == str(expected_value).lower()))
    if isinstance(expected_value, (int, float)) and not isinstance(expected_value, bool):
        found_numbers = __auto_grader_numbers(last_line)
        if found_numbers:
            try:
                return any(math.isclose(float(n), float(expected_value), rel_tol=1e-9, abs_tol=1e-9) for n in found_numbers)
            except Exception:
                return False
    if isinstance(expected_value, str) and expected_value:
        return expected_value.lower() in actual_text.lower()
    if isinstance(expected_value, (list, tuple)):
        actual_literal = __auto_grader_normalize(__auto_grader_maybe_literal(actual_text))
        if isinstance(actual_literal, (list, tuple)):
            return __auto_grader_values_equivalent(actual_literal, expected_value)
    if isinstance(expected_value, dict):
        actual_literal = __auto_grader_normalize(__auto_grader_maybe_literal(actual_text))
        if isinstance(actual_literal, dict):
            return __auto_grader_values_equivalent(actual_literal, expected_value)
    return False

def __auto_grader_shape_matches(actual, expected):
    if expected is None:
        return True
    actual_text = __auto_grader_clean_text(actual)
    if not actual_text:
        return expected in (None, "")
    actual_value = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
    expected_value = __auto_grader_normalize(__auto_grader_maybe_literal(expected))
    if type(expected_value).__name__ in ("list", "tuple", "set"):
        return isinstance(actual_value, (list, tuple, set)) or bool(re.search(r"[\[({].*[\])}]", actual_text, re.DOTALL))
    if isinstance(expected_value, dict):
        return isinstance(actual_value, dict) or (":" in actual_text and bool(re.search(r"[\[{].*[\]}]", actual_text, re.DOTALL)))
    if isinstance(expected_value, bool):
        if isinstance(actual_value, bool):
            return True
        return bool(re.search(r"\\b(true|false)\\b", actual_text, re.IGNORECASE))
    if isinstance(expected_value, (int, float)) and not isinstance(expected_value, bool):
        return bool(__auto_grader_numbers(actual_text))
    if isinstance(expected_value, str):
        if not expected_value:
            return True
        if expected_value.startswith("b'") or expected_value.startswith('b"'):
            return actual_text.startswith("b'") or actual_text.startswith('b"') or isinstance(actual_value, (bytes, bytearray))
        return True
    return True

def __auto_grader_same(actual, expected, compare):
    if compare == "typeName":
        return type(actual).__name__ == expected
    actual = __auto_grader_normalize(actual)
    expected = __auto_grader_normalize(expected)
    if isinstance(actual, str) and isinstance(expected, (list, dict, tuple, set)):
        actual = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
    if compare == "float":
        try:
            actual_num = float(actual)
            expected_num = float(expected)
            if math.isclose(actual_num, expected_num, rel_tol=1e-6, abs_tol=1e-6):
                return True
            if round(actual_num, 2) == round(expected_num, 2):
                return True
            return False
        except Exception:
            try:
                actual_numbers = __auto_grader_numbers(str(actual))
                expected_num = float(expected)
                if actual_numbers:
                    return any(math.isclose(float(n), expected_num, rel_tol=1e-6, abs_tol=1e-6) for n in actual_numbers)
            except Exception:
                pass
            return False
    if compare == "printedOrReturn":
        actual_text = __auto_grader_clean_text(actual)
        expected_text = __auto_grader_clean_text(expected)
        actual_lines = [line.strip() for line in actual_text.splitlines() if line.strip()]
        expected_lines = [line.strip() for line in expected_text.splitlines() if line.strip()]
        # Check if all expected lines appear in actual (unordered)
        unordered_match = len(expected_lines) > 0 and all(
            any(__auto_grader_deep_normalize(el) == __auto_grader_deep_normalize(al) for al in actual_lines)
            for el in expected_lines
        )
        # Check if expected value appears anywhere in actual output
        normalized_expected = __auto_grader_deep_normalize(expected)
        normalized_actual = __auto_grader_deep_normalize(actual)
        substring_match = normalized_expected and normalized_expected in normalized_actual
        return (
            __auto_grader_values_equivalent(actual, expected)
            or actual_text == expected_text
            or expected_text in actual_text
            or __auto_grader_compact_pattern(actual_text) == __auto_grader_compact_pattern(expected_text)
            or any(__auto_grader_values_equivalent(line, expected) for line in actual_lines)
            or __auto_grader_meaningful_text_matches(actual_text, expected)
            or __auto_grader_deep_normalize(actual) == __auto_grader_deep_normalize(expected)
            or unordered_match
            or substring_match
        )
    if compare == "printedFlex":
        actual_text = __auto_grader_clean_text(actual)
        expected_text = __auto_grader_clean_text(expected)
        try:
            pat = re.escape(expected_text)
            # Make single-letter variables flexible
            pat = re.sub(r'\b[a-zA-Z]\b', r'\\w+', pat)
            # Make multi-letter variable-like words flexible (words followed by : or =)
            pat = re.sub(r'\\b([a-zA-Z_][a-zA-Z0-9_]*)\\b(?=\\s*[:=])', r'\\w+', pat)
            # Make values after labels flexible (e.g., "Name: Alice" → "Name: \\w+")
            pat = re.sub(r'(:\\s*)([a-zA-Z_][a-zA-Z0-9_]*)(?=\\s|$|,)', r'\\1\\w+', pat)
            pat = pat.replace(r'\ ', r'\\s+')
            return bool(re.search(pat, actual_text, re.IGNORECASE))
        except Exception:
            return actual_text == expected_text
    if compare == "sourceIntent":
        return __auto_grader_shape_matches(actual, expected)
    if compare == "valuesPresent":
        actual_text = __auto_grader_clean_text(actual)
        expected_text = __auto_grader_clean_text(expected)
        # Extract all values from expected
        expected_numbers = __auto_grader_numbers(expected_text)
        expected_strings = re.findall(r"['\\\"]([^'\\\"]+)['\\\"]", expected_text)
        # Check all numbers appear in actual
        actual_numbers = __auto_grader_numbers(actual_text)
        for num in expected_numbers:
            if not any(math.isclose(float(a), float(num), rel_tol=1e-9, abs_tol=1e-9) for a in actual_numbers):
                return False
        # Check all strings appear in actual (case-insensitive)
        actual_lower = actual_text.lower()
        for s in expected_strings:
            if s.lower() not in actual_lower:
                return False
        return True
    if compare == "structuralMatch":
        try:
            actual_struct = __auto_grader_maybe_literal(actual)
            expected_struct = __auto_grader_maybe_literal(expected)
            # Check structure matches (same type, same keys for dicts, same length for lists)
            if type(actual_struct) != type(expected_struct):
                return False
            if isinstance(expected_struct, dict):
                if set(actual_struct.keys()) != set(expected_struct.keys()):
                    return False
                # Recursively check values
                for key in expected_struct:
                    if not __auto_grader_same(actual_struct[key], expected_struct[key], "structuralMatch"):
                        return False
                return True
            if isinstance(expected_struct, (list, tuple)):
                if len(actual_struct) != len(expected_struct):
                    return False
                for a, e in zip(actual_struct, expected_struct):
                    if not __auto_grader_same(a, e, "structuralMatch"):
                        return False
                return True
            # For primitives, use exact comparison
            return actual_struct == expected_struct
        except Exception:
            return False
    if compare == "lenient":
        # Try multiple strategies — if ANY pass, the test passes
        return (
            __auto_grader_same(actual, expected, "exact")
            or __auto_grader_same(actual, expected, "printedOrReturn")
            or __auto_grader_same(actual, expected, "printedFlex")
            or __auto_grader_same(actual, expected, "valuesPresent")
            or __auto_grader_same(actual, expected, "structuralMatch")
        )
    if compare == "numberRange":
        numbers = __auto_grader_numbers(actual)
        if not numbers or not isinstance(expected, list) or len(expected) != 2:
            return False
        value = numbers[-1]
        return float(expected[0]) <= value <= float(expected[1])
    if compare == "setPop":
        if not isinstance(expected, list):
            return False
        lines = __auto_grader_clean_text(actual).splitlines()
        if len(lines) < 2:
            return False
        try:
            removed_values = __auto_grader_numbers(lines[0])
            remaining = __auto_grader_maybe_literal(lines[1])
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
            actual = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
            expected = __auto_grader_normalize(__auto_grader_maybe_literal(expected))
            if not isinstance(actual, (list, tuple)):
                actual = __auto_grader_normalize(__auto_grader_maybe_literal(str(actual)))
            if not isinstance(expected, (list, tuple)):
                expected = __auto_grader_normalize(__auto_grader_maybe_literal(str(expected)))
            if not isinstance(actual, (list, tuple)) or not isinstance(expected, (list, tuple)):
                return False
            if len(actual) != len(expected):
                return False
            actual_sorted = sorted(actual, key=lambda x: str(x))
            expected_sorted = sorted(expected, key=lambda x: str(x))
            return all(__auto_grader_values_equivalent(a, e) for a, e in zip(actual_sorted, expected_sorted))
        except Exception:
            return False
    if compare == "unorderedWords":
        try:
            actual = __auto_grader_maybe_literal(actual)
            expected = __auto_grader_maybe_literal(expected)
            if isinstance(actual, str):
                actual = re.split(r'[,\s]+', actual.strip('[](){}'))
            if isinstance(expected, str):
                expected = re.split(r'[,\s]+', expected.strip('[](){}'))
            if not isinstance(actual, (list, tuple)):
                actual = list(actual) if hasattr(actual, '__iter__') else [actual]
            if not isinstance(expected, (list, tuple)):
                expected = list(expected) if hasattr(expected, '__iter__') else [expected]
            actual_strs = sorted(str(x).strip().lower() for x in actual if str(x).strip())
            expected_strs = sorted(str(x).strip().lower() for x in expected if str(x).strip())
            return actual_strs == expected_strs
        except Exception:
            return False
    if compare == "numberList":
        try:
            actual_numbers = __auto_grader_numbers(actual)
            expected_numbers = [float(item) for item in expected]
            if len(actual_numbers) != len(expected_numbers):
                return False
            return all(
                math.isclose(a, e, rel_tol=1e-6, abs_tol=1e-6) or round(a, 2) == round(e, 2)
                for a, e in zip(actual_numbers, expected_numbers)
            )
        except Exception:
            return False
    if compare == "dictUnorderedLists":
        actual = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
        expected = __auto_grader_normalize(__auto_grader_maybe_literal(expected))
        if not isinstance(actual, dict) or not isinstance(expected, dict):
            return False
        actual_str_keys = {str(k): v for k, v in actual.items()}
        expected_str_keys = {str(k): v for k, v in expected.items()}
        if set(actual_str_keys.keys()) != set(expected_str_keys.keys()):
            return False
        try:
            for key in expected_str_keys:
                actual_list = actual_str_keys.get(key, [])
                expected_list = expected_str_keys[key]
                if not isinstance(actual_list, (list, tuple)):
                    actual_list = [actual_list]
                if not isinstance(expected_list, (list, tuple)):
                    expected_list = [expected_list]
                if len(actual_list) != len(expected_list):
                    return False
                actual_sorted = sorted(actual_list, key=lambda x: str(x))
                expected_sorted = sorted(expected_list, key=lambda x: str(x))
                if not all(__auto_grader_values_equivalent(a, e) for a, e in zip(actual_sorted, expected_sorted)):
                    return False
            return True
        except Exception:
            return False
    if compare == "dictAddedPair":
        actual = __auto_grader_normalize(__auto_grader_maybe_literal(actual))
        expected = __auto_grader_normalize(__auto_grader_maybe_literal(expected))
        if not isinstance(actual, dict) or not isinstance(expected, dict):
            return False
        if len(actual) <= len(expected):
            return False
        actual_str_keys = {str(k): v for k, v in actual.items()}
        expected_str_keys = {str(k): v for k, v in expected.items()}
        for key, value in expected_str_keys.items():
            if key not in actual_str_keys or not __auto_grader_values_equivalent(actual_str_keys[key], value):
                return False
        return True
    if compare == "letterCounts":
        if isinstance(actual, dict):
            actual_lower_keys = {k.lower().replace("_", "").replace(" ", ""): v for k, v in actual.items()}
            upper = actual_lower_keys.get("upper") or actual_lower_keys.get("uppercase") or actual_lower_keys.get("uppercount") or actual_lower_keys.get("numupper")
            lower = actual_lower_keys.get("lower") or actual_lower_keys.get("lowercase") or actual_lower_keys.get("lowercount") or actual_lower_keys.get("numlower")
            if upper is not None and lower is not None:
                return upper == expected.get("upper") and lower == expected.get("lower")
        if isinstance(actual, (list, tuple)) and len(actual) == 2:
            return list(actual) in ([expected.get("upper"), expected.get("lower")], [expected.get("lower"), expected.get("upper")])
        text = str(actual).lower()
        lower_match = re.search(r"lower\\D+(\\d+)", text)
        upper_match = re.search(r"upper\\D+(\\d+)", text)
        if not lower_match:
            lower_match = re.search(r"(\\d+)\\D*lower", text)
        if not upper_match:
            upper_match = re.search(r"(\\d+)\\D*upper", text)
        return bool(lower_match and upper_match and int(lower_match.group(1)) == expected.get("lower") and int(upper_match.group(1)) == expected.get("upper"))
    if compare == "vowelConsonantCounts":
        if isinstance(actual, dict):
            actual_lower_keys = {k.lower().replace("_", "").replace(" ", ""): v for k, v in actual.items()}
            vowels = actual_lower_keys.get("vowels") or actual_lower_keys.get("vowel") or actual_lower_keys.get("vowelcount") or actual_lower_keys.get("numvowels")
            consonants = actual_lower_keys.get("consonants") or actual_lower_keys.get("consonant") or actual_lower_keys.get("consonantcount") or actual_lower_keys.get("numconsonants")
            if vowels is not None and consonants is not None:
                return vowels == expected.get("vowels") and consonants == expected.get("consonants")
        if isinstance(actual, (list, tuple)) and len(actual) == 2:
            return list(actual) in ([expected.get("vowels"), expected.get("consonants")], [expected.get("consonants"), expected.get("vowels")])
        text = str(actual).lower()
        vowel_match = re.search(r"vowels?\\D+(\\d+)", text)
        consonant_match = re.search(r"consonants?\\D+(\\d+)", text)
        if not vowel_match:
            vowel_match = re.search(r"(\\d+)\\D*vowels?", text)
        if not consonant_match:
            consonant_match = re.search(r"(\\d+)\\D*consonants?", text)
        return bool(vowel_match and consonant_match and int(vowel_match.group(1)) == expected.get("vowels") and int(consonant_match.group(1)) == expected.get("consonants"))
    if __auto_grader_deep_normalize(actual) == __auto_grader_deep_normalize(expected):
        return True
    return actual == expected

def __auto_grader_accepts_args(candidate, args, kwargs=None):
    try:
        inspect.signature(candidate).bind(*args, **(kwargs or {}))
        return True
    except Exception:
        return False

def __auto_grader_is_user_function(name, candidate):
    if name.startswith("__"):
        return False
    if isinstance(candidate, (type, types.ModuleType)):
        return False
    if not callable(candidate):
        return False
    return inspect.isfunction(candidate) and getattr(candidate, "__globals__", None) is globals()

def __auto_grader_find_callable(function_names, args, required_name=None, kwargs=None):
    names = [required_name] if required_name else function_names
    for name in names:
        candidate = globals().get(name)
        if callable(candidate) and __auto_grader_accepts_args(candidate, args, kwargs):
            return name, candidate
    if required_name:
        return None, None
    fallback_matches = []
    for name, candidate in globals().items():
        if name in function_names:
            continue
        if not __auto_grader_is_user_function(name, candidate):
            continue
        if callable(candidate) and __auto_grader_accepts_args(candidate, args, kwargs):
            fallback_matches.append((name, candidate))
    if len(fallback_matches) == 1:
        return fallback_matches[0]
    return None, None

def __auto_grader_is_simple_case(case):
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

def __auto_grader_is_generated_input_case(case):
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

def __auto_grader_input_generated_cases(function_names, tests):
    if not tests or not all(__auto_grader_is_generated_input_case(case) for case in tests):
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

def __auto_grader_metamorphic_cases(function_names, tests):
    if not tests or not all(__auto_grader_is_simple_case(case) for case in tests):
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
        if "format_calculation" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in [left, right]):
            return [([2, 9], "2 + 9 = 11"), ([-3, 5], "-3 + 5 = 2")]
        if "calculate_sum_range" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([3, 6], 18), ([-1, 1], 0)]
        if "get_even_range" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([3, 9], [4, 6, 8]), ([4, 4], [4])]
        if "get_odd_range" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([3, 9], [3, 5, 7, 9]), ([4, 4], [])]
        if "add_lists" in name_set and isinstance(left, list) and isinstance(right, list):
            return [([[1, -2, 3], [4, 5, -6]], [5, 3, -3])]
        if "filter_by_length" in name_set and isinstance(left, list) and isinstance(right, int):
            return [([["a", "abcd", "xy", "python"], 4], ["abcd", "python"])]
        if "calculate_lcm" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in [left, right]):
            return [([21, 6], 42), ([8, 12], 24)]
        if "calculate_weighted_average" in name_set and isinstance(left, list) and isinstance(right, list):
            return [([[10, 20, 30], [1, 1, 2]], 22.5)]
        if "get_pairs_summing_to" in name_set and isinstance(left, list) and isinstance(right, (int, float)) and not isinstance(right, bool):
            return [([[2, 4, 5, 6, 8], 10], [[2, 8], [4, 6]])]
        if "get_words_with_vowel_count" in name_set and isinstance(left, str) and isinstance(right, int) and not isinstance(right, bool):
            return [(["code sky audio tree", 2], ["code", "tree"])]
        if "main" in name_set and isinstance(left, list) and isinstance(right, int) and not isinstance(right, bool):
            return [([[7, 8, 9, 10, 11], 4], [8, 9, 10, 7, 11])]
        return []
    if len(first_args) == 3:
        if "max_of_three" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([10, 25, 15], 25), ([-10, -2, -5], -2)]
        if "get_maximum" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([10, 25, 15], 25), ([-10, -2, -5], -2)]
        if "find_minimum" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([10, -2, 5], -2), ([3, 3, 8], 3)]
        if "get_minimum" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([10, -2, 5], -2), ([3, 3, 8], 3)]
        if "get_words_by_length_range" in name_set and isinstance(first_args[0], str) and all(isinstance(value, int) and not isinstance(value, bool) for value in first_args[1:]):
            return [(["a aa aaa aaaa aaaaa", 3, 5], ["aaa", "aaaa", "aaaaa"])]
        if "check_in_range" in name_set and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args):
            return [([5, 5, 5], True), ([4, 5, 10], False)]
        if "format_time" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in first_args):
            return [([0, 5, 9], "00:05:09"), ([23, 59, 1], "23:59:01")]
        if "calculate_age" in name_set and all(isinstance(value, int) and not isinstance(value, bool) for value in first_args):
            return [([2023, 1, 1], 1), ([2023, 1, 2], 0)]
        if "get_numbers_in_range" in name_set and isinstance(first_args[0], list) and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args[1:]):
            return [([[2, 4, 6, 8, 10], 4, 8], [4, 6, 8])]
        if "get_strings_with_length_range" in name_set and isinstance(first_args[0], list) and all(isinstance(value, int) and not isinstance(value, bool) for value in first_args[1:]):
            return [([["a", "able", "bee", "python"], 3, 4], ["able", "bee"])]
        if "get_sublist_sum" in name_set and isinstance(first_args[0], list) and all(isinstance(value, int) and not isinstance(value, bool) for value in first_args[1:]):
            return [([[5, 10, 15, 20], 0, 2], 15), ([[5, 10, 15, 20], 2, 4], 35)]
        if "get_numbers_summing_to_range" in name_set and isinstance(first_args[0], list) and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in first_args[1:]):
            return [([[1, 3, 4, 6], 7, 9], [[1, 6], [3, 4], [3, 6]])]
        if "get_elements_by_frequency_range" in name_set and isinstance(first_args[0], list) and all(isinstance(value, int) and not isinstance(value, bool) for value in first_args[1:]):
            return [([["a", "a", "b", "b", "b", "c"], 2, 3], ["a", "b"])]
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
    if "check_perfect_square" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
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
    if "get_fibonacci_sequence" in name_set and isinstance(sample, int):
        return [([6], [0, 1, 1, 2, 3, 5]), ([2], [0, 1])]
    if "fibonacci" in name_set and isinstance(sample, int) and isinstance(first_expected, int):
        return [([6], 8), ([8], 21)]
    if "fibonacci_sequence" in name_set and isinstance(sample, int):
        return [([6], "0\\n1\\n1\\n2\\n3\\n5"), ([2], "0\\n1")]
    if "sum_n" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([7], 28), ([1], 1)]
    if "print_reverse" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], "4\\n3\\n2\\n1"), ([1], "1")]
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
    if "get_season" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([2], "Winter"), ([7], "Summer"), ([11], "Fall")]
    if "check_all_conditions" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([12], True), ([9], False), ([0], False)]
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
    if "calculate_sum_of_list" in name_set and isinstance(sample, list):
        return [([[1, 2, -3]], 0), ([[10]], 10)]
    if "get_average_of_list" in name_set and isinstance(sample, list):
        return [([[2, 4, 9]], 5), ([[-2, 2, 6]], 2)]
    if "get_middle_element" in name_set and isinstance(sample, list):
        return [([[9, 8, 7, 6, 5]], 7), ([[1, 2]], 2)]
    if "get_even_numbers" in name_set and isinstance(sample, list):
        return [([[1, 3, 8, 10]], [8, 10])]
    if "get_even_numbers_comprehension" in name_set and isinstance(sample, list):
        return [([[1, 3, 8, 10]], [8, 10])]
    if "get_odd_numbers" in name_set and isinstance(sample, list):
        return [([[1, 2, 8, 9]], [1, 9])]
    if "get_squared_numbers" in name_set and isinstance(sample, list):
        return [([[3, -2, 0]], [9, 4, 0])]
    if "remove_duplicates_from_list" in name_set and isinstance(sample, list):
        return [([[3, 1, 3, 2, 1]], [3, 1, 2])]
    if "remove_duplicates_preserve_order" in name_set and isinstance(sample, list):
        return [([[3, 1, 3, 2, 1]], [3, 1, 2])]
    if "sort_list_ascending" in name_set and isinstance(sample, list):
        return [([[5, -1, 0]], [-1, 0, 5])]
    if "get_index_of_max" in name_set and isinstance(sample, list):
        return [([[10, 20, 30, 25]], 2)]
    if "get_index_of_min" in name_set and isinstance(sample, list):
        return [([[10, -2, 30, -5]], 3)]
    if "get_min_max" in name_set and isinstance(sample, list):
        return [([[5, -2, 10]], [-2, 10])]
    if "filter_and_transform" in name_set and isinstance(sample, list):
        return [([[1, 2, 8, 9]], [4, 16])]
    if "find_duplicate_elements" in name_set and isinstance(sample, list):
        return [([[3, 1, 3, 2, 1, 3]], [3, 1])]
    if "get_even_indices" in name_set and isinstance(sample, list):
        return [([["a", "b", "c", "d", "e"]], ["a", "c", "e"])]
    if "get_odd_indices" in name_set and isinstance(sample, list):
        return [([["a", "b", "c", "d", "e"]], ["b", "d"])]
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
    if "calculate_perimeter_square" in name_set and isinstance(sample, (int, float)) and not isinstance(sample, bool):
        return [([7], 28), ([2.5], 10)]
    if "square_of_number" in name_set and isinstance(sample, (int, float)) and not isinstance(sample, bool):
        return [([7], 49), ([-3], 9)]
    if "closest_to_zero" in name_set and isinstance(sample, list):
        return [([[-8, -3, 5, 2]], 2), ([[4, -1, 9]], -1)]
    if "print_odd_index_elements" in name_set and isinstance(sample, list):
        return [([["a", "b", "c", "d"]], "b\\nd"), ([["x", "y"]], "y")]
    if "index_element_if_vowel" in name_set and isinstance(sample, list):
        return [([["apple", "berry", "orange"]], [[0, "apple"], [2, "orange"]]), ([["egg", "fish"]], [[0, "egg"]])]
    if "print_index_squared" in name_set and isinstance(sample, list):
        return [([[2, -3]], "Index: 0, Squared: 4\\nIndex: 1, Squared: 9")]
    if "replace_based_on_index" in name_set and isinstance(sample, list):
        return [([["a", "b", "c"]], ["Even", "Odd", "Even"]), ([[1, 2]], ["Even", "Odd"])]
    if "enumerate_lst" in name_set and isinstance(sample, list) and isinstance(first_expected, str) and "index" not in first_expected.lower():
        return [([["a", "b", "c", "d", "e"]], "0 a\\n2 c\\n4 e")]
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
    if "reverse_order" in name_set and isinstance(sample, list):
        return [([["alpha", "zulu", "beta"]], ["zulu", "beta", "alpha"])]
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
    if "sort_by_multiple_criteria" in name_set and isinstance(sample, list):
        return [([[
            ["Zed", 30, 88],
            ["Ana", 20, 90],
            ["Bo", 20, 70],
            ["Cy", 30, 80],
        ]], [["Bo", 20, 70], ["Ana", 20, 90], ["Cy", 30, 80], ["Zed", 30, 88]])]
    if "calculate_statistics" in name_set and isinstance(sample, list):
        return [([[4, 8, 12]], {"sum": 24, "average": 8, "min": 4, "max": 12})]
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
        return [([{"zeta": 1, "alpha": 2, "mid": 3}], "alpha\\nmid\\nzeta")]
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
    if name_set & {"square_pattern", "print_square_pattern"} and isinstance(sample, int) and not isinstance(sample, bool):
        first_line = str(first_expected).splitlines()[0] if first_expected is not None else ""
        if set(first_line.replace(" ", "")) == {"*"}:
            return [([4], "****\\n****\\n****\\n****")]
        return [([4], "1 2 3 4\\n1 2 3 4\\n1 2 3 4\\n1 2 3 4")]
    if "print_hollow_square" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], "****\\n*  *\\n*  *\\n****")]
    if "print_reverse_pyramid" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], "1 2 3 4\\n1 2 3\\n1 2\\n1")]
    if "print_cross" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([7], "*     *\\n *   * \\n  * *  \\n   *   \\n  * *  \\n *   * \\n*     *")]
    if "print_reverse_hill_pattern" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], "*******\\n *****\\n  ***\\n   *")]
    if "print_reverse_star_pattern" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([4], "****\\n***\\n**\\n*")]
    if "print_number_square" in name_set and isinstance(sample, int) and not isinstance(sample, bool):
        return [([3], "1 2 3\\n4 5 6\\n7 8 9")]
    if "get_middle_char" in name_set and isinstance(sample, str):
        return [(["abcde"], "c"), (["abcdef"], "d")]
    if "get_first_word" in name_set and isinstance(sample, str):
        return [(["alpha beta gamma"], "alpha")]
    if "get_last_word" in name_set and isinstance(sample, str):
        return [(["alpha beta gamma"], "gamma")]
    if "count_characters" in name_set and isinstance(sample, str) and isinstance(first_expected, int):
        return [(["a b c"], 3), ([" spaced text "], 10)]
    if "check_vowel" in name_set and isinstance(sample, str):
        return [(["e"], True), (["z"], False)]
    if "strip_whitespace" in name_set and isinstance(sample, str):
        return [(["  a"], "a"), (["b  "], "b")]
    if "capitalize_first_letter" in name_set and isinstance(sample, str):
        return [(["python"], "Python"), (["pYTHON"], "Python")]
    if "capitalize_all_words" in name_set and isinstance(sample, str):
        return [(["hello codex app"], "Hello Codex App")]
    if "get_longest_word" in name_set and isinstance(sample, str):
        return [(["cat elephant dog"], "elephant")]
    if "get_shortest_word" in name_set and isinstance(sample, str):
        return [(["long to a"], "a")]
    if "remove_vowels_from_string" in name_set and isinstance(sample, str):
        return [(["Beautiful"], "Btfl"), (["rhythm"], "rhythm")]
    if "remove_consonants_from_string" in name_set and isinstance(sample, str):
        return [(["Beautiful"], "eauiu"), (["rhythm"], "")]
    if "count_vowels_in_string" in name_set and isinstance(sample, str):
        return [(["Beautiful"], 5), (["rhythm"], 0)]
    if "swap_first_last_words" in name_set and isinstance(sample, str):
        return [(["alpha beta gamma"], "gamma beta alpha"), (["solo"], "solo")]
    if "get_middle_word" in name_set and isinstance(sample, str):
        return [(["one two three four five"], "three"), (["one two three four"], "three")]
    if "get_words_starting_with_vowel" in name_set and isinstance(sample, str):
        return [(["apple pear orange ice"], ["apple", "orange", "ice"])]
    if "count_vowels_and_consonants" in name_set and isinstance(sample, str):
        return [(["codex ai"], [4, 3]), (["rhythm"], [0, 6])]
    if "check_palindrome_and_length" in name_set and isinstance(sample, str):
        return [(["level"], [True, 5]), (["python"], [False, 6])]
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
    if "get_sum_of_squares" in name_set and isinstance(sample, list):
        return [([[3, -4, 1]], 26)]
    if "get_product_of_even" in name_set and isinstance(sample, list):
        return [([[2, 3, 4, 6]], 48)]
    if "get_sum_of_odd" in name_set and isinstance(sample, list):
        return [([[2, 3, 5, 8, 9]], 17)]
    if "get_elements_greater_than_average" in name_set and isinstance(sample, list):
        return [([[2, 4, 10, 12]], [10, 12])]
    if "get_elements_less_than_average" in name_set and isinstance(sample, list):
        return [([[2, 4, 10, 12]], [2, 4])]
    if "calculate_median" in name_set and isinstance(sample, list):
        return [([[9, 1, 5]], 5), ([[9, 1, 5, 7]], 6)]
    if "calculate_weighted_average" in name_set and isinstance(sample, list):
        return [([[10, 20, 30], [1, 1, 2]], 22.5)]
    if "get_strings_sorted_by_length" in name_set and isinstance(sample, list):
        return [([["aaaa", "b", "cc"]], ["b", "cc", "aaaa"])]
    if "get_pairs_summing_to" in name_set and isinstance(sample, list):
        return [([[2, 4, 5, 6, 8], 10], [[2, 8], [4, 6]])]
    if "get_numbers_summing_to_range" in name_set and isinstance(sample, list):
        return [([[1, 3, 4, 6], 7, 9], [[1, 6], [3, 4], [3, 6]])]
    if "get_frequency_dict" in name_set and isinstance(sample, list):
        return [([["x", "y", "x", "z", "y", "x"]], {"x": 3, "y": 2, "z": 1})]
    if "get_strings_with_all_vowels" in name_set and isinstance(sample, list):
        return [([["sequoia", "rhythm", "education", "hello"]], ["sequoia", "education"])]
    if "get_elements_with_max_frequency" in name_set and isinstance(sample, list):
        return [([[1, 1, 2, 2, 3]], [1, 2])]
    if "get_elements_by_frequency_range" in name_set and isinstance(sample, list):
        return [([["a", "a", "b", "b", "b", "c"], 2, 3], ["a", "b"])]
    if "calculate_statistical_summary" in name_set and isinstance(sample, list):
        return [([[2, 4, 6, 8]], {"mean": 5, "median": 5, "min": 2, "max": 8, "range": 6})]
    if "get_comprehensive_statistics" in name_set and isinstance(sample, list):
        return [([[2, 4, 6]], {"sum": 12, "average": 4, "min": 2, "max": 6, "count": 3, "standard_deviation": 1.632993161855452})]
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
    if "count_vowels_per_word" in name_set and isinstance(sample, str):
        return [(["code sky audio"], {"code": 2, "sky": 0, "audio": 4})]
    if "get_words_with_vowel_count" in name_set and isinstance(sample, str):
        return [(["code sky audio tree", 2], ["code", "tree"])]
    if "count_character_types" in name_set and isinstance(sample, str):
        return [(["A b2!"], {"vowels": 1, "consonants": 1, "digits": 1, "spaces": 1})]
    if "get_words_by_vowel_count" in name_set and isinstance(sample, str):
        return [(["sky code audio tree"], {0: ["sky"], 2: ["code", "tree"], 4: ["audio"]})]
    if "get_words_sorted_by_vowels" in name_set and isinstance(sample, str):
        return [(["audio sky code"], ["sky", "code", "audio"])]
    return []

def __auto_grader_named_metamorphic_cases(function_names, tests):
    if not tests:
        return []
    for case in tests:
        if not case.get("functionName"):
            return []
        simple_copy = {key: value for key, value in case.items() if key != "functionName"}
        if not __auto_grader_is_simple_case(simple_copy):
            return []
    name_set = set(function_names)
    cases = []
    def add(function_name, args, expected):
        if function_name in name_set:
            cases.append({"functionName": function_name, "args": args, "expected": expected, "label": "generated helper metamorphic"})
    if name_set >= {"sum_list", "add"}:
        add("sum_list", [[10, -3, 5]], 12)
        add("add", [-4, 9], 5)
    if name_set >= {"calculate_sum", "multiply"}:
        add("calculate_sum", [[10, -3, 5]], 12)
        add("multiply", [[-2, 4, 5]], -40)
    if name_set >= {"sum", "multiply"}:
        add("sum", [[10, -3, 5]], 12)
        add("multiply", [[-2, 4, 5]], -40)
    if name_set >= {"max_func", "max_in_list"}:
        add("max_func", [-8, -3], -3)
        add("max_in_list", [[-10, 0, 7, 3]], 7)
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

def __auto_grader_kwargs_metamorphic_cases(function_names, tests):
    if not tests:
        return []
    for case in tests:
        if not isinstance(case.get("kwargs"), dict) or not __auto_grader_is_simple_case({**case, "kwargs": {}}):
            return []
    name_set = set(function_names)
    if "sum_kwargs" in name_set:
        return [{"args": [], "kwargs": {"one": 1, "two": 2.5, "skip": "x"}, "expected": 3.5, "label": "generated kwargs metamorphic"}]
    if "even_kwargs" in name_set:
        return [{"args": [], "kwargs": {"a": 2, "b": 3, "c": 6, "d": "8"}, "expected": "a: 2\\nc: 6", "label": "generated kwargs metamorphic"}]
    if "sorted_kwargs" in name_set:
        return [{"args": [], "kwargs": {"gamma": 3, "alpha": 1, "beta": 2}, "expected": "alpha: 1\\nbeta: 2\\ngamma: 3", "label": "generated kwargs metamorphic"}]
    if "reverse_kwargs" in name_set:
        return [{"args": [], "kwargs": {"left": "L", "right": "R"}, "expected": {"L": "left", "R": "right"}, "label": "generated kwargs metamorphic"}]
    if "max_numeric" in name_set:
        return [{"args": [], "kwargs": {"a": -10, "b": 3.25, "c": "x"}, "expected": 3.25, "label": "generated kwargs metamorphic"}]
    if "even_or_odd_kwargs" in name_set:
        return [{"args": [], "kwargs": {"a": 1, "b": 2, "c": 3, "d": 4}, "expected": "Even", "label": "generated kwargs metamorphic"}]
    return []

def __auto_grader_run_metamorphic_tests(target, target_name, function_names, tests, compare):
    for index, (args, expected) in enumerate(__auto_grader_metamorphic_cases(function_names, tests), start=1):
        if not __auto_grader_accepts_args(target, args):
            continue
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            returned = target(*args)
            printed = sys.stdout.getvalue().strip()
        except Exception as exc:
            return f"extra generated test {index} raised {type(exc).__name__}: {exc}"
        finally:
            sys.stdout = old_stdout
        returned_ok = __auto_grader_same(returned, expected, compare)
        printed_ok = bool(printed) and __auto_grader_same(printed, expected, compare)
        if not printed_ok and (compare == "printedOrReturn" or returned is None):
            printed_ok = bool(printed) and __auto_grader_same(printed, expected, "printedOrReturn")
        if not returned_ok and not printed_ok:
            actual = printed if printed else returned
            return f"extra generated test {index} failed for args={args}. Expected {expected!r}, got {__auto_grader_jsonable(actual)!r}."
    if tests and len(tests) < 3:
        first_args = tests[0].get("args", [])
        if first_args and len(first_args) >= 1:
            probe_inputs = __auto_grader_generate_probe_inputs(first_args)
            if probe_inputs:
                outputs = []
                for probe_args in probe_inputs:
                    if not __auto_grader_accepts_args(target, probe_args):
                        continue
                    old_stdout = sys.stdout
                    sys.stdout = io.StringIO()
                    try:
                        result = target(*probe_args)
                        output = sys.stdout.getvalue().strip()
                    except Exception:
                        result = None
                        output = ""
                    finally:
                        sys.stdout = old_stdout
                    outputs.append((result, output))
                if len(outputs) >= 2:
                    all_same = all(
                        __auto_grader_deep_normalize(str(r)) == __auto_grader_deep_normalize(str(outputs[0][0]))
                        and __auto_grader_deep_normalize(o) == __auto_grader_deep_normalize(outputs[0][1])
                        for r, o in outputs[1:]
                    )
                    if all_same and outputs[0][0] is not None:
                        first_expected = tests[0].get("expected")
                        if not isinstance(first_expected, bool) and first_expected is not None:
                            return f"Hardcoded answer suspected: your function returned the same value {outputs[0][0]!r} for {len(outputs)} different inputs. Make sure your function computes the answer dynamically."
    return None

def __auto_grader_generate_probe_inputs(first_args):
    probes = []
    if all(isinstance(a, (int, float)) and not isinstance(a, bool) for a in first_args):
        probes.append([a * 2 + 1 for a in first_args])
        probes.append([a + 7 for a in first_args])
        probes.append([-a for a in first_args])
    elif all(isinstance(a, str) for a in first_args):
        probes.append([s + "x" for s in first_args])
        probes.append([s.upper() if s.islower() else s.lower() for s in first_args])
        probes.append(["test" + s for s in first_args])
    elif isinstance(first_args[0], list):
        probes.append([first_args[0] + [99]] + list(first_args[1:]))
        probes.append([first_args[0][::-1]] + list(first_args[1:]))
        probes.append([[]] + list(first_args[1:]))
    return probes[:3] if probes else []

def __auto_grader_function_script_test_cases(function_names, tests):
    cases = list(tests) + __auto_grader_input_generated_cases(function_names, tests)
    cases += __auto_grader_named_metamorphic_cases(function_names, tests)
    cases += __auto_grader_kwargs_metamorphic_cases(function_names, tests)
    for args, expected in __auto_grader_metamorphic_cases(function_names, tests):
        cases.append({"args": args, "expected": expected, "label": "generated script fallback"})
    return cases

def __auto_grader_is_function_script_case(case):
    blocked_keys = set()
    return not any(case.get(key) for key in blocked_keys)

def __auto_grader_script_helper_function(name):
    if name == "add_one":
        return lambda value: value + 1
    if name == "multiply_by_two":
        return lambda value: value * 2
    if name == "example_func":
        return lambda index, value: index * value
    return None

def __auto_grader_script_method_expression_args(expression):
    parsed = ast.parse(expression, mode="eval").body
    if not isinstance(parsed, ast.Call):
        raise ValueError("method expression must be a call")
    return [ast.literal_eval(arg) for arg in parsed.args]

def __auto_grader_script_namespace_for_args(args, required_name=None, call_args=None, method_name=None, method_args=None, attr_names=None, kwargs=None, expression_args=None, get_files=None, helper_functions=None, set_attrs=None, delete_attrs=None, set_items=None, delete_items=None, method_expression_args=None):
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

def __auto_grader_read_case_files(file_names):
    files = {}
    for file_name in file_names:
        try:
            with open(file_name, "r", encoding="utf-8") as result_file:
                files[file_name] = result_file.read()
        except FileNotFoundError:
            files[file_name] = None
    return files

def __auto_grader_script_result_matches(namespace, printed, expected, compare):
    if compare == "sourceOnly":
        return True
    result_names = ["result", "answer", "output", "total", "count", "value", "final", "res", "solution"]
    explicit_result_names = ["result", "answer", "output", "final", "res", "solution"]
    if expected is None and not printed and not any(name in namespace for name in explicit_result_names):
        return True
    if printed and (__auto_grader_same(printed, expected, compare) or __auto_grader_same(printed, expected, "printedOrReturn")):
        return True
    for name in result_names:
        if name in namespace and (
            __auto_grader_same(namespace[name], expected, compare) or
            __auto_grader_same(namespace[name], expected, "printedOrReturn")
        ):
            return True
    return False

def __auto_grader_run_function_script_fallback(function_names, tests, compare):
    test_cases = __auto_grader_function_script_test_cases(function_names, tests)
    if not test_cases or not all(__auto_grader_is_function_script_case(case) for case in test_cases):
        return None
    if all(case.get("expectedException") for case in test_cases):
        return None
    try:
        compiled = compile(__auto_grader_source, __auto_grader_source_name, "exec")
    except Exception as exc:
        return {
            "passed": False,
            "message": f"Script answer could not compile: {type(exc).__name__}: {exc}"
        }
    sample_output = None
    for index, case in enumerate(test_cases, start=1):
        expected = case.get("expected")
        hardcoded_error = __auto_grader_hardcoded_expected_error(expected)
        if hardcoded_error:
            return {
                "passed": False,
                "message": hardcoded_error
            }
        expected_exception = case.get("expectedException")
        args = list(case.get("args", []))
        expression_args = [eval(expression, {"math": math, "re": re, "json": json}) for expression in case.get("argExpressions", [])]
        args = args + expression_args
        helper_names = list(case.get("argFunctionNames", []))
        helper_functions = {name: __auto_grader_script_helper_function(name) for name in helper_names}
        function_list_names = list(case.get("functionListArgNames", []))
        function_list = [__auto_grader_script_helper_function(name) for name in function_list_names]
        if any(function is None for function in helper_functions.values()) or any(function is None for function in function_list):
            return None
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
        method_expression_args = [__auto_grader_script_method_expression_args(expression) for expression in case.get("callMethodArgExpressions", [])]
        input_values = list(case.get("inputValues", []))
        random_values = list(case.get("randomValues", []))
        random_float_values = list(case.get("randomFloatValues", []))
        random_choice_values = list(case.get("randomChoiceValues", []))
        random_sample_values = list(case.get("randomSampleValues", []))
        random_shuffle_values = list(case.get("randomShuffleValues", []))
        setup_remove = case.get("setupRemove", [])
        setup_dirs = case.get("setupDirs", [])
        setup_files = case.get("setupFiles", {})
        setup_symlinks = case.get("setupSymlinks", {})
        permission_denied_paths = set(case.get("permissionDeniedPaths", []))
        label = case.get("label") or ("script fallback test " + str(index))

        old_stdout = sys.stdout
        old_input = builtins.input
        old_open = builtins.open
        old_cwd = os.getcwd()
        old_sys_path = list(sys.path)
        temp_dir = tempfile.mkdtemp(prefix="auto_grader_script_")
        old_random_methods = {}
        sys.stdout = io.StringIO()
        printed = ""
        file_result = None
        exception_name = None
        exception_message = ""
        input_iter = iter(input_values)
        random_iter = iter(random_values)
        random_float_iter = iter(random_float_values)
        random_choice_iter = iter(random_choice_values)
        random_sample_iter = iter(random_sample_values)
        random_shuffle_iter = iter(random_shuffle_values)
        builtins.input = lambda prompt='': next(input_iter)

        def __fallback_guarded_open(file, *open_args, **open_kwargs):
            if str(file) in permission_denied_paths:
                raise PermissionError("Permission denied")
            return old_open(file, *open_args, **open_kwargs)
        try:
            os.chdir(temp_dir)
            if __auto_grader_project_root not in sys.path:
                sys.path.insert(0, __auto_grader_project_root)
            import random
            for __name in ("randint", "randrange", "random", "uniform", "choice", "sample", "shuffle", "choices"):
                old_random_methods[__name] = getattr(random, __name)
            if random_values:
                def __fallback_randint(_start, _end):
                    try:
                        return next(random_iter)
                    except StopIteration:
                        return random_values[-1]
                random.randint = __fallback_randint
                random.randrange = lambda *_args: __fallback_randint(0, 0)
            if random_float_values:
                def __fallback_random():
                    try:
                        return next(random_float_iter)
                    except StopIteration:
                        return random_float_values[-1]
                random.random = __fallback_random
                random.uniform = lambda _start, _end: __fallback_random()
            if random_choice_values:
                def __fallback_choice(_items):
                    try:
                        return next(random_choice_iter)
                    except StopIteration:
                        return random_choice_values[-1]
                random.choice = __fallback_choice
                random.choices = lambda _items, k=1: [__fallback_choice(_items) for _ in range(k)]
            if random_sample_values:
                def __fallback_sample(_items, _count):
                    try:
                        return list(next(random_sample_iter))
                    except StopIteration:
                        return list(random_sample_values[-1])
                random.sample = __fallback_sample
            if random_shuffle_values:
                def __fallback_shuffle(items):
                    try:
                        replacement = list(next(random_shuffle_iter))
                    except StopIteration:
                        replacement = list(random_shuffle_values[-1])
                    items[:] = replacement
                    return None
                random.shuffle = __fallback_shuffle
            for path_name in setup_remove:
                if os.path.islink(path_name) or os.path.isfile(path_name):
                    os.remove(path_name)
                elif os.path.isdir(path_name):
                    shutil.rmtree(path_name)
            for dir_name in setup_dirs:
                os.makedirs(dir_name, exist_ok=True)
            for file_name, file_content in setup_files.items():
                dir_name = os.path.dirname(file_name)
                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)
                with open(file_name, "w", encoding="utf-8") as setup_file:
                    setup_file.write(file_content)
            for link_name, target_name in setup_symlinks.items():
                dir_name = os.path.dirname(link_name)
                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)
                if os.path.lexists(link_name):
                    os.remove(link_name)
                os.symlink(target_name, link_name)
            if permission_denied_paths:
                builtins.open = __fallback_guarded_open
            namespace = __auto_grader_script_namespace_for_args(args, case.get("functionName"), call_args, method_name, method_args, attr_names, kwargs, expression_args, get_files, helper_functions, set_attrs, delete_attrs, set_items, delete_items, method_expression_args)
            exec(compiled, namespace)
            printed = sys.stdout.getvalue().strip()
            file_result = __auto_grader_read_case_files(get_files) if get_files else None
            if sample_output is None:
                sample_output = printed
        except Exception as exc:
            printed = sys.stdout.getvalue().strip()
            exception_name = type(exc).__name__
            exception_message = str(exc)
        finally:
            try:
                import random
                for __name, __method in old_random_methods.items():
                    setattr(random, __name, __method)
            except Exception:
                pass
            try:
                os.chdir(old_cwd)
            except Exception:
                pass
            sys.path[:] = old_sys_path
            sys.stdout = old_stdout
            builtins.input = old_input
            builtins.open = old_open
            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass
        if expected_exception:
            if exception_name != expected_exception:
                actual_exception = exception_name or "no exception"
                return {
                    "passed": False,
                    "message": f"{label} expected {expected_exception}, got {actual_exception}."
                }
            continue
        if exception_name:
            return {
                "passed": False,
                "message": f"{label} raised {exception_name}: {exception_message}"
            }
        file_ok = bool(get_files) and __auto_grader_same(file_result, expected, compare)
        if not file_ok and not __auto_grader_script_result_matches(namespace, printed, expected, compare):
            actual = file_result if get_files else printed if printed else namespace.get("result", None)
            return {
                "passed": False,
                "message": (
                    f"{label} failed as script answer. "
                    f"Expected {expected!r}, got {__auto_grader_jsonable(actual)!r}."
                )
            }
    return {
        "passed": True,
        "functionName": "script answer",
        "message": f"All {len(test_cases)} tests passed as a script answer.",
        "output": sample_output or ""
    }

def __auto_grader_run():
    if __auto_grader_spec.get("mode") == "script":
        source_requirement_error = __auto_grader_check_source_requirements()
        if source_requirement_error:
            return {
                "passed": False,
                "message": source_requirement_error
            }
        return __auto_grader_run_script()

    try:
        __auto_grader_load_function_namespace()
    except Exception as exc:
        return {
            "passed": False,
            "message": f"Could not prepare functions/classes for grading: {type(exc).__name__}: {exc}"
        }

    function_names = __auto_grader_spec.get("functionNames", [])
    compare = __auto_grader_spec.get("compare", "printedOrReturn")
    tests = __auto_grader_spec.get("tests", [])
    optional_tests = __auto_grader_spec.get("optionalTests", [])
    first_args = tests[0].get("args", []) if tests else []
    first_kwargs = tests[0].get("kwargs", {}) if tests else {}
    if tests and tests[0].get("argFunctionNames"):
        first_args = first_args + [None] * len(tests[0].get("argFunctionNames", []))
    if tests and tests[0].get("argExpressions"):
        first_args = first_args + [None] * len(tests[0].get("argExpressions", []))
    if tests and tests[0].get("functionListArgNames"):
        first_args = [None] + first_args
    target_name, target = __auto_grader_find_callable(function_names, first_args, kwargs=first_kwargs)
    active_tests = tests
    use_optional_tests = False
    if target is None and optional_tests:
        optional_first_args = optional_tests[0].get("args", [])
        optional_first_kwargs = optional_tests[0].get("kwargs", {})
        target_name, target = __auto_grader_find_callable(function_names, optional_first_args, kwargs=optional_first_kwargs)
        if target is not None:
            active_tests = optional_tests
            use_optional_tests = True

    if not use_optional_tests:
        source_requirement_error = __auto_grader_check_source_requirements()
        if source_requirement_error:
            return {
                "passed": False,
                "message": source_requirement_error
            }

    if target is None:
        script_result = __auto_grader_run_function_script_fallback(function_names, tests, compare)
        if script_result and script_result.get("passed"):
            return script_result
        if script_result:
            return script_result
        return {
            "passed": False,
            "message": "Missing function. Expected one of: " + ", ".join(function_names) + ". A script answer is also accepted if it passes every visible and generated test."
        }

    if use_optional_tests:
        test_cases = list(active_tests)
    else:
        test_cases = list(active_tests) + __auto_grader_input_generated_cases(function_names, active_tests) + __auto_grader_named_metamorphic_cases(function_names, active_tests) + __auto_grader_kwargs_metamorphic_cases(function_names, active_tests)
    for index, case in enumerate(test_cases, start=1):
        args = case.get("args", [])
        kwargs = case.get("kwargs", {})
        arg_function_names = case.get("argFunctionNames", [])
        arg_expressions = case.get("argExpressions", [])
        function_list_arg_names = case.get("functionListArgNames")
        expected = case.get("expected")
        setup_remove = case.get("setupRemove", [])
        setup_dirs = case.get("setupDirs", [])
        setup_files = case.get("setupFiles", {})
        setup_symlinks = case.get("setupSymlinks", {})
        permission_denied_paths = set(case.get("permissionDeniedPaths", []))
        get_files = case.get("getFiles")
        call_returned_with = case.get("callReturnedWith")
        call_method = case.get("callMethod")
        call_method_args = case.get("callMethodArgs", [])
        call_method_arg_expressions = case.get("callMethodArgExpressions", [])
        get_attrs = case.get("getAttrs")
        set_attrs = case.get("setAttrs", {})
        delete_attrs = case.get("deleteAttrs", [])
        set_items = case.get("setItems", [])
        delete_items = case.get("deleteItems", [])
        expected_exception = case.get("expectedException")
        input_values = list(case.get("inputValues", []))
        random_values = list(case.get("randomValues", []))
        random_float_values = list(case.get("randomFloatValues", []))
        random_choice_values = list(case.get("randomChoiceValues", []))
        random_sample_values = list(case.get("randomSampleValues", []))
        random_shuffle_values = list(case.get("randomShuffleValues", []))
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
        for arg_expression in arg_expressions:
            try:
                resolved_args.append(eval(arg_expression, globals()))
            except Exception as exc:
                return {
                    "passed": False,
                    "functionName": case_target_name,
                    "message": f"{label} could not prepare callable argument {arg_expression!r}: {type(exc).__name__}: {exc}"
                }
        if required_name:
            case_target_name, case_target = __auto_grader_find_callable(function_names, resolved_args, required_name, kwargs)
            if case_target is None:
                return {
                    "passed": False,
                    "message": f"{label} missing required function {required_name}()."
                }
        old_stdout = sys.stdout
        old_input = builtins.input
        old_open = builtins.open
        old_cwd = os.getcwd()
        old_sys_path = list(sys.path)
        temp_dir = tempfile.mkdtemp(prefix="auto_grader_")
        old_random_methods = {}
        sys.stdout = io.StringIO()
        input_iter = iter(input_values)
        random_iter = iter(random_values)
        random_float_iter = iter(random_float_values)
        random_choice_iter = iter(random_choice_values)
        random_sample_iter = iter(random_sample_values)
        random_shuffle_iter = iter(random_shuffle_values)
        builtins.input = lambda prompt='': next(input_iter)
        def __guarded_open(file, *open_args, **open_kwargs):
            if str(file) in permission_denied_paths:
                raise PermissionError("Permission denied")
            return old_open(file, *open_args, **open_kwargs)
        try:
            os.chdir(temp_dir)
            if __auto_grader_project_root not in sys.path:
                sys.path.insert(0, __auto_grader_project_root)
            import random
            for __name in ("randint", "randrange", "random", "uniform", "choice", "sample", "shuffle", "choices"):
                old_random_methods[__name] = getattr(random, __name)
            if random_values:
                def __function_randint(_start, _end):
                    try:
                        return next(random_iter)
                    except StopIteration:
                        return random_values[-1]
                random.randint = __function_randint
                random.randrange = lambda *_args: __function_randint(0, 0)
            if random_float_values:
                def __function_random():
                    try:
                        return next(random_float_iter)
                    except StopIteration:
                        return random_float_values[-1]
                random.random = __function_random
                random.uniform = lambda _start, _end: __function_random()
            if random_choice_values:
                def __function_choice(_items):
                    try:
                        return next(random_choice_iter)
                    except StopIteration:
                        return random_choice_values[-1]
                random.choice = __function_choice
                def __function_choices(_items, k=1):
                    values = []
                    for _index in range(k):
                        try:
                            values.append(next(random_choice_iter))
                        except StopIteration:
                            values.append(random_choice_values[-1])
                    return values
                random.choices = __function_choices
            if random_sample_values:
                def __function_sample(_items, _count):
                    try:
                        return list(next(random_sample_iter))
                    except StopIteration:
                        return list(random_sample_values[-1])
                random.sample = __function_sample
            if random_shuffle_values:
                def __function_shuffle(items):
                    try:
                        replacement = list(next(random_shuffle_iter))
                    except StopIteration:
                        replacement = list(random_shuffle_values[-1])
                    items[:] = replacement
                    return None
                random.shuffle = __function_shuffle
            for path_name in setup_remove:
                if os.path.islink(path_name) or os.path.isfile(path_name):
                    os.remove(path_name)
                elif os.path.isdir(path_name):
                    shutil.rmtree(path_name)
            for dir_name in setup_dirs:
                os.makedirs(dir_name, exist_ok=True)
            for file_name, file_content in setup_files.items():
                dir_name = os.path.dirname(file_name)
                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)
                with open(file_name, "w", encoding="utf-8") as setup_file:
                    setup_file.write(file_content)
            for link_name, target_name in setup_symlinks.items():
                dir_name = os.path.dirname(link_name)
                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)
                if os.path.lexists(link_name):
                    os.remove(link_name)
                os.symlink(target_name, link_name)
            if permission_denied_paths:
                builtins.open = __guarded_open
            returned = case_target(*resolved_args, **kwargs)
            if call_returned_with is not None:
                if not callable(returned):
                    return {
                        "passed": False,
                        "functionName": case_target_name,
                        "message": f"{label} expected {case_target_name}() to return a callable function."
                    }
                returned = returned(*call_returned_with)
            for attr_name, attr_value in set_attrs.items():
                setattr(returned, attr_name, attr_value)
            for attr_name in delete_attrs:
                delattr(returned, attr_name)
            for item_spec in set_items:
                returned[item_spec.get("key")] = item_spec.get("value")
            for item_key in delete_items:
                del returned[item_key]
            if call_method is not None:
                method = getattr(returned, call_method, None)
                if not callable(method):
                    return {
                        "passed": False,
                        "functionName": case_target_name,
                        "message": f"{label} expected returned object to have method {call_method}()."
                    }
                resolved_call_method_args = list(call_method_args)
                for call_method_arg_expression in call_method_arg_expressions:
                    try:
                        resolved_call_method_args.append(eval(call_method_arg_expression, globals()))
                    except Exception as exc:
                        return {
                            "passed": False,
                            "functionName": case_target_name,
                            "message": f"{label} could not prepare method argument {call_method_arg_expression!r}: {type(exc).__name__}: {exc}"
                        }
                returned = method(*resolved_call_method_args)
            if get_attrs is not None:
                returned = {name: getattr(returned, name, None) for name in get_attrs}
            if get_files is not None:
                returned = {}
                for file_name in get_files:
                    try:
                        with open(file_name, "r", encoding="utf-8") as result_file:
                            returned[file_name] = result_file.read()
                    except FileNotFoundError:
                        returned[file_name] = None
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
            try:
                import random
                for __name, __method in old_random_methods.items():
                    setattr(random, __name, __method)
            except Exception:
                pass
            try:
                os.chdir(old_cwd)
            except Exception:
                pass
            sys.path[:] = old_sys_path
            sys.stdout = old_stdout
            builtins.input = old_input
            builtins.open = old_open
            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass

        if expected_exception:
            return {
                "passed": False,
                "functionName": case_target_name,
                "message": f"{label} expected {expected_exception} to be raised."
            }

        returned_ok = __auto_grader_same(returned, expected, compare)
        printed_ok = bool(printed) and __auto_grader_same(printed, expected, compare)
        if not printed_ok and (compare == "printedOrReturn" or returned is None):
            printed_ok = __auto_grader_same(printed, expected, "printedOrReturn")
        if not returned_ok and not printed_ok and compare not in ("dictAddedPair",):
            returned_ok = __auto_grader_same(returned, expected, "lenient")
            printed_ok = bool(printed) and __auto_grader_same(printed, expected, "lenient")
        if not returned_ok and not printed_ok:
            actual = printed if printed else returned
            hint = ""
            if returned is None and printed and __auto_grader_same(printed, expected, "printedOrReturn"):
                hint = " Hint: your function printed the answer instead of returning it. Use 'return' instead of 'print'."
            elif returned is None and not printed:
                hint = " Hint: your function returned None and printed nothing. Make sure to use a 'return' statement."
            elif isinstance(returned, str) and isinstance(expected, (int, float)) and not isinstance(expected, bool):
                try:
                    if math.isclose(float(returned), float(expected), rel_tol=1e-6, abs_tol=1e-6):
                        hint = " Hint: your answer is correct but returned as a string. Try returning a number instead of printing it."
                except Exception:
                    pass
            elif isinstance(expected, str) and isinstance(returned, (int, float)) and not isinstance(returned, bool):
                hint = " Hint: expected a string but got a number. Try converting with str()."
            return {
                "passed": False,
                "functionName": case_target_name,
                "message": (
                    f"{label} failed for args={args}. "
                    f"Expected {expected!r}, got {__auto_grader_jsonable(actual)!r}."
                    + hint
                )
            }

    metamorphic_error = None if use_optional_tests else __auto_grader_run_metamorphic_tests(target, target_name, function_names, active_tests, compare)
    if metamorphic_error:
        return {
            "passed": False,
            "functionName": target_name,
            "message": metamorphic_error
        }

    return {
        "passed": True,
        "functionName": target_name,
        "message": f"All {len(test_cases)} tests passed using {target_name}()."
    }

def __auto_grader_run_script():
    compare = __auto_grader_spec.get("compare", "printedOrReturn")
    tests = __auto_grader_spec.get("tests", [])
    compiled = compile(__auto_grader_source, __auto_grader_source_name, "exec")
    sample_output = None

    for index, case in enumerate(tests, start=1):
        expected = case.get("expected")
        hardcoded_error = None if compare in ("sourceOnly", "sourceIntent") else __auto_grader_hardcoded_expected_error(expected)
        if hardcoded_error:
            return {
                "passed": False,
                "message": hardcoded_error
            }
        input_values = list(case.get("inputValues", []))
        random_values = list(case.get("randomValues", []))
        random_float_values = list(case.get("randomFloatValues", []))
        random_choice_values = list(case.get("randomChoiceValues", []))
        random_sample_values = list(case.get("randomSampleValues", []))
        random_shuffle_values = list(case.get("randomShuffleValues", []))
        setup_remove = case.get("setupRemove", [])
        setup_dirs = case.get("setupDirs", [])
        setup_files = case.get("setupFiles", {})
        setup_symlinks = case.get("setupSymlinks", {})
        permission_denied_paths = set(case.get("permissionDeniedPaths", []))
        label = case.get("label") or ("test " + str(index))

        old_stdout = sys.stdout
        old_input = builtins.input
        old_open = builtins.open
        old_cwd = os.getcwd()
        old_sys_path = list(sys.path)
        temp_dir = tempfile.mkdtemp(prefix="auto_grader_")
        old_random_methods = {}
        sys.stdout = io.StringIO()
        input_iter = iter(input_values)
        random_iter = iter(random_values)
        random_float_iter = iter(random_float_values)
        random_choice_iter = iter(random_choice_values)
        random_sample_iter = iter(random_sample_values)
        random_shuffle_iter = iter(random_shuffle_values)

        def __script_input(prompt=""):
            try:
                return next(input_iter)
            except StopIteration:
                raise Exception("No test input left for input().")

        builtins.input = __script_input
        def __script_guarded_open(file, *open_args, **open_kwargs):
            if str(file) in permission_denied_paths:
                raise PermissionError("Permission denied")
            return old_open(file, *open_args, **open_kwargs)
        try:
            os.chdir(temp_dir)
            if __auto_grader_project_root not in sys.path:
                sys.path.insert(0, __auto_grader_project_root)
            import random
            for __name in ("randint", "randrange", "random", "uniform", "choice", "sample", "shuffle", "choices"):
                old_random_methods[__name] = getattr(random, __name)
            if random_values:
                def __script_randint(_start, _end):
                    try:
                        return next(random_iter)
                    except StopIteration:
                        return random_values[-1]
                random.randint = __script_randint
                random.randrange = lambda *_args: __script_randint(0, 0)
            if random_float_values:
                def __script_random():
                    try:
                        return next(random_float_iter)
                    except StopIteration:
                        return random_float_values[-1]
                random.random = __script_random
                random.uniform = lambda _start, _end: __script_random()
            if random_choice_values:
                def __script_choice(_items):
                    try:
                        return next(random_choice_iter)
                    except StopIteration:
                        return random_choice_values[-1]
                random.choice = __script_choice
            if random_sample_values:
                def __script_sample(_items, _count):
                    try:
                        return list(next(random_sample_iter))
                    except StopIteration:
                        return list(random_sample_values[-1])
                random.sample = __script_sample
            if random_shuffle_values:
                def __script_shuffle(items):
                    try:
                        replacement = list(next(random_shuffle_iter))
                    except StopIteration:
                        replacement = list(random_shuffle_values[-1])
                    items[:] = replacement
                    return None
                random.shuffle = __script_shuffle
            if random_choice_values:
                def __script_choices(_items, k=1):
                    values = []
                    for _index in range(k):
                        try:
                            values.append(next(random_choice_iter))
                        except StopIteration:
                            values.append(random_choice_values[-1])
                    return values
                random.choices = __script_choices

            for path_name in setup_remove:
                if os.path.islink(path_name) or os.path.isfile(path_name):
                    os.remove(path_name)
                elif os.path.isdir(path_name):
                    shutil.rmtree(path_name)
            for dir_name in setup_dirs:
                os.makedirs(dir_name, exist_ok=True)
            for file_name, file_content in setup_files.items():
                dir_name = os.path.dirname(file_name)
                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)
                with open(file_name, "w", encoding="utf-8") as setup_file:
                    setup_file.write(file_content)
            for link_name, target_name in setup_symlinks.items():
                dir_name = os.path.dirname(link_name)
                if dir_name:
                    os.makedirs(dir_name, exist_ok=True)
                if os.path.lexists(link_name):
                    os.remove(link_name)
                os.symlink(target_name, link_name)
            if permission_denied_paths:
                builtins.open = __script_guarded_open
            namespace = {"__name__": "__main__", "re": re, "math": math, "json": json}
            exec(compiled, namespace)
            printed = sys.stdout.getvalue().strip()
            if sample_output is None:
                sample_output = printed
        except Exception as exc:
            return {
                "passed": False,
                "message": f"{label} raised {type(exc).__name__}: {exc}"
            }
        finally:
            try:
                import random
                for __name, __method in old_random_methods.items():
                    setattr(random, __name, __method)
            except Exception:
                pass
            try:
                os.chdir(old_cwd)
            except Exception:
                pass
            sys.path[:] = old_sys_path
            sys.stdout = old_stdout
            builtins.input = old_input
            builtins.open = old_open
            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass

        if not __auto_grader_same(printed, expected, compare):
            if not __auto_grader_same(printed, expected, "lenient"):
                hint = ""
                if not printed:
                    hint = " Hint: your code produced no output. Make sure to use print() to display the result."
                elif expected and isinstance(expected, str) and printed.lower() == expected.lower():
                    hint = " Hint: check capitalization — your output matches case-insensitively."
                return {
                    "passed": False,
                    "message": (
                        f"{label} failed. "
                        f"Expected output {expected!r}, got {__auto_grader_jsonable(printed)!r}."
                        + hint
                    )
                }

    return {
        "passed": True,
        "message": f"All {len(tests)} script tests passed.",
        "output": sample_output or ""
    }

__auto_grader_result = __auto_grader_run()
__auto_grader_json = json.dumps(__auto_grader_result)
`;

// BUILTIN TAB - Python Built-in Functions
const BUILTIN_CONTENT = `
# --- A ---

# abs(x)
# Returns the absolute value of a number. The argument can be int or float.
# In-depth: For integers, returns the non-negative magnitude. For floats,
# returns the positive magnitude. For complex numbers, returns sqrt(real^2 + imag^2).

print(abs(-5))     # 5
print(abs(3.14))   # 3.14
print(abs(-3.14))  # 3.14


# all(iterable)
# Returns True if all elements of the iterable are truthy (or iterable is empty).
# In-depth: Equivalent to a loop that short-circuits on the first falsy value.
# Empty iterables return True (vacuous truth).

print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([]))                    # True


# any(iterable)
# Returns True if any element of the iterable is truthy.
# In-depth: Short-circuits on the first truthy value. Returns False if empty.

print(any([False, False, True]))  # True
print(any([False, False]))        # False
print(any([]))                    # False


# ascii(object)
# Returns a string containing a printable representation of object, escaping
# non-ASCII characters with \\\\u or \\\\U escapes.
# In-depth: Like repr(), but escapes non-ASCII so the result is pure ASCII.
# Useful for safe display of strings with international characters.

print(ascii("hello"))           # 'hello'
print(ascii("café"))           # 'caf\\\\u00e9'
print(ascii("\\\\n"))             # '\\\\n'


# --- B ---

# bin(x)
# Converts an integer to a binary string prefixed with "0b".
# In-depth: The result is a valid Python expression. x must be an integer.
# Use format(x, 'b') to get the binary without the prefix.

print(bin(3))     # 0b11
print(bin(10))    # 0b1010
print(bin(-5))    # -0b101


# bool(x=False)
# Returns a boolean value: True or False.
# In-depth: Converts x to True or False using the standard truth-testing
# procedure (empty sequences/zero/None are False, everything else is True).
# bool is a subclass of int, so True == 1 and False == 0.

print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool("abc"))   # True


# bytearray(source=b'', encoding='utf-8')
# Returns a mutable array of bytes.
# In-depth: Arguments: string + encoding -> encode; integer -> array of zeros
# of that size; iterable of ints -> initialize from ints; bytes-like -> copy.
# The resulting object is mutable and supports list-like operations.

print(bytearray(5))              # bytearray(b'\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00')
print(bytearray([65, 66, 67]))   # bytearray(b'ABC')
print(bytearray("abc", "utf-8")) # bytearray(b'abc')


# bytes(source=b'', encoding='utf-8')
# Returns an immutable sequence of bytes.
# In-depth: Same construction rules as bytearray, but the result is immutable.
# Use bytes literals (b'...') for literal byte strings in code.

print(bytes(5))                  # b'\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00'
print(bytes([65, 66, 67]))       # b'ABC'
print(bytes("abc", "utf-8"))     # b'abc'


# --- C ---

# callable(object)
# Returns True if object appears callable (can be invoked with () operator).
# In-depth: Checks for __call__ in the class. May return True for objects
# whose __call__ raises TypeError. Does not guarantee invocation succeeds.

print(callable(print))      # True
print(callable(42))         # False
print(callable(lambda: 0))  # True


# chr(i)
# Returns the Unicode character represented by integer i.
# In-depth: i must be in range 0x110000 (0 to 1,114,111). Inverse of ord().
# Raises ValueError if i is outside the valid range.

print(chr(65))      # A
print(chr(8364))    # €
print(chr(128640))  # 🚀


# classmethod(function)
# Transforms a method into a class method, receiving the class as first arg.
# In-depth: A class method receives the class (cls) implicitly as the first
# argument, not the instance (self). Can be called on the class or instance.
# Commonly used as a decorator: @classmethod.

class MyClass:
    @classmethod
    def greet(cls):
        return f"Hello from {cls.__name__}"

print(MyClass.greet())  # Hello from MyClass


# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# Compiles source code into a code object executable by exec() or eval().
# In-depth: mode is 'exec' for module-level code, 'eval' for single expression,
# or 'single' for a single interactive statement. filename should be the file
# the code was read from; use '<string>' if it came from a string.

code = compile("x = 42\\\\nprint(x)", "<string>", "exec")
exec(code)  # 42


# complex(real=0, imag=0)
# Creates a complex number from real and imaginary components.
# In-depth: Accepts two numeric args (real, imag) or a string argument
# (like "1+2j"). The string form must not have whitespace around the +.

print(complex(2, 3))     # (2+3j)
print(complex("1+2j"))   # (1+2j)
print(complex(5))        # (5+0j)


# --- D ---

# delattr(object, name)
# Deletes the named attribute from object, equivalent to del object.name.
# In-depth: name must be a string. Raises AttributeError if the attribute
# doesn't exist. The inverse of setattr().

class Person:
    name = "Alice"
    age = 30

delattr(Person, "age")
print(hasattr(Person, "age"))  # False


# dict(**kwargs)
# Creates a new dictionary (mapping of keys to values).
# In-depth: Accepts keyword args, an iterable of key-value pairs, or
# another mapping. Dicts are ordered (insertion order preserved as of 3.7).

print(dict(a=1, b=2))                    # {'a': 1, 'b': 2}
print(dict([("x", 10), ("y", 20)]))      # {'x': 10, 'y': 20}
print(dict({"one": 1}, two=2))           # {'one': 1, 'two': 2}


# dir(object)
# Returns a sorted list of names in the current or given object's scope.
# In-depth: Without args, returns names in current scope. With an object,
# returns its attributes (including inherited ones). Tries __dir__() first.

print(dir([]))       # [... 'append', 'clear', 'copy', 'count'...]
print(dir(42))       # [... 'bit_length', 'conjugate', 'denominator'...]
print("sort" in dir([]))  # True


# divmod(a, b)
# Returns a tuple (a // b, a % b) — quotient and remainder.
# In-depth: Uses floor division. For integers, result is (floor division,
# modulus). For floats, returns (floor div, remainder) with floating math.
# The relationship: a = b * quotient + remainder.

print(divmod(13, 4))   # (3, 1)
print(divmod(10, 3))   # (3, 1)
print(divmod(7, 2))    # (3, 1)


# --- E ---

# enumerate(iterable, start=0)
# Returns an enumerate object yielding (index, element) pairs.
# In-depth: Useful for loop iteration when you need both the index and value.
# The start parameter controls the beginning index.

for i, v in enumerate(["a", "b", "c"]):
    print(i, v)
# 0 a
# 1 b
# 2 c

print(list(enumerate("abc", start=1)))
# [(1, 'a'), (2, 'b'), (3, 'c')]


# eval(expression, globals=None, locals=None)
# Evaluates a string as a Python expression and returns the result.
# In-depth: expression must be a single expression (not statements). Can
# accept optional globals and locals dicts for namespace control.
# Security risk: never eval untrusted input.

x = 10
print(eval("x * 2"))        # 20
print(eval("pow(2, 3)"))    # 8
print(eval("[n*2 for n in range(5)]"))  # [0, 2, 4, 6, 8]


# exec(object, globals=None, locals=None)
# Executes dynamically created Python code (statements and expressions).
# In-depth: Unlike eval(), exec() supports statements (def, class, import,
# loops). Returns None. Modifies the provided namespace if given.

code = """
result = []
for i in range(3):
    result.append(i * 10)
"""
ns = {}
exec(code, ns)
print(ns["result"])  # [0, 10, 20]


# --- F ---

# filter(function, iterable)
# Constructs an iterator yielding elements from iterable where function returns True.
# In-depth: If function is None, uses the identity function (filters falsy values).
# Equivalent to: (item for item in iterable if function(item)).

print(list(filter(None, [0, 1, "", "hi", [], [1]])))
# [1, 'hi', [1]]

print(list(filter(lambda x: x % 2 == 0, range(10))))
# [0, 2, 4, 6, 8]


# float(x=0.0)
# Converts a number or string to a floating-point number.
# In-depth: Accepts int, float, or string. Strings can be NaN, Inf, or
# regular decimal strings. Raises ValueError for invalid inputs.

print(float(42))        # 42.0
print(float("3.14"))    # 3.14
print(float("inf"))     # inf
print(float("nan"))     # nan


# format(value, format_spec='')
# Formats a value according to a format specification.
# In-depth: Calls value.__format__(format_spec). The format_spec uses
# the mini-language: padding, alignment, precision, type codes.

print(format(255, 'b'))      # 11111111
print(format(255, 'x'))      # ff
print(format(3.14159, '.2f'))  # 3.14
print(format(42, '06d'))     # 000042


# frozenset(iterable=set())
# Returns an immutable, hashable set object.
# In-depth: Like set() but immutable, so it can be used as a dict key or
# set element. Cannot be modified after creation.

fs = frozenset([1, 2, 3, 2])
print(fs)            # frozenset({1, 2, 3})
print({fs: "works"})  # {frozenset({1, 2, 3}): 'works'}


# --- G ---

# getattr(object, name, default=None)
# Returns the value of the named attribute of object.
# In-depth: Equivalent to object.name. If the attribute doesn't exist and
# default is provided, returns default. Without default, raises AttributeError.

class Point:
    x = 10
    y = 20

pt = Point()
print(getattr(pt, "x"))          # 10
print(getattr(pt, "z", "N/A"))   # N/A


# globals()
# Returns a dictionary of the current global symbol table.
# In-depth: The dict is the module-level namespace. Modifying it changes
# global variables. Inside a function, returns the globals of the module
# where the function was defined.

print(type(globals()))   # <class 'dict'>
print("__file__" in globals())  # True


# --- H ---

# hasattr(object, name)
# Returns True if object has the named attribute (string name).
# In-depth: Implements by calling getattr() and catching AttributeError.
# Returns False if the attribute does not exist.

class Car:
    wheels = 4
    color = "red"

c = Car()
print(hasattr(c, "wheels"))   # True
print(hasattr(c, "engine"))   # False


# hash(object)
# Returns the hash value of object (an integer) for use in dict lookups.
# In-depth: Hashable objects must have equal hashes when compared equal.
# Mutable objects (lists, dicts, sets) are not hashable. Strings, ints,
# tuples of hashables are. Raises TypeError for unhashable types.

print(hash(42))           # 42
print(hash("hello"))      # some large integer
print(hash((1, 2, 3)))    # some integer


# help(object)
# Invokes the built-in help system for the given object.
# In-depth: Shows documentation: docstrings, methods, attributes. Can be
# called without args to enter interactive help. Not typically kept in
# production code — used interactively or in debugging.

# help(print)
# help(dict)
# help(str.upper)


# hex(x)
# Converts an integer to a hexadecimal string prefixed with "0x".
# In-depth: x must be an integer. Returns lowercase. Use format(x, 'X')
# for uppercase hex. Inverse of int(string, 16).

print(hex(255))    # 0xff
print(hex(16))     # 0x10
print(hex(-42))    # -0x2a


# --- I ---

# id(object)
# Returns the identity (memory address) of an object as an integer.
# In-depth: Unique and constant for the object's lifetime. Two objects
# with non-overlapping lifetimes may have the same id(). On CPython,
# this is the memory address.

a = [1, 2, 3]
print(id(a))        # 140342345678912
print(id([1, 2]))   # different memory address


# input(prompt='')
# Reads a line from stdin, converts to string (stripping the trailing newline).
# In-depth: If prompt is given, writes it to stdout without a trailing newline.
# On EOF, raises EOFError. The result is always a string.

# name = input("Enter name: ")
# print(f"Hello, {name}")


# int(x=0, base=10)
# Converts a number or string to an integer.
# In-depth: With a string, base can be 0 (auto-detect) or 2-36. With a
# number, truncates toward zero (like int(3.9) -> 3). Without args, returns 0.

print(int(3.14))       # 3
print(int("1010", 2))  # 10
print(int("ff", 16))   # 255
print(int("0xA", 0))   # 10


# isinstance(object, classinfo)
# Returns True if object is an instance of classinfo (or a tuple of classes).
# In-depth: Checks against class, subclass, or tuple of classes and types.
# Supports abstract base classes (e.g., isinstance([], Iterable) -> True).

print(isinstance(42, int))                 # True
print(isinstance([], (list, tuple)))        # True
print(isinstance("abc", str))              # True


# issubclass(class, classinfo)
# Returns True if class is a subclass of classinfo (direct, indirect, or virtual).
# In-depth: classinfo can be a class or tuple of classes. A class is considered
# a subclass of itself. Checks virtual inheritance via ABCs.

class A: pass
class B(A): pass

print(issubclass(B, A))      # True
print(issubclass(A, A))      # True
print(issubclass(bool, int)) # True


# iter(object, sentinel=None)
# Returns an iterator object for the given object.
# In-depth: With one arg, calls object.__iter__() or builds an iterator
# from __getitem__(). With sentinel, calls object repeatedly until sentinel.

print(list(iter([1, 2, 3])))     # [1, 2, 3]
print(list(iter("abc")))         # ['a', 'b', 'c']


# --- L ---

# len(object)
# Returns the length (number of items) of a container.
# In-depth: Calls __len__() magic method. Works on sequences, mappings,
# sets, and any object implementing __len__. Raises TypeError otherwise.

print(len([1, 2, 3]))        # 3
print(len("hello"))          # 5
print(len({"a": 1, "b": 2})) # 2


# list(iterable=())
# Creates a new list from an iterable (or empty list if no argument).
# In-depth: Accepts any iterable. Lists are ordered, mutable sequences.
# Can also use square bracket literals [].

print(list((1, 2, 3)))       # [1, 2, 3]
print(list("abc"))           # ['a', 'b', 'c']
print(list(range(5)))        # [0, 1, 2, 3, 4]


# locals()
# Returns a dictionary of the current local symbol table.
# In-depth: Inside a function, returns the local names. At module level,
# returns the same as globals(). Modifying the dict may not affect local
# variables (behavior is implementation-dependent).

def test():
    x = 10
    y = 20
    print(locals())

test()  # {'x': 10, 'y': 20}


# --- M ---

# map(function, *iterables)
# Applies function to every item of iterable(s), yielding results.
# In-depth: Returns an iterator. With multiple iterables, function must
# accept that many arguments. Stops at the shortest iterable. Equivalent
# to a generator expression.

print(list(map(str.upper, ["a", "b", "c"])))
# ['A', 'B', 'C']

print(list(map(pow, [2, 3, 4], [5, 2, 3])))
# [32, 9, 64]


# max(iterable, *[, key, default])
# Returns the largest item in an iterable or among arguments.
# In-depth: With a single iterable, returns its max element. With multiple
# args, returns the max of those. key is a one-arg ordering function.
# default is returned if the iterable is empty (otherwise ValueError).

print(max(3, 7, 1, 9))          # 9
print(max([10, 20, 30]))        # 30
print(max("hello world"))       # 'w'
print(max([], default="empty")) # empty


# memoryview(object)
# Returns a memoryview object exposing buffer protocol access.
# In-depth: Allows memory-efficient access to data without copying.
# Supports slicing, indexing, and casting. Useful for binary data and
# large byte arrays where copying would be expensive.

mv = memoryview(b"hello")
print(mv[0])         # 104
print(mv[1:3].tobytes())  # b'el'


# min(iterable, *[, key, default])
# Returns the smallest item in an iterable or among arguments.
# In-depth: With a single iterable, returns its min element. With multiple
# args, returns the min of those. key is a one-arg ordering function.

print(min(3, 7, 1, 9))          # 1
print(min([10, 20, 30]))        # 10
print(min("hello world"))       # ' '
print(min([], default="empty")) # empty


# --- N ---

# next(iterator, default=None)
# Retrieves the next item from an iterator.
# In-depth: Calls iterator.__next__(). If the iterator is exhausted and
# default is given, returns default. Without default, raises StopIteration.

it = iter([1, 2, 3])
print(next(it))        # 1
print(next(it))        # 2
print(next(it))        # 3
print(next(it, "done"))  # done


# --- O ---

# object()
# Returns a new featureless object (the base for all classes).
# In-depth: The base class of all Python objects. Provides common methods
# like __str__, __repr__, __eq__, __hash__. Cannot have arbitrary
# attributes set on instances of plain object() directly.

obj = object()
print(isinstance(obj, object))  # True
print(type(obj).__name__)       # 'object'


# oct(x)
# Converts an integer to an octal string prefixed with "0o".
# In-depth: x must be an integer. Returns lowercase. Use format(x, 'o')
# for the octal representation without the prefix.

print(oct(8))    # 0o10
print(oct(64))   # 0o100
print(oct(-10))  # -0o12


# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Opens file and returns a file object.
# In-depth: mode is 'r' (read), 'w' (write), 'a' (append), 'x' (create),
# 'b' (binary), 't' (text), '+'. Encoding is needed for text mode.
# Always use with context manager (with statement).

# with open("example.txt", "w") as f:
#     f.write("Hello")

# with open("example.txt", "r") as f:
#     print(f.read())


# ord(c)
# Returns the Unicode code point (integer) for a single character string.
# In-depth: Inverse of chr(). For ASCII characters, returns 0-127.
# For emoji, returns the full Unicode code point.

print(ord("A"))     # 65
print(ord("€"))     # 8364
print(ord("🚀"))    # 128640


# --- P ---

# pow(base, exp, mod=None)
# Returns base raised to power exp, optionally modulo mod.
# In-depth: With mod, computes (base**exp) % mod efficiently for large
# numbers using modular exponentiation. mod must be non-zero.

print(pow(2, 3))       # 8
print(pow(2, 3, 5))    # 3  (8 % 5)
print(pow(10, -2))     # 0.01


# print(*objects, sep=' ', end='\\\\n', file=None, flush=False)
# Prints objects to the text stream file (default stdout), separated by sep.
# In-depth: Converts objects to strings using str(). Keyword args control
# separator, terminator, output file, and flushing. Returns None.

print("Hello", "World")            # Hello World
print("A", "B", "C", sep="-")      # A-B-C
print("Loading...", end="")        # no newline


# property(fget=None, fset=None, fdel=None, doc=None)
# Returns a managed attribute descriptor (getter/setter/deleter).
# In-depth: Typically used as a decorator. Allows defining getter, setter,
# and deleter methods that control attribute access. The doc string
# becomes the attribute's docstring.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature(0)
print(t.fahrenheit)  # 32.0
t.fahrenheit = 100
print(t._celsius)    # 37.777... (approx)


# --- R ---

# range(stop) | range(start, stop, step=1)
# Returns an immutable arithmetic progression of integers.
# In-depth: Generates numbers from start (default 0) to stop (exclusive),
# incrementing by step. Lazy — computes values on iteration. Memory
# efficient even for huge ranges.

print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(2, 7)))        # [2, 3, 4, 5, 6]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))    # [5, 4, 3, 2, 1]


# repr(object)
# Returns a string containing a printable representation of object.
# In-depth: Should look like a valid Python expression that recreates
# the object. For debugging. In contrast to str(), repr() aims to be
# unambiguous rather than readable.

print(repr("hello"))    # "'hello'"
print(repr([1, 2, 3]))  # '[1, 2, 3]'
print(repr(42))         # '42'


# reversed(sequence)
# Returns a reverse iterator over a sequence.
# In-depth: Works on any sequence with __reversed__() or __len__() +
# __getitem__(). For iterables that aren't sequences, use reversed()
# by converting to list first.

print(list(reversed([1, 2, 3])))  # [3, 2, 1]
print(list(reversed("abc")))      # ['c', 'b', 'a']


# round(number, ndigits=None)
# Rounds a number to ndigits precision (default 0).
# In-depth: Banker's rounding: rounds .5 to the nearest even number.
# For floats, ndigits can be negative (rounds to powers of 10).
# Returns int when ndigits is omitted, float otherwise.

print(round(3.14159, 2))   # 3.14
print(round(2.5))          # 2 (banker's rounding)
print(round(3.5))          # 4 (banker's rounding)
print(round(12345, -2))    # 12300


# --- S ---

# set(iterable=None)
# Returns a new set object (unordered collection of unique hashable items).
# In-depth: Elements must be hashable. Sets support union, intersection,
# difference, symmetric difference. Mutable — add/remove elements.

print(set([1, 2, 2, 3, 3]))   # {1, 2, 3}
print(set("abracadabra"))      # {'a', 'b', 'c', 'd', 'r'}
print(set())                   # set()


# setattr(object, name, value)
# Sets the named attribute on object (equivalent to object.name = value).
# In-depth: name must be a string. Useful when the attribute name is
# dynamic. Can set attributes on most objects (instances, classes, modules).

class User:
    pass

u = User()
setattr(u, "username", "alice")
setattr(u, "score", 100)
print(u.username)  # alice
print(u.score)     # 100


# slice(stop) | slice(start, stop, step=None)
# Returns a slice object representing a range of indices.
# In-depth: Used for extended slicing: obj[slice(1, 5)] is equivalent
# to obj[1:5]. Stores start, stop, step attributes.

s = slice(1, 5, 2)
print(s)                       # slice(1, 5, 2)
print([0, 1, 2, 3, 4, 5][s])  # [1, 3]


# sorted(iterable, *, key=None, reverse=False)
# Returns a new sorted list from the items in iterable.
# In-depth: Stable sort (preserves order of equal elements). key is a
# function that extracts a comparison key. reverse=True for descending.
# The Timsort algorithm (hybrid stable sort, O(n log n)).

print(sorted([3, 1, 4, 1, 5]))              # [1, 1, 3, 4, 5]
print(sorted("python"))                      # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted(["bb", "a", "ccc"], key=len))   # ['a', 'bb', 'ccc']
print(sorted([3, 1, 4], reverse=True))       # [4, 3, 1]


# staticmethod(function)
# Transforms a method into a static method (no implicit first argument).
# In-depth: Static methods don't receive self or cls. They behave like
# regular functions but belong to the class namespace. Used as a
# decorator: @staticmethod.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 4))  # 7


# str(object='', encoding='utf-8', errors='strict')
# Returns a string version of object (human-readable representation).
# In-depth: Calls object.__str__() if available, else __repr__().
# Encoding and errors are only valid if object is a bytes-like object.
# Without args, returns empty string.

print(str(42))          # '42'
print(str([1, 2, 3]))   # '[1, 2, 3]'
print(str(b"abc"))      # "b'abc'"


# sum(iterable, start=0)
# Sums the items of an iterable from left to right, starting with start.
# In-depth: start is added to the total. For strings, use ''.join().
# For non-numeric types that support +, provide an appropriate start.

print(sum([1, 2, 3, 4]))          # 10
print(sum([1, 2, 3], 10))         # 16
print(sum([[1], [2], [3]], []))   # [1, 2, 3]


# super(type=None, object_or_type=None)
# Returns a proxy object delegating method calls to a parent class.
# In-depth: Used in cooperative multiple inheritance. Without args,
# returns the super object bound to the current class and instance.
# Essential for calling parent __init__() from child classes.

class Base:
    def greet(self):
        return "Base"

class Child(Base):
    def greet(self):
        return super().greet() + " -> Child"

print(Child().greet())  # Base -> Child


# --- T ---

# tuple(iterable=())
# Creates a new tuple from an iterable (or empty tuple if no argument).
# In-depth: Tuples are immutable, ordered sequences. Can be used as dict
# keys (if all elements are hashable). Parentheses optional in many cases.

print(tuple([1, 2, 3]))       # (1, 2, 3)
print(tuple("abc"))           # ('a', 'b', 'c')
print(tuple())                # ()


# type(object) | type(name, bases, dict)
# With one arg, returns the type of object. With three, creates a new class.
# In-depth: type() is a metaclass. With three args: name (string), bases
# (tuple of parent classes), dict (namespace dict). Equivalent to class statement.

print(type(42))              # <class 'int'>
print(type("hello"))         # <class 'str'>

MyClass = type("MyClass", (object,), {"x": 10})
obj = MyClass()
print(obj.x)                 # 10


# --- V ---

# vars(object=None)
# Returns the __dict__ (namespace dict) of the given object.
# In-depth: With no args, equivalent to locals(). With an object, returns
# its __dict__ attribute. Raises TypeError if object doesn't have __dict__
# (e.g., class with __slots__).

class MyObj:
    def __init__(self):
        self.a = 1
        self.b = 2

obj = MyObj()
print(vars(obj))  # {'a': 1, 'b': 2}


# --- Z ---

# zip(*iterables, strict=False)
# Iterates over multiple iterables in parallel, yielding tuples.
# In-depth: Stops at the shortest iterable. strict=True (3.10+) raises
# ValueError if lengths differ. Use itertools.zip_longest for unequal
# lengths with fill value.

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))
# [('a', 1), ('b', 2), ('c', 3)]

print(dict(zip(letters, numbers)))
# {'a': 1, 'b': 2, 'c': 3}


# --- _ ---

# __import__(name, globals=None, locals=None, fromlist=(), level=0)
# Imports a module by name string (the underlying import implementation).
# In-depth: Advanced usage; prefer importlib.import_module() for most
# dynamic imports. fromlist controls whether submodules are imported.
# level: 0 for absolute, positive for relative (1 = current package).

os = __import__("os")
print(os.pathsep)  # ':'
`;

// RULES TAB - Complete Python Reference
const RULES_CONTENT = `
# PYTHON RULES — Complete Reference
# ================================
# This is a comprehensive Python reference rendered in CodeMirror.
# All explanations use # comments (gray), code examples use full
# Python syntax highlighting (keywords blue, strings green, etc.).
# ================================


# 1. VARIABLES & DATA TYPES
# =========================
# Easy definition: Variables are named containers that store references
# to objects in memory. Python is dynamically typed — you never declare
# a variable's type explicitly.
# In-depth: Every variable is a name bound to an object. The type is
# determined at runtime by the object itself. Multiple names can refer
# to the same object (aliasing). Python uses reference counting and
# garbage collection under the hood.

# Creating variables
name = "Alice"
age = 30
height = 5.7
is_student = True
nothing = None

# Dynamic typing — variables can change type freely
value = 42
print(type(value))          # <class 'int'>
value = "now a string"
print(type(value))          # <class 'str'>

# type() and id() — introspection tools
print(type(42))             # <class 'int'>
print(id(name))             # unique memory address (integer)

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0               # all three bound to same 0

# Pythonic swap
a, b = b, a

# Delete a variable
del value                   # removes the name binding

# Built-in data types
some_int = 42               # int
some_float = 3.14           # float
some_str = "hello"          # str
some_bool = True            # bool (subclass of int)
some_bytes = b"hello"       # bytes
some_bytearray = bytearray(b"hello")  # bytearray (mutable)

# Naming rules:
# - Must start with letter or underscore
# - Rest can be letters, digits, underscores
# - Case-sensitive: total != Total != TOTAL
# - Cannot use reserved keywords (if, else, for, while, class, def, etc.)
# - Convention: snake_case for variables/functions, UPPER_CASE for constants


# 2. NUMBERS & MATH
# ==================
# Easy definition: Python has integers (unbounded) and floats (IEEE 754
# double-precision). All standard arithmetic operations are supported.
# In-depth: int has arbitrary precision — no overflow. float follows
# IEEE 754 and may have rounding issues. Complex numbers use j suffix.
# The math module provides additional functions.

# Integers — arbitrary precision
big_num = 10**100
print(big_num)              # 100000000000000000000000000000000000000000000000000...

# Floats
pi = 3.14159
sci = 1.5e-10              # scientific notation

# Arithmetic operators
print(10 + 3)               # 13  addition
print(10 - 3)               # 7   subtraction
print(10 * 3)               # 30  multiplication
print(10 / 3)               # 3.3333333333333335  true division (always float)
print(10 // 3)              # 3   floor division (integer result)
print(10 % 3)               # 1   modulus (remainder)
print(10 ** 3)              # 1000  exponentiation (power)

# Floor division details — rounds toward negative infinity
print(-10 // 3)             # -4  (not -3! floors down)
print(10 // -3)             # -4

# Modulus with negatives — result has sign of divisor
print(-10 % 3)              # 2
print(10 % -3)              # -2

# Augmented assignment
x = 10
x += 5                      # x = 15  (x = x + 5)
x -= 3                      # x = 12
x *= 2                      # x = 24
x /= 4                      # x = 6.0
x //= 2                     # x = 3.0
x %= 2                      # x = 1.0
x **= 3                     # x = 1.0

# Type conversion
print(int(3.9))             # 3  (truncates toward zero)
print(float(5))             # 5.0
print(str(42))              # "42"
print(bool(1))              # True
print(bool(0))              # False
print(int("101", 2))        # 5  (parse binary string)

# round(), abs(), divmod(), pow()
print(round(3.14159, 2))    # 3.14
print(abs(-5))              # 5
print(divmod(17, 5))        # (3, 2)  quotient and remainder
print(pow(2, 10))           # 1024
print(pow(2, 10, 1000))     # 24  (2**10 % 1000, more efficient)

# math module
import math

print(math.ceil(3.2))       # 4
print(math.floor(3.9))      # 3
print(math.sqrt(16))        # 4.0
print(math.pow(2, 10))      # 1024.0  (returns float)
print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828459045
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(0))          # 0.0
print(math.log(100, 10))    # 2.0  (log base 10)
print(math.log(math.e))     # 1.0  (natural log)
print(math.factorial(5))    # 120
print(math.gcd(12, 18))     # 6
print(math.isfinite(1e308)) # True
print(math.isinf(float("inf")))  # True
print(math.isnan(float("nan")))  # True

# Complex numbers
c = 3 + 4j
print(c.real)               # 3.0
print(c.imag)               # 4.0
print(c.conjugate())        # (3-4j)
print(abs(c))               # 5.0  (magnitude)
import cmath
print(cmath.phase(c))       # phase angle


# 3. STRINGS
# ===========
# Easy definition: Strings are immutable sequences of Unicode characters.
# They can be created with single, double, or triple quotes.
# In-depth: Strings are sequences and support all sequence operations
# (indexing, slicing, len, in). They are immutable — every operation
# returns a new string. Python 3 strings are Unicode by default.

# Creating strings
single = 'hello'
double = "hello"
multiline = """This is a
multi-line string"""
multiline2 = '''Also multi-line'''

# Escape sequences
escaped = "She said, \\"Hello!\\""
newline = "Line 1\\nLine 2"
tabbed = "Column 1\\tColumn 2"
backslash = "C:\\\\Users\\\\Name"
raw_path = r"C:\\Users\\Name"     # raw string — no escape processing

# f-strings (Python 3.6+)
name = "Alice"
age = 30
greeting = f"Hello, {name}. You are {age} years old."
calc = f"2 + 2 = {2 + 2}"
formatted = f"Pi is approximately {math.pi:.3f}"
expr = f"{name.lower()} is {age // 10} decades old"
# Use {{ and }} for literal braces
braces = f"{{name}} is a literal template"

# str.format() method
template = "Hello, {}. You are {} years old."
print(template.format("Bob", 25))

named = "Hello, {name}. You are {age} years old."
print(named.format(name="Carol", age=35))

positional = "{0} is {1} and {0} likes Python"
print(positional.format("Dave", "cool"))

fancy = "{:>10} {:06.2f}".format("pi", 3.14159)
# right-aligned in 10 chars, float zero-padded 6 width 2 decimals

# % operator formatting (older style)
print("%s is %d years old" % ("Eve", 28))
print("Value: %.2f" % 3.14159)

# Common string methods
text = "  Hello, World!  "
print(text.upper())             # "  HELLO, WORLD!  "
print(text.lower())             # "  hello, world!  "
print(text.strip())             # "Hello, World!"
print(text.lstrip())            # "Hello, World!  "
print(text.rstrip())            # "  Hello, World!"
print(text.replace("World", "Python"))  # "  Hello, Python!  "

csv = "a,b,c,d"
print(csv.split(","))           # ['a', 'b', 'c', 'd']
items = ["a", "b", "c"]
print(",".join(items))          # "a,b,c"

s = "hello"
print(s.find("l"))              # 2  (first index)
print(s.find("z"))              # -1  (not found)
print(s.index("l"))             # 2  (raises ValueError if not found)
print(s.rfind("l"))             # 3  (last index)
print(s.count("l"))             # 2

print(s.startswith("he"))       # True
print(s.endswith("lo"))         # True
print("hello".isalpha())        # True
print("123".isdigit())          # True
print("abc123".isalnum())       # True
print("   ".isspace())          # True

# Slicing strings
s = "Python Programming"
print(s[0])                     # "P"
print(s[-1])                    # "g"
print(s[0:6])                   # "Python"
print(s[:6])                    # "Python"  (start defaults to 0)
print(s[7:])                    # "Programming"  (stop defaults to end)
print(s[::2])                   # "Pto rgamn"  (every 2nd char)
print(s[::-1])                  # "gnimmargorP nohtyP"  (reverse)

# len(), ord(), chr()
print(len(s))                   # 18
print(ord("A"))                 # 65
print(chr(65))                  # "A"

# in and not in
print("Python" in s)            # True
print("Java" not in s)          # True

# String immutability — this would FAIL
# s[0] = "J"  # TypeError: 'str' object does not support item assignment

# Must create a new string instead
s2 = "J" + s[1:]
print(s2)                       # "Jython Programming"


# 4. LISTS
# =========
# Easy definition: Lists are ordered, mutable sequences that can hold
# items of any type. They are created with square brackets.
# In-depth: Lists are dynamic arrays under the hood. They support
# indexing, slicing, and all sequence operations. Mutable means you
# can change elements, add, remove, and reorder items in place.

# Creating lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
from_range = list(range(5))     # [0, 1, 2, 3, 4]
from_string = list("hello")     # ['h', 'e', 'l', 'l', 'o']

# Indexing and slicing
nums = [10, 20, 30, 40, 50]
print(nums[0])                  # 10
print(nums[-1])                 # 50
print(nums[1:4])                # [20, 30, 40]
print(nums[:3])                 # [10, 20, 30]
print(nums[2:])                 # [30, 40, 50]
print(nums[::2])                # [10, 30, 50]
print(nums[::-1])               # [50, 40, 30, 20, 10]

# Lists are mutable — unlike tuples
nums[0] = 100
print(nums)                     # [100, 20, 30, 40, 50]
nums[1:3] = [200, 300]          # slice assignment
print(nums)                     # [100, 200, 300, 40, 50]

# List methods
lst = [3, 1, 4, 1, 5, 9, 2]
lst.append(6)                   # [3, 1, 4, 1, 5, 9, 2, 6]
lst.extend([10, 11])            # [3, 1, 4, 1, 5, 9, 2, 6, 10, 11]
lst.insert(2, 99)               # insert 99 at index 2
lst.remove(1)                   # remove first occurrence of 1
popped = lst.pop()              # removes and returns last item
popped_at = lst.pop(2)          # removes and returns item at index 2
lst.clear()                     # remove all items

lst = [3, 1, 4, 1, 5, 9, 2]
print(lst.index(4))             # 2  (first index of 4)
print(lst.count(1))             # 2

lst.sort()                      # in-place sort: [1, 1, 2, 3, 4, 5, 9]
lst.sort(reverse=True)          # [9, 5, 4, 3, 2, 1, 1]
lst.reverse()                   # in-place reverse

# sorted() and reversed() — return new objects, don't modify original
original = [3, 1, 4]
sorted_copy = sorted(original)  # [1, 3, 4]
reversed_copy = list(reversed(original))  # [4, 1, 3]

# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
matrix = [[x + y for x in range(3)] for y in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Nested list / matrix access
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(m[1][2])                  # 6

# List as stack (LIFO) — efficient with append/pop
stack = []
stack.append(1)                 # push
stack.append(2)
stack.append(3)
top = stack.pop()               # 3

# List as queue — use collections.deque for efficiency
from collections import deque
queue = deque(["a", "b", "c"])
queue.append("d")               # enqueue
front = queue.popleft()         # "a"  (O(1) instead of O(n) for list.pop(0))

# Shallow copy vs deep copy
import copy
original = [[1, 2], [3, 4]]

shallow = original.copy()        # or original[:]
shallow[0][0] = 99
print(original[0][0])            # 99  (shared inner list)

deep = copy.deepcopy(original)
deep[0][0] = 42
print(original[0][0])            # 99  (no change to original)

# len() on lists
print(len([1, 2, 3]))           # 3


# 5. TUPLES
# ==========
# Easy definition: Tuples are ordered, immutable sequences. Once created,
# their elements cannot be changed. They are created with parentheses.
# In-depth: Because tuples are immutable, they are hashable (can be used
# as dictionary keys). They use less memory than lists and are useful
# for fixed collections of related values.

# Creating tuples
empty = ()
single = (1,)                   # comma required — (1) is just int 1
numbers = (1, 2, 3)
mixed = (1, "hello", 3.14)
without_parens = 1, 2, 3       # comma syntax — also a tuple
from_list = tuple([1, 2, 3])   # tuple() constructor

# Immutability — once created, cannot be changed
t = (1, 2, 3)
# t[0] = 99  # TypeError: 'tuple' object does not support item assignment

# But if tuple contains mutable objects, those can be modified
t_mut = ([1, 2], [3, 4])
t_mut[0].append(99)            # ([1, 2, 99], [3, 4])  — tuple itself unchanged

# Indexing and slicing (same as lists)
print(numbers[0])               # 1
print(numbers[1:3])             # (2, 3)

# Tuple unpacking
point = (3, 4)
x, y = point
print(x, y)                     # 3 4

# Swapping via tuple packing/unpacking
a, b = 1, 2
a, b = b, a

# Extended unpacking (Python 3+)
first, *rest = (1, 2, 3, 4, 5)
print(first)                    # 1
print(rest)                     # [2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)
print(middle)                   # [2, 3, 4]

# When to use tuples
# - Dictionary keys (immutable, hashable)
# - Function return values returning multiple things
# - Fixed data that should not change
# - More memory-efficient than lists for fixed data

# Named tuples
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x)                      # 3
print(p.y)                      # 4
print(p[0])                     # 3  (also indexable)
x, y = p                        # unpackable

# Named tuple with defaults
Person = namedtuple("Person", ["name", "age", "city"])
p = Person("Alice", 30, "NYC")

# ._make() and ._asdict()
data = ["Bob", 25, "LA"]
p2 = Person._make(data)
print(p2._asdict())             # {'name': 'Bob', 'age': 25, 'city': 'LA'}

# One-element tuple gotcha
not_a_tuple = (1)               # int 1
actually_a_tuple = (1,)         # tuple with one element


# 6. DICTIONARIES
# ================
# Easy definition: Dictionaries map immutable keys to values. They are
# unordered (Python <3.7) or insertion-ordered (Python 3.7+).
# In-depth: Dictionaries are hash tables with O(1) average lookup,
# insertion, and deletion. Keys must be hashable (immutable types).
# Values can be any type.

# Creating dictionaries
empty = {}
ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])
from_kwargs = dict(name="Alice", age=30)
from_zip = dict(zip(["a", "b", "c"], [1, 2, 3]))

# Keys must be hashable
# Valid keys: int, float, str, tuple, frozenset, None, bool
# Invalid keys: list, dict, set, bytearray
# {[1, 2]: "value"}  # TypeError: unhashable type: 'list'

# Accessing values
print(ages["Alice"])            # 30
print(ages.get("Bob"))          # 25
print(ages.get("Nobody"))       # None
print(ages.get("Nobody", 0))    # 0  (default value)

# in operator checks keys
print("Alice" in ages)          # True
print("missing" in ages)        # False

# Methods
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())                 # dict_keys(['a', 'b', 'c'])
print(d.values())               # dict_values([1, 2, 3])
print(d.items())                # dict_items([('a', 1), ('b', 2), ('c', 3)])

d.update({"d": 4, "e": 5})     # add/update multiple keys
d["f"] = 6                     # add/update single key
popped = d.pop("a")            # removes and returns value
item = d.popitem()             # removes and returns (key, value) — LIFO in 3.7+
d.setdefault("g", 7)           # set only if key doesn't exist
d.setdefault("b", 99)          # no effect — "b" already exists

del d["c"]                     # delete a key
# d.clear()                      # remove all items

# Copying
d_copy = d.copy()
d_deepcopy = __import__("copy").deepcopy(d)

# Dictionary comprehensions
squares = {x: x**2 for x in range(10)}
even_squares = {x: x**2 for x in range(20) if x % 2 == 0}
swap = {v: k for k, v in {"a": 1, "b": 2}.items()}

# Merging dictionaries (Python 3.5+)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}          # {"a": 1, "b": 2, "c": 3, "d": 4}

# Merge operator (Python 3.9+)
merged2 = d1 | d2              # same result

# collections module
from collections import defaultdict, OrderedDict, Counter

# defaultdict — provides default for missing keys
dd = defaultdict(int)
dd["a"] += 1
dd["b"] += 2
print(dd["c"])                  # 0  (int() default)

dd_list = defaultdict(list)
dd_list["group1"].append("item1")

# OrderedDict — remembers insertion order (regular dict does too since 3.7)
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")            # move "a" to the end

# Counter — count hashable items
cnt = Counter("abracadabra")
print(cnt)                      # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(cnt.most_common(2))       # [('a', 5), ('b', 2)]

# Nested dictionaries
users = {
    "alice": {"age": 30, "city": "NYC"},
    "bob": {"age": 25, "city": "LA"},
}
print(users["alice"]["city"])   # "NYC"

# Iterating
for key, value in ages.items():
    print(f"{key}: {value}")


# 7. SETS
# ========
# Easy definition: Sets are unordered collections of unique, hashable
# elements. They are useful for membership testing and eliminating
# duplicates.
# In-depth: Sets are implemented as hash tables. Elements must be
# hashable (same requirement as dict keys). Sets support mathematical
# operations like union, intersection, difference.

# Creating sets
empty = set()                   # {} creates empty dict, not set
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} — duplicates removed
from_string = set("hello")      # {'h', 'e', 'l', 'o'} — unordered

# Set comprehensions
squares = {x**2 for x in range(10)}
evens = {x for x in range(20) if x % 2 == 0}

# Adding and removing
s = {1, 2, 3}
s.add(4)                        # {1, 2, 3, 4}
s.add(1)                        # no effect — 1 already present
s.remove(2)                     # {1, 3, 4} — KeyError if not found
s.discard(3)                    # {1, 4} — no error if not found
s.discard(999)                  # no error
popped = s.pop()                # removes and returns arbitrary element
s.clear()                       # remove all

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)                    # {1, 2, 3, 4, 5, 6, 7, 8}  union
print(a.union(b))               # same

print(a & b)                    # {4, 5}  intersection
print(a.intersection(b))        # same

print(a - b)                    # {1, 2, 3}  difference (in a but not b)
print(a.difference(b))          # same

print(a ^ b)                    # {1, 2, 3, 6, 7, 8}  symmetric difference
print(a.symmetric_difference(b))  # same

# Comparison operations
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print(x.issubset(y))            # True  — all elements of x are in y
print(y.issuperset(x))          # True
print(x.isdisjoint({4, 5, 6}))   # False  — x contains 4? No, but check

# Frozenset — immutable, hashable set
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
d = {fs: "frozenset as key"}    # valid — frozensets are hashable


# 8. CONTROL FLOW
# ================
# Easy definition: Control flow structures let you execute code
# conditionally with if/elif/else or match patterns.
# In-depth: Python uses indentation (4 spaces) to define blocks.
# No braces or begin/end keywords. The condition is evaluated for
# truthiness, not just boolean True.

# if, elif, else
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Truthy and falsy values
# Falsy: None, False, 0, 0.0, 0j, "" (empty string), [] (empty list),
#        {} (empty dict), set() (empty set), range(0)
# Truthy: everything else

if []:                          # False — empty list is falsy
    print("won't run")

if [1, 2]:                     # True — non-empty list is truthy
    print("will run")

# Comparison operators
print(5 == 5)                   # True  equal
print(5 != 6)                   # True  not equal
print(5 < 6)                    # True  less than
print(5 > 4)                    # True  greater than
print(5 <= 5)                   # True  less than or equal
print(5 >= 6)                   # False greater than or equal

# Chained comparisons
print(1 < 5 < 10)              # True  (equivalent to 1 < 5 and 5 < 10)
print(1 < 5 > 3)               # True

# Logical operators: and, or, not
print(True and False)          # False
print(True or False)           # True
print(not True)                # False

# Short-circuit evaluation
# and returns first falsy value or last value
print(0 and 42)                # 0  (short-circuits on 0)
print(1 and 42)                # 42  (both truthy, returns last)

# or returns first truthy value or last value
print(0 or 42)                 # 42
print(42 or 0)                 # 42  (short-circuits)

# Common pattern — provide default
name = input("name: ") or "Guest"

# Ternary/conditional expression
status = "adult" if age >= 18 else "minor"

# match/case (Python 3.10+) — structural pattern matching
def describe(value):
    match value:
        case 0:
            return "zero"
        case 1 | 2 | 3:
            return "small"
        case int() as n if n > 100:
            return "big number"
        case str() as s:
            return f"string: {s}"
        case [x, y]:
            return f"two-element list: {x}, {y}"
        case {"key": value}:
            return f"dict with key: {value}"
        case _:
            return "something else"


# 9. LOOPS
# =========
# Easy definition: Loops let you iterate over sequences (for) or repeat
# while a condition is true (while).
# In-depth: Python's for loop is a for-each — it iterates over elements
# of any iterable. The while loop runs as long as its condition is
# truthy. Both support break, continue, and else clauses.

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# range()
for i in range(5):              # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):           # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):       # 0, 2, 4, 6, 8
    print(i)

for i in range(10, 0, -1):      # 10, 9, 8, ..., 1
    print(i)

# enumerate() — get index and value
colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(f"{i}: {color}")

for i, color in enumerate(colors, start=1):
    print(f"{i}: {color}")

# zip() — iterate multiple sequences in parallel
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} and lives in {city}")

# zip() with unequal lengths — stops at shortest
for a, b in zip([1, 2, 3], [10, 20]):
    print(a, b)                 # (1, 10), (2, 20)  — 3 is skipped

# zip longest — from itertools
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], [10, 20], fillvalue=0):
    print(a, b)                 # (1, 10), (2, 20), (3, 0)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    response = input("quit? (y/n): ")
    if response == "y":
        break

# break — exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)                    # 0, 1, 2, 3, 4

# continue — skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)                    # 1, 3, 5, 7, 9

# pass — do nothing (placeholder)
for i in range(10):
    if i == 5:
        pass                    # placeholder for future code
    print(i)

# else clause on loops — runs only if loop completed without break
for i in range(5):
    print(i)
else:
    print("Loop completed normally")  # runs

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Won't run — loop was broken")

# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# Iterating over dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}
for key in person:              # keys by default
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

for value in person.values():
    print(value)

# reversed() — iterate backwards
for i in reversed(range(10)):
    print(i)


# 10. FUNCTIONS
# ==============
# Easy definition: Functions are reusable blocks of code defined with
# def. They can accept arguments and return values.
# In-depth: Functions are first-class objects — they can be assigned
# to variables, passed as arguments, and returned from other functions.
# Python supports positional, keyword, default, *args, **kwargs,
# keyword-only, and positional-only parameters.

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))           # "Hello, Alice!"

# Multiple parameters and return values
def add(a, b):
    return a + b

def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # returns a tuple

q, r = divide(17, 5)           # unpacking: q=3, r=2

# Default parameter values
def power(base, exp=2):
    return base ** exp

print(power(5))                 # 25  (uses default exp=2)
print(power(5, 3))              # 125

# Mutable default gotcha!
def add_item(item, lst=[]):     # BAD: list is created once, shared
    lst.append(item)
    return lst

print(add_item(1))              # [1]
print(add_item(2))              # [1, 2]  — not [2]!

# Correct pattern — use None
def add_item_correct(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Positional vs keyword arguments
def describe(name, age, city):
    print(f"{name}, {age}, {city}")

describe("Alice", 30, "NYC")    # positional
describe(age=30, name="Alice", city="NYC")  # keyword (order doesn't matter)
describe("Alice", city="NYC", age=30)  # mixed (positional first)

# *args — variable positional arguments
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15
# args inside the function is a tuple: (1, 2, 3, 4, 5)

# **kwargs — variable keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="NYC")
# kwargs inside is a dict: {"name": "Alice", "age": 30, "city": "NYC"}

# Combining parameter types
def func(a, b, *args, c=10, **kwargs):
    pass  # positional: a, b / *args extra positional / c keyword-default / **kwargs extra keyword

# Keyword-only arguments (after *)
def func_kw_only(a, b, *, verbose=False, debug=False):
    if verbose:
        print(f"a={a}, b={b}")
    return a + b

# verbose and debug must be passed as keywords
func_kw_only(1, 2, verbose=True)

# Positional-only arguments (before /) — Python 3.8+
def func_pos_only(a, b, /, c, d):
    pass  # a and b are positional-only; c and d are positional or keyword

# func_pos_only(1, 2, 3, 4)       # OK
# func_pos_only(a=1, b=2, c=3, d=4)  # ERROR: a and b are positional-only

# Lambda — anonymous function
square = lambda x: x**2
print(square(5))                # 25

# Lambda with multiple args
add = lambda a, b: a + b

# Lambda with sort
pairs = [(1, "one"), (3, "three"), (2, "two")]
pairs.sort(key=lambda pair: pair[0])

# Nested functions
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))              # 8

# Closures — inner function remembers outer scope
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter_a = make_counter()
print(counter_a())              # 1
print(counter_a())              # 2

counter_b = make_counter()
print(counter_b())              # 1  (independent counter)

# Docstrings
def multiply(a, b):
    """Multiply two numbers and return the result.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Product of a and b
    """
    return a * b

# Annotations/type hints (also see section 21)
def add_typed(x: int, y: int) -> int:
    return x + y


# 11. SCOPE — LEGB RULE
# ======================
# Easy definition: Scope determines where a variable name is visible.
# Python resolves names using the LEGB order.
# In-depth: LEGB stands for Local, Enclosing, Global, Built-in. Python
# searches scopes in this order when looking up a variable name.
# The global keyword lets you modify module-level variables inside
# functions. The nonlocal keyword lets you modify enclosing scope
# variables in nested functions.

# LEGB resolution order
# L — Local: variables defined inside the current function
# E — Enclosing: variables in outer (nested) functions
# G — Global: variables at the module level
# B — Built-in: Python's built-in names (print, len, range, etc.)

x = "global x"                  # Global scope

def outer():
    x = "outer x"               # Enclosing scope (for inner)
    y = "outer y"

    def inner():
        x = "inner x"           # Local scope
        print(x)                # "inner x"  — local found first
        print(y)                # "outer y"  — from enclosing scope

    inner()
    print(x)                    # "outer x"

outer()
print(x)                        # "global x"

# global keyword
count = 0

def increment():
    global count                # without this, count would be local
    count += 1

increment()
print(count)                    # 1

# nonlocal keyword
def make_accumulator():
    total = 0
    def add(n):
        nonlocal total          # without this, 'total += n' creates local
        total += n
        return total
    return add

acc = make_accumulator()
print(acc(5))                   # 5
print(acc(3))                   # 8

# Built-in scope example
# print, len, range, etc. are in built-in scope
# You can shadow them (but shouldn't)
# len = "shadow"  # now len refers to the string, not the built-in


# 12. COMPREHENSIONS & GENERATORS
# ================================
# Easy definition: Comprehensions provide a concise way to create
# collections. Generators lazily produce values one at a time.
# In-depth: List/dict/set comprehensions are syntactic sugar for
# for-loops with append. Generator expressions and generator functions
# produce items on demand, using far less memory for large sequences.

# List comprehension
squares = [x**2 for x in range(10)]
# Same as:
# squares = []
# for x in range(10):
#     squares.append(x**2)

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested loops
matrix = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# if-else in comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]

# Dict comprehension
square_dict = {x: x**2 for x in range(10)}
even_squares = {x: x**2 for x in range(20) if x % 2 == 0}
inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "hi", "there"]}

# Generator expression — memory efficient
# Uses () instead of []
gen = (x**2 for x in range(1000000))
# No list is created — values computed one at a time

print(next(gen))                # 0
print(next(gen))                # 1
# Can be used in functions that accept iterables
total = sum(x**2 for x in range(1000))  # note: extra () not needed

# Generator function with yield
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))                # 0
print(next(fib))                # 1
print(next(fib))                # 1
print(next(fib))                # 2

# Generator with termination
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)                    # 5, 4, 3, 2, 1

# yield from — delegate to sub-generator
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
print(list(flatten(nested)))    # [1, 2, 3, 4, 5, 6]

# Generator.send(), .throw(), .close()
def coroutine():
    value = yield "ready"
    while True:
        value = yield f"received: {value}"

c = coroutine()
print(next(c))                  # "ready"  (initialize)
print(c.send("hello"))          # "received: hello"
print(c.send(42))               # "received: 42"
c.close()                       # terminates generator

# Memory efficiency comparison
import sys
list_comp = [x for x in range(10000)]
gen_expr = (x for x in range(10000))
print(sys.getsizeof(list_comp)) # large (list)
print(sys.getsizeof(gen_expr))  # tiny (generator object)


# 13. MODULES & PACKAGES
# =======================
# Easy definition: Modules are .py files containing Python code.
# Packages are directories of modules with an __init__.py.
# In-depth: The import system searches sys.path for modules.
# Each module is executed once and cached in sys.modules.
# The __name__ == "__main__" pattern lets files be both imported and
# run directly.

# Import styles
import math                    # import the whole module
from math import sqrt, pi     # import specific names
import math as m               # import with alias
from math import sqrt as square_root  # alias individual name
from math import *             # import all public names (discouraged)

# __name__ == "__main__" pattern
# Put this at the bottom of every module meant to be run directly:
# if __name__ == "__main__":
#     main()

# When run directly: __name__ == "__main__"
# When imported: __name__ == module filename (without .py)

# Creating modules — just save a .py file
# my_module.py:
#   def greet():
#       return "Hello from my_module!"
#   if __name__ == "__main__":
#       print(greet())
#
# Then: from my_module import greet

# Packages — directory with __init__.py
# my_package/
#   __init__.py      # can be empty; runs when package is imported
#   module_a.py
#   module_b.py
#
# from my_package import module_a
# from my_package.module_b import some_function

# sys.path — where Python looks for modules
import sys
print(sys.path)                 # list of directories Python searches

# Adding custom path
# sys.path.append("/path/to/my_modules")

# PYTHONPATH environment variable
# $ export PYTHONPATH=/path/to/modules:$PYTHONPATH

# pip — package installer
# $ pip install requests
# $ pip install numpy==1.21.0
# $ pip install "pandas>=1.3"
# $ pip uninstall requests
# $ pip list  # list installed packages
# $ pip freeze  # list installed packages with versions
# $ pip freeze > requirements.txt
# $ pip install -r requirements.txt

# dir() and help()
print(dir(math))                # list all names in math module
# help(math.sqrt)               # show documentation (opens pager)


# 14. FILE I/O
# =============
# Easy definition: File I/O lets you read from and write to files on
# disk. The built-in open() function is the primary interface.
# In-depth: Always use the with statement (context manager) for file
# operations — it ensures the file is properly closed even if an error
# occurs. Files can be opened in text mode (default) or binary mode.

# Opening and reading files
file = open("example.txt", "r")  # open for reading
content = file.read()            # read entire file as string
file.close()                     # always close! (but with is better)

# Using context manager (preferred)
with open("example.txt", "r") as f:
    content = f.read()          # auto-closed after block

# Read modes
with open("example.txt", "r") as f:
    entire = f.read()           # whole file as one string
    f.seek(0)                   # go back to beginning
    line = f.readline()         # read one line
    f.seek(0)
    lines = f.readlines()       # list of all lines

# Iterating over lines (memory efficient)
with open("large_file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Writing to files
with open("output.txt", "w") as f:
    f.write("Hello, World!\\n")
    f.write("Second line\\n")

with open("output.txt", "a") as f:  # append mode
    f.write("Third line (appended)\\n")

# Write multiple lines
lines = ["line 1", "line 2", "line 3"]
with open("output.txt", "w") as f:
    f.writelines(line + "\\n" for line in lines)

# File modes
# "r"  — read (default)
# "w"  — write (overwrites)
# "a"  — append
# "r+" — read and write (no truncate)
# "w+" — read and write (truncates)
# "a+" — read and append
# "x"  — exclusive creation (fails if file exists)
# "b"  — binary mode (combine: "rb", "wb")
# "t"  — text mode (default, combine: "rt", "wt")

# Binary mode
with open("image.jpg", "rb") as f:
    data = f.read()
    print(len(data))            # number of bytes

with open("copy.jpg", "wb") as f:
    f.write(data)

# File encoding
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Unicode text: é, ñ, ü, 你好")

# seek() and tell()
with open("example.txt", "r") as f:
    print(f.tell())             # 0 (current position)
    f.read(10)                  # read 10 characters
    print(f.tell())             # 10
    f.seek(0)                   # back to beginning
    f.seek(10)                  # skip to byte/char 10
    f.seek(-5, 1)               # 5 back from current position
    f.seek(0, 2)                # seek to end (for getting file size)

# os.path — path manipulation (legacy)
import os
print(os.path.exists("file.txt"))
print(os.path.isfile("file.txt"))
print(os.path.isdir("mydir"))
print(os.path.join("dir", "subdir", "file.txt"))

# pathlib — modern path handling
from pathlib import Path
p = Path("dir/subdir/file.txt")
print(p.parent)                 # dir/subdir
print(p.name)                   # file.txt
print(p.stem)                   # file
print(p.suffix)                 # .txt
print(p.exists())
print(p.is_file())
print(p.is_dir())

# Path operations
Path("new_dir").mkdir(exist_ok=True)
Path("new_dir/new_file.txt").write_text("hello")
text = Path("new_dir/new_file.txt").read_text()
Path("new_dir/new_file.txt").rename("new_dir/renamed.txt")
# Path("new_dir/renamed.txt").unlink()  # delete file

# tempfile — temporary files
import tempfile
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=True) as f:
    f.write("temporary content")
    print(f.name)               # path to temp file
    # file is auto-deleted when context exits

# temp directory
with tempfile.TemporaryDirectory() as tmpdir:
    path = Path(tmpdir) / "test.txt"
    path.write_text("hello")
    # dir is auto-deleted when context exits

# shutil — high-level file operations
import shutil
# shutil.copy("source.txt", "dest.txt")         # copy file
# shutil.copytree("source_dir", "dest_dir")     # copy directory
# shutil.move("source.txt", "dest/location/")   # move file
# shutil.rmtree("dir_to_delete")                # delete directory (careful!)


# 15. EXCEPTION HANDLING
# =======================
# Easy definition: Exceptions handle runtime errors gracefully without
# crashing the program. Use try/except blocks.
# In-depth: Python uses exceptions for error handling — both built-in
# errors and custom ones. The try block runs code that might fail.
# except catches specific exceptions. else runs if no exception.
# finally always runs (for cleanup).

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Catching specific exception types
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Number can't be zero!")

# Multiple exceptions in one except
try:
    val = [1, 2, 3][10]
except (IndexError, KeyError, TypeError) as e:
    print(f"Caught: {e}")

# Catching exception object
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")        # "division by zero"
    print(f"Type: {type(e)}")   # <class 'ZeroDivisionError'>

# try/except/else
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Zero not allowed")
else:
    print(f"Result: {result}")  # runs only if no exception

# finally — always runs
try:
    f = open("file.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    f.close()                   # always executed

# raise — manually raise an exception
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

# raise from — chain exceptions
try:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("Computation failed") from e
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")

# Custom exception classes
class InsufficientFundsError(Exception):
    """Raised when account balance is insufficient."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.missing = amount - balance
        super().__init__(f"Need {self.missing} more")

try:
    raise InsufficientFundsError(100, 150)
except InsufficientFundsError as e:
    print(e.missing)            # 50

# Common built-in exceptions
# ValueError     — invalid value (int("abc"))
# TypeError      — wrong type (len(5))
# IndexError     — list index out of range
# KeyError       — dict key not found
# AttributeError — object has no attribute
# FileNotFoundError — file doesn't exist
# ZeroDivisionError — division by zero
# ImportError    — import failed
# RuntimeError   — general runtime error
# StopIteration  — end of iterator (next() on exhausted iterator)
# NameError      — variable not defined
# SyntaxError    — invalid Python syntax

# assert — debugging assertion
def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b

# assert can be disabled with -O flag: $ python -O script.py

# try/finally for cleanup (no except)
# Useful when you need cleanup but let exception propagate
def read_file(path):
    f = open(path, "r")
    try:
        return f.read()
    finally:
        f.close()               # file closed even if read() fails


# 16. OOP — CLASSES & OBJECTS
# ============================
# Easy definition: Classes are blueprints for creating objects (instances).
# They bundle data (attributes) and behavior (methods).
# In-depth: Everything in Python is an object. The __init__ method
# initializes new instances. self refers to the instance itself.
# Class variables are shared across instances; instance variables
# are unique to each instance.

# Basic class
class Dog:
    species = "Canis familiaris"  # class variable (shared)

    def __init__(self, name, age):  # constructor
        self.name = name            # instance variable
        self.age = age

    def bark(self):                 # instance method
        return f"{self.name} says Woof!"

    def __str__(self):              # string representation
        return f"{self.name} ({self.age})"

# Creating objects (instances)
buddy = Dog("Buddy", 5)
max_dog = Dog("Max", 3)

print(buddy.name)                   # "Buddy"
print(buddy.bark())                 # "Buddy says Woof!"
print(Dog.species)                  # "Canis familiaris" (class variable)
print(buddy.species)                # also accessible via instance

# Class variables are shared
Dog.species = "Canis lupus"
print(buddy.species)                # "Canis lupus"

# Instance variables are separate
buddy.age = 6
print(buddy.age)                    # 6
print(max_dog.age)                  # 3

# Instance methods, class methods, static methods
class MyClass:
    class_var = 0

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        """Regular method — receives instance as first arg."""
        return f"instance method: {self.value}"

    @classmethod
    def class_method(cls):
        """Receives class (not instance) as first arg."""
        cls.class_var += 1
        return f"class method: {cls.class_var}"

    @staticmethod
    def static_method(x, y):
        """No self or cls — just a function in the class namespace."""
        return x + y

obj = MyClass(42)
print(obj.instance_method())        # "instance method: 42"
print(MyClass.class_method())       # "class method: 1"
print(MyClass.static_method(3, 4))  # 7

# @property decorator — computed attributes
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

c = Circle(5)
print(c.radius)                     # 5  (uses @property getter)
c.radius = 10                       # uses @radius.setter
print(c.area)                       # 314.159...  (computed property)
# c.area = 100                      # AttributeError — no setter

# Public, protected, private naming conventions
# No actual access control — all are conventions
class Person:
    def __init__(self, name, age, ssn):
        self.name = name             # public
        self._age = age              # "protected" — internal use
        self.__ssn = ssn             # "private" — name mangling

    def display(self):
        print(f"{self.name}, {self._age}")
        # print(self.__ssn)           # OK inside class

p = Person("Alice", 30, "123-45-6789")
print(p.name)                        # "Alice"
print(p._age)                        # "protected" but accessible
# print(p.__ssn)                     # AttributeError — name mangled
print(p._Person__ssn)                # "123-45-6789" (mangled name)

# __slots__ — memory optimization
class Point:
    __slots__ = ("x", "y")          # only these attributes allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
# p.z = 5  # AttributeError: 'Point' has no attribute 'z'

# Introspection utilities
class Sample:
    def __init__(self):
        self.a = 1
        self.b = 2

s = Sample()
print(dir(s))                       # list of attributes and methods
print(hasattr(s, "a"))              # True
print(getattr(s, "a"))              # 1
print(getattr(s, "c", "default"))   # "default" (not found)
setattr(s, "d", 4)                  # s.d = 4
print(isinstance(s, Sample))        # True
print(issubclass(Sample, object))   # True


# 17. INHERITANCE
# ================
# Easy definition: Inheritance lets a class (child) reuse attributes
# and methods from another class (parent).
# In-depth: Python supports single and multiple inheritance.
# super() calls the parent class's methods. MRO (Method Resolution
# Order) determines which parent's method is called in diamond
# hierarchies. Abstract base classes enforce interface contracts.

# Basic inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement")

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())

# super() — call parent method
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # calls Rectangle.__init__

    def __str__(self):
        return f"Square(side={self.width})"

sq = Square(5)
print(sq.area())                    # 25

# Multiple inheritance
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

d = Duck()
print(d.fly())                      # "Flying"  (from Flyer)
print(d.swim())                     # "Swimming" (from Swimmer)

# MRO — Method Resolution Order
# Determines which method is called in diamond inheritance
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Flyer'>,
#  <class '__main__.Swimmer'>, <class 'object'>)

# Diamond inheritance — MRO prevents double calls
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B -> " + super().method()

class C(A):
    def method(self):
        return "C -> " + super().method()

class D(B, C):
    def method(self):
        return "D -> " + super().method()

d = D()
print(d.method())  # "D -> B -> C -> A"
# MRO: D -> B -> C -> A (Python uses C3 linearization)

# Abstract base classes (ABC)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Cannot instantiate ABC directly:
# s = Shape()  # TypeError: Can't instantiate abstract class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Mixins — provide specific behavior
class LogMixin:
    def log(self, message):
        print(f"[{type(self).__name__}] {message}")

class JsonSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(LogMixin, JsonSerializableMixin):
    def __init__(self, name):
        self.name = name
        self.log(f"Created user: {name}")

u = User("Alice")
print(u.to_json())  # {"name": "Alice"}


# 18. MAGIC METHODS (DUNDER METHODS)
# ===================================
# Easy definition: Magic methods are special methods with double
# underscores that define object behavior for built-in operations.
# In-depth: Dunder methods allow custom classes to work with Python's
# built-in functions and operators (+, len(), str(), ==, etc.).
# They are rarely called directly — Python calls them implicitly.

# __str__ and __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        """Unambiguous representation — for developers."""
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        """Readable representation — for users."""
        return f"{self.name} ({self.age})"

p = Person("Alice", 30)
print(repr(p))                      # Person('Alice', 30)
print(str(p))                       # Alice (30)
print(p)                            # same as str(p)

# __len__, __getitem__, __setitem__, __delitem__, __contains__
class CustomList:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        return repr(self._items)

cl = CustomList([1, 2, 3, 4, 5])
print(len(cl))                      # 5  (calls __len__)
print(cl[2])                        # 3  (calls __getitem__)
cl[2] = 99                          # (calls __setitem__)
print(99 in cl)                     # True  (calls __contains__)
del cl[2]                           # (calls __delitem__)

# __iter__ and __next__ — make objects iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.n = self.start + 1
        return self

    def __next__(self):
        self.n -= 1
        if self.n < 0:
            raise StopIteration
        return self.n

for i in Countdown(5):
    print(i)                        # 5, 4, 3, 2, 1

# __call__ — make objects callable like functions
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)
print(double(5))                    # 10
print(triple(5))                    # 15

# __enter__ and __exit__ — context managers
class ManagedFile:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        # Return True to suppress exceptions, False to propagate
        return False

with ManagedFile("test.txt", "w") as f:
    f.write("Hello from custom context manager!")

# __eq__, __ne__, __lt__, __le__, __gt__, __ge__ — comparisons
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __hash__(self):
        return hash(self.amount)

    def __repr__(self):
        return f"Money({self.amount})"

m1 = Money(100)
m2 = Money(200)
print(m1 == m2)                     # False
print(m1 < m2)                      # True
print(m1 <= m2)                     # True

# with total_ordering decorator — fill in remaining comparisons
from functools import total_ordering

@total_ordering
class Price:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    # remaining (<=, >, >=) are derived from == and <

# __add__ and other arithmetic operators
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):     # scalar * vector
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)                      # Vector(4, 6)
print(v1 - v2)                      # Vector(-2, -2)
print(v1 * 3)                       # Vector(3, 6)
print(3 * v1)                       # Vector(3, 6) (via __rmul__)

# __bool__ — defines truthiness
class MyList:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0

print(bool(MyList([1, 2, 3])))      # True
print(bool(MyList([])))              # False

# __new__ vs __init__ — object creation lifecycle
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

a = Singleton(1)
b = Singleton(2)
print(a is b)                       # True (same instance)
print(a.value)                      # 2  (overwritten by second init)

# __del__ — destructor (called when object is garbage collected)
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Acquired: {name}")

    def __del__(self):
        print(f"Released: {name}")


# 19. DECORATORS
# ===============
# Easy definition: Decorators are functions that modify the behavior
# of other functions or classes using the @ syntax.
# In-depth: A decorator is a callable that takes a function as argument
# and returns a new function. They're commonly used for logging,
# timing, access control, caching, and registration.

# Basic decorator — function that wraps another function
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before the function call
# Hello!
# After the function call

# Decorator with arguments — preserve original function signature
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# Calling add with (3, 5), {}
# add returned 8

# Preserving metadata with @wraps
from functools import wraps

def logger_better(func):
    @wraps(func)                    # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger_better
def greet(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

print(greet.__name__)               # "greet"  (not "wrapper")
print(greet.__doc__)                # "Say hello to someone."

# Decorators with arguments
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(message):
    print(message)

say("Hello!")                       # prints "Hello!" 3 times

# Multiple decorators — applied bottom up
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())                      # <b><i>Hello</i></b>
# Equivalent to: bold(italic(greet))

# Class decorators
def add_repr(cls):
    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p)                            # Point(x=3, y=4)

# Class-based decorators (using __call__)
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def hello():
    print("Hi!")

hello()                             # Call 1 of hello
hello()                             # Call 2 of hello

# Built-in decorators
# @property — already covered in OOP section
# @staticmethod — already covered
# @classmethod — already covered


# 20. BUILT-IN FUNCTIONS (IMPORTANT ONES)
# =========================================
# Easy definition: Python has many built-in functions available
# without importing anything. These are always ready to use.
# In-depth: Built-in functions cover type conversion, iteration,
# math, I/O, introspection, and more. They are loaded from builtins
# module but always available by default.

# map() — apply function to every item in iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# With multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
# [11, 22, 33]

# filter() — keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, range(10)))
# [0, 2, 4, 6, 8]

# reduce() — from functools, accumulate value
from functools import reduce
total = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])
# 15

product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
# 120

# sorted() — return sorted list copy
print(sorted([3, 1, 4, 1, 5, 9, 2]))
# [1, 1, 2, 3, 4, 5, 9]

# With key function
words = ["apple", "kiwi", "banana", "cherry"]
print(sorted(words, key=len))       # ["kiwi", "apple", "banana", "cherry"]
print(sorted(words, key=len, reverse=True))
# ["banana", "cherry", "apple", "kiwi"]

# Sort by last character
print(sorted(words, key=lambda s: s[-1]))
# ["banana", "apple", "cherry", "kiwi"]

# all() and any()
print(all([True, True, False]))     # False
print(any([False, False, True]))    # True

# With generators — short-circuit evaluation
print(all(x > 0 for x in [1, 2, 3]))    # True
print(any(x < 0 for x in [1, 2, -3]))   # True

# isinstance()
print(isinstance(42, int))              # True
print(isinstance("hello", (str, list)))  # True  (checks against tuple)

# hasattr(), getattr(), setattr() — covered in OOP section

# len()
print(len("hello"))                     # 5
print(len([1, 2, 3]))                   # 3
print(len({"a": 1, "b": 2}))            # 2

# sum(), min(), max()
print(sum([1, 2, 3, 4, 5]))             # 15
print(sum([1, 2, 3], start=10))         # 16  (start value)
print(min(3, 1, 4, 1, 5))              # 1
print(max("hello"))                     # "o"  (lexicographic)

# abs(), round()
print(abs(-5))                          # 5
print(round(3.14159, 3))                # 3.142

# range()
r = range(5)                            # 0, 1, 2, 3, 4
r = range(2, 8)                         # 2, 3, 4, 5, 6, 7
r = range(0, 10, 2)                     # 0, 2, 4, 6, 8

# iter() and next()
it = iter([1, 2, 3])
print(next(it))                         # 1
print(next(it))                         # 2
print(next(it))                         # 3
# print(next(it))                       # StopIteration

# type() and id()
print(type(42))                         # <class 'int'>
print(id("hello"))                      # memory address (int)

# dir() — list attributes
print(dir([]))                          # all list methods

# vars() — __dict__ of an object
class Demo:
    def __init__(self):
        self.x = 10
        self.y = 20

d = Demo()
print(vars(d))                          # {"x": 10, "y": 20}

# repr() and str()
import datetime
now = datetime.datetime.now()
print(repr(now))                        # "datetime.datetime(2026, 6, 27, ...)"
print(str(now))                         # "2026-06-27 14:30:00..."

# eval() and exec()
result = eval("2 + 3 * 4")               # 14
# exec("x = 10")                         # executes as code

# open(), print(), input() — covered in I/O sections

# zip(), reversed(), slice()
s = slice(1, 5, 2)
print([0, 1, 2, 3, 4, 5][s])            # [1, 3]

# staticmethod(), classmethod(), property() — covered in OOP

# globals() and locals()
print(list(globals().keys())[:3])        # global namespace keys
print(locals())                          # local namespace

# chr(), ord()
print(ord("A"))                         # 65
print(chr(65))                          # "A"

# bin(), hex(), oct(), format()
print(bin(42))                          # "0b101010"
print(hex(255))                         # "0xff"
print(oct(8))                           # "0o10"
print(format(255, "b"))                 # "11111111"  (binary without prefix)
print(format(255, "x"))                 # "ff"
print(format(255, "04x"))               # "00ff"
print(format(0.25, ".2%"))              # "25.00%"


# 21. TYPE HINTS
# ===============
# Easy definition: Type hints annotate variables, function parameters,
# and return values with expected types. They are not enforced at
# runtime but help with tooling and documentation.
# In-depth: Type hints are defined in PEP 484. They are ignored at
# runtime but checked by static type checkers (mypy, pyright).
# The typing module provides complex types like List, Dict, Optional.

# Basic type hints
name: str = "Alice"
age: int = 30
height: float = 5.7
active: bool = True

# Function parameter and return type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(x: int, y: int) -> int:
    return x + y

def nothing(x: int, y: int) -> None:
    print(x + y)

# Default values with hints
def power(base: float, exp: int = 2) -> float:
    return base ** exp

# Complex types (from typing module)
from typing import List, Dict, Tuple, Set, Optional, Any, Union, Callable

# List of integers
def process_numbers(nums: List[int]) -> List[int]:
    return [x * 2 for x in nums]

# Dictionary mapping string to int
def get_counts(items: List[str]) -> Dict[str, int]:
    return {item: items.count(item) for item in set(items)}

# Tuple with specific types
def get_point() -> Tuple[float, float]:
    return (3.0, 4.0)

# Tuple with variable length — homogenous
def get_coords() -> Tuple[float, ...]:
    return (1.0, 2.0, 3.0)

# Set
def unique(items: List[int]) -> Set[int]:
    return set(items)

# Optional — could be None
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

# Optional is shorthand for Union[str, None]
def find_user2(user_id: int) -> str | None:
    # Python 3.10+ inline union syntax
    if user_id == 1:
        return "Alice"
    return None

# Union — multiple possible types
def parse_number(value: str) -> Union[int, float]:
    if "." in value:
        return float(value)
    return int(value)

# Python 3.10+ inline union syntax
def parse_number2(value: str) -> int | float:
    if "." in value:
        return float(value)
    return int(value)

# Any — any type allowed
def log(value: Any) -> None:
    print(value)

# Callable — function type
# Callable[[Param1Type, Param2Type], ReturnType]
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply(lambda x, y: x + y, 3, 5))  # 8

# Type — the class itself, not an instance
def create_instance(cls: type, *args: Any) -> Any:
    return cls(*args)

# Forward references (class that hasn't been defined yet)
class TreeNode:
    def __init__(self, value: int, left: Optional["TreeNode"] = None):
        self.value = value
        self.left = left

# from __future__ import annotations — makes all hints strings
# (evaluated lazily, no forward reference needed)
from __future__ import annotations

# Now forward references work without quotes
# (implicitly all annotations are strings)

# Self type (Python 3.11+)
# from typing import Self
# class MyClass:
#     def copy(self) -> Self:
#         ...

# TypeVar — generic types
from typing import TypeVar

T = TypeVar("T")

def first(items: List[T]) -> T:
    return items[0]

# Constrained TypeVar
NumT = TypeVar("NumT", int, float)

def double(value: NumT) -> NumT:
    return value * 2

# TypedDict — typed dictionary with specific keys
from typing import TypedDict

class PersonDict(TypedDict):
    name: str
    age: int
    city: str

# pd: PersonDict = {"name": "Alice", "age": 30, "city": "NYC"}


# 22. INPUT & OUTPUT
# ===================
# Easy definition: input() reads user input as a string. print()
# outputs to the console with customizable formatting.
# In-depth: input() always returns a string (convert with int(),
# float() as needed). print() accepts sep, end, and file parameters.

# User input
name = input("Enter your name: ")   # returns string
age_str = input("Enter your age: ")
age = int(age_str)                  # convert to int

# input() always returns a string
value = input("Enter a number: ")
print(type(value))                  # <class 'str'>

# print() options
print("Hello", "World")             # "Hello World"  (default sep=" ")
print("Hello", "World", sep="-")    # "Hello-World"
print("Hello", end="!!!\\n")         # "Hello!!!"  (override newline)
print("Loading", end="")
print(".", end="")
print(".")                          # "Loading.."

# print to a file
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)   # writes to file instead of console

# print with formatting (f-strings)
name = "Alice"
age = 30
print(f"{name:10} is {age:3d} years old")
# "Alice      is  30 years old"

# Pretty printing
import pprint
data = {
    "name": "Alice",
    "age": 30,
    "pets": ["dog", "cat"],
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": 10001,
    },
}
pprint.pprint(data)                 # formatted, sorted keys
# {'address': {'city': 'NYC', 'street': '123 Main St', 'zip': 10001},
#  'age': 30,
#  'name': 'Alice',
#  'pets': ['dog', 'cat']}

# pformat — get pretty string without printing
formatted = pprint.pformat(data)


# 23. JSON & DATA SERIALIZATION
# ==============================
# Easy definition: JSON (JavaScript Object Notation) is a lightweight
# data interchange format. Python's json module handles encoding
# (serialization) and decoding (deserialization).
# In-depth: json.dumps() converts Python objects to JSON strings.
# json.loads() parses JSON strings to Python objects. Custom objects
# need a custom encoder/decoder.

import json

# Python to JSON (serialization)
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "scores": [95, 87, 92],
    "address": None,
}

json_str = json.dumps(data)
print(json_str)
# {"name": "Alice", "age": 30, "is_student": false, "scores": [95, 87, 92], "address": null}

# Pretty-print JSON
json_pretty = json.dumps(data, indent=2)
print(json_pretty)
# {
#   "name": "Alice",
#   "age": 30,
#   "is_student": false,
#   ...
# }

# Sorting keys
json_sorted = json.dumps(data, sort_keys=True, indent=2)

# JSON to Python (deserialization)
json_input = '{"name": "Bob", "age": 25, "active": true}'
parsed = json.loads(json_input)
print(parsed["name"])               # "Bob"
print(parsed["age"])                # 25

# Type mapping: JSON -> Python
# object      -> dict
# array       -> list
# string      -> str
# number      -> int or float
# boolean     -> bool
# null        -> None

# File I/O with JSON
# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json", "r") as f:
    loaded = json.load(f)

# Custom serialization
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Default approach — convert to dict first
def person_to_dict(person: Person) -> dict:
    return {"name": person.name, "age": person.age}

p = Person("Alice", 30)
json_str = json.dumps(p, default=person_to_dict)
# {"name": "Alice", "age": 30}

# Custom encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)

json_str = json.dumps(p, cls=PersonEncoder)

# Custom decoder
def decode_person(d):
    if "name" in d and "age" in d:
        return Person(d["name"], d["age"])
    return d

p2 = json.loads(json_str, object_hook=decode_person)
print(type(p2), p2.name)            # <class '__main__.Person'> Alice

# Handling datetime
from datetime import datetime

def json_serial(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

now = datetime.now()
json.dumps({"time": now}, default=json_serial)
# {"time": "2026-06-27T14:30:00"}


# 24. DATETIME
# =============
# Easy definition: The datetime module provides classes for working
# with dates, times, and time intervals.
# In-depth: datetime combines date and time. date handles dates
# (year, month, day). time handles time (hour, minute, second).
# timedelta represents durations. strftime/strptime format/parse
# date strings.

from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)                          # 2026-06-27 14:30:00.123456
print(now.year)                     # 2026
print(now.month)                    # 6
print(now.day)                      # 27
print(now.hour)                     # 14
print(now.minute)                   # 30
print(now.second)                   # 0
print(now.microsecond)              # 123456

# Current date only
today = date.today()
print(today)                        # 2026-06-27

# Creating specific dates and times
d = date(2026, 6, 27)
t = time(14, 30, 0)
dt = datetime(2026, 6, 27, 14, 30, 0)

# timedelta — time differences
delta = timedelta(days=7, hours=3)
future = now + delta
past = now - timedelta(weeks=2)
print(future)

# timedelta features
print(delta.days)                   # 7
print(delta.seconds)                # 10800 (3 hours)
print(delta.total_seconds())        # 615600.0

# Difference between datetimes
diff = future - now
print(type(diff))                   # <class 'datetime.timedelta'>

# strftime — format datetime to string
dt = datetime(2026, 6, 27, 14, 30, 0)
print(dt.strftime("%Y-%m-%d"))              # "2026-06-27"
print(dt.strftime("%B %d, %Y"))             # "June 27, 2026"
print(dt.strftime("%I:%M %p"))              # "02:30 PM"
print(dt.strftime("%A, %d %B %Y at %H:%M")) # "Saturday, 27 June 2026 at 14:30"

# Common format codes
# %Y — year (4 digits)
# %m — month (01-12)
# %d — day (01-31)
# %H — hour (00-23)
# %I — hour (01-12)
# %M — minute (00-59)
# %S — second (00-59)
# %p — AM/PM
# %A — weekday full name
# %a — weekday abbreviated
# %B — month full name
# %b — month abbreviated

# strptime — parse string to datetime
date_str = "2026-06-27 14:30:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)                       # 2026-06-27 14:30:00

# time.sleep() — pause execution
import time
print("Start")
time.sleep(1.5)                     # pause for 1.5 seconds
print("After 1.5 seconds")

# time.time() — Unix timestamp (performance measurement)
start = time.time()
# ... some operation ...
end = time.time()
print(f"Elapsed: {end - start:.4f} seconds")

# time.perf_counter() — more precise timing
start = time.perf_counter()
# ... operation ...
end = time.perf_counter()
print(f"Elapsed: {end - start:.6f} seconds")


# 25. REGULAR EXPRESSIONS (re MODULE)
# ====================================
# Easy definition: Regular expressions match patterns in text. The re
# module provides search, match, findall, sub, and split functions.
# In-depth: re.search() finds pattern anywhere in string. re.match()
# matches from beginning only. re.findall() returns all matches.
# re.sub() replaces matches. re.compile() pre-compiles for reuse.

import re

# re.search() — find pattern anywhere
text = "The rain in Spain falls mainly on the plain"
match = re.search(r"Spain", text)
if match:
    print(match.start())            # 14  (start index)
    print(match.end())              # 19  (end index)
    print(match.group())            # "Spain"
    print(match.span())             # (14, 19)

# re.match() — match from beginning only
match = re.match(r"The", text)
print(match.group() if match else None)  # "The"

match = re.match(r"rain", text)
print(match)                        # None (not at start)

# re.findall() — all matches as list
print(re.findall(r"ain", text))     # ['ain', 'ain', 'ain']

# re.finditer() — iterator of match objects
for match in re.finditer(r"\\w+ain", text):
    print(match.group())            # "rain", "Spain", "plain"

# re.sub() — replace matches
result = re.sub(r"ain", "XXX", text)
print(result)                       # "The rXXX in SpXXX falls mXXXly on the plXXX"

# re.split() — split by pattern
parts = re.split(r"\\s+", text)      # split on whitespace
print(parts[:3])                    # ["The", "rain", "in"]

# re.compile() — compile pattern for reuse
pattern = re.compile(r"\\b\\w{4}\\b")  # 4-letter words
matches = pattern.findall(text)
print(matches)                      # ["rain", "spain", "main", "plain"]

# Common patterns
# .       — any character except newline
# ^       — start of string
# $       — end of string
# *       — 0 or more repetitions
# +       — 1 or more repetitions
# ?       — 0 or 1 repetition
# {n}     — exactly n repetitions
# {n,}    — n or more repetitions
# {n,m}   — between n and m repetitions
# \\d      — digit [0-9]
# \\D      — non-digit
# \\w      — word character [a-zA-Z0-9_]
# \\W      — non-word character
# \\s      — whitespace [ \\t\\n\\r\\f\\v]
# \\S      — non-whitespace
# \\b      — word boundary
# []      — character class
# [^]     — negated character class
# |       — OR
# ()      — group
# (?:)    — non-capturing group

# Pattern examples
# Match email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
text2 = "Contact: alice@example.com or bob@test.org"
emails = re.findall(email_pattern, text2)
print(emails)                       # ["alice@example.com", "bob@test.org"]

# Match phone numbers (US)
phone_pattern = r"\\d{3}[-.]?\\d{3}[-.]?\\d{4}"
text3 = "Call 555-123-4567 or 555.987.6543"
phones = re.findall(phone_pattern, text3)
print(phones)                       # ["555-123-4567", "555.987.6543"]

# Match IP address
ip_pattern = r"\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}"

# Groups — extract parts
log_line = "2026-06-27 14:30:00 ERROR: Something went wrong"
pattern = r"(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) (\\w+): (.+)"
match = re.search(pattern, log_line)
if match:
    print(match.groups())           # ("2026-06-27", "14:30:00", "ERROR", "Something went wrong")
    print(match.group(1))           # "2026-06-27"
    print(match.group(2))           # "14:30:00"
    print(match.group(3))           # "ERROR"
    print(match.group(4))           # "Something went wrong"

# Named groups (?P<name>...)
pattern = r"(?P<date>\\d{4}-\\d{2}-\\d{2}) (?P<time>\\d{2}:\\d{2}:\\d{2})"
match = re.search(pattern, log_line)
if match:
    print(match.group("date"))      # "2026-06-27"
    print(match.group("time"))      # "14:30:00"

# Flags
# re.IGNORECASE (re.I) — case insensitive
print(re.findall(r"spain", text, re.IGNORECASE))

# re.MULTILINE (re.M) — ^ and $ match line starts/ends
# re.DOTALL (re.S) — . matches newlines
# re.VERBOSE (re.X) — allow whitespace and comments in pattern

# Greedy vs non-greedy
# * and + are greedy (match as much as possible)
text4 = "<div>hello</div><div>world</div>"
print(re.findall(r"<div>.*</div>", text4))      # greedy: entire string
print(re.findall(r"<div>.*?</div>", text4))      # non-greedy: each tag


# 26. WORKING WITH ITERATORS
# ============================
# Easy definition: Iterators are objects that produce values one at
# a time using __next__(). When exhausted, they raise StopIteration.
# In-depth: Any object with __iter__ and __next__ is an iterator.
# The for loop calls iter() on the iterable, then next() repeatedly.
# The itertools module provides powerful iterator combinators.

# iter() and next()
numbers = [1, 2, 3]
it = iter(numbers)                  # get iterator from iterable
print(next(it))                     # 1
print(next(it))                     # 2
print(next(it))                     # 3
# print(next(it))                   # StopIteration

# for loop is syntactic sugar for:
it = iter(numbers)
while True:
    try:
        value = next(it)
        print(value)
    except StopIteration:
        break

# Custom iterator class
class Range:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for i in Range(0, 5):
    print(i)                        # 0, 1, 2, 3, 4

# Iterator with two-way iteration
class Fibonacci:
    def __init__(self, max_count=10):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

# itertools module
from itertools import chain, cycle, repeat, product, permutations, combinations, groupby, count

# chain — combine iterables sequentially
combined = list(chain([1, 2, 3], [4, 5, 6]))
print(combined)                     # [1, 2, 3, 4, 5, 6]

# cycle — infinitely repeat an iterable
counter = 0
for item in cycle(["A", "B", "C"]):
    print(item)
    counter += 1
    if counter > 5:
        break
# A, B, C, A, B, C

# repeat — repeat a value N times
print(list(repeat("X", 5)))         # ["X", "X", "X", "X", "X"]

# count — infinite counter
for i in count(10, 2):              # 10, 12, 14, 16, ...
    if i > 20:
        break
    print(i)

# product — Cartesian product
print(list(product([1, 2], ["A", "B"])))
# [(1, "A"), (1, "B"), (2, "A"), (2, "B")]

print(list(product([1, 2], repeat=2)))
# [(1, 1), (1, 2), (2, 1), (2, 2)]

# permutations — all orderings
print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations — all subsets (order doesn't matter)
print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

# combinations_with_replacement
from itertools import combinations_with_replacement
print(list(combinations_with_replacement([1, 2, 3], 2)))
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# groupby — group consecutive elements by key function
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
data.sort()                         # groupby requires sorted data!
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# A [("A", 1), ("A", 2)]
# B [("B", 3), ("B", 4)]
# A [("A", 5)]

# islice — slice an iterator
from itertools import islice
result = list(islice(range(100), 10, 20, 2))
print(result)                       # [10, 12, 14, 16, 18]

# takewhile and dropwhile
from itertools import takewhile, dropwhile
print(list(takewhile(lambda x: x < 5, [1, 3, 7, 4, 2])))  # [1, 3]
print(list(dropwhile(lambda x: x < 5, [1, 3, 7, 4, 2])))  # [7, 4, 2]


# 27. BEST PRACTICES & PEP 8
# ===========================
# Easy definition: PEP 8 is Python's style guide. It defines
# conventions for naming, indentation, spacing, and code layout.
# In-depth: Following PEP 8 makes code consistent and readable.
# Tools like black, flake8, and pylint automate style checking.
# PEP 257 covers docstring conventions.

# Naming conventions
# Variables/functions/modules: snake_case
# Classes: PascalCase (CamelCase)
# Constants: UPPER_CASE
# Private attributes: _leading_underscore
# Name-mangled: __double_leading_underscore
# Dunder methods: __double_underscore__ (don't invent your own)

# Indentation — 4 spaces (never tabs)
# Bad:
# def func():
# ··return 42  (2 spaces)

# Good:
def func():
    return 42                   # 4 spaces

# Line length — max 79 characters for code, 72 for comments
long_string = ("This is a long string that exceeds the 79 character "
               "limit, so we use implicit string concatenation "
               "inside parentheses to break it up.")

# Implicit continuation — inside brackets/braces/parens
result = some_function(
    arg1=value1,
    arg2=value2,
    arg3=value3,
)

# Imports — grouped: stdlib first, third-party second, local third
import os
import sys

import requests
import numpy as np

from mypackage import mymodule

# Within groups, sort alphabetically
# Avoid: from module import *
# Prefer explicit imports

# Whitespace
# One space around assignment operators
x = 5

# No space before colon, one space after
if x == 5:
    pass

# One space after comma
def func(a, b, c):
    pass

# Docstrings (PEP 257)
# Module docstring at top of file
# Class docstring after class line
# Function docstring after def line

class MyClass:
    """One-line summary of class.

    More detailed description if needed. This follows PEP 257.
    """

    def my_method(self, param):
        """Do something.

        Args:
            param: Description of parameter.

        Returns:
            Description of return value.
        """
        return param

# Zen of Python
# import this
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one -- and preferably only one -- obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# EAFP (Easier to Ask for Forgiveness than Permission)
# vs LBYL (Look Before You Leap)

# EAFP — Pythonic: try first, handle errors
try:
    result = risky_operation()
except SomeError:
    result = default_value

# LBYL — checks before attempting
if can_do_risky_operation():
    result = risky_operation()
else:
    result = default_value

# EAFP is generally preferred in Python


# 28. ASYNC BASICS
# =================
# Easy definition: Async/await enables concurrent code using
# cooperative multitasking. async def declares an async function
# (coroutine). await pauses execution until the awaited task completes.
# In-depth: asyncio is the standard library for async programming.
# Async code runs in a single thread using an event loop. Tasks
# yield control at await points, allowing other tasks to run.

import asyncio

# Basic async function (coroutine)
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)          # non-blocking sleep
    print("World")

# Run the coroutine
# asyncio.run(say_hello())

# Multiple coroutines concurrently
async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay}s")
    return f"Result {name}"

async def main():
    # Run multiple tasks concurrently
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )
    print(results)                  # ["Result A", "Result B", "Result C"]

# asyncio.run(main())

# Create tasks
async def main_with_tasks():
    task_a = asyncio.create_task(task("A", 2))
    task_b = asyncio.create_task(task("B", 1))

    print("Both tasks running...")
    result_a = await task_a
    result_b = await task_b
    print(result_a, result_b)

# asyncio.run(main_with_tasks())

# Async context manager
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource...")
        await asyncio.sleep(0.5)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource...")
        await asyncio.sleep(0.3)

    async def use(self):
        print("Using resource...")
        await asyncio.sleep(0.2)

async def use_resource():
    async with AsyncResource() as res:
        await res.use()

# Async iterator
class AsyncRange:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        value = self.i
        self.i += 1
        return value

async def iterate_async():
    async for i in AsyncRange(5):
        print(i)


# 29. CONTEXT MANAGERS
# =====================
# Easy definition: Context managers handle setup and cleanup using
# the with statement. They're most commonly used for file operations.
# In-depth: The with statement calls __enter__ on setup and __exit__
# on cleanup — even if an exception occurs. You can create custom
# context managers with classes or the contextlib module.

# Basic with statement
with open("file.txt", "r") as f:
    data = f.read()
# File is auto-closed after block

# Multiple context managers
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())

# Class-based context manager
class ManagedConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        print(f"Connecting to {self.host}:{self.port}...")
        # self.connection = connect(self.host, self.port)
        return self                 # what "as x" gets

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")
        # self.connection.close()
        # Return True to suppress exceptions, False to propagate
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False                # propagate exception if any

# with ManagedConnection("localhost", 8080) as conn:
#     print(f"Connected to {conn.host}")

# contextlib.contextmanager decorator — simpler approach
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode="r"):
    """Context manager for file operations using generator syntax."""
    print(f"Opening {filename}")
    f = open(filename, mode)
    try:
        yield f                     # value yielded to "as" variable
    finally:
        print(f"Closing {filename}")
        f.close()

# with managed_file("test.txt", "w") as f:
#     f.write("Hello!")

# @contextmanager with exception handling
@contextmanager
def suppress(*exceptions):
    """Suppress specified exceptions."""
    try:
        yield
    except exceptions:
        pass                        # silently ignore

# with suppress(ValueError, TypeError):
#     x = int("not a number")       # ValueError suppressed

# contextlib.closing — close objects that have a close() method
from contextlib import closing
# with closing(some_resource()) as res:
#     res.use()

# contextlib.redirect_stdout — temporarily redirect output
from contextlib import redirect_stdout
import io
buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes to buffer, not console")
output = buffer.getvalue()
print(output)                       # "This goes to buffer, not console"


# 30. COMMON GOTCHAS
# ===================
# Easy definition: Python has several well-known pitfalls that trip
# up beginners and experienced developers alike. Understanding these
# saves hours of debugging.
# In-depth: These gotchas arise from Python's design decisions:
# default arguments are evaluated once, closures capture references
# not values, is compares identity not equality, and more.

# 1. Mutable default arguments
def add_item_bad(item, lst=[]):     # BAD
    lst.append(item)
    return lst

print(add_item_bad(1))              # [1]
print(add_item_bad(2))              # [1, 2]  — not [2]!
print(add_item_bad(3))              # [1, 2, 3]

# Why: Function defaults are evaluated once at definition time,
# not each time the function is called.
# Fix: Use None and create a new list each time

def add_item_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# 2. Late binding closures
def create_multipliers():
    return [lambda x: i * x for i in range(5)]

for mult in create_multipliers():
    print(mult(2))                  # 8, 8, 8, 8, 8  (not 0, 2, 4, 6, 8)

# Why: All lambdas capture the variable i by reference, not value.
# By the time they're called, i is 4.
# Fix 1: Default argument captures current value
def create_multipliers_fixed():
    return [lambda x, i=i: i * x for i in range(5)]

for mult in create_multipliers_fixed():
    print(mult(2))                  # 0, 2, 4, 6, 8

# Fix 2: Use a factory function
def create_multipliers_fixed2():
    def make_mult(i):
        return lambda x: i * x
    return [make_mult(i) for i in range(5)]

# 3. is vs ==
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)                       # True  (same value)
print(a is b)                       # False (different objects)

c = a
print(a is c)                       # True  (same object)

# is checks identity (id()), == checks equality (value)
# Use is for: None, True, False, singletons
x = None
if x is None:                       # correct
    pass

if x == None:                       # works but not idiomatic
    pass

# Integer caching (-5 to 256)
a = 256
b = 256
print(a is b)                       # True  (cached)

c = 257
d = 257
print(c is d)                       # False (not cached, separate objects)

# Use == for integer comparison, not is
# CPython caches small integers (-5 to 256) for performance

# 4. Shallow vs deep copy (covered in Lists section)
import copy
original = [[1, 2], [3, 4]]

shallow = original.copy()
shallow[0][0] = 99
print(original[0][0])               # 99  (shared)

deep = copy.deepcopy(original)
deep[0][0] = 42
print(original[0][0])               # 99 (unchanged)

# 5. String immutability
s = "hello"
# s[0] = "H"  # TypeError

# Must create new string
s = "H" + s[1:]
print(s)                            # "Hello"

# 6. Loop variable leakage (Python 2 vs 3)
# Python 3: loop variables don't leak (except in comprehensions)
i = 42
for i in range(5):
    pass
print(i)                            # 4  — loop variable DOES leak

# But list comprehensions in Python 2 leaked; in Python 3 they don't
# x = [i for i in range(5)]
# print(i)  # still 4 (not 4 if the comprehension created new i)

# 7. Chained assignment and mutable objects
x = y = []
x.append(1)
print(y)                            # [1]  — same object!

# Fix: create separately
x = []
y = []
x.append(1)
print(y)                            # []

# 8. Floating point precision
print(0.1 + 0.2)                    # 0.30000000000000004  (not 0.3!)
print(0.1 + 0.2 == 0.3)             # False

# Fix: use rounding or Decimal
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # Decimal("0.3")

# 9. Augmented assignment with mutable vs immutable
# Immutable (int, str, tuple) — creates new object
a = 1
print(id(a))                        # some id
a += 1
print(id(a))                        # different id (new object)

# Mutable (list, dict, set) — modifies in place
b = [1, 2]
print(id(b))                        # some id
b += [3, 4]                         # same as b.extend([3, 4])
print(id(b))                        # same id (modified in place)

# However: b = b + [3, 4]  would create a new list
c = [1, 2]
print(id(c))
c = c + [3, 4]                      # creates new list
print(id(c))                        # different id

# 10. Deleting while iterating
# Bad: modifying list while iterating
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)           # skips next element!
print(numbers)                      # [1, 3, 5]  — works here but dangerous

# Correct way 1: iterate over a copy
numbers = [1, 2, 3, 4, 5]
for n in numbers[:]:                # iterate over copy
    if n % 2 == 0:
        numbers.remove(n)

# Correct way 2: list comprehension (preferred)
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]

# 11. Unpacking with wrong length
# a, b = (1, 2, 3)  # ValueError: too many values to unpack
# Fixed with extended unpacking
a, b, *rest = (1, 2, 3, 4, 5)
print(a, b, rest)                   # 1 2 [3, 4, 5]

# 12. Module import side effects
# When you import a module, all top-level code runs immediately.
# This is why the if __name__ == "__main__": guard is critical.

# 13. Boolean is subclass of int
print(True + True)                  # 2  (True == 1, False == 0)
print(True * 5)                     # 5
print(isinstance(True, int))        # True
print(True == 1)                    # True
print(True is 1)                    # False (different objects, same value)

# 14. Negative indices and -0
lst = [1, 2, 3]
print(lst[-1])                      # 3  (last element)
print(lst[-0])                      # 1  (-0 is 0, first element)

# 15. Or operator returns value, not bool
print(0 or 42)                      # 42  (not True)
print("" or "default")              # "default"
print(42 or 0)                      # 42  (short-circuits)

# Common pattern: assign default
name = input("name: ") or "Guest"

# 16. Comparing different types (Python 2 vs 3)
# Python 3: raises TypeError
# print(42 > "hello")  # TypeError: '>' not supported between str and int

# Python 2: allowed (inconsistent behavior)

# 17. The += operator with tuples
t = (1, 2, [3, 4])
# t[2] += [5, 6]  # TypeError: 'tuple' object does not support item assignment
# But the list IS modified!
# t[2] += [5, 6] is equivalent to:
# t[2].extend([5, 6])  — list is modified
# t[2] = ...  — then fails because tuple doesn't support assignment
# Result: list gets extended but the assignment fails

# 18. All or any on empty iterables
print(all([]))                      # True  (vacuous truth)
print(any([]))                      # False

# 19. Generator exhaustion
gen = (x**2 for x in range(3))
print(list(gen))                    # [0, 1, 4]
print(list(gen))                    # []  — generator exhausted!

# 20. NameError in nested scopes
x = "global"
def outer():
    x = "outer"
    def inner():
        # If you try to access x before assigning, you get UnboundLocalError
        # x += "modified"  # UnboundLocalError: local 'x' referenced before assignment
        pass
    inner()
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
const REGEX_CONTENT = `
# PYTHON REGULAR EXPRESSIONS REFERENCE
# =====================================
# Regex (Regular Expressions) is a pattern-matching language for searching,
# extracting, and manipulating text. Python's re module provides full support.
#
# IMPORTANT: raw strings r"..." prevent Python from processing backslash escapes,
# which is critical since regex uses \\ extensively. Without r"...", you'd need
# \\\\d instead of \\d, making patterns hard to read.

import re

# ---------------------------------------------------------------------------
# 1. WHAT IS REGEX?
# ---------------------------------------------------------------------------

# Regex is a formal language of patterns built from literal characters and
# metacharacters. It describes text to find, match, or replace within strings.
#
# Key concepts:
#   - Pattern: the regex description you write
#   - String: the text you search in
#   - Match: when the pattern successfully describes part (or all) of the string
#
# Raw strings r"...": In normal Python strings, \\n means newline, \\t means tab.
# In raw strings, backslash is literal — exactly what regex engines expect.
#
# Without raw string:  "\\\\d+\\\\.\\\\d+"  (Python escapes the backslashes)
# With raw string:     r"\\d+\\.\\d+"    (what the regex engine actually reads)
#
# The re module provides all regex functionality:
#   re.search()    - find anywhere in string
#   re.match()     - find at start only
#   re.findall()   - find all non-overlapping matches
#   re.sub()       - substitute matches
#   re.split()     - split string at matches
#   re.compile()   - pre-compile for performance

# Basic example: finding digits in a string
pattern = r"\\d+"
text = "Order 42 has 100 items"
result = re.findall(pattern, text)
print(result)  # ['42', '100']

# Example: replacing text
cleaned = re.sub(r"\\d+", "NUMBER", text)
print(cleaned)  # 'Order NUMBER has NUMBER items'

# ---------------------------------------------------------------------------
# 2. METACHARACTERS
# ---------------------------------------------------------------------------

# Metacharacters are characters with special meaning in regex. To match them
# literally, escape with \\ (e.g., \\. matches a literal dot).

# . (dot) - matches ANY SINGLE character except newline
# Equivalent to "any character here"
pattern = r"h.t"
print(re.findall(pattern, "hat hot hit hut h\\t h\\n"))  # ['hat', 'hot', 'hit', 'hut', 'h\\t']
# NOTE: \\n (newline) is NOT matched by dot by default

# ^ (caret) - matches the START of the string
pattern = r"^Hello"
print(re.findall(pattern, "Hello world"))   # ['Hello']
print(re.findall(pattern, "Say Hello"))     # [] - not at start

# $ (dollar) - matches the END of the string
pattern = r"end$"
print(re.findall(pattern, "this is the end"))  # ['end']
print(re.findall(pattern, "end of the line"))  # [] - string doesn't end with it

# * (star) - matches 0 or MORE of the preceding element (GREEDY)
# "abc*" matches "ab", "abc", "abcc", "abccc", etc.
pattern = r"ab*c"
print(re.findall(pattern, "ac abc abbc abbbc abbbbc"))  # ['ac', 'abc', 'abbc', 'abbbc', 'abbbbc']

# + (plus) - matches 1 or MORE of the preceding element (GREEDY)
# "abc+" matches "abc", "abcc", but NOT "ab"
pattern = r"ab+c"
print(re.findall(pattern, "ac abc abbc abbbc"))  # ['abc', 'abbc', 'abbbc']
print(re.findall(pattern, "ac"))                  # [] - need at least one b

# ? (question mark) - matches 0 or 1 of the preceding element
# Makes something OPTIONAL
pattern = r"colou?r"
print(re.findall(pattern, "color colour"))  # ['color', 'colour']

# {n} - matches EXACTLY n repetitions
pattern = r"\\d{3}"  # exactly three digits
print(re.findall(pattern, "abc123def4567"))  # ['123', '456'] (only first 3 of 4567)

# {n,} - matches n or MORE repetitions
pattern = r"\\d{3,}"  # three or more digits
print(re.findall(pattern, "12 123 1234 12345"))  # ['123', '1234', '12345']

# {n,m} - matches BETWEEN n and m repetitions (inclusive)
pattern = r"\\d{2,4}"  # 2, 3, or 4 digits
print(re.findall(pattern, "1 12 123 1234 12345"))  # ['12', '123', '1234', '1234']

# [] (square brackets) - CHARACTER SET, matches ANY ONE character inside
pattern = r"[aeiou]"  # any vowel (single character)
print(re.findall(pattern, "hello world"))  # ['e', 'o', 'o']

# Inside a set, most metacharacters lose their special meaning
pattern = r"[.^$]"  # literal dot, caret, or dollar sign
print(re.findall(pattern, "abc.^$def"))  # ['.', '^', '$']

# | (pipe) - ALTERNATION (OR) between patterns
pattern = r"cat|dog"
print(re.findall(pattern, "I have a cat and a dog"))  # ['cat', 'dog']

# () (parentheses) - GROUPING
# Creates a group for capturing, applying quantifiers, or alternation scope
pattern = r"(ha)+"  # group "ha" one or more times
print(re.findall(pattern, "haha hahaha h"))  # ['ha', 'ha'] (last match of each)

# \\ (backslash) - ESCAPE character
# Two uses: (1) escape metacharacters, (2) create special sequences
pattern = r"\\."  # literal dot (not "any character")
print(re.findall(pattern, "a.b.c"))  # ['.', '.']

pattern = r"\\d"  # digit character class
print(re.findall(pattern, "a1b2c"))  # ['1', '2']

# ---------------------------------------------------------------------------
# 3. CHARACTER CLASSES
# ---------------------------------------------------------------------------

# Character classes define a SET of characters to match at a position.

# [abc] - matches ONE character: a, b, or c
pattern = r"[aeiou]"
print(re.findall(pattern, "python"))  # ['o']

# [^abc] - NEGATION: matches ANY character EXCEPT a, b, or c
pattern = r"[^aeiou]"  # all consonants (and non-letters)
print(re.findall(pattern, "hello"))  # ['h', 'l', 'l']

# [a-z] - RANGE: matches any character in the range a to z
pattern = r"[a-z]"  # any lowercase letter
print(re.findall(pattern, "Hello123"))  # ['e', 'l', 'l', 'o']

# Multiple ranges: [a-zA-Z0-9] matches any letter or digit
pattern = r"[a-zA-Z0-9]"
print(re.findall(pattern, "A b 3 !"))  # ['A', 'b', '3']

# \\d - DIGIT: matches [0-9] (single character)
pattern = r"\\d"
print(re.findall(pattern, "Room 42B"))  # ['4', '2']

# \\D - NOT a digit: matches [^0-9]
pattern = r"\\D"
print(re.findall(pattern, "A1 B2"))  # ['A', ' ', 'B', ' ']

# \\w - WORD CHARACTER: matches [a-zA-Z0-9_]
# Includes letters (both cases), digits, and underscore
pattern = r"\\w+"
print(re.findall(pattern, "hello_world 123 !@#"))  # ['hello_world', '123']

# \\W - NOT a word character: matches [^a-zA-Z0-9_]
pattern = r"\\W+"
print(re.findall(pattern, "hello world!"))  # [' ', '!']

# \\s - WHITESPACE: matches [ \\t\\n\\r\\f\\v] (space, tab, newline, etc.)
pattern = r"\\s+"
print(re.findall(pattern, "hello   world\\nnext"))  # ['   ', '\\n']

# \\S - NOT whitespace: matches non-whitespace characters
pattern = r"\\S+"
print(re.findall(pattern, "a b\\tc\\nd"))  # ['a', 'b', 'c', 'd']

# Practical: find all words in text
pattern = r"\\w+"
text = "Hello, world! It's 2025."
print(re.findall(pattern, text))  # ['Hello', 'world', 'It', 's', '2025']

# Practical: find all non-words (punctuation, spaces)
pattern = r"\\W+"
text = "Hello, world! It's 42."
print(re.findall(pattern, text))  # [', ', '! ', "'s ", '.']

# ---------------------------------------------------------------------------
# 4. QUANTIFIERS - GREEDY vs LAZY (NON-GREEDY)
# ---------------------------------------------------------------------------

# QUANTIFIERS control HOW MANY times a pattern element repeats.
#
# GREEDY (default): tries to match AS MUCH AS POSSIBLE, then backtracks if
# the rest of the pattern fails. The engine grabs everything it can, then
# gives back one character at a time until the overall pattern matches.
#
# LAZY (with ? after quantifier): tries to match AS LITTLE AS POSSIBLE.
# The engine matches the minimum, then expands if the overall pattern fails.

# Greedy: * matches as much as possible
text = "<div>hello</div><span>world</span>"
pattern = r"<.*>"  # greedy: from first < to LAST >
print(re.findall(pattern, text))  # ['<div>hello</div><span>world</span>']

# Lazy: *? matches as little as possible
pattern = r"<.*?>"  # lazy: from each < to the next >
print(re.findall(pattern, text))  # ['<div>', '</div>', '<span>', '</span>']

# Greedy vs Lazy comparison table:
#   Quantifier  | Greedy (max) | Lazy (min)
#   ---------------------------------------
#   star        | *            | *?
#   plus        | +            | +?
#   optional    | ?            | ??
#   range       | {n,m}        | {n,m}?
#   range+      | {n,}         | {n,}?

# + vs +? examples
text = "abcabc"
print(re.findall(r"ab+c", text))   # greedy:  ['abcabc'] (matches from a to last c)
print(re.findall(r"ab+?c", text))  # lazy:   ['abc'] (first a to first c)

# ? vs ??
pattern_greedy = r"colou?r"  # greedy optional
pattern_lazy = r"colou??r"   # lazy optional (prefer without u)
print(re.findall(pattern_greedy, "color colour"))  # ['color', 'colour']
print(re.findall(pattern_lazy, "color colour"))    # ['color', 'colour']

# {n,m} vs {n,m}? examples
text = "aaaa"
pattern_greedy = r"a{2,4}"   # 2 to 4 a's, prefer 4
pattern_lazy = r"a{2,4}?"    # 2 to 4 a's, prefer 2
print(re.findall(pattern_greedy, text))  # ['aaaa']
print(re.findall(pattern_lazy, text))    # ['aa', 'aa']

# How backtracking works with greedy quantifiers:
# Pattern: r"a.*b"  on string "a---b---b"
# Step 1: a matches a at position 0
# Step 2: .* matches "---b---b" (everything to end)
# Step 3: b needs to match but we're at end -> FAIL
# Step 4: .* gives back "b" -> now we have "---b---"
# Step 5: b matches the last b -> SUCCESS
# Match: "a---b---b"

# With lazy: r"a.*?b"  on same string
# Step 1: a matches a at position 0
# Step 2: .*? matches "" (minimum)
# Step 3: b matches first b -> SUCCESS immediately
# Match: "a---b"

# ---------------------------------------------------------------------------
# 5. ANCHORS
# ---------------------------------------------------------------------------

# Anchors match POSITIONS in the string, not characters.

# ^ (caret) - start of string (or start of line with re.MULTILINE)
pattern = r"^Hello"
print(re.search(pattern, "Hello world"))     # <re.Match...> at position 0
print(re.search(pattern, "Say Hello world"))  # None

# With re.MULTILINE: ^ matches after each newline
text = "First line\\nSecond line\\nThird line"
pattern = r"^\\w+"
print(re.findall(pattern, text))                          # ['First'] (start of string only)
print(re.findall(pattern, text, re.MULTILINE))            # ['First', 'Second', 'Third']

# $ (dollar) - end of string (or end of line with re.MULTILINE)
pattern = r"line$"
print(re.search(pattern, "end of line"))      # matches
print(re.search(pattern, "line of text"))     # None

# With re.MULTILINE: $ matches before each newline
text = "First line\\nSecond line\\nThird line"
pattern = r"\\w+$"
print(re.findall(pattern, text))               # ['line'] (end of string only)
print(re.findall(pattern, text, re.MULTILINE)) # ['line', 'line', 'line']

# \\b - WORD BOUNDARY: position between a word char (\\w) and non-word char (\\W)
# Matches at start/end of words (zero-width)
pattern = r"\\bcat\\b"  # whole word "cat", not in "catalog" or "scat"
print(re.findall(pattern, "cat catalog scat concat"))  # ['cat']

# \\b at start: words starting with pattern
pattern = r"\\bun"  # words starting with "un"
print(re.findall(pattern, "unable unit fun under"))  # ['un', 'un', 'un']

# \\b at end: words ending with pattern
pattern = r"ing\\b"  # words ending with "ing"
print(re.findall(pattern, "running walk singing"))  # ['ing', 'ing']

# \\B - NOT a word boundary: opposite of \\b
pattern = r"\\Bcat\\B"  # "cat" NOT at word boundary (inside a word)
print(re.findall(pattern, "catalog concat"))  # ['cat'] (in "concat", between n and a)

# \\A - start of string ONLY (never affected by re.MULTILINE)
pattern = r"\\AHello"
text = "Hello\\nHello"
print(re.findall(pattern, text))                # ['Hello']
print(re.findall(pattern, text, re.MULTILINE))  # ['Hello'] (only first, \\A ignores multiline)

# \\Z - end of string ONLY (never affected by re.MULTILINE)
pattern = r"end\\Z"
print(re.findall(pattern, "line end"))                       # ['end']
print(re.findall(pattern, "line end\\nline end", re.MULTILINE))  # ['end'] (only last)

# ---------------------------------------------------------------------------
# 6. GROUPS & CAPTURING
# ---------------------------------------------------------------------------

# Groups capture parts of a match for extraction, reuse, or backreferencing.

# (pattern) - CAPTURING GROUP: captures and stores matched text by number
pattern = r"(\\w+)@(\\w+)\\.(\\w+)"  # three groups: user, domain, tld
match = re.search(pattern, "user@example.com")
if match:
    print(match.group())    # 'user@example.com' (full match)
    print(match.group(1))   # 'user'
    print(match.group(2))   # 'example'
    print(match.group(3))   # 'com'
    print(match.groups())   # ('user', 'example', 'com')

# Groups are numbered by opening parenthesis position, starting at 1
# Group 0 is always the entire match
pattern = r"((\\w+)@(\\w+))\\.(\\w+)"  # nested groups
match = re.search(pattern, "user@example.com")
print(match.groups())  # ('user@example', 'user', 'example', 'com')

# (?P<name>pattern) - NAMED CAPTURING GROUP: capture by name instead of number
pattern = r"(?P<user>\\w+)@(?P<domain>\\w+)\\.(?P<tld>\\w+)"
match = re.search(pattern, "user@example.com")
if match:
    print(match.group("user"))    # 'user'
    print(match.group("domain"))  # 'example'
    print(match.group("tld"))     # 'com'
    print(match.groupdict())      # {'user': 'user', 'domain': 'example', 'tld': 'com'}

# Named groups can still be accessed by number too
print(match.group(1))  # also 'user'

# (?:pattern) - NON-CAPTURING GROUP: groups without storing the match
# Use when you need grouping (for quantifiers or alternation) but not extraction
text = "hello123 hello456"
pattern = r"(?:\\w+)(\\d+)"  # first group non-capturing, second captures digits
print(re.findall(pattern, text))  # ['123', '456'] - only captured groups returned

# Non-capturing is more efficient and cleaner when you don't need the capture
pattern = r"(?:ha)+"  # group for repetition, but we don't need "ha" saved
print(re.findall(pattern, "haha ha"))  # ['haha', 'ha'] (full matches only)

# \\1, \\2, etc. - BACKREFERENCES in the pattern itself
# Reference a previously captured group WITHIN the same pattern
# Finds repeated words
pattern = r"(\\w+) \\1"  # same word twice, separated by space
print(re.findall(pattern, "cat cat dog hello dog dog"))  # ['cat', 'dog']

# Backreferences can match quotes, HTML tags, etc.
pattern = r"(['\\"])(.*?)\\1"  # matching opening and closing quotes
print(re.findall(pattern, "'hello' \\"world\\" 'broken" ))
# [("'", 'hello'), ('"', 'world')]

# \\g<name> - BACKREFERENCE by name (for named groups)
pattern = r"(?P<word>\\w+) \\g<word>"  # same as (\\w+) \\1 but by name
print(re.findall(pattern, "hello hello world"))  # ['hello']

# Practical: extract key=value pairs
text = "name=John age=30 city=NYC"
pattern = r"(\\w+)=(\\w+)"
matches = re.findall(pattern, text)
print(matches)  # [('name', 'John'), ('age', '30'), ('city', 'NYC')]

# ---------------------------------------------------------------------------
# 7. LOOKAHEAD & LOOKBEHIND (Lookaround Assertions)
# ---------------------------------------------------------------------------

# Lookaround assertions check for a pattern WITHOUT including it in the match.
# They are ZERO-WIDTH — they assert something about the surrounding text.
#
# All four types:
#   (?=...)  Positive Lookahead:  must follow, not consumed
#   (?!...)  Negative Lookahead:  must NOT follow
#   (?<=...) Positive Lookbehind: must precede, not consumed
#   (?<!...) Negative Lookbehind: must NOT precede

# (?=pattern) - POSITIVE LOOKAHEAD: match if "pattern" follows, but don't include it
# Example: find all numbers followed by "px"
text = "12px 34em 56px 78pt"
pattern = r"\\d+(?=px)"  # digits only if followed by "px"
print(re.findall(pattern, text))  # ['12', '56']

# (?!pattern) - NEGATIVE LOOKAHEAD: match if "pattern" does NOT follow
# Example: find all numbers NOT followed by "px"
pattern = r"\\d+(?!px)"  # digits not followed by "px"
print(re.findall(pattern, "12px 34em 56px 78pt"))
# ['3', '56', '78'] - 12 excluded (px follows), 34 gives '3' (4 matches px...)

# Better negative lookahead with word boundary
pattern = r"\\b\\d+(?!px)\\b"
print(re.findall(pattern, "12px 34em 56px 78pt"))  # ['34', '78']

# Practical: find "foo" NOT followed by "bar"
text = "foobar foo foo baz"
pattern = r"foo(?!bar)"
print(re.findall(pattern, text))  # ['foo', 'foo'] (first "foo" in "foobar" excluded)

# (?<=pattern) - POSITIVE LOOKBEHIND: match if preceded by "pattern"
# Example: extract dollar amounts (digits after $ sign)
text = "Price: $42.50, Cost: $15"
pattern = r"(?<=\\$)\\d+\\.?\\d*"  # digits with optional decimal after $
print(re.findall(pattern, text))  # ['42', '50', '15'] wait — '50' is after the dot

# Let me be more precise
pattern = r"(?<=\\$)\\d+(?:\\.\\d+)?"  # digits plus optional decimal part
print(re.findall(pattern, text))    # ['42.50', '15']

# (?<!pattern) - NEGATIVE LOOKBEHIND: match if NOT preceded by pattern
# Example: find "foo" NOT preceded by "bar"
text = "barfoo foo foobar"
pattern = r"(?<!bar)foo"
print(re.findall(pattern, text))  # ['foo', 'foo'] (first "foo" in "barfoo" excluded actually no)

# Let me be clearer
text = "prefix_foo foo barfoo"
pattern = r"(?<!bar)foo"
print(re.findall(pattern, text))  # ['foo'] only the second "foo" — "barfoo" has "foo" after "bar"

# Practical: extract usernames from Twitter handles
text = "Follow @user1 and @user2 but not user3"
pattern = r"(?<=@)\\w+"  # word after @ sign
print(re.findall(pattern, text))  # ['user1', 'user2']

# Practical: find "python" when it IS followed by "3" or "regex"
text = "I love python3 and python regex but not python2"
pattern = r"python(?=\\s*[3r])"  # python followed by optional space then 3 or r
print(re.findall(pattern, text))  # ['python', 'python']

# Practical: find numbers NOT preceded by $
text = "Total: 42 items, Price: $10, Quantity: 5"
pattern = r"(?<!\\$)\\b\\d+\\b"
print(re.findall(pattern, text))  # ['42', '5'] (not '10')

# NOTE: Python's re module requires lookbehinds to be FIXED-WIDTH.
# This is WRONG: r"(?<=\\s*\\$)\\d+"  (variable width)
# Use a fixed-width alternative or the regex module (third-party) instead.
# WRONG: pattern = r"(?<=\\s+)\\d+"  # ValueError: lookbehind requires fixed-width pattern

# ---------------------------------------------------------------------------
# 8. ALTERNATION
# ---------------------------------------------------------------------------

# Alternation lets the pattern match one option OR another.

# pattern1|pattern2|pattern3 - try each from left to right, return first match
pattern = r"cat|dog|bird"
print(re.findall(pattern, "I have a cat and a dog"))  # ['cat', 'dog']

# Alternation with grouping: limit the scope of |
# Without grouping: the | applies to everything left vs right
text = "I see a catfish and a dog"
pattern = r"cat|catfish"  # matches "cat" first (order matters!)
print(re.findall(pattern, text))  # ['cat', 'cat'] — "catfish" = "cat" + "fish"

# With grouping: | applies only within the group
pattern = r"(cat|dog)fish"  # either "catfish" or "dogfish"
print(re.findall(pattern, text))                                 # ['cat']
print(re.findall(r"(?:cat|dog)fish", "I see a catfish dogfish"))  # ['catfish', 'dogfish']

# Order matters in alternation: re tries patterns left to right
# If an earlier alternative matches, later ones are never tried for that position
text = "abcdef"
pattern = r"(abc|abcd|abcdef)"
print(re.search(pattern, text).group())  # 'abc' (first alternative matches)

pattern = r"(abcdef|abcd|abc)"
print(re.search(pattern, text).group())  # 'abcdef' (longest matched first)

# Practical: match common date formats
text = "Date: 2024-01-15 or 01/15/2024"
pattern = r"\\d{4}-\\d{2}-\\d{2}|\\d{2}/\\d{2}/\\d{4}"
print(re.findall(pattern, text))  # ['2024-01-15', '01/15/2024']

# Practical: match file extensions
filenames = "file.txt image.jpg document.pdf script.py"
pattern = r"\\.(txt|jpg|png|pdf|py)"
print(re.findall(pattern, filenames))  # ['txt', 'jpg', 'pdf', 'py']

# ---------------------------------------------------------------------------
# 9. FLAGS
# ---------------------------------------------------------------------------

# Flags modify how the regex engine interprets the pattern.
# Pass as the flags argument to re functions, or embed inline in the pattern.

# --- re.IGNORECASE (re.I) ---
# Makes matching case-insensitive for ASCII letters by default
pattern = r"python"
print(re.findall(pattern, "Python PYTHON python"))           # ['python']
print(re.findall(pattern, "Python PYTHON python", re.I))     # ['Python', 'PYTHON', 'python']

# --- re.MULTILINE (re.M) ---
# Changes ^ and $ to match at start/end of EACH LINE, not just the string
text = "line1\\nline2\\nline3"
pattern = r"^\\w+"
print(re.findall(pattern, text))            # ['line1']
print(re.findall(pattern, text, re.M))      # ['line1', 'line2', 'line3']

pattern = r"\\w+$"
print(re.findall(pattern, text))            # ['line3']
print(re.findall(pattern, text, re.M))      # ['line1', 'line2', 'line3']

# --- re.DOTALL (re.S) ---
# Makes . match ANY character INCLUDING newline
text = "hello\\nworld"
print(re.findall(r"hello.world", text))     # [] (dot doesn't match \\n)
print(re.findall(r"hello.world", text, re.S))  # ['hello\\nworld']

# --- re.VERBOSE (re.X) ---
# Allows whitespace and comments in the pattern for readability
# Spaces in the pattern are IGNORED (use \\s or [ ] to match literal space)
# Comments with # are ignored to end of line

# Without VERBOSE — hard to read:
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

# With VERBOSE — readable:
email_pattern = re.compile(r"""
    ^                        # start of string
    [a-zA-Z0-9._%+-]+        # local part (username)
    @                        # literal @
    [a-zA-Z0-9.-]+           # domain name
    \\.                       # literal dot
    [a-zA-Z]{2,}             # TLD (at least 2 letters)
    $                        # end of string
""", re.VERBOSE)

print(email_pattern.match("user@example.com"))   # <re.Match...>
print(email_pattern.match("user@example.com.org"))  # None (extra domain part)

# --- re.ASCII (re.A) ---
# Makes \\w, \\d, \\s, \\b match only ASCII characters, ignoring Unicode
text = "café 123"
print(re.findall(r"\\w+", text))             # ['café', '123'] (Unicode aware)
print(re.findall(r"\\w+", text, re.A))       # ['caf', '123']  (é is not ASCII \\w)

# --- re.UNICODE (re.U) ---
# This is the DEFAULT in Python 3. Makes \\w, \\d, \\s Unicode-aware.
# Usually you don't need to specify it explicitly.

# --- INLINE FLAGS ---
# Embed flags directly in the pattern using (?flags)
# (?i) = IGNORECASE, (?m) = MULTILINE, (?s) = DOTALL, (?x) = VERBOSE
# (?aiLmsux) — combine multiple flags

# Inline ignorecase: (?i) makes rest of pattern case-insensitive
pattern = r"(?i)python"
print(re.findall(pattern, "Python PYTHON python"))  # ['Python', 'PYTHON', 'python']

# Inline flags can be scoped to part of the pattern with (?i:pattern)
pattern = r"(?i:hello) world"  # only "hello" is case-insensitive
print(re.findall(pattern, "HELLO world"))   # ['HELLO world']
print(re.findall(pattern, "HELLO WORLD"))   # [] (world is case-sensitive)

# Multiple inline flags: (?im) = IGNORECASE + MULTILINE
pattern = r"(?im)^python"
text = "Python\\nPYTHON\\npython"
print(re.findall(pattern, text))  # ['Python', 'PYTHON', 'python']

# Disable flags: (?-i) turns off ignorecase
pattern = r"(?i)hello(?-i) world"  # "hello" case-insensitive, " world" not
print(re.findall(pattern, "HELLO world"))   # ['HELLO world']
print(re.findall(pattern, "HELLO WORLD"))   # []

# ---------------------------------------------------------------------------
# 10. PYTHON re MODULE METHODS
# ---------------------------------------------------------------------------

# ============ re.search(pattern, string, flags=0) ============
# Scans through string looking for FIRST match anywhere.
# Returns Match object or None.

text = "My email is john@example.com and support@test.org"
match = re.search(r"\\w+@\\w+\\.\\w+", text)
if match:
    print(match.group())  # 'john@example.com' (first match only)

match = re.search(r"zzz", text)
print(match)  # None

# ============ re.match(pattern, string, flags=0) ============
# Looks for match ONLY at the START of the string.
# Returns Match object or None.
# NOTE: "at start" means the match must begin at position 0.

text = "123-456-7890"
match = re.match(r"\\d{3}", text)
print(match.group())  # '123' (matches at start)

match = re.match(r"-\\d{3}", text)
print(match)  # None (text doesn't start with -)

# re.match vs re.search difference:
text = "Contact: 555-1234"
print(re.match(r"\\d+", text))   # None (no digit at position 0)
print(re.search(r"\\d+", text))  # <re.Match...> (digits found at position 9)

# ============ re.fullmatch(pattern, string, flags=0) ============
# Requires the ENTIRE string to match the pattern.
# Returns Match object or None.

print(re.fullmatch(r"\\d+", "123"))     # <re.Match...>
print(re.fullmatch(r"\\d+", "123abc"))  # None (extra characters)
print(re.match(r"\\d+", "123abc"))      # <re.Match...> (match succeeds at start)

# ============ re.findall(pattern, string, flags=0) ============
# Returns ALL non-overlapping matches as a list of strings.
# If the pattern has groups, returns list of tuples (one tuple per group set).

text = "red 5, blue 10, green 15"

# No groups: returns list of full match strings
print(re.findall(r"\\d+", text))  # ['5', '10', '15']

# With groups: returns list of tuples
print(re.findall(r"(\\w+) (\\d+)", text))  # [('red', '5'), ('blue', '10'), ('green', '15')]

# Multiple groups in one pattern
text = "Name: John, Age: 30 | Name: Jane, Age: 25"
pattern = r"Name: (\\w+), Age: (\\d+)"
print(re.findall(pattern, text))  # [('John', '30'), ('Jane', '25')]

# ============ re.finditer(pattern, string, flags=0) ============
# Returns an ITERATOR yielding Match objects.
# More memory-efficient than findall when you need Match object features.

text = "apple 10, banana 20, cherry 30"
for match in re.finditer(r"(\\w+) (\\d+)", text):
    item = match.group(1)
    count = match.group(2)
    print(f"{item}: {count}")
# Output:
# apple: 10
# banana: 20
# cherry: 30

# finditer gives you access to positions, while findall only gives strings
for match in re.finditer(r"\\d+", "results: 42, 100, 7"):
    print(f"Value: {match.group()} at position {match.start()}-{match.end()}")
# Output:
# Value: 42 at position 9-11
# Value: 100 at position 13-16
# Value: 7 at position 18-19

# ============ re.sub(pattern, repl, string, count=0, flags=0) ============
# Replaces matches with replacement string.
# count=0 means replace ALL. count=N means replace first N matches.
# Returns the modified string.

text = "I have 2 cats and 3 dogs"
result = re.sub(r"\\d+", "N", text)
print(result)  # 'I have N cats and N dogs'

# count limits replacements
result = re.sub(r"\\d+", "N", text, count=1)
print(result)  # 'I have N cats and 3 dogs'

# Replacement can reference groups: \\1, \\2 or \\g<1>, \\g<name>
text = "John Smith"
result = re.sub(r"(\\w+) (\\w+)", r"\\2, \\1", text)
print(result)  # 'Smith, John'

# Using named groups in replacement
result = re.sub(r"(?P<first>\\w+) (?P<last>\\w+)", r"\\g<last>, \\g<first>", text)
print(result)  # 'Smith, John'

# Replacement can be a FUNCTION:
def multiply(match):
    value = int(match.group())
    return str(value * 2)

result = re.sub(r"\\d+", multiply, "3 cats and 5 dogs")
print(result)  # '6 cats and 10 dogs'

# ============ re.subn(pattern, repl, string, count=0, flags=0) ============
# Same as re.sub but RETURNS A TUPLE: (new_string, number_of_replacements)

text = "a1 b2 c3 d4"
result, count = re.subn(r"\\d+", "X", text)
print(result)  # 'aX bX cX dX'
print(count)   # 4

result, count = re.subn(r"\\d+", "X", text, count=2)
print(result)  # 'aX bX c3 d4'
print(count)   # 2

# ============ re.split(pattern, string, maxsplit=0, flags=0) ============
# Splits string at every match of the pattern.
# maxsplit=0 means no limit. maxsplit=N limits to N splits.

text = "apple,banana;cherry|date"
result = re.split(r"[,;|]", text)
print(result)  # ['apple', 'banana', 'cherry', 'date']

# maxsplit limits splits
result = re.split(r"[,;|]", text, maxsplit=2)
print(result)  # ['apple', 'banana', 'cherry|date']

# If pattern captures groups, captured groups appear in the result
result = re.split(r"(,|;|\\|)", text)
print(result)  # ['apple', ',', 'banana', ';', 'cherry', '|', 'date']
# Useful for keeping the delimiters

# Split on whitespace
text = "one   two\\tthree\\nfour"
result = re.split(r"\\s+", text)
print(result)  # ['one', 'two', 'three', 'four']

# ============ re.compile(pattern, flags=0) ============
# Pre-compiles a pattern into a RegexObject for repeated use.
# Much faster when using the same pattern many times.

# Without compile (re-parsed every call):
for word in ["cat", "dog", "bird"]:
    if re.search(r"\\d+", word):  # pattern compiled each iteration
        pass

# With compile (pattern parsed once):
digit_pattern = re.compile(r"\\d+")
for word in ["cat", "dog", "bird"]:
    if digit_pattern.search(word):  # reuse compiled pattern
        pass

# Compiled pattern has all the same methods:
pattern = re.compile(r"(\\w+)@(\\w+)\\.(\\w+)", re.I)
match = pattern.search("John@Example.COM")
if match:
    print(match.groups())  # ('John', 'Example', 'COM')

# Methods on compiled pattern:
#   .search(string)     .match(string)     .fullmatch(string)
#   .findall(string)    .finditer(string)  .sub(repl, string)
#   .subn(repl, string) .split(string)
# No need to pass flags again — already compiled in

pattern = re.compile(r"\\d+")
print(pattern.findall("a1 b2 c3"))     # ['1', '2', '3']
print(pattern.sub("X", "a1 b2 c3"))    # 'aX bX cX'

# Get pattern info from compiled object:
print(pattern.pattern)  # '\\d+'
print(pattern.flags)    # 32 (or whatever flags were passed)

# ---------------------------------------------------------------------------
# 11. MATCH OBJECT METHODS & ATTRIBUTES
# ---------------------------------------------------------------------------

# When re.search, re.match, re.fullmatch, or re.finditer succeed, they return
# or yield Match objects. These provide details about where and what matched.

text = "Contact: john.doe@example.com (work)"
match = re.search(r"(?P<user>\\w+\\.\\w+)@(?P<domain>\\w+\\.\\w+)", text)

if match:
    # .group() - entire match (same as .group(0))
    print(match.group())       # 'john.doe@example.com'

    # .group(n) - specific numbered group
    print(match.group(1))      # 'john.doe'
    print(match.group(2))      # 'example.com'

    # .group(name) - named group
    print(match.group("user"))    # 'john.doe'
    print(match.group("domain"))  # 'example.com'

    # .groups() - all groups as tuple
    print(match.groups())     # ('john.doe', 'example.com')
    print(match.groups(0))    # ('john.doe', 'example.com') — default=None for unmatched groups

    # .groupdict() - named groups as dict
    print(match.groupdict())  # {'user': 'john.doe', 'domain': 'example.com'}

    # .start() - start position of match (or specific group)
    print(match.start())      # 9 (where 'john.doe@example.com' starts)
    print(match.start(1))     # 9 (where group 1 starts)
    print(match.start(2))     # 18 (where group 2 starts)

    # .end() - end position of match (or specific group)
    print(match.end())        # 30 (where match ends, exclusive)
    print(match.end(1))       # 17 (where group 1 ends)

    # .span() - (start, end) tuple
    print(match.span())       # (9, 30)
    print(match.span(1))      # (9, 17)
    print(match.span("domain"))  # (18, 30)

    # .string - the original string passed to the search
    print(match.string)       # 'Contact: john.doe@example.com (work)'

    # .re - the compiled pattern object used
    print(match.re)           # re.compile('...')
    print(match.re.pattern)   # the pattern string
    print(match.re.flags)     # the flags integer

# Example: Using match object for extraction
log_line = "2024-01-15 14:30:00 ERROR: Connection timeout on port 8080"
pattern = r"(?P<date>\\d{4}-\\d{2}-\\d{2}) (?P<time>\\d{2}:\\d{2}:\\d{2}) (?P<level>\\w+): (?P<message>.+)"
match = re.search(pattern, log_line)

if match:
    print(f"Date: {match.group('date')}")       # '2024-01-15'
    print(f"Time: {match.group('time')}")       # '14:30:00'
    print(f"Level: {match.group('level')}")     # 'ERROR'
    print(f"Message: {match.group('message')}") # 'Connection timeout on port 8080'
    print(f"Line occupies: {match.span()}")     # (0, 56)

# ---------------------------------------------------------------------------
# 12. COMMON PATTERNS
# ---------------------------------------------------------------------------

# ---------- Email Address ----------
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
text = "Contact: support@example.com or admin@test.co.uk"
print(re.findall(email_pattern, text))  # ['support@example.com', 'admin@test.co.uk']

# ---------- URL ----------
url_pattern = r"https?://[^\\s]+"
text = "Visit https://example.com/path?q=1 and http://test.org"
print(re.findall(url_pattern, text))  # ['https://example.com/path?q=1', 'http://test.org']

# ---------- Phone Number (US) ----------
phone_pattern = r"\\d{3}[-.]?\\d{3}[-.]?\\d{4}"
text = "Call 555-123-4567 or 555.123.4568 or 5551234569"
print(re.findall(phone_pattern, text))
# ['555-123-4567', '555.123.4568', '5551234569']

# With area code in parens:
phone2 = r"\\(?\\d{3}\\)?[-.]?\\d{3}[-.]?\\d{4}"
text = "Call (555) 123-4567 or 555-123-4568"
# Note: this simplified version doesn't handle the space after parens
print(re.findall(phone2, text))
# ['(555)', '123-4567', '555-123-4568'] — broken because we need to handle the whole thing

# Better phone pattern
phone3 = r"\\(?\\d{3}\\)?[\\s-]?\\d{3}[-.]?\\d{4}"
text = "Call (555) 123-4567 or 555-123-4568"
print(re.findall(phone3, text))  # ['(555) 123-4567', '555-123-4568']

# ---------- Date (ISO format) ----------
date_pattern = r"\\d{4}-\\d{2}-\\d{2}"
text = "Events: 2024-01-15, 2024-12-25, and invalid 2024-2-1"
print(re.findall(date_pattern, text))  # ['2024-01-15', '2024-12-25']

# ---------- IP Address (IPv4) ----------
ip_pattern = r"\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}"
# Note: this validates format but not range (0-255). Each octet is 1-3 digits.
text = "Server: 192.168.1.1, Gateway: 10.0.0.1"
print(re.findall(ip_pattern, text))
# ['192.168.1.1', '10.0.0.1']

# More precise: validates each octet 0-255 (advanced pattern)
ip_precise = r"(?:(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d\\d?)"
text = "Valid: 192.168.1.1, Invalid: 999.999.999.999"
print(re.findall(ip_precise, text))  # ['192.168.1.1']

# ---------- Hexadecimal Number ----------
hex_pattern = r"0[xX][0-9a-fA-F]+"
text = "Colors: 0xFF, 0x00, 0x1A2B, and 123 (not hex)"
print(re.findall(hex_pattern, text))  # ['0xFF', '0x00', '0x1A2B']

# ---------- Password Validation ----------
# Check if password meets rules (must combine multiple patterns):
# Rule: at least 8 chars, one uppercase, one lowercase, one digit, one special char

password = "MyP@ssw0rd"
rules = [
    (r".{8,}",         "at least 8 characters"),
    (r"[A-Z]",         "uppercase letter"),
    (r"[a-z]",         "lowercase letter"),
    (r"\\d",            "digit"),
    (r"[!@#$%^&*(),.?\\":{}|<>_]", "special character"),
]

for pattern, desc in rules:
    if re.search(pattern, password):
        print(f"[PASS] {desc}")
    else:
        print(f"[FAIL] {desc}")

# Single-pattern password validation (full match):
password_pattern = re.compile(r"""
    ^
    (?=.*[A-Z])        # at least one uppercase
    (?=.*[a-z])        # at least one lowercase
    (?=.*\\d)           # at least one digit
    (?=.*[!@#$%^&*])   # at least one special char
    .{8,}              # at least 8 characters total
    $
""", re.VERBOSE)

print(password_pattern.match("MyP@ssw0rd"))  # <re.Match...>
print(password_pattern.match("weak"))        # None

# ---------- Whitespace Stripping ----------
# Strip leading whitespace
text = "   hello   "
print(re.sub(r"^\\s+", "", text))    # 'hello   '

# Strip trailing whitespace
print(re.sub(r"\\s+$", "", text))    # '   hello'

# Strip both
print(re.sub(r"^\\s+|\\s+$", "", text))  # 'hello'

# Normalize multiple spaces to one
text = "hello    world    python"
print(re.sub(r"\\s+", " ", text))  # 'hello world python'

# ---------- HTML Tag Stripping (basic) ----------
html = "<div><p>Hello <b>world</b>!</p></div>"
strip = re.sub(r"<[^>]*>", "", html)
print(strip)  # 'Hello world!'

# More careful: strip tags but keep content
html = '<a href="link">Click here</a> for <span class="info">more</span>'
strip = re.sub(r"<[^>]*>", "", html)
print(strip)  # 'Click here for more'

# ---------- Extracting All Numbers from Text ----------
text = "Order #42: 100 units at $19.99 each, total $1,999.00"
numbers = re.findall(r"\\d+\\.?\\d*", text)
print(numbers)  # ['42', '100', '19.99', '1', '999.00'] (1,999 split due to comma)

# Better: handle commas in numbers
text = "Total: 1,999.00 and 42 and 3.14"
nums = re.findall(r"\\d{1,3}(?:,\\d{3})*(?:\\.\\d+)?|\\d+\\.\\d+|\\d+", text)
print(nums)  # ['1,999.00', '42', '3.14']

# ---------- Extract Domain from URL ----------
urls = "https://www.example.com/path http://test.org/page"
pattern = r"https?://(?:www\\.)?([^/\\s]+)"
matches = re.findall(pattern, urls)
print(matches)  # ['example.com', 'test.org']

# ---------------------------------------------------------------------------
# 13. ADVANCED PATTERNS
# ---------------------------------------------------------------------------

# ---------- Backreferences: Finding Repeated Words ----------
text = "this this is a test test of repeated word word patterns"
pattern = r"(\\w+) \\1"  # word repeated after a space
print(re.findall(pattern, text))  # ['this', 'test', 'word']

# Case-insensitive repeated word
text = "This this is a test Test"
pattern = r"(?i)(\\w+) \\1"
match = re.search(pattern, text)
print(match.group())  # 'This this'

# Backreferences in substitution: fixing repeated words
text = "this this is is a test"
fixed = re.sub(r"\\b(\\w+) \\1\\b", r"\\1", text)
print(fixed)  # 'this is a test'

# ---------- Recursive Patterns (not in re module) ----------
# Python's built-in re module does NOT support recursive patterns.
# For recursive matching (e.g., nested parentheses, balanced HTML tags),
# you need the third-party \\\`regex\\\` module:
#
#   pip install regex
#
# Example with regex module (not available in standard re):
#
#   import regex
#   pattern = regex.compile(r"\\((?:[^()]++|(?R))*+\\)")
#   matches = pattern.findall("((a+b) * (c+d)) / 2")
#   print(matches)  # ['((a+b) * (c+d))']

# ---------- Balancing Groups ----------
# Some regex engines support balancing groups (.NET, PCRE) to match
# balanced pairs. Python's re does NOT support this natively.
#
# Workaround for simple balanced pairs using recursion or manual counting:
def find_balanced_pairs(text, open_bracket="(", close_bracket=")"):
    """Find text within balanced parentheses using basic counting."""
    results = []
    start = None
    depth = 0
    for i, char in enumerate(text):
        if char == open_bracket:
            if depth == 0:
                start = i
            depth += 1
        elif char == close_bracket:
            depth -= 1
            if depth == 0 and start is not None:
                results.append(text[start:i+1])
                start = None
    return results

text = "(a + (b * c) + (d / e))"
print(find_balanced_pairs(text))  # ['(a + (b * c) + (d / e))']
# Only the outermost match because inner ones close before outer
# Better with recursive approach or regex module

# ---------- Conditional Patterns ----------
# Python's re module does NOT support conditional patterns like:
#   (?(condition)yes-pattern|no-pattern)
#
# This is a PCRE/Perl feature. Workaround: use multiple patterns.
#
# Example: match US vs UK spellings using alternation instead
text = "color colour flavor flavour"
# Match either: "color", "colour", "flavor", or "flavour"
pattern = r"colou?r|flavou?r"
print(re.findall(pattern, text))  # ['colour', 'color', 'flavour', 'flavor']
# Wait, that matched all four... let me verify
# "colou?r" matches "color" and "colour"
# "flavou?r" matches "flavor" and "flavour"
# So all four would be found. Good.

# Workaround for "if group captured" scenario using two separate patterns:
def conditional_match(text):
    """Match differently based on presence of a prefix."""
    # Pattern 1: with prefix
    match = re.search(r"prefix_(abc|def)", text)
    if match:
        return f"Has prefix, matched: {match.group(1)}"
    # Pattern 2: without prefix
    match = re.search(r"^abc|def$", text)
    if match:
        return f"No prefix, matched: {match.group()}"
    return None

print(conditional_match("prefix_abc_test"))  # 'Has prefix, matched: abc'
print(conditional_match("abc_test"))         # 'No prefix, matched: abc'

# ---------------------------------------------------------------------------
# 14. PERFORMANCE & BEST PRACTICES
# ---------------------------------------------------------------------------

# ---------- Compile Patterns Used Repeatedly ----------
# DON'T: re-parsing every call
for i in range(1000):
    re.search(r"\\d+\\.\\d+", f"value {i}.{i}")  # pattern compiled 1000 times

# DO: compile once
pattern = re.compile(r"\\d+\\.\\d+")
for i in range(1000):
    pattern.search(f"value {i}.{i}")  # compiled once, reused 1000 times

# ---------- Always Use Raw Strings r"..." ----------
# Without raw string, you need double escaping
# BAD:
pattern = "\\\\d+\\\\.\\\\d+"  # Python sees \\\\d -> \\d, \\\\. -> \\.

# GOOD:
pattern = r"\\d+\\.\\d+"  # Regex sees exactly what you wrote

# Even worse — what if you forget?
# pattern = "\\d+\\.\\d+"  # \\d -> literal d, \\. -> literal .
# This would match "d+.d+" not digits!

# ---------- Be Specific in Character Classes ----------
# BAD: too broad
pattern = r".*"  # matches everything — often not what you want

# BETTER: be specific
pattern = r"[a-zA-Z0-9]+"  # exactly what you need

# BAD: using .* when you know the character range
html_pattern = r"<div>(.*)</div>"  # greedy, matches too much

# BETTER: be specific about what's inside
html_pattern = r"<div>([^<]*)</div>"  # matches non-< characters

# ---------- Avoid Catastrophic Backtracking ----------
# WARNING: This pattern can cause severe performance issues with long strings:
#   r"(a+)+b"  on "aaaaaaaaaaaaaaaaaaaaaaaaac"
#
# Why it breaks:
#   (a+)+ creates nested quantifiers.
#   When "b" fails to match, the engine tries every possible way to split
#   the a's into groups before giving up.
#   For N characters, it tries ~2^N combinations.
#   With 30 a's: about 1 billion attempts. With 100 a's: literally impossible.

# Bad — catastrophic backtracking risk:
bad_pattern = r"(a+)+b"

# Bad — another common pattern:
bad_url = r"https?://([^\\s]+)+"  # nested quantifiers on [^\\s]+

# Bad — (.*)* or (.+)* patterns:
bad_any = r"(.*)*b"  # DON'T DO THIS

# Safe alternatives:
# Remove nesting:
safe_pattern = r"a+b"     # explicit
safe_url = r"https?://\\S+"  # simpler, no nesting

# Use atomic groups or possessive quantifiers if supported (regex module only)
# Python's re doesn't support these; use the \\\`regex\\\` module if needed

# Use re.DOTALL with caution — * and + will match everything including newlines
# and can create backtracking issues with large texts

# ---------- Use re.VERBOSE for Complex Patterns ----------
# BAD: unreadable one-liner
complex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

# GOOD: readable with VERBOSE and comments
email_verbose = re.compile(r"""
    ^                              # start of string
    [a-zA-Z0-9._%+-]+              # local part
    @                              # literal @ symbol
    [a-zA-Z0-9.-]+                 # domain name
    \\.                             # literal dot
    [a-zA-Z]{2,}                   # top-level domain (at least 2 chars)
    $                              # end of string
""", re.VERBOSE)

# ---------- re.search vs re.match ----------
# Use re.search when you want to find a pattern ANYWHERE in the string
# Use re.match when the pattern MUST start at position 0

text = "The code is 12345"

# search finds anywhere:
print(re.search(r"\\d+", text))  # <re.Match...> (finds 12345)

# match only at start:
print(re.match(r"\\d+", text))   # None (text starts with "The", not digits)

# If you want "at start" behavior, use re.match.
# Otherwise, use re.search — it's what most people actually want.

# ---------- Use Non-Capturing Groups When You Don't Need the Capture ----------
# BAD: capturing when you don't need it
pattern = r"(ha)+"  # captures group 1, even if we don't need it
match = re.search(pattern, "haha")
print(match.groups())  # ('ha',) — stored even if unused

# GOOD: non-capturing
pattern = r"(?:ha)+"  # groups for quantifier, no capture
match = re.search(pattern, "haha")
print(match.groups())  # () — empty, no capture overhead

# Performance difference: non-capturing groups use less memory and are faster
# because the engine doesn't need to store the matched substring.

# ---------- Additional Performance Tips ----------
# 1. Use specific character classes instead of .*
#    r"[a-z]+" is faster than r".*" and more precise

# 2. Anchor when possible — ^ and $ help the engine fail faster
#    r"^abc" can immediately reject strings not starting with "abc"

# 3. Use finditer instead of findall for large texts
#    finditer returns a lazy iterator; findall builds the full list

# 4. Use raw strings — always. No exceptions.

# 5. Test your patterns with re.DEBUG flag:
try:
    re.compile(r"(\\w+)@(\\w+)\\.(\\w+)", re.DEBUG)
except re.error:
    pass  # DEBUG is internal, output varies by Python version
# Better: use regex101.com or similar online testers

# 6. For simple string operations, don't use regex:
#    str.startswith(), str.endswith(), str.find(), str.split(), str.strip()
#    are all faster than their regex equivalents for simple patterns.

# 7. Pre-compile patterns used in loops, inside functions called frequently.
#    Use functools.lru_cache or module-level constants.

# ---------- Quick Decision Guide ----------
# Which method to use?
#
# Method         | Returns           | Use when
# ---------------+-------------------+------------------------------
# re.search()    | Match or None     | Find anywhere in string
# re.match()     | Match or None     | Must match at start
# re.fullmatch() | Match or None     | Must match entire string
# re.findall()   | List of strings   | All matches as text
# re.finditer()  | Iterator of Match | All matches with positions
# re.sub()       | String            | Find and replace
# re.subn()      | (str, int)        | Replace with count
# re.split()     | List of strings   | Split on pattern
# re.compile()   | Pattern object    | Reuse pattern many times

# When to use raw strings?
#   r"..." — ALWAYS for regex patterns.
#   Exception: when you want \\n, \\t etc. to be interpreted by Python.
#   But even then, use r"..." with explicit \\n if needed: r"\\d+\\n" is fine.

# ---------- Summary ----------
# Regex is a powerful but complex tool. Start simple, use VERBOSE for complex
# patterns, test incrementally, and always use raw strings.
#
# Remember:
#   - Greedy quantifiers try to match as much as possible, then backtrack
#   - Lazy quantifiers try to match as little as possible, then expand
#   - Lookaround asserts position without consuming characters
#   - Groups capture for extraction and backreferencing
#   - Flags change matching behavior globally or inline
#   - Compile patterns you reuse frequently
#   - Avoid nested quantifiers that cause catastrophic backtracking
#   - Test your patterns with sample data before relying on them
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

interface SyntaxDocSection {
    title: string;
    lines: string[];
}

const SYNTAX_SECTION_STYLES: Record<string, { border: string; bg: string; title: string; dot: string }> = {
    SYNTAX: {
        border: 'border-[#3b82f6]/35',
        bg: 'bg-[#3b82f6]/10',
        title: 'text-[#93c5fd]',
        dot: 'bg-[#3b82f6]'
    },
    'EVALUATION ORDER': {
        border: 'border-[#FF9700]/35',
        bg: 'bg-[#FF9700]/10',
        title: 'text-[#fbbf24]',
        dot: 'bg-[#FF9700]'
    },
    'EXECUTION ORDER': {
        border: 'border-[#22c55e]/35',
        bg: 'bg-[#22c55e]/10',
        title: 'text-[#86efac]',
        dot: 'bg-[#22c55e]'
    },
    'EXECUTION FLOW': {
        border: 'border-[#8b5cf6]/35',
        bg: 'bg-[#8b5cf6]/10',
        title: 'text-[#c4b5fd]',
        dot: 'bg-[#8b5cf6]'
    }
};

const cleanSyntaxLine = (line: string) => {
    const withoutComment = line.replace(/^\s*#\s?/, '');
    return withoutComment.replace(/^"""\s*|\s*"""$/g, '').trimEnd();
};

const parseSyntaxDocumentation = (content: string): SyntaxDocSection[] => {
    const sections: SyntaxDocSection[] = [];
    let current: SyntaxDocSection | null = null;

    for (const rawLine of content.split('\n')) {
        const line = cleanSyntaxLine(rawLine);
        const trimmed = line.trim();

        if (!trimmed || /^Problem\s+\d+:?$/i.test(trimmed)) {
            continue;
        }

        const heading = trimmed.replace(/:$/, '').toUpperCase();
        if (Object.prototype.hasOwnProperty.call(SYNTAX_SECTION_STYLES, heading)) {
            current = { title: heading, lines: [] };
            sections.push(current);
            continue;
        }

        if (!current) {
            current = { title: 'OVERVIEW', lines: [] };
            sections.push(current);
        }
        current.lines.push(line);
    }

    return sections.filter(section => section.lines.some(line => line.trim()));
};

function SyntaxDocumentationPanel({ content }: { content: string }) {
    const sections = useMemo(() => parseSyntaxDocumentation(content), [content]);

    return (
        <div className="space-y-3 p-3 text-xs text-gray-200">
            {sections.map(section => {
                const style = SYNTAX_SECTION_STYLES[section.title] ?? {
                    border: 'border-[#1d2d44]',
                    bg: 'bg-[#071225]',
                    title: 'text-gray-200',
                    dot: 'bg-gray-400'
                };
                return (
                    <section key={section.title} className={`rounded-2xl border ${style.border} ${style.bg} p-3 shadow-lg`}>
                        <h3 className={`mb-3 flex items-center gap-2 text-[11px] font-black uppercase tracking-[0.16em] ${style.title}`}>
                            <span className={`h-2 w-2 rounded-full ${style.dot}`} />
                            {section.title.replace('EVALUATION ORDER', 'Evaluation Order').replace('EXECUTION ORDER', 'Execution Order').replace('EXECUTION FLOW', 'Execution Flow').replace('SYNTAX', 'Syntax')}
                        </h3>
                        <div className="space-y-1.5">
                            {section.lines.map((line, index) => {
                                const trimmed = line.trim();
                                const isCode = /^[A-Za-z_][\w.]*\(|^(def|class|if|for|while|return|print|import|from)\b|^[A-Za-z_]\w*\s*=/.test(trimmed);
                                const isFlow = trimmed.startsWith('→') || trimmed.startsWith('def blocks') || trimmed.startsWith('Execution starts');
                                return (
                                    <div
                                        key={`${section.title}-${index}`}
                                        className={isCode
                                            ? 'rounded-lg border border-[#1d2d44] bg-[#050c18]/85 px-3 py-2 font-mono text-[11px] leading-relaxed text-[#e5e7eb]'
                                            : isFlow
                                                ? 'rounded-lg bg-black/20 px-3 py-2 font-mono text-[11px] leading-relaxed text-[#d8b4fe]'
                                                : 'leading-relaxed text-gray-300'}
                                    >
                                        {trimmed}
                                    </div>
                                );
                            })}
                        </div>
                    </section>
                );
            })}
        </div>
    );
}

type AiTextPart =
    | { type: 'text'; value: string }
    | { type: 'code'; value: string };

const parseAiTextParts = (text: string): AiTextPart[] => {
    const parts: AiTextPart[] = [];
    const fencePattern = /```(?:python|py)?\s*([\s\S]*?)```/gi;
    let lastIndex = 0;
    let match: RegExpExecArray | null;

    while ((match = fencePattern.exec(text)) !== null) {
        if (match.index > lastIndex) {
            parts.push({ type: 'text', value: text.slice(lastIndex, match.index) });
        }
        parts.push({ type: 'code', value: match[1].trim() });
        lastIndex = fencePattern.lastIndex;
    }

    if (lastIndex < text.length) {
        parts.push({ type: 'text', value: text.slice(lastIndex) });
    }

    return parts.filter(part => part.value.trim());
};

const looksLikePythonCode = (text: string) => {
    const trimmed = text.trim();
    const lines = trimmed.split('\n').map(line => line.trim()).filter(Boolean);
    if (lines.length === 0) return false;
    const codeLines = lines.filter(line => (
        /^(def|class|return|if|elif|else:|for|while|try:|except|finally:|with|import|from|print\s*\(|raise\b|yield\b|pass\b|break\b|continue\b)\b/.test(line)
        || /^[A-Za-z_]\w*\s*(?:=|\+=|-=|\*=|\/=|%=|\/\/=|\*\*=)/.test(line)
        || /^[A-Za-z_]\w*\s*\(.*\)\s*$/.test(line)
        || /^\s{2,}\S/.test(line)
    ));
    return codeLines.length >= Math.max(1, Math.ceil(lines.length * 0.35));
};

const isSolutionHeading = (line: string) => /^#\s*(Using|Script|Direct|Built|Manual|Alternative|Try|Another|Equivalent|Convert|Modify|Consider)\b/i.test(line.trim());

const normalizeSolutionHeadings = (solution: string) => {
    const lines = solution.split('\n');
    const normalized = [...lines];

    for (let index = 0; index < lines.length; index += 1) {
        const heading = lines[index].trim();
        if (!/^#\s*Using function approach\b/i.test(heading)) continue;

        const body: string[] = [];
        for (let next = index + 1; next < lines.length; next += 1) {
            if (isSolutionHeading(lines[next])) break;
            body.push(lines[next]);
        }

        const bodyText = body.join('\n');
        if (!/\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(bodyText) && !/\bclass\s+[A-Za-z_][A-Za-z0-9_]*\b/.test(bodyText)) {
            normalized[index] = lines[index].replace(/Using function approach/i, 'Using script approach');
        }
    }

    return normalized.join('\n');
};

const getInlinePythonTokenColor = (token: string, editorColors: EditorColorSettings) => {
    if (/^#/.test(token)) return editorColors.comment;
    if (/^(['"]).*\1$/.test(token)) return editorColors.string;
    if (/^\d+(?:\.\d+)?$/.test(token)) return editorColors.number;
    if (PYTHON_KEYWORDS.includes(token)) return editorColors.keyword;
    if (PYTHON_BUILTINS.includes(token)) return editorColors.builtin;
    if (/^[A-Za-z_][A-Za-z0-9_]*$/.test(token)) return editorColors.identifier;
    return '#e5e7eb';
};

const renderInlinePythonCode = (code: string, editorColors: EditorColorSettings, keyPrefix: string) => {
    const tokens = code.match(/#[^\n]*|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|\b\d+(?:\.\d+)?\b|\b[A-Za-z_][A-Za-z0-9_]*\b|\s+|./g) || [code];
    return (
        <code className="rounded-md border border-[#1d2d44] bg-[#050c18]/80 px-1.5 py-0.5 font-mono text-[0.92em]">
            {tokens.map((token, index) => (
                <span key={`${keyPrefix}-${index}`} style={{ color: /^\s+$/.test(token) ? undefined : getInlinePythonTokenColor(token, editorColors) }}>
                    {token}
                </span>
            ))}
        </code>
    );
};

const renderAiParagraphText = (text: string, editorColors: EditorColorSettings, keyPrefix: string) => {
    const parts = text.split(/(`[^`]+`)/g).filter(Boolean);
    return parts.map((part, index) => {
        if (part.startsWith('`') && part.endsWith('`')) {
            return renderInlinePythonCode(part.slice(1, -1), editorColors, `${keyPrefix}-code-${index}`);
        }
        return <React.Fragment key={`${keyPrefix}-text-${index}`}>{part}</React.Fragment>;
    });
};

interface GuideSection {
    title: string;
    tone: 'goal' | 'requirements' | 'steps' | 'hints';
    lines: string[];
}

const normalizeGuideLine = (line: string) => line
    .replace(/^\s*\d+[.)]\s*/, '')
    .replace(/^\s*[-*]\s*/, '')
    .replace(/\s+/g, ' ')
    .trim();

const extractGuideExamples = (description: string) => {
    const lines = description.split('\n').map(line => line.trim()).filter(Boolean);
    const examples: string[] = [];
    let inExamples = false;
    for (const line of lines) {
        if (/^examples?:/i.test(line)) {
            inExamples = true;
            const inline = line.replace(/^examples?:\s*/i, '').trim();
            if (inline) examples.push(inline);
            continue;
        }
        if (inExamples && /(→|->|=>)/.test(line)) {
            examples.push(line);
        }
    }
    return examples.slice(0, 3);
};

const extractFunctionSignatures = (initialCode: string) => {
    const signatures: string[] = [];
    const seen = new Set<string>();
    const regex = /^\s*def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)\s*:/gm;
    let match: RegExpExecArray | null;
    while ((match = regex.exec(initialCode)) !== null) {
        const signature = `def ${match[1]}(${match[2].trim()}):`;
        if (!seen.has(signature)) {
            seen.add(signature);
            signatures.push(signature);
        }
    }
    return signatures;
};

const extractClassNames = (initialCode: string) => {
    const classNames: string[] = [];
    const seen = new Set<string>();
    const regex = /^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)/gm;
    let match: RegExpExecArray | null;
    while ((match = regex.exec(initialCode)) !== null) {
        if (!seen.has(match[1])) {
            seen.add(match[1]);
            classNames.push(match[1]);
        }
    }
    return classNames;
};

const getGuideConceptHints = (exercise: Exercise) => {
    const text = `${exercise.description}\n${exercise.initialCode}`.toLowerCase();
    const hints: string[] = [];
    const add = (condition: boolean, hint: string) => {
        if (condition && !hints.includes(hint)) hints.push(hint);
    };
    add(text.includes('input(') || text.includes('prompt the user'), 'If the problem asks for user input, read it with `input()` and convert it with `int()`, `float()`, or `.split()` before using it.');
    add(text.includes('return'), 'If the problem says “returns”, use `return`, not only `print()`. Printing can look correct but fail function tests.');
    add(text.includes('print'), 'If the problem says “print”, make sure the visible output format matches the example line by line.');
    add(text.includes('list'), 'For list problems, check whether you should return a new list, a number from the list, or a filtered list.');
    add(text.includes('dictionary') || text.includes('dict'), 'For dictionary problems, be clear whether the task needs keys, values, items, or a new dictionary.');
    add(text.includes('string'), 'For string problems, watch spaces, uppercase/lowercase, and whether the result should be a string, list, or boolean.');
    add(text.includes('while loop'), 'Because the problem asks for a `while` loop, use a counter and update it inside the loop so it does not run forever.');
    add(text.includes('for loop'), 'Because the problem asks for a `for` loop, iterate over the range or collection directly instead of hard-coding the answer.');
    add(text.includes('and operator'), 'For `and`, every condition must be true. Test at least one case where each condition fails.');
    add(text.includes('or operator'), 'For `or`, one true condition is enough. Also test a case where all conditions are false.');
    add(text.includes('class '), 'For class problems, define `__init__`, store attributes with `self`, and create methods only if the prompt asks for them.');
    add(text.includes('recursion'), 'For recursion, write a base case first, then make the recursive call move closer to that base case.');
    return hints.slice(0, 5);
};

const getSpecificGuideGoal = (exercise: Exercise, promptLine: string) => {
    const text = `${exercise.description}\n${exercise.initialCode}`.toLowerCase();
    if (/parse\s+a?\s*boolean|boolean\s+from\s+a\s+string/.test(text)) {
        return [
            'Convert text such as `"True"` or `"False"` into the real Python boolean values `True` or `False`.',
            'Do not use `bool(text)` for this task: `bool("False")` is still `True` because non-empty strings are truthy.',
            'Normalize the text with `.strip().lower()`, then compare it to accepted true words like `"true"`.',
        ];
    }
    if (/convert .*string.*(integer|int)|parse .*integer|integer from a string/.test(text)) {
        return ['Turn numeric text into an actual integer value using `int()`, then use or print that number as requested.'];
    }
    if (/convert .*string.*float|parse .*float|float from a string/.test(text)) {
        return ['Turn decimal text into an actual floating-point number using `float()`, then use or print that number as requested.'];
    }
    if (/reverse.*string/.test(text)) {
        return ['Create the same string in reverse order. The first character becomes last, and the last character becomes first.'];
    }
    if (/reverse.*list/.test(text)) {
        return ['Create a new list with elements in reverse order — last element first, first element last.'];
    }
    if (/palindrome/.test(text)) {
        return ['Check whether the value reads the same forward and backward. Usually you compare the cleaned value with its reverse.'];
    }
    if (/count.*vowel/.test(text)) {
        return ['Count only vowel characters (`a`, `e`, `i`, `o`, `u`) in the input, usually ignoring case.'];
    }
    if (/sum.*values.*dictionary|sum of all values in a dictionary/.test(text)) {
        return ['Add together the numeric values stored inside the dictionary, not the keys.'];
    }
    if (/reverse.*keys.*values|keys and values in a dictionary/.test(text)) {
        return ['Build a new dictionary where each original value becomes a key and each original key becomes its value.'];
    }
    if (/maximum value in a dictionary|max value/.test(text)) {
        return ['Find the largest number among the dictionary values. The keys are only labels; compare the values.'];
    }
    if (/perfect square.*perfect cube/.test(text)) {
        return ['Check two possibilities: whether the number is a perfect square or whether it is a perfect cube. Return true if either test passes.'];
    }
    if (/divisible/.test(text)) {
        return ['Use the remainder operator `%`. A number is divisible by another number when the remainder is `0`.'];
    }
    if (/between|range/.test(text)) {
        return ['Check the lower boundary and the upper boundary separately, then combine those comparisons as the prompt says.'];
    }
    return [promptLine];
};

const getSpecificGuideSteps = (exercise: Exercise, fallbackLines: string[]) => {
    const text = `${exercise.description}\n${exercise.initialCode}`.toLowerCase();
    if (/parse\s+a?\s*boolean|boolean\s+from\s+a\s+string/.test(text)) {
        return [
            'Start with the string value, for example `value = "True"`.',
            'Clean the input with `value.strip().lower()` so `" TRUE "` and `"true"` are treated the same.',
            'Compare the cleaned string to `"true"` to produce a real boolean result.',
            'Print or return the boolean result, so the output is `True` or `False` without quotes.',
        ];
    }
    if (/substring|slice.*(?:from|extract)/.test(text)) {
        return [
            'Identify the string parameter and the start/end index parameters from the function signature.',
            'Use slicing: `text[start:end]` extracts characters from `start` up to (not including) `end`.',
            'Python slicing is forgiving — if `end` is beyond the string length, no error occurs.',
            'Return the extracted substring.',
        ];
    }
    if (/replace.*char(?:acter)?/.test(text)) {
        return [
            'Identify the `text`, `old_char`, and `new_char` parameters.',
            'Call `text.replace(old_char, new_char)` — this replaces all occurrences.',
            'The `.replace()` method returns a NEW string; it does not modify the original.',
            'Return the new string directly.',
        ];
    }
    if (/remove.*char(?:acter)?/.test(text)) {
        return [
            'Identify the `text` and `char` parameters.',
            'Call `text.replace(char, "")` to replace the character with an empty string, removing it.',
            'This removes ALL occurrences of the character, not just the first one.',
            'Return the cleaned string.',
        ];
    }
    if (/reverse/.test(text)) {
        if (/list/.test(text)) return [
            'Use slicing `my_list[::-1]` to create a new list in reverse order.',
            '`.reverse()` modifies in-place and returns `None` — avoid it here.',
            'Return the reversed list.',
        ];
        if (/string/.test(text)) return [
            'Use slicing `text[::-1]` to reverse the string.',
            'Strings have no `.reverse()` method — slicing is the way.',
            'Return the reversed string.',
        ];
    }
    if (/len(?:gth)?/.test(text) && /list/.test(text)) {
        return [
            'Call `len(my_list)` directly on the list parameter.',
            '`len()` works on any iterable — no loop needed.',
            'Return the integer result.',
        ];
    }
    if (/\b(?:check|return).*(?:if|whether).*(?:in the list|contain|present|exist|member)\b/.test(text)) {
        return [
            'Use `element in my_list` to test membership. The `in` operator returns a boolean.',
            'Return the result directly — no `if True return True else return False` needed.',
        ];
    }
    if (/\bhow many\b[\s\S]*?\b(?:time|appear)\w*\b|\bfrequency\b/.test(text)) {
        return [
            'Call `.count(element)` on the list to count how many times it appears.',
            '`.count()` returns 0 if the element never appears — no separate check needed.',
            'Return the integer count.',
        ];
    }
    if (/\bindex\b[\s\S]*?\b(?:first|occurrence|position)\b/.test(text)) {
        return [
            'First check `if element in my_list` to avoid a `ValueError` if the element is missing.',
            'If found, use `.index(element)` to get the position of the first occurrence.',
            'If not found, return `-1` (or whatever the problem specifies for "not found").',
        ];
    }
    if (/(?:even|odd)\s+number/.test(text) || /filter (?:even|odd)/.test(text) || /only the (?:even|odd)/.test(text)) {
        const even = /even/.test(text);
        const condition = even ? 'x % 2 == 0' : 'x % 2 != 0';
        return [
            `Use a list comprehension: \`[x for x in numbers if ${condition}]\`.`,
            `This filters the list to keep only ${even ? 'even' : 'odd'} numbers.`,
            'Return the filtered list.',
        ];
    }
    if (/palindrome/.test(text)) {
        return [
            'Compare the input to its reverse: `text == text[::-1]`.',
            'If equal, it is a palindrome (return `True`); otherwise return `False`.',
            'Be careful about case — use `.lower()` if case should be ignored.',
        ];
    }
    if (/prime/.test(text)) {
        return [
            'Numbers less than 2 are not prime.',
            'Check divisors from 2 up to `int(sqrt(n))` using `%` operator.',
            'If any divisor divides evenly, the number is not prime.',
            'Return the boolean result.',
        ];
    }
    if (/sort(?:ed)?\b/.test(text)) {
        return [
            'Call `sorted()` on the input to get a new sorted list (original stays unchanged).',
            '`.sort()` sorts in-place and returns `None` — prefer `sorted()`.',
            'Return the sorted result.',
        ];
    }
    if (/factorial/.test(text)) {
        return [
            'Use a loop from 1 to n, multiplying each number into a running product.',
            'Or use `math.factorial(n)` from the math module.',
            'Return the factorial result.',
        ];
    }
    if (/capitalize/.test(text)) {
        return [
            'Call `.capitalize()` on the string — makes first char uppercase, rest lowercase.',
            'Return the capitalized string.',
        ];
    }
    if (/upper(?:case)?/.test(text)) {
        return [
            'Call `.upper()` on the string — converts all characters to uppercase.',
            'Return the uppercased string.',
        ];
    }
    if (/lower(?:case)?/.test(text)) {
        return [
            'Call `.lower()` on the string — converts all characters to lowercase.',
            'Return the lowercased string.',
        ];
    }
    if (/set|union|intersection|difference/.test(text)) {
        return [
            'Convert lists to sets using `set()` for set operations.',
            'Use `|` for union, `&` for intersection, `-` for difference.',
            'Convert the result back to a list if needed.',
            'Return the result.',
        ];
    }
    if (/dictionary|dict/.test(text)) {
        if (/invert|reverse|swap|key.*value|value.*key/.test(text)) return [
            'Iterate over `d.items()` to access each key-value pair.',
            'Build a new dictionary where each value becomes a key and each key becomes its value.',
            'Return the inverted dictionary.',
        ];
        if (/merge|combine|update/.test(text)) return [
            'Use `{**dict1, **dict2}` or `.update()` to merge the dictionaries.',
            'Return the merged dictionary.',
        ];
        return [
            'Use `.get(key, default)` for safe dictionary access.',
            'Iterate with `.items()` when you need both keys and values.',
            'Return the result.',
        ];
    }
    return fallbackLines;
};

const getSpecificGuideHints = (exercise: Exercise) => {
    const text = `${exercise.description}\n${exercise.initialCode}`.toLowerCase();
    if (/parse\s+a?\s*boolean|boolean\s+from\s+a\s+string/.test(text)) {
        return [
            '`bool("False")` is a trap: it returns `True` because the string is not empty.',
            'Use comparison instead: `text.strip().lower() == "true"`.',
            'The result should be a boolean value, not the string `"True"`.',
        ];
    }
    if (/substring|slice/.test(text)) {
        return ['Slicing with `[start:end]` does NOT include `end` index.', 'Negative indices count from the end of the string.'];
    }
    if (/replace.*char/.test(text)) {
        return ['`.replace()` replaces ALL occurrences, not just the first.', 'It returns a new string — the original is unchanged.'];
    }
    if (/reverse/.test(text) && /string/.test(text)) {
        return ['Strings have no `.reverse()` — use `[::-1]` slicing.', '`.reverse()` only exists for lists.'];
    }
    if (/reverse/.test(text) && /list/.test(text)) {
        return ['`.reverse()` modifies in-place and returns `None`.', 'Use `[::-1]` slicing to get a reversed copy.'];
    }
    if (/\b(?:check|test|return).*(?:if|whether).*(?:in the list|contain|present)\b/.test(text)) {
        return ['The `in` operator returns a boolean — use it directly.', 'Avoid `if element in list: return True else: return False` — just `return element in list`.'];
    }
    if (/\bhow many\b[\s\S]*?\b(?:time|appear)\w*\b|\bfrequency\b/.test(text)) {
        return ['`.count(element)` returns 0 if element is missing — no extra check needed.', 'It counts ALL occurrences, not just the first one.'];
    }
    if (/\bindex\b[\s\S]*?\b(?:first|occurrence|position)\b/.test(text)) {
        return ['`.index(element)` raises `ValueError` if not found — guard with `in` first.', 'It finds only the FIRST occurrence.'];
    }
    if (/(?:even|odd)\s+number/.test(text) || /filter (?:even|odd)/.test(text)) {
        return ['Use `x % 2 == 0` for even, `x % 2 != 0` for odd.', 'A list comprehension is cleaner than a manual loop.'];
    }
    if (/palindrome/.test(text)) {
        return ['`text == text[::-1]` is all you need.', 'Consider whether case matters — use `.lower()` if not.'];
    }
    if (/prime/.test(text)) {
        return ['Only check divisors up to `sqrt(n)`.', 'Numbers less than 2 are not prime.'];
    }
    if (/factorial/.test(text)) {
        return ['`0! = 1` — handle this edge case.', 'Use a loop or `math.factorial()`.'];
    }
    if (/sort(?:ed)?\b/.test(text)) {
        return ['`.sort()` returns `None`; `sorted()` returns a new list.', 'Use `sorted()` to keep the original unchanged.'];
    }
    if (/dictionary|dict/.test(text) && /invert|reverse|swap/.test(text)) {
        return ['Dictionary values must be hashable to become keys.', 'If duplicate values exist, the last one wins.'];
    }
    return [];
};

const buildExerciseGuideSections = (exercise: Exercise): GuideSection[] => {
    const descriptionLines = exercise.description.split('\n').map(line => line.trim()).filter(Boolean);
    const promptLine = descriptionLines.find(line => !/^examples?:/i.test(line) && !/(→|->|=>)/.test(line)) ?? exercise.description.trim();
    const signatures = extractFunctionSignatures(exercise.initialCode);
    const classNames = extractClassNames(exercise.initialCode);
    const examples = extractGuideExamples(exercise.description);
    const specificGoalLines = getSpecificGuideGoal(exercise, promptLine);
    const rawBreakdownLines = (exercise.breakdown ?? '')
        .split('\n')
        .map(normalizeGuideLine)
        .filter(Boolean)
        .filter(line => !/^\[?input\(\)\]?$/i.test(line))
        .filter(line => !(specificGoalLines.some(goal => /boolean/i.test(goal)) && /\bbool\(\)/i.test(line)))
        .filter((line, index, arr) => arr.findIndex(item => item.toLowerCase() === line.toLowerCase()) === index)
        .slice(0, 8);
    const stepLines = getSpecificGuideSteps(exercise, rawBreakdownLines.length ? rawBreakdownLines : [
        'Create the required function or script structure first.',
        'Store the input values in clearly named variables.',
        'Apply the operation described in the prompt.',
        'Return or print the final result exactly as requested.',
    ]);
    const conceptHints = getGuideConceptHints(exercise);
    const specificHints = getSpecificGuideHints(exercise);
    const customHint = exercise.hint && !/^check the description for requirements\.?$/i.test(exercise.hint.trim())
        ? exercise.hint.trim()
        : '';

    const requirementLines = [
        signatures.length ? `Use the expected function signature: ${signatures.map(signature => `\`${signature}\``).join(', ')}` : '',
        classNames.length ? `Define the required class${classNames.length > 1 ? 'es' : ''}: ${classNames.map(name => `\`${name}\``).join(', ')}` : '',
        examples.length ? `Match the example behavior: ${examples.map(example => `\`${example}\``).join(' | ')}` : '',
        /return/i.test(promptLine) ? 'The final value should be returned from the function.' : '',
        /print/i.test(promptLine) ? 'The output should be printed in the same format as the example.' : '',
    ].filter(Boolean);

    return [
        {
            title: 'What The Problem Wants',
            tone: 'goal',
            lines: specificGoalLines,
        },
        {
            title: 'Must-Have Requirements',
            tone: 'requirements',
            lines: requirementLines.length ? requirementLines : ['Identify the required inputs, the expected output, and whether the answer should use `return` or `print()`.'],
        },
        {
            title: 'How To Build It',
            tone: 'steps',
            lines: stepLines,
        },
        {
            title: 'Hints To Avoid Mistakes',
            tone: 'hints',
            lines: [customHint, ...specificHints, ...conceptHints].filter(Boolean).slice(0, 6),
        },
    ].filter(section => section.lines.length > 0);
};

const getGuideSectionStyle = (tone: GuideSection['tone']) => {
    switch (tone) {
        case 'goal':
            return { color: '#38bdf8', borderColor: 'rgba(56, 189, 248, 0.28)', backgroundColor: 'rgba(8, 47, 73, 0.24)' };
        case 'requirements':
            return { color: '#FF9700', borderColor: 'rgba(255, 151, 0, 0.30)', backgroundColor: 'rgba(69, 26, 3, 0.22)' };
        case 'steps':
            return { color: '#22c55e', borderColor: 'rgba(34, 197, 94, 0.26)', backgroundColor: 'rgba(20, 83, 45, 0.20)' };
        case 'hints':
            return { color: '#a78bfa', borderColor: 'rgba(167, 139, 250, 0.26)', backgroundColor: 'rgba(49, 46, 129, 0.20)' };
        default:
            return { color: '#FF9700', borderColor: 'rgba(255, 151, 0, 0.26)', backgroundColor: 'rgba(8, 18, 34, 0.34)' };
    }
};

const getAiStepTitle = (step: string, index: number) => {
    const normalized = step.toLowerCase();
    if (normalized.includes('problem requirement')) return 'Problem Requirement';
    if (normalized.includes('line-by-line') || normalized.includes('code inspection')) return 'Code Check';
    if (normalized.includes('output analysis')) return 'Output Analysis';
    if (normalized.includes('code explanation') || normalized.includes('syntax explanation') || normalized.includes('concept explanation')) return 'Code Explanation';
    if (normalized.includes('expected solution workflow') || normalized.includes('function workflow')) return 'Solution Workflow';
    if (normalized.includes('execution order') || normalized.includes('order of operation')) return 'Execution Order';
    if (normalized.includes('grader') || normalized.includes('mismatch') || normalized.includes('failed') || normalized.includes('rejected')) return 'Result / Error';
    if (normalized.includes('built-in review') || normalized.includes('local model')) return 'Review Status';
    if (normalized.includes('suggested fix') || normalized.includes('what to change')) return 'What To Change';
    return `Review Point ${index + 1}`;
};

const getAiStepTone = (step: string, accentColor: string) => {
    const normalized = step.toLowerCase();
    if (normalized.includes('output analysis')) {
        if (normalized.includes('incorrect')) {
            return {
                color: '#FF1900',
                borderColor: 'rgba(255, 25, 0, 0.38)',
                backgroundColor: 'rgba(127, 29, 29, 0.22)',
            };
        }
        if (normalized.includes('correct')) {
            return {
                color: '#22c55e',
                borderColor: 'rgba(34, 197, 94, 0.38)',
                backgroundColor: 'rgba(20, 83, 45, 0.22)',
            };
        }
    }
    return {
        color: accentColor,
        borderColor: 'rgba(88, 118, 160, 0.22)',
        backgroundColor: 'rgba(8, 18, 34, 0.34)',
    };
};

const splitAiStepParagraphs = (step: string) => {
    const cleaned = step
        .replace(/\s*;\s*(?=step\s+\d+:)/gi, '\n')
        .replace(/\s+(?=step\s+\d+:)/gi, '\n')
        .trim();
    const semicolonParts = cleaned
        .split(/;\s+(?=(?:step\s+\d+:|line\s+\d+|[A-Z]))/i)
        .map(part => part.trim())
        .filter(Boolean);

    if (semicolonParts.length > 2) return semicolonParts;

    return cleaned
        .split(/\n+/)
        .map(part => part.trim())
        .filter(Boolean);
};

const splitAiReviewSteps = (text: string) => {
    const normalized = text
        .replace(/\n\s*---\s*\n/g, '\n\n')
        .replace(/\s+(?=(?:Problem requirement|Line-by-line code inspection|Code inspection|Output analysis|Code explanation|Syntax explanation|Concept explanation|Expected solution workflow|Function workflow|Execution order|Order of operation|The code still contains|The grader\/run system|The local model response|Specific built-in analysis|Built-in analysis|Suggested fix):)/g, '\n\n')
        .replace(/\s+(?=The deterministic grader|A function that reaches|If this is|For this grader)/g, '\n\n')
        .trim();

    const explicitSections = normalized
        .split(/\n\s*\n+/)
        .map(section => section.trim())
        .filter(Boolean);

    if (explicitSections.length > 1) {
        return explicitSections
            .map(section => section.replace(/^\d+[.)]\s*/, '').trim())
            .filter(section => !/^(Specific built-in analysis|Built-in analysis):?$/i.test(section));
    }

    const sentenceSections = normalized
        .split(/(?<=[.!?])\s+(?=[A-Z])/)
        .map(section => section.trim())
        .filter(Boolean);

    return sentenceSections.length > 1 ? sentenceSections : [normalized];
};

function AiReviewText({ text, editorColors, accentColor = '#93c5fd', detectBareCode = false, numbered = false }: { text: string; editorColors: EditorColorSettings; accentColor?: string; detectBareCode?: boolean; numbered?: boolean }) {
    const parts = parseAiTextParts(text);
    const renderCode = (code: string, key: string) => (
        <div key={key} className="my-2 overflow-hidden rounded-xl border" style={{ borderColor: 'rgba(88, 118, 160, 0.28)', backgroundColor: 'rgba(5, 12, 24, 0.72)' }}>
            <div className="border-b px-3 py-1 text-[10px] font-black uppercase tracking-[0.14em]" style={{ borderColor: 'rgba(88, 118, 160, 0.16)', color: accentColor }}>
                Python
            </div>
            <CodeMirror
                value={code}
                height="auto"
                readOnly={true}
                extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]}
                theme="none"
                basicSetup={{ lineNumbers: true, foldGutter: false, highlightActiveLine: false, bracketMatching: true }}
            />
        </div>
    );

    if (detectBareCode && parts.length === 1 && parts[0].type === 'text' && looksLikePythonCode(parts[0].value)) {
        return renderCode(parts[0].value, 'ai-code-only');
    }

    return (
        <div className="space-y-2 text-sm leading-relaxed text-gray-200">
            {parts.map((part, index) => {
                if (part.type === 'code' || (detectBareCode && looksLikePythonCode(part.value))) {
                    return renderCode(part.value, `ai-code-${index}`);
                }
                if (numbered) {
                    const steps = splitAiReviewSteps(part.value);
                    return (
                        <div key={`ai-numbered-${index}`} className="space-y-2.5">
                            {steps.map((step, stepIndex) => {
                                const tone = getAiStepTone(step, accentColor);
                                return (
                                <div key={`ai-step-${index}-${stepIndex}`} className="grid grid-cols-[28px_1fr] gap-2 rounded-xl border p-3" style={{ borderColor: tone.borderColor, backgroundColor: tone.backgroundColor }}>
                                    <div className="flex h-7 w-7 items-center justify-center rounded-full text-[11px] font-black" style={{ backgroundColor: hexToRgba(tone.color, 0.16), color: tone.color }}>
                                        {stepIndex + 1}
                                    </div>
                                    <div className="min-w-0 space-y-2">
                                        <div className="text-[10px] font-black uppercase tracking-[0.16em]" style={{ color: tone.color }}>
                                            {getAiStepTitle(step, stepIndex)}
                                        </div>
                                        <div className="space-y-1.5">
                                            {splitAiStepParagraphs(step).map((paragraph, paragraphIndex, paragraphs) => (
                                                <p key={`ai-step-text-${index}-${stepIndex}-${paragraphIndex}`} className="whitespace-pre-wrap text-gray-200">
                                                    {paragraphs.length > 1 && (
                                                        <span className="mr-2 text-gray-500">•</span>
                                                    )}
                                                    {renderAiParagraphText(paragraph, editorColors, `ai-step-text-${index}-${stepIndex}-${paragraphIndex}`)}
                                                </p>
                                            ))}
                                        </div>
                                    </div>
                                </div>
                                );
                            })}
                        </div>
                    );
                }
                return (
                    <p key={`ai-text-${index}`} className="whitespace-pre-wrap">
                        {renderAiParagraphText(part.value.trim(), editorColors, `ai-text-${index}`)}
                    </p>
                );
            })}
        </div>
    );
}

const renderProblemAiInlineText = (text: string) => {
    const parts = text.split(/(`[^`]+`)/g);
    return parts.map((part, index) => {
        if (part.startsWith('`') && part.endsWith('`')) {
            return (
                <code key={`problem-ai-inline-${index}`} className="rounded-md border px-1.5 py-0.5 text-[0.85em]" style={{ borderColor: 'rgba(96, 165, 250, 0.24)', backgroundColor: 'rgba(15, 23, 42, 0.65)', color: '#bfdbfe' }}>
                    {part.slice(1, -1)}
                </code>
            );
        }
        return <React.Fragment key={`problem-ai-inline-${index}`}>{part}</React.Fragment>;
    });
};

function ProblemAiText({ text, editorColors, accentColor = '#93c5fd' }: { text: string; editorColors: EditorColorSettings; accentColor?: string }) {
    const parts = parseAiTextParts(text);
    const renderCode = (code: string, key: string) => (
        <div key={key} className="my-2 overflow-hidden rounded-xl border" style={{ borderColor: 'rgba(88, 118, 160, 0.28)', backgroundColor: 'rgba(5, 12, 24, 0.72)' }}>
            <div className="border-b px-3 py-1 text-[10px] font-black uppercase tracking-[0.14em]" style={{ borderColor: 'rgba(88, 118, 160, 0.16)', color: accentColor }}>
                Python
            </div>
            <CodeMirror
                value={code}
                height="auto"
                readOnly={true}
                extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]}
                theme="none"
                basicSetup={{ lineNumbers: true, foldGutter: false, highlightActiveLine: false, bracketMatching: true }}
            />
        </div>
    );

    return (
        <div className="space-y-2.5 text-sm leading-relaxed text-gray-200">
            {parts.map((part, index) => {
                if (part.type === 'code' || looksLikePythonCode(part.value)) {
                    return renderCode(part.value, `problem-ai-code-${index}`);
                }

                const sections = part.value
                    .split(/\n\s*\n+/)
                    .map(section => section.trim())
                    .filter(Boolean);

                return (
                    <div key={`problem-ai-text-${index}`} className="space-y-2.5">
                        {sections.map((section, sectionIndex) => {
                            const cleaned = section.replace(/^\d+[.)]\s*/, '').trim();
                            const lines = cleaned.split(/\n+/).map(line => line.trim()).filter(Boolean);
                            return (
                                <div key={`problem-ai-section-${index}-${sectionIndex}`} className="grid grid-cols-[28px_1fr] gap-2 rounded-xl border p-3" style={{ borderColor: hexToRgba(accentColor, 0.24), backgroundColor: 'rgba(8, 18, 34, 0.48)' }}>
                                    <div className="flex h-7 w-7 items-center justify-center rounded-full text-[11px] font-black" style={{ backgroundColor: hexToRgba(accentColor, 0.16), color: accentColor }}>
                                        {sectionIndex + 1}
                                    </div>
                                    <div className="min-w-0 space-y-1.5 text-gray-200">
                                        {lines.map((line, lineIndex) => (
                                            <p key={`problem-ai-line-${index}-${sectionIndex}-${lineIndex}`} className="whitespace-pre-wrap">
                                                {renderProblemAiInlineText(line)}
                                            </p>
                                        ))}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                );
            })}
        </div>
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
    const [files, setFiles] = useState<ProjectFile[]>(() =>
        localStorage.getItem('python_plain_mode') === 'true'
            ? [{ name: 'main.py', content: '' }]
            : [{ name: 'main.py', content: initialExercise.initialCode }]
    );
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
    const [cacheClearBusy, setCacheClearBusy] = useState(false);
    const [loadTime, setLoadTime] = useState<number>(0);
    const [isInFrame, setIsInFrame] = useState(false);
    const [showModal, setShowModal] = useState<'none' | 'instructions' | 'hint' | 'solution' | 'settings' | 'api_key' | 'restart_confirm' | 'delete_confirm' | 'problem_full' | 'customize' | 'stats_by_mode' | 'problem_ai'>('none');
    const countRowLongPressRef = useRef<ReturnType<typeof setTimeout> | null>(null);
    const [modalTab, setModalTab] = useState<'how' | 'cheat' | 'glossary' | 'regex'>('how');
    const [solutionTab, setSolutionTab] = useState<'code' | 'logic' | 'requirements' | 'syntax'>('code');
    const [customizeTab, setCustomizeTab] = useState<CustomizeModalTab>('count');
    const [showHowToUse, setShowHowToUse] = useState(false);
    const [aiHintText, setAiHintText] = useState<string>('');
    const [latestAiReviewRequest, setLatestAiReviewRequest] = useState<AiReviewRequest | null>(null);
    const [latestAiReviewResult, setLatestAiReviewResult] = useState<AiReviewResult | null>(null);
    const [aiReviewRunning, setAiReviewRunning] = useState(false);
    const [problemAiMessages, setProblemAiMessages] = useState<ProblemAiMessage[]>([]);
    const [problemAiDraft, setProblemAiDraft] = useState('');
    const [problemAiRunning, setProblemAiRunning] = useState(false);
    const [problemAiProblemId, setProblemAiProblemId] = useState<number | null>(null);
    const [copyFeedback, setCopyFeedback] = useState(false);
    const [apiKey, setApiKey] = useState<string>(() => {
        return localStorage.getItem('gemini_api_key') || '';
    });
    const [difficultyMode, setDifficultyMode] = useState<DifficultyMode>(() => getSavedDifficultyMode());
    const [countRowColors, setCountRowColors] = useState<CountRowColorSettings>(() => loadColorSettings('python_count_row_colors', DEFAULT_COUNT_ROW_COLORS));
    const [editorColors, setEditorColors] = useState<EditorColorSettings>(() => loadColorSettings('python_editor_colors', DEFAULT_EDITOR_COLORS));
    const [toolPanelColors, setToolPanelColors] = useState<ToolPanelColorSettings>(() => loadToolPanelColorSettings());
    const [panelColors, setPanelColors] = useState<PanelColorSettings>(() => loadPanelColorSettings());
    const [offlineAiState, setOfflineAiState] = useState(() => loadOfflineAiState());
    const [offlineAiNow, setOfflineAiNow] = useState(() => Date.now());
    const offlineAiOperationRef = useRef(0);
    const offlineAiBusy = offlineAiState.status === 'downloading' || offlineAiState.status === 'removing';
    const [keyboardHaptics, setKeyboardHaptics] = useState(() => localStorage.getItem('python_keyboard_haptics') === 'true');
    const [keyboardSound, setKeyboardSound] = useState(() => localStorage.getItem('python_keyboard_sound') === 'true');
    const [resultSound, setResultSound] = useState(() => localStorage.getItem('python_result_sound') !== 'false');
    const [plainMode, setPlainMode] = useState(() => localStorage.getItem('python_plain_mode') === 'true');
    const [logExpanded, setLogExpanded] = useState(false);
    const [showBreakdownFor, setShowBreakdownFor] = useState<number | null>(null);
    const [showSnippetSaveInput, setShowSnippetSaveInput] = useState(false);
    const [snippetNameInput, setSnippetNameInput] = useState('');
    const [savedSnippets, setSavedSnippets] = useState<Array<{ id: number; name: string; content: string; savedAt: string }>>(() => {
        try { return JSON.parse(localStorage.getItem('python_saved_snippets') || '[]'); } catch { return []; }
    });
    const [isOutputExpanded, setIsOutputExpanded] = useState(false);
    const [showActionPanel, setShowActionPanel] = useState(false);
    const [outputHeight, setOutputHeight] = useState(85);
    const [logicContent, setLogicContent] = useState<string>('');
    const [requirementsContent, setRequirementsContent] = useState<string>('');
    const [syntaxContent, setSyntaxContent] = useState<string>('');
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

    const [idLogProblems, setIdLogProblems] = useState<SavedProblem[]>(() => {
        try {
            const raw = localStorage.getItem('python_mastery_id_log');
            return raw ? JSON.parse(raw) : [];
        } catch {
            return [];
        }
    });

    const [expandedSavedProblem, setExpandedSavedProblem] = useState<number | null>(null);
    const [expandedIdLogProblem, setExpandedIdLogProblem] = useState<number | null>(null);
    const [idLogInput, setIdLogInput] = useState('');
    const [deleteConfirmId, setDeleteConfirmId] = useState<number | null>(null);
    const [deleteConfirmType, setDeleteConfirmType] = useState<'saved' | 'idlog' | null>(null);
    const [descCopied, setDescCopied] = useState(false);

    useEffect(() => {
        localStorage.setItem('python_mastery_saved_problems', JSON.stringify(savedProblems));
    }, [savedProblems]);

    useEffect(() => {
        localStorage.setItem('python_mastery_id_log', JSON.stringify(idLogProblems));
    }, [idLogProblems]);

    const isProblemSaved = (id: number) => savedProblems.some(p => p.exerciseId === id);

    const saveCurrentProblem = () => {
        if (isProblemSaved(exercise.id)) return;
        const newProblem: SavedProblem = {
            exerciseId: exercise.id,
            description: exercise.description,
            initialCode: files[0]?.content ?? exercise.initialCode,
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
        const ex = EXERCISES.find(e => e.id === problem.exerciseId);
        if (ex) {
            setPlainMode(false);
            setExercise(ex);
            setFiles([{ name: 'main.py', content: ex.initialCode }]);
            setActiveFileIndex(0);
            setOutput('Run code to see output...');
            setOutputStatus('idle');
            setPendingNextProblem(false);
            setAiHintText('');
            setLatestAiReviewRequest(null);
            setLatestAiReviewResult(null);
            setShowModal('none');
        }
    };

    const isProblemInIdLog = (id: number) => idLogProblems.some(p => p.exerciseId === id);

    const addProblemToIdLog = (id: number) => {
        if (id < 1 || id > 2000) return;
        if (isProblemInIdLog(id)) return;
        const ex = EXERCISES.find(e => e.id === id);
        if (ex) {
            const newProblem: SavedProblem = {
                exerciseId: ex.id,
                description: ex.description,
                initialCode: ex.initialCode,
                solution: ex.solution,
                savedAt: new Date().toISOString(),
                mastered: false,
            };
            setIdLogProblems(prev => [...prev, newProblem]);
        }
    };

    const deleteIdLogProblem = (id: number) => {
        setIdLogProblems(prev => prev.filter(p => p.exerciseId !== id));
    };

    const markIdLogProblemMastered = (id: number) => {
        setIdLogProblems(prev =>
            prev.map(p => (p.exerciseId === id ? { ...p, mastered: true } : p))
        );
    };

    const loadIdLogProblem = (problem: SavedProblem) => {
        const ex = EXERCISES.find(e => e.id === problem.exerciseId);
        if (ex) {
            setPlainMode(false);
            setExercise(ex);
            setFiles([{ name: 'main.py', content: ex.initialCode }]);
            setActiveFileIndex(0);
            setOutput('Run code to see output...');
            setOutputStatus('idle');
            setPendingNextProblem(false);
            setAiHintText('');
            setLatestAiReviewRequest(null);
            setLatestAiReviewResult(null);
            setShowModal('none');
        }
    };

    const handleIdLogSubmit = () => {
        const id = parseInt(idLogInput);
        if (!isNaN(id) && id >= 1 && id <= 2000) {
            addProblemToIdLog(id);
            setIdLogInput('');
        }
    };

    const handleDeleteConfirm = (id: number, type: 'saved' | 'idlog') => {
        setDeleteConfirmId(id);
        setDeleteConfirmType(type);
        setShowModal('delete_confirm');
    };

    const handleDeleteCancel = () => {
        setDeleteConfirmId(null);
        setDeleteConfirmType(null);
        setShowModal('settings');
    };

    const handleDeleteExecute = () => {
        if (deleteConfirmId === null || deleteConfirmType === null) return;
        
        if (deleteConfirmType === 'saved') {
            deleteSavedProblem(deleteConfirmId);
        } else if (deleteConfirmType === 'idlog') {
            deleteIdLogProblem(deleteConfirmId);
        }
        
        setDeleteConfirmId(null);
        setDeleteConfirmType(null);
        setShowModal('settings');
    };

    const mainScrollRef = useRef<HTMLDivElement>(null);
    const editorShellRef = useRef<HTMLDivElement>(null);
    const activeEditorViewRef = useRef<EditorView | null>(null);
    const stdinValuesRef = useRef<string[]>([]);
    const keyboardHapticsRef = useRef(keyboardHaptics);
    const keyboardSoundRef = useRef(keyboardSound);
    const resultSoundRef = useRef(resultSound);
    const keyboardAudioRef = useRef<AudioContext | null>(null);
    const lastKeyboardFeedbackRef = useRef(0);
    const keyboardMainScrollRef = useRef<number | null>(null);
    const keyboardRestoreTimersRef = useRef<number[]>([]);
    const deleteHoldDelayRef = useRef<number | null>(null);
    const deleteHoldTimerRef = useRef<number | null>(null);
    const longPressTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
    const outputRef = useRef<HTMLDivElement>(null);
    const headerRef = useRef<HTMLDivElement>(null);
    const [headerHeight, setHeaderHeight] = useState(70);
    const totalFixedEnd = !plainMode
        ? Math.max(headerHeight + 8, 78) + 190
        : headerHeight;
    const editorToolbarTop = Math.max(totalFixedEnd + 4, 270);
    const editorContentTop = editorToolbarTop + 54;
    const runButtonLabel = 'RUN';
    const runButtonClass = 'ml-1 flex items-center gap-1.5 px-3 py-1 rounded-lg font-bold text-xs bg-[#22c55e1a] border border-[#22c55e4d] text-[#22c55e]';
    const selectedModeLabel = getDifficultyLabel(difficultyMode);
    const currentStats = statsByMode[difficultyMode] ?? EMPTY_STATS;
    const userRank = useMemo(() => getUserRank(statsByMode), [statsByMode]);
    const displaySolution = useMemo(() => normalizeSolutionHeadings(exercise.solution), [exercise.solution]);
    const modeExerciseCount = useMemo(() => {
        return getExercisePoolForMode(difficultyMode).length;
    }, [difficultyMode]);

    useEffect(() => {
        localStorage.setItem('python_count_row_colors', JSON.stringify(countRowColors));
    }, [countRowColors]);

    useEffect(() => {
        localStorage.setItem('python_editor_colors', JSON.stringify(editorColors));
    }, [editorColors]);

    useEffect(() => {
        localStorage.setItem('python_tool_panel_colors', JSON.stringify(toolPanelColors));
    }, [toolPanelColors]);

    useEffect(() => {
        localStorage.setItem('python_panel_colors', JSON.stringify(panelColors));
    }, [panelColors]);

    useEffect(() => {
        saveOfflineAiState(offlineAiState);
    }, [offlineAiState]);

    useEffect(() => {
        if (offlineAiState.status !== 'downloading') return;
        const intervalId = window.setInterval(() => setOfflineAiNow(Date.now()), 1000);
        return () => window.clearInterval(intervalId);
    }, [offlineAiState.status]);

    useEffect(() => {
        keyboardHapticsRef.current = keyboardHaptics;
        localStorage.setItem('python_keyboard_haptics', String(keyboardHaptics));
    }, [keyboardHaptics]);

    useEffect(() => {
        keyboardSoundRef.current = keyboardSound;
        localStorage.setItem('python_keyboard_sound', String(keyboardSound));
    }, [keyboardSound]);

    useEffect(() => {
        resultSoundRef.current = resultSound;
        localStorage.setItem('python_result_sound', String(resultSound));
    }, [resultSound]);

    useEffect(() => {
        localStorage.setItem('python_plain_mode', String(plainMode));
    }, [plainMode]);

    useEffect(() => {
        localStorage.setItem('python_saved_snippets', JSON.stringify(savedSnippets));
    }, [savedSnippets]);

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

    const playResultFeedback = useCallback((kind: 'win' | 'fail') => {
        if (!resultSoundRef.current) return;
        try {
            const AudioCtor = window.AudioContext || (window as any).webkitAudioContext;
            if (!AudioCtor) return;
            const audio = keyboardAudioRef.current ?? new AudioCtor();
            keyboardAudioRef.current = audio;
            if (audio.state === 'suspended') audio.resume();

            const notes = kind === 'win'
                ? [523.25, 659.25, 783.99, 1046.5]
                : [392, 329.63, 261.63];
            const spacing = kind === 'win' ? 0.055 : 0.075;
            const duration = kind === 'win' ? 0.09 : 0.12;
            const peak = kind === 'win' ? 0.055 : 0.04;
            notes.forEach((frequency, index) => {
                const start = audio.currentTime + index * spacing;
                const oscillator = audio.createOscillator();
                const gain = audio.createGain();
                oscillator.type = kind === 'win' ? 'triangle' : 'sine';
                oscillator.frequency.setValueAtTime(frequency, start);
                gain.gain.setValueAtTime(0.0001, start);
                gain.gain.exponentialRampToValueAtTime(peak, start + 0.012);
                gain.gain.exponentialRampToValueAtTime(0.0001, start + duration);
                oscillator.connect(gain);
                gain.connect(audio.destination);
                oscillator.start(start);
                oscillator.stop(start + duration + 0.015);
            });
        } catch {
            // Result audio is optional and may be blocked until the browser allows sound.
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
        // Immediate update
        updateHeaderHeight();
        // Update after a short delay to ensure DOM is ready
        const timeoutId1 = setTimeout(() => {
            updateHeaderHeight();
        }, 50);
        const timeoutId2 = setTimeout(() => {
            updateHeaderHeight();
        }, 200);
        const handleResize = () => {
            updateHeaderHeight();
        };
        window.addEventListener('resize', handleResize);

        // Use ResizeObserver to watch for content changes
        let headerObserver: ResizeObserver | null = null;
        if (headerRef.current && typeof ResizeObserver !== 'undefined') {
            headerObserver = new ResizeObserver(() => {
                updateHeaderHeight();
            });
            headerObserver.observe(headerRef.current);
        }
        return () => {
            clearTimeout(timeoutId1);
            clearTimeout(timeoutId2);
            window.removeEventListener('resize', handleResize);
            if (headerObserver) {
                headerObserver.disconnect();
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

    const clearAppCacheAndReload = async () => {
        if (cacheClearBusy) return;
        setCacheClearBusy(true);
        try {
            if (window.caches) {
                const keys = await window.caches.keys();
                await Promise.all(keys.map(k => window.caches.delete(k)));
            }
            if (navigator.serviceWorker) {
                const registrations = await navigator.serviceWorker.getRegistrations();
                await Promise.all(registrations.map(registration => registration.unregister()));
            }
            sessionStorage.removeItem('cache_cleared');
            const nextUrl = new URL(window.location.href);
            nextUrl.searchParams.set('cache', Date.now().toString());
            window.location.replace(nextUrl.toString());
        } catch (error) {
            console.error('Cache clear failed:', error);
            window.location.reload();
        }
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
        setLatestAiReviewRequest(null);
        setLatestAiReviewResult(null);
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

    const tryAiAutoWinFallback = async (request: AiReviewRequest): Promise<{ review: AiReviewResult | null; autoWinReview: AiReviewResult | null }> => {
        try {
            const review = await withAiReviewTimeout(reviewWithAvailableAi(request, offlineAiState));
            setLatestAiReviewResult(review);
            setAiHintText(formatAiReviewHintText(review));
            return {
                review,
                autoWinReview: isAiAutoWinReview(review) ? review : null,
            };
        } catch (error: any) {
            const fallback = buildDiagnosticReview({
                ...request,
                graderMessage: `AI fallback failed: ${String(error?.message || error || 'Unknown error')}`,
                graderPassed: false,
            });
            setLatestAiReviewResult(fallback);
            setAiHintText(formatAiReviewHintText(fallback));
            return { review: fallback, autoWinReview: null };
        }
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
        const autoGrader = !plainMode ? AUTO_GRADERS[exercise.id] : null;
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
            const code = `exec(compile(${JSON.stringify(activeFile.content)}, ${JSON.stringify(activeFile.name)}, 'exec'))`;
            await pyodide.runPythonAsync(code);
            stdout = pyodide.runPython("sys.stdout.getvalue()");
            stdinValuesRef.current = [];
            setStdinValues([]);

            if (plainMode) {
                setOutput(stdout?.trim() || 'Success (No output).');
                setOutputStatus('info');
            } else if (autoGrader) {
                pyodide.runPython(`
import builtins
builtins.input = lambda prompt='': (_ for _ in ()).throw(Exception("__AUTO_GRADER_INPUT_UNAVAILABLE__" + str(prompt)))
`);
                pyodide.runPython(buildAutoGradeScript(autoGrader, activeFile.content, activeFile.name));
                const gradeResult = JSON.parse(pyodide.runPython("__auto_grader_json")) as AutoGradeResult;
                const graderOutput = gradeResult.output?.trim()
                    ? `Program output:\n${gradeResult.output.trim()}\n\n`
                    : '';
                const userOutput = stdout?.trim() ? `Program output:\n${stdout.trim()}\n\n` : '';
                const displayOutput = userOutput || graderOutput;
                const reviewRequest: AiReviewRequest = {
                    problemId: exercise.id,
                    title: exercise.title,
                    description: exercise.description,
                    userCode: activeFile.content,
                    graderMessage: gradeResult.message,
                    graderPassed: gradeResult.passed,
                    graderSpec: autoGrader,
                    programOutput: stdout || gradeResult.output || '',
                    visibleSolution: displaySolution,
                };
                setLatestAiReviewRequest(reviewRequest);
                setLatestAiReviewResult(null);

                if (gradeResult.passed) {
                    updateCurrentModeStats('success');
                    setOutputStatus('win');
                    playResultFeedback('win');
                    setPendingNextProblem(true);
                    setOutput(`${displayOutput}AUTO WIN\n${gradeResult.message}\n\nUse the Next button in the problem panel for another problem.`);
                } else {
                    setOutputStatus('info');
                    setPendingNextProblem(true);
                    setOutput(`${displayOutput}AUTO CHECK\n${gradeResult.message}\n\nDeterministic grader failed. AI reviewer is checking whether this is logically correct...`);
                    const aiFallback = await tryAiAutoWinFallback(reviewRequest);
                    if (aiFallback.autoWinReview) {
                        updateCurrentModeStats('success');
                        setOutputStatus('win');
                        playResultFeedback('win');
                        setOutput(`${displayOutput}AI AUTO WIN\nDeterministic grader failed, but ${getAiReviewSourceLabel(aiFallback.autoWinReview.source)} judged this answer logically correct with ${Math.round(aiFallback.autoWinReview.confidence * 100)}% confidence.\n\nOriginal grader message:\n${gradeResult.message}\n\nUse the Next button in the problem panel for another problem.`);
                    } else {
                        updateCurrentModeStats('failed');
                        setOutputStatus('fail');
                        playResultFeedback('fail');
                        const review = aiFallback.review;
                        const reviewNote = review
                            ? review.source === 'diagnostic'
                                ? '\n\nAI reviewer used built-in diagnostics only. No model-backed review confirmed this as correct.'
                                : `\n\nAI reviewer returned ${review.verdict.replace('_', ' ')} with ${Math.round(review.confidence * 100)}% confidence from ${getAiReviewSourceLabel(review.source)}.`
                            : '\n\nAI reviewer could not complete.';
                        setOutput(`${displayOutput}AUTO FAILED\n${gradeResult.message}${reviewNote}\n\nFix your code and press RUN again, or use the Next button in the problem panel.`);
                    }
                }
            } else {
                setOutputStatus('info');
                setOutput(`${stdout || 'Success (No output).'}\n\nNo auto-grader yet for Problem ${exercise.id}. Use Win/Failed manually from Tools.`);
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
            if (plainMode) {
                setOutputStatus('fail');
                playResultFeedback('fail');
                setOutput(`${stdout || ''}\n${errorMessage}`);
            } else if (autoGrader) {
                updateCurrentModeStats('failed');
                const reviewRequest: AiReviewRequest = {
                    problemId: exercise.id,
                    title: exercise.title,
                    description: exercise.description,
                    userCode: files[activeFileIndex].content,
                    graderMessage: errorMessage,
                    graderPassed: false,
                    graderSpec: autoGrader,
                    programOutput: stdout || '',
                    visibleSolution: displaySolution,
                };
                setLatestAiReviewRequest(reviewRequest);
                const diagnosticReview = buildDiagnosticReview(reviewRequest);
                setLatestAiReviewResult(diagnosticReview);
                setAiHintText(formatAiReviewHintText(diagnosticReview));
                setOutputStatus('fail');
                playResultFeedback('fail');
                setPendingNextProblem(true);
                setOutput(`${userOutput}AUTO FAILED\n${errorMessage}\n\nAI REVIEW\n${diagnosticReview.explanation}${diagnosticReview.suggestedFix ? `\n\nSuggested fix:\n${diagnosticReview.suggestedFix}` : ''}\n\nFix your code and press RUN again, or use the Next button in the problem panel.`);
            } else {
                setOutputStatus('fail');
                playResultFeedback('fail');
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
        setLatestAiReviewResult(null);
        setLatestAiReviewRequest(null);
    };

    const handleMarkSuccess = () => {
        updateCurrentModeStats('success');
        playResultFeedback('win');
        loadRandomExercise();
    };

    const handleMarkFailed = () => {
        updateCurrentModeStats('failed');
        playResultFeedback('fail');
        loadRandomExercise();
    };

    const buildProblemAiRequest = useCallback((question: string): AiReviewRequest => {
        const reusableReviewRequest =
            latestAiReviewRequest?.problemId === exercise.id &&
            latestAiReviewRequest.userCode === files[activeFileIndex]?.content
                ? latestAiReviewRequest
                : null;
        const currentGrader = AUTO_GRADERS[exercise.id] || null;
        const activeCode = files[activeFileIndex]?.content || '';
        const contextMessage = [
            `USER QUESTION: ${question}`,
            '',
            'Answer as a patient Python tutor for this exact exercise.',
            'Do not grade manually unless the user asks. Explain concepts, syntax, current output, and next steps.',
            `Latest output/status: ${outputStatus}`,
            `Latest output text: ${output}`,
            reusableReviewRequest?.graderMessage ? `Latest grader message: ${reusableReviewRequest.graderMessage}` : 'Latest grader message: none yet',
        ].join('\n');

        return {
            problemId: exercise.id,
            title: exercise.title,
            description: `${exercise.description}\n\n${contextMessage}`,
            userCode: activeCode,
            graderMessage: reusableReviewRequest?.graderMessage || contextMessage,
            graderPassed: reusableReviewRequest?.graderPassed ?? outputStatus === 'win',
            graderSpec: reusableReviewRequest?.graderSpec || currentGrader,
            programOutput: reusableReviewRequest?.programOutput || output,
            visibleSolution: displaySolution,
        };
    }, [activeFileIndex, displaySolution, exercise, files, latestAiReviewRequest, output, outputStatus]);

    const buildBuiltInProblemAiAnswer = useCallback((question: string, request: AiReviewRequest): string => {
        const q = question.toLowerCase();
        const description = exercise.description;
        const hint = exercise.hint?.trim();
        const breakdown = exercise.breakdown?.trim();
        const code = request.userCode || '';
        const graderMessage = request.graderMessage || '';
        const promptMethods = Array.from(new Set(description.match(/`[^`]+`|\.[A-Za-z_]\w*\(\)|\b[A-Za-z_]\w*\(\)/g) || []))
            .slice(0, 8);
        const asksWhy = /why|wrong|failed|fail|error|output|red|incorrect/.test(q);
        const asksMethod = /method|isdigit|isalpha|isalnum|string|integer|int|digit|syntax|built.?in|append|split|join|strip|lower|upper|replace|sort|sorted/.test(q);
        const asksHint = /hint|help|start|how|what should|what do/.test(q);
        const asksDigitMethod = /\bis\s*(?:there\s*)?(?:is\s*)?digit\b/.test(q) || q.includes('isdigit') || (q.includes('digit') && q.includes('string') && q.includes('method'));
        const asksIntegerArgument = /(?:integer|int|number).*(?:argument|input|parameter)|can i.*(?:integer|int|number)|write an? (?:integer|int|number)/.test(q);
        const firstLine = description.split('\n')[0];
        const functionName = description.match(/`([A-Za-z_]\w*)`/)?.[1] || exercise.initialCode.match(/def\s+([A-Za-z_]\w*)/)?.[1] || 'your_function';
        const lowerDescription = description.toLowerCase();
        const asksBoolean = /\b(bool|boolean|true|false)\b/.test(q);
        const asksArgument = /\b(argument|parameter|input|pass|put|use)\b/.test(q);
        const returnsBoolean = /\b(return|returns)\b[^.]*\b(true|false|boolean|bool)\b/.test(lowerDescription) || /\btrue\b.*\bif\b|\bfalse\b/.test(lowerDescription);
        const wantsCharacter = /\b(character|char)\b/.test(lowerDescription);
        const wantsString = wantsCharacter || /\b(string|str)\b/.test(lowerDescription);
        const wantsNumber = /\b(integer|number|int|float)\b/.test(lowerDescription);
        const promptMethodNames = promptMethods
            .map(item => item.replace(/[`()]/g, '').trim())
            .filter(Boolean);
        const taskSummary = [
            `The task is asking you to build \`${functionName}\`, not just copy the example output.`,
            returnsBoolean ? 'The answer should be a Boolean result: `True` or `False`.' : '',
            wantsCharacter ? 'The input is described as a character, so use a one-character string like `"5"` or `"a"`.' : '',
            wantsString && !wantsCharacter ? 'The input is text, so string methods and string indexing may be useful.' : '',
            wantsNumber && !wantsString ? 'The input is numeric, so arithmetic or numeric comparison is probably the main operation.' : '',
            promptMethodNames.length ? `Useful prompt syntax: ${promptMethodNames.map(name => `\`${name}\``).join(', ')}.` : '',
        ].filter(Boolean);
        const directContextAnswer = (lead: string, extra: string[] = []) => [
            `1. Direct answer`,
            lead,
            '',
            `2. How it applies here`,
            ...(taskSummary.length ? taskSummary : [firstLine]),
            '',
            ...extra,
        ].join('\n');
        const conceptAnswers: Array<{ pattern: RegExp; text: string }> = [
            {
                pattern: /\b(list|lists)\b/,
                text: [
                    '1. A list is an ordered collection of values.',
                    'Use square brackets:',
                    '```python',
                    'numbers = [1, 2, 3]',
                    "names = ['Ada', 'Bob']",
                    '```',
                    '2. Lists can change. You can add, remove, sort, index, and loop through them.',
                    '```python',
                    'numbers.append(4)',
                    'print(numbers[0])  # 1',
                    '```',
                    '3. In a problem, if it says “takes a list”, the function parameter should receive something like `[1, 2, 3]`.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(dict|dictionary|dictionaries)\b/,
                text: [
                    '1. A dictionary stores key-value pairs.',
                    'Use curly braces with `key: value`:',
                    '```python',
                    "person = {'name': 'Ada', 'age': 30}",
                    "print(person['name'])  # Ada",
                    '```',
                    '2. Use dictionaries when the problem asks you to map one thing to another, like word counts, names to scores, or keys to values.',
                    '3. Common dictionary methods are `.keys()`, `.values()`, `.items()`, and `.get()`.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(tuple|tuples)\b/,
                text: [
                    '1. A tuple is an ordered collection like a list, but it is immutable.',
                    'Use parentheses:',
                    '```python',
                    'point = (3, 4)',
                    'x, y = point',
                    '```',
                    '2. Use a tuple when the problem asks for a fixed group of values, like `(min_value, max_value)`.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(set|sets)\b/,
                text: [
                    '1. A set stores unique values only.',
                    'Use curly braces or `set()`:',
                    '```python',
                    'numbers = {1, 2, 2, 3}',
                    'print(numbers)  # {1, 2, 3}',
                    '```',
                    '2. Sets are useful for removing duplicates and checking membership quickly with `in`.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(string|strings|str)\b/,
                text: [
                    '1. A string is text in quotes.',
                    '```python',
                    "word = 'python'",
                    '```',
                    '2. Strings have methods like `.lower()`, `.upper()`, `.replace()`, `.split()`, `.strip()`, `.isdigit()`, and `.isalpha()`.',
                    '3. Strings are sequences, so indexing and slicing work:',
                    '```python',
                    "word = 'python'",
                    'print(word[0])   # p',
                    'print(word[-1])  # n',
                    '```',
                ].join('\n\n'),
            },
            {
                pattern: /\b(method|methods)\b/,
                text: [
                    '1. A method is a function that belongs to an object.',
                    'You call it with dot notation:',
                    '```python',
                    "text = 'hello'",
                    'print(text.upper())  # HELLO',
                    '```',
                    '2. In this app, if the problem mentions a string/list/dictionary method, it usually wants you to call it on that value.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(function|def)\b/,
                text: [
                    '1. A function is a reusable block of code.',
                    '```python',
                    'def add(a, b):',
                    '    return a + b',
                    '```',
                    '2. `def` creates the function. `return` sends the answer back to the grader.',
                    '3. For these problems, prefer `return` inside functions unless the prompt specifically asks you to print.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(oop|class|object)\b/,
                text: [
                    '1. OOP means object-oriented programming.',
                    'A class is a blueprint. An object is an instance made from that blueprint.',
                    '```python',
                    'class Dog:',
                    '    def __init__(self, name):',
                    '        self.name = name',
                    '```',
                    '2. `self` means “this object”. Methods inside a class usually take `self` first.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(loop|for|while)\b/,
                text: [
                    '1. A loop repeats code.',
                    'Use `for` when looping through a sequence:',
                    '```python',
                    'for number in [1, 2, 3]:',
                    '    print(number)',
                    '```',
                    '2. Use `while` when repeating until a condition changes.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(return|print)\b/,
                text: [
                    '1. `return` sends a value back from a function.',
                    '2. `print()` only displays text in the output.',
                    '```python',
                    'def square(n):',
                    '    return n * n',
                    '```',
                    '3. For most function problems in this app, the grader expects `return`, not only `print()`.',
                ].join('\n\n'),
            },
            {
                pattern: /\b(index|indexes|indices|slice|slicing)\b/,
                text: [
                    '1. Indexing gets one item from a sequence.',
                    '```python',
                    "text = 'python'",
                    'print(text[0])   # p',
                    'print(text[-1])  # n',
                    '```',
                    '2. Slicing gets a range:',
                    '```python',
                    'print(text[1:4])  # yth',
                    '```',
                ].join('\n\n'),
            },
        ];

        if (asksDigitMethod) {
            return [
                '1. Yes — `isdigit()` is a string method.',
                'You call it on a string value, like this:',
                '```python',
                "char = '5'",
                'print(char.isdigit())  # True',
                '```',
                '2. For this problem, `check_digit(char)` should take one character as a string and return `True` if it is a digit from `0` to `9`.',
                '```python',
                'def check_digit(char):',
                '    return char.isdigit()',
                '```',
                '3. Do not pass an integer directly if the task says “character”. Use `"5"` not `5`. If you already have an integer, convert it first with `str(value).isdigit()`.',
            ].join('\n\n');
        }

        if (asksIntegerArgument) {
            const characterProblem = /character|char|string/.test(lowerDescription);
            if (characterProblem) {
                return [
                    '1. For this problem, use a string character, not an integer.',
                    'The prompt says the function takes a character. In Python, that usually means a one-character string like `"5"` or `"a"`.',
                    '```python',
                    "check_digit('5')  # correct",
                    'check_digit(5)    # not ideal for this task',
                    '```',
                    '2. Why?',
                    '`isdigit()` is a string method, so it works on strings:',
                    '```python',
                    "char = '5'",
                    'print(char.isdigit())  # True',
                    '```',
                    '3. If you already have an integer, convert it first:',
                    '```python',
                    'value = 5',
                    'print(str(value).isdigit())  # True',
                    '```',
                ].join('\n\n');
            }
            return [
                '1. It depends on the problem input.',
                'If the prompt says number or integer, passing an integer is fine.',
                'If the prompt says string or character, use quotes, for example `"5"` instead of `5`.',
                '2. Match the function parameter to the prompt, because the grader tests the type the problem asks for.',
            ].join('\n\n');
        }

        if (asksBoolean) {
            return directContextAnswer(
                returnsBoolean
                    ? 'Yes. For this problem, the function should return a Boolean value: `True` when the condition is satisfied, otherwise `False`.'
                    : 'A Boolean is only needed if the prompt asks for `True`/`False`, a yes/no check, or a condition result.',
                returnsBoolean ? [
                    '3. Example shape',
                    '```python',
                    `def ${functionName}(value):`,
                    '    return condition_here',
                    '```',
                    'The important part is that the expression after `return` evaluates to `True` or `False`.',
                ] : [
                    '3. What to return instead',
                    'For this problem, return the type requested by the prompt, such as a number, string, list, dictionary, or other calculated result.',
                ],
            );
        }

        if (asksArgument) {
            return directContextAnswer(
                wantsString
                    ? 'Use a string argument for this task. If the prompt says character, pass a quoted value like `"5"` or `"a"`.'
                    : wantsNumber
                        ? 'Use a numeric argument for this task unless the prompt specifically asks for text.'
                        : 'Use the argument type described by the prompt. The variable name can be different, but the value type and logic must match the task.',
                [
                    '3. Variable names do not matter',
                    `The grader cares that \`${functionName}\` performs the requested logic. The parameter can be named \`char\`, \`x\`, \`value\`, or another valid name.`,
                ],
            );
        }

        const conceptAnswer = conceptAnswers.find(item => item.pattern.test(q));
        if (conceptAnswer && !asksWhy && !q.includes('explain task')) {
            return conceptAnswer.text;
        }

        const parts: string[] = [];
        parts.push(`1. Task breakdown\n${taskSummary.length ? taskSummary.join('\n') : firstLine}`);

        const expectedShape = [
            `Function: \`${functionName}\``,
            promptMethods.length ? `Useful syntax from the prompt: ${promptMethods.join(', ')}` : '',
        ].filter(Boolean).join('\n');
        if (expectedShape) {
            parts.push(`2. Important details\n${expectedShape}`);
        }

        if (asksMethod || promptMethods.length) {
            let methodText = promptMethods.length ? promptMethods.join(', ') : 'No specific method name is written in the prompt.';
            if (description.toLowerCase().includes('digit')) {
                methodText += `\n\nFor digit checks, \`isdigit()\` is a string method. Use \`char.isdigit()\` on a string character like \`'7'\`.`;
            }
            parts.push(`3. Method or syntax\n${methodText}`);
        }

        if (asksWhy || outputStatus === 'fail') {
            const outputText = output && output !== 'Run code to see output...' ? output : 'No run output is available yet.';
            parts.push(`4. Current output check\nStatus: ${outputStatus.toUpperCase()}.\nOutput/grader context:\n${graderMessage || outputText}\n\nIf the output is wrong, compare what your code returns or prints against the operation requested by the problem.`);
        }

        if (code.trim() && asksWhy) {
            const lines = code.split('\n').filter(line => line.trim()).slice(0, 8).join('\n');
            parts.push(`5. Your code context\n\`\`\`python\n${lines}\n\`\`\``);
        }

        if (asksHint || hint || breakdown) {
            parts.push(`6. Simple next step\n${hint || 'Break the problem into input, operation, and returned output.'}${breakdown ? `\n\nGuide:\n${breakdown}` : ''}`);
        }

        if (parts.length <= 2 && !asksHint && !asksWhy && !asksMethod) {
            parts.push(`3. If your question is more specific\nAsk it directly, for example: “Should this return ` + '`True` or `False`?”, “Can the argument be an integer?”, or “What does this method do?”.');
        }

        return parts.join('\n\n');
    }, [exercise, output, outputStatus]);

    const openProblemAi = useCallback(() => {
        const request = buildProblemAiRequest('Explain this problem.');
        const shouldReset = problemAiProblemId !== exercise.id || problemAiMessages.length === 0;
        if (shouldReset) {
            setProblemAiProblemId(exercise.id);
            setProblemAiMessages([{
                id: Date.now(),
                role: 'assistant',
                source: 'built_in',
                text: buildBuiltInProblemAiAnswer(
                    outputStatus === 'fail' ? 'Why did my output fail?' : 'Explain this problem.',
                    request,
                ),
            }]);
        }
        setShowModal('problem_ai');
    }, [buildBuiltInProblemAiAnswer, buildProblemAiRequest, exercise.id, outputStatus, problemAiMessages.length, problemAiProblemId]);

    const sendProblemAiQuestion = useCallback(async (rawQuestion: string) => {
        const question = rawQuestion.trim();
        if (!question || problemAiRunning) return;
        const request = buildProblemAiRequest(question);
        const lowerQuestion = question.toLowerCase();
        const shouldUseReviewer =
            /review my code|check my code|is my code correct|is this correct|why failed|why did.*fail|auto failed|grader|output wrong|error/.test(lowerQuestion);
        const userMessage: ProblemAiMessage = { id: Date.now(), role: 'user', source: 'user', text: question };
        setProblemAiMessages(prev => [...prev, userMessage]);
        setProblemAiDraft('');
        setProblemAiRunning(true);

        try {
            if (!shouldUseReviewer) {
                const modelAnswer = await answerProblemQuestionWithAvailableAi(question, request, offlineAiState);
                if (modelAnswer) {
                    setProblemAiMessages(prev => [...prev, {
                        id: Date.now() + 1,
                        role: 'assistant',
                        source: 'offline',
                        text: modelAnswer,
                    }]);
                    return;
                }

                setProblemAiMessages(prev => [...prev, {
                    id: Date.now() + 1,
                    role: 'assistant',
                    source: 'built_in',
                    text: buildBuiltInProblemAiAnswer(question, request),
                }]);
                return;
            }
            if (offlineAiState.status !== 'ready') {
                setProblemAiMessages(prev => [...prev, {
                    id: Date.now() + 1,
                    role: 'assistant',
                    source: 'built_in',
                    text: buildBuiltInProblemAiAnswer(question, request),
                }]);
                return;
            }
            const review = await withAiReviewTimeout(reviewWithAvailableAi(request, offlineAiState));
            const answer = [
                review.explanation,
                review.suggestedFix ? `Suggested direction:\n${review.suggestedFix}` : '',
            ].filter(Boolean).join('\n\n');
            setProblemAiMessages(prev => [...prev, {
                id: Date.now() + 1,
                role: 'assistant',
                source: review.source === 'diagnostic' ? 'built_in' : 'offline',
                text: answer || buildBuiltInProblemAiAnswer(question, request),
            }]);
        } catch {
            setProblemAiMessages(prev => [...prev, {
                id: Date.now() + 1,
                role: 'assistant',
                source: 'built_in',
                text: `Offline AI could not answer this time, so built-in help answered instead.\n\n${buildBuiltInProblemAiAnswer(question, request)}`,
            }]);
        } finally {
            setProblemAiRunning(false);
        }
    }, [buildBuiltInProblemAiAnswer, buildProblemAiRequest, offlineAiState, problemAiRunning]);

    const handleAiHint = async () => {
        const reusableReviewRequest =
            latestAiReviewRequest?.problemId === exercise.id &&
            latestAiReviewRequest.userCode === files[activeFileIndex].content
                ? latestAiReviewRequest
                : null;
        const currentGrader = AUTO_GRADERS[exercise.id] || null;
        const request: AiReviewRequest = reusableReviewRequest || {
            problemId: exercise.id,
            title: exercise.title,
            description: exercise.description,
            userCode: files[activeFileIndex].content,
            graderMessage: 'Run has not been pressed for this code yet.',
            graderPassed: false,
            graderSpec: currentGrader,
            programOutput: output,
            visibleSolution: displaySolution,
        };

        setShowModal('hint');
        setLatestAiReviewRequest(request);

        const diagnosticResult = (() => {
            try {
                return buildDiagnosticReview(request);
            } catch (error: any) {
                return {
                    verdict: 'unclear' as const,
                    confidence: 0.25,
                    explanation: `Built-in review could not inspect this code automatically: ${String(error?.message || error || 'Unknown error')}`,
                    suggestedFix: 'Run the code first, then press AI Review again so the reviewer can compare the code, output, and grader result.',
                    source: 'diagnostic' as const,
                };
            }
        })();
        const setupNote = offlineAiState.status !== 'ready'
            ? `Offline model status: ${getOfflineAiStatusLabel(offlineAiState.status)}. Built-in offline review is active.\n\n`
            : 'Built-in review is shown immediately while the local model checks the code.\n\n';
        const immediateResult = {
            ...diagnosticResult,
            explanation: `${setupNote}${diagnosticResult.explanation}`,
        };
        setLatestAiReviewResult(immediateResult);
        setAiHintText(formatAiReviewHintText(immediateResult));

        setAiReviewRunning(true);
        try {
            const review = await withAiReviewTimeout(reviewWithAvailableAi(request, offlineAiState));
            const setupNote = offlineAiState.status !== 'ready'
                ? `Offline model status: ${getOfflineAiStatusLabel(offlineAiState.status)}. Built-in offline review is active.\n\n`
                : '';
            const result = review.source === 'diagnostic' && setupNote
                ? { ...review, explanation: `${setupNote}${review.explanation}` }
                : review;
            setLatestAiReviewResult(result);
            setAiHintText(formatAiReviewHintText(result));
        } catch (error: any) {
            const fallback = buildDiagnosticReview({
                ...request,
                graderMessage: `AI review failed: ${String(error?.message || error || 'Unknown error')}`,
                graderPassed: false,
            });
            const result = {
                ...fallback,
                explanation: `AI review could not complete, so built-in offline review checked this code instead. ${fallback.explanation}`,
            };
            setLatestAiReviewResult(result);
            setAiHintText(formatAiReviewHintText(result));
        } finally {
            setAiReviewRunning(false);
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
            setSyntaxContent('');
            return;
        }

        try {
            const logicFile = `level1_${filePrefix}_codelogic.py`;
            const reqFile1 = `level1_${filePrefix}_requirements.py`;
            const reqFile2 = `level1_${filePrefix}_requirements..py`;
            const syntaxFile = `level1_${filePrefix}_syntax.py`;

            // Handle GitHub Pages subdirectory
            const isGitHubPages = window.location.hostname === 'llomj.github.io';
            const basePath = isGitHubPages ? '/python_app' : '';
            const cacheBuster = `?cb=${Date.now()}`;

            // Fetch and parse logic file
            try {
                const logicResponse = await fetch(`${basePath}/${logicFile}${cacheBuster}`);
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
                let reqResponse = await fetch(`${basePath}/${reqFile1}${cacheBuster}`);
                if (!reqResponse.ok) {
                    reqResponse = await fetch(`${basePath}/${reqFile2}${cacheBuster}`);
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

            // Fetch and parse syntax file
            try {
                const syntaxResponse = await fetch(`${basePath}/${syntaxFile}${cacheBuster}`);
                if (syntaxResponse.ok) {
                    const syntaxText = await syntaxResponse.text();
                    const problemSyntax = extractProblemContent(syntaxText, exerciseId);
                    setSyntaxContent(problemSyntax || '');
                } else {
                    setSyntaxContent('');
                    console.warn(`Syntax file not found: ${syntaxFile}`);
                }
            } catch (err) {
                setSyntaxContent('');
                console.warn(`Error loading syntax file: ${err.message}`);
            }
        } catch (err) {
            console.error('Error loading solution files:', err);
            setLogicContent('');
            setRequirementsContent('');
            setSyntaxContent('');
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

    const panelAlpha = 1 - (panelColors.alpha / 100);
    const panelBackground = hexToRgba(panelColors.background, panelAlpha);
    const panelBorder = hexToRgba(panelColors.border, 0.3);
    const panelBorderSoft = hexToRgba(panelColors.border, 0.3);
    const sharedPanelSurface = {
        backgroundColor: panelBackground,
        border: `1px solid ${panelBorder}`,
        backdropFilter: 'blur(8px)',
        WebkitBackdropFilter: 'blur(8px)',
    } as const;
    const semitransparentBg = hexToRgba(panelColors.background, panelAlpha);
    const effectiveEditorColors = useMemo<EditorColorSettings>(() => ({
        ...editorColors,
        appBackground: semitransparentBg,
        problemBackground: semitransparentBg,
        problemBorder: panelColors.border,
        panelBackground: semitransparentBg,
        panelBorder: panelColors.border,
        tabBackground: semitransparentBg,
        activeTabBackground: editorColors.activeTabBackground,
        outputBackground: semitransparentBg,
        background: semitransparentBg,
        gutterBackground: semitransparentBg,
    }), [editorColors, panelColors.background, panelColors.border, panelAlpha]);

    const editorExtensions = useMemo(() => [
        python(),
        indentUnit.of("    "),
        holdBackspaceExtension,
        autocompletion({ override: [pythonCompletionSource, pythonSnippets] }),
        EditorView.lineWrapping,
        ...createCustomPythonTheme(effectiveEditorColors)
    ], [pythonCompletionSource, effectiveEditorColors]);

    if (bootStage !== 'launched') {
        return (
            <div className="fixed inset-0 z-[100] flex flex-col items-center justify-start pt-16 p-8 text-center text-white overflow-y-auto animate-in fade-in duration-500" style={{ backgroundColor: '#050c18' }}>
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
                            <button onClick={clearAppCacheAndReload} disabled={cacheClearBusy} className="w-full bg-red-500/10 border border-red-500/20 text-red-500 py-4 rounded-2xl font-black text-[10px] uppercase flex items-center justify-center gap-2 disabled:opacity-60"><Trash2 size={14} /> {cacheClearBusy ? 'Clearing...' : 'Clear App Cache'}</button>
                        </div>
                    </>
                ) : (
                    <div className="animate-in fade-in zoom-in duration-500 flex flex-col items-center flex-shrink-0">
                        <h1 className="text-3xl font-black tracking-tighter mb-2 text-[#3b82f6]">LOCAL ENGINE READY</h1>
                        <p className="text-gray-400 text-xs mb-6 uppercase tracking-widest font-bold">Standard Library Loaded</p>
                        <button onClick={handleLaunch} className="mt-4 bg-[#3b82f6] text-white px-10 py-4 rounded-2xl font-black text-lg shadow-[0_0_40px_rgba(59,130,246,0.3)] active:scale-95 transition-all flex items-center gap-2"><Zap size={20} fill="currentColor" /> ENTER EDITOR</button>
                        <button onClick={clearAppCacheAndReload} disabled={cacheClearBusy} className="mt-4 w-full max-w-xs bg-red-500/10 border border-red-500/25 text-red-400 py-3 rounded-2xl font-black text-[10px] uppercase flex items-center justify-center gap-2 disabled:opacity-60"><Trash2 size={14} /> {cacheClearBusy ? 'Clearing Cache...' : 'Clear App Cache'}</button>
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
            className="h-screen text-white flex flex-col max-w-2xl mx-auto overflow-hidden animate-in fade-in duration-700 relative"
            style={{ backgroundColor: '#050c18' }}
        >
            <div
                ref={headerRef}
                className="fixed left-1/2 z-20 w-full max-w-2xl -translate-x-1/2"
                style={{
                    top: 0,
                    backgroundColor: hexToRgba(panelColors.background, 0.18),
                    paddingTop: 'max(0.75rem, calc(env(safe-area-inset-top) + 0.75rem))',
                    paddingLeft: 'max(1rem, calc(var(--safe-area-inset-left, 0px) + 1rem))',
                    paddingRight: 'max(1rem, calc(var(--safe-area-inset-right, 0px) + 1rem))',
                    paddingBottom: '0.75rem'
                }}
            >
                <div className="flex items-center justify-center mb-3">
                    <div
                        className="flex gap-3 sm:gap-5 items-center px-3 py-2 rounded-full shadow-lg text-[10px] sm:text-xs font-black tracking-tight select-none"
                        style={{ ...sharedPanelSurface, pointerEvents: 'auto' }}
                        onPointerDown={() => {
                            countRowLongPressRef.current = setTimeout(() => {
                                setShowModal('stats_by_mode');
                            }, 500);
                        }}
                        onPointerUp={() => {
                            if (countRowLongPressRef.current) {
                                clearTimeout(countRowLongPressRef.current);
                                countRowLongPressRef.current = null;
                            }
                        }}
                        onPointerCancel={() => {
                            if (countRowLongPressRef.current) {
                                clearTimeout(countRowLongPressRef.current);
                                countRowLongPressRef.current = null;
                            }
                        }}
                        onPointerLeave={() => {
                            if (countRowLongPressRef.current) {
                                clearTimeout(countRowLongPressRef.current);
                                countRowLongPressRef.current = null;
                            }
                        }}
                    >
                        <button onClick={() => setShowModal('api_key')} className="transition-all p-1.5 rounded-full border" style={{ backgroundColor: countRowColors.iconBackground, borderColor: panelColors.border, color: countRowColors.icon }} title="API key settings"><Key size={14} /></button>
                        <div className="flex items-center"><span className="mr-1 uppercase" style={{ color: countRowColors.count }}>Count:</span><span style={{ color: countRowColors.value }}>{currentStats.shots}</span></div>
                        <div className="flex items-center"><span className="mr-1 uppercase" style={{ color: countRowColors.wins }}>Wins:</span><span style={{ color: countRowColors.value }}>{currentStats.success}</span></div>
                        <div className="flex items-center"><span className="mr-1 uppercase" style={{ color: countRowColors.fail }}>Fail:</span><span style={{ color: countRowColors.value }}>{currentStats.failed}</span></div>
                        <div className="flex items-center pl-3 ml-1" style={{ borderLeft: `1px solid ${hexToRgba(panelColors.border, 0.3)}` }}><span className="mr-1 uppercase" style={{ color: countRowColors.rate }}>Rate:</span><span style={{ color: countRowColors.value }}>{rate}%</span></div>
                        <button onClick={() => setShowModal('settings')} className="transition-all p-1.5 rounded-full border" style={{ backgroundColor: countRowColors.iconBackground, borderColor: panelColors.border, color: countRowColors.icon }} title="Settings"><Settings size={14} /></button>
                    </div>
                </div>

                {plainMode && (
                    <>
                    <div
                        className="bg-[#0a1628] rounded-xl border border-[#1d2d44] shadow-2xl overflow-hidden"
                        style={{
                            minHeight: '64px',
                            maxHeight: '64px',
                            ...sharedPanelSurface,
                        }}
                    >
                        <div className="flex items-center justify-between gap-3 px-4 py-3">
                            <div className="flex items-center gap-2">
                                <Terminal size={16} style={{ color: countRowColors.count }} />
                                <h2 className="text-sm font-black uppercase tracking-[0.16em] text-gray-200 m-0">Plain IDE</h2>
                            </div>
                            <span className="text-[10px] text-gray-400">Free Python environment</span>
                        </div>
                    </div>
                    <div
                        className="bg-[#0a1628] rounded-xl border border-[#1d2d44] shadow-2xl overflow-hidden mt-2"
                        style={{
                            ...sharedPanelSurface,
                        }}
                    >
                        <div className="flex items-center justify-between gap-3 px-4 py-3">
                            <button
                                onClick={() => { setLogExpanded(prev => !prev); setShowSnippetSaveInput(false); }}
                                className="flex items-center gap-2 flex-1 text-left"
                            >
                                <FileText size={14} style={{ color: countRowColors.rate }} />
                                <h3 className="text-[11px] font-black uppercase tracking-[0.16em] text-gray-300">Log</h3>
                                {savedSnippets.length > 0 && (
                                    <span className="text-[10px] font-bold px-1.5 py-0.5 rounded-full" style={{ backgroundColor: hexToRgba(countRowColors.rate, 0.2), color: countRowColors.rate }}>{savedSnippets.length}</span>
                                )}
                                <ChevronDown size={12} className="text-gray-500" style={{ transform: logExpanded ? 'rotate(180deg)' : 'rotate(0deg)', transition: 'transform 0.2s' }} />
                            </button>
                            {showSnippetSaveInput ? (
                                <div className="flex items-center gap-1">
                                    <input
                                        autoFocus
                                        value={snippetNameInput}
                                        onChange={(e) => setSnippetNameInput(e.target.value)}
                                        onKeyDown={(e) => {
                                            if (e.key === 'Enter' && snippetNameInput.trim()) {
                                                setSavedSnippets(prev => [...prev, { id: Date.now(), name: snippetNameInput.trim(), content: files[activeFileIndex]?.content || '', savedAt: new Date().toISOString() }]);
                                                setSnippetNameInput('');
                                                setShowSnippetSaveInput(false);
                                            }
                                            if (e.key === 'Escape') { setShowSnippetSaveInput(false); setSnippetNameInput(''); }
                                        }}
                                        placeholder="Snippet name..."
                                        className="bg-[#050c18] border border-[#1d2d44] rounded px-2 py-1 text-[10px] text-white outline-none w-24"
                                    />
                                    <button
                                        onClick={() => {
                                            if (snippetNameInput.trim()) {
                                                setSavedSnippets(prev => [...prev, { id: Date.now(), name: snippetNameInput.trim(), content: files[activeFileIndex]?.content || '', savedAt: new Date().toISOString() }]);
                                                setSnippetNameInput('');
                                                setShowSnippetSaveInput(false);
                                            }
                                        }}
                                        className="text-[10px] px-1.5 py-1 rounded-md transition-all hover:brightness-125"
                                        style={{ color: countRowColors.count }}
                                        title="Save snippet"
                                    >
                                        <Check size={12} />
                                    </button>
                                    <button
                                        onClick={() => { setShowSnippetSaveInput(false); setSnippetNameInput(''); }}
                                        className="text-[10px] px-1.5 py-1 rounded-md transition-all hover:brightness-125 text-gray-400"
                                    >
                                        <X size={12} />
                                    </button>
                                </div>
                            ) : (
                                <button
                                    onClick={() => { setSnippetNameInput(''); setShowSnippetSaveInput(true); }}
                                    className="text-[10px] px-3 py-1.5 rounded-lg transition-all hover:brightness-125 font-bold"
                                    style={{ backgroundColor: hexToRgba(countRowColors.count, 0.15), color: countRowColors.count, border: `1px solid ${hexToRgba(countRowColors.count, 0.35)}` }}
                                >
                                    Save
                                </button>
                            )}
                        </div>
                        {logExpanded && (
                            <div className="border-t border-[#1d2d44] max-h-[240px] overflow-y-auto">
                                {savedSnippets.length === 0 ? (
                                    <p className="text-[11px] text-gray-400 italic px-4 py-3">No saved snippets yet. Press Save to save your current code.</p>
                                ) : (
                                    savedSnippets.map(snippet => (
                                        <div
                                            key={snippet.id}
                                            className="flex items-center justify-between gap-2 px-4 py-2 cursor-pointer transition-all hover:bg-[#0d1b2a]/50 border-b border-[#1d2d44]/50 last:border-b-0"
                                            onClick={() => {
                                                const updatedFiles = [...files];
                                                if (updatedFiles[activeFileIndex]) {
                                                    updatedFiles[activeFileIndex].content = snippet.content;
                                                    setFiles(updatedFiles);
                                                }
                                            }}
                                        >
                                            <div className="flex-1 min-w-0">
                                                <span className="text-[11px] font-bold text-gray-200 block truncate">{snippet.name}</span>
                                                <span className="text-[9px] text-gray-500 block truncate">{snippet.content.slice(0, 80)}{snippet.content.length > 80 ? '...' : ''}</span>
                                            </div>
                                            <button
                                                onClick={(e) => { e.stopPropagation(); setSavedSnippets(prev => prev.filter(s => s.id !== snippet.id)); }}
                                                className="p-1 rounded-md transition-all hover:brightness-125 flex-shrink-0"
                                                style={{ color: toolPanelColors.failed }}
                                                title="Delete snippet"
                                            >
                                                <Trash2 size={12} />
                                            </button>
                                        </div>
                                    ))
                                )}
                            </div>
                        )}
                    </div>
                    </>
                )}
            </div>

            {!plainMode && (
                <div
                    className="fixed z-20 w-full max-w-2xl"
                    style={{
                        left: 0,
                        right: 0,
                        margin: '0 auto',
                        top: `${Math.max(headerHeight + 8, 78)}px`,
                        paddingLeft: 'max(1rem, calc(var(--safe-area-inset-left, 0px) + 1rem))',
                        paddingRight: 'max(1rem, calc(var(--safe-area-inset-right, 0px) + 1rem))',
                    }}
                >
                    <div
                        style={{
                            height: '190px',
                            display: 'flex',
                            flexDirection: 'column',
                            ...sharedPanelSurface,
                            borderRadius: '0.75rem',
                            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
                        }}
                    >
                        <div style={{ flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '0.75rem', padding: '0.75rem 1rem 0.25rem 1rem', borderTopLeftRadius: '0.75rem', borderTopRightRadius: '0.75rem' }}>
                            <h2 style={{ fontSize: '1.125rem', fontWeight: 700, color: editorColors.text, margin: 0 }}>#{exercise.id}</h2>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                                <button onClick={openProblemAi} title="Ask AI about this problem" style={{ backgroundColor: showModal === 'problem_ai' ? hexToRgba(toolPanelColors.ai, 0.15) : 'transparent', border: `1px solid ${panelBorderSoft}`, borderRadius: '0.5rem', padding: '0.25rem 0.5rem', color: toolPanelColors.ai, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.75rem', flexShrink: 0, pointerEvents: 'auto', transition: 'all 0.2s ease' }}>
                                    <Bot size={14} />
                                    <span>AI</span>
                                </button>
                                <button onClick={saveCurrentProblem} title={isProblemSaved(exercise.id) ? 'Saved' : 'Save problem'} style={{ backgroundColor: isProblemSaved(exercise.id) ? hexToRgba(countRowColors.count, 0.15) : 'transparent', border: `1px solid ${panelBorderSoft}`, borderRadius: '0.5rem', padding: '0.25rem 0.5rem', color: countRowColors.count, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.75rem', flexShrink: 0, pointerEvents: 'auto', opacity: isProblemSaved(exercise.id) ? 1 : 0.7, transition: 'all 0.2s ease' }}>
                                    <Bookmark size={14} fill={isProblemSaved(exercise.id) ? 'currentColor' : 'none'} />
                                    <span>{isProblemSaved(exercise.id) ? 'Saved' : 'Save'}</span>
                                </button>
                                <button onClick={() => setShowBreakdownFor(showBreakdownFor === exercise.id ? null : exercise.id)} title="Problem guide and hints" style={{ backgroundColor: showBreakdownFor === exercise.id ? hexToRgba(countRowColors.rate, 0.15) : 'transparent', border: `1px solid ${panelBorderSoft}`, borderRadius: '0.5rem', padding: '0.25rem 0.5rem', color: countRowColors.rate, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.75rem', flexShrink: 0, pointerEvents: 'auto', transition: 'all 0.2s ease' }}>
                                    <Lightbulb size={14} fill={showBreakdownFor === exercise.id ? 'currentColor' : 'none'} />
                                    <span>Guide</span>
                                </button>
                                <button onClick={() => { setPendingNextProblem(false); loadRandomExercise(); }} style={{ backgroundColor: 'transparent', border: `1px solid ${panelBorderSoft}`, borderRadius: '0.5rem', padding: '0.25rem 0.5rem', color: countRowColors.count, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.75rem', flexShrink: 0, pointerEvents: 'auto' }} title="Load next problem">
                                    <SkipForward size={14} />
                                    <span>Next</span>
                                </button>
                            </div>
                        </div>
                        <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', color: editorColors.problemText, fontSize: '0.875rem', lineHeight: 1.75, whiteSpace: 'pre-wrap', wordWrap: 'break-word', overflowWrap: 'break-word', padding: '0.25rem 1rem 0.75rem', fontFamily: 'inherit', userSelect: 'text', WebkitUserSelect: 'text', WebkitOverflowScrolling: 'touch' }}>
                            {exercise.description}
                            {showBreakdownFor === exercise.id && (
                                <div style={{ marginTop: '0.75rem', borderTop: '1px solid rgba(255, 151, 0, 0.2)', paddingTop: '0.5rem' }}>
                                    <h4 style={{ fontSize: '0.7rem', fontWeight: 700, color: '#FF9700', margin: '0 0 0.35rem', display: 'flex', alignItems: 'center', gap: '0.3rem', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                                        <Lightbulb size={11} /> Guide
                                    </h4>
                                    <div style={{ display: 'grid', gap: '0.55rem', color: '#c8cdd5', fontSize: '0.8125rem', lineHeight: 1.65 }}>
                                        {(() => {
                                            const sections = buildExerciseGuideSections(exercise);
                                            return sections.map((section, sectionIndex) => {
                                                const sectionStyle = getGuideSectionStyle(section.tone);
                                                return (
                                                <div
                                                    key={`guide-section-${section.title}`}
                                                    style={{
                                                        border: `1px solid ${sectionStyle.borderColor}`,
                                                        backgroundColor: sectionStyle.backgroundColor,
                                                        borderRadius: '0.7rem',
                                                        padding: '0.55rem 0.65rem',
                                                    }}
                                                >
                                                    <div style={{ color: sectionStyle.color, fontSize: '0.66rem', fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase', marginBottom: '0.35rem' }}>
                                                        {section.title}
                                                    </div>
                                                    <div style={{ display: 'grid', gap: '0.35rem' }}>
                                                        {section.lines.map((line, lineIndex) => (
                                                            <div key={`guide-line-${sectionIndex}-${lineIndex}`} style={{ display: 'flex', gap: '0.4rem', alignItems: 'flex-start', whiteSpace: 'pre-wrap', wordWrap: 'break-word', overflowWrap: 'break-word' }}>
                                                                <span style={{ color: sectionStyle.color, fontSize: '0.7rem', lineHeight: 1.7, flexShrink: 0 }}>{section.tone === 'steps' ? `${lineIndex + 1}.` : '•'}</span>
                                                                <span>{renderAiParagraphText(line, editorColors, `guide-line-${sectionIndex}-${lineIndex}`)}</span>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                                );
                                            });
                                        })()}
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            )}

            {descCopied && (
                <div className="fixed left-1/2 z-[200] -translate-x-1/2 top-24 text-center px-4 py-2 rounded-lg text-xs text-[#4ade80] font-bold bg-[#050c18]/90 border border-[#4ade80]/30 shadow-xl pointer-events-none">
                    Problem copied to clipboard
                </div>
            )}
            <div
                className="fixed left-1/2 z-[110] w-full max-w-2xl -translate-x-1/2 px-4"
                style={{
                    top: `${editorToolbarTop}px`,
                    pointerEvents: 'none'
                }}
            >
                <div
                        className="flex items-center justify-between rounded-xl border p-2 shadow-2xl shadow-black/40"
                    style={{
                        ...sharedPanelSurface,
                        pointerEvents: 'auto',
                    }}
                >
                    <div className="flex items-center gap-2 overflow-hidden">
                        <button onClick={startRenaming} className="p-1 hover:bg-[#1d2d44] rounded-full" style={{ color: toolPanelColors.fileText }}><Pencil size={14} /></button>
                        {isEditingFileName ? (
                            <input autoFocus value={newName} onChange={(e) => setNewName(e.target.value)} onBlur={finishRenaming} onKeyDown={(e) => e.key === 'Enter' && finishRenaming()} className="bg-[#112240] text-sm border border-[#3b82f6] rounded px-2 py-0.5 outline-none text-white w-24" />
                        ) : (
                            <span className="text-sm font-bold font-mono truncate max-w-[100px]" style={{ color: toolPanelColors.fileText }}>{files[activeFileIndex].name}</span>
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
                    paddingBottom: `max(16rem, calc(env(safe-area-inset-bottom) + ${Math.max(headerHeight + 490, 620)}px))`,
                    scrollPaddingTop: `${editorContentTop}px`,
                    WebkitOverflowScrolling: 'touch',
                    overscrollBehaviorY: 'contain'
                }}
            >
                <div
                    data-editor-panel
                    className="mb-28 rounded-xl flex flex-col shadow-2xl border overflow-hidden"
                    style={{ scrollMarginTop: `${editorContentTop + 12}px`, backgroundColor: panelColors.background, borderColor: panelColors.border }}
                >
                    <div
                        className="hidden"
                    >
                        <div className="flex items-center gap-2 overflow-hidden">
                            <button onClick={startRenaming} className="p-1 hover:bg-[#1d2d44] rounded-full" style={{ color: toolPanelColors.fileText }}><Pencil size={14} /></button>
                            {isEditingFileName ? (
                                <input autoFocus value={newName} onChange={(e) => setNewName(e.target.value)} onBlur={finishRenaming} onKeyDown={(e) => e.key === 'Enter' && finishRenaming()} className="bg-[#112240] text-sm border border-[#3b82f6] rounded px-2 py-0.5 outline-none text-white w-24" />
                            ) : (
                                <span className="text-sm font-bold font-mono truncate max-w-[100px]" style={{ color: toolPanelColors.fileText }}>{files[activeFileIndex].name}</span>
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
                        className="flex border-b overflow-x-auto no-scrollbar"
                        style={{ position: 'sticky', top: 0, zIndex: 50, backgroundColor: panelColors.background, borderColor: panelColors.border }}
                    >
                        {files.map((f, idx) => (
                            <button
                                key={idx}
                                onClick={() => setActiveFileIndex(idx)}
                                className="px-4 py-1.5 text-[10px] font-bold tracking-wider transition-all border-r whitespace-nowrap"
                                style={{
                                    backgroundColor: activeFileIndex === idx ? editorColors.activeTabBackground : panelColors.background,
                                    borderColor: panelColors.border,
                                    borderBottom: activeFileIndex === idx ? `2px solid ${countRowColors.count}` : `1px solid ${panelColors.border}`,
                                    color: activeFileIndex === idx ? toolPanelColors.fileText : editorColors.gutterText,
                                }}
                            >
                                {f.name}
                            </button>
                        ))}
                    </div>
                    <div
                        ref={editorShellRef}
                        className="flex-grow relative border-b"
                        style={{ minHeight: '320px', scrollMarginTop: `${editorContentTop}px`, borderColor: panelBorder }}
                    >
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
                    <div className="flex-shrink-0" style={{ backgroundColor: panelColors.background }}>
                        <div className="flex items-center justify-between px-2 py-1 border-b" style={{ borderColor: panelColors.border }}>
                            <span className="text-xs font-bold uppercase tracking-wider" style={{ color: toolPanelColors.panelLabelText }}>Output</span>
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
                                        : `1px solid ${hexToRgba(panelColors.border, 0.25)}`,
                                borderRadius: '0.75rem',
                                backgroundColor: outputStatus === 'win'
                                    ? 'rgba(12, 45, 28, 0.85)'
                                    : outputStatus === 'fail'
                                        ? 'rgba(64, 15, 20, 0.85)'
                                    : outputStatus === 'running'
                                        ? 'rgba(30, 41, 59, 0.85)'
                                        : hexToRgba(panelColors.background, 1),
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
                        <div
                            className="border-t"
                            style={{ backgroundColor: panelColors.background, borderColor: hexToRgba(panelColors.border, 0.3) }}
                        >
                            <button
                                onClick={() => setShowActionPanel(prev => !prev)}
                                className="w-full flex items-center justify-center gap-2 px-3 py-2 text-[11px] font-black uppercase tracking-[0.18em] transition-colors"
                                style={{ backgroundColor: panelColors.background, color: toolPanelColors.toggleText }}
                            >
                                <span>{showActionPanel ? 'Hide Tools' : 'Show Tools'}</span>
                                {showActionPanel ? <ChevronDown size={14} /> : <ChevronUp size={14} />}
                            </button>
                            {showActionPanel && (
                                <div className="flex justify-center gap-2 sm:gap-3 px-2 pb-3 animate-in fade-in slide-in-from-top-1 duration-200">
                                    <ActionButton icon={<Book size={16} />} iconColor={toolPanelColors.info} description="Info" onClick={() => { setShowModal('instructions'); setModalTab('how'); }} />
                                    <ActionButton icon={<Lightbulb size={16} />} iconColor={toolPanelColors.solution} description="Sol" onClick={() => setShowModal('solution')} />
                                    <ActionButton icon={<Bot size={16} />} iconColor={toolPanelColors.ai} description="AI" onClick={handleAiHint} />
                                    <ActionButton icon={<SlidersHorizontal size={16} />} iconColor={toolPanelColors.custom} description="Custom" onClick={() => setShowModal('customize')} />
                                    <ActionButton icon={<CheckCircle size={16} />} iconColor={toolPanelColors.win} description="Win" onClick={handleMarkSuccess} />
                                    <ActionButton icon={<XCircle size={16} />} iconColor={toolPanelColors.failed} description="Failed" onClick={handleMarkFailed} />
                                    <ActionButton icon={<RotateCcw size={16} />} iconColor={toolPanelColors.reset} description="Reset" onClick={() => { setResetConfirmArmed(false); setShowModal('restart_confirm'); }} />
                                </div>
                            )}
                        </div>
                        <div className="h-2 flex-shrink-0 border-t" style={{ backgroundColor: panelColors.border, borderColor: panelColors.border }} />
                    </div>
                </div>
            </div>

            {/* Fixed footer - centered version button */}
            <div
                className="fixed bottom-0 left-1/2 -translate-x-1/2 w-full max-w-2xl z-20 border-t py-2 px-4"
                style={{ paddingBottom: 'max(0.5rem, env(safe-area-inset-bottom))', backgroundColor: hexToRgba(panelColors.background, panelAlpha), borderColor: panelBorderSoft }}
            >
                <div className="relative flex items-center justify-center">
                     <button onClick={() => window.location.reload()} className="flex items-center gap-2 hover:brightness-125 transition-all px-3 py-2 rounded-full border" title="Reload app" style={{ backgroundColor: countRowColors.iconBackground, borderColor: panelColors.border, color: toolPanelColors.footerText }}
                         onMouseEnter={(e) => { e.currentTarget.style.borderColor = hexToRgba(countRowColors.count, 0.5); e.currentTarget.style.color = countRowColors.count; }}
                         onMouseLeave={(e) => { e.currentTarget.style.borderColor = panelColors.border; e.currentTarget.style.color = toolPanelColors.footerText; }}>
                         <RefreshCw size={18} />
                        <span className="text-xs font-bold tracking-tight">{typeof window !== 'undefined' && (window as any).APP_VERSION || 'PythonV2'}</span>
                        <span className="text-base" title={`Rank: ${userRank.name}`}>{userRank.icon}</span>
                        <span className="rounded-full border px-2 py-0.5 text-[10px] font-black uppercase tracking-[0.14em]" style={{ borderColor: hexToRgba(countRowColors.count, 0.35), backgroundColor: hexToRgba(countRowColors.count, 0.1), color: countRowColors.count }}>{selectedModeLabel}</span>
                    </button>
                </div>
            </div>

            {showModal !== 'none' && (
                <div
                    className="fixed inset-0 backdrop-blur-md flex items-center justify-center p-4 z-[120] animate-in fade-in duration-200"
                    style={{
                        backgroundColor: hexToRgba(panelColors.background, 0.82),
                        paddingTop: 'max(1rem, calc(env(safe-area-inset-top) + 1rem))',
                        paddingBottom: 'max(1rem, calc(env(safe-area-inset-bottom) + 1rem))',
                        paddingLeft: 'max(1rem, calc(env(safe-area-inset-left) + 1rem))',
                        paddingRight: 'max(1rem, calc(env(safe-area-inset-right) + 1rem))'
                    }}
                >
                    <div
                        className="rounded-3xl p-4 sm:p-6 max-w-4xl w-full border border-[#1d2d44] shadow-2xl relative flex flex-col overflow-hidden"
                        style={{
                            backgroundColor: hexToRgba(panelColors.background, showModal === 'settings' || showModal === 'customize' || showModal === 'stats_by_mode' ? 0.82 : 0.96),
                            borderColor: panelColors.border,
                            backdropFilter: 'blur(18px)',
                            WebkitBackdropFilter: 'blur(18px)',
                            height: 'calc(100dvh - 2rem - env(safe-area-inset-top) - env(safe-area-inset-bottom))',
                            maxHeight: 'calc(100dvh - 2rem - env(safe-area-inset-top) - env(safe-area-inset-bottom))'
                        }}
                    >
                        <button onClick={() => setShowModal('none')} className="absolute top-4 right-4 text-gray-400 z-10" aria-label="Close modal"><X size={24} /></button>
                        {showModal === 'instructions' && (
                            <div className="flex flex-col h-full overflow-hidden">
                                <div className="flex gap-4 mb-4 border-b border-[#1d2d44] mx-1 mt-1">
                                    <TabButton active={modalTab === 'cheat'} onClick={() => setModalTab('cheat')} label="Cheat" />
                                    <TabButton active={modalTab === 'glossary'} onClick={() => setModalTab('glossary')} label="Glossary" />
                                    <TabButton active={modalTab === 'regex'} onClick={() => setModalTab('regex')} label="Regex" />
                                    <TabButton active={modalTab === 'builtin'} onClick={() => setModalTab('builtin')} label="Built-in" />
                                    <TabButton active={modalTab === 'how'} onClick={() => setModalTab('how')} label="Rules" />
                                </div>
                                <div className="flex-grow overflow-y-auto">
                                    {modalTab === 'cheat' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={CHEAT_CONTENT} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={CHEAT_CONTENT} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
                                            </div>
                                        </div>
                                    )}
                                    {modalTab === 'glossary' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={GLOSSARY_CONTENT} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={GLOSSARY_CONTENT} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
                                            </div>
                                        </div>
                                    )}
                                    {modalTab === 'regex' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={REGEX_CONTENT} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={REGEX_CONTENT} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
                                            </div>
                                        </div>
                                    )}
                                    {modalTab === 'builtin' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={BUILTIN_CONTENT} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={BUILTIN_CONTENT} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
                                            </div>
                                        </div>
                                    )}
                                    {modalTab === 'how' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={RULES_CONTENT} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={RULES_CONTENT} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
                                            </div>
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
                                    <TabButton active={solutionTab === 'syntax'} onClick={() => setSolutionTab('syntax')} label="Syntax" />
                                </div>
                                <div className="flex-grow overflow-y-auto">
                                    {solutionTab === 'code' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={displaySolution} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                <CodeMirror value={displaySolution} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
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
                                                    <CodeMirror value={logicContent} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
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
                                                    <CodeMirror value={requirementsContent} height="100%" readOnly={true} extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]} />
                                                ) : (
                                                    <div className="p-8 text-center text-gray-500 text-sm">
                                                        Searching requirements...
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    )}
                                    {solutionTab === 'syntax' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] h-full flex flex-col">
                                            <div className="flex justify-end items-center px-3 py-1.5 border-b border-[#1d2d44]">
                                                <CopyButton text={syntaxContent || ''} />
                                            </div>
                                            <div className="flex-1 overflow-auto">
                                                {syntaxContent ? (
                                                    <SyntaxDocumentationPanel content={syntaxContent} />
                                                ) : (
                                                    <div className="p-8 text-center text-gray-500 text-sm">
                                                        Searching syntax documentation...
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                        {showModal === 'hint' && (
                            <div className="flex h-full min-h-0 flex-col gap-3">
                                <h2 className="text-lg font-bold" style={{ color: toolPanelColors.ai }}>AI Review</h2>
                                <div className="min-h-0 flex-1 overflow-y-auto -mx-1 px-1 space-y-3">
                                    <>
                                            {aiReviewRunning && (
                                                <div className="rounded-2xl border px-3 py-2 text-xs font-black uppercase tracking-[0.12em]" style={{ borderColor: hexToRgba(toolPanelColors.ai, 0.35), backgroundColor: hexToRgba(toolPanelColors.ai, 0.08), color: toolPanelColors.ai }}>
                                                    Local model is checking this exact problem, code, output, and grader result...
                                                </div>
                                            )}
                                            {/* Problem section */}
                                            {exercise && (
                                                <div className="rounded-2xl border p-3" style={{ borderColor: 'rgba(88, 118, 160, 0.25)', backgroundColor: 'rgba(8, 18, 34, 0.4)' }}>
                                                    <div className="mb-1.5 text-[10px] font-black uppercase tracking-[0.16em]" style={{ color: countRowColors.rate }}>Problem {exercise.id}</div>
                                                    <p className="text-[13px] leading-relaxed text-gray-200">{exercise.description}</p>
                                                </div>
                                            )}

                                            {/* User code section */}
                                            {latestAiReviewRequest?.userCode && (
                                                <div className="rounded-2xl border overflow-hidden" style={{ borderColor: 'rgba(88, 118, 160, 0.25)' }}>
                                                    <div className="flex items-center justify-between px-3 py-1.5" style={{ backgroundColor: 'rgba(8, 18, 34, 0.6)', borderBottom: '1px solid rgba(88, 118, 160, 0.15)' }}>
                                                        <span className="text-[10px] font-black uppercase tracking-[0.16em] text-gray-400">Your Code</span>
                                                        <span className="text-[10px] text-gray-500">{latestAiReviewRequest.userCode.split('\n').length} lines</span>
                                                    </div>
                                                    <div className="max-h-[240px] overflow-y-auto" style={{ backgroundColor: 'rgba(5, 12, 24, 0.5)' }}>
                                                        <CodeMirror
                                                            value={latestAiReviewRequest.userCode}
                                                            height="auto"
                                                            readOnly={true}
                                                            extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(editorColors)]}
                                                            theme="none"
                                                            basicSetup={{ lineNumbers: true, foldGutter: false, highlightActiveLine: false, bracketMatching: true }}
                                                        />
                                                    </div>
                                                </div>
                                            )}

                                            {/* Analysis section */}
                                            {latestAiReviewResult ? (
                                                <div className="space-y-3">
                                                    <div className="flex flex-wrap items-center gap-2">
                                                        <span className="rounded-full border px-3 py-1 text-[11px] font-black uppercase tracking-[0.12em]"
                                                            style={{
                                                                borderColor: latestAiReviewResult.verdict === 'likely_correct' ? 'rgba(34, 197, 94, 0.4)' : latestAiReviewResult.verdict === 'likely_incorrect' ? 'rgba(239, 68, 68, 0.4)' : 'rgba(251, 191, 36, 0.4)',
                                                                backgroundColor: latestAiReviewResult.verdict === 'likely_correct' ? 'rgba(34, 197, 94, 0.15)' : latestAiReviewResult.verdict === 'likely_incorrect' ? 'rgba(239, 68, 68, 0.15)' : 'rgba(251, 191, 36, 0.15)',
                                                                color: latestAiReviewResult.verdict === 'likely_correct' ? '#86efac' : latestAiReviewResult.verdict === 'likely_incorrect' ? '#fca5a5' : '#fde68a',
                                                            }}
                                                        >
                                                            {latestAiReviewResult.verdict.replace('_', ' ')}
                                                        </span>
                                                        <span className="text-xs text-gray-400">
                                                            Confidence {Math.round(latestAiReviewResult.confidence * 100)}% · {getAiReviewSourceLabel(latestAiReviewResult.source)}
                                                        </span>
                                                    </div>
                                                    <AiReviewText text={latestAiReviewResult.explanation} editorColors={editorColors} accentColor={toolPanelColors.ai} numbered={true} />
                                                    {latestAiReviewResult.suggestedFix && (
                                                        <div className="rounded-xl border p-3" style={{ borderColor: 'rgba(251, 191, 36, 0.3)', backgroundColor: 'rgba(251, 191, 36, 0.08)' }}>
                                                            <div className="mb-1 text-[10px] font-black uppercase tracking-[0.16em]" style={{ color: '#fbbf24' }}>Suggested Fix</div>
                                                            <AiReviewText text={latestAiReviewResult.suggestedFix} editorColors={editorColors} accentColor="#fbbf24" detectBareCode={true} />
                                                        </div>
                                                    )}
                                                    {latestAiReviewResult.verdict === 'likely_correct' && latestAiReviewRequest?.graderPassed === false && (
                                                        <div className="rounded-xl border p-3" style={{ borderColor: 'rgba(34, 197, 94, 0.35)', backgroundColor: 'rgba(34, 197, 94, 0.1)' }}>
                                                            <p className="text-sm" style={{ color: '#86efac' }}>AI Suggested Win: review this answer and use the manual Win button if you agree.</p>
                                                        </div>
                                                    )}
                                                </div>
                                            ) : (
                                                <p className="whitespace-pre-wrap text-sm text-gray-400">{aiHintText || 'Press Run first for the strongest review, or press AI again to analyze the current code.'}</p>
                                            )}

                                            {/* Grader message section */}
                                            {latestAiReviewRequest?.graderMessage && (
                                                <div className="rounded-2xl border max-h-36 overflow-y-auto p-3" style={{ borderColor: 'rgba(239, 68, 68, 0.3)', backgroundColor: 'rgba(239, 68, 68, 0.08)' }}>
                                                    <div className="mb-1 text-[10px] font-black uppercase tracking-[0.12em]" style={{ color: '#fecaca' }}>Grader Message</div>
                                                    <div className="whitespace-pre-wrap text-xs" style={{ color: '#fecaca' }}>{latestAiReviewRequest.graderMessage}</div>
                                                </div>
                                            )}
                                    </>
                                </div>
                            </div>
                        )}
                        {showModal === 'problem_ai' && (
                            <div className="flex h-full min-h-0 flex-col gap-3">
                                <div className="flex flex-shrink-0 items-start justify-between gap-3">
                                    <div>
                                        <h2 className="text-lg font-bold" style={{ color: toolPanelColors.ai }}>Problem AI</h2>
                                        <p className="mt-1 text-xs text-gray-400">Ask about Problem {exercise.id}, your code, output, or why the grader failed.</p>
                                    </div>
                                    <span className="rounded-full border px-2.5 py-1 text-[10px] font-black uppercase tracking-[0.12em]" style={{ borderColor: hexToRgba(toolPanelColors.ai, 0.35), color: toolPanelColors.ai, backgroundColor: hexToRgba(toolPanelColors.ai, 0.08) }}>
                                        {offlineAiState.status === 'ready' ? 'Offline AI' : 'Built-in help'}
                                    </span>
                                </div>

                                <div className="grid grid-cols-2 gap-2 text-[11px]">
                                    {['Explain task', 'Why failed?', 'What method?', 'Show hint'].map(prompt => (
                                        <button
                                            key={prompt}
                                            onClick={() => sendProblemAiQuestion(prompt)}
                                            disabled={problemAiRunning}
                                            className="rounded-xl border px-3 py-2 text-left font-bold transition-all hover:brightness-125 disabled:opacity-50"
                                            style={{ borderColor: hexToRgba(toolPanelColors.ai, 0.25), backgroundColor: hexToRgba(toolPanelColors.ai, 0.07), color: '#dbeafe' }}
                                        >
                                            {prompt}
                                        </button>
                                    ))}
                                </div>

                                <div className="min-h-0 flex-1 space-y-3 overflow-y-auto pr-1">
                                    {problemAiMessages.map(message => (
                                        <div
                                            key={message.id}
                                            className="rounded-2xl border p-3"
                                            style={{
                                                borderColor: message.role === 'user' ? hexToRgba(countRowColors.count, 0.3) : hexToRgba(toolPanelColors.ai, 0.28),
                                                backgroundColor: message.role === 'user' ? hexToRgba(countRowColors.count, 0.08) : 'rgba(8, 18, 34, 0.55)',
                                            }}
                                        >
                                            <div className="mb-1.5 flex items-center justify-between gap-2">
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]" style={{ color: message.role === 'user' ? countRowColors.count : toolPanelColors.ai }}>
                                                    {message.role === 'user' ? 'You' : 'Problem AI'}
                                                </span>
                                                {message.source && message.role === 'assistant' && (
                                                    <span className="text-[10px] text-gray-500">{message.source === 'offline' ? 'Offline AI' : 'Built-in help'}</span>
                                                )}
                                            </div>
                                            {message.role === 'assistant' ? (
                                                <ProblemAiText text={message.text} editorColors={editorColors} accentColor={toolPanelColors.ai} />
                                            ) : (
                                                <p className="whitespace-pre-wrap text-sm leading-relaxed text-gray-100">{message.text}</p>
                                            )}
                                        </div>
                                    ))}
                                    {problemAiRunning && (
                                        <div className="rounded-2xl border px-3 py-2 text-xs font-black uppercase tracking-[0.12em]" style={{ borderColor: hexToRgba(toolPanelColors.ai, 0.35), backgroundColor: hexToRgba(toolPanelColors.ai, 0.08), color: toolPanelColors.ai }}>
                                            Thinking about this problem...
                                        </div>
                                    )}
                                </div>

                                <form
                                    className="flex flex-shrink-0 gap-2 border-t border-[#1d2d44] pt-3"
                                    onSubmit={(event) => {
                                        event.preventDefault();
                                        sendProblemAiQuestion(problemAiDraft);
                                    }}
                                >
                                    <input
                                        value={problemAiDraft}
                                        onChange={(event) => setProblemAiDraft(event.target.value)}
                                        placeholder="Ask about this problem..."
                                        className="min-w-0 flex-1 rounded-xl border bg-[#050c18] px-3 py-2 text-sm text-white placeholder-gray-500 focus:outline-none"
                                        style={{ borderColor: hexToRgba(toolPanelColors.ai, 0.3) }}
                                    />
                                    <button
                                        type="submit"
                                        disabled={!problemAiDraft.trim() || problemAiRunning}
                                        className="rounded-xl border px-4 py-2 text-xs font-black uppercase tracking-[0.12em] transition-all hover:brightness-125 disabled:opacity-40"
                                        style={{ borderColor: hexToRgba(toolPanelColors.ai, 0.4), backgroundColor: hexToRgba(toolPanelColors.ai, 0.15), color: toolPanelColors.ai }}
                                    >
                                        Ask
                                    </button>
                                </form>
                            </div>
                        )}
                        {showModal === 'customize' && (
                            <div className="flex h-full min-h-0 flex-col py-2">
                                <h2 className="mb-4 flex-shrink-0 text-center text-lg font-bold">Customize</h2>
                                <div className="mb-4 flex flex-shrink-0 gap-3 border-b border-[#1d2d44]">
                                    <TabButton active={customizeTab === 'count'} onClick={() => setCustomizeTab('count')} label="Count Row" />
                                    <TabButton active={customizeTab === 'ide'} onClick={() => setCustomizeTab('ide')} label="IDE" />
                                    <TabButton active={customizeTab === 'tools'} onClick={() => setCustomizeTab('tools')} label="Tools" />
                                    <TabButton active={customizeTab === 'panels'} onClick={() => setCustomizeTab('panels')} label="Panels" />
                                </div>
                                <div className="min-h-0 flex-1 overflow-y-auto overscroll-contain pr-1 pb-8">
                                    {customizeTab === 'count' && (
                                        <div className="space-y-4">
                                            <div
                                                className="flex flex-wrap items-center justify-center gap-3 rounded-2xl px-4 py-3 text-xs font-black"
                                                style={{ backgroundColor: hexToRgba(panelColors.background, panelAlpha), border: `1px solid ${hexToRgba(panelColors.border, 0.3)}` }}
                                            >
                                                <span className="rounded-full border p-1" style={{ color: countRowColors.icon, backgroundColor: countRowColors.iconBackground, borderColor: panelColors.border }}><Key size={14} /></span>
                                                <span><span className="uppercase" style={{ color: countRowColors.count }}>Count:</span> <span style={{ color: countRowColors.value }}>12</span></span>
                                                <span><span className="uppercase" style={{ color: countRowColors.wins }}>Wins:</span> <span style={{ color: countRowColors.value }}>8</span></span>
                                                <span><span className="uppercase" style={{ color: countRowColors.fail }}>Fail:</span> <span style={{ color: countRowColors.value }}>4</span></span>
                                                <span className="pl-3" style={{ borderLeft: `1px solid ${hexToRgba(panelColors.border, 0.3)}` }}><span className="uppercase" style={{ color: countRowColors.rate }}>Rate:</span> <span style={{ color: countRowColors.value }}>67%</span></span>
                                                <span className="rounded-full border p-1" style={{ color: countRowColors.icon, backgroundColor: countRowColors.iconBackground, borderColor: panelColors.border }}><Settings size={14} /></span>
                                            </div>
                                            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                                                {([
                                                    ['count', 'Count Text'],
                                                    ['wins', 'Wins Text'],
                                                    ['fail', 'Fail Text'],
                                                    ['rate', 'Rate Text'],
                                                    ['value', 'Stats Value Text'],
                                                    ['icon', 'Icon Color'],
                                                    ['iconBackground', 'Icon Background'],
                                                ] as Array<[keyof Omit<CountRowColorSettings, 'background' | 'border'>, string]>).map(([key, label]) => (
                                                    <ColorField
                                                        key={key}
                                                        label={label}
                                                        value={countRowColors[key]}
                                                        onChange={(value) => setCountRowColors(prev => ({ ...prev, [key]: value }))}
                                                    />
                                                ))}
                                            </div>
                                            <button
                                                onClick={() => setCountRowColors(DEFAULT_COUNT_ROW_COLORS)}
                                                className="w-full rounded-xl border px-4 py-3 text-xs font-black uppercase tracking-[0.14em] transition-all hover:brightness-125"
                                                style={{ borderColor: hexToRgba(countRowColors.count, 0.35), backgroundColor: hexToRgba(countRowColors.count, 0.1), color: countRowColors.count }}
                                             >
                                                  Reset Count Row Defaults
                                            </button>
                                        </div>
                                    )}
                                    {customizeTab === 'ide' && (
                                        <div className="space-y-4">
                                            <div
                                                className="rounded-2xl border p-3"
                                                style={{ backgroundColor: panelBackground, borderColor: panelBorder }}
                                            >
                                                <div className="mb-2 flex items-center justify-between">
                                                    <div className="text-[10px] font-black uppercase tracking-[0.14em]" style={{ color: editorColors.gutterText }}>Problem Panel Preview</div>
                                                    <span className="rounded-lg border px-2 py-1 text-[10px] font-black" style={{ borderColor: panelBorder, color: countRowColors.count }}>Next</span>
                                                </div>
                                                <p className="m-0 text-sm leading-6" style={{ color: editorColors.problemText }}>Write a Python function, test different variable names, and solve the problem using the required logic.</p>
                                            </div>
                                            <div
                                                className="rounded-2xl border p-3"
                                                style={{ backgroundColor: panelBackground, borderColor: panelBorder }}
                                            >
                                                <div className="mb-2 text-[10px] font-black uppercase tracking-[0.14em]" style={{ color: editorColors.gutterText }}>Live IDE Preview</div>
                                                <div className="mb-2 flex overflow-hidden rounded-xl border text-[10px] font-bold" style={{ borderColor: panelBorder, backgroundColor: panelBackground }}>
                                                    <span className="px-3 py-1.5" style={{ backgroundColor: editorColors.activeTabBackground, color: toolPanelColors.fileText, borderRight: `1px solid ${panelBorder}` }}>main.py</span>
                                                    <span className="px-3 py-1.5" style={{ color: editorColors.gutterText }}>helper.py</span>
                                                </div>
                                                <CodeMirror
                                                    value={"# comment\nnumber = 42\ntext = 'Python'\nprint(text)\nif number > 10:\n    return True"}
                                                    height="150px"
                                                    readOnly={true}
                                                    extensions={[python(), EditorView.lineWrapping, ...createCustomPythonTheme(effectiveEditorColors)]}
                                                />
                                                <div className="mt-2 rounded-xl border px-3 py-2 font-mono text-[10px]" style={{ backgroundColor: panelBackground, borderColor: panelBorder, color: '#4ade80' }}>
                                                    Output preview: code results appear here
                                                </div>
                                            </div>
                                            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                                                {([
                                                    ['problemText', 'Problem Text'],
                                                    ['activeTabBackground', 'Active File Tab'],
                                                    ['text', 'Code Text'],
                                                    ['gutterText', 'Line Number Text'],
                                                    ['comment', 'Comment'],
                                                    ['identifier', 'Identifier'],
                                                    ['builtin', 'Built-in'],
                                                    ['keyword', 'Keyword'],
                                                    ['number', 'Number'],
                                                    ['string', 'String'],
                                                ] as Array<[keyof EditorColorSettings, string]>).map(([key, label]) => (
                                                    <ColorField
                                                        key={key}
                                                        label={label}
                                                        value={editorColors[key]}
                                                        onChange={(value) => setEditorColors(prev => ({ ...prev, [key]: value }))}
                                                    />
                                                ))}
                                            </div>
                                            <button
                                                onClick={() => setEditorColors(DEFAULT_EDITOR_COLORS)}
                                                className="w-full rounded-xl border px-4 py-3 text-xs font-black uppercase tracking-[0.14em] transition-all hover:brightness-125"
                                                style={{ borderColor: hexToRgba(countRowColors.count, 0.35), backgroundColor: hexToRgba(countRowColors.count, 0.1), color: countRowColors.count }}
                                             >
                                                 Reset IDE Defaults
                                            </button>
                                        </div>
                                    )}
                                    {customizeTab === 'tools' && (
                                        <div className="space-y-4">
                                            <div
                                                className="rounded-2xl border p-3"
                                                style={{ backgroundColor: hexToRgba(panelColors.background, panelAlpha), borderColor: hexToRgba(panelColors.border, 0.3) }}
                                            >
                                                <div
                                                    className="mb-3 flex items-center justify-center gap-2 rounded-xl px-3 py-2 text-[11px] font-black uppercase tracking-[0.18em]"
                                                    style={{ backgroundColor: hexToRgba(panelColors.background, panelAlpha), color: toolPanelColors.toggleText }}
                                                >
                                                    <span>Hide Tools</span>
                                                    <ChevronDown size={14} />
                                                </div>
                                                <div className="flex flex-wrap justify-center gap-2">
                                                    <ActionButton icon={<Book size={16} />} iconColor={toolPanelColors.info} description="Info" onClick={() => undefined} />
                                                    <ActionButton icon={<Lightbulb size={16} />} iconColor={toolPanelColors.solution} description="Sol" onClick={() => undefined} />
                                                    <ActionButton icon={<Bot size={16} />} iconColor={toolPanelColors.ai} description="AI" onClick={() => undefined} />
                                                    <ActionButton icon={<SlidersHorizontal size={16} />} iconColor={toolPanelColors.custom} description="Custom" onClick={() => undefined} />
                                                    <ActionButton icon={<CheckCircle size={16} />} iconColor={toolPanelColors.win} description="Win" onClick={() => undefined} />
                                                    <ActionButton icon={<XCircle size={16} />} iconColor={toolPanelColors.failed} description="Failed" onClick={() => undefined} />
                                                    <ActionButton icon={<RotateCcw size={16} />} iconColor={toolPanelColors.reset} description="Reset" onClick={() => undefined} />
                                                </div>
                                            </div>
                                            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                                                {([
                                                    ['fileText', 'main.py Text'],
                                                    ['footerText', 'PythonV2 Text'],
                                                    ['panelLabelText', 'Output Label Text'],
                                                    ['toggleText', 'Toggle Text'],
                                                    ['info', 'Info Tool'],
                                                    ['solution', 'Solution Tool'],
                                                    ['ai', 'AI Tool'],
                                                    ['custom', 'Customize Tool'],
                                                    ['win', 'Win Tool'],
                                                    ['failed', 'Failed Tool'],
                                                    ['reset', 'Reset Tool'],
                                                ] as Array<[keyof Omit<ToolPanelColorSettings, 'panelBackground' | 'panelBorder' | 'toggleBackground'>, string]>).map(([key, label]) => (
                                                    <ColorField
                                                        key={key}
                                                        label={label}
                                                        value={toolPanelColors[key]}
                                                        onChange={(value) => setToolPanelColors(prev => ({ ...prev, [key]: value }))}
                                                    />
                                                ))}
                                            </div>
                                            <button
                                                onClick={() => setToolPanelColors(DEFAULT_TOOL_PANEL_COLORS)}
                                                className="w-full rounded-xl border px-4 py-3 text-xs font-black uppercase tracking-[0.14em] transition-all hover:brightness-125"
                                                style={{ borderColor: hexToRgba(countRowColors.count, 0.35), backgroundColor: hexToRgba(countRowColors.count, 0.1), color: countRowColors.count }}
                                             >
                                                 Reset Tools Defaults
                                            </button>
                                        </div>
                                    )}
                                    {customizeTab === 'panels' && (
                                        <div className="space-y-4">
                                            <div className="relative overflow-hidden rounded-2xl border border-[#1d2d44]">
                                                {/* Opaque output panel (IDE + output) behind the transparent panels */}
                                                <div className="absolute inset-0 p-3" style={{ backgroundColor: panelColors.background }}>
                                                    <div className="mb-2 rounded-lg border px-2 py-1.5 font-mono text-[9px]" style={{ backgroundColor: editorColors.background, borderColor: panelColors.border, color: editorColors.text }}>
                                                        <span style={{ color: editorColors.keyword }}>def</span> <span style={{ color: editorColors.identifier }}>solve</span>(text):
                                                        <br />    <span style={{ color: editorColors.keyword }}>return</span> text[1:-1]
                                                        <br /><br />
                                                        <span style={{ color: editorColors.builtin }}>print</span>(solve(<span style={{ color: editorColors.string }}>"Python"</span>))
                                                    </div>
                                                    <div className="rounded-lg border px-2 py-1.5" style={{ backgroundColor: editorColors.outputBackground, borderColor: panelColors.border }}>
                                                        <div className="text-[9px] font-bold uppercase tracking-wider text-gray-400">Output</div>
                                                        <div className="font-mono text-[10px] text-[#4ade80]">ytho</div>
                                                    </div>
                                                </div>
                                                {/* Transparent overlay panels */}
                                                <div className="relative space-y-2 p-3">
                                                    <div className="flex flex-wrap items-center justify-center gap-2 rounded-full px-3 py-2 text-[9px] font-black" style={{ backgroundColor: hexToRgba(panelColors.background, panelAlpha), border: `1px solid ${hexToRgba(panelColors.border, 0.3)}` }}>
                                                        <span className="uppercase" style={{ color: '#3b82f6' }}>Count:</span> 12
                                                        <span className="uppercase" style={{ color: '#22c55e' }}>Wins:</span> 8
                                                    </div>
                                                    <div className="rounded-xl px-3 py-3 text-[10px] leading-relaxed text-gray-300" style={{ backgroundColor: hexToRgba(panelColors.background, panelAlpha), border: `1px solid ${hexToRgba(panelColors.border, 0.3)}`, backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)' }}>
                                                        <span className="font-bold text-white">Problem 1005</span>
                                                        <div className="mt-1 text-gray-400">Write a program to remove first and last characters from a string.</div>
                                                    </div>
                                                    <div className="rounded-xl px-3 py-2 text-[10px] text-gray-400" style={{ backgroundColor: hexToRgba(panelColors.background, panelAlpha), border: `1px solid ${hexToRgba(panelColors.border, 0.35)}`, backdropFilter: 'blur(8px)', WebkitBackdropFilter: 'blur(8px)' }}>
                                                        <span className="font-bold text-gray-200">main.py</span>
                                                        <span className="ml-3 uppercase text-[#22c55e]">▶ Run</span>
                                                    </div>
                                                    <div className="rounded-xl px-3 py-3 text-[10px] text-gray-400" style={{ backgroundColor: panelColors.background, border: `1px solid ${hexToRgba(panelColors.border, 0.35)}` }}>
                                                        <span className="font-bold text-gray-200">Output</span>
                                                        <div className="mt-1 font-mono text-[#4ade80]">ytho</div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="space-y-3">
                                                <ColorField label="Panel Background" value={panelColors.background} onChange={(value) => setPanelColors(prev => ({ ...prev, background: value }))} />
                                                <ColorField label="Panel Border" value={panelColors.border} onChange={(value) => setPanelColors(prev => ({ ...prev, border: value }))} />
                                                <label className="flex items-center justify-between gap-3 rounded-xl border border-[#1d2d44] bg-[#050c18]/80 px-3 py-3">
                                                    <span className="min-w-0">
                                                        <span className="block text-xs font-bold text-gray-200">Transparency</span>
                                                        <span className="mt-1 block font-mono text-[10px] text-gray-500">{panelColors.alpha}%</span>
                                                    </span>
                                                    <input
                                                        type="range"
                                                        min={0}
                                                        max={100}
                                                        value={panelColors.alpha}
                                                        onChange={(event) => setPanelColors(prev => ({ ...prev, alpha: Number(event.target.value) }))}
                                                        className="h-2 w-24 cursor-pointer appearance-none rounded-full bg-[#1d2d44] accent-[#3b82f6]"
                                                        aria-label="Panel transparency"
                                                    />
                                                </label>
                                            </div>
                                            <button
                                                onClick={() => setPanelColors(DEFAULT_PANEL_COLORS)}
                                                className="w-full rounded-xl border px-4 py-3 text-xs font-black uppercase tracking-[0.14em] transition-all hover:brightness-125"
                                                style={{ borderColor: hexToRgba(countRowColors.count, 0.35), backgroundColor: hexToRgba(countRowColors.count, 0.1), color: countRowColors.count }}
                                             >
                                                  Reset Panel Defaults
                                            </button>
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                        {showModal === 'settings' && (
                            <div className="flex h-full min-h-0 flex-col py-2">
                                <h2 className="mb-4 flex-shrink-0 text-center text-lg font-bold">Settings</h2>
                                <div className="min-h-0 flex-1 overflow-y-auto overscroll-contain pr-1 pb-8">

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-4 text-center">
                                    <div className="text-4xl mb-2">{userRank.icon}</div>
                                    <h3 className="text-sm font-black uppercase tracking-[0.18em] text-white mb-1">{userRank.name}</h3>
                                    <p className="text-[10px] text-gray-400">
                                        {(() => {
                                            const totalShots = Object.values(statsByMode).reduce((sum, s) => sum + s.shots, 0);
                                            const totalWins = Object.values(statsByMode).reduce((sum, s) => sum + s.success, 0);
                                            const rate = totalShots > 0 ? ((totalWins / totalShots) * 100).toFixed(0) : '0';
                                            return `${totalShots} exercises | ${rate}% win rate`;
                                        })()}
                                    </p>
                                    <div className="mt-2 flex items-center justify-center gap-1">
                                        {RANKS.map((rank, idx) => {
                                            const isActive = rank.name === userRank.name;
                                            return (
                                                <div
                                                    key={rank.name}
                                                    className="w-1.5 h-1.5 rounded-full transition-all"
                                                    style={{ backgroundColor: isActive ? countRowColors.count : '#1d2d44', width: isActive ? '0.75rem' : '0.375rem', height: '0.375rem' }}
                                                    title={rank.name}
                                                />
                                            );
                                        })}
                                    </div>
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 flex items-center gap-2 text-xs font-black uppercase tracking-[0.16em] text-gray-200">
                                        <Terminal size={14} style={{ color: countRowColors.count }} /> Mode
                                    </h3>
                                    <div className="grid grid-cols-2 gap-2">
                                        <button
                                            onClick={() => { setPlainMode(false); setExercise(getInitialExercise()); setFiles([{ name: 'main.py', content: getInitialExercise().initialCode }]); }}
                                            className="rounded-xl border px-3 py-3 text-left transition-all hover:brightness-125"
                                            style={!plainMode ? { borderColor: hexToRgba(countRowColors.wins, 0.6), backgroundColor: hexToRgba(countRowColors.wins, 0.15), color: '#ffffff' } : { borderColor: '#1d2d44', backgroundColor: 'rgba(5, 12, 24, 0.7)', color: '#9ca3af' }}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <span className="text-xs font-black uppercase tracking-[0.14em]">Play</span>
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]" style={{ color: !plainMode ? countRowColors.wins : '#6b7280' }}>On</span>
                                            </span>
                                            <span className="block text-xs font-bold">Exercises</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">Practice with problems.</span>
                                        </button>
                                        <button
                                            onClick={() => { setPlainMode(true); setFiles([{ name: 'main.py', content: '' }]); setOutput(''); setOutputStatus('idle'); }}
                                            className="rounded-xl border px-3 py-3 text-left transition-all hover:brightness-125"
                                            style={plainMode ? { borderColor: hexToRgba(countRowColors.count, 0.6), backgroundColor: hexToRgba(countRowColors.count, 0.15), color: '#ffffff' } : { borderColor: '#1d2d44', backgroundColor: 'rgba(5, 12, 24, 0.7)', color: '#9ca3af' }}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <span className="text-xs font-black uppercase tracking-[0.14em]">Plain</span>
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]" style={{ color: plainMode ? countRowColors.count : '#6b7280' }}>On</span>
                                            </span>
                                            <span className="block text-xs font-bold">Free IDE</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">No problems, just code.</span>
                                        </button>
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
                                            className="rounded-xl border px-3 py-3 text-left transition-all hover:brightness-125"
                                            style={keyboardHaptics ? { borderColor: hexToRgba(countRowColors.wins, 0.6), backgroundColor: hexToRgba(countRowColors.wins, 0.15), color: '#ffffff' } : { borderColor: '#1d2d44', backgroundColor: 'rgba(5, 12, 24, 0.7)', color: '#9ca3af' }}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <Vibrate size={15} style={{ color: keyboardHaptics ? countRowColors.wins : '#6b7280' }} />
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]">{keyboardHaptics ? 'On' : 'Off'}</span>
                                            </span>
                                            <span className="block text-xs font-bold">Haptic</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">Tiny vibration while typing.</span>
                                        </button>
                                        <button
                                            onClick={() => setKeyboardSound(prev => !prev)}
                                            className="rounded-xl border px-3 py-3 text-left transition-all hover:brightness-125"
                                            style={keyboardSound ? { borderColor: hexToRgba(countRowColors.wins, 0.6), backgroundColor: hexToRgba(countRowColors.wins, 0.15), color: '#ffffff' } : { borderColor: '#1d2d44', backgroundColor: 'rgba(5, 12, 24, 0.7)', color: '#9ca3af' }}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <Volume2 size={15} style={{ color: keyboardSound ? countRowColors.wins : '#6b7280' }} />
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]">{keyboardSound ? 'On' : 'Off'}</span>
                                            </span>
                                            <span className="block text-xs font-bold">Sound</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">Soft key click in editor.</span>
                                        </button>
                                        <button
                                            onClick={() => setResultSound(prev => !prev)}
                                            className="rounded-xl border px-3 py-3 text-left transition-all hover:brightness-125"
                                            style={resultSound ? { borderColor: hexToRgba(countRowColors.wins, 0.6), backgroundColor: hexToRgba(countRowColors.wins, 0.15), color: '#ffffff' } : { borderColor: '#1d2d44', backgroundColor: 'rgba(5, 12, 24, 0.7)', color: '#9ca3af' }}
                                        >
                                            <span className="mb-2 flex items-center justify-between gap-2">
                                                <Zap size={15} style={{ color: resultSound ? countRowColors.wins : '#6b7280' }} />
                                                <span className="text-[10px] font-black uppercase tracking-[0.14em]">{resultSound ? 'On' : 'Off'}</span>
                                            </span>
                                            <span className="block text-xs font-bold">Result</span>
                                            <span className="mt-1 block text-[10px] text-gray-400">Cute win/fail sounds after grading.</span>
                                        </button>
                                    </div>
                                </div>

                                <div className="mb-6">
                                    <label className="block text-sm font-bold mb-2 text-gray-200">
                                        <span>Problem Mode</span>
                                        <button onClick={() => setShowHowToUse(!showHowToUse)} className="inline-flex items-center ml-2 align-middle transition-all hover:brightness-125" title="How to use this app">
                                            <Info size={14} style={{ color: countRowColors.count }} />
                                        </button>
                                    </label>
                                    <div className="grid grid-cols-1 gap-2">
                                        {DIFFICULTY_MODES.map(mode => {
                                            const isSelected = difficultyMode === mode.id;
                                            return (
                                                <button
                                                    key={mode.id}
                                                    onClick={() => handleDifficultyModeSelect(mode.id)}
                                                    className="w-full rounded-xl border px-3 py-2 text-left transition-all hover:brightness-125"
                                                    style={isSelected ? { borderColor: countRowColors.count, backgroundColor: hexToRgba(countRowColors.count, 0.25), color: '#ffffff' } : { borderColor: '#1d2d44', backgroundColor: 'rgba(7, 18, 37, 0.7)', color: '#9ca3af' }}
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
                                    {showHowToUse && (
                                        <div className="mt-3 rounded-xl border border-[#1d2d44] bg-[#071225]/80 p-4 text-[11px] text-gray-300 leading-relaxed space-y-2">
                                            <p className="font-bold text-white text-xs">How to use this app</p>
                                            <p>Choose a mode above — Beginner, Intermediate, Expert, or Legend — to filter problems by difficulty, or use Normal to see everything mixed together.</p>
                                            <p className="font-bold text-white text-xs mt-3">Win / Failed Tools</p>
                                            <p>When you run code, the auto-grader tries to check your answer, but it's <span className="text-yellow-300">not 100% accurate</span>. Use the <CheckCircle size={12} className="inline align-text-top" style={{ color: toolPanelColors.win }} /> <strong>Win</strong> and <XCircle size={12} className="inline align-text-top" style={{ color: toolPanelColors.failed }} /> <strong>Failed</strong> buttons at the bottom to manually mark the result. This is how your rank and win rate are tracked — the more you get right, and the more problems you do, the higher your rank climbs.</p>
                                            <p className="font-bold text-white text-xs mt-3">Settings</p>
                                            <p>Customize colors, haptic feedback, keyboard sound, and tool panel appearance from the <SlidersHorizontal size={12} className="inline align-text-top" /> Customize section above. Your progress is saved automatically in this browser.</p>
                                            <p className="font-bold text-white text-xs mt-3">Ranking</p>
                                            <p>Your rank is calculated from <strong>all modes combined</strong> using a weighted score: <code className="text-[#93c5fd]">shots × winRate</code>. Doing more problems and keeping a high win rate both matter.</p>
                                        </div>
                                    )}
                                    <p className="mt-2 text-[10px] text-gray-300">
                                        Current mode has {modeExerciseCount} matching problems. Normal mode uses all problems.
                                    </p>
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-gray-200">Stats By Mode</h3>
                                    <div className="grid grid-cols-[1fr_52px_52px_52px_52px_52px] gap-x-2 gap-y-1.5 text-[11px]">
                                        <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500">Mode</div>
                                        <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Count</div>
                                        <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Wins</div>
                                        <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Fails</div>
                                        <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Rate</div>
                                        <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Rank</div>
                                        {DIFFICULTY_MODES.map(mode => {
                                            const modeStats = statsByMode[mode.id] ?? EMPTY_STATS;
                                            const modeRate = modeStats.shots > 0 ? ((modeStats.success / modeStats.shots) * 100).toFixed(0) : '0';
                                            const modeRank = getModeRank(modeStats);
                                            return [
                                                <span key={`${mode.id}-label`} className="font-bold uppercase tracking-[0.12em] text-gray-200 truncate">{mode.label}</span>,
                                                <span key={`${mode.id}-shots`} className="font-mono text-right">{modeStats.shots}</span>,
                                                <span key={`${mode.id}-wins`} className="font-mono text-right" style={{ color: countRowColors.wins }}>{modeStats.success}</span>,
                                                <span key={`${mode.id}-fails`} className="font-mono text-right" style={{ color: toolPanelColors.failed }}>{modeStats.failed}</span>,
                                                <span key={`${mode.id}-rate`} className="font-mono text-right" style={{ color: modeStats.shots > 0 ? countRowColors.rate : 'inherit' }}>{modeRate}%</span>,
                                                <span key={`${mode.id}-rank`} className="font-mono text-right" title={modeRank.name}>{modeRank.icon}</span>,
                                            ];
                                        })}
                                    </div>
                                    <div className="mt-3 border-t border-[#1d2d44] pt-2 grid grid-cols-[1fr_52px_52px_52px_52px_52px] gap-x-2 gap-y-1.5 text-[11px]">
                                        <div className="font-bold uppercase tracking-[0.12em] text-gray-200">Total</div>
                                        <div className="font-mono text-right text-gray-200">{Object.values(statsByMode).reduce((s, m) => s + m.shots, 0)}</div>
                                        <div className="font-mono text-right" style={{ color: countRowColors.wins }}>{Object.values(statsByMode).reduce((s, m) => s + m.success, 0)}</div>
                                        <div className="font-mono text-right" style={{ color: toolPanelColors.failed }}>{Object.values(statsByMode).reduce((s, m) => s + m.failed, 0)}</div>
                                        <div className="font-mono text-right" style={{ color: countRowColors.rate }}>{(() => { const t = Object.values(statsByMode).reduce((s, m) => s + m.shots, 0); const w = Object.values(statsByMode).reduce((s, m) => s + m.success, 0); return t > 0 ? ((w / t) * 100).toFixed(0) + '%' : '0%'; })()}</div>
                                        <div className="font-mono text-right" title={userRank.name}>{userRank.icon}</div>
                                    </div>
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-gray-200 flex items-center gap-2">
                                        <Bookmark size={14} style={{ color: countRowColors.count }} /> Saved Problems
                                    </h3>
                                    {savedProblems.length === 0 ? (
                                        <p className="text-[11px] text-gray-400 italic">No saved problems yet. Press Save on any problem to add it here.</p>
                                    ) : (
                                        <div className="space-y-1 max-h-[280px] overflow-y-auto pr-1">
                                            {savedProblems.map(problem => {
                                                const isExpanded = expandedSavedProblem === problem.exerciseId;
                                                return (
                                                    <div key={problem.exerciseId} className="rounded-lg border overflow-hidden" style={{ borderColor: '#1d2d44', backgroundColor: '#050c18' }}>
                                                        <div
                                                            onClick={() => loadSavedProblem(problem)}
                                                            className="flex items-center justify-between gap-2 px-3 py-2 cursor-pointer transition-all hover:brightness-125"
                                                            onMouseEnter={(e) => { if (e.currentTarget) e.currentTarget.style.borderColor = hexToRgba(countRowColors.count, 0.5); }}
                                                            onMouseLeave={(e) => { if (e.currentTarget) e.currentTarget.style.borderColor = '#1d2d44'; }}
                                                        >
                                                            <div className="flex-1 text-left min-w-0">
                                                                <span className="text-[11px] font-bold text-gray-200 block truncate">
                                                                    Problem {problem.exerciseId}
                                                                    {problem.mastered && (
                                                                        <span className="ml-2 text-[10px] font-black uppercase tracking-wider" style={{ color: countRowColors.wins }}>Mastered</span>
                                                                    )}
                                                                </span>
                                                                <span className="text-[10px] text-gray-400 block truncate">
                                                                    {problem.description.split('\n')[0]}
                                                                </span>
                                                            </div>
                                                            <div className="flex items-center gap-1 flex-shrink-0" onClick={(e) => e.stopPropagation()}>
                                                                {!problem.mastered && (
                                                                    <button
                                                                        onClick={() => markSavedProblemMastered(problem.exerciseId)}
                                                                        title="Mark as mastered"
                                                                        className="p-1.5 rounded-md transition-all hover:brightness-125"
                                                                        style={{ color: countRowColors.wins }}
                                                                    >
                                                                        <CheckCircle size={14} />
                                                                    </button>
                                                                )}
                                                                <button
                                                                    onClick={() => handleDeleteConfirm(problem.exerciseId, 'saved')}
                                                                    title="Remove"
                                                                    className="p-1.5 rounded-md transition-all hover:brightness-125"
                                                                    style={{ color: toolPanelColors.failed }}
                                                                >
                                                                    <Trash2 size={14} />
                                                                </button>
                                                                <button
                                                                    onClick={() => setExpandedSavedProblem(isExpanded ? null : problem.exerciseId)}
                                                                    title={isExpanded ? 'Hide details' : 'Show details'}
                                                                    className="p-1.5 rounded-md transition-all hover:brightness-125"
                                                                    style={{ color: hexToRgba(countRowColors.count, 0.7) }}
                                                                >
                                                                    {isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                                                                </button>
                                                            </div>
                                                        </div>
                                                        {isExpanded && (
                                                            <div className="border-t border-[#1d2d44] px-3 py-2.5 space-y-2" style={{ backgroundColor: 'rgba(5, 12, 24, 0.5)' }}>
                                                                <p className="text-[12px] leading-relaxed text-gray-300">{problem.description}</p>
                                                                <div className="flex gap-2">
                                                                    <button
                                                                        onClick={() => loadSavedProblem(problem)}
                                                                        className="flex-1 py-1.5 rounded-lg text-[11px] font-bold transition-all hover:brightness-125"
                                                                        style={{ backgroundColor: hexToRgba(countRowColors.count, 0.15), border: `1px solid ${hexToRgba(countRowColors.count, 0.3)}`, color: countRowColors.count }}
                                                                    >
                                                                        Practice in IDE
                                                                    </button>
                                                                </div>
                                                            </div>
                                                        )}
                                                    </div>
                                                );
                                            })}
                                        </div>
                                    )}
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-3">
                                    <h3 className="mb-3 text-xs font-black uppercase tracking-[0.16em] text-gray-200 flex items-center gap-2">
                                        <FileText size={14} style={{ color: countRowColors.rate }} /> ID Log
                                    </h3>
                                    <div className="mb-3 flex gap-2">
                                        <input
                                            type="number"
                                            min="1"
                                            max="2000"
                                            value={idLogInput}
                                            onChange={(e) => setIdLogInput(e.target.value)}
                                            onKeyDown={(e) => e.key === 'Enter' && handleIdLogSubmit()}
                                            placeholder="Enter problem ID (1-2000)"
                                            className="flex-1 bg-[#050c18] border border-[#1d2d44] rounded-lg px-3 py-2 text-xs text-white placeholder-gray-500 focus:outline-none"
                                            style={{ borderColor: '#1d2d44' }}
                                            onFocus={(e) => e.target.style.borderColor = countRowColors.rate}
                                            onBlur={(e) => e.target.style.borderColor = '#1d2d44'}
                                        />
                                        <button
                                            onClick={handleIdLogSubmit}
                                            disabled={!idLogInput || parseInt(idLogInput) < 1 || parseInt(idLogInput) > 2000}
                                            className="px-4 py-2 rounded-lg text-xs font-bold transition-all hover:brightness-125 disabled:opacity-30 disabled:cursor-not-allowed"
                                            style={{ backgroundColor: hexToRgba(countRowColors.rate, 0.2), border: `1px solid ${hexToRgba(countRowColors.rate, 0.4)}`, color: countRowColors.rate }}
                                        >
                                            Add
                                        </button>
                                    </div>
                                    {idLogProblems.length === 0 ? (
                                        <p className="text-[11px] text-gray-400 italic">No problems in ID Log yet. Enter a problem ID above to add it.</p>
                                    ) : (
                                        <div className="space-y-1 max-h-[280px] overflow-y-auto pr-1">
                                            {idLogProblems.map(problem => {
                                                const isExpanded = expandedIdLogProblem === problem.exerciseId;
                                                return (
                                                    <div key={problem.exerciseId} className="rounded-lg border overflow-hidden" style={{ borderColor: '#1d2d44', backgroundColor: '#050c18' }}>
                                                        <div
                                                            onClick={() => loadIdLogProblem(problem)}
                                                            className="flex items-center justify-between gap-2 px-3 py-2 cursor-pointer transition-all hover:brightness-125"
                                                            onMouseEnter={(e) => { if (e.currentTarget) e.currentTarget.style.borderColor = hexToRgba(countRowColors.rate, 0.5); }}
                                                            onMouseLeave={(e) => { if (e.currentTarget) e.currentTarget.style.borderColor = '#1d2d44'; }}
                                                        >
                                                            <div className="flex-1 text-left min-w-0">
                                                                <span className="text-[11px] font-bold text-gray-200 block truncate">
                                                                    Problem {problem.exerciseId}
                                                                    {problem.mastered && (
                                                                        <span className="ml-2 text-[10px] font-black uppercase tracking-wider" style={{ color: countRowColors.wins }}>Mastered</span>
                                                                    )}
                                                                </span>
                                                                <span className="text-[10px] text-gray-400 block truncate">
                                                                    {problem.description.split('\n')[0]}
                                                                </span>
                                                            </div>
                                                            <div className="flex items-center gap-1 flex-shrink-0" onClick={(e) => e.stopPropagation()}>
                                                                {!problem.mastered && (
                                                                    <button
                                                                        onClick={() => markIdLogProblemMastered(problem.exerciseId)}
                                                                        title="Mark as mastered"
                                                                        className="p-1.5 rounded-md transition-all hover:brightness-125"
                                                                        style={{ color: countRowColors.wins }}
                                                                    >
                                                                        <CheckCircle size={14} />
                                                                    </button>
                                                                )}
                                                                <button
                                                                    onClick={() => handleDeleteConfirm(problem.exerciseId, 'idlog')}
                                                                    title="Remove"
                                                                    className="p-1.5 rounded-md transition-all hover:brightness-125"
                                                                    style={{ color: toolPanelColors.failed }}
                                                                >
                                                                    <Trash2 size={14} />
                                                                </button>
                                                                <button
                                                                    onClick={() => setExpandedIdLogProblem(isExpanded ? null : problem.exerciseId)}
                                                                    title={isExpanded ? 'Hide details' : 'Show details'}
                                                                    className="p-1.5 rounded-md transition-all hover:brightness-125"
                                                                    style={{ color: hexToRgba(countRowColors.rate, 0.7) }}
                                                                >
                                                                    {isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                                                                </button>
                                                            </div>
                                                        </div>
                                                        {isExpanded && (
                                                            <div className="border-t border-[#1d2d44] px-3 py-2.5 space-y-2" style={{ backgroundColor: 'rgba(5, 12, 24, 0.5)' }}>
                                                                <p className="text-[12px] leading-relaxed text-gray-300">{problem.description}</p>
                                                                <div className="flex gap-2">
                                                                    <button
                                                                        onClick={() => loadIdLogProblem(problem)}
                                                                        className="flex-1 py-1.5 rounded-lg text-[11px] font-bold transition-all hover:brightness-125"
                                                                        style={{ backgroundColor: hexToRgba(countRowColors.rate, 0.15), border: `1px solid ${hexToRgba(countRowColors.rate, 0.3)}`, color: countRowColors.rate }}
                                                                    >
                                                                        Practice in IDE
                                                                    </button>
                                                                </div>
                                                            </div>
                                                        )}
                                                    </div>
                                                );
                                            })}
                                        </div>
                                    )}
                                </div>

                                <div className="mb-6 rounded-2xl border border-[#1d2d44] bg-[#071225]/80 p-4">
                                    <div className="mb-3 flex items-center justify-between gap-3">
                                        <div>
                                            <h3 className="text-sm font-black uppercase tracking-[0.14em] text-[#93c5fd]">Offline AI Reviewer</h3>
                                            <p className="mt-1 text-xs text-gray-400">{offlineAiState.message}</p>
                                        </div>
                                        <button
                                            onClick={() => {
                                                if (offlineAiBusy) return;
                                                setOfflineAiState(prev => {
                                                    if (prev.status !== 'ready' && !prev.enabled) {
                                                        return {
                                                            ...prev,
                                                            enabled: false,
                                                            message: 'Download and test the offline model before turning model review on.',
                                                        };
                                                    }
                                                    return {
                                                        ...prev,
                                                        enabled: !prev.enabled,
                                                        message: !prev.enabled ? 'Offline model review is on.' : 'Offline model review is off. Built-in offline review remains active.',
                                                    };
                                                });
                                            }}
                                            disabled={offlineAiBusy}
                                            className={`rounded-xl px-3 py-2 text-xs font-black uppercase tracking-[0.12em] disabled:cursor-not-allowed disabled:opacity-50 ${offlineAiState.enabled && offlineAiState.status === 'ready' ? 'bg-[#22c55e]/20 text-[#86efac]' : 'bg-[#334155] text-gray-300'}`}
                                        >
                                            Model {offlineAiState.enabled && offlineAiState.status === 'ready' ? 'On' : 'Off'}
                                        </button>
                                    </div>
                                    <div className="mb-3 grid grid-cols-2 gap-2 text-[11px] font-black uppercase tracking-[0.12em]">
                                        <div className="rounded-xl border border-[#1d2d44] bg-[#020817]/60 p-3 text-gray-300">
                                            <div className="text-gray-500">Installed</div>
                                            <div className={offlineAiState.status === 'ready' ? 'mt-1 text-[#86efac]' : 'mt-1 text-[#fca5a5]'}>
                                                {offlineAiState.status === 'ready' ? 'Yes' : 'No'}
                                            </div>
                                        </div>
                                        <div className="rounded-xl border border-[#1d2d44] bg-[#020817]/60 p-3 text-gray-300">
                                            <div className="text-gray-500">Using Model</div>
                                            <div className={offlineAiState.enabled && offlineAiState.status === 'ready' ? 'mt-1 text-[#86efac]' : 'mt-1 text-gray-400'}>
                                                {offlineAiState.enabled && offlineAiState.status === 'ready' ? 'On' : 'Off'}
                                            </div>
                                        </div>
                                    </div>
                                    <div className="mb-3 rounded-2xl border border-[#1d2d44] bg-[#020817]/60 p-3">
                                        <div className="mb-2 flex items-center justify-between gap-3 text-[11px] font-black uppercase tracking-[0.12em] text-gray-400">
                                            <span>Download / Test</span>
                                            <span>
                                                {getOfflineAiProgressLabel(offlineAiState.status, offlineAiState.progress)}
                                                {offlineAiState.status === 'downloading' && offlineAiState.startedAt ? ` · ${getOfflineAiElapsedLabel(offlineAiState.startedAt, offlineAiNow)}` : ''}
                                            </span>
                                        </div>
                                        <div className="h-3 overflow-hidden rounded-full bg-[#0f172a] ring-1 ring-[#1d2d44]">
                                            <div
                                                className={`h-full rounded-full bg-gradient-to-r from-[#38bdf8] via-[#3b82f6] to-[#22c55e] transition-all duration-500 ${offlineAiState.status === 'downloading' && !offlineAiState.progress ? 'animate-pulse' : ''}`}
                                                style={{
                                                    width: offlineAiState.status === 'ready'
                                                        ? '100%'
                                                        : offlineAiState.status === 'downloading'
                                                            ? `${Math.max(8, Math.min(99, Math.round((offlineAiState.progress || 0) * 100)))}%`
                                                            : '0%',
                                                }}
                                            />
                                        </div>
                                        <div className="mt-2 text-[11px] leading-relaxed text-gray-400">
                                            Status: {getOfflineAiStatusLabel(offlineAiState.status)} · Model: {offlineAiState.modelId}
                                            {offlineAiState.status === 'downloading' ? ' · Built-in review stays active during setup.' : ''}
                                        </div>
                                    </div>
                                    <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                                        <button
                                            onClick={() => {
                                                if (offlineAiBusy) return;
                                                const operationId = ++offlineAiOperationRef.current;
                                                downloadOfflineAiModel(offlineAiState, next => {
                                                    if (operationId === offlineAiOperationRef.current) {
                                                        setOfflineAiState(next);
                                                    }
                                                }).catch(error => {
                                                    if (operationId !== offlineAiOperationRef.current) return;
                                                    setOfflineAiState(prev => {
                                                        if (prev.status !== 'downloading') return prev;
                                                        return {
                                                            ...prev,
                                                            status: 'failed',
                                                            message: String(error?.message || error || 'Offline AI download failed.'),
                                                            progress: 0,
                                                        };
                                                    });
                                                });
                                            }}
                                            disabled={offlineAiBusy}
                                            className="rounded-xl border border-[#3b82f6]/35 bg-[#3b82f6]/10 px-3 py-2 text-xs font-black uppercase tracking-[0.12em] text-[#93c5fd] disabled:cursor-not-allowed disabled:opacity-50"
                                        >
                                            {offlineAiState.status === 'ready' ? 'Re-Test Download' : offlineAiState.status === 'downloading' ? 'Preparing...' : 'Prepare Download'}
                                        </button>
                                        <button
                                            onClick={() => {
                                                if (offlineAiState.status === 'downloading') {
                                                    ++offlineAiOperationRef.current;
                                                    setOfflineAiState({
                                                        ...DEFAULT_OFFLINE_AI_STATE,
                                                        message: 'Offline model setup canceled. Built-in offline review is active.',
                                                    });
                                                    void removeOfflineAiModel(offlineAiState.modelId).catch(() => undefined);
                                                    return;
                                                }
                                                if (offlineAiBusy) return;
                                                const operationId = ++offlineAiOperationRef.current;
                                                setOfflineAiState(prev => ({
                                                    ...prev,
                                                    enabled: false,
                                                    status: 'removing',
                                                    message: 'Removing offline AI model...',
                                                    progress: 0,
                                                }));
                                                removeOfflineAiModel(offlineAiState.modelId).then(next => {
                                                    if (operationId === offlineAiOperationRef.current) {
                                                        setOfflineAiState(next);
                                                    }
                                                }).catch(() => {
                                                    if (operationId === offlineAiOperationRef.current) {
                                                        setOfflineAiState(DEFAULT_OFFLINE_AI_STATE);
                                                    }
                                                });
                                            }}
                                            disabled={offlineAiState.status === 'removing'}
                                            className="rounded-xl border border-[#ef4444]/35 bg-[#ef4444]/10 px-3 py-2 text-xs font-black uppercase tracking-[0.12em] text-[#fecaca] disabled:cursor-not-allowed disabled:opacity-50"
                                        >
                                            {offlineAiState.status === 'downloading' ? 'Cancel Setup' : 'Remove Offline AI'}
                                        </button>
                                    </div>
                                </div>

                                <div className="mb-6 rounded-2xl border p-4" style={{ borderColor: hexToRgba(toolPanelColors.failed, 0.3), backgroundColor: hexToRgba(toolPanelColors.failed, 0.08) }}>
                                    <h3 className="mb-2 flex items-center gap-2 text-xs font-black uppercase tracking-[0.16em]" style={{ color: toolPanelColors.failed }}>
                                        <Trash2 size={14} /> App Cache
                                    </h3>
                                    <p className="mb-3 text-[11px] leading-relaxed text-gray-300">
                                        If the phone app is stuck on an old GitHub Pages version, clear only the app cache and service worker. Progress, stats, saved problems, and settings stay in place.
                                    </p>
                                    <button
                                        onClick={clearAppCacheAndReload}
                                        disabled={cacheClearBusy}
                                        className="w-full rounded-xl border px-4 py-3 text-xs font-black uppercase tracking-[0.14em] transition-all disabled:opacity-60 hover:brightness-125"
                                        style={{ borderColor: hexToRgba(toolPanelColors.failed, 0.4), backgroundColor: hexToRgba(toolPanelColors.failed, 0.15), color: toolPanelColors.failed }}
                                    >
                                        {cacheClearBusy ? 'Clearing Cache...' : 'Clear App Cache & Reload'}
                                    </button>
                                </div>

                                </div>

                                <button onClick={() => { setResetConfirmArmed(false); setShowModal('restart_confirm'); }} className="w-full flex-shrink-0 border py-3 rounded-xl transition-all hover:brightness-125" style={{ borderColor: hexToRgba(toolPanelColors.failed, 0.4), color: toolPanelColors.failed, backgroundColor: hexToRgba(toolPanelColors.failed, 0.15) }}>Reset Progress</button>
                            </div>
                        )}
                        {showModal === 'stats_by_mode' && (
                            <div className="flex flex-col h-full min-h-0 py-2">
                                <h2 className="mb-4 flex-shrink-0 text-center text-lg font-bold">Stats By Mode</h2>
                                <div className="min-h-0 flex-1 overflow-y-auto overscroll-contain pr-1 pb-8">
                                    <div className="rounded-2xl border border-[#1d2d44] bg-[#071225]/70 p-4">
                                        <div className="grid grid-cols-[1fr_52px_52px_52px_52px_52px] gap-x-2 gap-y-1.5 text-[11px]">
                                            <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500">Mode</div>
                                            <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Count</div>
                                            <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Wins</div>
                                            <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Fails</div>
                                            <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Rate</div>
                                            <div className="text-[9px] font-bold uppercase tracking-[0.12em] text-gray-500 text-right">Rank</div>
                                            {DIFFICULTY_MODES.map(mode => {
                                                const modeStats = statsByMode[mode.id] ?? EMPTY_STATS;
                                                const modeRate = modeStats.shots > 0 ? ((modeStats.success / modeStats.shots) * 100).toFixed(0) : '0';
                                                const modeRank = getModeRank(modeStats);
                                                return [
                                                    <span key={`${mode.id}-label`} className="font-bold uppercase tracking-[0.12em] text-gray-200 truncate">{mode.label}</span>,
                                                    <span key={`${mode.id}-shots`} className="font-mono text-right">{modeStats.shots}</span>,
                                                    <span key={`${mode.id}-wins`} className="font-mono text-right" style={{ color: countRowColors.wins }}>{modeStats.success}</span>,
                                                    <span key={`${mode.id}-fails`} className="font-mono text-right" style={{ color: toolPanelColors.failed }}>{modeStats.failed}</span>,
                                                    <span key={`${mode.id}-rate`} className="font-mono text-right" style={{ color: modeStats.shots > 0 ? countRowColors.rate : 'inherit' }}>{modeRate}%</span>,
                                                    <span key={`${mode.id}-rank`} className="font-mono text-right" title={modeRank.name}>{modeRank.icon}</span>,
                                                ];
                                            })}
                                        </div>
                                        <div className="mt-3 border-t border-[#1d2d44] pt-2 grid grid-cols-[1fr_52px_52px_52px_52px_52px] gap-x-2 gap-y-1.5 text-[11px]">
                                            <div className="font-bold uppercase tracking-[0.12em] text-gray-200">Total</div>
                                            <div className="font-mono text-right text-gray-200">{Object.values(statsByMode).reduce((s, m) => s + m.shots, 0)}</div>
                                            <div className="font-mono text-right" style={{ color: countRowColors.wins }}>{Object.values(statsByMode).reduce((s, m) => s + m.success, 0)}</div>
                                            <div className="font-mono text-right" style={{ color: toolPanelColors.failed }}>{Object.values(statsByMode).reduce((s, m) => s + m.failed, 0)}</div>
                                            <div className="font-mono text-right" style={{ color: countRowColors.rate }}>{(() => { const t = Object.values(statsByMode).reduce((s, m) => s + m.shots, 0); const w = Object.values(statsByMode).reduce((s, m) => s + m.success, 0); return t > 0 ? ((w / t) * 100).toFixed(0) + '%' : '0%'; })()}</div>
                                            <div className="font-mono text-right" title={userRank.name}>{userRank.icon}</div>
                                        </div>
                                    </div>
                                </div>
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
                                        className="w-full bg-[#0d1b2a] border border-[#1d2d44] text-white px-4 py-3 rounded-xl text-sm font-mono transition-all"
                                        style={{ borderColor: '#1d2d44' }}
                                        onFocus={(e) => e.target.style.borderColor = countRowColors.count}
                                        onBlur={(e) => e.target.style.borderColor = '#1d2d44'}
                                    />
                                    <p className="text-[10px] text-gray-400 mt-2 leading-relaxed">
                                        Get your API key from{' '}
                                        <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noreferrer" className="underline inline-flex items-center gap-0.5" style={{ color: countRowColors.count }}>
                                            Google AI Studio <ExternalLink size={10} />
                                        </a>
                                    </p>
                                </div>
                                <button
                                    onClick={() => {
                                        localStorage.setItem('gemini_api_key', apiKey);
                                        setShowModal('none');
                                    }}
                                    className="w-full text-white font-bold py-4 rounded-xl flex items-center justify-center gap-2 transition-all hover:brightness-125"
                                    style={{ backgroundColor: countRowColors.count }}
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
                                    className="w-full py-4 rounded-xl font-bold mb-3 transition-all hover:brightness-125"
                                    style={resetConfirmArmed ? { backgroundColor: toolPanelColors.failed, color: '#ffffff' } : { backgroundColor: hexToRgba(toolPanelColors.failed, 0.15), color: toolPanelColors.failed, border: `1px solid ${hexToRgba(toolPanelColors.failed, 0.4)}` }}
                                >
                                    {resetConfirmArmed ? 'Yes, Reset Everything' : 'Reset Now'}
                                </button>
                                <button onClick={() => { setResetConfirmArmed(false); setShowModal('none'); }} className="w-full bg-[#1d2d44] py-4 rounded-xl">Cancel</button>
                            </div>
                        )}
                        {showModal === 'delete_confirm' && (
                            <div className="text-center py-4">
                                <h2 className="text-lg font-bold mb-2" style={{ color: toolPanelColors.failed }}>⚠️ Confirm Delete</h2>
                                <p className="text-xs text-gray-300 mb-4 leading-relaxed">
                                    Are you sure you want to remove Problem {deleteConfirmId} from your {deleteConfirmType === 'saved' ? 'Saved Problems' : 'ID Log'}?
                                </p>
                                <button
                                    onClick={handleDeleteExecute}
                                    className="w-full py-4 rounded-xl font-bold mb-3 text-white transition-all hover:brightness-125"
                                    style={{ backgroundColor: toolPanelColors.failed }}
                                >
                                    Yes, Delete
                                </button>
                                <button onClick={handleDeleteCancel} className="w-full py-4 rounded-xl transition-all hover:brightness-125" style={{ backgroundColor: countRowColors.background, border: `1px solid ${countRowColors.border}`, color: '#9ca3af' }}>Cancel</button>
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
                                        overflowWrap: 'break-word',
                                        pointerEvents: 'auto',
                                        userSelect: 'text',
                                        WebkitUserSelect: 'text'
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

const ActionButton: React.FC<{ icon: React.ReactNode, iconColor: string, description: string, onClick: () => void }> = ({ icon, iconColor, description, onClick }) => (
    <button
        onClick={onClick}
        style={{
            backgroundColor: hexToRgba(iconColor, 0.15),
            borderColor: hexToRgba(iconColor, 0.3),
            color: iconColor,
            pointerEvents: 'auto'
        }}
        className="w-[42px] h-[42px] rounded-full flex flex-col items-center justify-center shadow-lg active:scale-90 transition-all border border-white/5"
    >
        {icon}
        <span className="text-[6px] font-bold mt-0.5 uppercase tracking-tighter">{description}</span>
    </button>
);

const TabButton: React.FC<{ active: boolean, onClick: () => void, label: string }> = ({ active: isActive, onClick, label }) => (
    <button onClick={onClick} className={`pb-2 px-1 font-bold transition-all text-xs ${isActive ? 'text-white border-b-2 border-[#3b82f6]' : 'text-gray-500'}`}>{label}</button>
);

const ColorField: React.FC<{ label: string; value: string; onChange: (value: string) => void }> = ({ label, value, onChange }) => (
    <label className="flex items-center justify-between gap-3 rounded-xl border border-[#1d2d44] bg-[#050c18]/80 px-3 py-3">
        <span className="min-w-0">
            <span className="block text-xs font-bold text-gray-200">{label}</span>
            <span className="mt-1 block font-mono text-[10px] uppercase text-gray-500">{value}</span>
        </span>
        <input
            type="color"
            value={value}
            onInput={(event) => onChange((event.currentTarget as HTMLInputElement).value)}
            onChange={(event) => onChange(event.target.value)}
            className="h-10 w-14 cursor-pointer rounded-xl border border-white/10 bg-transparent p-0"
            aria-label={`${label} color`}
        />
    </label>
);

export default App;
