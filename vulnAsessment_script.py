import sys
import subprocess
import re

# Get the target IP address, port range, vulnerability scanner, and output directory from the main script
TARGET_IP = sys.argv[1]
PORT_RANGE = sys.argv[2]
VULNERABILITY_SCANNER = sys.argv[3]
OUTPUT_DIR = sys.argv[4]

# Define the port scan output file
PORT_SCAN_OUTPUT = f"{OUTPUT_DIR}/port_scan.txt"

# Define the vulnerability scan output file
VULNERABILITY_SCAN_OUTPUT = f"{OUTPUT_DIR}/vulnerability_scan.txt"

# Read the port scan results
with open(PORT_SCAN_OUTPUT, 'r') as file:
    port_scan_results = file.read()

# Extract the open ports from the port scan results
open_ports = re.findall(r'open\s+(\d+)/tcp', port_scan_results)

# Run the vulnerability scan using Nmap
print(f"Running vulnerability scan on {TARGET_IP} for open ports: {', '.join(open_ports)}...")
subprocess.run([VULNERABILITY_SCANNER, "-sV", "-p", ",".join(open_ports), TARGET_IP, "-oN", VULNERABILITY_SCAN_OUTPUT], check=True)

print(f"Vulnerability scan output: {VULNERABILITY_SCAN_OUTPUT}")
