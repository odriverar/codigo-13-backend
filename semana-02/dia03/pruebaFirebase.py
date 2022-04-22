## Para conectarse a FireBase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token-firebase.json")
firebase_admin.initialize_app(cred)

### Para conectarse a firestore
from firebase_admin import firestore
db = firestore.client()

colProyectos = db.collection('proyectos')
docProyectos = colProyectos.get()

for doc in docProyectos:
    print(doc.to_dict())

