#### LIBRERIA DE ALUMNOS

############## FUNCIONES ##############
def menu():
    print("-" * 52)
    print("|" + " " * 10 + "MATRICULA DE ALUMNOS EN CODIGO" + " " * 10 + "|")
    print("-" * 52)
    print("|" + " " * 10 + "MENU DE OPCIONES              "  + " " * 10 + "|")
    print("|" + " " * 10 + "[1] REGISTRAR ALUMNO          "  + " " * 10 + "|")
    print("|" + " " * 10 + "[2] MOSTRAR ALUMNO            "  + " " * 10 + "|")
    print("|" + " " * 10 + "[3] ACTUALIZAR ALUMNO         "  + " " * 10 + "|")
    print("|" + " " * 10 + "[4] ELIMINAR ALUMNO           "  + " " * 10 + "|")
    print("|" + " " * 10 + "[5] SALIR                     "  + " " * 10 + "|")
    print("-" * 52)
    
def buscarAlumno(valorBusqueda, alumnos):
    indexAlumno = -1
    for i in range(len(alumnos)):
        dicAlumnoBusqueda = alumnos[i]
        for clave, valor in dicAlumnoBusqueda.items():
            if valor == valorBusqueda and clave == 'email':
                indexAlumno = i
                break
    return indexAlumno

def insertarAlumno(alumnos):
    nombre =  input("Nombre   : ")
    email =   input("Email    : ")
    celular = input("Celular  : ")
    dictAlumno = {
        'nombre': nombre,
        'email': email,
        'celular': celular,
    } 
    alumnos.append(dictAlumno)
    print("ALUMNO REGISTRADO CON EXITO!!!")
    
def actualizarAlumno(indexAlumno, alumnos):
    nombre =  input("Nombre   : ")
    email =   input("Email    : ")
    celular = input("Celular  : ")
    dictAlumno = {
        'nombre': nombre,
        'email': email,
        'celular': celular,
    } 
    alumnos[indexAlumno] = dictAlumno
    print("ALUMNO ACTUALIZADO CON EXITO!!!")

def eliminarAlumno(indexAlumno, alumnos):
    alumnos.pop(indexAlumno)
    print("ALUMNO ELIMINADO CON EXITO!!!")
    
def cargarAlumnos():
    f = open('alumnos.txt', 'r')
    strAlumnos = f.read()
    
    alumnos = []
    #Proceso de convcersion, el mismo que convertira una cadena string en una lista de diccionarios
    listaAlumnos = strAlumnos.splitlines()
    for l in listaAlumnos:
        alumnoData = l.split(',')
        dictAlumno = {
            'nombre': alumnoData[0],
            'email': alumnoData[1],
            'celular': alumnoData[2],
        }
        alumnos.append(dictAlumno)
    f.close
    return alumnos

def grabarAlumnos(alumnos):
    f = open('alumnos.txt', 'w')
    strAlumnos = ""
    c = 1
    for l in alumnos:
        for clave, valor in l.items():
            strAlumnos += valor
            if clave != 'celular':
                strAlumnos += ','
            elif clave == 'celular':
                strAlumnos += '\n'
    f.write(strAlumnos)
    f.close
    return strAlumnos    
#######################################