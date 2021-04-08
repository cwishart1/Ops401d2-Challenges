#!/usr/bin/env python3

# Script Name:                  Challenge2-ICMPdetector2
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      4/6/21
# Purpose:                      Use ICMP to determine if a host is online, send gmail alerts if status changes

# Import libraries
import os, time, datetime, smtplib

# Mail setup and login
server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
#server.ehlo()
server.login('tt4626970@gmail.com', 'po-ta-tos boil em mash em stick em in a stew')
destination = input("Input gmail address to send alerts to: ")

# Variable
targetIp = input("Enter target computer's IP address: ")
upt = int(3)

# Main
while True:
    now = str(datetime.datetime.now())
    check = os.system("ping -c 1 " + targetIp + " > ohyeah.txt") 
    with open('ohyeah.txt') as file:
        contents = file.read() 
        if '1 received' in contents:
            msgUp = (now + " Network Active to " + targetIp)
            print (msgUp)
            if upt == 0:
                server.sendmail('tt4626970@gmail.com', destination, msgUp)
                upt == 1
        else:
            msgDown = print(now + " Network Inactive to " + targetIp)
            print (msgDown)
            if upt == 1:
                server.sendmail('tt4626970@gmail.com', destination, msgDown)
                upt == 0
    time.sleep(5)

# End
