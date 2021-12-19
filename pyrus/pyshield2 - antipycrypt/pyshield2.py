import glob
from cryptography.fernet import Fernet

potentialaffected = glob.glob("*.key.key") # identifying key files to find potential targets for decryption

for affected in potentialaffected:# trying to decrypt each potebtial target
    try:
        affectedfile = open(affected.replace(".key.key", ""), "rb") # seeing if a file exists in correspondence with the key file
        affectedcode = affectedfile.read() # reading encryoted binary from fule
        affectedfile.close()

        keyfile = open(affected, "rb")
        key = keyfile.read() # reading the key from the keyfile
        keyfile.close()

        fernet = Fernet(key) # fernetting key

        d3crypteddata = fernet.decrypt(affectedcode) # decrypting data with fernet 

        affectedfile = open(affected.replace(".key.key", ""), "wb")
        affectedfile.write(d3crypteddata) # writing decrypted data back to file
        affectedfile.close()

    except:
        pass

