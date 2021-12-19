import os, re, win32api, sys
import curses

stdscr = curses.initscr()

def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            stdscr.addstr(0, 0, "SEARCHING:    %s\r" % root)
            stdscr.refresh()
            if result:
                print("\n######### FILE FOUND #########\n")
                print(os.path.join(root, f))
                break # if you want to find only 

def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )


#find_file_in_all_drives(sys.argv[1]) #for all drives
find_file("C:\\users\\User\\", re.compile(sys.argv[1]))
#python widerfilesearch.py "EnglishX.pdf"
