## Network Architecture Overview

```mermaid
graph TB
    subgraph "INTERNAL NETWORK (192.168.0.0/24)"
        
        subgraph WAZUH["WAZUH MANAGER"]
            style WAZUH fill:#e1f5fe,stroke:#01579b,stroke-width:2px
            W1["Ubuntu 24.04<br/>192.168.0.177"]
            W2["• Wazuh Manager<br/>• Wazuh Dashboard<br/>• Custom Rules: 100001-100005"]
        end
        
        subgraph N8N["n8n + AI"]
            style N8N fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
            N1["Ubuntu 24.04<br/>192.168.0.185"]
            N2["• n8n Webhook<br/>• IF Filter (Level 8)<br/>• AI Investigation<br/>• Telegram Bot"]
        end
        
        subgraph WIN["WINDOWS ENDPOINT"]
            style WIN fill:#fff3e0,stroke:#e65100,stroke-width:2px
            W11["Windows 10<br/>192.168.0.175"]
            W22["• Wazuh Agent<br/>• Sysmon<br/>• Atomic Red Team<br/>• Detection Tests"]
        end
        
        subgraph EXT["EXTERNAL"]
            style EXT fill:#f5f5f5,stroke:#333,stroke-width:2px
            TELEGRAM["📱 Telegram<br/>SOC Alerts"]
        end
        
        W11 -->|Port 1514/55000| W1
        W1 -->|HTTP 5678| N1
        N1 -->|HTTPS 443| TELEGRAM
        
        W1 <-.-> W11
        
    end
    
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
```

**Note**: Kali Linux will be implemented in a future phase as part of a dedicated penetration testing project.

## VM Resource Summary

| VM               | IP Address    | RAM | CPU Cores | Storage | Status  | Purpose             |
|------------------|---------------|-----|-----------|---------|---------|---------------------|
| Wazuh Manager    | 192.168.0.177 | 8GB | 2 cores   | 50GB    | Active  | SIEM + Detection    |
| Windows Endpoint | 192.168.0.175 | 8GB | 2 cores   | 120GB   | Active  | Telemetry + Testing |
| n8n+TheHive      | 192.168.0.185 | 8GB | 2 cores   | 50GB    | Active  | SOAR + AI Analysis + Telegram       |
| Kali Linux       | TBD          | 8GB | 2 cores       | 60GB     | Planned | Penetration Testing Project     |

## Network Communication

| Source | Destination | Port | Protocol | Purpose |
|--------|-------------|------|----------|---------|
| Windows (192.168.0.175) | Wazuh (192.168.0.177) | 1514 | TCP/UDP | Agent connection (event forwarding) |
| Windows (192.168.0.175) | Wazuh (192.168.0.177) | 55000 | TCP | 	Agent enrollment/registration |
| Wazuh (192.168.0.177) | n8n (192.168.0.185) | 5678 | HTTP | 	Webhook alerts (JSON payload) |
| n8n (192.168.0.185) | DeepSeek API | 443 | HTTPS | AI analysis for alert triage |
| n8n (192.168.0.185) | Telegram API | 443 | HTTPS | Instant notifications to SOC channel |

## Active Detection Rules (MITRE ATT&CK Mapped)

| Rule ID | MITRE Tactic | MITRE Technique | Description | Alert Level |
|---------|--------------|-----------------|-------------|-------|
| **100001** | Execution (TA0002) | T1059.001 | Detects encoded/obfuscated PowerShell commands | 8 (High) |
| **100002** | Credential Access (TA0006) | T1003.001 | Detects Mimikatz/LSASS process access attempts | 14 (Critical) |
| **100003** | Defense Evasion (TA0005) | T1562.001 | Detects attempts to disable Windows Defender | 12 (Critical) |
| **100004** | Persistence (TA0003) | T1053.005 | Detects unauthorized scheduled task creation | 8 (High) |
| **100005** | Command & Control (TA0011) | T1095 | Detects suspicious C2 communication patterns | 12 (Critical) |

