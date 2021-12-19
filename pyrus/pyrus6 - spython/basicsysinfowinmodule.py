import os
import sys
import subprocess

with open("basicsysinfowin\\sys_info_win.txt","a") as f:
        batcmd="systeminfo"
        result1 = subprocess.check_output(batcmd, shell=True)
        result = result1.decode('utf-8')
        f.write("SYSTEM INFO\n")
        f.write(result)
        batcmd1 = "ipconfig"
        result1 = subprocess.check_output(batcmd1, shell=True)
        result = result1.decode('utf-8')
        f.write("------------------------------------------------------")
        f.write("\nIP info \n")
        f.write(result)
        batcmd1 = "netsh wlan show profile"
        result1 = subprocess.check_output(batcmd1, shell=True)
        result = result1.decode('utf-8')
        f.write("------------------------------------------------------")
        f.write("\nCONNECTED HOTSPOT's HISTORY \n")
        f.write(result)
        batcmd1 = "netsh wlan show profiles"
        data = subprocess.check_output(batcmd1, shell=True).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        f.write('------------------------------------------------------')
        f.write('\nCONNECTED WIFI PASSWORDS\n')
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'], shell=True).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                f.write("\n{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                f.write("\n{:<30}|  {:<}".format(i, ""))
