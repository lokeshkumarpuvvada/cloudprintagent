/* Bump this value when changing cache behavior or offline assets. */
const CACHE_VERSION = "v1";
const CACHE_PREFIX = "hanvika-pwa-";
const ASSET_CACHE = `${CACHE_PREFIX}${CACHE_VERSION}-assets`;
const OFFLINE_CACHE = `${CACHE_PREFIX}${CACHE_VERSION}-offline`;
const OFFLINE_URL = "/offline.html";
const PRECACHE_URLS = [
  OFFLINE_URL,
  "/manifest.json",
  "/icons/icon-192.png",
  "/icons/icon-512.png",
  "/icons/maskable-192.png",
  "/icons/maskable-512.png",
  "/icons/apple-touch-icon.png",
  "/icons/mstile-150.png"
];
const STATIC_DESTINATIONS = new Set(["style", "script", "image", "font"]);
const STATIC_FILE_PATTERN = /\.(?:css|js|mjs|png|jpe?g|gif|webp|svg|ico|woff2?|ttf|otf)$/i;
const MAX_ASSET_ENTRIES = 80;

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(OFFLINE_CACHE);
    await cache.addAll(PRECACHE_URLS);
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const cacheNames = await caches.keys();
    await Promise.all(cacheNames
      .filter((name) =>
        name.startsWith(CACHE_PREFIX) &&
        name !== ASSET_CACHE &&
        name !== OFFLINE_CACHE
      )
      .map((name) => caches.delete(name)));
    await self.clients.claim();
  })());
});

function isSameOriginGet(request, url) {
  return request.method === "GET" && url.origin === self.location.origin;
}

function isCacheableStaticAsset(request, url) {
  return STATIC_DESTINATIONS.has(request.destination) &&
    !request.headers.has("range") &&
    !url.search &&
    STATIC_FILE_PATTERN.test(url.pathname);
}

function isCacheableResponse(request, response) {
  const cacheControl = response.headers.get("cache-control") || "";
  const contentType = response.headers.get("content-type") || "";
  const expectedTypes = {
    style: ["text/css"],
    script: ["application/javascript", "text/javascript", "application/ecmascript", "text/ecmascript"],
    image: ["image/"],
    font: ["font/", "application/font-woff", "application/vnd.ms-fontobject"]
  }[request.destination] || [];
  return response.status === 200 &&
    response.type === "basic" &&
    !/\b(?:private|no-store|no-cache)\b/i.test(cacheControl) &&
    !/\*/.test(response.headers.get("vary") || "") &&
    expectedTypes.some((type) => contentType.toLowerCase().startsWith(type));
}

async function trimCache(cacheName) {
  const cache = await caches.open(cacheName);
  const requests = await cache.keys();
  const excess = requests.length - MAX_ASSET_ENTRIES;
  if (excess > 0) {
    await Promise.all(requests.slice(0, excess).map((request) => cache.delete(request)));
  }
}

async function cacheFirstStaticAsset(request) {
  const cache = await caches.open(ASSET_CACHE);
  const cached = await cache.match(request);
  if (cached) return cached;

  const response = await fetch(request);
  if (isCacheableResponse(request, response)) {
    await cache.put(request, response.clone());
    await trimCache(ASSET_CACHE);
  }
  return response;
}

async function networkFirstNavigation(request) {
  try {
    return await fetch(request);
  } catch {
    const offlinePage = await caches.match(OFFLINE_URL);
    return offlinePage || new Response(
      "You are offline. Reconnect and try again.",
      { status: 503, headers: { "Content-Type": "text/plain; charset=utf-8" } }
    );
  }
}

function networkOnly(request) {
  return fetch(request, { cache: "no-store" });
}

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (!isSameOriginGet(request, url)) return;

  if (request.mode === "navigate") {
    event.respondWith(networkFirstNavigation(request));
    return;
  }

  // Streamlit/API traffic stays network-only so user-specific data is never cached.
  if (url.pathname === "/_stcore" || url.pathname.startsWith("/_stcore/")) {
    event.respondWith(networkOnly(request));
    return;
  }

  if (isCacheableStaticAsset(request, url)) {
    event.respondWith(cacheFirstStaticAsset(request));
    return;
  }

  event.respondWith(networkOnly(request));
});
