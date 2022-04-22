from multiprocessing import context
from flask import Flask, render_template, request
import requests

URL = 'https://api.github.com/users/odriverar'


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("tokenfirebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    # return '<center> <h1> BIENVENIDO A MI SITIO WEB </h1> </center>'
    # nombre = request.args.get('nombre', 'no hay nombre')
    data = requests.get(URL)
    context = data.json()
    print(context)
    return render_template('home.html', **context)

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
    
    # print(docProyectos)
    
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