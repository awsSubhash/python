# 

import time
import requests

def ping():
    while True:
        repose = requests.get("https://google.com")
        print(repose.status_code)
        time.sleep(1)

ping()




