# Enterprise SOC Platform: Wazuh + n8n + Telegram Notification
![Proxmox](https://img.shields.io/badge/Hypervisor-Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white)
![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-005571?style=for-the-badge&logo=wazuh&logoColor=white)
![n8n](https://img.shields.io/badge/SOAR-n8n-3b0a6b?style=for-the-badge&logo=n8n&logoColor=white)
![VirusTotal](https://img.shields.io/badge/Threat%20Intel-VirusTotal-394eef?style=for-the-badge&logo=virustotal&logoColor=white)
![AbuseIPDB](https://img.shields.io/badge/Reputation-AbuseIPDB-7b1fa2?style=for-the-badge&logo=abuseipdb&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-000000?style=for-the-badge&logo=mitre&logoColor=white)
![Atomic Red Team](https://img.shields.io/badge/Testing-Atomic%20Red%20Team-FF6F61?style=for-the-badge&logo=redhat&logoColor=white)

## Project Overview

A complete Security Operations Center (SOC) platform built from scratch that simulates a real-world enterprise security environment. This project demonstrates my ability to deploy, configure, and automate security operations using industry-standard tools with AI-powered alert triage and instant Telegram notifications.

The platform integrates SIEM and SOAR capabilities with 5 custom detection rules mapped to the MITRE ATT&CK framework, all automated through n8n workflows with OpenAI-powered analysis and real-time Telegram alerts.

---

## Purpose & Goals

### Why I Built This

As a IT Administrator transitioning into security, I created this project to:

- **Bridge the gap** between theoretical knowledge and hands-on implementation
- **Demonstrate practical skills** in SIEM deployment, detection engineering, and SOAR automation
- **Build a portfolio** that proves I can design and operate enterprise security tools
- **Understand the full attack lifecycle** from detection to response

---

## Project Status

| Goal | Status | Description |
|------|--------|-------------|
| SIEM Implementation | Complete | Wazuh deployed with Windows endpoint |
| Custom Detection Rules | Complete | 5 rules across 5 MITRE tactics |
| SOAR Automation | Complete | n8n workflows for alert processing |
| Telegram Integration | Complete | Real-time alerts to SOC channel |
| AI-Powered Triage | Complete | DeepSeek-V3.2 generates context-rich reports |
| Penetration Testing | Planned | Kali Linux for red team exercises |

---

## Key Achievements

| Achievement | Details |
|-------------|---------|
| **Custom Detection Rules** | 5 rules mapped to MITRE ATT&CK |
| **MITRE Tactics Covered** | Execution, Credential Access, Defense Evasion, Persistence, C2 |
| **SOAR Workflows** | 5 automated n8n workflows |
| **Alert Triage** | DeepSeek-V3.2 generates context-rich reports |
| **Response Time** | < 3 seconds from alert to Telegram notification |
| **Noise Reduction** | Smart severity filtering eliminates alert fatigue |

---

## Technology Stack

| Category | Tools |
|----------|-------|
| **SIEM** | Wazuh (Manager, Agent, Dashboard) |
| **Endpoint Security** | Sysmon, Windows Event Logs |
| **SOAR/Automation** | n8n |
| **AI Analysis** | DeepSeek-V3.2 (custom SOC prompts) |
| **Notifications** | Telegram Bot API |
| **Attack Simulation** | Atomic Red Team, MITRE ATT&CK |
| **Operating Systems** | Ubuntu 24.04, Windows 10, Kali Linux (planned) |
| **Virtualization** | Proxmox Virtual Environment|

---
