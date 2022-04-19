f = open('alumnos.txt', 'w')
f.write('David Rivera Robles,odriverar@gmail.com,987762000\n')
f.write('Trend Rivera León,trend@gmail.com,987762001\n')
f.write('Jenny Rivera León,jenny@gmail.com,987762002\n')

# f = open('alumnos.txt', 'r')
# alumnos = f.read()
# print(alumnos)

# listaAlumnos = alumnos.splitlines()
# print(listaAlumnos)

# listaResultado = []

# for dictAlumno in listaAlumnos:
#     listaDiccionarioAlumnos = dictAlumno.split(',')
#     print(listaDiccionarioAlumnos)
#     dictAlumno = {
#         'nombre':listaDiccionarioAlumnos[0],
#         'email':listaDiccionarioAlumnos[1],
#         'celular':listaDiccionarioAlumnos[2],
#     }
#     listaResultado.append(dictAlumno)

# print(listaResultado)  