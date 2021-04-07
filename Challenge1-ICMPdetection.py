#!/usr/bin/env python3

# Script Name:                  Challenge6-listPractice
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      4/6/21
# Purpose:                      Use ICMP to determine if a host is online

# Import libraries
import os
import time
import datetime

# Variable
targetIp = input("Enter target computer's IP address: ")

# Main
while True:
    now = datetime.datetime.now()
    check = os.system("ping -c 1 " + targetIp + " > ohyeah.txt") 
    with open('ohyeah.txt') as file:
        contents = file.read() 
        if '1 received' in contents:
            print (now," Network Active to ",targetIp)
        else:
            print (now," Network Inactive to ",targetIp)
    time.sleep(5)

# End
