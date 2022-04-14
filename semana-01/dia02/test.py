from os import remove
import tabulate
alumnos = [{'nombre': 'David Rivera Robles', 'email': 'odriverar@gmail.com', 'celular': '987762000'},
           {'nombre': 'Jose Pardo Hinostroza', 'email': 'jose@gmail.com', 'celular': '987762000'}]

cabeceras = alumnos[0].keys()
registros = [x.values() for x in alumnos]
print(tabulate.tabulate(registros, cabeceras, tablefmt="psql"))

alu = input("Alumno: ")

for alumno in alumnos:
    alumno.pop('nombre')

print(alumnos)