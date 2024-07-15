#!/usr/bin/env python3

import sys
import subprocess

# Get the target IP address and port range from the main script
TARGET_IP = sys.argv[1]
PORT_RANGE = sys.argv[2]
OUTPUT_DIR = sys.argv[3]

# Define the output file
PORT_SCAN_OUTPUT = f"{OUTPUT_DIR}/port_scan.txt"

# Run the port scan using Nmap
print(f"Running port scan on {TARGET_IP} for ports {PORT_RANGE}...")
subprocess.run(["nmap", "-p", PORT_RANGE, TARGET_IP, "-oN", PORT_SCAN_OUTPUT], check=True)

print(f"Port scan output: {PORT_SCAN_OUTPUT}")
