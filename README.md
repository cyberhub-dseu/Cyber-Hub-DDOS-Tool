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

Here's a rewritten version for your `README.md` file:

```markdown
## Usage

### Clone the Repository
To get started, clone the repository using the following command:

```bash
git clone https://github.com/cyberhub-dseu/Cyber-Hub-DDOS-Tool.git
```

### Create and Activate a Virtual Environment
Next, create a virtual environment and activate it:

```bash
sudo apt install python3-venv
cd Cyber-Hub-DDOS-Tool
python3 -m venv venv
source venv/bin/activate
pip install setuptools
```

### Install Required Packages
After activating the virtual environment, install the required packages with:

```bash
pip install -r requirements.txt
```

### Run the Python Script
Finally, you can run the Python script using:

```bash
python chdt.py
```
