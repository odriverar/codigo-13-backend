from multiprocessing import Value
import tabulate
# PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D 
from pickletools import OpcodeInfo


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

opcion = 0
alumnos = [{'nombre': 'David Rivera Robles', 'email': 'odriverar@gmail.com', 'celular': '987762000'}]
while (opcion != 5):
    opcion = int(input("INGRESE OPCIÓN MENU: "))
    if opcion == 1:
        print("NUEVO ALUMNO")
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
    elif opcion == 2:
        print()
        print("RELACIÓN DE ALUMNOS")
        print("-" * 52)
        numRegistros = len(alumnos)
        if numRegistros == 0:
            print("No existen registros")
            print("-" * 52)
        else:
            cabeceras = alumnos[0].keys()
            registros = [x.values() for x in alumnos]
            print(tabulate.tabulate(registros, cabeceras, tablefmt="psql"))
            print("Numero de registros: ", numRegistros)
    elif opcion == 3:
        print()
        print("ACTUALIZAR ALUMNO")
        print("-" * 52)
        valorBusqueda = input("Ingrese el email del alumno a actualizar: ")
        indexAlumno = -1
        for i in range(len(alumnos)):
            dicAlumnoBusqueda = alumnos[i]
            for clave, valor in dicAlumnoBusqueda.items():
                if valor == valorBusqueda:
                    indexAlumno = i
                    break
        if indexAlumno == -1:
            print("No se encontro el email del alumno, favor de verificar")
        else:
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
    elif opcion == 4:
        print()
        print("ELIMINAR ALUMNO")
        print("-" * 52)
        if len(alumnos) == 0:
            print("No existen registros")
            print("-" * 52)
        else:
            valorBusqueda = input("Escriba el nombre del alumno a eliminar: ")
            indexAlumno = -1
            for i in range(len(alumnos)):
                dicAlumnoBusqueda = alumnos[i]
                for clave, valor in dicAlumnoBusqueda.items():
                    if valor == valorBusqueda:
                        indexAlumno = i
                        break
            if indexAlumno == -1:
                print("No se encontro el email del alumno, favor de verificar")
            else:
                alumnos.pop(indexAlumno)
                print("ALUMNO ELIMINADO CON EXITO!!!")
    elif opcion == 5:
        print()
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCIÓN INCORRECTA")