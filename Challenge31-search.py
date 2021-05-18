#!/usr/bin/env python3

# Script Name:                  Challenge31-search
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      5/17/21
# Purpose:                      Search for an inputted file in an inputed dir

# This requires the tree command to be installed on Linux which isn't preinstalled
# Install using 'sudo apt install tree'


# Import Lib
import os, platform

# Function
def search ():
    
    targetFile = input("Enter file to search for: ")
    targetDir = input("Enter directory to search in (leave blank for current dir): ")
    host = platform.system()

    if host == 'Linux':
        treeCMD = "tree -afi " + targetDir + " > temp.txt"
        matchesCMD = "cat temp.txt | grep " + targetFile
        os.system(treeCMD)
        
        print("\nPositive matches:")
        os.system(matchesCMD)

        print("\nAreas searched:")
        os.system("cat temp.txt | grep directories,")
        
        os.remove("temp.txt")

    elif host == 'Windows':
        for (root, dirs, files) in os.walk(targetDir):
            for d in dirs:
                cmd1 = "echo " + os.path.join(root, d) + " >> dirs.txt"
                os.system(cmd1)   
            for f in files:
                cmd2 = "echo " + os.path.join(root, f) + " >> files.txt"
                os.system(cmd2)

        cmd = "cat ./files.txt | Select-String -Pattern " + targetFile
        print("\nPositive matches")
        os.system(cmd)

        with open("files.txt") as f:
            fileNum = 0
            for line in f:
                fileNum += 1

        with open("dirs.txt") as f:
            dirNum = 0
            for line in f:
                dirNum += 1

        print("\nAreas searched:")
        print(str(dirNum) + " directories, " + str(fileNum) + " files")
            
        os.remove("dirs.txt")
        os.remove("files.txt")

    else:
        print("Incompatible operating system... quitting")


# Main
search()
