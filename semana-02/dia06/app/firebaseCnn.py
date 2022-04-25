## Para conectarse a FireBase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("app/credentials/token-firebase.json")
firebase_admin.initialize_app(cred)

### Para conectarse a firestore
from firebase_admin import firestore

db = firestore.client()