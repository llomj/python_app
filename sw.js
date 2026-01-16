const CACHE_VERSION = "v56";
const CORE_ASSETS = [
    './',
    './index.html',
    './manifest.json',
    './index.tsx',
    // './App.tsx', // REMOVED: Don't cache App.tsx to always get fresh version
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
    'https://esm.sh/@codemirror/autocomplete@6.20.0',
    'https://esm.sh/@codemirror/lang-python@6.2.1',
    'https://esm.sh/@codemirror/language@6.12.1',
    'https://esm.sh/@codemirror/state@6.5.3',
    'https://esm.sh/@codemirror/theme-one-dark@6.1.3',
    'https://esm.sh/@codemirror/view@6.39.8',
    'https://esm.sh/@codemirror/language@6.12.1',
    'https://esm.sh/@codemirror/autocomplete@6.20.0',
    'https://esm.sh/@codemirror/state@6.5.3',
    'https://esm.sh/@codemirror/view@6.39.8',
    'https://esm.sh/@lezer/highlight@1.2.3',
    'https://esm.sh/lucide-react@0.294.0'
];

self.addEventListener('install', (e) => {
    console.log('🔧 Service Worker Installing:', CACHE_VERSION);
    self.skipWaiting();

    // Safari-specific service worker registration conflict resolution
    if (event.target && event.target.client && !event.target.controller) {
        console.log('🔧 Safari SW Conflict - unregistering old worker');
        event.target.addEventListener('controllerchange', () => {
            console.log('🔧 Safari SW Conflict - old controller found:', event.target.controller);
            event.target.controller.postMessage({ type: 'UNREGISTER' });
            event.target.controller.unregister();
        });
    }

    e.waitUntil(
        caches.open(CACHE_VERSION).then(c => c.addAll(CORE_ASSETS)).then(() => {
            console.log('✅ Core assets cached:', CORE_ASSETS.length);
                return self.skipWaiting();
            });
    });
});

self.addEventListener('activate', (e) => {
    console.log('🚀 Service Worker Activated:', CACHE_VERSION);

    // Clear old caches
    e.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_VERSION) {
                        console.log('🗑️ Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );

    // Force update immediately on activation
    if (self.registration) {
        self.registration.update();

        // Also force immediate cache invalidation
        const cacheNames = await caches.keys();
        await Promise.all(cacheNames.map(name => caches.delete(name)));
        console.log('🧹 FORCE CACHE INVALIDATION:', cacheNames.length);
    }

    // Take control of all clients
    self.clients.claim();
});

self.addEventListener('fetch', (e) => {
    const request = e.request;
    const url = request.url;

    // Use NETWORK-FIRST for ALL JavaScript files and exercise files (NEVER CACHE)
    if (request.url.endsWith('.js') || request.url.endsWith('.mjs') || request.url.endsWith('/assets/')) {
        console.log('🌐 Network-first for JS file:', request.url);
        e.respondWith(fetch(request));
        return;
    }

    // Use NETWORK-FIRST for App.tsx and other source files (NEVER CACHE)
    if (request.url.endsWith('.tsx') || request.url.endsWith('.ts') || request.url.endsWith('/level1_')) {
        console.log('📄 NEVER CACHE for source file:', request.url);
        e.respondWith(fetch(request));
        return;
    }

    // Cache-first for all other requests (HTML, CSS, images, etc.)
    console.log('💾 Cache-first for:', request.url);
    e.respondWith(
        caches.open(CACHE_VERSION).then(cache => {
            return cache.match(request).then(response => {
                // If found in cache, return it
                if (response) {
                    return response;
                }

                // If not in cache, fetch from network and cache the response
                return fetch(request).then(networkResponse => {
                    // Don't cache exercise files - they change too frequently
                    const shouldCache = !request.url.includes('level1_') && !request.url.includes('requirements') && !request.url.includes('codelogic');
                    return cache.put(request, networkResponse.clone()).then(() => {
                        return networkResponse;
                    });
                });
            });
        });
    })
});

self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        console.log('⏳ Client told me to skip version check');
        self.skipWaiting();
    }

    if (event.data && event.data.type === 'FORCE_UPDATE_NOW') {
        console.log('🔄 Force update initiated');
        self.registration.update();
    }
});

console.log('🔧 Service Worker loaded, version:', CACHE_VERSION);