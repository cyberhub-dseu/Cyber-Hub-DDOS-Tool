## Cyber Hub DDoS Tool (CHDT)

### Description:
The **Cyber Hub DDoS Tool (CHDT)** is an educational tool designed to demonstrate how a Distributed Denial of Service (DDoS) attack can flood a target using ICMP packets. The tool supports multi-threaded execution and allows launching multiple instances across terminals, making it suitable for simulating various levels of attack intensities.

> **Disclaimer**: This tool is strictly for educational purposes and network testing. Unauthorized use against systems without consent is illegal. Use responsibly.

### Features:
- **Custom ICMP Packet Creation**: Manually constructs ICMP echo request packets for precise flooding.
- **Multi-Threading**: Users can choose the number of threads to launch based on attack intensity (normal, medium, high, or custom).
- **ASCII Banner with `pyfiglet`**: Displays a fun, artistic banner when the script starts.
- **Multiple Terminal Windows**: Launches multiple instances of the tool to scale attacks across different windows.
- **Cross-Platform Support**: Compatible with Linux, macOS, and Windows.

### Purpose:
This tool is designed to educate security professionals, ethical hackers, and students about DDoS vulnerabilities and protection techniques. It simulates how attackers might perform an ICMP flood attack and provides insight into traffic handling and server load testing.


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
