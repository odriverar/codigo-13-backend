# ENTRADA
tabla = input("Ingresa la tabla de multiplicar que desea mostrar: ")
# PROCESO
for contador in range(1, 13):
    valor = float(tabla) * contador
    print(str(tabla) + ' x ' + str(contador) + ' = ' + str(valor))
# SALIDA