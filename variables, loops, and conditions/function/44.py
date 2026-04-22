import requests
import time

#while True:
 #  print(requests.get("https://google.com").status_code)
  # time.sleep(60)


def api(url):
    response = requests.get(url)
    status_code = response.status_code
    time.sleep(60)
    print(status_code)
    return status_code


a = input("enter any url")

print(api(a))

