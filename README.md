# Cyber Hub DDoS Tool (CHDT)

This project is a simple ICMP flood tool designed for educational purposes. It allows users to flood a target IP with ICMP packets using multiple threads and windows.

**Disclaimer: This tool is for educational purposes only. Misuse of this tool for malicious purposes is illegal.**

## Features
- Custom ICMP packet creation
- Multi-threaded execution
- ASCII banner using `pyfiglet`
- Ability to launch multiple terminal windows
- Adjustable attack intensity

## Installation

### Requirements
- Python 3.x
- `pyfiglet` library
- Administrator/root access (due to raw socket usage)

### Install dependencies:
```bash
pip install pyfiglet

Run the tool:
python chdt.py
Usage:
Enter a target domain or IP and select the attack intensity (Normal, Medium, High, or Custom).
python chdt.py
