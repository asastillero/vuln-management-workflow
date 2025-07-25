# 🔐 Vulnerability Management Workflow

This project demonstrates a basic **Vulnerability Management Workflow** using:

- 🖥️ Kali Linux (with Nessus Essentials)
- 🎯 Metasploitable 2 as the vulnerable target
- 🐍 A custom Python script to parse `.nessus` scan results into a readable `.csv`

---

## 🎯 Project Goal

Simulate a real-world process of:

1. **Scanning a vulnerable machine**
2. **Identifying CVEs and their severity**
3. **Extracting scan data to CSV**
4. **Recommending remediation actions**

This project highlights your ability to detect, assess, and recommend fixes for vulnerabilities — applicable to SOC, GRC, and Vulnerability Analyst roles.

---

## 🧰 Tools Used

| Tool               | Purpose                               |
|--------------------|---------------------------------------|
| Kali Linux         | Security OS for scanning              |
| Nessus Essentials  | Vulnerability scanner                 |
| Metasploitable 2   | Vulnerable VM for testing             |
| Python 3           | Script automation (built-in on Kali)  |
| Visual Studio Code | For documentation and version control |

---

## 🔎 Nessus Scan Summary

- **Target**: Metasploitable 2 VM on the same bridged network 
- **Scanner**: Kali Linux with Nessus Essentials
- **Scan Type**: Basic Network Scan
- **Vulnerabilities Found**: 60+
- **Exported File**: `.nessus` (XML format)

---

## 🐍 Python Script: `parse_nessus_report.py`

This script extracts relevant findings from a `.nessus` file and outputs a clean CSV with key fields:

| Field         | Description                                |
|---------------|--------------------------------------------|
| IP Address    | Target system's IP                         |
| Port          | Vulnerable port                            |
| Plugin Name   | Description of vulnerability               |
| Severity      | Nessus Severity (1 = Low → 4 = Critical)   |
| CVSS Score    | CVSS v3 score if available                 |
| CVE           | Related CVE identifiers (if any)           |

> ℹ️ Informational severity (`0`) is excluded to focus on actionable issues.

---

## 📁 Example Output (`nessus_report.csv`)

```csv
IP Address,Port,Plugin Name,Severity,CVSS Score,CVE
192.168.1.17,8009,Apache Tomcat AJP Connector Request Injection,4,7.5,CVE-2020-1938
192.168.1.17,5432,SSL Version 2 and 3 Protocol Detection,4,10.0,
192.168.1.17,25,SSL DROWN Attack Vulnerability,2,4.3,CVE-2016-0800