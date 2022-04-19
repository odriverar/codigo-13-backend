class moneda:
    def __init__(self, tipo, cambio):
        self.tipo = tipo
        self.cambio = cambio
        
    def mostrar(self):
        print("La moneda es: ", self.tipo, " y su cambio a Soles es: ", str(self.cambio))
    
    def convertir(self, monConvertir, tipo):
        if tipo == "soles":
            resultado = monConvertir * self.cambio
        else:
            resultado = monConvertir / self.cambio
        
        return resultado

    
monedaDolar = moneda("Dolar $", 3.76)
monedaEuro = moneda("Euro €", 4.10)

monedaDolar.mostrar()
monedaEuro.mostrar()

tipo = input("Ingrese el tipo de moneda a convertir: ")
monOrigen = float(input("Ingrese el monto: "))
opcion = input("Ingrese la opcion para convertir 1) soles a " + tipo + " 2) de " + tipo + " a soles: ")

