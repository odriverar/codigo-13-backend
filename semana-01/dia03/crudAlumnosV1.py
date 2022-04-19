import tabulate
from libAlumnos import buscarAlumno, menu, insertarAlumno, actualizarAlumno, eliminarAlumno, cargarAlumnos, grabarAlumnos
# PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D 



menu()
opcion = 0
# alumnos = [{'nombre': 'David Rivera Robles', 'email': 'odriverar@gmail.com', 'celular': '987762000'}]
#Cargamos datos del archivo de texto
alumnos = cargarAlumnos()

while (opcion != 5):
    opcion = int(input("INGRESE OPCIÓN MENU: "))
    if opcion == 1:
        print("NUEVO ALUMNO")       
        insertarAlumno(alumnos)
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
        indexAlumno = buscarAlumno(valorBusqueda, alumnos)
        if indexAlumno == -1:
            print("No se encontro el email del alumno, favor de verificar")
        else:
            actualizarAlumno(indexAlumno, alumnos)
    elif opcion == 4:
        print()
        print("ELIMINAR ALUMNO")
        print("-" * 52)
        if len(alumnos) == 0:
            print("No existen registros")
            print("-" * 52)
        else:
            valorBusqueda = input("Escriba el nombre del alumno a eliminar: ")
            indexAlumno = buscarAlumno(valorBusqueda, alumnos)
            if indexAlumno == -1:
                print("No se encontro el email del alumno, favor de verificar")
            else:
                eliminarAlumno(indexAlumno, alumnos)
    elif opcion == 5 or opcion == 0:
        print()
        strAlumnos = grabarAlumnos(alumnos)
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCIÓN INCORRECTA")