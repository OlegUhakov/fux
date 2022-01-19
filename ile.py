import os
import time



def ile():
    start_del = input('Start ')
    end_del = input('End ')
    num = int(input('How many remove? '))
    for name in os.listdir():
        if name.startswith(start_del) and name.endswith(end_del):
            call = name.split(".")
            call_zero = str(call[0])
            call_two = str(call[1])
            zero = call_zero[:-num]
            st = zero + '.' + call_two
            os.rename(name, st)
            time.sleep(0.5)

