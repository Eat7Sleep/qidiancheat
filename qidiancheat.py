import os
import time


def tap(cursor_x, cursor_y):
    cmd = 'adb shell input tap '+str(cursor_x)+' '+str(cursor_y)
    os.system(cmd)

while(1):
    tap(0, 0)
    time.sleep(10)




