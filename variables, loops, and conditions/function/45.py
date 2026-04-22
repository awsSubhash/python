# check cpu

import time
import psutil

def cpu():
    cpu_uses = psutil.cpu_percent(interval=1)
    if cpu_uses > 9:
        print("your cpu uses is high")
    else:
        print("your cpu uses is normal")
    time.sleep(10)

while True:
    cpu()
    time.sleep(10)
