import time
import os
import json

#import firebase_admin
#from datetime import datetime
#from firebase_admin import credentials
#from firebase_admin import firestore

#Firebase
#cred = credentials.Certificate("./assets/secure/firebaseKey.json")
#firebase_admin.initialize_app(cred)
#db = firestore.client()
#collection = db.collection('core')

pid = os.getpid()

a_file = open("./values/global.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)

json_object["pid"] = pid

a_file = open("./values/global.json", "w")
json.dump(json_object, a_file)
a_file.close()

while True:

   # now = datetime.now()

   # current_time_H = now.strftime("%H")
    #current_time_M = now.strftime("%M")
   time.sleep(5)

   print("HI!!")

   # res = collection.document('values').get().to_dict()
    #print(res['pc_enabled'])



