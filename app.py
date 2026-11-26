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


st.set_page_config(
    page_title="Hanvika IT Solutions",
    page_icon="H",
    layout="wide",
    initial_sidebar_state="collapsed",
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
            radial-gradient(ellipse at 5% 0%, rgba(35, 122, 224, 0.18), transparent 34rem),
            linear-gradient(135deg, #0d1b31, #10182b 58%, #13182c);
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
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"] { display: none; }

    .topbar {
        display: flex;
        justify-content: center;
        gap: 1rem;
        padding: 0.55rem 1rem;
        border: 1px solid rgba(52, 177, 174, 0.26);
        border-radius: 14px 14px 0 0;
        background: linear-gradient(90deg, rgba(10, 112, 111, 0.30), rgba(17, 44, 75, 0.72), rgba(81, 57, 123, 0.25));
        color: #c4d5e5;
        font-size: 0.8rem;
        text-align: center;
    }
    .topbar a { color: #78dfd0; font-weight: 800; text-decoration: none; }
    .site-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.25rem;
        padding: .95rem 1.2rem;
        border: 1px solid #1c3046;
        border-top: 0;
        border-radius: 0 0 18px 18px;
        background: rgba(10, 22, 38, .92);
        box-shadow: 0 15px 40px rgba(0, 0, 0, .16);
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
    .brand-location { margin-top: .2rem; color: #8da1b5; font-size: .68rem; letter-spacing: .11em; }
    .header-nav { display: flex; align-items: center; justify-content: center; gap: clamp(.35rem, .75vw, .8rem); }
    .header-nav a {
        color: #adbed0;
        font-size: .72rem;
        font-weight: 700;
        text-decoration: none;
        white-space: nowrap;
        transition: color 150ms ease;
    }
    .header-nav a:hover { color: #79ded1; }
    .nav-emoji { margin-right: .18rem; font-size: .82rem; }
    .header-actions { display: flex; align-items: center; gap: .55rem; }
    .mobile-menu { display: none; position: relative; z-index: 60; }
    .mobile-menu summary {
        display: grid;
        place-items: center;
        width: 42px;
        height: 42px;
        border: 1px solid #2b465e;
        border-radius: 11px;
        background: rgba(17, 36, 57, .92);
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
        border: 1px solid #263d55;
        border-radius: 16px;
        background: rgba(8, 20, 35, .98);
        box-shadow: 0 18px 42px rgba(0, 0, 0, .4);
        backdrop-filter: blur(16px);
    }
    .mobile-menu-panel a {
        display: flex;
        align-items: center;
        gap: .65rem;
        padding: .68rem .75rem;
        border-radius: 10px;
        color: #c4d5e5;
        font-size: .88rem;
        font-weight: 700;
        text-decoration: none;
    }
    .mobile-menu-panel a:hover { background: rgba(54, 133, 159, .18); color: #7fe6d2; }
    .header-action {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 40px;
        padding: .55rem .85rem;
        border: 1px solid #277f91;
        border-radius: 11px;
        background: linear-gradient(110deg, #087f82, #147fc1);
        color: #fff !important;
        font-size: .8rem;
        font-weight: 800;
        text-decoration: none;
        white-space: nowrap;
        transition: 180ms ease;
    }
    .header-action.whatsapp {
        border-color: rgba(49, 201, 140, .42);
        background: linear-gradient(110deg, #087e65, #0b9a78);
    }
    .header-action:hover { transform: translateY(-2px); filter: brightness(1.13); }
    .hero {
        position: relative;
        isolation: isolate;
        margin-top: 1.1rem;
        padding: 4.2rem 3.5rem;
        border: 1px solid #1b3048;
        border-radius: 28px;
        background:
            radial-gradient(circle at 85% 15%, rgba(41, 137, 255, 0.24), transparent 28rem),
            radial-gradient(circle at 15% 100%, rgba(12, 184, 155, 0.15), transparent 24rem),
            radial-gradient(circle at 100% 100%, rgba(161, 98, 255, 0.12), transparent 22rem),
            linear-gradient(145deg, #0c1a2b, #091525);
        overflow: hidden;
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
        margin: 1.2rem 0 1rem;
        color: #f7fbff;
        font-size: clamp(2.4rem, 5vw, 4.8rem);
        line-height: 1.02;
        letter-spacing: -0.055em;
    }
    .accent {
        color: #76c9ff;
        background: linear-gradient(90deg, #70d7cf, #72baff 55%, #b39aff);
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-copy {
        max-width: 730px;
        color: #b2c1d1;
        font-size: 1.05rem;
        line-height: 1.75;
    }
    .status-card, .service-card, .info-card {
        border: 1px solid #1c3046;
        border-radius: 18px;
        background: linear-gradient(145deg, #0e1d2e, #0a1725);
    }
    .status-card {
        padding: 1.15rem;
        border-color: #263d55;
        background:
            radial-gradient(ellipse at 100% 0%, rgba(35, 182, 170, .1), transparent 22rem),
            linear-gradient(145deg, #0e1d2e, #091522);
        box-shadow: 0 22px 54px rgba(0, 0, 0, .24);
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
    .status-rows { display: grid; gap: .58rem; padding: .9rem 0; }
    .status-row {
        display: flex;
        align-items: center;
        gap: .65rem;
        min-width: 0;
        padding: .65rem .7rem;
        border: 1px solid rgba(123, 164, 198, .14);
        border-radius: 13px;
        background: rgba(5, 15, 27, .58);
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
    .status-copy small { display: block; margin-top: .13rem; color: #90a5ba; font-size: .7rem; line-height: 1.4; }
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
        min-height: 38px;
        padding: .45rem .55rem;
        border: 1px solid rgba(120, 223, 208, .28);
        border-radius: 10px;
        color: #b7eee5;
        font-size: .72rem;
        font-weight: 800;
        text-decoration: none;
        transition: background 150ms ease, border-color 150ms ease, transform 150ms ease;
    }
    .status-action.whatsapp { border-color: rgba(82, 213, 154, .34); background: rgba(82, 213, 154, .1); }
    .status-action.call { background: rgba(44, 153, 191, .12); }
    .status-action:hover { border-color: #78dfd0; background: rgba(35, 122, 135, .3); transform: translateY(-1px); }
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
    .section-heading {
        text-align: center;
        margin: 4.5rem 0 2rem;
    }
    .section-heading h2 {
        color: #f4f8fc;
        font-size: 2.35rem;
        letter-spacing: -0.04em;
        margin: 0.6rem 0;
    }
    .section-heading p {
        max-width: 700px;
        margin: auto;
        color: #91a4b8;
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
        color: #aee4d9;
        font-size: .82rem;
        line-height: 1.45;
    }
    .service-card {
        display: flex;
        min-height: 0;
        height: 100%;
        flex-direction: column;
        padding: 1.35rem;
        border: 1px solid rgba(123, 164, 198, .18);
        border-top: 2px solid var(--card-accent, #35b8c2);
        border-radius: 17px;
        background:
            linear-gradient(145deg, color-mix(in srgb, var(--card-accent, #35b8c2) 8%, #0e1d2e), #0a1725 74%);
        transition: border-color 160ms ease, transform 160ms ease, box-shadow 160ms ease;
    }
    .service-card:hover {
        border-color: color-mix(in srgb, var(--card-accent, #35b8c2) 48%, #31506a);
        box-shadow: 0 14px 32px rgba(0, 0, 0, .2);
        transform: translateY(-3px);
    }
    .service-preview-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        align-items: stretch;
        gap: 1rem;
    }
    .service-icon {
        display: grid;
        place-items: center;
        width: 58px;
        height: 58px;
        margin-bottom: 1rem;
        border: 1px solid color-mix(in srgb, var(--card-accent, #35b8c2) 58%, #fff);
        border-radius: 17px;
        background:
            radial-gradient(circle at 28% 18%, color-mix(in srgb, var(--card-accent, #35b8c2) 42%, #fff), transparent 68%),
            linear-gradient(145deg, color-mix(in srgb, var(--card-accent, #35b8c2) 34%, #0e1d2e), #111b30);
        box-shadow:
            0 10px 26px color-mix(in srgb, var(--card-accent, #35b8c2) 34%, transparent),
            inset 0 1px 0 rgba(255, 255, 255, .18);
        font-size: 2rem;
        text-shadow: 0 2px 12px color-mix(in srgb, var(--card-accent, #35b8c2) 55%, transparent);
        transition: transform 180ms ease, box-shadow 180ms ease;
    }
    .service-card:hover .service-icon {
        transform: translateY(-3px) scale(1.06);
        box-shadow:
            0 14px 32px color-mix(in srgb, var(--card-accent, #35b8c2) 44%, transparent),
            inset 0 1px 0 rgba(255, 255, 255, .22);
    }
    @media (prefers-reduced-motion: reduce) {
        .service-icon { transition: none; }
        .service-card:hover .service-icon { transform: none; }
    }
    .service-card h3 { margin: .15rem 0 .45rem; color: var(--card-accent, #eef6ff); font-size: 1.05rem; }
    .service-card p { flex: 1; margin: 0 0 .9rem; color: #94a7ba; line-height: 1.55; font-size: .84rem; }
    .service-card-link {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: .5rem;
        width: 100%;
        min-height: 42px;
        margin-top: auto;
        padding: .55rem .75rem;
        border: 1px solid color-mix(in srgb, var(--card-accent, #35b8c2) 32%, transparent);
        border-radius: 11px;
        background: color-mix(in srgb, var(--card-accent, #35b8c2) 9%, #0b1828);
        color: var(--card-accent, #7bded1);
        font-size: .8rem;
        font-weight: 800;
        text-decoration: none;
        transition: border-color 150ms ease, background 150ms ease, transform 150ms ease;
    }
    .service-card-link:hover {
        border-color: color-mix(in srgb, var(--card-accent, #35b8c2) 65%, transparent);
        background: color-mix(in srgb, var(--card-accent, #35b8c2) 17%, #0b1828);
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
        border: 1px solid #35516a;
        border-radius: 11px;
        background: rgba(9, 24, 39, .9);
        color: #dce8f2;
        font-size: 1.45rem;
        line-height: 1;
        text-decoration: none;
    }
    .detail-close:hover { background: rgba(54, 133, 159, .2); color: #7fe6d2; }
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
    .detail-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: .8rem;
        margin-top: 1.15rem;
    }
    .detail-item {
        min-width: 0;
        padding: .95rem;
        border: 1px solid rgba(120, 157, 190, .16);
        border-radius: 14px;
        background: rgba(5, 15, 27, .52);
    }
    .detail-item h4 {
        display: flex;
        align-items: flex-start;
        gap: .45rem;
        margin: 0 0 .45rem;
        color: #e8f2fb;
        font-size: .88rem;
        line-height: 1.45;
    }
    .detail-item p { margin: 0; color: #96aabd; font-size: .81rem; line-height: 1.6; }
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
        margin-top: 1.1rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(123, 164, 198, .18);
    }
    .modal-catalog h4 { margin: 0 0 .7rem; color: #e8f2fb; font-size: .96rem; }
    .modal-catalog-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: .85rem;
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
        min-height: 210px;
        background: rgba(3, 10, 19, .45);
        cursor: zoom-in;
    }
    .modal-catalog-image img {
        display: block;
        max-width: 100%;
        max-height: 300px;
        width: auto;
        height: auto;
        object-fit: contain;
    }
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
    .modal-catalog-copy p { margin: .3rem 0 0; color: #a4b7c9; font-size: .78rem; line-height: 1.5; }
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
        border: 1px solid rgba(255, 255, 255, .32);
        border-radius: 12px;
        background: rgba(3, 10, 19, .82);
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
    .warranty-service-copy strong { display: block; color: #dce8f2; font-size: .78rem; line-height: 1.4; }
    .warranty-service-copy small { display: block; margin-top: .2rem; color: #96aabd; font-size: .72rem; line-height: 1.5; }
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
        border: 1px solid rgba(120, 223, 208, .28);
        border-radius: 11px;
        color: #c8dbea;
        font-size: .8rem;
        font-weight: 800;
        text-align: center;
        text-decoration: none;
        transition: background 150ms ease, border-color 150ms ease, transform 150ms ease;
    }
    .detail-action.whatsapp { border-color: rgba(82, 213, 154, .36); background: rgba(82, 213, 154, .1); color: #8ce2b5; }
    .detail-action.call { background: rgba(44, 153, 191, .13); color: #9cdbef; }
    .detail-action:hover { border-color: #78dfd0; background: rgba(35, 122, 135, .3); transform: translateY(-1px); }
    .info-card { padding: 1.5rem; height: 100%; }
    .info-card h3 { color: #eff7ff; }
    .info-card p, .info-card li { color: #9dafc1; }
    .site-footer {
        margin-top: 2.5rem;
        padding: 2.3rem clamp(1.25rem, 3vw, 2.5rem) 1.2rem;
        border: 1px solid rgba(82, 147, 177, .28);
        border-radius: 26px;
        background:
            radial-gradient(ellipse at 0% 100%, rgba(12, 184, 155, 0.16), transparent 28rem),
            radial-gradient(ellipse at 100% 0%, rgba(104, 104, 255, .13), transparent 26rem),
            linear-gradient(135deg, #0d1b2b, #10182a 65%, #15182b);
        box-shadow: 0 -12px 50px rgba(15, 47, 74, .16);
    }
    .footer-grid {
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr 1.35fr;
        gap: 2rem;
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
        border: 1px solid #35516a;
        border-radius: 11px;
        color: #dce8f2;
        font-size: 1.45rem;
        line-height: 1;
        text-decoration: none;
    }
    .policy-close:hover { background: rgba(54, 133, 159, .2); color: #7fe6d2; }
    body:has(.detail-group:target) #tidio-chat,
    body:has(.footer-legal:target) #tidio-chat { display: none !important; }
    .footer-brandline { display: flex; align-items: center; gap: .75rem; }
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
    .footer-copy { color: #9dafc1; font-size: .88rem; line-height: 1.7; margin: .9rem 0; }
    .footer-column h4 { color: #e8f2fb; font-size: .95rem; margin: .15rem 0 .85rem; }
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
        width: fit-content;
        color: #9dafc1;
        font-size: .86rem;
        line-height: 1.9;
        text-decoration: none;
        transition: color 150ms ease;
    }
    .footer-emoji { margin-right: .35rem; }
    .footer-column a:hover, .footer-phone:hover { color: #73ded0; }
    .footer-contact-card {
        margin-top: .9rem;
        padding: .9rem 1rem;
        border: 1px solid rgba(48, 190, 166, .24);
        border-radius: 14px;
        background: rgba(9, 39, 45, .55);
    }
    .footer-contact-card .footer-phone { color: #75dfd0; font-weight: 800; }
    .footer-bottom {
        margin-top: 1.6rem;
        padding-top: 1.1rem;
        border-top: 1px solid #203247;
        color: #71869b;
        font-size: .78rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }
    .footer-security { color: #83c7bd; }
    .footer-version { color: #8fa9bd; white-space: nowrap; }
    .footer-bottom a { color: #8fa9bd; text-decoration: none; }
    .footer-bottom a:hover { color: #73ded0; }
    .policy-trigger {
        display: inline-flex;
        align-items: center;
        gap: .3rem;
        min-height: 34px;
        padding: .38rem .68rem;
        border: 1px solid rgba(89, 160, 188, .3);
        border-radius: 999px;
        background: rgba(11, 31, 49, .72);
        color: #b6ccdf !important;
        font-size: .76rem;
        font-weight: 700;
        line-height: 1.35 !important;
        text-decoration: none;
        transition: border-color 150ms ease, background 150ms ease, color 150ms ease, transform 150ms ease;
    }
    .footer-column a.policy-trigger { margin: .25rem 0; }
    .policy-trigger:hover {
        border-color: rgba(71, 213, 192, .7);
        background: rgba(28, 91, 94, .42);
        color: #80e6d3 !important;
        transform: translateY(-1px);
    }
    @media (max-width: 1050px) {
        .footer-grid { grid-template-columns: 1.2fr 1fr 1fr; }
        .footer-grid > :last-child { grid-column: 1 / -1; }
        .detail-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .service-preview-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    }
    @media (max-width: 1100px) {
        .site-header { flex-wrap: nowrap; gap: .85rem; }
        .header-nav { display: none; }
        .mobile-menu { display: block; }
    }
    @media (max-width: 760px) {
        div[data-testid="stHorizontalBlock"]:has(.hero, .status-card) {
            flex-direction: column;
            gap: 1rem;
        }
        div[data-testid="stHorizontalBlock"]:has(.hero, .status-card) > div[data-testid="stColumn"] {
            width: 100% !important;
            max-width: 100% !important;
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }
        .footer-grid { grid-template-columns: 1fr 1fr; gap: 1.5rem; }
        .site-header { padding: .75rem; }
        .policy-dialog { padding: 1.3rem; }
        .warranty-panels { grid-template-columns: 1fr; }
        .service-preview-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .section-heading .service-guide { border-radius: 14px; }
    }
    @media (max-width: 480px) {
        .footer-grid { grid-template-columns: 1fr; }
        .footer-grid > :last-child { grid-column: auto; }
        .topbar { flex-direction: column; gap: .25rem; }
        .site-header { gap: .45rem; padding: .55rem .65rem; }
        .header-brand { min-width: 0; gap: .5rem; }
        .brand-mark { width: 40px; height: 40px; border-radius: 11px; }
        .brand-name { font-size: .78rem; white-space: nowrap; }
        .brand-location { font-size: .53rem; letter-spacing: .07em; }
        .header-actions { width: auto; gap: .35rem; }
        .header-action { min-height: 36px; padding: .4rem .5rem; font-size: .7rem; }
        .header-action.whatsapp { display: none; }
        .mobile-menu summary { width: 36px; height: 36px; }
        .footer-bottom { flex-direction: column; }
        .hero { padding: 3rem 1.4rem; }
        .hero::after { right: -13rem; }
        .detail-grid { grid-template-columns: 1fr; }
        .service-preview-grid { grid-template-columns: 1fr; }
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
        border: 1px solid #2c9b9b;
        background: linear-gradient(110deg, #087f82, #147fc1);
        color: #fff;
        transition: 180ms ease;
    }
    div[data-testid="stButton"] > button:hover,
    div[data-testid="stLinkButton"] > a:hover {
        border-color: #76d9cb;
        background: linear-gradient(110deg, #0b9a91, #258fd1);
        color: #fff;
        box-shadow: 0 8px 22px rgba(16, 158, 158, 0.2);
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
    hr { border-color: #192b3e; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.html(
    '<script src="https://code.tidio.co/dnp0ykgircft6qsxxacgwdjwoh8oky8u.js" async></script>',
    unsafe_allow_javascript=True,
)


st.markdown(
    f"""
    <div class="topbar">
        <span>⚡ IT &amp; Infrastructure Services in Guntur</span>
        <span> · </span>
        <span>📍 {ADDRESS}</span>
        <span> · </span>
        <a href="tel:+{PHONE_LINK}">📞 {PHONE_DISPLAY}</a>
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
            <a href="#home"><span class="nav-emoji" aria-hidden="true">🏠</span>Home</a>
            <a href="#cyber-security-details"><span class="nav-emoji" aria-hidden="true">🛡️</span>Security</a>
            <a href="#office-lan-details"><span class="nav-emoji" aria-hidden="true">🖧</span>LAN Setup</a>
            <a href="#network-amc-details"><span class="nav-emoji" aria-hidden="true">🧰</span>AMC</a>
            <a href="#antivirus-details"><span class="nav-emoji" aria-hidden="true">🔐</span>Antivirus</a>
            <a href="#hardware-warranty-details"><span class="nav-emoji" aria-hidden="true">🛠️</span>Warranty</a>
            <a href="#os-server-details"><span class="nav-emoji" aria-hidden="true">🖥️</span>OS &amp; Server</a>
            <a href="#advanced-connectivity-details"><span class="nav-emoji" aria-hidden="true">📡</span>Networking</a>
        </nav>
        <div class="header-actions">
            <a class="header-action whatsapp" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer"><span aria-hidden="true">💬</span>&nbsp; WhatsApp</a>
            <a class="header-action" href="tel:+{PHONE_LINK}"><span aria-hidden="true">📞</span>&nbsp; {PHONE_DISPLAY}</a>
        </div>
        <details class="mobile-menu">
            <summary aria-label="Toggle navigation" aria-controls="mobile-navigation">
                <span aria-hidden="true">☰</span>
            </summary>
            <nav class="mobile-menu-panel" id="mobile-navigation" aria-label="Mobile navigation">
                <a href="#home"><span aria-hidden="true">🏠</span>Home</a>
                <a href="#cyber-security-details"><span aria-hidden="true">🛡️</span>Security</a>
                <a href="#office-lan-details"><span aria-hidden="true">🖧</span>LAN Setup</a>
                <a href="#network-amc-details"><span aria-hidden="true">🧰</span>AMC</a>
                <a href="#antivirus-details"><span aria-hidden="true">🔐</span>Antivirus</a>
                <a href="#hardware-warranty-details"><span aria-hidden="true">🛠️</span>Warranty</a>
                <a href="#os-server-details"><span aria-hidden="true">🖥️</span>OS &amp; Server</a>
                <a href="#advanced-connectivity-details"><span aria-hidden="true">📡</span>Networking</a>
            </nav>
        </details>
    </header>
    """,
    unsafe_allow_html=True,
)


hero_left, hero_right = st.columns([1.15, 0.85], gap="large")
with hero_left:
    st.markdown(
        """
        <div class="hero" id="home">
            <span class="eyebrow">🚀 Business IT Infrastructure in Guntur</span>
            <h1>Complete Networking, Cyber Security & <span class="accent">IT Infrastructure</span></h1>
            <p class="hero-copy">
                End-to-end IT services across Guntur and Andhra Pradesh:
                office LAN setup, Tally data sharing, network AMC, firewall security,
                antivirus, hardware support and Windows/Linux servers.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-header">
                <div class="status-brand">
                    <span class="status-light red" aria-hidden="true"></span>
                    <span class="status-light yellow" aria-hidden="true"></span>
                    <span class="status-light green" aria-hidden="true"></span>
                    <span class="status-label">hanvika-it-status</span>
                </div>
                <span class="online"><span class="online-dot" aria-hidden="true"></span>ONLINE</span>
            </div>
            <div class="status-rows">
                <div class="status-row" style="--status-accent:#ff8b98">
                    <span class="status-icon" aria-hidden="true">🛡️</span>
                    <span class="status-copy"><strong>Firewall &amp; Cyber Security</strong><small>Fortinet, Sophos, IPS/IDS &amp; VPN</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                </div>
                <div class="status-row" style="--status-accent:#63c8e8">
                    <span class="status-icon" aria-hidden="true">🖧</span>
                    <span class="status-copy"><strong>Office LAN &amp; Tally Sharing</strong><small>Centralized server &amp; multi-system setup</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                </div>
                <div class="status-row" style="--status-accent:#67d6a5">
                    <span class="status-icon" aria-hidden="true">🖥️</span>
                    <span class="status-copy"><strong>Windows &amp; Linux OS/Servers</strong><small>Active Directory, DNS, Hyper-V &amp; Ubuntu</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                </div>
                <div class="status-row" style="--status-accent:#f5bb60">
                    <span class="status-icon" aria-hidden="true">📶</span>
                    <span class="status-copy"><strong>Mesh Wi-Fi &amp; P2P Links</strong><small>Wireless links &amp; multi-WAN options</small></span>
                    <span class="status-check" aria-label="Available">✓</span>
                </div>
            </div>
            <div class="status-footer">
                <p>Need immediate network setup or AMC support in Guntur?</p>
                <div class="status-actions">
                    <a class="status-action whatsapp" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">💬 WhatsApp</a>
                    <a class="status-action call" href="tel:+{PHONE_LINK}">📞 Call Engineer</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


services = [
    ("🛡️", "Cyber Security", "Firewall, VPN, access rules and threat monitoring.", "#ff7c83", "cyber-security-details"),
    ("🖧", "Office LAN", "Cabling, Wi-Fi, Tally, printer and file sharing.", "#54c7e8", "office-lan-details"),
    ("🧰", "Network AMC", "Routine health checks, troubleshooting and maintenance.", "#a78bfa", "network-amc-details"),
    ("🔐", "Antivirus", "Endpoint protection, malware cleanup and safer browsing.", "#f5b95f", "antivirus-details"),
    ("🖥️", "Windows & Linux", "Workstations, business servers and Linux support.", "#67d6a5", "os-server-details"),
    ("📡", "Advanced Connectivity", "Mesh Wi-Fi, P2P links, branch VPN and multi-WAN.", "#ff8fc9", "advanced-connectivity-details"),
    ("🛠️", "Hardware Warranty", "Registration, coverage checks and claim guidance.", "#67d6a5", "hardware-warranty-details"),
]

service_cards = "".join(
    f'<article class="service-card" style="--card-accent:{escape(color)}">'
    f'<span class="service-icon" aria-hidden="true">{escape(icon)}</span>'
    f'<h3>{escape(title)}</h3><p>{escape(description)}</p>'
    f'<a class="service-card-link" href="#{escape(detail_id)}" aria-haspopup="dialog">'
    f'<span>Explore service details</span><span aria-hidden="true">↗</span></a></article>'
    for icon, title, description, color, detail_id in services
)

with st.container(key="services_section"):
    st.markdown(
        """
        <div class="section-heading" id="service-details">
            <span class="eyebrow">✨ What we do</span>
            <h2>Complete IT services for your business</h2>
            <p class="service-guide">👆 Want the service details? Click any service card to explore features and related catalog items in a popup.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="service-preview-grid">{service_cards}</div>', unsafe_allow_html=True)

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
        "intro": "Technical and administrative assistance for warranty registration, coverage checks, and claim preparation.",
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
        "notice": "Warranty terms, coverage, and claim approval are decided by the product manufacturer. Hanvika IT Solutions provides guidance and administrative assistance only.",
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
   ("wqeads.jpg", "🧵", "Networking Setup & Cabling", "LAN, Wi-Fi 6, routers, switches, cabling and troubleshooting."),
   ("werewa.jpg", "📡", "Advanced Site Networking", "Headquarters LAN, branch VPN, P2P antennas and mesh Wi-Fi."),
   ("wrwqr.jpg", "🪟", "Windows OS Infrastructure", "Windows Server, hybrid security and workstation support."),
   ("werad.jpg", "🐧", "Linux & Raspberry Pi", "Linux servers, Raspberry Pi OS and IoT operating systems."),
   ("asd.jpg", "🛠️", "Hardware Warranty Support", "Registration, validity checks and service ticket assistance."),
   ("2313.jpg", "🔧", "Office Network AMC", "On-site support, health checks and Tally data sharing."),
]
catalog_by_image = {image: (image, icon, title, description) for image, icon, title, description in catalog}
service_catalog_images = {
   "cyber-security-details": ("werewa.jpg",),
   "office-lan-details": ("wqeads.jpg",),
   "network-amc-details": ("2313.jpg",),
   "antivirus-details": ("wrwqr.jpg",),
   "hardware-warranty-details": ("asd.jpg",),
   "os-server-details": ("wrwqr.jpg", "werad.jpg"),
   "advanced-connectivity-details": ("wqeads.jpg", "werewa.jpg"),
}

detail_modals = []
for service in detailed_services:
    feature_markup = "".join(
        f'<article class="detail-item"><h4><span aria-hidden="true">{escape(icon)}</span>'
        f'<span>{escape(title)}</span></h4><p>{escape(description)}</p></article>'
        for icon, title, description in service["features"]
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
        device_icons = {
            "Laptops": "💻",
            "Inkjet printers": "🖨️",
            "Desktop PCs": "🖥️",
            "Laser printers": "🖨️",
            "All-in-One systems": "🖥️",
            "Scanners": "📠",
            "Monitors": "🖥️",
            "Multi-Function devices": "🖨️",
        }
        devices_markup = "".join(
            f'<li><span aria-hidden="true">{device_icons.get(tag, "📦")}</span>{escape(tag)}</li>'
            for tag in service.get("tags", [])
        )
        services_markup = "".join(
            f'<li><span aria-hidden="true">{escape(icon)}</span><span class="warranty-service-copy"><strong>{escape(title)}</strong><small>{escape(description)}</small></span></li>'
            for icon, title, description in service["features"]
        )
        service_content = (
            f'<div class="warranty-panels">'
            f'<section class="warranty-panel"><h4>📦 Supported Devices</h4>'
            f'<ul class="warranty-device-list">{devices_markup}</ul></section>'
            f'<section class="warranty-panel"><h4>🤝 Our Services</h4>'
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
        image_url = f"{IMAGE_BASE}/{escape(image)}"
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
            f'<img src="{image_url}" alt="{image_title}">'
            f'<span class="catalog-zoom-hint">🔍 Click to enlarge</span></label>'
            f'<div class="modal-catalog-copy"><strong>{escape(icon)} {escape(title)}</strong>'
            f'<p>{escape(description)}</p></div>{zoom_overlay}</article>'
        )
    catalog_markup = "".join(catalog_cards)
    related_catalog = (
        f'<div class="modal-catalog"><h4>🧩 Related catalog items</h4>'
        f'<div class="modal-catalog-grid">{catalog_markup}</div></div>'
    )
    whatsapp_message = quote(
        f"Hello Hanvika IT Solutions, I am interested in {service['title']}. Please share more details."
    )
    whatsapp_url = f"{WHATSAPP_URL}?text={whatsapp_message}"
    contact_actions = (
        f'<div class="detail-actions">'
        f'<a class="detail-action whatsapp" href="{escape(whatsapp_url, quote=True)}" target="_blank" rel="noopener noreferrer">💬 WhatsApp about this service</a>'
        f'<a class="detail-action call" href="tel:+{PHONE_LINK}">📞 Call {PHONE_DISPLAY}</a>'
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
        f'{service_content}{related_catalog}{notice}{contact_actions}</div></section>'
    )

st.html("\n".join(detail_modals))

with st.container(key="estimator_section"):
    st.markdown(
        """
        <div class="section-heading">
            <span class="eyebrow">🧮 Cost estimator</span>
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
    st.link_button(
        "✅ Confirm Estimate via WhatsApp",
        f"{WHATSAPP_URL}?text={quote(estimate_text)}",
        use_container_width=True,
    )

with st.container(key="contact_section"):
    st.markdown(
        """
        <div class="section-heading">
            <span class="eyebrow">📩 Contact us</span>
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
                <p><b>📞 Phone / WhatsApp</b><br>{PHONE_DISPLAY}</p>
                <p><b>🗺️ Service Region</b><br>Guntur and surrounding regions across Andhra Pradesh</p>
                <p><b>🕒 Support</b><br>Availability confirmed when you contact us</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with contact_right:
        name = st.text_input("👤 Your name")
        phone = st.text_input("📱 Phone number")
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
            ],
        )
        details = st.text_area("📝 Details / message", height=130)
        st.caption(
            "Submitting prepares a WhatsApp link; your details are shared only if you choose to open it. "
            "Do not enter passwords or confidential network information."
        )

        if st.button("💬 Send Inquiry on WhatsApp", type="primary", use_container_width=True):
            if not name or not phone:
                st.error("Please enter your name and phone number.")
            else:
                inquiry = (
                    f"Hello Hanvika IT Solutions, my name is {name}. "
                    f"My phone number is {phone}. I need {required_service}. "
                    f"Details: {details or 'Please contact me'}"
                )
                st.link_button("📲 Open WhatsApp", f"{WHATSAPP_URL}?text={quote(inquiry)}")

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
                    <a class="footer-phone" href="tel:+{PHONE_LINK}">📞 Call {PHONE_DISPLAY}</a>
                    <a class="footer-phone" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">💬 Chat on WhatsApp ↗</a>
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
                <a class="policy-trigger" href="#privacy-policy-details"><span class="footer-emoji" aria-hidden="true">🔒</span>Privacy Policy</a>
                <a class="policy-trigger" href="#terms-conditions-details"><span class="footer-emoji" aria-hidden="true">📄</span>Terms &amp; Conditions</a>
                <a class="policy-trigger" href="#refund-policy-details"><span class="footer-emoji" aria-hidden="true">↩️</span>Refund Policy</a>
            </div>
        </div>
        <div class="footer-legal-grid">
            <section class="footer-legal" id="privacy-policy-details" aria-labelledby="privacy-policy-title">
                <a class="policy-backdrop" href="#legal-notices" tabindex="-1" aria-hidden="true"></a>
                <div class="policy-dialog" role="dialog" aria-labelledby="privacy-policy-title">
                    <a class="policy-close" href="#legal-notices" aria-label="Close Privacy Policy">×</a>
                    <h4 id="privacy-policy-title">🔒 Privacy Policy</h4>
                    <p>
                        This app is not configured with a database for inquiries. Form details are processed to prepare
                        a WhatsApp message; choosing to open the link shares its contents with WhatsApp, subject to its
                        privacy terms. The website host may process requests or technical logs. The page also requests
                        fonts from Google Fonts and images from GitHub Pages; those providers may receive standard
                        connection data. The optional Tidio chat widget may process messages and technical data when
                        you use chat. Please do not submit passwords, access keys, or other sensitive information.
                    </p>
                </div>
            </section>
            <section class="footer-legal" id="terms-conditions-details" aria-labelledby="terms-conditions-title">
                <a class="policy-backdrop" href="#legal-notices" tabindex="-1" aria-hidden="true"></a>
                <div class="policy-dialog" role="dialog" aria-labelledby="terms-conditions-title">
                    <a class="policy-close" href="#legal-notices" aria-label="Close Terms &amp; Conditions">×</a>
                    <h4 id="terms-conditions-title">📄 Terms &amp; Conditions</h4>
                    <p>
                        Website content is general information about Hanvika IT Solutions. Service availability,
                        scope, deliverables, schedule, and fees are confirmed in a written quote, invoice, or service
                        agreement; website estimates are indicative only. Customers must have authorization for any
                        systems they ask us to access. Third-party software, hardware, and external links remain subject
                        to their respective providers' terms. These terms do not limit rights provided by applicable law.
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
            <span>© {COPYRIGHT_YEAR} Hanvika IT Solutions. All rights reserved.</span>
            <span class="footer-security">🔒 Click a notice to review our privacy and security details.</span>
            <span class="footer-version">Version {APP_VERSION}</span>
            <a class="policy-trigger" href="#privacy-policy-details">🔒 Privacy Policy</a>
            <a class="policy-trigger" href="#terms-conditions-details">📄 Terms &amp; Conditions</a>
            <a class="policy-trigger" href="#refund-policy-details">↩️ Refund Policy</a>
            <a class="policy-trigger" href="#security-disclaimer-details">🛡️ Security Disclaimer</a>
            <a href="#home">🏠 Back to top ↑</a>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
