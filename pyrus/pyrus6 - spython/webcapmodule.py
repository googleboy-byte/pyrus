import cv2
from datetime import datetime
from threading import Timer
import time

def web_cap(imgsavename):
    
    cam = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = cam.read()
        cv2.imwrite(imgsavename,frame)
        result = False
    cam.release()
    cv2.destroyAllWindows()
    print("img taken\n")
    
def web_cap_main(x):
    for i in range(x):
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        time.sleep(1)
        web_cap("caps\\" + dt_string + ".jpg")

web_cap_main(5)
