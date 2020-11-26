"""
Herencia 
"""   
class Animal: #clase padre padre
    @property
    def terrestre(self):
        return True

class Felino(Animal): #clase padre
    @property
    def garras_retractiles(self):
        return True
    def cazar(self):
        print("El felino esta cazando...")

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(self.nombre)

class Gato(Felino,Mascota): #Herencia multiple de felino y de mascota 
    def __init__(self, nombre): #Sobre escritora de init en mascota
        Mascota.__init__(self, nombre)
        self.nombre_gato = nombre

    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self):   #Sobre escritura de método de clase
        Mascota.mostrar_nombre(self)   #ejecución del método anterior en mascota
        print("El nombre del gato es:   {}".format(self.nombre)) #Nuevo código


class Jaguar(Felino):
   pass

gato = Gato('Michi')
jaguar = Jaguar()

print(gato.cazar())
print(jaguar.garras_retractiles)
print(gato.gato_cazador())
print(gato.terrestre)

"""
v39 Herencia múltiple
"""
#gato.nombre='Michi michi'
"""
v40 Overrride - Sobre escritura de métodos
"""
gato.mostrar_nombre()