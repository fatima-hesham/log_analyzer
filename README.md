# Log Analyzer Tool

A Python tool for parsing Windows Event Logs (EVTX XML) to detect login activity. Designed for SOC analysts and cybersecurity learners.

## Features
- Detects:
  - Failed login attempts (Event ID 4625)
  - Successful logins (Event ID 4624)
  - Account lockouts (Event ID 4740)
- Supports EVTX XML export from Event Viewer

## Requirements
- Python 3.x
- XML logs exported from Windows Event Viewer

##  Usage

```bash
python log_analyzer.py Security.evtx.xml
