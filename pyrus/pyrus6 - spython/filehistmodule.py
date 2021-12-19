import subprocess
import sys

LOCATION = "dir %userprofile%\AppData\Roaming\Microsoft\Windows\Recent"

with open("rcntfiles\\recent_files.txt", 'a') as f:
    result1 = subprocess.check_output(LOCATION, shell=True)
    result = result1.decode('utf-8')
    f.write(result)
