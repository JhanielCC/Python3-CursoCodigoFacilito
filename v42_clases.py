"""
Métodos Magicos
estos inician y terminan con doble guión bajo __init__
"""
class Usuario:
    def __new__(cls):#Método constructor de la clase
        print("Este método es le primero que se ejecuta.")
        return super().__new__(cls)

    def __init__(self):
        print("Este método es el segundo en ejecutarse.")
        self.__password = 'Contraseña12345'
    def __str__(self):
        return "Esto se imprime cuando se muestra el objeto"
    def __getattr__(self,nombre):
        print("Aquí mostramos que no se contro el atributo")
        self.otro_metodos()

    def otro_metodos(self):
        print("Otro Método")
    
    def mostrar_password(self):
        print(self.__password)

usuario = Usuario()
"""
print(usuario.__dict__)
usuario.nombre = 'Jhaniel'  #Se crea un nuevo atributo público dentro del objeto
print(usuario.nombre)
print(usuario.__dict__) #atributos del objeto

usuario.__password = 'Cambio de contraseña'
print(usuario.__password) #Este seria un nuevo atributo
usuario.mostrar_password() #Este atributo solo esta dentro de la clase
"""
print(usuario) #__str__
print(usuario.apellido) #__getattr__