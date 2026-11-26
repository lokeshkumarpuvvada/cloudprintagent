PHONE = "+91 9885138489"
ADDRESS = "Guntur - 522002, Andhra Pradesh, India"


SERVICES = {
    "1": (
        "Cyber Security",
        [
            "Hardware and software firewall setup",
            "Inbound and outbound security rules",
            "Fortinet, Sophos, Cisco firewall support",
            "Secure VPN and remote access",
            "IPS/IDS threat and intrusion prevention",
            "Network traffic monitoring and security audits",
        ],
    ),
    "2": (
        "Office Networking",
        [
            "Small office LAN setup",
            "Tally and business application sharing",
            "File and printer sharing",
            "Structured cabling and cable management",
            "Router, switch and Wi-Fi setup",
            "Central storage and shared-folder permissions",
        ],
    ),
    "3": (
        "Network AMC",
        [
            "Network health checks",
            "Router and switch maintenance",
            "Wi-Fi and LAN troubleshooting",
            "ISP link and failover support",
            "Preventive maintenance",
            "On-demand technical support",
        ],
    ),
    "4": (
        "Antivirus and Endpoint Security",
        [
            "Antivirus installation and configuration",
            "Real-time virus and malware scanning",
            "USB drive protection",
            "Safe browsing and anti-phishing protection",
            "Ransomware protection and backup",
        ],
    ),
    "5": (
        "Windows and Linux Servers",
        [
            "Windows desktop and server installation",
            "Active Directory, DNS and DHCP setup",
            "Hyper-V virtualization",
            "Linux web and database server setup",
            "SSH, mail server and automated backup",
            "Server security hardening",
        ],
    ),
    "6": (
        "Advanced Connectivity",
        [
            "Multi-floor mesh Wi-Fi",
            "Point-to-point wireless links",
            "Branch-to-branch VPN",
            "Multi-WAN and load balancing",
            "Personal cloud storage",
            "Multi-user RDP server setup",
        ],
    ),
    "7": (
        "IT Hardware Warranty Support",
        [
            "Warranty registration assistance",
            "Warranty validity and coverage check",
            "Invoice, serial number and document support",
            "Service ticket and complaint registration",
            "Authorized service center guidance",
        ],
    ),
}


def show_service(number):
    title, details = SERVICES[number]
    print(f"\n{title}")
    print("-" * len(title))
    for detail in details:
        print(f"- {detail}")


print("=" * 52)
print("HANVIKA IT SOLUTIONS")
print("Complete Networking, Cyber Security & IT Infrastructure")
print("=" * 52)
print(f"Phone / WhatsApp: {PHONE}")
print(f"Address: {ADDRESS}")
print("Service Area: Guntur and surrounding regions")

print("\nAvailable Services:")
for number, (title, _) in SERVICES.items():
    print(f"{number}. {title}")
print("0. Exit")

while True:
    choice = input("\nSelect a service number: ").strip()

    if choice == "0":
        print("\nThank you for contacting Hanvika IT Solutions!")
        break

    if choice in SERVICES:
        show_service(choice)
    else:
        print("Invalid selection. Please enter a number from 0 to 7.")