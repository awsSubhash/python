import psutil
import os
import time

def memory():
    process = psutil.Process(os.getpid())
    memory_uses = process.memory_info().rss / (1024 * 1024)  # MB

    if memory_uses > 20:
        print("Memory usage is high:", memory_uses, "MB")
    else:
        print("Don't worry, memory usage is low:", memory_uses, "MB")

while True:
    memory()
    time.sleep(10)
