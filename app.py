import json
from datetime import date
from html import escape
from urllib.parse import quote

import streamlit as st

COPYRIGHT_YEAR = date.today().year
PHONE_DISPLAY = "+91 9885138489"
PHONE_LINK = "919885138489"
ADDRESS = "Guntur - 522002, Andhra Pradesh, India"
APP_VERSION = "1.0"
WHATSAPP_URL = f"https://wa.me/{PHONE_LINK}"
IMAGE_BASE = "https://lokeshkumarpuvvada.github.io/hit"
GITHUB_CATALOG_IMAGE_BASE = "https://raw.githubusercontent.com/lokeshkumarpuvvada/cloudprintagent/main"
PWA_NAME = "Hanvika IT Solutions"
PWA_THEME_COLOR = "#070b17"
SEO_DESCRIPTION = (
    "Local IT support in Guntur: office LAN and Wi-Fi setup, Tally and printer sharing, "
    "network AMC, firewall, antivirus, and Windows/Linux server support."
)
SEO_KEYWORDS = (
    "IT services Guntur, IT support Guntur, computer networking Guntur, office network setup, "
    "office LAN setup, Wi-Fi installation Guntur, Tally data sharing, printer and file sharing, "
    "network AMC, firewall security, antivirus support, Windows server setup, Linux server support, "
    "hardware support Guntur, IT infrastructure Andhra Pradesh"
)
GITHUB_CATALOG_IMAGES = {"pca (1).jpeg", "pca (2).jpeg", "pca (3).jpeg"}


def catalog_image_url(filename):
    if filename in GITHUB_CATALOG_IMAGES:
        return f"{GITHUB_CATALOG_IMAGE_BASE}/{quote(filename, safe='')}"
    return f"{IMAGE_BASE}/{quote(filename, safe='')}"


# Font Awesome Free 6.7.2 by Fonticons, Inc.; icons licensed CC BY 4.0.
# https://fontawesome.com/license/free
WHATSAPP_ICON = (
    '<svg class="whatsapp-icon" viewBox="0 0 448 512" aria-hidden="true">'
    '<path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>'
    '</svg>'
)
CALL_ICON = (
    '<svg class="call-icon" viewBox="0 0 512 512" aria-hidden="true">'
    '<path fill="currentColor" d="M164.9 24.6c-7.7-18.6-28-28.5-47.4-23.2l-88 24C12.1 30.2 0 46 0 64 0 311.4 200.6 512 448 512c18 0 33.8-12.1 38.6-29.5l24-88c5.3-19.4-4.6-39.7-23.2-47.4l-96-40c-16.3-6.8-35.2-2.1-46.3 11.6L304.7 368C234.3 334.7 177.3 277.7 144 207.3L193.3 167c13.7-11.2 18.4-30 11.6-46.3l-40-96z"/>'
    '</svg>'
)


st.set_page_config(
    page_title="Hanvika IT Solutions | IT Support in Guntur",
    page_icon="H",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(
    f"""
    <script>
    (() => {{
        const pwaName = {json.dumps(PWA_NAME)};
        const pwaThemeColor = {json.dumps(PWA_THEME_COLOR)};
        const metadata = [
            ["name", "description", {json.dumps(SEO_DESCRIPTION)}],
            ["name", "keywords", {json.dumps(SEO_KEYWORDS)}],
            ["property", "og:title", "Hanvika IT Solutions | IT Support in Guntur"],
            ["property", "og:description", {json.dumps(SEO_DESCRIPTION)}]
        ];
        for (const [attribute, key, content] of metadata) {{
            let tag = document.head.querySelector('meta[' + attribute + '="' + key + '"]');
            if (!tag) {{
                tag = document.createElement("meta");
                tag.setAttribute(attribute, key);
                document.head.appendChild(tag);
            }}
            tag.setAttribute("content", content);
        }}

        const setMeta = (name, content) => {{
            let tag = document.head.querySelector('meta[name="' + name + '"]');
            if (!tag) {{
                tag = document.createElement("meta");
                tag.name = name;
                document.head.appendChild(tag);
            }}
            tag.content = content;
        }};
        const setLink = (rel, href, sizes) => {{
            let tag = document.head.querySelector('link[rel="' + rel + '"]');
            if (!tag) {{
                tag = document.createElement("link");
                tag.rel = rel;
                document.head.appendChild(tag);
            }}
            tag.href = href;
            if (sizes) tag.sizes = sizes;
        }};

        setMeta("theme-color", pwaThemeColor);
        setMeta("mobile-web-app-capable", "yes");
        setMeta("apple-mobile-web-app-capable", "yes");
        setMeta("apple-mobile-web-app-title", pwaName);
        setMeta("apple-mobile-web-app-status-bar-style", "black-translucent");
        setMeta("msapplication-TileColor", pwaThemeColor);
        setMeta("msapplication-TileImage", "/icons/mstile-150.png");

        let installButton = document.getElementById("hanvika-install-app");
        if (!installButton) {{
            installButton = document.createElement("button");
            installButton.id = "hanvika-install-app";
            installButton.type = "button";
            installButton.textContent = "Install App";
            installButton.setAttribute("aria-label", "Install Hanvika IT Solutions");
            installButton.hidden = true;
            installButton.style.cssText = [
                "position:fixed",
                "right:1rem",
                "bottom:1rem",
                "z-index:2147483000",
                "padding:.75rem 1rem",
                "border:1px solid rgba(255,255,255,.28)",
                "border-radius:999px",
                "background:#087e83",
                "color:#fff",
                "font:600 14px system-ui,sans-serif",
                "box-shadow:0 8px 24px rgba(0,0,0,.28)",
                "cursor:pointer"
            ].join(";");
            document.body.appendChild(installButton);
        }}

        if (!window.__hanvikaInstallPromptBound) {{
            window.__hanvikaInstallPromptBound = true;
            let deferredInstallPrompt = null;
            window.addEventListener("beforeinstallprompt", (event) => {{
                event.preventDefault();
                deferredInstallPrompt = event;
                installButton.hidden = false;
            }});
            installButton.addEventListener("click", async () => {{
                if (!deferredInstallPrompt) return;
                const promptEvent = deferredInstallPrompt;
                deferredInstallPrompt = null;
                installButton.disabled = true;
                try {{
                    await promptEvent.prompt();
                    await promptEvent.userChoice;
                    installButton.hidden = true;
                }} catch (error) {{
                    console.error("PWA install prompt failed:", error);
                }} finally {{
                    installButton.disabled = false;
                }}
            }});
            window.addEventListener("appinstalled", () => {{
                installButton.hidden = true;
            }});
        }}

        const isSecureOrigin =
            location.protocol === "https:" ||
            ["localhost", "127.0.0.1", "[::1]"].includes(location.hostname);
        if (isSecureOrigin && "serviceWorker" in navigator) {{
            fetch("/manifest.json", {{ cache: "no-store" }})
                .then(async (response) => {{
                    const contentType = response.headers.get("content-type") || "";
                    if (!response.ok || !contentType.includes("json")) return;

                    const manifest = await response.json();
                    if (!manifest || manifest.name !== pwaName) return;
                    if (manifest.start_url !== "/" || manifest.scope !== "/") {{
                        console.error("PWA manifest has an unexpected name or scope.");
                        return;
                    }}

                    setLink("manifest", "/manifest.json");
                    setLink("apple-touch-icon", "/icons/apple-touch-icon.png");
                    setLink("icon", "/icons/icon-192.png", "192x192");
                    await navigator.serviceWorker.register("/sw.js", {{
                        scope: "/",
                        updateViaCache: "none"
                    }});
                }})
                .catch((error) => console.error("PWA setup failed:", error));
        }}

    }})();
    </script>
    """,
    unsafe_allow_javascript=True,
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, .stApp, .stApp *, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }
    html, body { min-height: 100%; background: #070b17; scroll-behavior: smooth; }
    .stApp {
        position: relative;
        isolation: isolate;
        min-height: 100vh;
        background: transparent;
        color: #e5eef8;
    }
    .stApp::before, .stApp::after {
        content: "";
        position: fixed;
        inset: -8vh -8vw;
        z-index: -1;
        pointer-events: none;
    }
    .stApp::before {
        background:
            radial-gradient(ellipse at 12% 8%, rgba(147, 195, 255, .24), transparent 34rem),
            radial-gradient(ellipse at 88% 35%, rgba(117, 105, 235, .15), transparent 32rem),
            radial-gradient(ellipse at 48% 78%, rgba(16, 153, 165, .11), transparent 36rem),
            linear-gradient(160deg, #172c48 0%, #0c1830 42%, #070b17 100%);
        transform-origin: center top;
        animation: space-zoom 55s ease-in-out infinite alternate;
        will-change: transform;
    }
    .stApp::after {
        opacity: .38;
        background-image:
            radial-gradient(1.5px 1.5px at 24px 32px, rgba(220, 238, 255, .78) 50%, transparent 100%),
            radial-gradient(1px 1px at 88px 112px, rgba(166, 207, 255, .64) 50%, transparent 100%),
            radial-gradient(1px 1px at 142px 56px, rgba(220, 238, 255, .5) 50%, transparent 100%);
        background-size: 180px 180px;
        animation: stars-drift 70s linear infinite alternate;
        will-change: transform;
    }
    @keyframes space-zoom {
        from { transform: scale(1); }
        to { transform: scale(1.08); }
    }
    @keyframes stars-drift {
        from { transform: translate3d(0, 0, 0); }
        to { transform: translate3d(0, -4vh, 0); }
    }
    @supports (animation-timeline: scroll()) {
        [data-testid="stMain"] {
            scroll-timeline-name: --page-scroll;
            scroll-timeline-axis: block;
        }
    }
    @media (prefers-reduced-motion: reduce) {
        html { scroll-behavior: auto; }
        .stApp::before, .stApp::after, .hero::after {
            animation: none !important;
            transform: none !important;
            will-change: auto;
        }
    }
    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }
    .st-key-services_section,
    .st-key-estimator_section,
    .st-key-contact_section {
        padding: 1.4rem clamp(1rem, 3vw, 2.2rem) 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(123, 164, 198, 0.18);
        border-radius: 26px;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.14);
    }
    .st-key-services_section {
        background:
            radial-gradient(ellipse at 5% 0%, rgba(72, 152, 238, .14), transparent 34rem),
            linear-gradient(135deg, rgba(20, 38, 61, .58), rgba(16, 24, 43, .46));
        border-color: rgba(176, 216, 240, .28);
        box-shadow: 0 24px 60px rgba(0, 0, 0, .16), inset 0 1px 0 rgba(255, 255, 255, .1);
        backdrop-filter: blur(22px) saturate(145%);
    }
    .st-key-estimator_section {
        background:
            radial-gradient(ellipse at 4% 5%, rgba(161, 98, 255, 0.17), transparent 32rem),
            radial-gradient(ellipse at 95% 95%, rgba(245, 185, 95, 0.10), transparent 28rem),
            linear-gradient(135deg, #1a1730, #15192d 58%, #211a2c);
    }
    .st-key-contact_section {
        background:
            radial-gradient(ellipse at 90% 5%, rgba(12, 184, 155, 0.15), transparent 34rem),
            linear-gradient(135deg, #0c202a, #10232b 58%, #102b2b);
    }
    .st-key-estimator_section,
    .st-key-contact_section {
        padding: 1rem clamp(.9rem, 2.5vw, 1.8rem) 1.35rem;
        margin: 1.25rem 0;
    }
    .st-key-services_section .section-heading,
    .st-key-estimator_section .section-heading,
    .st-key-contact_section .section-heading {
        margin: 2rem 0 1.25rem;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"] { display: none; }

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.55rem 1rem;
        border: 1px solid rgba(52, 177, 174, 0.26);
        border-radius: 14px 14px 0 0;
        background: linear-gradient(90deg, rgba(10, 112, 111, 0.30), rgba(17, 44, 75, 0.72), rgba(81, 57, 123, 0.25));
        backdrop-filter: blur(14px);
        color: #c4d5e5;
        font-size: 0.8rem;
        text-align: left;
    }
    .topbar-info { display: flex; align-items: center; flex-wrap: wrap; gap: .35rem 1rem; min-width: 0; }
    .topbar-phone { display: inline-flex; flex: 0 0 auto; align-items: center; gap: .35rem; color: #9ce8dc; font-weight: 800; text-decoration: none; white-space: nowrap; }
    .topbar-phone .call-icon { color: #38bdf8; vertical-align: middle; }
    .topbar-location { color: #c4d5e5; }
    .site-header {
        box-sizing: border-box;
        width: 100%;
        container-type: inline-size;
        container-name: site-header;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.25rem;
        padding: .95rem 1.2rem;
        border: 1px solid #1c3046;
        border-top: 0;
        border-radius: 0 0 18px 18px;
        background: rgba(10, 22, 38, .74);
        box-shadow: 0 15px 40px rgba(0, 0, 0, .2), inset 0 1px 0 rgba(255, 255, 255, .06);
        backdrop-filter: blur(14px);
        position: sticky;
        top: 0;
        z-index: 50;
    }
    .header-brand { display: flex; align-items: center; gap: .75rem; min-width: max-content; }
    .brand-mark {
        width: 48px;
        height: 48px;
        display: grid;
        place-items: center;
        border-radius: 12px;
        background: linear-gradient(135deg, #09b8a5, #47a8ff 55%, #9b7aff);
        color: white;
        font-size: 1.5rem;
        font-weight: 800;
        box-shadow: 0 10px 30px rgba(38, 180, 193, 0.28);
    }
    .brand-name { font-size: 1rem; font-weight: 800; color: #f5f9ff; letter-spacing: .015em; }
    .brand-name span { color: #7bcaff; }
    .brand-location { margin-top: .2rem; color: #b0bfce; font-size: .7rem; letter-spacing: .08em; }
    .header-nav {
        display: grid;
        flex: 1 1 auto;
        grid-template-columns: repeat(8, max-content);
        align-items: center;
        justify-content: center;
        gap: .2rem;
        min-width: 0;
    }
    .header-nav a {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 34px;
        padding: .35rem .4rem;
        border: 1px solid rgba(187, 217, 240, .22);
        border-radius: 9px;
        background: rgba(210, 230, 248, .1);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1);
        backdrop-filter: blur(16px) saturate(145%);
        color: #adbed0;
        font-size: .72rem;
        font-weight: 700;
        text-decoration: none;
        white-space: nowrap;
        transition: color 150ms ease, background 150ms ease, border-color 150ms ease, transform 150ms ease, box-shadow 150ms ease;
    }
    .header-nav a:hover {
        transform: translateY(-2px) scale(1.035);
        border-color: rgba(154, 224, 232, .42);
        background: rgba(72, 158, 177, .24);
        color: #b7eee5;
        box-shadow: 0 5px 14px rgba(0, 0, 0, .2);
    }
    .header-call { display: flex; flex: 0 0 auto; align-items: center; }
    .mobile-menu { display: none; position: relative; z-index: 60; }
    .mobile-menu summary {
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border: 1px solid #2b465e;
        border-radius: 11px;
        background: rgba(22, 44, 64, .42);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .12);
        backdrop-filter: blur(16px) saturate(145%);
        color: #e8f2fb;
        cursor: pointer;
        font-size: 1.45rem;
        line-height: 1;
        list-style: none;
    }
    .mobile-menu summary::-webkit-details-marker { display: none; }
    .mobile-menu[open] summary { border-color: #3ab7b4; color: #7fe6d2; }
    .mobile-menu-panel {
        position: absolute;
        top: calc(100% + .65rem);
        right: 0;
        display: grid;
        gap: .2rem;
        width: min(290px, calc(100vw - 2rem));
        max-height: 70vh;
        overflow-y: auto;
        padding: .65rem;
        border: 1px solid rgba(190, 220, 244, .24);
        border-radius: 16px;
        background: rgba(8, 20, 35, .68);
        box-shadow: 0 18px 42px rgba(0, 0, 0, .4);
        backdrop-filter: blur(20px) saturate(145%);
    }
    .mobile-menu-panel a {
        display: flex;
        align-items: center;
        gap: .65rem;
        padding: .68rem .75rem;
        border: 1px solid rgba(190, 220, 244, .2);
        border-radius: 10px;
        background: rgba(210, 230, 248, .09);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .08);
        backdrop-filter: blur(10px);
        color: #c4d5e5;
        font-size: .88rem;
        font-weight: 700;
        text-decoration: none;
        transition: background 150ms ease, border-color 150ms ease, transform 150ms ease;
    }
    .mobile-menu-panel a:hover {
        transform: translateY(-1px) scale(1.015);
        border-color: rgba(154, 224, 232, .38);
        background: rgba(72, 158, 177, .2);
        color: #e7fbff;
    }
    .mobile-menu-panel a:focus-visible,
    .header-nav a:focus-visible {
        outline: 2px solid #78dfd0;
        outline-offset: 2px;
    }
    .header-action {
        box-sizing: border-box;
        flex: 0 0 auto;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 40px;
        padding: .5rem .65rem;
        border: 1px solid rgba(166, 222, 240, .38);
        border-radius: 11px;
        background: rgba(24, 112, 158, .42);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .18);
        backdrop-filter: blur(16px) saturate(150%);
        color: #fff !important;
        font-size: .76rem;
        font-weight: 800;
        text-decoration: none;
        white-space: nowrap;
        transition: 180ms ease;
    }
    .whatsapp-icon, .call-icon {
        display: block;
        flex: 0 0 18px;
        width: 18px;
        height: 18px;
        color: currentColor;
    }
    .whatsapp-cta {
        border: 1px solid #25d366 !important;
        background: #128c4a !important;
        color: #fff !important;
    }
    .whatsapp-cta:hover {
        border-color: #6be69a !important;
        background: #0f7a40 !important;
        color: #fff !important;
    }
    .call-cta {
        border: 1px solid rgba(77, 174, 235, .72) !important;
        background: linear-gradient(135deg, #075985, #0284c7) !important;
        color: #fff !important;
    }
    .call-cta:hover {
        border-color: #8bd5ff !important;
        background: linear-gradient(135deg, #0369a1, #0ea5e9) !important;
        color: #fff !important;
    }
    .header-action:hover { transform: translateY(-1px); filter: brightness(1.08); box-shadow: 0 5px 14px rgba(0, 0, 0, .2); }
    .hero {
        position: relative;
        isolation: isolate;
        padding: clamp(2rem, 4vw, 3rem) clamp(1.4rem, 3vw, 2.6rem);
        border: 1px solid #1b3048;
        border-radius: 28px;
        background:
            radial-gradient(circle at 85% 15%, rgba(41, 137, 255, 0.24), transparent 28rem),
            radial-gradient(circle at 15% 100%, rgba(12, 184, 155, 0.15), transparent 24rem),
            radial-gradient(circle at 100% 100%, rgba(161, 98, 255, 0.12), transparent 22rem),
            linear-gradient(145deg, #0c1a2b, #091525);
        overflow: hidden;
    }
    .hero-overview {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        align-items: stretch;
        gap: clamp(1rem, 2.5vw, 2rem);
        width: 100%;
        box-sizing: border-box;
        margin-top: clamp(1.25rem, 2.5vw, 2rem);
    }
    @media (min-width: 761px) {
        .hero-overview > .hero,
        .hero-overview > .status-card {
            height: 100%;
        }
    }
    .hero::after {
        content: "";
        position: absolute;
        top: -9rem;
        right: -7rem;
        width: 25rem;
        aspect-ratio: 1;
        border: 1px solid rgba(133, 190, 255, .17);
        border-radius: 50%;
        background: radial-gradient(circle at 42% 42%, rgba(91, 174, 255, .15), transparent 62%);
        box-shadow: 0 0 0 2.2rem rgba(123, 184, 255, .025), 0 0 0 4.4rem rgba(123, 184, 255, .02);
        pointer-events: none;
        animation: hero-orbit-drift 60s ease-in-out infinite alternate;
        will-change: transform;
    }
    .hero > * { position: relative; z-index: 1; }
    @keyframes hero-orbit-drift {
        from { transform: translate3d(0, 0, 0) scale(1); }
        to { transform: translate3d(0, 3rem, 0) scale(1.12); }
    }
    @supports (animation-timeline: scroll()) {
        .hero::after {
            animation: hero-scroll-parallax 1s linear both;
            animation-timeline: --page-scroll;
            animation-range: 0% 100%;
        }
    }
    @keyframes hero-scroll-parallax {
        from { transform: translate3d(0, 0, 0) scale(1); }
        to { transform: translate3d(0, 8rem, 0) scale(1.16); }
    }
    .eyebrow {
        display: inline-block;
        color: #7fe6d2;
        background: rgba(15, 91, 91, 0.24);
        border: 1px solid rgba(48, 190, 166, 0.35);
        border-radius: 999px;
        padding: 0.42rem 0.75rem;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .hero h1 {
        max-width: 840px;
        margin: 1rem 0 .8rem;
        color: #f7fbff;
        font-size: clamp(2rem, 4vw, 3.9rem);
        line-height: 1.04;
        letter-spacing: -0.035em;
    }
    .accent {
        color: #91c9ed;
        font-weight: 700;
    }
    .hero-copy {
        max-width: 730px;
        color: #b2c1d1;
        font-size: .98rem;
        line-height: 1.6;
    }
    .status-card, .service-card, .info-card {
        border: 1px solid rgba(186, 217, 241, .28);
        border-radius: 18px;
        background: linear-gradient(145deg, rgba(36, 62, 88, .48), rgba(8, 20, 34, .4));
        backdrop-filter: blur(18px) saturate(145%);
        box-shadow: 0 12px 32px rgba(0, 0, 0, .14), inset 0 1px 0 rgba(255, 255, 255, .12);
    }
    .status-card {
        padding: .9rem;
        border-color: rgba(186, 217, 241, .24);
        background:
            radial-gradient(ellipse at 100% 0%, rgba(35, 182, 170, .13), transparent 22rem),
            linear-gradient(145deg, rgba(30, 55, 79, .58), rgba(8, 20, 34, .46));
        box-shadow: 0 22px 54px rgba(0, 0, 0, .24), inset 0 1px 0 rgba(255, 255, 255, .12);
        backdrop-filter: blur(20px) saturate(145%);
    }
    .status-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: .6rem;
        padding-bottom: .85rem;
        border-bottom: 1px solid #203247;
    }
    .status-brand { display: flex; align-items: center; gap: .28rem; min-width: 0; }
    .status-light { width: 9px; height: 9px; flex: 0 0 9px; border-radius: 50%; }
    .status-light.red { background: #ff6b73; box-shadow: 0 0 10px rgba(255, 107, 115, .45); }
    .status-light.yellow { background: #f7c65a; box-shadow: 0 0 10px rgba(247, 198, 90, .38); }
    .status-light.green { background: #4fd69a; box-shadow: 0 0 10px rgba(79, 214, 154, .42); }
    .status-label { margin-left: .4rem; overflow: hidden; color: #93a6b9; font-family: Consolas, monospace; font-size: .68rem; text-overflow: ellipsis; white-space: nowrap; }
    .online { display: inline-flex; align-items: center; gap: .38rem; flex: 0 0 auto; }
    .online-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #52d59a;
        box-shadow: 0 0 10px rgba(82, 213, 154, .72);
        animation: status-pulse 1.8s ease-in-out infinite;
    }
    @keyframes status-pulse { 50% { opacity: .48; } }
    .status-rows { display: grid; gap: .48rem; padding: .7rem 0; }
    .status-row {
        display: flex;
        align-items: center;
        gap: .55rem;
        min-width: 0;
        padding: .55rem .65rem;
        border: 1px solid rgba(123, 164, 198, .14);
        border-radius: 13px;
        background: rgba(12, 29, 46, .34);
        backdrop-filter: blur(14px);
        color: inherit;
        text-decoration: none;
        cursor: pointer;
        transition: background 150ms ease, border-color 150ms ease, box-shadow 150ms ease, transform 150ms ease;
    }
    .status-row:hover {
        border-color: color-mix(in srgb, var(--status-accent) 48%, rgba(201, 230, 247, .5));
        background: rgba(35, 63, 84, .54);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .12);
        transform: translateY(-1px);
    }
    .status-row:focus-visible {
        outline: 2px solid #78dfd0;
        outline-offset: 3px;
    }
    .status-icon {
        display: grid;
        place-items: center;
        flex: 0 0 38px;
        width: 38px;
        height: 38px;
        border: 1px solid color-mix(in srgb, var(--status-accent) 36%, transparent);
        border-radius: 11px;
        background: color-mix(in srgb, var(--status-accent) 14%, #0b1828);
        color: var(--status-accent);
        font-size: 1.15rem;
    }
    .status-copy { flex: 1; min-width: 0; }
    .status-copy strong { display: block; color: #e5eef7; font-size: .82rem; line-height: 1.35; }
    .status-copy small { display: block; margin-top: .13rem; color: #b0bfce; font-size: .74rem; line-height: 1.45; }
    .status-check {
        display: grid;
        place-items: center;
        flex: 0 0 21px;
        width: 21px;
        height: 21px;
        border-radius: 50%;
        background: rgba(82, 213, 154, .12);
        color: #52d59a;
        font-size: .78rem;
        font-weight: 900;
    }
    .status-link-indicator {
        display: grid;
        place-items: center;
        flex: 0 0 20px;
        width: 20px;
        height: 20px;
        border: 1px solid rgba(186, 217, 241, .24);
        border-radius: 50%;
        background: rgba(210, 230, 248, .08);
        color: #d7e8f5;
        font-size: .72rem;
        font-weight: 800;
        transition: background 150ms ease, border-color 150ms ease;
    }
    .status-row:hover .status-link-indicator {
        border-color: rgba(205, 248, 243, .64);
        background: rgba(72, 158, 177, .28);
    }
    .status-footer {
        padding: .72rem .8rem;
        border: 1px solid rgba(48, 190, 166, .2);
        border-radius: 12px;
        background: rgba(9, 39, 45, .45);
        text-align: center;
    }
    .status-footer p { margin: 0; color: #b6c7d7; font-size: .72rem; line-height: 1.45; }
    .status-actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .55rem; margin-top: .55rem; }
    .status-action {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: .4rem;
        min-height: 38px;
        padding: .45rem .55rem;
        border: 1px solid rgba(120, 223, 208, .28);
        border-radius: 10px;
        background: rgba(25, 56, 70, .52);
        backdrop-filter: blur(12px);
        color: #b7eee5;
        font-size: .72rem;
        font-weight: 800;
        text-decoration: none;
        transition: background 150ms ease, border-color 150ms ease, transform 150ms ease;
    }
    .status-action:hover { border-color: rgba(196, 247, 241, .72); background: rgba(35, 122, 135, .48); transform: translateY(-1px) scale(1.02); }
    @media (prefers-reduced-motion: reduce) {
        .online-dot { animation: none; }
    }
    .online {
        color: #52d59a;
        background: rgba(82, 213, 154, 0.1);
        border-radius: 999px;
        padding: 0.28rem 0.55rem;
        font-size: 0.75rem;
        font-weight: 800;
    }
    .status-header-actions { display: flex; align-items: center; gap: .38rem; flex: 0 0 auto; }
    .onsite {
        display: inline-flex;
        align-items: center;
        gap: .38rem;
        flex: 0 0 auto;
        color: #f5b95f;
        background: rgba(245, 185, 95, 0.11);
        border: 1px solid rgba(245, 185, 95, 0.18);
        border-radius: 999px;
        padding: 0.28rem 0.55rem;
        font-size: 0.75rem;
        font-weight: 800;
    }
    .onsite-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #f5b95f;
        box-shadow: 0 0 10px rgba(245, 185, 95, .72);
    }
    .section-heading {
        text-align: center;
        margin: 4.5rem 0 2rem;
    }
    .section-heading h2 {
        color: #f4f8fc;
        font-size: 2.35rem;
        letter-spacing: -0.02em;
        margin: 0.6rem 0;
    }
    .st-key-services_section .section-heading h2 {
        font-size: clamp(1.45rem, 4vw, 2.1rem);
        line-height: 1.15;
    }
    .section-heading p {
        max-width: 700px;
        margin: auto;
        color: #b0bfce;
    }
    .section-heading .service-guide {
        display: inline-flex;
        align-items: center;
        gap: .45rem;
        max-width: 100%;
        margin: .65rem auto 0;
        padding: .5rem .85rem;
        border: 1px solid rgba(73, 198, 185, .24);
        border-radius: 999px;
        background: rgba(15, 54, 59, .42);
        backdrop-filter: blur(12px);
        color: #aee4d9;
        font-size: .82rem;
        line-height: 1.45;
    }
    .service-card {
        display: flex;
        flex: 0 0 calc(32% - .8rem);
        scroll-snap-align: start;
        scroll-snap-stop: always;
        min-width: 0;
        flex-direction: column;
        height: 430px;
        overflow: hidden;
        border: 1px solid rgba(123, 164, 198, .18);
        border-top: 2px solid var(--card-accent, #35b8c2);
        border-radius: 17px;
        background: linear-gradient(150deg, rgba(27, 46, 65, .98), rgba(10, 22, 36, .98));
        box-shadow: 0 14px 34px rgba(0, 0, 0, .2), inset 0 1px 0 rgba(255, 255, 255, .14);
        transition: border-color 160ms ease, transform 160ms ease, box-shadow 160ms ease;
    }
    .service-card-image-link {
        display: block;
        min-height: 0;
        flex: 0 0 44%;
        overflow: hidden;
        border-bottom: 1px solid rgba(186, 217, 241, .14);
    }
    .service-card-image-link:focus-visible {
        outline: 2px solid #78dfd0;
        outline-offset: -3px;
    }
    .service-card-image {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 300ms ease;
    }
    .service-card-image-link .service-card-image {
        max-width: none;
        object-fit: cover;
    }
    .service-card-content {
        display: flex;
        width: 100%;
        min-width: 0;
        flex: 1;
        flex-direction: column;
        justify-content: flex-start;
        padding: 1rem;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .04);
    }
    .service-card:hover {
        border-color: color-mix(in srgb, var(--card-accent, #35b8c2) 52%, rgba(201, 230, 247, .5));
        box-shadow: 0 16px 36px rgba(0, 0, 0, .24), inset 0 1px 0 rgba(255, 255, 255, .2);
        transform: translateY(-3px);
    }
    .service-card:hover .service-card-image { transform: scale(1.045); }
    .service-card-image-link:focus-visible .service-card-image { transform: scale(1.035); }
    .service-preview-grid {
        display: flex;
        align-items: stretch;
        gap: 1rem;
        overflow-x: auto;
        overscroll-behavior-x: contain;
        padding: .2rem .1rem .45rem;
        scroll-padding-inline: .1rem;
        scroll-snap-type: x mandatory;
        scroll-behavior: smooth;
        scrollbar-width: none;
        -ms-overflow-style: none;
        -webkit-overflow-scrolling: touch;
    }
    .service-preview-grid::-webkit-scrollbar { display: none; }
    @media (prefers-reduced-motion: reduce) {
        .service-preview-grid { scroll-behavior: auto; }
        .service-card, .service-card-image { transition: none; }
    }
    .service-card h3 { margin: 0 0 .45rem; color: #f5f8fc; font-size: 1.15rem; line-height: 1.25; }
    .service-card p {
        display: -webkit-box;
        overflow: hidden;
        margin: 0 0 .85rem;
        color: #d3deea;
        font-size: .84rem;
        line-height: 1.5;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 3;
    }
    .service-card-link {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: .5rem;
        width: 100%;
        min-height: 42px;
        margin-top: auto;
        padding: .55rem .75rem;
        border: 1px solid color-mix(in srgb, var(--card-accent, #35b8c2) 32%, transparent);
        border-radius: 11px;
        background: color-mix(in srgb, var(--card-accent, #35b8c2) 12%, rgba(12, 28, 44, .48));
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .12);
        backdrop-filter: blur(14px) saturate(145%);
        color: var(--card-accent, #7bded1);
        font-size: .8rem;
        font-weight: 800;
        text-decoration: none;
        transition: border-color 150ms ease, background 150ms ease, transform 150ms ease;
    }
    .service-card-link:focus-visible {
        outline: 2px solid #78dfd0;
        outline-offset: 3px;
    }
    .service-card-link:hover {
        border-color: color-mix(in srgb, var(--card-accent, #35b8c2) 65%, transparent);
        background: color-mix(in srgb, var(--card-accent, #35b8c2) 20%, rgba(14, 35, 52, .54));
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .2);
        transform: translateY(-1px);
    }
    .detail-group {
        display: none;
    }
    .detail-group:target {
        position: fixed;
        inset: 0;
        z-index: 9990;
        display: grid;
        place-items: center;
        padding: 1rem;
        background: rgba(2, 8, 18, .8);
        backdrop-filter: blur(8px);
    }
    .detail-backdrop { position: absolute; inset: 0; cursor: default; }
    .detail-dialog {
        position: relative;
        z-index: 1;
        width: min(100%, 1100px);
        max-height: min(90vh, 960px);
        overflow: auto;
        padding: clamp(1.1rem, 2.5vw, 1.7rem);
        border: 1px solid rgba(123, 164, 198, .26);
        border-left: 3px solid var(--detail-accent, #45c8d1);
        border-radius: 20px;
        background:
            radial-gradient(ellipse at 0% 0%, color-mix(in srgb, var(--detail-accent, #45c8d1) 12%, transparent), transparent 28rem),
            linear-gradient(145deg, rgba(14, 29, 46, .96), rgba(9, 20, 33, .96));
        box-shadow: 0 24px 80px rgba(0, 0, 0, .56);
        animation: detail-pop 180ms ease-out;
    }
    @keyframes detail-pop {
        from { opacity: 0; transform: translateY(12px) scale(.985); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }
    .detail-close {
        position: absolute;
        top: 1rem;
        right: 1rem;
        z-index: 2;
        display: grid;
        place-items: center;
        width: 38px;
        height: 38px;
        border: 1px solid rgba(190, 220, 244, .32);
        border-radius: 11px;
        background: rgba(9, 24, 39, .68);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1);
        backdrop-filter: blur(14px);
        color: #dce8f2;
        font-size: 1.45rem;
        line-height: 1;
        text-decoration: none;
    }
    .detail-close:hover { background: rgba(54, 133, 159, .46); color: #d7fff8; }
    .detail-header { display: flex; align-items: flex-start; gap: 1rem; padding-right: 3rem; }
    .detail-icon {
        display: grid;
        place-items: center;
        flex: 0 0 54px;
        width: 54px;
        height: 54px;
        border: 1px solid color-mix(in srgb, var(--detail-accent, #45c8d1) 48%, transparent);
        border-radius: 16px;
        background: color-mix(in srgb, var(--detail-accent, #45c8d1) 18%, #0c1a2b);
        box-shadow: 0 8px 24px color-mix(in srgb, var(--detail-accent, #45c8d1) 18%, transparent);
        font-size: 1.8rem;
    }
    .detail-kicker {
        margin: .1rem 0 .25rem;
        color: var(--detail-accent, #45c8d1);
        font-size: .72rem;
        font-weight: 800;
        letter-spacing: .13em;
        text-transform: uppercase;
    }
    .detail-header h3 { margin: 0 0 .45rem; color: #f2f7fc; font-size: 1.28rem; }
    .detail-intro { max-width: 900px; margin: 0; color: #a4b7c9; line-height: 1.65; }
    .detail-body {
        display: grid;
        grid-template-columns: minmax(0, 1.4fr) minmax(270px, .9fr);
        align-items: start;
        gap: 1rem;
        margin-top: 1.15rem;
    }
    .detail-services-column, .detail-catalog-column { min-width: 0; }
    .detail-column-heading { margin: 0 0 .7rem; color: #e8f2fb; font-size: .96rem; }
    .detail-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: .8rem;
        margin-top: 1.15rem;
    }
    .detail-services-column .detail-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); margin-top: 0; }
    .detail-services-column .warranty-panels { grid-template-columns: 1fr; margin-top: 0; }
    .detail-item {
        min-width: 0;
        padding: .95rem;
        border: 1px solid rgba(120, 157, 190, .16);
        border-radius: 14px;
        background: rgba(5, 15, 27, .52);
    }
    .detail-item h4 {
        display: block;
        margin: 0 0 .45rem;
        color: #e8f2fb;
        font-size: .88rem;
        line-height: 1.45;
    }
    .detail-item p { margin: 0; color: #b0bfce; font-size: .85rem; line-height: 1.6; }
    .detail-tags { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1rem; }
    .detail-tag {
        padding: .38rem .65rem;
        border: 1px solid color-mix(in srgb, var(--detail-accent, #45c8d1) 25%, transparent);
        border-radius: 999px;
        background: color-mix(in srgb, var(--detail-accent, #45c8d1) 9%, #0b1828);
        color: #d3e2ef;
        font-size: .76rem;
    }
    .detail-notice {
        margin: 1rem 0 0;
        padding: .85rem 1rem;
        border: 1px solid rgba(245, 185, 95, .25);
        border-radius: 12px;
        background: rgba(245, 185, 95, .07);
        color: #e9c98f;
        font-size: .8rem;
        line-height: 1.6;
    }
    .modal-catalog {
        padding: .9rem;
        border: 1px solid rgba(123, 164, 198, .2);
        border-radius: 16px;
        background: rgba(5, 15, 27, .42);
    }
    .modal-catalog h4 { margin: 0 0 .7rem; color: #e8f2fb; font-size: .96rem; }
    .modal-catalog-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: .7rem;
        max-height: min(70vh, 680px);
        overflow-y: auto;
        overscroll-behavior: contain;
        padding-right: .25rem;
    }
    .modal-catalog-item {
        position: relative;
        display: flex;
        flex-direction: column;
        min-width: 0;
        overflow: hidden;
        border: 1px solid rgba(120, 157, 190, .18);
        border-radius: 13px;
        background: rgba(5, 15, 27, .58);
    }
    .catalog-zoom-toggle {
        position: absolute;
        width: 1px;
        height: 1px;
        overflow: hidden;
        clip-path: inset(50%);
        white-space: nowrap;
    }
    .modal-catalog-image {
        position: relative;
        display: grid;
        place-items: center;
        min-height: 260px;
        background: rgba(3, 10, 19, .45);
        cursor: zoom-in;
    }
    .modal-catalog-image img {
        display: block;
        max-width: 100%;
        max-height: 260px;
        width: auto;
        height: auto;
        object-fit: contain;
        transition: transform 180ms ease;
    }
    .modal-catalog-image:hover img { transform: scale(1.035); }
    .catalog-zoom-toggle:focus-visible + .modal-catalog-image { outline: 3px solid #78dfd0; outline-offset: -3px; }
    .catalog-zoom-hint {
        position: absolute;
        right: .65rem;
        bottom: .65rem;
        padding: .35rem .55rem;
        border: 1px solid rgba(255, 255, 255, .18);
        border-radius: 999px;
        background: rgba(3, 10, 19, .8);
        color: #e7f2fa;
        font-size: .7rem;
        font-weight: 800;
        pointer-events: none;
    }
    .modal-catalog-copy { padding: .8rem .9rem .9rem; }
    .modal-catalog-copy strong { display: block; color: #dce8f2; font-size: .88rem; line-height: 1.4; }
    .modal-catalog-copy p { margin: .3rem 0 0; color: #b0bfce; font-size: .84rem; line-height: 1.55; }
    .modal-image-zoom {
        display: none;
        position: fixed;
        inset: 0;
        z-index: 3;
        place-items: center;
        padding: 1rem;
        background: rgba(1, 6, 14, .94);
        backdrop-filter: blur(12px);
    }
    .modal-catalog-item:has(.catalog-zoom-toggle:checked) .modal-image-zoom { display: grid; }
    .modal-image-backdrop { position: absolute; inset: 0; cursor: zoom-out; }
    .modal-image-view {
        position: relative;
        z-index: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: min(96vw, 1400px);
        max-height: 92vh;
    }
    .modal-image-view img {
        display: block;
        max-width: 100%;
        max-height: 80vh;
        width: auto;
        height: auto;
        border: 1px solid rgba(163, 195, 220, .28);
        border-radius: 16px;
        object-fit: contain;
        box-shadow: 0 28px 90px rgba(0, 0, 0, .6);
    }
    .modal-image-view p { margin: .65rem 0 0; color: #eaf3fa; font-size: .9rem; font-weight: 800; text-align: center; }
    .modal-image-close {
        position: absolute;
        top: .65rem;
        right: .65rem;
        z-index: 2;
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border: 1px solid rgba(210, 233, 250, .4);
        border-radius: 12px;
        background: rgba(12, 27, 43, .68);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .14);
        backdrop-filter: blur(14px);
        color: #fff;
        cursor: pointer;
        font-size: 1.5rem;
        line-height: 1;
    }
    @media (prefers-reduced-motion: reduce) {
        .service-card, .service-card-link { transition: none; }
        .service-card:hover { transform: none; }
        .detail-dialog { animation: none; }
    }
    .warranty-panels {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 1.15rem;
    }
    .warranty-panel {
        min-width: 0;
        padding: 1.15rem;
        border: 1px solid rgba(148, 163, 184, .2);
        border-radius: 17px;
        background: linear-gradient(145deg, rgba(15, 23, 42, .94), rgba(8, 18, 31, .94));
    }
    .warranty-panel h4 { margin: 0 0 .85rem; color: #f0f6fc; font-size: .98rem; }
    .warranty-device-list, .warranty-service-list { padding: 0; margin: 0; list-style: none; }
    .warranty-device-list {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: .55rem;
    }
    .warranty-device-list li {
        display: flex;
        align-items: center;
        gap: .45rem;
        min-width: 0;
        padding: .6rem .65rem;
        border: 1px solid rgba(112, 204, 222, .14);
        border-radius: 11px;
        background: rgba(5, 15, 27, .58);
        color: #c5d5e4;
        font-size: .78rem;
    }
    .warranty-service-list { display: grid; gap: .55rem; }
    .warranty-service-list li {
        display: flex;
        align-items: flex-start;
        gap: .55rem;
        padding: .62rem .7rem;
        border: 1px solid rgba(112, 204, 222, .12);
        border-radius: 11px;
        background: rgba(5, 15, 27, .58);
    }
    .warranty-service-copy strong { display: block; color: #dce8f2; font-size: .82rem; line-height: 1.4; }
    .warranty-service-copy small { display: block; margin-top: .2rem; color: #b0bfce; font-size: .76rem; line-height: 1.55; }
    .detail-actions {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: .65rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(123, 164, 198, .18);
    }
    .detail-action {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: .4rem;
        min-height: 44px;
        padding: .6rem .8rem;
        border: 1px solid rgba(166, 222, 240, .3);
        border-radius: 11px;
        background: rgba(36, 66, 88, .4);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .16);
        backdrop-filter: blur(16px) saturate(145%);
        color: #c8dbea;
        font-size: .8rem;
        font-weight: 800;
        text-align: center;
        text-decoration: none;
        transition: background 150ms ease, border-color 150ms ease, transform 150ms ease;
    }
    .detail-action:hover { border-color: rgba(196, 247, 241, .72); background: rgba(35, 122, 135, .48); transform: translateY(-1px) scale(1.015); }
    .info-card { padding: 1.5rem; height: 100%; }
    .info-card h3 { color: #eff7ff; }
    .info-card p, .info-card li { color: #9dafc1; }
    .site-footer {
        margin-top: 2.5rem;
        padding: 1.6rem clamp(1rem, 2.5vw, 1.8rem) 1rem;
        border: 1px solid rgba(82, 147, 177, .28);
        border-radius: 22px;
        background:
            radial-gradient(ellipse at 0% 100%, rgba(12, 184, 155, 0.16), transparent 28rem),
            radial-gradient(ellipse at 100% 0%, rgba(104, 104, 255, .13), transparent 26rem),
            linear-gradient(135deg, #0d1b2b, #10182a 65%, #15182b);
        box-shadow: 0 -12px 50px rgba(15, 47, 74, .16);
    }
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        grid-auto-rows: 1fr;
        align-items: stretch;
        gap: 1rem;
    }
    .footer-grid > div {
        min-width: 0;
        padding: 1.1rem;
        border: 1px solid rgba(123, 164, 198, .18);
        border-radius: 15px;
        background: rgba(8, 20, 34, .34);
    }
    .footer-legal-grid {
        display: contents;
    }
    .footer-legal {
        display: none;
    }
    .footer-legal:target {
        position: fixed;
        inset: 0;
        z-index: 10000;
        display: grid;
        place-items: center;
        padding: 1rem;
        border: 0;
        border-radius: 0;
        background: rgba(2, 8, 18, .8);
        backdrop-filter: blur(7px);
    }
    .policy-backdrop { position: absolute; inset: 0; cursor: default; }
    .policy-dialog {
        position: relative;
        z-index: 1;
        width: min(100%, 720px);
        max-height: min(82vh, 760px);
        overflow: auto;
        padding: 1.6rem;
        border: 1px solid rgba(82, 147, 177, .42);
        border-radius: 20px;
        background: linear-gradient(145deg, #10243a, #081421 72%);
        box-shadow: 0 24px 80px rgba(0, 0, 0, .56);
    }
    .policy-dialog h4 { color: #e8f2fb; margin: 0 3rem .8rem 0; font-size: 1.2rem; }
    .policy-dialog p { color: #adbed0; margin: 0; font-size: .92rem; line-height: 1.75; }
    .policy-close {
        position: absolute;
        top: 1rem;
        right: 1rem;
        display: grid;
        place-items: center;
        width: 38px;
        height: 38px;
        border: 1px solid rgba(190, 220, 244, .32);
        border-radius: 11px;
        background: rgba(9, 24, 39, .68);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .1);
        backdrop-filter: blur(14px);
        color: #dce8f2;
        font-size: 1.45rem;
        line-height: 1;
        text-decoration: none;
    }
    .policy-close:hover { background: rgba(54, 133, 159, .46); color: #d7fff8; }
    .footer-brandline { display: flex; align-items: center; gap: .75rem; min-height: 42px; }
    .footer-mark {
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(135deg, #09b8a5, #47a8ff 55%, #9b7aff);
        color: #fff;
        font-size: 1.35rem;
        font-weight: 800;
    }
    .footer-title { color: #f2f7fc; font-weight: 800; letter-spacing: .04em; }
    .footer-brand-subtitle { color: #72caff; font-size: .68rem; font-weight: 700; letter-spacing: .13em; }
    .footer-copy { color: #b0bfce; font-size: .86rem; line-height: 1.6; margin: .8rem 0; }
    .footer-column h4 { color: #e8f2fb; font-size: .95rem; margin: .1rem 0 .8rem; }
    .footer-column h4:after {
        content: "";
        display: block;
        width: 34px;
        height: 2px;
        margin-top: .55rem;
        border-radius: 3px;
        background: linear-gradient(90deg, #35cbb6, #538dff);
    }
    .footer-column a, .footer-phone {
        display: block;
        width: 100%;
        color: #9dafc1;
        font-size: .82rem;
        line-height: 1.45;
        text-decoration: none;
        transition: color 150ms ease;
    }
    .footer-column > a:not(.policy-trigger) {
        min-height: 36px;
        margin: .3rem 0;
        padding: .5rem .65rem;
        border: 1px solid rgba(123, 164, 198, .16);
        border-radius: 9px;
        background: rgba(10, 25, 41, .42);
    }
    .footer-column a.policy-trigger {
        display: flex;
        align-items: center;
        width: 100%;
        min-height: 36px;
        margin: .3rem 0;
        padding: .45rem .65rem;
        border-radius: 9px;
        background: rgba(10, 25, 41, .42);
    }
    .footer-emoji { margin-right: .35rem; }
    .footer-column a:hover, .footer-phone:hover { color: #73ded0; }
    .footer-contact-card {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: .55rem;
        margin-top: .9rem;
        padding: .7rem;
        border: 1px solid rgba(48, 190, 166, .24);
        border-radius: 11px;
        background: rgba(9, 39, 45, .55);
    }
    .footer-contact-card .footer-phone { color: #75dfd0; font-weight: 800; }
    .footer-contact-card .footer-phone.whatsapp-cta,
    .footer-contact-card .footer-phone.call-cta {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: .45rem;
        width: 100%;
        min-height: 38px;
        margin: 0;
        padding: .4rem .5rem;
        border-radius: 9px;
        line-height: 1.4;
        text-align: center;
    }
    .footer-bottom {
        margin-top: 1.6rem;
        padding-top: 1rem;
        border-top: 1px solid #203247;
        color: #a5b4c3;
        font-size: .78rem;
    }
    .footer-policy-links {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        align-items: center;
        gap: .65rem;
    }
    .footer-meta {
        display: grid;
        grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);
        align-items: center;
        gap: 1rem;
        margin-top: .9rem;
    }
    .footer-copyright { white-space: nowrap; }
    .footer-security {
        justify-self: end;
        color: #83c7bd;
        text-align: right;
        white-space: nowrap;
    }
    .footer-version {
        justify-self: center;
        color: #8fa9bd;
        text-align: center;
        white-space: nowrap;
    }
    .footer-policy-links > a {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 36px;
        padding: .4rem .55rem;
        border: 1px solid rgba(89, 160, 188, .22);
        border-radius: 9px;
        background: rgba(11, 31, 49, .5);
        color: #8fa9bd;
        text-align: center;
        text-decoration: none;
    }
    .footer-policy-links > a:hover { color: #73ded0; }
    .policy-trigger {
        display: inline-flex;
        align-items: center;
        gap: .3rem;
        min-height: 34px;
        padding: .38rem .68rem;
        border: 1px solid rgba(89, 160, 188, .3);
        border-radius: 999px;
        background: rgba(11, 31, 49, .72);
        backdrop-filter: blur(12px);
        color: #b6ccdf !important;
        font-size: .76rem;
        font-weight: 700;
        line-height: 1.35 !important;
        text-decoration: none;
        transition: border-color 150ms ease, background 150ms ease, color 150ms ease, transform 150ms ease;
    }
    .policy-trigger:hover {
        border-color: rgba(71, 213, 192, .7);
        background: rgba(28, 91, 94, .42);
        color: #80e6d3 !important;
        transform: translateY(-1px);
    }
    @media (max-width: 1050px) {
        .footer-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .detail-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .service-card { flex-basis: calc(39% - 1rem); }
    }
    @container site-header (min-width: 961px) {
        .header-nav { grid-template-columns: repeat(8, max-content); }
        .mobile-menu { display: none; }
    }
    @container site-header (max-width: 960px) {
        .header-nav { display: none; }
        .mobile-menu { display: block; }
    }
    @container site-header (max-width: 700px) {
        .header-brand { flex: 1 1 auto; min-width: 0; }
        .header-action {
            width: 36px;
            height: 36px;
            min-height: 36px;
            padding: 0;
            font-size: 0;
            line-height: 1;
        }
        .header-action span { font-size: 1rem; }
    }
    @media (max-width: 1300px) {
        .site-header { flex-wrap: nowrap; gap: .85rem; }
    }
    @media (max-width: 700px) {
        .site-header { gap: .55rem; }
        .header-brand { flex: 1 1 auto; min-width: 0; }
        .header-call .header-action {
            width: 38px;
            height: 38px;
            min-height: 38px;
            padding: 0;
            font-size: 0;
            line-height: 1;
        }
        .header-call .header-action span { font-size: 1rem; }
    }
    @media (max-width: 760px) {
        .detail-body { grid-template-columns: 1fr; }
        .modal-catalog-grid {
            grid-template-columns: 1fr;
            max-height: none;
        }
        .modal-catalog-image {
            width: 100%;
            min-height: 200px;
        }
        .modal-catalog-image img {
            width: 100%;
            max-height: 260px;
            object-fit: contain;
        }
        .hero-overview { grid-template-columns: 1fr; gap: 1rem; }
        .footer-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .75rem; }
        .footer-grid > div { padding: .9rem; }
        .footer-policy-links { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .footer-meta { grid-template-columns: minmax(0, 1fr) auto; gap: .65rem; }
        .footer-security { grid-column: 1 / -1; }
        .site-header { padding: .75rem; }
        .policy-dialog { padding: 1.3rem; }
        .warranty-panels { grid-template-columns: 1fr; }
        .service-card { flex-basis: calc(50% - 1rem); height: 400px; }
        .section-heading .service-guide { border-radius: 14px; }
    }
    @media (max-width: 480px) {
        .footer-grid { grid-template-columns: 1fr; grid-auto-rows: auto; }
        .footer-policy-links { grid-template-columns: 1fr; }
        .footer-meta { grid-template-columns: 1fr; gap: .4rem; }
        .footer-copyright, .footer-security { font-size: .64rem; }
        .footer-version { justify-self: start; }
        .service-card { flex-basis: 84vw; height: 400px; }
        .service-card-image-link { flex-basis: 190px; height: 190px; }
        .service-card-image { width: 100%; height: 190px; object-fit: cover; object-position: center; }
        .topbar {
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            grid-template-rows: auto auto;
            align-items: center;
            justify-content: stretch;
            gap: .3rem .6rem;
            padding: .55rem .7rem;
        }
        .topbar-info { display: contents; }
        .topbar-phone { grid-column: 1; grid-row: 1; justify-self: start; white-space: nowrap; }
        .topbar-location { grid-column: 1 / -1; grid-row: 2; }
        .topbar > .header-action { grid-column: 2; grid-row: 1; justify-self: end; align-self: center; }
        .site-header { gap: .45rem; padding: .55rem .65rem; }
        .header-brand { min-width: 0; gap: .5rem; }
        .brand-mark { width: 40px; height: 40px; border-radius: 11px; }
        .brand-name { font-size: .78rem; white-space: nowrap; }
        .brand-location { font-size: .6rem; letter-spacing: .05em; }
        .header-actions { width: auto; gap: .25rem; }
        .header-call .header-action {
            width: 36px;
            height: 36px;
            min-height: 36px;
        }
        .mobile-menu summary { width: 36px; height: 36px; }
        .hero { padding: 2rem 1.1rem; }
        .hero::after { right: -13rem; }
        .detail-grid { grid-template-columns: 1fr; }
        .detail-header { gap: .75rem; }
        .detail-icon { flex-basis: 46px; width: 46px; height: 46px; font-size: 1.5rem; }
        .detail-group:target { padding: .5rem; }
        .detail-dialog { max-height: calc(100vh - 1rem); padding: 1rem; }
        .detail-header { padding-right: 2.6rem; }
    }
    div[data-testid="stButton"] > button,
    div[data-testid="stLinkButton"] > a {
        width: 100%;
        border-radius: 10px;
        min-height: 48px;
        font-weight: 800;
        border: 1px solid rgba(166, 222, 240, .38);
        background: rgba(20, 112, 150, .42);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, .22);
        backdrop-filter: blur(16px) saturate(150%);
        color: #fff;
        transition: transform 160ms ease, border-color 160ms ease, background 160ms ease, box-shadow 160ms ease;
    }
    div[data-testid="stButton"] > button:hover,
    div[data-testid="stLinkButton"] > a:hover {
        transform: translateY(-1px) scale(1.01);
        border-color: rgba(205, 248, 243, .72);
        background: rgba(27, 144, 153, .56);
        color: #fff;
        box-shadow: 0 8px 22px rgba(16, 158, 158, .22), inset 0 1px 0 rgba(255, 255, 255, .2);
    }
    div[data-testid="stButton"] > button[kind="primary"] {
        border-color: #25d366;
        background: #128c4a;
        color: #fff;
    }
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        border-color: #6be69a;
        background: #0f7a40;
        color: #fff;
    }
    .header-nav a:focus-visible,
    .mobile-menu summary:focus-visible,
    .mobile-menu-panel a:focus-visible,
    .header-action:focus-visible,
    .service-card-link:focus-visible,
    .footer-column a:focus-visible,
    .footer-bottom a:focus-visible,
    .policy-close:focus-visible,
    .detail-close:focus-visible {
        outline: 2px solid #78dfd0;
        outline-offset: 4px;
        border-radius: 4px;
    }
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background: #0a1725;
        color: #edf5fc;
        border-radius: 10px;
    }
    label[data-testid="stWidgetLabel"],
    label[data-testid="stWidgetLabel"] p {
        color: #e8f2fb !important;
        font-weight: 700 !important;
    }
    label[data-testid="stWidgetLabel"] p { text-shadow: 0 1px 2px rgba(0, 0, 0, .45); }
    hr { border-color: #192b3e; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.html(
    """
    <script>
    (() => {
        if (window.__hanvikaTidioControllerInitialized) return;
        window.__hanvikaTidioControllerInitialized = true;

        const isMobile = () => window.matchMedia("(max-width: 760px)").matches;
        let shownAtBottom = false;
        let lastScrollY = window.scrollY;
        let tidioReady = false;

        const updateMobileChatVisibility = () => {
            if (!tidioReady) {
                lastScrollY = window.scrollY;
                return;
            }

            const chat = window.tidioChatApi;
            if (!isMobile()) {
                chat.show();
                shownAtBottom = false;
                lastScrollY = window.scrollY;
                return;
            }

            const pageBottom = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
            const atBottom = pageBottom > 0 && window.scrollY >= pageBottom - 16;
            const scrollingDown = window.scrollY > lastScrollY + 4;
            const scrollingUp = window.scrollY < lastScrollY - 4;

            if (atBottom) {
                if (!shownAtBottom) {
                    chat.show();
                    shownAtBottom = true;
                }
            } else if (scrollingDown || scrollingUp || shownAtBottom) {
                chat.hide();
                shownAtBottom = false;
            }

            lastScrollY = window.scrollY;
        };
        window.addEventListener("scroll", updateMobileChatVisibility, { passive: true });
        window.addEventListener("resize", updateMobileChatVisibility);

        const onTidioReady = () => {
            const chat = window.tidioChatApi;
            if (!chat || typeof chat.show !== "function" || typeof chat.hide !== "function") {
                console.error("Tidio chat API was unavailable after the widget loaded.");
                return;
            }

            tidioReady = true;
            chat.show();
            updateMobileChatVisibility();
        };

        document.addEventListener("tidioChat-ready", onTidioReady, { once: true });
        const script = document.createElement("script");
        script.src = "https://code.tidio.co/dnp0ykgircft6qsxxacgwdjwoh8oky8u.js";
        script.async = true;
        script.onerror = () => console.error("Tidio live chat failed to load.");
        document.head.appendChild(script);
    })();
    </script>
    """,
    unsafe_allow_javascript=True,
)

st.markdown(
    f"""
    <div class="topbar">
        <div class="topbar-info">
            <a class="topbar-phone" href="tel:+{PHONE_LINK}">{CALL_ICON} {PHONE_DISPLAY}</a>
            <span class="topbar-location">{ADDRESS}</span>
        </div>
        <a class="header-action whatsapp whatsapp-cta" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer" aria-label="Open WhatsApp chat">{WHATSAPP_ICON}&nbsp; WhatsApp</a>
    </div>
    <header class="site-header">
        <a class="header-brand" href="#home" style="text-decoration:none">
            <span class="brand-mark">H</span>
            <span>
                <span class="brand-name">HANVIKA <span>IT SOLUTIONS</span></span>
                <span class="brand-location" style="display:block">GUNTUR, ANDHRA PRADESH</span>
            </span>
        </a>
        <nav class="header-nav" aria-label="Main navigation">
            <a href="#home">Home</a>
            <a href="#cyber-security-details">Security</a>
            <a href="#office-lan-details">LAN Setup</a>
            <a href="#network-amc-details">AMC</a>
            <a href="#antivirus-details">Antivirus</a>
            <a href="#hardware-warranty-details">Warranty</a>
            <a href="#os-server-details">OS &amp; Server</a>
            <a href="#advanced-connectivity-details">Networking</a>
        </nav>
        <div class="header-call">
            <a class="header-action call-cta" href="tel:+{PHONE_LINK}" aria-label="Call {PHONE_DISPLAY}">{CALL_ICON}&nbsp; Call</a>
        </div>
        <details class="mobile-menu">
            <summary aria-label="Toggle navigation" aria-controls="mobile-navigation">
                <span aria-hidden="true">☰</span>
            </summary>
            <nav class="mobile-menu-panel" id="mobile-navigation" aria-label="Mobile navigation">
                <a href="#home">Home</a>
                <a href="#cyber-security-details">Security</a>
                <a href="#office-lan-details">LAN Setup</a>
                <a href="#network-amc-details">AMC</a>
                <a href="#antivirus-details">Antivirus</a>
                <a href="#hardware-warranty-details">Warranty</a>
                <a href="#os-server-details">OS &amp; Server</a>
                <a href="#advanced-connectivity-details">Networking</a>
            </nav>
        </details>
    </header>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    f"""
    <div class="hero-overview">
        <div class="hero" id="home">
            <span class="eyebrow">Business IT Infrastructure in Guntur</span>
            <h1>Complete Networking, Cyber Security & <span class="accent">IT Infrastructure</span></h1>
            <p class="hero-copy">
                Looking for computer network or Wi-Fi setup, Tally and printer sharing, or local IT support?
                We provide professional office LAN, network AMC, firewall and antivirus, Windows/Linux server,
                and hardware support in Guntur and across Andhra Pradesh.
            </p>
        </div>
        <div class="status-card">
            <div class="status-header">
                <div class="status-brand">
                    <span class="status-light red" aria-hidden="true"></span>
                    <span class="status-light yellow" aria-hidden="true"></span>
                    <span class="status-light green" aria-hidden="true"></span>
                    <span class="status-label">hanvika-it-status</span>
                </div>
                <div class="status-header-actions" aria-label="Service availability">
                    <span class="online"><span class="online-dot" aria-hidden="true"></span>ONLINE</span>
                    <span class="onsite"><span class="onsite-dot" aria-hidden="true"></span>ON-SITE</span>
                </div>
            </div>
            <div class="status-rows">
                <a class="status-row" href="#cyber-security-details" aria-haspopup="dialog" aria-label="View Firewall and Cyber Security details and related catalog" style="--status-accent:#ff8b98">
                    <span class="status-icon" aria-hidden="true">🛡️</span>
                    <span class="status-copy"><strong>Firewall &amp; Cyber Security</strong><small>Fortinet, Sophos, IPS/IDS &amp; VPN</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                    <span class="status-link-indicator" aria-hidden="true">↗</span>
                </a>
                <a class="status-row" href="#office-lan-details" aria-haspopup="dialog" aria-label="View Office LAN and Tally Sharing details and related catalog" style="--status-accent:#63c8e8">
                    <span class="status-icon" aria-hidden="true">🖧</span>
                    <span class="status-copy"><strong>Office LAN &amp; Tally Sharing</strong><small>Centralized server &amp; multi-system setup</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                    <span class="status-link-indicator" aria-hidden="true">↗</span>
                </a>
                <a class="status-row" href="#os-server-details" aria-haspopup="dialog" aria-label="View Windows and Linux server details and related catalog" style="--status-accent:#67d6a5">
                    <span class="status-icon" aria-hidden="true">🖥️</span>
                    <span class="status-copy"><strong>Windows &amp; Linux OS/Servers</strong><small>Active Directory, DNS, Hyper-V &amp; Ubuntu</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                    <span class="status-link-indicator" aria-hidden="true">↗</span>
                </a>
                <a class="status-row" href="#advanced-connectivity-details" aria-haspopup="dialog" aria-label="View Mesh Wi-Fi and P2P networking details and related catalog" style="--status-accent:#f5bb60">
                    <span class="status-icon" aria-hidden="true">📶</span>
                    <span class="status-copy"><strong>Mesh Wi-Fi &amp; P2P Links</strong><small>Wireless links &amp; multi-WAN options</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                    <span class="status-link-indicator" aria-hidden="true">↗</span>
                </a>
                <a class="status-row" href="#offline-pc-assembly-details" aria-haspopup="dialog" aria-label="View Offline PC Assembly and Setup details and related catalog" style="--status-accent:#54c7e8">
                    <span class="status-icon" aria-hidden="true">🖥️</span>
                    <span class="status-copy"><strong>Offline: PC Assembly &amp; Setup</strong><small>On-site assembly and initial system setup</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                    <span class="status-link-indicator" aria-hidden="true">↗</span>
                </a>
                <a class="status-row" href="#offline-hardware-troubleshooting-details" aria-haspopup="dialog" aria-label="View Offline Hardware Troubleshooting details and related catalog" style="--status-accent:#f5b95f">
                    <span class="status-icon" aria-hidden="true">🔧</span>
                    <span class="status-copy"><strong>Offline: Hardware Troubleshooting</strong><small>On-site diagnosis and repair assistance</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                    <span class="status-link-indicator" aria-hidden="true">↗</span>
                </a>
            </div>
            <div class="status-footer">
                <p>Need immediate network setup or AMC support in Guntur?</p>
                <div class="status-actions">
                    <a class="status-action whatsapp whatsapp-cta" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">{WHATSAPP_ICON} WhatsApp</a>
                    <a class="status-action call call-cta" href="tel:+{PHONE_LINK}">{CALL_ICON} Call Engineer</a>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


service_catalog_images = {
    "cyber-security-details": ("45648.jpg",),
    "office-lan-details": ("6468.jpg",),
    "network-amc-details": ("2313.jpg",),
    "antivirus-details": ("8648.jpg",),
    "hardware-warranty-details": ("asd.jpg",),
    "os-server-details": ("wrwqr.jpg",),
    "advanced-connectivity-details": ("werewa.jpg",),
    "offline-pc-assembly-details": ("pca (1).jpeg", "pca (2).jpeg", "pca (3).jpeg"),
    "offline-hardware-troubleshooting-details": ("215.jpg",),
}

services = [
    ("Cyber Security", "Firewall, VPN, access rules and threat monitoring.", "#ff7c83", "cyber-security-details"),
    ("Office LAN", "Cabling, Wi-Fi, Tally, printer and file sharing.", "#54c7e8", "office-lan-details"),
    ("Network AMC", "Routine health checks, troubleshooting and maintenance.", "#a78bfa", "network-amc-details"),
    ("Antivirus", "Endpoint protection, malware cleanup and safer browsing.", "#f5b95f", "antivirus-details"),
    ("Windows & Linux", "Workstations, business servers and Linux support.", "#67d6a5", "os-server-details"),
    ("Advanced Connectivity", "Mesh Wi-Fi, P2P links, branch VPN and multi-WAN.", "#ff8fc9", "advanced-connectivity-details"),
    ("Hardware Warranty", "Registration, coverage checks and claim guidance.", "#67d6a5", "hardware-warranty-details"),
    ("PC Assembly & Setup", "On-site desktop assembly, parts installation, and initial setup.", "#54c7e8", "offline-pc-assembly-details"),
    ("Hardware Troubleshooting", "On-site diagnosis and repair assistance for PCs and office hardware.", "#f5b95f", "offline-hardware-troubleshooting-details"),
]

service_cards = "".join(
    f'<article class="service-card" style="--card-accent:{escape(color)}">'
    f'<a class="service-card-image-link" href="#{escape(detail_id, quote=True)}" aria-haspopup="dialog" '
    f'aria-label="View {escape(title, quote=True)} details and catalog">'
    f'<img class="service-card-image" src="{escape(catalog_image_url(service_catalog_images[detail_id][0]), quote=True)}" '
    f'alt="{escape(title, quote=True)}" loading="eager" decoding="async"></a>'
    f'<div class="service-card-content"><h3>{escape(title)}</h3><p>{escape(description)}</p>'
    f'<a class="service-card-link" href="#{escape(detail_id, quote=True)}" aria-haspopup="dialog" aria-label="View {escape(title, quote=True)} details">'
    f'<span>Learn more</span></a></div></article>'
    for title, description, color, detail_id in services
)

with st.container(key="services_section"):
    st.markdown(
        """
        <div class="section-heading" id="service-details">
            <span class="eyebrow">Our services</span>
            <h2>Complete IT services for your business</h2>
            <p class="service-guide">Cards move both ways automatically; hover, swipe, or use the mouse wheel to pause and browse.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="service-preview-grid" id="service-carousel-track" role="region" aria-label="IT services, scroll horizontally to browse" tabindex="0">{service_cards}</div>',
        unsafe_allow_html=True,
    )
    st.html(
        """
        <script>
        (() => {
            const initialize = () => {
                const track = document.getElementById("service-carousel-track");
                if (!track) return false;
                if (track.dataset.carouselReady) return true;

                const cards = Array.from(track.querySelectorAll(".service-card"));
                if (!cards.length) return false;

                const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
                let isVisible = false;
                let pointerOver = false;
                let focusWithin = false;
                let direction = 1;
                let autoplayTimer = null;
                let resumeTimer = null;

                const stopAutoplay = () => {
                    if (autoplayTimer !== null) {
                        clearInterval(autoplayTimer);
                        autoplayTimer = null;
                    }
                };
                const canAutoplay = () =>
                    isVisible &&
                    !pointerOver &&
                    !focusWithin &&
                    resumeTimer === null &&
                    !reducedMotion.matches &&
                    document.visibilityState === "visible";
                const updateAutoplay = () => {
                    if (!canAutoplay()) {
                        stopAutoplay();
                        return;
                    }
                    if (autoplayTimer !== null) return;

                    autoplayTimer = setInterval(() => {
                        const maxScroll = track.scrollWidth - track.clientWidth;
                        if (maxScroll <= 1) return;

                        const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
                        const step = cards[0].getBoundingClientRect().width + gap;
                        const nextPosition = track.scrollLeft + direction * step;
                        if (nextPosition >= maxScroll - 1) {
                            direction = -1;
                            track.scrollTo({ left: maxScroll, behavior: "smooth" });
                        } else if (nextPosition <= 1) {
                            direction = 1;
                            track.scrollTo({ left: 0, behavior: "smooth" });
                        } else {
                            track.scrollTo({ left: nextPosition, behavior: "smooth" });
                        }
                    }, 3500);
                };
                const pauseForInteraction = () => {
                    stopAutoplay();
                    if (resumeTimer !== null) clearTimeout(resumeTimer);
                    resumeTimer = setTimeout(() => {
                        resumeTimer = null;
                        updateAutoplay();
                    }, 6000);
                };

                track.addEventListener("wheel", event => {
                    pauseForInteraction();
                    if (Math.abs(event.deltaY) <= Math.abs(event.deltaX)) return;
                    const maxScroll = track.scrollWidth - track.clientWidth;
                    const canScroll = event.deltaY > 0
                        ? track.scrollLeft < maxScroll - 1
                        : track.scrollLeft > 1;
                    if (!canScroll) return;

                    event.preventDefault();
                    track.scrollBy({ left: event.deltaY, behavior: "auto" });
                }, { passive: false });
                track.addEventListener("pointerenter", () => {
                    pointerOver = true;
                    updateAutoplay();
                });
                track.addEventListener("pointerleave", () => {
                    pointerOver = false;
                    updateAutoplay();
                });
                track.addEventListener("pointerdown", pauseForInteraction);
                track.addEventListener("keydown", pauseForInteraction);
                track.addEventListener("focusin", () => {
                    focusWithin = true;
                    updateAutoplay();
                });
                track.addEventListener("focusout", event => {
                    if (!track.contains(event.relatedTarget)) {
                        focusWithin = false;
                        updateAutoplay();
                    }
                });
                document.addEventListener("visibilitychange", updateAutoplay);
                reducedMotion.addEventListener("change", updateAutoplay);

                const visibilityObserver = new IntersectionObserver(entries => {
                    isVisible = entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= 0.25);
                    updateAutoplay();
                }, { threshold: [0, 0.25] });
                visibilityObserver.observe(track);
                track.dataset.carouselReady = "true";
                return true;
            };

            if (!initialize()) {
                const observer = new MutationObserver(() => {
                    if (initialize()) observer.disconnect();
                });
                observer.observe(document.documentElement, { childList: true, subtree: true });
                setTimeout(() => observer.disconnect(), 5000);
            }
        })();
        </script>
        """,
        unsafe_allow_javascript=True,
    )

detailed_services = [
    {
        "id": "cyber-security-details",
        "icon": "🛡️",
        "category": "Cyber Security",
        "title": "Firewall & Network Security Services",
        "intro": "Security setup and support scoped to your office network, devices, and access requirements.",
        "color": "#ff7c83",
        "features": [
            ("🔥", "Hardware & Software Firewall Setup", "Fortinet, Sophos, Cisco, or native Windows/Linux firewall options configured for the site."),
            ("🚦", "Inbound & Outbound Rules", "Security rules and port-forwarding configured to match agreed operational policies."),
            ("🔐", "Remote Access & VPN", "Site-to-site and client-to-site VPN options for remote work and branch connectivity."),
            ("🕵️", "Threat & Intrusion Monitoring", "IPS/IDS deployment and configuration based on the environment and agreed scope."),
            ("📊", "Traffic Monitoring & Support", "Traffic analysis, periodic security reviews, maintenance, and device troubleshooting."),
        ],
    },
    {
        "id": "office-lan-details",
        "icon": "🖧",
        "category": "Office Infrastructure",
        "title": "Small Office LAN & Application Sharing",
        "intro": "Local network setup for small offices and commercial spaces, including workstations, shared resources, and business applications.",
        "color": "#54c7e8",
        "features": [
            ("💻", "Multi-System Connectivity", "Connect around 4–5 office workstations within a unified local network."),
            ("🖨️", "File & Printer Sharing", "Configure shared folders, printers, and access between office devices."),
            ("📊", "Tally & Business Applications", "Set up server-to-client access for Tally Prime and other business applications."),
            ("🧵", "Structured Cabling", "Plan office cabling and cable management for a maintainable network."),
            ("📶", "Router & Gigabit Switch Setup", "Install and configure Wi-Fi routers and gigabit switches to suit the site."),
            ("🗄️", "Central Storage & Permissions", "Configure shared storage and folder permissions for authorized users."),
            ("🧰", "Troubleshooting & Maintenance", "Support for common local network, printer, and connectivity issues."),
        ],
    },
    {
        "id": "network-amc-details",
        "icon": "🧰",
        "category": "Network Maintenance",
        "title": "Office Network AMC",
        "intro": "Annual maintenance options for routine checks, troubleshooting, and configuration support. Scope and response availability are confirmed in the service agreement.",
        "color": "#a78bfa",
        "features": [
            ("🩺", "Network Health Checks", "Routine diagnostics and review of connected network equipment."),
            ("🔀", "Router & Switch Maintenance", "Configuration review, performance tuning, and firmware update guidance."),
            ("📶", "Wi-Fi & LAN Troubleshooting", "Investigate connection drops, coverage issues, and speed problems."),
            ("🌐", "Internet & ISP Support", "Help troubleshoot ISP links and review redundant connection or failover options."),
            ("🖨️", "File & Printer Sharing", "Support shared printers, folders, and local storage access."),
            ("⚙️", "Network Configuration", "Assistance with IP settings, bandwidth allocation, and firewall parameters."),
            ("🗓️", "Preventive Maintenance", "Scheduled system reviews to identify maintenance needs."),
            ("🧑‍🔧", "On-Demand Technical Help", "Support for network disruptions and system issues, subject to agreed availability."),
        ],
    },
    {
        "id": "antivirus-details",
        "icon": "🔐",
        "category": "Antivirus & Endpoint Security",
        "title": "Antivirus & Internet Security Solutions",
        "intro": "Recommendations and setup can be tailored to the device usage and protection needs discussed with you.",
        "color": "#f5b95f",
        "features": [
            ("🦠", "Antivirus Protection", "Real-time system scanning, malware and virus removal, and USB drive protection."),
            ("🌍", "Internet Security", "Safe browsing, anti-phishing, payment protection options, and personal firewall features."),
            ("💾", "Total Security & Backup", "Options may include anti-ransomware tools, encryption, backup, recovery, and security optimization."),
        ],
    },
    {
        "id": "hardware-warranty-details",
        "icon": "🛠️",
        "category": "Warranty Support",
        "title": "IT Hardware Warranty Guidance",
        "intro": "Hanvika IT Solutions provides administrative guidance only for warranty registration, coverage information, documentation, and claim preparation.",
        "color": "#67d6a5",
        "features": [
            ("📝", "Registration Assistance", "Guidance with product warranty registration."),
            ("🔎", "Validity & Coverage Check", "Help review available warranty status and coverage information."),
            ("🧾", "Invoice & Serial Documentation", "Assistance organizing purchase and device details for a service request."),
            ("🎫", "Service Ticket Support", "Guidance with complaint and service-ticket registration."),
            ("🏢", "Service Center Guidance", "Help locate or contact the relevant manufacturer service channel."),
            ("✅", "Claim Preparation", "Precautions and best-practice guidance when preparing a claim."),
        ],
        "tags_title": "Supported devices",
        "tags": ["Laptops", "Inkjet printers", "Desktop PCs", "Laser printers", "All-in-One systems", "Scanners", "Monitors", "Multi-Function devices"],
        "notice": "Hanvika IT Solutions provides administrative guidance only. All warranty terms, coverage, and claim approvals are determined solely by the respective hardware manufacturers. Our services do not modify or conflict with official manufacturer policies.",
    },
    {
        "id": "offline-pc-assembly-details",
        "icon": "🖥️",
        "category": "Offline Services",
        "title": "PC Assembly & Setup",
        "intro": "On-site desktop and workstation assembly, parts installation, and initial system setup.",
        "color": "#54c7e8",
        "features": [
            ("🧩", "Custom PC Assembly", "Assembly of compatible components for office or personal desktop systems."),
            ("🔌", "Hardware Installation", "Installation and connection of drives, RAM, graphics cards, power supplies, and peripherals."),
            ("⚙️", "System Setup", "Basic BIOS, operating system, driver, and required software setup."),
            ("🧪", "Power-On & Hardware Check", "Post-assembly checks for normal startup, device recognition, and basic stability."),
        ],
    },
    {
        "id": "offline-hardware-troubleshooting-details",
        "icon": "🔧",
        "category": "Offline Services",
        "title": "Hardware Troubleshooting",
        "intro": "On-site diagnosis and practical repair assistance for desktops, laptops, printers, and office hardware.",
        "color": "#f5b95f",
        "features": [
            ("🔎", "Fault Diagnosis", "Initial inspection and diagnosis of startup, display, power, storage, and peripheral issues."),
            ("🧰", "Component-Level Assistance", "Help identify faulty parts and determine suitable repair or replacement options."),
            ("🖨️", "Peripheral Support", "Troubleshooting for printers, scanners, monitors, keyboards, and other local devices."),
            ("🧹", "Cleaning & Preventive Care", "Dust cleaning and basic preventive checks subject to device access and condition."),
        ],
    },
    {
        "id": "os-server-details",
        "icon": "🖥️",
        "category": "Operating Systems",
        "title": "Windows OS & Server Solutions",
        "intro": "Installation, configuration, security hardening, and support for desktop systems and business servers.",
        "color": "#54c7a5",
        "features": [
            ("🪟", "Windows Desktop (Home & Pro)", "Clean installs and upgrades · genuine licensing assistance · drivers and performance · RDP setup · user and privacy settings · crash troubleshooting."),
            ("🏢", "Windows Server (Standard & Datacenter)", "Server deployment · Active Directory, DNS, DHCP · file and print services · Hyper-V · GPO and RBAC · security hardening and maintenance."),
            ("🐧", "Linux Server Solutions", "Ubuntu, Debian, CentOS, and RHEL · Nginx/Apache · MySQL/PostgreSQL · mail and SSH · cron and shell scripts · backups and resource optimization."),
        ],
    },
    {
        "id": "advanced-connectivity-details",
        "icon": "📡",
        "category": "Enterprise Connectivity",
        "title": "Advanced Networking Solutions",
        "intro": "Network design and deployment options for homes, offices, retail, schools, hospitals, and multi-building sites.",
        "color": "#ff8fc9",
        "features": [
            ("📶", "Multi-Floor Mesh Wi-Fi", "Plan access-point coverage and a unified network name across floors."),
            ("📡", "Point-to-Point Wireless Links", "Wireless bridge options for connecting nearby buildings where suitable."),
            ("🔒", "Branch-to-Branch VPN", "Site-to-site VPN configuration options for connecting office locations."),
            ("⚖️", "Multi-WAN & Load Balancing", "Review multiple ISP connections, failover, and bandwidth distribution."),
            ("☁️", "Personal Cloud Storage", "On-premise storage options for remote access to files and business data."),
            ("🖥️", "Multi-User RDP Server", "Remote desktop server configuration options for multiple users."),
        ],
    },
]

catalog = [
   ("werewa.jpg", "📡", "Advanced Site Networking", "Headquarters LAN, branch VPN, P2P antennas and mesh Wi-Fi."),
   ("wrwqr.jpg", "🪟", "Windows OS Infrastructure", "Windows Server, hybrid security and workstation support."),
   ("asd.jpg", "🛠️", "Hardware Warranty Support", "Registration, validity checks and service ticket assistance."),
   ("2313.jpg", "🔧", "Office Network AMC", "On-site support, health checks and Tally data sharing."),
   ("45648.jpg", "🕵️", "Managed Security & Response", "Security monitoring, incident response and threat visibility."),
   ("6468.jpg", "🏢", "Small Office LAN & Data Sharing", "Office LAN, connected workstations and shared business data."),
   ("8648.jpg", "🛡️", "Antivirus & Internet Security", "Endpoint protection, safer browsing and online threat protection."),
   ("pca (1).jpeg", "🖥️", "Custom Gaming PC Build", "High-performance components, liquid cooling, and a multi-monitor setup."),
   ("pca (2).jpeg", "🧰", "PC Assembly Workbench", "PC component installation and assembly on an anti-static workbench."),
   ("pca (3).jpeg", "🎮", "Graphics Card Installation", "Graphics card alignment, installation, and power connection."),
   ("215.jpg", "🔧", "Hardware Troubleshooting", "On-site diagnosis and assistance for PCs and office hardware."),
]
catalog_by_image = {image: (image, icon, title, description) for image, icon, title, description in catalog}
detail_modals = []
for service in detailed_services:
    feature_markup = "".join(
        f'<article class="detail-item"><h4>{escape(title)}</h4><p>{escape(description)}</p></article>'
        for _, title, description in service["features"]
    )
    tags_markup = "".join(
        f'<span class="detail-tag">{escape(tag)}</span>'
        for tag in service.get("tags", [])
    )
    tags_section = (
        f'<div class="detail-tags" aria-label="{escape(service.get("tags_title", ""))}">{tags_markup}</div>'
        if tags_markup
        else ""
    )
    if service["id"] == "hardware-warranty-details":
        devices_markup = "".join(
            f'<li>{escape(tag)}</li>'
            for tag in service.get("tags", [])
        )
        services_markup = "".join(
            f'<li><span class="warranty-service-copy"><strong>{escape(title)}</strong><small>{escape(description)}</small></span></li>'
            for _, title, description in service["features"]
        )
        service_content = (
            f'<div class="warranty-panels">'
            f'<section class="warranty-panel"><h4>Supported devices</h4>'
            f'<ul class="warranty-device-list">{devices_markup}</ul></section>'
            f'<section class="warranty-panel"><h4>Support services</h4>'
            f'<ul class="warranty-service-list">{services_markup}</ul></section>'
            f'</div>'
        )
    else:
        service_content = f'<div class="detail-grid">{feature_markup}</div>{tags_section}'
    catalog_cards = []
    related_items = [
        catalog_by_image[image]
        for image in dict.fromkeys(service_catalog_images[service["id"]])
    ]
    for index, (image, icon, title, description) in enumerate(related_items):
        zoom_id = f"catalog-zoom-{service['id']}-{index}"
        zoom_id_html = escape(zoom_id, quote=True)
        image_url = escape(catalog_image_url(image), quote=True)
        image_title = escape(title, quote=True)
        zoom_overlay = (
            f'<div class="modal-image-zoom">'
            f'<label class="modal-image-backdrop" for="{zoom_id_html}" aria-label="Close enlarged image"></label>'
            f'<div class="modal-image-view">'
            f'<label class="modal-image-close" for="{zoom_id_html}" aria-label="Close enlarged image preview">×</label>'
            f'<img src="{image_url}" alt="{image_title}"><p>{escape(title)}</p>'
            f'</div></div>'
        )
        catalog_cards.append(
            f'<article class="modal-catalog-item">'
            f'<input class="catalog-zoom-toggle" id="{zoom_id_html}" type="checkbox" aria-label="Enlarge {image_title} image">'
            f'<label class="modal-catalog-image" for="{zoom_id_html}">'
            f'<img src="{image_url}" alt="{image_title}" loading="eager" decoding="async">'
            f'<span class="catalog-zoom-hint">Click to enlarge</span></label>'
            f'<div class="modal-catalog-copy"><strong>{escape(title)}</strong>'
            f'<p>{escape(description)}</p></div>{zoom_overlay}</article>'
        )
    catalog_markup = "".join(catalog_cards)
    related_catalog = (
        f'<div class="modal-catalog"><h4>Related catalog</h4>'
        f'<div class="modal-catalog-grid">{catalog_markup}</div></div>'
    )
    whatsapp_message = quote(
        f"Hello Hanvika IT Solutions, I am interested in {service['title']}. Please share more details."
    )
    whatsapp_url = f"{WHATSAPP_URL}?text={whatsapp_message}"
    contact_actions = (
        f'<div class="detail-actions">'
        f'<a class="detail-action whatsapp whatsapp-cta" href="{escape(whatsapp_url, quote=True)}" target="_blank" rel="noopener noreferrer">{WHATSAPP_ICON} WhatsApp about this service</a>'
        f'<a class="detail-action call call-cta" href="tel:+{PHONE_LINK}">{CALL_ICON} Call {PHONE_DISPLAY}</a>'
        f'</div>'
    )
    notice = (
        f'<p class="detail-notice">⚠️ {escape(service["notice"])}</p>'
        if service.get("notice")
        else ""
    )
    detail_modals.append(
        f'<section class="detail-group" id="{escape(service["id"])}" style="--detail-accent:{escape(service["color"])}">'
        f'<a class="detail-backdrop" href="#service-details" tabindex="-1" aria-hidden="true"></a>'
        f'<div class="detail-dialog" role="dialog" aria-label="{escape(service["title"])}">'
        f'<a class="detail-close" href="#service-details" aria-label="Close {escape(service["title"])} details">×</a>'
        f'<div class="detail-header"><span class="detail-icon" aria-hidden="true">{escape(service["icon"])}</span>'
        f'<div><p class="detail-kicker">{escape(service["category"])}</p>'
        f'<h3>{escape(service["title"])}</h3>'
        f'<p class="detail-intro">{escape(service["intro"])}</p></div></div>'
        f'<div class="detail-body">'
        f'<section class="detail-services-column"><h4 class="detail-column-heading">Service details</h4>'
        f'{service_content}{notice}{contact_actions}</section>'
        f'<aside class="detail-catalog-column" aria-label="Related catalog images">{related_catalog}</aside>'
        f'</div></div></section>'
    )

st.markdown("\n".join(detail_modals), unsafe_allow_html=True)

with st.container(key="estimator_section"):
    st.markdown(
        """
        <div class="section-heading">
            <span class="eyebrow">Cost estimator</span>
            <h2>Estimate your annual IT package</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    estimate_left, estimate_right = st.columns([1, 0.65], gap="large")
    with estimate_left:
        workstations = st.slider("🖥️ Number of workstations / PCs", 1, 100, 5)
        servers = st.slider("🗄️ Windows / Linux servers", 0, 10, 1)
        firewall = st.checkbox("🛡️ Fortinet / Sophos firewall")
        tally = st.checkbox("📊 Tally & printer data sharing")
        antivirus = st.checkbox("🔐 Total security antivirus licenses")
        vpn = st.checkbox("🌐 Branch VPN & remote RDP")

        estimate = 8500 + (workstations * 650) + (servers * 2400)
        estimate += 4200 if firewall else 0
        estimate += 1800 if tally else 0
        estimate += 900 if antivirus else 0
        estimate += 3500 if vpn else 0

    with estimate_right:
        st.markdown(
            f"""
            <div class="info-card">
                <span class="eyebrow">💰 Estimated package</span>
                <h2 style="font-size:2.6rem;margin:.8rem 0;color:#64b5ff">₹ {estimate:,.0f}</h2>
                <p>Estimated annual package. Final pricing depends on the site and equipment requirements.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    estimate_text = (
        f"Hello Hanvika IT Solutions, I need an IT service estimate. "
        f"Workstations: {workstations}, Servers: {servers}, "
        f"Firewall: {'Yes' if firewall else 'No'}, Tally sharing: {'Yes' if tally else 'No'}, "
        f"Antivirus: {'Yes' if antivirus else 'No'}, VPN/RDP: {'Yes' if vpn else 'No'}, "
        f"Estimated annual package: INR {estimate:,.0f}"
    )
    estimate_whatsapp_url = f"{WHATSAPP_URL}?text={quote(estimate_text)}"
    st.markdown(
        f'<a class="detail-action whatsapp whatsapp-cta" style="width:100%" href="{escape(estimate_whatsapp_url, quote=True)}" target="_blank" rel="noopener noreferrer">{WHATSAPP_ICON} Confirm Estimate via WhatsApp</a>',
        unsafe_allow_html=True,
    )

with st.container(key="contact_section"):
    st.markdown(
        """
        <div class="section-heading">
            <span class="eyebrow">Contact us</span>
            <h2>Send a service inquiry</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    contact_left, contact_right = st.columns([0.7, 1.3], gap="large")
    with contact_left:
        st.markdown(
            f"""
            <div class="info-card">
                <h3>Hanvika IT Solutions</h3>
                <p><b>📍 Address</b><br>{ADDRESS}</p>
                <p><b>{CALL_ICON} {WHATSAPP_ICON} Phone / WhatsApp</b><br>{PHONE_DISPLAY}</p>
                <p><b>🗺️ Service Region</b><br>Guntur and surrounding regions across Andhra Pradesh</p>
                <p><b>🕒 Support</b><br>Availability confirmed when you contact us</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with contact_right:
        name = st.text_input("👤 Your name", placeholder="e.g., Yashwardhan Kumar")
        phone = st.text_input("📱 Phone number", placeholder="e.g., +91 9XXXXXXXXX")
        required_service = st.selectbox(
            "🧰 Required service",
            [
                "🛡️ Cyber Security",
                "🖧 Office LAN",
                "🧰 Network AMC",
                "🔐 Antivirus",
                "🖥️ Windows / Linux Server",
                "📡 Advanced Networking",
                "🛠️ Hardware Warranty",
                "🧰 Offline Services",
                "🖥️ PC Assembly & Setup",
                "🔧 Hardware Troubleshooting",
            ],
        )
        details = st.text_area("📝 Details / message", height=130)
        st.caption(
            "Submitting prepares a WhatsApp link; your details are shared only if you choose to open it. "
            "Do not enter passwords or confidential network information."
        )

        if st.button("Send Inquiry on WhatsApp", type="primary", use_container_width=True):
            if not name or not phone:
                st.error("Please enter your name and phone number.")
            else:
                inquiry = (
                    f"Hello Hanvika IT Solutions, my name is {name}. "
                    f"My phone number is {phone}. I need {required_service}. "
                    f"Details: {details or 'Please contact me'}"
                )
                inquiry_whatsapp_url = f"{WHATSAPP_URL}?text={quote(inquiry)}"
                st.markdown(
                    f'<a class="detail-action whatsapp whatsapp-cta" href="{escape(inquiry_whatsapp_url, quote=True)}" target="_blank" rel="noopener noreferrer">{WHATSAPP_ICON} Open WhatsApp</a>',
                    unsafe_allow_html=True,
                )

st.markdown(
    f"""
    <footer class="site-footer">
        <div class="footer-grid">
            <div>
                <div class="footer-brandline">
                    <span class="footer-mark">H</span>
                    <span>
                        <span class="footer-title">HANVIKA IT SOLUTIONS</span>
                        <span class="footer-brand-subtitle" style="display:block">NETWORK · SECURITY · SERVERS</span>
                    </span>
                </div>
                <p class="footer-copy">
                    Complete Enterprise IT Infrastructure, Office LAN, Cyber Security
                    Firewalls, Server Solutions &amp; AMC Services in Guntur - 522002,
                    Andhra Pradesh.
                </p>
                <div class="footer-contact-card">
                    <a class="footer-phone call-cta" href="tel:+{PHONE_LINK}">{CALL_ICON} Call {PHONE_DISPLAY}</a>
                    <a class="footer-phone whatsapp whatsapp-cta" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">{WHATSAPP_ICON} Chat on WhatsApp ↗</a>
                </div>
            </div>
            <div class="footer-column">
                <h4>🧰 Core Services</h4>
                <a href="#cyber-security-details"><span class="footer-emoji" aria-hidden="true">🛡️</span>Firewall &amp; Security</a>
                <a href="#office-lan-details"><span class="footer-emoji" aria-hidden="true">🖧</span>Small Office LAN Setup</a>
                <a href="#network-amc-details"><span class="footer-emoji" aria-hidden="true">🔧</span>Office Network AMC</a>
                <a href="#antivirus-details"><span class="footer-emoji" aria-hidden="true">🔐</span>Antivirus Solutions</a>
                <a href="#os-server-details"><span class="footer-emoji" aria-hidden="true">🖥️</span>Windows &amp; Linux Server</a>
            </div>
            <div class="footer-column">
                <h4>🌐 Specialized Networking</h4>
                <a href="#advanced-connectivity-details"><span class="footer-emoji" aria-hidden="true">📶</span>Multi-Floor Mesh Wi-Fi</a>
                <a href="#advanced-connectivity-details"><span class="footer-emoji" aria-hidden="true">📡</span>P2P Wireless Links</a>
                <a href="#advanced-connectivity-details"><span class="footer-emoji" aria-hidden="true">🔒</span>Branch-to-Branch VPN</a>
                <a href="#advanced-connectivity-details"><span class="footer-emoji" aria-hidden="true">⚖️</span>Multi-WAN Load Balancing</a>
                <a href="#hardware-warranty-details"><span class="footer-emoji" aria-hidden="true">🛠️</span>Hardware Warranty Guidance</a>
            </div>
            <div class="footer-column">
                <h4>🏢 Hanvika IT Solutions</h4>
                <p class="footer-copy">
                    Professional networking, firewall security, and hardware technical
                    guidance across Guntur, Andhra Pradesh.
                </p>
                <a href="#send-a-service-inquiry"><span class="footer-emoji" aria-hidden="true">✉️</span>Send a service inquiry →</a>
            </div>
        </div>
        <div class="footer-legal-grid">
            <section class="footer-legal" id="privacy-policy-details" aria-labelledby="privacy-policy-title">
                <a class="policy-backdrop" href="#legal-notices" tabindex="-1" aria-hidden="true"></a>
                <div class="policy-dialog" role="dialog" aria-labelledby="privacy-policy-title">
                    <a class="policy-close" href="#legal-notices" aria-label="Close Privacy Policy">×</a>
                    <h4 id="privacy-policy-title">🔒 Privacy Policy</h4>
                    <p><strong>Effective date:</strong> November 27, 2026.</p>
                    <p>
                        This website is for advertising and showcasing Hanvika IT Solutions services. It has no database
                        and does not use analytics or advertising trackers. Inquiry form details are used in your
                        browser to prepare a WhatsApp message; nothing is sent to Hanvika IT Solutions unless you choose
                        to contact us directly. The Tidio chat widget loads when this page opens and may process page,
                        device, and chat data under its
                        <a href="https://www.tidio.com/privacy-policy/" target="_blank" rel="noopener noreferrer">Privacy Policy</a>.
                    </p>
                    <p>
                        If you voluntarily contact us by WhatsApp or email, we use your message only to reply to your
                        inquiry and permanently delete the message or email within 30 days. This deletion period does
                        not cover chat data processed by Tidio, which is subject to Tidio's policies. To ask a privacy
                        question or request earlier deletion of information we hold, contact us at [Insert Your Email Here].
                    </p>
                    <p>
                        The hosting provider may create standard access logs and automatically purges them under its
                        retention practices. The page requests fonts from Google Fonts and displays images hosted on
                        GitHub Pages; these providers may receive standard connection data. Google Fonts and GitHub
                        Pages assets are used only to display this website. WhatsApp and phone icons use Font Awesome
                        Free 6.7.2 by Fonticons, Inc., under the
                        <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0 license</a>;
                        see <a href="https://fontawesome.com/license/free" target="_blank" rel="noopener noreferrer">Font Awesome Free</a>.
                    </p>
                    <p>Please do not send passwords, access keys, or other sensitive information.</p>
                </div>
            </section>
            <section class="footer-legal" id="terms-conditions-details" aria-labelledby="terms-conditions-title">
                <a class="policy-backdrop" href="#legal-notices" tabindex="-1" aria-hidden="true"></a>
                <div class="policy-dialog" role="dialog" aria-labelledby="terms-conditions-title">
                    <a class="policy-close" href="#legal-notices" aria-label="Close Terms &amp; Conditions">×</a>
                    <h4 id="terms-conditions-title">📄 Terms &amp; Conditions</h4>
                    <p><strong>Effective date:</strong> November 27, 2026.</p>
                    <p>
                        This website is strictly for advertising and showcasing Hanvika IT Solutions services. Website
                        content, displayed details, and estimates are informational only and are not binding offers or
                        quotations. Final pricing and a quotation are confirmed only after direct contact and discussion,
                        and may be documented in a written quote, invoice, or service agreement. Service availability,
                        scope, deliverables, and schedule are confirmed directly with the customer.
                    </p>
                    <p>
                        Customers must have authorization for any systems they ask us to access. Third-party software,
                        hardware, and external links remain subject to their respective providers' terms. These terms
                        do not limit rights provided by applicable law.
                    </p>
                </div>
            </section>
            <section class="footer-legal" id="refund-policy-details" aria-labelledby="refund-policy-title">
                <a class="policy-backdrop" href="#legal-notices" tabindex="-1" aria-hidden="true"></a>
                <div class="policy-dialog" role="dialog" aria-labelledby="refund-policy-title">
                    <a class="policy-close" href="#legal-notices" aria-label="Close Refund Policy">×</a>
                    <h4 id="refund-policy-title">↩️ Refund Policy</h4>
                    <p>
                        No payments are processed on this website. Any cancellation or refund request is handled
                        directly under the applicable written quote or invoice and applicable law. Please contact
                        Hanvika IT Solutions to discuss a request. Nothing in this notice limits any rights that
                        cannot be excluded under applicable law.
                    </p>
                </div>
            </section>
            <section class="footer-legal" id="security-disclaimer-details" aria-labelledby="security-disclaimer-title">
                <a class="policy-backdrop" href="#legal-notices" tabindex="-1" aria-hidden="true"></a>
                <div class="policy-dialog" role="dialog" aria-labelledby="security-disclaimer-title">
                    <a class="policy-close" href="#legal-notices" aria-label="Close Security Disclaimer">×</a>
                    <h4 id="security-disclaimer-title">🛡️ Security Disclaimer</h4>
                    <p>
                        Service descriptions and estimates are informational; scope and final pricing require
                        confirmation. Security services depend on the environment and agreed scope, and cannot
                        guarantee prevention of every threat or outage. Do not share confidential network details
                        through this public form; request a suitable private channel for sensitive discussions.
                    </p>
                </div>
            </section>
        </div>
        <div class="footer-bottom" id="legal-notices">
            <div class="footer-policy-links">
                <a class="policy-trigger" href="#privacy-policy-details">🔒 Privacy Policy</a>
                <a class="policy-trigger" href="#terms-conditions-details">📄 Terms &amp; Conditions</a>
                <a class="policy-trigger" href="#refund-policy-details">↩️ Refund Policy</a>
                <a class="policy-trigger" href="#security-disclaimer-details">🛡️ Security Disclaimer</a>
                <a href="#home">🏠 Back to top ↑</a>
            </div>
            <div class="footer-meta">
                <span class="footer-copyright">© {COPYRIGHT_YEAR} Hanvika IT Solutions. All rights reserved.</span>
                <span class="footer-version">Version {APP_VERSION}</span>
                <span class="footer-security">🔒 Click a notice to review our privacy and security details.</span>
            </div>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
