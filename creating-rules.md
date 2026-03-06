# Rule 100001 - PowerShell Download Detection (T1059.001)

```bash
<group name="execution,powershell,download,custom,">
  <rule id="100001" level="8">
    <if_group>windows|sysmon</if_group>
    <field name="win.eventdata.image" type="pcre2">(?i)powershell\.exe|pwsh\.exe</field>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)Invoke-WebRequest|iwr|curl|wget|Net\.WebClient|DownloadFile|DownloadString</field>
    <description>Execution - PowerShell Download Detected</description>
    <mitre>
      <id>T1059.001</id>
    </mitre>
  </rule>
</group>
```

What it detects: PowerShell downloading files from the internet (common malware staging technique)

## Test Command:

```bash
Invoke-AtomicTest T1059.001
```

powershell -Command "Invoke-WebRequest -Uri 'https://example.com' -OutFile C:\temp\test.txt"
# Rule 100002 - Mimikatz Credential Dumping (T1003.001)
xml
<group name="credential-access,mimikatz,critical,custom,">
  <rule id="100002" level="14">
    <if_group>windows|sysmon</if_group>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)sekurlsa::logonpasswords|lsadump::|privilege::debug</field>
    <description>Mimikatz Credential Dumping Detected</description>
    <mitre>
      <id>T1003.001</id>
    </mitre>
  </rule>
</group>
What it detects: Mimikatz commands used to dump passwords from memory

Test Command (safe simulation):

powershell
echo "sekurlsa::logonpasswords" > C:\temp\test.txt
# Rule 100003 - Windows Defender Disable Attempt (T1562.001)
xml
<group name="defense-evasion,defender-tampering,critical,custom,">
  <rule id="100003" level="12">
    <if_group>windows|sysmon</if_group>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)(Set-MpPreference|Add-MpPreference|Remove-MpPreference).*(DisableRealtimeMonitoring|DisableBehaviorMonitoring|DisableBlockAtFirstSeen|DisableIOAVProtection|DisablePrivacyMode)</field>
    <description>Windows Defender Disable Attempt</description>
    <mitre>
      <id>T1562.001</id>
    </mitre>
  </rule>
</group>
What it detects: Attackers trying to turn off Windows Defender

Test Command (safe version - doesn't actually disable):

powershell
powershell -Command "Get-MpPreference | Select-Object DisableRealtimeMonitoring"
# Rule 100004 - Scheduled Task Persistence (T1053.005)
xml
<group name="persistence,scheduled-task,custom,">
  <rule id="100004" level="8">
    <if_group>windows|sysmon</if_group>
    <field name="win.eventdata.image" type="pcre2">(?i)schtasks\.exe</field>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)/create</field>
    <description>Potential Persistence - Scheduled Task Created</description>
    <mitre>
      <id>T1053.005</id>
    </mitre>
  </rule>
</group>
What it detects: Creation of scheduled tasks (common persistence mechanism)

Test Command:

powershell
schtasks /create /tn "TestTask" /tr "calc.exe" /sc once /st 00:00 /f
# Rule 100005 - Netcat C2 Connection (T1095)
xml
<group name="command-and-control,netcat,c2,critical,custom,">
  <rule id="100005" level="12">
    <if_group>windows|sysmon</if-group>
    <field name="win.eventdata.eventID">1</field>
    <field name="win.eventdata.image" type="pcre2">(?i)(ncat|nc)\.exe</field>
    <field name="win.eventdata.commandLine" type="pcre2">(?i)\d+\.\d+\.\d+\.\d+\s+\d+</field>
    <description>C2 - Netcat Connection Detected (T1095)</description>
    <mitre>
      <id>T1095</id>
    </mitre>
  </rule>
</group>
What it detects: Netcat/ncat connections used for C2 communication

Test Command (if netcat installed):

powershell
nc.exe -e cmd.exe 127.0.0.1 4444
