from unittest import result
from flask import Flask, request

# Creamos un objeto de la clase flask

app = Flask(__name__)

#Creamod mi primera ruta
@app.route('/')
def index():
    return '<center> <h1> HOLA MUNDO FLASK </h1> </center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre', 'no hay nombre')
    return '<center> <b> Hola {}</b> </center>'.format(nombre)

@app.route('/suma')
def suma():
    n1 = request.args.get('n1', '0')
    n2 = request.args.get('n2', '0')
    resultado = int(n1) + int(n2)
    return '<center> <h1> la suma de {} + {} es {} </h1> </center>'.format(n1, n2, resultado)

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0, n2=0):
    resultado = n1 - n2
    return '<center> <h1> la resta de {} - {} es {} </h1> </center>'.format(n1, n2, resultado)

# Desplegamos nuestra app web
app.run(debug = True)