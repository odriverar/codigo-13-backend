from flask import Flask, render_template, request, session

from . import portafolio

## Para conectarse a FireBase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("app/credentials/token-firebase.json")
firebase_admin.initialize_app(cred)

### Para conectarse a firestore
from firebase_admin import firestore

db = firestore.client()


@portafolio.route('/')
def home():
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
    
    return render_template('portafolio/home.html')

@portafolio.route('/proyectos')
def proyectos():
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
    
    return render_template('portafolio/portafolio.html', **context)

@portafolio.route('/acercade')
def about(): 
    return render_template('portafolio/acercade.html')

@portafolio.route('/contacto')
def contacto():
    return render_template('portafolio/contacto.html')