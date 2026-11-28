# Hanvika IT Solutions - Streamlit Website

**README last updated:** 2026-11-28

## Run locally

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local address displayed by Streamlit, normally `http://localhost:8501`.

On Windows, if using a project-local virtual environment:

```powershell
Set-Location "E:\git\hit"
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py --server.address 127.0.0.1 --server.port 8501
```

Check that the app is responding with `curl.exe -I http://127.0.0.1:8501`;
a successful response includes `HTTP/1.1 200 OK`.

## Run the workflow test

`test_app.py` contains a sample pytest assertion and checks that the PC Assembly
catalog references the repository-hosted images. Pytest is not part of the app
runtime requirements; install it in the development environment before running:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -q test_app.py
```

## Deploy on Streamlit Community Cloud

1. Push the repository to GitHub.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), create an app using repository `lokeshkumarpuvvada/cloudprintagent`, branch `main`, and entrypoint `app.py`.
3. Use the supported Python version shown in the deployment settings. No app secrets are currently required.
4. Choose an available app subdomain, such as `hanvikaits`, to get a URL under `streamlit.app`.

Community Cloud documents customizable `*.streamlit.app` subdomains, not binding a custom domain such as `hanvikaits.com`. No repository setting can attach that domain; use a Streamlit subdomain or a host that supports custom domains. The latter also requires DNS access. Never commit `.streamlit/secrets.toml`; add any future secrets through the app's Cloud settings.

## Service information

The hero status card groups services into `ONLINE` and `ON-SITE` lists. On-site
PC Assembly & Setup and Hardware Troubleshooting entries link to their service
details and catalogs; preventive maintenance is covered by the existing Network
AMC service.

Hanvika IT Solutions provides administrative guidance only for warranty
assistance. Warranty terms, coverage, and claim approvals are determined solely
by the respective hardware manufacturers. The service does not modify or
conflict with official manufacturer policies.

## Site metadata

The page metadata is defined in `app.py` and added to the document head at
runtime. Keep this reference in sync whenever those values change.

- Page title and Open Graph title: `Hanvika IT Solutions | IT Support in Guntur`
- SEO description and Open Graph description: `Local IT support in Guntur:
  office LAN and Wi-Fi setup, Tally and printer sharing, network AMC, firewall,
  antivirus, and Windows/Linux server support.`
- SEO keywords: `IT services Guntur, IT support Guntur, computer networking
  Guntur, office network setup, office LAN setup, Wi-Fi installation Guntur,
  Tally data sharing, printer and file sharing, network AMC, firewall,
  antivirus support, Windows server setup, Linux server support, hardware
  support Guntur, IT infrastructure Andhra Pradesh`
- PWA name: `Hanvika IT Solutions`
- Theme color: `#070b17`
- Mobile web app metadata enables install-style display on supported browsers;
  tile color and tile image reference the PWA icons under `/icons/`.

## Website maintenance workflow

Follow this sequence for future website changes:

1. Confirm the requested behavior and inspect the relevant code in `app.py`,
   related assets, and this README before editing.
2. Reuse existing service details, catalog entries, styles, and helpers where
   possible. For new services, keep the detail IDs, cards, status-card links,
   inquiry options, and catalog images consistent. Add app-served image files
   under `static/` and keep that directory limited to public assets.
   Catalog zoom behavior is automatic: a single image has zoom/close controls;
   multiple images have next/previous controls and close when moved past an end.
3. Keep site metadata, service descriptions, warranty/legal wording, and this
   README synchronized whenever their source values change. Do not invent
   contact details or commit credentials.
4. Run the syntax check:

   ```powershell
   .\.venv\Scripts\python.exe -m py_compile app.py
   ```

5. Run the app locally and check the changed UI in a browser. Verify relevant
   links, detail/policy close controls, image loading, and desktop/mobile
   layouts; confirm the local endpoint returns `200 OK`.
6. For security-sensitive or deployment changes, review the affected app and
   deployment configuration. Treat UI controls as navigation only; they do not
   authenticate users or protect private operations.
7. Deploy only after checks pass, using the applicable deployment instructions
   above. Record each significant change with its date in the log below.

## Recent change record

[2026-11-28] Updated PC Assembly catalog images to use the root-level GitHub
  repository image URLs instead of `/app/static/`; verified all three raw image
  URLs return `200 image/jpeg`. Added a pytest assertion for the generated URLs.
[2026-11-28] Added previous/next controls when zooming multiple images in the
  any service catalog. Single-image catalogs keep zoom/close only; multi-image
  catalogs close at either end and reopen at the thumbnail that started preview.
[2026-11-28] Added `test_app.py` with a sample pytest assertion to smoke-test
  the test workflow and checks for catalog image URLs/navigation. Verified
  locally: 2 tests passed.
[2026-11-28] Restarted the local Streamlit app after enabling static serving and
  verified that all three PCA image routes return JPEGs. Browser checks confirmed
  the PC Assembly & Setup card image loads with `object-fit: cover` and all three
  catalog images load; public-site deployment is still pending.
[2026-11-28] Clarified warranty support as administrative guidance only; hardware
  manufacturers alone determine warranty terms, coverage, and claim approvals.
[2026-11-28] Added PC Assembly & Setup and Hardware Troubleshooting as on-site services
  with dedicated detail/catalog entries. Existing Network AMC covers preventive
  maintenance.
[2026-11-28] Added the amber ON-SITE indicator beside ONLINE and kept the on-site links in
  the status card. Aligned the desktop hero and status-card heights.
[2026-11-28] Fixed catalog images to use the verified GitHub Pages image host after the
  previous raw GitHub URL returned 404. Browser verification confirmed 28/28
  images loaded.
[2026-11-28] Added the three supplied PCA images to the PC Assembly & Setup
  service card and catalog. They were initially served from Streamlit's
  `/app/static/` path; the current GitHub-hosted image URL is recorded above.
[2026-11-28] Documented the current SEO, Open Graph, and PWA metadata in this README.
[2026-11-28] Smoke-tested service and policy navigation, detail/policy close controls,
  and catalog image zoom. A focused review reported no exploitable issues in
  the reviewed app and deployment files; this is not a guarantee against all
  attacks or a review of hosting/account security.

## Mobile experience

Service catalog images load from the verified GitHub Pages image path. The
detail catalog uses a single-column layout on narrow screens to keep images
readable.
PC Assembly & Setup images are hosted at the root of the `cloudprintagent`
GitHub repository and referenced through its `raw.githubusercontent.com` URLs.

The Tidio live chat launcher appears on page load. On mobile, it hides while
visitors scroll and reappears near the bottom of the page; the chat conversation
opens only when the visitor selects the launcher. Tidio may process page, device,
and chat data under its own privacy policy.

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

## Website data and analytics

The app has no website database and does not use analytics or advertising
trackers. The Tidio live chat widget loads when a visitor opens the page; Tidio
may process page, device, and chat data under its own privacy policy. Hosting
providers may process standard access logs, and third-party display assets may
receive standard connection data; see the in-app Privacy Policy.