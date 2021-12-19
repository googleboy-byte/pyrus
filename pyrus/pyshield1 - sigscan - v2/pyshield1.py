
import glob
import re
import sys
import pereader

while True:

    print("\n\n\n######### SCANNING FOR VIRUS SIGNATURES #########\n\n\n")
   
    try:
        filetoscan = sys.argv[1]
        signature = sys.argv[2]
    except:
        print("PROVIDE PROPER ARGUMENTS. FIRST ARGUMENT AFTER PROGRAM NAME SHOULD BE THE TARGET FILE TO SCAN AND THE NEXT SHOULD BE THE SIGNATURE TO LOOK FOR IN THE CODE OF THE FILE.")
    try:
        scantarget = open(filetoscan, "r", encoding="latin-1")
        scantargetcontent = scantarget.readlines()
        scantarget.close()
    except:
        scantarget = open(filetoscan, "r", encoding="utf-8")
        scantargetcontent = scantarget.readlines()
        scantarget.close()

    filecontainsvsig = False
    
    pe = pereader.PE(filetoscan)

    codedatafile = open(filetoscan+".txt", "a")
    codedatafile.write(str(scantargetcontent))
    codedatafile.close()
    
    #print(pe)
    
    
    #print(scantargetcontent)
    for line in scantargetcontent:
        if re.search(signature, line):
            print("\nTHIS FILE CONTAINS VIRUS SIGNATURE")
            filecontainsvsig = True
            break
    if filecontainsvsig == False:
        print("\nTHIS FILE DOESN\'T CONTAIN VIRUS SIGNATURE")


    print("\n\n\n######### SCANNING FINISHED #########")

    print("\n######### PROBABLE INTERESTING METADATA PIECES #########\n")
    for entry in pe.directory_entry_resource.resource_directory.entries:
        if entry.RESOURCE_DIRECTORY_ENTRY.str_Type == 'RT_STRING':
            for k in entry.strings:
                print(k, entry.strings[k])
                print("\n")
    
    for entry in pe.directory_entry_resource.resource_directory.entries:
        if entry.RESOURCE_DIRECTORY_ENTRY.str_Type == 'RT_VERSION':
            version = entry.version

            for e in version.stringfileinfo:
                for stringtable in e.stringtables:
                    for string in stringtable.strings:
                        print(string.str_szKey, string.str_Value)

            for e in version.varfileinfo:
                for var in e.vars:
                    for w1, w2 in var.translations:
                        print(w1, w2)
    print("\n##################\n")
    break
