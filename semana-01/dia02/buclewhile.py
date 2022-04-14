# Tabla de multiplicar
from calendar import c


n = int(input("Ingrese la tabla de multiplicar que desea mostrar: "))
c = 1
while(c <= 12):
    valor = n * c
    print(str(n) + " x " + str(c) + " = " + str(valor))
    c += 1