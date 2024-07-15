#!/usr/bin/env python3

import os
import sys
import subprocess

# Prompt the user for the target IP address
TARGET_IP = input("Enter the target IP address: ")

# Prompt the user for the port range
PORT_RANGE = input("Enter the port range (e.g., 1-1024): ")

# Prompt the user for the vulnerability scanner
VULNERABILITY_SCANNER = input("Enter the vulnerability scanner (e.g., nmap): ")

# Prompt the user for the exploit tool
EXPLOIT_TOOL = input("Enter the exploit tool (e.g., metasploit): ")

# Prompt the user for the output directory
OUTPUT_DIR = input("Enter the output directory (e.g., /path/to/output): ")

# Define the port scan script
PORT_SCAN_SCRIPT = "port_scan.py"

# Define the vulnerability scan script
VULNERABILITY_SCAN_SCRIPT = "vulnerability_scan.sh"

# Define the exploit script
EXPLOIT_SCRIPT = "exploit.py"

# Create the output directory if it does not exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Run the port scan script
subprocess.run(["./" + PORT_SCAN_SCRIPT, TARGET_IP, PORT_RANGE, OUTPUT_DIR], check=True)

# Run the vulnerability scan script
subprocess.run(["./" + VULNERABILITY_SCAN_SCRIPT, TARGET_IP, VULNERABILITY_SCANNER, PORT_RANGE, OUTPUT_DIR], check=True)

# Run the exploit script
subprocess.run(["./" + EXPLOIT_SCRIPT, TARGET_IP, EXPLOIT_TOOL, OUTPUT_DIR], check=True)

print("Penetration testing tasks completed.")
