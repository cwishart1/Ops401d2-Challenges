#!/usr/bin/env python3

# Script Name:                  Challenge41-portScanner
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      6/4/21
# Purpose:                      Determine port status

# Crashes when port is closed. Using 'try' with an exception would fix that but would go out of bounds of the given template.
# Perhaps 'sockmod.connect' wasn't the intended function but eh

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 3
sockmod.settimeout(timeout)

hostip = input("Enter target IP: ")
portno = input("Enter target port: ")

def portScanner(portno):
    if sockmod.connect((hostip, portno)): 
        print("Port closed")
    else:
        print("Port open")

portScanner(int(portno))
