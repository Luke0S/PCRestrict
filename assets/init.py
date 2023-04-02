import time
import json
import os

def add_process():
    while not os.path.exists("./values/global.json"):
        time.sleep(1)

    if os.path.isfile("./values/global.json"):
        pid = os.getpid()
        with open("./values/global.json", 'r+') as file:
            file_data = json.load(file)
            file_data["pid"].append(pid)
            file.seek(0)
            json.dump(file_data, file, indent=4)

add_process()

while True:
    time.sleep(5)
    print("ALIVE")