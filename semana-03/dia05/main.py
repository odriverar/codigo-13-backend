from crypt import methods
import json
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#### CONEXION A MYSQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB'] = 'db_colegio'

mysql = MySQL(app)

@app.route('/')
def index():
    return jsonify({
        'status': 'Ok',
        'mensaje': 'Bienvenido a mi apirest con Flask'
    })
    
@app.route('/alumno')
def getAlumno():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno")
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)    
    
    return jsonify({
        'ok': True,
        'message': 'Lista de alumnos',
        'content': data
    })
    
@app.route('/alumno', methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    celular = request.json['celular']
    github = request.json['github']
    
    cursor = mysql.connection.cursor()
    
    cursor.execute("insert into tbl_alumno(alumno_nombre, alumno_celular, alumno_github) values('" + nombre + "', '" + celular + "', '" + github + "')")
    
    mysql.connection.commit()
    
    cursor.close()
    
    return jsonify({
        'ok': True,
        'message': 'Registro insertado exitosamente'
    })
    
@app.route('/alumno/<id>')
def getAlumnoById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno where alumno_id = '" + id + "'")
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)    
    
    return jsonify({
        'ok': True,
        'message': 'Datos de un alumno',
        'content': data
    })
    
@app.route('/alumno/<id>', methods=['PUT'])
def updAlumno(id):
    nombre = request.json['nombre']
    email = request.json['email'] 
    celular = request.json['celular']
    github = request.json['github']
    
    cursor = mysql.connection.cursor()
    
    sqlUpdAlumno = "update tbl_alumno set alumno_nombre = '" + nombre + "', alumno_email = '" + email + "', alumno_celular = '" + celular + "', alumno_github = '" + github + "' where alumno_id = '" + id + "'"
    
    cursor.execute(sqlUpdAlumno)
    
    mysql.connection.commit()
    
    cursor.close()
    
    return jsonify({
        'ok': True,
        'message': 'Registro actualizado'
    })
    
@app.route('/alumno/<id>', methods=['DELETE'])
def delAlumno(id):
    try:    
        cursor = mysql.connection.cursor()
        
        sqlUpdAlumno = "delete from tbl_alumno where alumno_id = '" + id + "'"
        
        cursor.execute(sqlUpdAlumno)
        
        mysql.connection.commit()
        
        cursor.close()
        
        return jsonify({
            'ok': True,
            'message': 'Registro eliminado'
        })
    except Exception as err:
        return jsonify({
            'ok': False,
            'message': 'Error al ejecutar delete: ' + err.__str__()
        }), 401
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)