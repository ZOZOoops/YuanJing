import time
import datetime

def time_sj():
    sj = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(sj)
    return sj