from urllib.parse import quote

IMAGE_BASE = "https://lokeshkumarpuvvada.github.io/hit"
GITHUB_CATALOG_IMAGE_BASE = (
    "https://raw.githubusercontent.com/lokeshkumarpuvvada/cloudprintagent/main"
)
GITHUB_CATALOG_IMAGES = {"pca (1).jpeg", "pca (2).jpeg", "pca (3).jpeg"}

SERVICE_CATALOG_IMAGES = {
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

SERVICES = [
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

CATALOG_ITEMS = [
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


def catalog_image_url(filename):
    encoded_filename = quote(filename, safe="")
    if filename in GITHUB_CATALOG_IMAGES:
        return f"{GITHUB_CATALOG_IMAGE_BASE}/{encoded_filename}"
    return f"{IMAGE_BASE}/{encoded_filename}"


def build_default_service_catalog():
    catalog_by_image = {
        image: {
            "url": catalog_image_url(image),
            "icon": icon,
            "title": title,
            "description": description,
            "public_id": "",
        }
        for image, icon, title, description in CATALOG_ITEMS
    }
    return {
        service_id: [catalog_by_image[image].copy() for image in images]
        for service_id, images in SERVICE_CATALOG_IMAGES.items()
    }


DEFAULT_SERVICE_CATALOG = build_default_service_catalog()
SERVICE_NAMES = {detail_id: title for title, _, _, detail_id in SERVICES}
