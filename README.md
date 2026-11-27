# Hanvika IT Solutions - Streamlit Website

## Run locally

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local address displayed by Streamlit, normally `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push the repository to GitHub.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app using repository `lokeshkumarpuvvada/cloudprintagent`, branch `main`, and entrypoint `app.py`.
3. Use the supported Python version shown in the deployment settings. No app secrets are currently required.
4. Choose an available app subdomain, such as `hanvikaits`, to get a URL under `streamlit.app`.

Community Cloud documents customizable `*.streamlit.app` subdomains, not binding a custom domain such as `hanvikaits.com`. No repository setting can attach that domain; use a Streamlit subdomain or a host that supports custom domains. The latter also requires DNS access. Never commit `.streamlit/secrets.toml`; add any future secrets through the app's Cloud settings.

## Full PWA deployment

The PWA files are served from the site root so the service worker can control `/`.
Streamlit Community Cloud serves repository static files under `/app/static/` and
does not provide this app with a configurable `Service-Worker-Allowed` response
header. The install prompt and offline behavior therefore activate only when the
app is hosted behind a server that can expose the PWA files at the root.

For a self-hosted Streamlit deployment:

1. Run Streamlit on `127.0.0.1:8501` and terminate HTTPS at Nginx.
2. Adapt `deploy/nginx-pwa.conf` to the checkout path and include it inside the
   HTTPS server block. It serves only the PWA files at the root and proxies the
   remaining requests, including Streamlit WebSockets, to the app.
3. Keep `Strict-Transport-Security` on HTTPS only. Start with the provided
   Content-Security-Policy-Report-Only header, review browser reports, and only
   enforce a policy after confirming Streamlit and required external assets work.
4. Validate the Nginx configuration with `nginx -t` before reloading it.

The service worker caches only same-origin static assets and the offline page.
Navigation requests are network-first; Streamlit/API requests are not cached so
user-specific data is not persisted in Cache Storage. Offline mode displays an
informational page; Streamlit interactions still require a live connection.
Increment `CACHE_VERSION` in `sw.js` when changing the cache behavior or
pre-cached assets.

## Optional privacy-oriented analytics

The app loads [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/get-started/)
only when a site token is configured. Create a Web Analytics site for the
production hostname, then add the token in Streamlit Community Cloud's Secrets
settings or in the ignored local file
`.streamlit/secrets.toml`:

```toml
[analytics]
cloudflare_web_analytics_token = "PASTE_SITE_TOKEN_HERE"
```

Do not commit the real token. The app does not write visitor IP addresses,
inquiry data, or analytics records to this GitHub repository. Cloudflare still
receives beacon requests and may process connection metadata under its privacy
terms; see the in-app Privacy Policy.