from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status':'Ok',
        'mensaje': 'Bienvenido a mi apirest con Flask'
    })
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)