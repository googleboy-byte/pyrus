######### importing required libs

import glob
import re
import sys

#########

while True:
    
######### scanning potential targets

    print("\n\n\n######### SCANNING FOR VIRUS SIGNATURES #########\n\n\n")
    try:
        potentials = glob.glob(sys.argv[1] + "\\*.py") # taking the directory to scan as the first argument
    except:
        print("A relative or superlative folder address is required as the first argument to scan")
        break

    for potentialfile in potentials:
        infected = False # infected bool

        ######### checking for infection signature in file

        file = open(potentialfile, "r")
        lines = file.readlines()
        file.close()
        try:
            for line in lines:
                
                if re.search("%s" % sys.argv[2], line): # scanned for virus signature in each line of the code..... this is a line unique to this virus which usually helps in identifying the start or end of the virus....this one is unique to the pyrus1 - replicaload
                    print("!!!!!INFECTED FILE:    %s" % potentialfile)
                    infected = True

                if infected == False:
                    print("CLEAN FILE:    %s" % potentialfile)

                break
        except IndexError:
            print("The signature is needed to be given as the second argument to the program.")
            break
        #########
    print("\n\n\n######### SCANNING FINISHED #########")
    break
