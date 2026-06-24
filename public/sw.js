const CACHE_VERSION = "v74";
// Pre-cache stable runtime deps. The app shell and bundles are cached after a
// successful network fetch so phones do not get stuck on old UI code.
const CORE_ASSETS = [
    './manifest.json',
    'https://cdn.tailwindcss.com',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.asm.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.asm.wasm',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/python_stdlib.zip',
    'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/repodata.json',
    'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'
];

self.addEventListener('install', event => {
    console.log('Service Worker Installing:', CACHE_VERSION);

    event.waitUntil(
        caches.open(CACHE_VERSION)
            .then(cache => cache.addAll(CORE_ASSETS))
            .catch(error => {
                console.warn('Core pre-cache failed; continuing with runtime cache.', error);
            })
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', event => {
    console.log('Service Worker Activated:', CACHE_VERSION);

    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_VERSION) {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            return self.clients.claim();
        })
    );
});

// Network-first with cache fallback: try network, on failure serve from cache. Enables FULL OFFLINE support.
self.addEventListener('fetch', event => {
    const request = event.request;

    if (request.method !== 'GET') {
        event.respondWith(fetch(request));
        return;
    }

    event.respondWith(
        fetch(request)
            .then(networkResponse => {
                if (networkResponse.ok) {
                    caches.open(CACHE_VERSION).then(cache => cache.put(request, networkResponse.clone()));
                }
                return networkResponse;
            })
            .catch(() =>
                caches.open(CACHE_VERSION).then(cache =>
                    cache.match(request).then(cached => cached || new Response('', { status: 503, statusText: 'Offline' }))
                )
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

console.log('Service Worker loaded, version:', CACHE_VERSION);
