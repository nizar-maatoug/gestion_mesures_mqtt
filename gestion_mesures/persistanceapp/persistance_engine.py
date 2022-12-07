import pyrebase
import json
from datetime import datetime
# from website.models import Grandeur, Mesure


config={
    "apiKey": "AIzaSyCgfLQCFdUzLtnE-jKraOOOLY6yZal_pj0",
    "authDomain": "sensorsapp-13450.firebaseapp.com",
    "databaseURL": "https://sensorsapp-13450-default-rtdb.firebaseio.com",
    "projectId": "sensorsapp-13450",
    "storageBucket": "sensorsapp-13450.appspot.com",
    "messagingSenderId": "714436108961",
    "appId": "1:714436108961:web:3c567613af1cbab00546e0"
}

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
database=firebase.database()

def persistData(message):
    #Firebase: RealTime DB
    json_object = json.loads(message)
    json_object['time']= str(datetime.now())
    database.child('temperature').push(json_object)
    #SQLite
    # grandeur=Grandeur.objects.filter(nom="temperature")
    # mesure=Mesure(valeur=json_object['val'],datePrise=json_object['time'],grandeur=grandeur)
    # mesure.save()
