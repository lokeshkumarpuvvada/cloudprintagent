from urllib.parse import quote

import streamlit as st


PHONE_DISPLAY = "+91 9885138489"
PHONE_LINK = "919885138489"
ADDRESS = "Guntur - 522002, Andhra Pradesh, India"
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
    .stApp {
        position: relative;
        isolation: isolate;
        background:
            radial-gradient(ellipse at 8% 10%, rgba(12, 118, 126, 0.14), transparent 34rem),
            radial-gradient(ellipse at 92% 38%, rgba(106, 69, 173, 0.12), transparent 32rem),
            #07111f;
        color: #e5eef8;
    }
    .stApp::before {
        content: "";
        position: fixed;
        inset: -12vh -10vw;
        z-index: 0;
        pointer-events: none;
        background:
            radial-gradient(ellipse at 18% 22%, rgba(65, 184, 255, .26), transparent 34%),
            radial-gradient(ellipse at 78% 30%, rgba(147, 105, 255, .19), transparent 38%),
            radial-gradient(ellipse at 54% 82%, rgba(23, 194, 174, .16), transparent 36%);
        opacity: .46;
        transform: translateZ(0) scale(.96);
        transform-origin: center;
        animation: space-depth-zoom 38s ease-in-out infinite alternate;
        will-change: transform, opacity;
    }
    .stAppViewContainer {
        position: relative;
        z-index: 1;
    }
    @keyframes space-depth-zoom {
        0% {
            opacity: .34;
            transform: translate3d(-.6%, .4%, 0) scale(.96);
        }
        50% {
            opacity: .15;
            transform: translate3d(0, 0, 0) scale(1.045);
        }
        100% {
            opacity: .26;
            transform: translate3d(.6%, -.35%, 0) scale(1.12);
        }
    }
    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }
    .st-key-services_section,
    .st-key-catalog_section,
    .st-key-estimator_section,
    .st-key-contact_section {
        position: relative;
        isolation: isolate;
        padding: 1.4rem clamp(1rem, 3vw, 2.2rem) 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(123, 164, 198, 0.18);
        border-radius: 26px;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.14);
    }
    .st-key-services_section::before,
    .st-key-catalog_section::before,
    .st-key-estimator_section::before,
    .st-key-contact_section::before {
        content: "";
        position: absolute;
        inset: -10% 0;
        z-index: -1;
        pointer-events: none;
        opacity: .35;
        background-size: 112px 112px, 173px 173px;
        background-position: 12px 24px, 63px 80px;
        will-change: transform;
    }
    .st-key-services_section > *,
    .st-key-catalog_section > *,
    .st-key-estimator_section > *,
    .st-key-contact_section > * {
        position: relative;
        z-index: 1;
    }
    .st-key-services_section {
        background:
            radial-gradient(ellipse at 5% 0%, rgba(35, 122, 224, 0.18), transparent 34rem),
            linear-gradient(135deg, #0d1b31, #10182b 58%, #13182c);
        background-attachment: fixed, scroll;
    }
    .st-key-services_section::before {
        background-image:
            radial-gradient(circle, rgba(102, 188, 255, .72) 1px, transparent 1.6px),
            radial-gradient(circle, rgba(122, 221, 214, .42) 1px, transparent 1.7px);
    }
    .st-key-catalog_section {
        background:
            radial-gradient(ellipse at 95% 0%, rgba(26, 176, 126, 0.17), transparent 34rem),
            linear-gradient(135deg, #0b211f, #0d1d25 55%, #10242a);
        background-attachment: fixed, scroll;
    }
    .st-key-catalog_section::before {
        background-image:
            radial-gradient(circle, rgba(111, 233, 178, .62) 1px, transparent 1.6px),
            radial-gradient(circle, rgba(91, 190, 255, .4) 1px, transparent 1.7px);
    }
    .st-key-estimator_section {
        background:
            radial-gradient(ellipse at 4% 5%, rgba(161, 98, 255, 0.17), transparent 32rem),
            radial-gradient(ellipse at 95% 95%, rgba(245, 185, 95, 0.10), transparent 28rem),
            linear-gradient(135deg, #1a1730, #15192d 58%, #211a2c);
        background-attachment: fixed, fixed, scroll;
    }
    .st-key-estimator_section::before {
        background-image:
            radial-gradient(circle, rgba(202, 158, 255, .62) 1px, transparent 1.6px),
            radial-gradient(circle, rgba(255, 207, 123, .44) 1px, transparent 1.7px);
    }
    .st-key-contact_section {
        background:
            radial-gradient(ellipse at 90% 5%, rgba(12, 184, 155, 0.15), transparent 34rem),
            linear-gradient(135deg, #0c202a, #10232b 58%, #102b2b);
        background-attachment: fixed, scroll;
    }
    .st-key-contact_section::before {
        background-image:
            radial-gradient(circle, rgba(105, 235, 213, .6) 1px, transparent 1.6px),
            radial-gradient(circle, rgba(110, 178, 255, .4) 1px, transparent 1.7px);
    }
    @keyframes scroll-parallax {
        from { transform: translate3d(0, 28px, 0); }
        to { transform: translate3d(0, -28px, 0); }
    }
    @supports (animation-timeline: view()) {
        .st-key-services_section::before,
        .st-key-catalog_section::before,
        .st-key-estimator_section::before,
        .st-key-contact_section::before {
            animation: scroll-parallax linear both;
            animation-timeline: view(block);
            animation-range: entry 0% exit 100%;
        }
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
        position: relative;
        z-index: 2;
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
    .header-nav { display: flex; align-items: center; justify-content: center; gap: clamp(.6rem, 1.4vw, 1.3rem); }
    .header-nav a {
        color: #adbed0;
        font-size: .79rem;
        font-weight: 700;
        text-decoration: none;
        transition: color 150ms ease;
    }
    .header-nav a:hover { color: #79ded1; }
    .header-actions { display: flex; align-items: center; gap: .55rem; }
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
        margin-top: 1.1rem;
        padding: 4.2rem 3.5rem;
        border: 1px solid #1b3048;
        border-radius: 28px;
        background:
            radial-gradient(circle at 85% 15%, rgba(41, 137, 255, 0.24), transparent 28rem),
            radial-gradient(circle at 15% 100%, rgba(12, 184, 155, 0.15), transparent 24rem),
            radial-gradient(circle at 100% 100%, rgba(161, 98, 255, 0.12), transparent 22rem),
            linear-gradient(145deg, #0c1a2b, #091525);
        background-attachment: fixed, fixed, fixed, scroll;
        overflow: hidden;
        position: relative;
        isolation: isolate;
    }
    .hero > * { position: relative; z-index: 1; }
    .hero::before,
    .hero::after {
        content: "";
        position: absolute;
        pointer-events: none;
        z-index: 0;
        will-change: transform;
    }
    .hero::before {
        width: 250px;
        height: 250px;
        top: -105px;
        right: -78px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(83, 171, 255, .24), rgba(103, 116, 255, .07) 48%, transparent 72%);
        animation: float-glow 10s ease-in-out infinite;
    }
    .hero::after {
        inset: 0;
        opacity: .30;
        background-image:
            radial-gradient(circle, rgba(137, 221, 255, .82) 1px, transparent 1.8px),
            radial-gradient(circle, rgba(167, 146, 255, .65) 1px, transparent 1.8px);
        background-size: 89px 89px, 137px 137px;
        background-position: 12px 18px, 55px 73px;
        animation: float-particles 22s linear infinite;
    }
    @keyframes float-glow {
        0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
        50% { transform: translate3d(-12px, 18px, 0) scale(1.05); }
    }
    @keyframes float-particles {
        0%, 100% { transform: translate3d(0, 0, 0); }
        50% { transform: translate3d(0, -10px, 0); }
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
    .status-card, .service-card, .info-card, .catalog-card {
        border: 1px solid #1c3046;
        border-radius: 18px;
        background: linear-gradient(145deg, #0e1d2e, #0a1725);
    }
    .status-card { padding: 1.25rem; }
    .status-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.85rem 0.95rem;
        margin-top: 0.75rem;
        border: 1px solid #1b3045;
        border-radius: 12px;
        background: #091521;
        color: #c7d5e5;
    }
    .online {
        color: #52d59a;
        background: rgba(82, 213, 154, 0.1);
        border-radius: 999px;
        padding: 0.28rem 0.55rem;
        font-size: 0.75rem;
        font-weight: 800;
        box-shadow: 0 0 0 0 rgba(82, 213, 154, .28);
        animation: online-pulse 2.8s ease-out infinite;
    }
    @keyframes online-pulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(82, 213, 154, .22); }
        50% { box-shadow: 0 0 0 5px rgba(82, 213, 154, 0); }
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
    .service-card {
        position: relative;
        overflow: hidden;
        min-height: 210px;
        padding: 1.35rem;
        transition: transform 220ms ease, border-color 220ms ease, box-shadow 220ms ease;
        border-top: 2px solid var(--card-accent, #35b8c2);
        background:
            linear-gradient(145deg, color-mix(in srgb, var(--card-accent, #35b8c2) 8%, #0e1d2e), #0a1725 74%);
    }
    .service-card::after {
        content: "";
        position: absolute;
        inset: 0;
        pointer-events: none;
        opacity: 0;
        background: linear-gradient(115deg, transparent 20%, color-mix(in srgb, var(--card-accent, #35b8c2) 10%, transparent) 50%, transparent 78%);
        transform: translateX(-35%);
        transition: opacity 220ms ease, transform 420ms ease;
    }
    .service-card:hover {
        transform: translateY(-4px);
        border-color: var(--card-accent, #35b8c2);
        box-shadow: 0 16px 35px color-mix(in srgb, var(--card-accent, #35b8c2) 16%, transparent);
    }
    .service-card:hover::after { opacity: 1; transform: translateX(25%); }
    .service-card h3 { color: var(--card-accent, #eef6ff); font-size: 1.05rem; }
    .service-card p { color: #94a7ba; line-height: 1.65; font-size: 0.9rem; }
    .catalog-card {
        overflow: hidden;
        border-color: #263d55;
        transition: transform 220ms ease, border-color 220ms ease, box-shadow 220ms ease;
    }
    .catalog-card:hover {
        border-color: #59bcb7;
        transform: translateY(-4px);
        box-shadow: 0 16px 34px rgba(26, 176, 126, .12);
    }
    .catalog-card img {
        width: 100%;
        height: 190px;
        object-fit: cover;
        transition: transform 420ms ease;
    }
    .catalog-card:hover img { transform: scale(1.035); }
    .catalog-card div { padding: 1.1rem; }
    .catalog-card h3 { color: #edf5fc; font-size: 1rem; }
    .catalog-card p { color: #91a4b8; font-size: 0.86rem; }
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
        justify-content: space-between;
        gap: 1rem;
    }
    .footer-bottom a { color: #8fa9bd; text-decoration: none; }
    .footer-bottom a:hover { color: #73ded0; }
    @media (max-width: 1050px) {
        .site-header { flex-wrap: wrap; }
        .header-nav { order: 3; width: 100%; justify-content: flex-start; flex-wrap: wrap; }
        .footer-grid { grid-template-columns: 1.2fr 1fr 1fr; }
        .footer-grid > :last-child { grid-column: 1 / -1; }
    }
    @media (max-width: 760px) {
        .footer-grid { grid-template-columns: 1fr 1fr; gap: 1.5rem; }
        .site-header { padding: .85rem; }
        .header-nav { gap: .8rem; }
    }
    @media (max-width: 480px) {
        .footer-grid { grid-template-columns: 1fr; }
        .footer-grid > :last-child { grid-column: auto; }
        .topbar { flex-direction: column; gap: .25rem; }
        .header-actions { width: 100%; }
        .header-action { flex: 1; }
        .footer-bottom { flex-direction: column; }
    }
    @media (max-width: 760px) {
        .hero::before { width: 180px; height: 180px; opacity: .75; }
        .hero::after { opacity: .18; }
        .hero,
        .st-key-services_section,
        .st-key-catalog_section,
        .st-key-estimator_section,
        .st-key-contact_section {
            background-attachment: scroll !important;
        }
        .st-key-services_section::before,
        .st-key-catalog_section::before,
        .st-key-estimator_section::before,
        .st-key-contact_section::before { opacity: .2; }
    }
    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            animation-duration: .01ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
            transition-duration: .01ms !important;
        }
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
    .header-action:focus-visible,
    .footer-column a:focus-visible,
    .footer-bottom a:focus-visible {
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


st.markdown(
    f"""
    <div class="topbar">
        <span>Official IT &amp; Infrastructure Partner in Guntur</span>
        <span> · </span>
        <span>{ADDRESS}</span>
        <span> · </span>
        <a href="tel:+{PHONE_LINK}">{PHONE_DISPLAY}</a>
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
            <a href="#cyber-security">Security</a>
            <a href="#office-lan">LAN Setup</a>
            <a href="#network-amc">AMC</a>
            <a href="#antivirus">Antivirus</a>
            <a href="#hardware-warranty-support">Warranty</a>
            <a href="#windows-and-linux">OS &amp; Server</a>
            <a href="#advanced-connectivity">Networking</a>
        </nav>
        <div class="header-actions">
            <a class="header-action whatsapp" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
            <a class="header-action" href="tel:+{PHONE_LINK}">Call us</a>
        </div>
    </header>
    """,
    unsafe_allow_html=True,
)


hero_left, hero_right = st.columns([1.35, 0.65], gap="large")
with hero_left:
    st.markdown(
        """
        <div class="hero" id="home">
            <span class="eyebrow">Official IT Partner in Guntur</span>
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
    action_left, action_right = st.columns(2)
    with action_left:
        st.link_button("Quick Quote on WhatsApp", WHATSAPP_URL, use_container_width=True)
    with action_right:
        st.link_button("Call 9885138489", "tel:+919885138489", use_container_width=True)

with hero_right:
    st.markdown(
        """
        <div class="status-card">
            <div style="display:flex;justify-content:space-between;color:#8097ad">
                <b>hanvika-it-status</b><span class="online">ONLINE</span>
            </div>
            <div class="status-row"><span>Firewall & Cyber Security</span><b style="color:#52d59a">✓</b></div>
            <div class="status-row"><span>Office LAN & Tally Sharing</span><b style="color:#52d59a">✓</b></div>
            <div class="status-row"><span>Windows & Linux Servers</span><b style="color:#52d59a">✓</b></div>
            <div class="status-row"><span>Mesh Wi-Fi & P2P</span><b style="color:#52d59a">✓</b></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


services = [
    ("Cyber Security", "Firewall setup, inbound/outbound rules, VPN, IPS/IDS, threat prevention and network auditing.", "#ff7c83"),
    ("Office LAN", "Small office networking, Tally sharing, file and printer access, cabling and centralized storage.", "#54c7e8"),
    ("Network AMC", "Health checks, router and switch maintenance, ISP support, preventive maintenance and on-demand help.", "#a78bfa"),
    ("Antivirus", "Endpoint protection, malware removal, USB security, anti-phishing, ransomware shield and backup.", "#f5b95f"),
    ("Windows & Linux", "Desktop/server setup, Active Directory, DNS, DHCP, Hyper-V, web servers and automated backups.", "#67d6a5"),
    ("Advanced Connectivity", "Multi-floor mesh Wi-Fi, P2P links, branch VPN, multi-WAN, cloud storage and RDP servers.", "#ff8fc9"),
]

with st.container(key="services_section"):
    st.markdown(
        """
        <div class="section-heading">
            <span class="eyebrow">What we do</span>
            <h2>Complete IT services for your business</h2>
            <p>Reliable infrastructure, security and maintenance support for offices, branches and enterprises.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for row in range(0, len(services), 3):
        columns = st.columns(3, gap="medium")
        for column, (title, description, color) in zip(columns, services[row:row + 3]):
            with column:
                st.markdown(
                    f'<div class="service-card" style="--card-accent:{color}"><h3>{title}</h3><p>{description}</p></div>',
                    unsafe_allow_html=True,
                )

catalog = [
    ("wqeads.jpg", "Networking Setup & Cabling", "LAN, Wi-Fi 6, routers, switches, cabling and troubleshooting."),
    ("werewa.jpg", "Advanced Site Networking", "Headquarters LAN, branch VPN, P2P antennas and mesh Wi-Fi."),
    ("wrwqr.jpg", "Windows OS Infrastructure", "Windows Server, hybrid security and workstation support."),
    ("werad.jpg", "Linux & Raspberry Pi", "Linux servers, Raspberry Pi OS and IoT operating systems."),
    ("asd.jpg", "Hardware Warranty Support", "Registration, validity checks and service ticket assistance."),
    ("2313.jpg", "Office Network AMC", "On-site support, health checks and Tally data sharing."),
]

with st.container(key="catalog_section"):
    st.markdown(
        """
        <div class="section-heading">
            <span class="eyebrow">Solutions catalog</span>
            <h2>Built for everyday business operations</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for row in range(0, len(catalog), 3):
        columns = st.columns(3, gap="medium")
        for column, (image, title, description) in zip(columns, catalog[row:row + 3]):
            with column:
                st.markdown(
                    f"""
                    <div class="catalog-card">
                        <img src="{IMAGE_BASE}/{image}" alt="{title}">
                        <div><h3>{title}</h3><p>{description}</p></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

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
        workstations = st.slider("Number of workstations / PCs", 1, 100, 5)
        servers = st.slider("Windows / Linux servers", 0, 10, 1)
        firewall = st.checkbox("Fortinet / Sophos firewall")
        tally = st.checkbox("Tally & printer data sharing")
        antivirus = st.checkbox("Total security antivirus licenses")
        vpn = st.checkbox("Branch VPN & remote RDP")

        estimate = 8500 + (workstations * 650) + (servers * 2400)
        estimate += 4200 if firewall else 0
        estimate += 1800 if tally else 0
        estimate += 900 if antivirus else 0
        estimate += 3500 if vpn else 0

    with estimate_right:
        st.markdown(
            f"""
            <div class="info-card">
                <span class="eyebrow">Estimated package</span>
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
        "Confirm Estimate via WhatsApp",
        f"{WHATSAPP_URL}?text={quote(estimate_text)}",
        use_container_width=True,
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
                <p><b>Address</b><br>{ADDRESS}</p>
                <p><b>Phone / WhatsApp</b><br>{PHONE_DISPLAY}</p>
                <p><b>Service Region</b><br>Guntur and surrounding regions across Andhra Pradesh</p>
                <p><b>Support</b><br>Emergency support available 24/7</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with contact_right:
        name = st.text_input("Your name")
        phone = st.text_input("Phone number")
        required_service = st.selectbox(
            "Required service",
            [
                "Cyber Security",
                "Office LAN",
                "Network AMC",
                "Antivirus",
                "Windows / Linux Server",
                "Advanced Networking",
                "Hardware Warranty",
            ],
        )
        details = st.text_area("Details / message", height=130)

        if st.button("Send Inquiry on WhatsApp", type="primary", use_container_width=True):
            if not name or not phone:
                st.error("Please enter your name and phone number.")
            else:
                inquiry = (
                    f"Hello Hanvika IT Solutions, my name is {name}. "
                    f"My phone number is {phone}. I need {required_service}. "
                    f"Details: {details or 'Please contact me'}"
                )
                st.link_button("Open WhatsApp", f"{WHATSAPP_URL}?text={quote(inquiry)}")

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
                    <a class="footer-phone" href="tel:+{PHONE_LINK}">☎ Call {PHONE_DISPLAY}</a>
                    <a class="footer-phone" href="{WHATSAPP_URL}" target="_blank" rel="noopener noreferrer">Chat on WhatsApp ↗</a>
                </div>
            </div>
            <div class="footer-column">
                <h4>Core Services</h4>
                <a href="#cyber-security">Firewall &amp; Security</a>
                <a href="#office-lan">Small Office LAN Setup</a>
                <a href="#network-amc">Office Network AMC</a>
                <a href="#antivirus">Antivirus Solutions</a>
                <a href="#windows-and-linux">Windows &amp; Linux Server</a>
            </div>
            <div class="footer-column">
                <h4>Specialized Networking</h4>
                <a href="#advanced-connectivity">Multi-Floor Mesh Wi-Fi</a>
                <a href="#advanced-connectivity">P2P Wireless Links</a>
                <a href="#advanced-connectivity">Branch-to-Branch VPN</a>
                <a href="#advanced-connectivity">Multi-WAN Load Balancing</a>
                <a href="#hardware-warranty-support">Hardware Warranty Guidance</a>
            </div>
            <div class="footer-column">
                <h4>Hanvika IT Solutions</h4>
                <p class="footer-copy">
                    Professional networking, firewall security, and hardware technical
                    guidance across Guntur, Andhra Pradesh.
                </p>
                <a href="#send-a-service-inquiry">Send a service inquiry →</a>
            </div>
        </div>
        <div class="footer-bottom">
            <span>© Hanvika IT Solutions · Guntur, Andhra Pradesh</span>
            <a href="#home">Back to top ↑</a>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
