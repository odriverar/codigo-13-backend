# Similar a JSON
capitales = {
    'Perú': 'Lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
}

print(capitales)
## ini ---> Agregar un nuevo valor al diccionario
nuevaCapital = {'Brasil': 'Brasilia'}
capitales.update(nuevaCapital)
print(capitales)
## fin ---> Agregar un nuevo valor al diccionario

## ini ---> Eliminar valores del diccionario
c = capitales.pop("P", 'No existe ese pais en el diccionario')
print(capitales)
print(c)
## fin ---> Eliminar valores del diccionario

### RECORRER DICCIONARIOS
for capital in capitales:
    print(capital + " : " + capitales[capital])

print(capitales.keys())
print(capitales.values())
print(capitales.items())

for clave in capitales.keys():
    print(clave + " => " + capitales[clave])

for clave, valor in capitales.items():
    print(clave + " --- ", valor)

alumno1 = {
    'Nombre': 'David Rivera',
    'Edad': 41,
    'Nota': 19.5,
    'Aprobado': True,
    'Cursos': ['Java', 'Python', 'C#']
}

alumno2 = {
    'Nombre': 'Jose Pendiente',
    'Edad': 40,
    'Nota': 19.5,
    'Aprobado': True,
    'Cursos': ['Java', 'Swift', 'Kotlin']
}

alumnos = [alumno1, alumno2]
print(alumnos)

print("*" * 120)
for columna in alumno1:
    print(columna, end=" | ")
print()
print("*" * 120)

for alumno in alumnos:
    for clave, valor in alumno.items():
        print(valor, end= " | ")
    print()