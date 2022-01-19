import os
import time



def go():
    start = input('Start ')
    end = input('End ')
    add = input('Add ')
    for name in os.listdir():
        if name.startswith(start) and name.endswith(end):
            num = name.split(".")
            num[0] += add
            st = str(num[0] + '.' + num[1])
            os.rename(name, st)
            time.sleep(0.5)

