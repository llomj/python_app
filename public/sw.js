const CACHE_VERSION = "v58";
// Pre-cache core shell + CDN deps for offline. Bundled JS/assets cached at runtime.
const CORE_ASSETS = [
    './',
    './index.html',
    './manifest.json',
    'https://cdn.tailwindcss.com',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.asm.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.asm.wasm',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/python_stdlib.zip',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/repodata.json',
    'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'
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
        }).then(() => {
            if (self.registration) self.registration.update();
            return self.clients.claim();
        })
    );
});

// Network-first with cache fallback: try network, on failure serve from cache. Enables FULL OFFLINE support.
self.addEventListener('fetch', (e) => {
    const request = e.request;
    e.respondWith(
        fetch(request)
            .then(networkResponse => {
                if (networkResponse.ok && request.method === 'GET') {
                    caches.open(CACHE_VERSION).then(cache => cache.put(request, networkResponse.clone()));
                }
                return networkResponse;
            })
            .catch(() =>
                caches.open(CACHE_VERSION).then(cache =>
                    cache.match(request).then(cached => cached || new Response('', { status: 503, statusText: 'Offline' }))
            )
    );
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