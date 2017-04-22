import requests

with open("events.txt", "r") as f:
    for line in f.readlines():
        r = requests.post("http://localhost:5000/upload", data=line)
        if r.status_code != 200:
            print("error on post new log...")
            break
