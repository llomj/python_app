const CACHE_VERSION = 'v266';
const CACHE_NAME = `python-mastery-${CACHE_VERSION}`;
const MANIFEST_URL = './offline-assets.json';

const cacheCompleteBuild = async () => {
    const manifestResponse = await fetch(MANIFEST_URL, { cache: 'no-store' });
    if (!manifestResponse.ok) throw new Error(`Offline manifest failed: ${manifestResponse.status}`);
    const manifest = await manifestResponse.json();
    if (manifest.version !== CACHE_VERSION || !Array.isArray(manifest.assets)) {
        throw new Error('Offline manifest does not match this service worker.');
    }

    const cache = await caches.open(CACHE_NAME);
    const assets = [MANIFEST_URL, ...manifest.assets];
    for (let index = 0; index < assets.length; index += 20) {
        await cache.addAll(assets.slice(index, index + 20));
    }
    const windows = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    windows.forEach(client => client.postMessage({ type: 'OFFLINE_READY', version: CACHE_VERSION }));
};

self.addEventListener('install', event => {
    event.waitUntil(cacheCompleteBuild().then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
    event.waitUntil((async () => {
        const cacheNames = await caches.keys();
        const previousCaches = cacheNames
            .filter(cacheName => cacheName.startsWith('python-mastery-') && cacheName !== CACHE_NAME)
            .sort()
            .reverse();
        const retainedCaches = new Set([CACHE_NAME, previousCaches[0]].filter(Boolean));
        await Promise.all(cacheNames
            .filter(cacheName => cacheName.startsWith('python-mastery-') && !retainedCaches.has(cacheName))
            .map(cacheName => caches.delete(cacheName)));
        await self.clients.claim();
    })());
});

const cachedResponse = request => caches.open(CACHE_NAME)
    .then(cache => cache.match(request, { ignoreSearch: true }));

self.addEventListener('fetch', event => {
    const request = event.request;
    if (request.method !== 'GET') return;

    event.respondWith((async () => {
        const cached = await cachedResponse(request);
        if (cached) return cached;

        try {
            const response = await fetch(request);
            if (response.ok) {
                const cache = await caches.open(CACHE_NAME);
                await cache.put(request, response.clone());
            }
            return response;
        } catch {
            if (request.mode === 'navigate') {
                return (await cachedResponse(new Request('./index.html'))) || Response.error();
            }
            return new Response('Offline asset unavailable', { status: 503 });
        }
    })());
});

self.addEventListener('message', event => {
    if (event.data?.type === 'SKIP_WAITING') self.skipWaiting();
    if (event.data?.type === 'FORCE_UPDATE_NOW') self.registration.update();
});
