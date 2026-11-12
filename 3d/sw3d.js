// Costa Turbo 3D: funciona sin conexión. Código y páginas: primero la red; modelos, texturas y sonidos: primero la caché.
const CACHE = 'ct3d-v1';
self.addEventListener('install', e => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('ct3d-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url); if (e.request.method !== 'GET' || !u.pathname.includes('/3d/') && u.origin === location.origin) return;
  const heavy = /\.(glb|gltf|bin|jpg|jpeg|png|webp|hdr|exr|mp3|ogg|wav|woff2?)$/i.test(u.pathname);
  if (heavy) e.respondWith(caches.open(CACHE).then(c => c.match(e.request).then(r => r || fetch(e.request).then(n => { if (n.ok) c.put(e.request, n.clone()); return n; }))));
  else e.respondWith(fetch(e.request).then(n => { if (n.ok) caches.open(CACHE).then(c => c.put(e.request, n.clone())); return n; }).catch(() => caches.match(e.request)));
});
