class Automovil:
    def __init__(self, aa, pl, col, mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    def encender(self):
        print('encender ', self.marca)
        
    def avanzar(self):
        print('avanzar ', self.marca)
    
    def acelerar(self):
        print('acelerar ', self.marca)
        
    def frenar(self):
        print('frenar ', self.marca)
    
vw = Automovil(1970, 'CH-1234', 'Amarillo', 'Volkswagen')
print("Se creó el objeto vw con los datos")
print("Año: ", str(vw.año))
print("Placa: ", vw.placa)
print("Color: ", vw.color)
print("Marca: ", vw.marca)

vw.encender()

tico = Automovil(1985, 'EJ-2345', 'Rojo', 'TICO')
tico.encender()
tico.frenar()

lamborghini = Automovil(2018, 'E7P-367', 'Amarillo', 'Lamborghini')
lamborghini.acelerar()
