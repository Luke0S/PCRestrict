import time
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore

#Firebase
cred = credentials.Certificate("./assets/secure/firebaseKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('core')

while True:

    now = datetime.now()

    current_time_H = now.strftime("%H")
    current_time_M = now.strftime("%M")

    time.sleep(5)

    res = collection.document('values').get().to_dict()
    print(res['pc_enabled'])



