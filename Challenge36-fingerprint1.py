#! /usr/bin/env python3

# Script Name:                  Challenge36-fingerprint1
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      5/24/21
# Purpose:                      Perform banner grab on target site

# Import Lib
import os

# Main
address = input("Enter URL or IP address: ")
port = input("Enter port number: ")
print("\nFingerprinting using Netcat:\n")
os.system(f"nc {address} {port}")
print("\nFingerprinting using Telnet:\n")
os.system(f"telnet {address} {port}")
print("\nFingerprinting using Nmap:\n")
os.system(f"nmap -Pn -p 1-1023 -sV --script=banner {address}")
