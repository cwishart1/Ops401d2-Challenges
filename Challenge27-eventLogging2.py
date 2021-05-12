#!/usr/bin/env python3

# Script Name:                  Challenge27-eventLogging2
# Class Name:                   Ops 401
# Author Name:                  Cody Wishart
# Date of latest revision:      5/11/21
# Purpose:                      Implement logging into encryption tool

#### Functions 5 and 6 do NOT work, need os walk ####

# Import lib
from cryptography.fernet import Fernet
from logging.handlers import RotatingFileHandler
import os, logging

# Global var # Not sure if this section is needed, will review on next version #
check1 = ()
key = ()
f = ()

# Create key
def writeKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyFile:
        keyFile.write(key) 

# Load key
def loadKey():
    return open("key.key", "rb").read()

# Preform cryptographic operation based on $check1 
def crypt(check):
    key = loadKey()
    f = Fernet(key)
    if check == 1: #encrypt file
        toEncrypt0 = input("Enter file's directory to be encrypted: ")
        with open(toEncrypt0, 'rb') as originalFile:
            original = originalFile.read()
        encrypt0 = f.encrypt(original) 
        with open('encryptedFile', 'w') as encryptedFile:
            encryptedFile.write(str(encrypt0.decode('utf-8')))
        os.remove(toEncrypt0)
    elif check == 2: #decrypt file
        toDecrypt0 = input("Enter file's directory to be decrypted: ")
        with open(toDecrypt0, 'rb') as originalFile:
            original1 = originalFile.read()
        decrypt0 = f.decrypt(original1)
        with open('decryptedFile', 'w') as decryptedFile:
            decryptedFile.write(str(decrypt0.decode('utf-8')))
        os.remove(toDecrypt0)
    elif check == 3: #encrypt msg
        toEncrypt1 = input("Enter message to be encrypted: ")
        x2 = toEncrypt1.encode()
        encrypt1 = f.encrypt(x2)
        print ("Encrypted message:")
        print (encrypt1.decode('utf-8'))
    elif check == 4: #decrypt msg
        toDecrypt = input("Enter message to be decrypted: ")
        x3 = toDecrypt.encode()
        decrypt1 = f.decrypt(x3)
        print ("Decrypted message:")
        print (decrypt1.decode('utf-8'))
    elif check == 5: #encrypt a dir
        dDir = input("Enter directory to be encrypted: ")
        dirs = os.listdir(path=dDir)
        for files in dirs:
            with open(files, 'rb') as originalFile:
                original = originalFile.read()
            encrypt0 = f.encrypt(original) 
            with open('encryptedFile', 'w') as encryptedFile:
                encryptedFile.write(str(encrypt0.decode('utf-8')))
            os.remove(files)
    elif check == 6: #decrypt a dir
        eDir = input("Enter directory to be decrypted: ")
        dirs = os.listdir(path=eDir)
        for files in dirs:
            with open(toDecrypt0, 'rb') as originalFile:
                original1 = originalFile.read()
            decrypt0 = f.decrypt(original1)
            with open('decryptedFile', 'w') as decryptedFile:
                decryptedFile.write(str(decrypt0.decode('utf-8')))
            os.remove(toDecrypt0)
    else: #tiny bit of input sanitization
        print ("Invalid input")

# Initialize UI
def init():
    check0 = input("Do you want to generate a new keyfile? WARNING: will overwrite old keyfile!\n(y/n): ")
    if check0 == 'y':
        print ("Generating key")
        writeKey()
    check1 = input("\nEncrypt a file (1)\nDecrypt a file (2)\nEncrypt a message (3)\nDecrypt a message (4)\nEncrypt a directory (5)\nDecrypt a directory (6)\nWhat operation would you like to preform? (1-4): ")
    crypt(int(check1))


# Main

# Logging System
logger = logging.getLogger('my_logger')
handler = RotatingFileHandler('log.log', maxBytes=200, backupCount=200) 
logger.addHandler(handler)

logging.basicConfig(filename='./log.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
print ('Logging initialized')
logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.critical('Critical Error')

init()
