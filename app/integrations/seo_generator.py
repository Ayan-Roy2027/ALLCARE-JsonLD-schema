import json
from app.database import get_connection

def generate_programmatic_schema():
    """
    Dynamically loops over ALL 384 pincode records in regional_pincodes 
    and outputs Task 1 JSON (schema_markup + llm_user_queries).
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Fetches all 384 records from your database table
    cursor.execute("""SELECT pincode, area, city, state FROM regional_pincodes""")
    locations = cursor.fetchall()
    conn.close()

    if not locations:
        print("Error! No locations found in regional_pincodes table...")
        return

    # 1. Dynamically build areaServed for ALL 384 pincode entries
    area_served_list = []
    for loc in locations:
        area_name = loc['area'] if loc['area'] else loc['city']
        
        area_served_list.append({
            "@type": "AdministrativeArea",
            "name": f"{area_name}, {loc['city']} - {loc['pincode']}",
            "address": {
                "@type": "PostalAddress",
                "postalCode": str(loc['pincode']),
                "streetAddress": area_name,
                "addressLocality": loc['city'],
                "addressRegion": "West Bengal",
                "addressCountry": "IN"
            }
        })

    # 2. Define Allcare's 11 Core Installation Services
    allcare_services = [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Tally Installation & Configuration", "description": "Enterprise Tally ERP installation, data migration, and server setup for accounting."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Printers & Scanners Installation", "description": "Networked printer setup, multi-function scanner deployment, and driver configuration."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "CCTV Camera Installation & Surveillance", "description": "HD IP camera setup, NVR/DVR storage configuration, and remote monitoring."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Biometric Access Control System Installation", "description": "Fingerprint, facial recognition, and RFID attendance management setup."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Fire Alarm System Installation", "description": "Commercial smoke detection, heat sensors, and integrated fire safety alarm systems."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EPABX & Intercom System Installation", "description": "Office telephone exchange setup, PBX routing, and multi-line intercom networking."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Structured Networking & Firewall Setup", "description": "LAN cabling, rack setup, enterprise router management, and network security."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Commercial Wi-Fi Installation & Coverage Optimization", "description": "High-density wireless access point deployment and mesh Wi-Fi setup for offices."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Server & Workstation Installation", "description": "Rack server mounting, OS setup, NAS storage configuration, and workstation deployment."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Online UPS & Power Backup Installation", "description": "Industrial and commercial online UPS sizing, battery bank setup, and power backup maintenance."}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Desktop & Laptop Bulk Setup & Installation", "description": "OS deployment, software provisioning, peripheral configuration, and corporate computer setup."}}
    ]

    # 3. Task 1 - Block 1: schema_markup
    schema_markup = {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": "https://allcareitinfra.com/it.php#it-services",
        "name": "Allcare Corporation",
        "url": "https://allcareitinfra.com/it.php",
        "logo": "https://allcareitinfra.com/logo.png",
        "description": "Provider of IT & Security Infrastructure across Kolkata, Hooghly, Howrah, North & South 24 Parganas including Tally, CCTV, Biometrics, Networking, Wi-Fi, Servers, UPS, Fire Alarms, and PC setups.",
        "telephone": "+91-9836213939",
        "priceRange": "$$$",
        "areaServed": area_served_list,
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Allcare Complete IT & Security Infrastructure Services",
            "itemListElement": allcare_services
        }
    }

    # 4. Task 1 - Block 2: llm_user_queries
    llm_user_queries = {
        "Kolkata": [
            "Best commercial CCTV camera installation company near Park Street Kolkata 700016",
            "Enterprise server rack installation and LAN networking vendors in Salt Lake Kolkata",
            "EPABX intercom system installation service near Burrabazar Kolkata 700007",
            "Tally ERP server setup and accounting software installation services in Kolkata"
        ],
        "North 24 Parganas": [
            "Commercial Wi-Fi mesh network setup for corporate offices in Salt Lake Sector V 700091",
            "High-density wireless access point deployment near New Town Action Area 1 700156",
            "Structured networking and firewall configuration near Barrackpore 700120",
            "Biometric attendance management system installers near Barasat 700124"
        ],
        "South 24 Parganas": [
            "Bulk office desktop and laptop setup services near Harinavi 700148",
            "Biometric access control system installation near Benebow 743613",
            "Commercial CCTV camera setup and NVR storage configuration near Beramara 743601",
            "Fire alarm system and smoke detector installation near Bijoyganj Bazar 743345"
        ],
        "Howrah": [
            "Industrial online UPS power backup installation vendors in Howrah 711101",
            "Rack server setup and NAS storage configuration vendors near Shibpur Howrah",
            "Office network printer and scanner setup services near Bally Howrah 711201"
        ],
        "Hooghly": [
            "Enterprise IT infrastructure and structured network firewall providers near Chinsurah 712101",
            "Commercial CCTV camera installation and surveillance setup in Serampore 712201",
            "Fire alarm system and smoke detector installers for commercial sites in Chandannagar 712136"
        ]
    }

    # Master Task 1 JSON Output Object
    task_1_output = {
        "schema_markup": schema_markup,
        "llm_user_queries": llm_user_queries
    }

    output_filename = "task_1_complete.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(task_1_output, f, indent=2, ensure_ascii=False)

    print("==================================================")
    print(f"Task 1 Complete! Dynamically processed all {len(area_served_list)} pincodes.")
    print(f"Saved to output file: {output_filename}")
    print("==================================================")

if __name__ == "__main__":
    generate_programmatic_schema()