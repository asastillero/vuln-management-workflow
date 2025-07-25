# parse_nessus.py
import xml.etree.ElementTree as ET
import csv

# Set the input and output paths
INPUT_FILE = "My Basic Network Scan_91t54m.nessus"
OUTPUT_FILE = "nessus_report.csv"

# Parse the Nessus XML file
tree = ET.parse(INPUT_FILE)
root = tree.getroot()

# Prepare CSV file for writing
with open(OUTPUT_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IP Address", "Port", "Plugin Name", "Severity", "CVSS Score", "CVE"])

    # Traverse ReportHosts and ReportItems
    for report_host in root.findall(".//ReportHost"):
        ip = report_host.attrib.get('name', 'Unknown')
        for report_item in report_host.findall("ReportItem"):
            port = report_item.attrib.get("port", "Unknown")
            plugin_name = report_item.attrib.get("pluginName", "Unknown")
            severity = report_item.attrib.get("severity", "0")
            cvss = report_item.findtext("cvss_base_score", default="-")
            cve = report_item.findtext("cve", default="-")

            writer.writerow([ip, port, plugin_name, severity, cvss, cve])

print(f"Report successfully written to {OUTPUT_FILE}")
