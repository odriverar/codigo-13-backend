from multiprocessing import context
from flask import Flask, render_template, request, session

## Para conectarse a FireBase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token-firebase.json")
firebase_admin.initialize_app(cred)

### Para conectarse a firestore
from firebase_admin import firestore
db = firestore.client()
    
app = Flask(__name__)
## creamos una clave secreta para las variables de sesion.
app.secret_key = 'ClavesecretA123456'

@app.route('/')
def index():
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    for doc in docBiografia:
        dicBiografia = doc.to_dict()
        
    colEnlace = db.collection('enlaces')
    docEnlace = colEnlace.get()

    lstEnlaces = []
    for doc in docEnlace:
        dicEnlace = doc.to_dict()
        lstEnlaces.append(dicEnlace)
    
    session['biografia'] = dicBiografia
    session['enlace'] = lstEnlaces
    
    return render_template('home.html')

@app.route('/peliculas')
def peliculas():
    nombre = request.args.get('nombre', 'no hay nombre')
    listaPeliculas = ['CODA', 'ENCANTO', 'SONIC 2']
    context = {
        'nombre': nombre,
        'peliculas': listaPeliculas,
    }
    return render_template('peliculas.html', **context)


@app.route('/acercade')
def about(): 
    return render_template('acercade.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/portafolio')
def portafolio(): 
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()

    lstProyectos = []
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)   
    
    context = {
        'proyectos': lstProyectos
    }
    
    return render_template('portafolio.html', **context)
        
app.run(debug = True)