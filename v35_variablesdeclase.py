
class Circulo:
    #pi = 3.1416  #variable de clase  _pi cuando encontremos una variable asi, no las debemos modificar*
    def __init__(self,radio):
        self.radio = radio
        #self.pi = 3.1416   #Le pertenece a los objetos
    def area(self): #Métodos de instancia - si tiene la palabra reservada self y esta dentro de la clase
        return self.radio * self.radio * Circulo.pi()#==self.pi()#* Circulo.pi #Acceder a las variables de clase   == self.pi
    @staticmethod   #Decorarlo para ser método estatico
    def pi():       #Método estatico - cuando la función no tiene la palabra reservada self
        return 3.1416    

circulo_uno = Circulo(4)
"""
circulo_dos = Circulo(3)

print("Radio del circulo uno:  ",circulo_uno.radio)
print("Radio del circulo dos:  ",circulo_dos.radio)

print("Accediendo a Pi desde la clase:  ",Circulo.pi) #No necesito crear un objeto para usar pi
print("Accediendo a Pi desde objeto:  ",circulo_uno.pi)
print("Diccionario de atributos del objeto:  ",circulo_uno.__dict__) #muestra un diccionario con los atributos de la clase excepto las variables de clase
print("Area del objeto:  ",circulo_uno.area())

Circulo.pi = 20 #Las variables de clase no son inmutables, se puede cambiar su valor
print("Modificación de Pi:  ",circulo_uno.pi)
print("Area con nuevo Pi:  ",circulo_uno.area())
"""
"""
v37 Métodos de instancia y estaticos
Cuando algu muy puntual le pertenezca a la clase y no a las instancias

"""
print("---------------------------------------------")
print("PI:  ",Circulo.pi())
print("PI Circulo uno:  ",circulo_uno.pi())
print("Area Circulo uno:  ",circulo_uno.area())