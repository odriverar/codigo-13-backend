#PROGRAMA PARA CONVERTIR MONEDAS.
#version 1.0 - convertir soles a dolares
#INPUTS - ENTRADAS
monto = input("ingrese monto: ")
#PROCESO
opcion = ""
while(opcion == ""):
    print(" opción 1 - Soles a Dolares")
    print(" opción 2 - Dolares a Soles")
    print(" opción 3 - Soles a Euros")
    print(" opción 3 - Euros a Soles")
    opcion = input("Elija una opción: ")
    if (opcion == "1"):
        montoDolares = float(monto) / 3.80
        montoResultado = "$ {:,.2f}".format(montoDolares)
        #OUTPUTS - SALIDAS
        print("El monto en dolares es: " + str(montoResultado))
    elif(opcion == "2"):
        montoSoles = float(monto) * 3.80
        montoResultado = "S/ {:,.2f}".format(montoSoles)
        #OUTPUTS - SALIDAS
        print("El monto en soles es: ", montoResultado)
    elif(opcion == "3"):
        montoSoles = float(monto) / 4.04
        montoResultado = "€ {:,.2f}".format(montoSoles)
        #OUTPUTS - SALIDAS
        print("El monto en Euros es: ", montoResultado)
    elif(opcion == "4"):
        montoSoles = float(monto) * 4.04
        montoResultado = "€ {:,.2f}".format(montoSoles)
        #OUTPUTS - SALIDAS
        print("El monto en Euros es: ", montoResultado)
    else:
        print("ALERTA !!! debe seleccionar una opcion valida")
        opcion = ""