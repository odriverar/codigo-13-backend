# Crear una clase para administrar los usuarios de un sistema.
class Usuario:
    def __init__(self, nom, pwd):
        self.nombre = nom
        self.password = pwd
    
    def login(self):
        if self.nombre == 'admin' and self.password == '123456789':
            print("Bienvenido ", self.nombre)
        else:
            print("Datos de acceso incorrecto")
            
## usando mi clase

usuario1 = Usuario('admin', 'admin')
usuario1.login()

usuario1 = Usuario('admin', '123456789')
usuario1.login()