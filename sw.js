const CACHE_NAME = 'python-pro-v40';
const CORE_ASSETS = [
    './',
    './index.html',
    './manifest.json',
    './index.tsx',
    './App.tsx',
    './types.ts',
    './exercises.ts',
    './services/geminiService.ts',
    './editorTheme.ts',
    'https://cdn.tailwindcss.com',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.asm.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.asm.wasm',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/python_stdlib.zip',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/repodata.json',
    'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg',
    'https://esm.sh/react@19.0.0',
    'https://esm.sh/react-dom@19.0.0',
    'https://esm.sh/react-dom@19.0.0/client',
    'https://esm.sh/@google/genai@1.34.0',
    'https://esm.sh/lucide-react@0.462.0?external=react',
    'https://esm.sh/@uiw/react-codemirror@4.23.0?external=react',
    'https://esm.sh/@codemirror/lang-python@6.1.3',
    'https://esm.sh/@codemirror/theme-one-dark@6.1.2',
    'https://esm.sh/@codemirror/language@6.10.1',
    'https://esm.sh/@codemirror/autocomplete@6.18.3',
    'https://esm.sh/@codemirror/state@6.4.1',
    'https://esm.sh/@codemirror/view@6.39.8',
    'https://esm.sh/@lezer/highlight@1.2.1'
];

self.addEventListener('install', (e) => {
    self.skipWaiting();
    e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(CORE_ASSETS)));
});

self.addEventListener('activate', (e) => {
    e.waitUntil(caches.keys().then(ks => Promise.all(ks.map(k => k !== CACHE_NAME && caches.delete(k)))));
    self.clients.claim();
});

self.addEventListener('fetch', (e) => {
    const url = new URL(e.request.url);
    if (url.origin === location.origin || CORE_ASSETS.includes(e.request.url) || CORE_ASSETS.some(a => e.request.url.startsWith(a))) {
        e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(nr => {
            if (nr.status === 200 && e.request.method === 'GET') {
                const rc = nr.clone();
                caches.open(CACHE_NAME).then(c => c.put(e.request, rc));
            }
            return nr;
        })));
    }
});
