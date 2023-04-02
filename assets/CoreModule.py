import time
import os
import json

# import firebase_admin
# from datetime import datetime
# from firebase_admin import credentials
# from firebase_admin import firestore

# Firebase
# cred = credentials.Certificate("./assets/secure/firebaseKey.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()
# collection = db.collection('core')




def add_process():
   pid = os.getpid()
   with open("./values/global.json", 'r+') as file:
        file_data = json.load(file)
        file_data["pid"].append(pid)
        file.seek(0)
        json.dump(file_data, file, indent=4)


add_process()

while True:
    # now = datetime.now()

    # current_time_H = now.strftime("%H")
    # current_time_M = now.strftime("%M")
    time.sleep(5)

    print("HI!!")

    # res = collection.document('values').get().to_dict()
    # print(res['pc_enabled'])
