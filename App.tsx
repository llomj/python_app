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
    Info
} from 'lucide-react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { indentUnit } from '@codemirror/language';
import { autocompletion, snippetCompletion, CompletionContext } from '@codemirror/autocomplete';
import { EXERCISES } from './exercises';
import { Exercise, Stats } from './types';
import { getAiHint } from './services/geminiService';
import { customPythonTheme } from './editorTheme';

// Fixed: Removed local AIStudio interface definition as it conflicts with environment-provided types.

declare global {
    interface Window {
        __PYODIDE_INSTANCE__: any;
        __PYODIDE_INIT_LOCK__: boolean;
        loadPyodide: any;
        // Fixed: Removed aistudio declaration to resolve redeclaration conflict with identical modifiers/types.
    }
}

interface ProjectFile {
    name: string;
    content: string;
}

const CHEAT_SHEET_CONTENT = `# Python Templates & Examples
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

# List of dictionaries
lst_dic = [{"name": "Jon", "age": 67}, {"name": "mike", "age": 55}]

# Nested list
nested_lst = [[1,2,3], [4,5,6], [7,8,9]]
`;

// COMPLETE CHEAT SHEET FROM cheat_sheet.py - DO NOT EDIT, UPDATE THE cheat_sheet.py FILE INSTEAD
const CHEAT_SHEET_FULL = `# Python Cheat Sheet - Complete Reference
# See cheat_sheet.py for the source

# === PYTHON EXAMPLES ===
import collections
from collections import Counter
import datetime
from functools import reduce
import math, os, random, string, re, time
from pathlib import Path
from urllib.parse import parse_qs

# Dictionary Example
def main(dic):
    return len(dic)
    
dic = {"apple": 1, "orange": 33}
print(main(dic))

# List Comprehension
squares = [x**2 for x in range(10)]

# Dictionary with target
def get_value(dic, target):
    return dic.get(target)

# Two dictionaries merge
def merge(d1, d2):
    return {**d1, **d2}

# List of dictionaries
people = [
    {"name": "Jon", "age": 67},
    {"name": "mike", "age": 55}
]

# Nested structures
nested = [[1,2,3], [4,5,6], [7,8,9]]
tuples_list = [(55,7), (2,4), (27,23)]

# Keyword arguments
def process(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# === PYTHON GLOSSARY ===
# A comprehensive reference of Python terms

# **all()** - Returns True if all elements are truthy
# **any()** - Returns True if any element is truthy  
# **Argument** - Value passed to a function
# **Assert** - Tests condition, raises AssertionError if False
# **Attribute** - Value associated with an object
# **Class** - Blueprint for creating objects
# **Closure** - Function with enclosing scope access
# **Comprehension** - Concise way to create collections
# **Decorator** - Modifies function behavior
# **Dictionary** - Key-value pairs collection
# **Filter** - Returns elements where function is True
# **Generator** - Yields values on-the-fly
# **Global** - Module-level variable
# **Immutable** - Cannot be changed (int, str, tuple)
# **Import** - Brings code from another module
# **isinstance()** - Checks object type
# **Iterable** - Can be used in for loop
# **Iterator** - Accesses elements one at a time
# **Lambda** - Anonymous function: lambda x: x * 2
# **List** - Ordered, mutable collection
# **Map** - Applies function to every item
# **Max/Min** - Largest/smallest item
# **Method** - Function belonging to object
# **Module** - File with Python code
# **Mutable** - Can be changed (list, dict, set)
# **None** - Absence of value
# **Object** - Instance of a class
# **Parameter** - Input variable in function definition
# **Range** - Generates sequence of numbers
# **Return** - Exits function, returns value
# **Set** - Unordered unique elements
# **Sorted** - Returns new sorted list
# **String** - Immutable sequence of characters
# **Tuple** - Ordered, immutable collection
# **Type** - Category of value (int, str, list)
# **Variable** - Container holding a value
# **Zip** - Combines iterables element-wise

# LEGB Rule - Scope Resolution:
# L = Local (function)
# E = Enclosing (outer function)  
# G = Global (module)
# B = Built-in (print, len, etc.)

# === REGEX PATTERNS ===
# Character Classes: a-z, A-Z, 0-9
# \\d (digit), \\w (word), \\s (space)
# 
# Special: . (any), ^ (start), $ (end)
# * (0+), + (1+), ? (0-1), {n,m} (n to m)
#
# Examples:
# \\d{4}-\\d{2}-\\d{2} - Date (YYYY-MM-DD)
# [a-z]+@[a-z]+\\.[a-z]{2,} - Email
# \\d{3}-\\d{3}-\\d{4} - Phone

# For full details, see cheat_sheet.py file (511 lines)
`;

const GLOSSARY_CONTENT = `# Python Glossary

**all()** - Returns True if all elements are truthy
**any()** - Returns True if any element is truthy
**Argument** - Value passed to a function
**Assert** - Tests a condition, raises AssertionError if False
**Class** - Blueprint for creating objects
**Closure** - Function that remembers its enclosing scope
**Comprehension** - Concise way to create collections
**Decorator** - Modifies function behavior
**Dictionary** - Key-value pairs collection
**Filter** - Returns elements where function returns True
**Generator** - Yields values on-the-fly
**Global** - Module-level variable
**Immutable** - Cannot be changed (int, str, tuple)
**Import** - Brings code from another module
**isinstance()** - Checks if object is instance of class
**Iterable** - Can be used in for loop
**Iterator** - Accesses elements one at a time
**Lambda** - Anonymous function: lambda x: x * 2
**List** - Ordered, mutable collection
**Map** - Applies function to every item
**Max/Min** - Largest/smallest item
**Method** - Function belonging to object
**Module** - File with Python code
**Mutable** - Can be changed (list, dict, set)
**None** - Absence of value
**Object** - Instance of a class
**Parameter** - Input variable in function definition
**Range** - Generates sequence of numbers
**Return** - Exits function, returns value
**Set** - Unordered unique elements
**Sorted** - Returns new sorted list
**String** - Immutable sequence of characters
**Tuple** - Ordered, immutable collection
**Type** - Category of value (int, str, list)
**Variable** - Container holding a value
**Zip** - Combines iterables element-wise

## LEGB Rule
Python finds names in this order:
• L = Local (function)
• E = Enclosing (outer function)
• G = Global (module)
• B = Built-in (print, len, etc.)
`;

const REGEX_CONTENT = `# Regular Expressions

**Character Classes**
a-z, A-Z, 0-9, \\d (digit), \\w (word), \\s (space)

**Special Characters**
. (any char), ^ (start), $ (end)
* (0+), + (1+), ? (0 or 1)
{n,m} (n to m times)

**Examples**
\\d{4}-\\d{2}-\\d{2} - Date (YYYY-MM-DD)
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,} - Email
`;


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
    const [exercise, setExercise] = useState<Exercise>(EXERCISES[0]);
    const [files, setFiles] = useState<ProjectFile[]>([{ name: 'main.py', content: EXERCISES[0].initialCode }]);
    const [activeFileIndex, setActiveFileIndex] = useState(0);
    const [isEditingFileName, setIsEditingFileName] = useState(false);
    const [newName, setNewName] = useState('');

    const [output, setOutput] = useState('Run code to see output...');
    const [isRunning, setIsRunning] = useState(false);
    const [stats, setStats] = useState<Stats>({ shots: 0, success: 0, failed: 0 });
    const [pyodide, setPyodide] = useState<any>(null);
    const [bootStage, setBootStage] = useState<'loading' | 'ready' | 'launched'>('loading');
    const [bootLog, setBootLog] = useState<string>('Handshaking...');
    const [loadTime, setLoadTime] = useState<number>(0);
    const [isInFrame, setIsInFrame] = useState(false);
    const [showModal, setShowModal] = useState<'none' | 'instructions' | 'hint' | 'solution' | 'settings' | 'restart_confirm'>('none');
    const [modalTab, setModalTab] = useState<'how' | 'cheat' | 'glossary' | 'regex'>('how');
    const [aiHintText, setAiHintText] = useState<string>('');
    const [copyFeedback, setCopyFeedback] = useState(false);

    const outputRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        setIsInFrame(window.self !== window.top);
        const savedStats = localStorage.getItem('python_mastery_stats');
        if (savedStats) setStats(JSON.parse(savedStats));

        const bootEl = document.getElementById('boot');
        if (bootEl) {
            setTimeout(() => { bootEl.style.opacity = '0'; }, 500);
            setTimeout(() => { bootEl.style.display = 'none'; }, 1000);
        }
    }, []);

    useEffect(() => {
        localStorage.setItem('python_mastery_stats', JSON.stringify(stats));
    }, [stats]);

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

    const handleCopyLink = () => {
        const url = window.location.href;
        navigator.clipboard.writeText(url);
        setCopyFeedback(true);
        setTimeout(() => setCopyFeedback(false), 2000);
    };

    const setProblemById = (id: number) => {
        const targetId = Math.min(Math.max(1, id), 2000);
        const ex = EXERCISES[targetId - 1];
        setExercise(ex);
        setFiles([{ name: 'main.py', content: ex.initialCode }]);
        setActiveFileIndex(0);
        setOutput('Run code to see output...');
        setAiHintText('');
    };

    const loadRandomExercise = useCallback(() => {
        const randomIndex = Math.floor(Math.random() * EXERCISES.length);
        setProblemById(randomIndex + 1);
    }, []);

    const handleRestartProgress = () => {
        setStats({ shots: 0, success: 0, failed: 0 });
        loadRandomExercise();
        setShowModal('none');
    };

    const runCode = async () => {
        if (!pyodide || isRunning) return;
        setIsRunning(true);
        setOutput('Executing...');
        try {
            // Write all files to the virtual filesystem
            files.forEach(file => {
                pyodide.FS.writeFile(file.name, file.content);
            });

            // Clear user-defined modules from sys.modules to ensure fresh imports
            const userModules = files.map(f => f.name.replace('.py', ''));
            const clearModulesCode = `
import sys
import importlib
import io

# Ensure current directory is in path (crucial for imports)
if '.' not in sys.path:
    sys.path.insert(0, '.')

for mod in ${JSON.stringify(userModules)}:
    if mod in sys.modules:
        del sys.modules[mod]

importlib.invalidate_caches()
sys.stdout = io.StringIO()
`;
            pyodide.runPython(clearModulesCode);

            const activeFile = files[activeFileIndex];
            // CRITICAL FIX: Use exec with filename context so imports work
            const code = `exec(compile(${JSON.stringify(activeFile.content)}, ${JSON.stringify(activeFile.name)}, 'exec'))`;
            await pyodide.runPythonAsync(code);
            const stdout = pyodide.runPython("sys.stdout.getvalue()");
            setOutput(stdout || 'Success (No output).');
        } catch (err: any) {
            setOutput(err.message);
        } finally {
            setIsRunning(false);
        }
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
    };

    const handleMarkSuccess = () => {
        setStats(prev => ({ ...prev, shots: prev.shots + 1, success: prev.success + 1 }));
        loadRandomExercise();
    };

    const handleMarkFailed = () => {
        setStats(prev => ({ ...prev, shots: prev.shots + 1, failed: prev.failed + 1 }));
        loadRandomExercise();
    };

    const handleAiHint = async () => {
        // Rely on window.aistudio which is assumed to be globally available per instructions.
        // @ts-ignore
        const hasKey = window.aistudio ? await window.aistudio.hasSelectedApiKey() : true;
        if (!hasKey) {
            setShowModal('settings');
            return;
        }
        setShowModal('hint');
        if (!aiHintText) {
            setAiHintText('Asking Gemini...');
            const hint = await getAiHint(exercise.description, files[activeFileIndex].content);
            setAiHintText(hint);
        }
    };

    const rate = stats.shots > 0 ? ((stats.success / stats.shots) * 100).toFixed(2) : '0.00';

    const editorExtensions = useMemo(() => [
        python(),
        indentUnit.of("    "),
        autocompletion({ override: [pythonSnippets] }),
        ...customPythonTheme
    ], []);

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
        <div className="min-h-screen bg-[#040b16] text-white flex flex-col p-4 max-w-md mx-auto overflow-hidden animate-in fade-in duration-700">
            <div className="relative flex items-center justify-center mb-4 flex-shrink-0">
                <div className="flex gap-4 sm:gap-5 items-center bg-[#0a1628] border border-[#1d2d44] px-4 py-2 rounded-full shadow-lg text-[10px] sm:text-xs font-black tracking-tight">
                    <div className="flex items-center"><span className="text-[#3b82f6] mr-1 uppercase">Shot:</span><span>{stats.shots}</span></div>
                    <div className="flex items-center"><span className="text-[#22c55e] mr-1 uppercase">Win:</span><span>{stats.success}</span></div>
                    <div className="flex items-center"><span className="text-[#ef4444] mr-1 uppercase">Fail:</span><span>{stats.failed}</span></div>
                    <div className="flex items-center border-l border-[#1d2d44] pl-4 ml-1"><span className="text-[#f59e0b] mr-1 uppercase">Rate:</span><span>{rate}%</span></div>
                </div>
                <div className="absolute right-0">
                    <button onClick={() => setShowModal('settings')} className="text-gray-400 hover:text-[#3b82f6] transition-all bg-[#0a1628] p-2 rounded-full border border-[#1d2d44]"><Key size={16} /></button>
                </div>
            </div>

            <div className="flex justify-center gap-2 sm:gap-3 mb-4 flex-shrink-0">
                <ActionButton icon={<Book size={16} />} color="rgba(245, 158, 11, 0.15)" borderColor="rgba(245, 158, 11, 0.3)" iconColor="#f59e0b" description="Info" onClick={() => { setShowModal('instructions'); setModalTab('how'); }} />
                <ActionButton icon={<Lightbulb size={16} />} color="rgba(59, 130, 246, 0.15)" borderColor="rgba(59, 130, 246, 0.3)" iconColor="#3b82f6" description="Sol" onClick={() => setShowModal('solution')} />
                <ActionButton icon={<Bot size={16} />} color="rgba(139, 92, 246, 0.15)" borderColor="rgba(139, 92, 246, 0.3)" iconColor="#8b5cf6" description="AI" onClick={handleAiHint} />
                <ActionButton icon={<CheckCircle size={16} />} color="rgba(34, 197, 94, 0.15)" borderColor="rgba(34, 197, 94, 0.3)" iconColor="#22c55e" description="Win" onClick={handleMarkSuccess} />
                <ActionButton icon={<XCircle size={16} />} color="rgba(239, 68, 68, 0.15)" borderColor="rgba(239, 68, 68, 0.3)" iconColor="#ef4444" description="Failed" onClick={handleMarkFailed} />
                <ActionButton icon={<RotateCcw size={16} />} color="rgba(249, 115, 22, 0.15)" borderColor="rgba(249, 115, 22, 0.3)" iconColor="#f97316" description="Reset" onClick={() => setShowModal('restart_confirm')} />
            </div>

            <div className="bg-[#0a1628] rounded-xl p-4 mb-3 shadow-xl border border-[#1d2d44] flex-shrink-0">
                <h2 className="text-lg font-bold mb-1">Problem {exercise.id}</h2>
                <p className="text-gray-300 text-xs leading-tight line-clamp-2">{exercise.description}</p>
            </div>

            <div className="bg-[#0a1628] rounded-xl flex flex-col shadow-2xl border border-[#1d2d44] overflow-hidden flex-grow min-h-0">
                <div className="flex items-center justify-between p-2 bg-[#0d1b2a] border-b border-[#1d2d44] flex-shrink-0">
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
                        <button onClick={runCode} disabled={isRunning} className="ml-1 flex items-center gap-1.5 px-3 py-1 rounded-lg font-bold text-xs bg-[#22c55e1a] border border-[#22c55e4d] text-[#22c55e]">
                            {isRunning ? <Loader2 size={12} className="animate-spin" /> : <Play size={12} fill="currentColor" />} RUN
                        </button>
                    </div>
                </div>
                <div className="flex bg-[#0a1628] border-b border-[#1d2d44] overflow-x-auto no-scrollbar">
                    {files.map((f, idx) => (
                        <button key={idx} onClick={() => setActiveFileIndex(idx)} className={`px-4 py-1.5 text-[10px] font-bold tracking-wider transition-all border-r border-[#1d2d44] whitespace-nowrap ${activeFileIndex === idx ? 'bg-[#050c18] text-[#3b82f6] border-b-2 border-b-[#3b82f6]' : 'text-gray-500'}`}>
                            {f.name}
                        </button>
                    ))}
                </div>
                <div className="flex-grow overflow-hidden bg-[#050c18] relative">
                    <CodeMirror
                        value={files[activeFileIndex].content} height="100%" extensions={editorExtensions} onChange={updateActiveContent}
                        basicSetup={{ lineNumbers: true, autocompletion: true, bracketMatching: true, closeBrackets: true, indentOnInput: true }}
                    />
                </div>
                <div className="border-t border-[#1d2d44] p-2 bg-[#0a1628] flex-shrink-0">
                    <div ref={outputRef} className="h-24 overflow-y-auto">
                        <pre className="text-[10px] font-mono text-[#4ade80] whitespace-pre-wrap select-text">{output}</pre>

                    </div>
                </div>
            </div>

            {showModal !== 'none' && (
                <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 z-50 animate-in fade-in duration-200">
                    <div className="bg-[#112240] rounded-3xl p-6 max-w-lg w-full border border-[#1d2d44] shadow-2xl relative max-h-[80vh] flex flex-col overflow-hidden">
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
                                                value={CHEAT_SHEET_FULL}
                                                height="400px"
                                                readOnly={true}
                                                extensions={[python(), ...customPythonTheme]}
                                                basicSetup={{ lineNumbers: false, foldGutter: false }}
                                            />
                                        </div>
                                    )}
                                    {modalTab === 'glossary' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44]">
                                            <CodeMirror
                                                value={CHEAT_SHEET_FULL}
                                                height="400px"
                                                readOnly={true}
                                                extensions={[python(), ...customPythonTheme]}
                                                basicSetup={{ lineNumbers: false, foldGutter: false }}
                                            />
                                        </div>
                                    )}
                                    {modalTab === 'regex' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44]">
                                            <CodeMirror
                                                value={CHEAT_SHEET_FULL}
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
                                <h2 className="text-lg font-bold mb-3 text-[#3b82f6]">Solution</h2>
                                <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] flex-grow">
                                    <CodeMirror value={exercise.solution} height="100%" readOnly={true} extensions={[python(), ...customPythonTheme]} />
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
                            <div className="py-2 text-center">
                                <h2 className="text-lg font-bold mb-4">Settings</h2>
                                <button onClick={async () => {
                                    // @ts-ignore
                                    window.aistudio?.openSelectKey();
                                    setShowModal('none');
                                }} className="w-full bg-[#3b82f6] text-white font-bold py-4 rounded-xl mb-2 flex items-center justify-center gap-2">
                                    <Key size={18} /> Select API Key
                                </button>
                                <p className="text-[10px] text-gray-400 mb-6 leading-relaxed">
                                    Note: You must select an API key from a <b>paid GCP project</b>.
                                    <a href="https://ai.google.dev/gemini-api/docs/billing" target="_blank" rel="noreferrer" className="text-[#3b82f6] ml-1 inline-flex items-center gap-0.5 underline">
                                        Billing Docs <ExternalLink size={10} />
                                    </a>
                                </p>
                                <button onClick={() => setShowModal('restart_confirm')} className="w-full border border-red-500/30 text-red-500 py-3 rounded-xl">Reset Progress</button>
                            </div>
                        )}
                        {showModal === 'restart_confirm' && (
                            <div className="text-center py-4">
                                <h2 className="text-lg font-bold mb-2">Clear Stats?</h2>
                                <button onClick={handleRestartProgress} className="w-full bg-red-500 py-4 rounded-xl font-bold mb-3">Reset Now</button>
                                <button onClick={() => setShowModal('none')} className="w-full bg-[#1d2d44] py-4 rounded-xl">Cancel</button>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

const ActionButton: React.FC<{ icon: React.ReactNode, color: string, borderColor: string, iconColor: string, description: string, onClick: () => void }> = ({ icon, color, borderColor, iconColor, description, onClick }) => (
    <button onClick={onClick} style={{ backgroundColor: color, borderColor: borderColor, color: iconColor }} className="w-[42px] h-[42px] rounded-full flex flex-col items-center justify-center shadow-lg active:scale-90 transition-all border border-white/5">
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
