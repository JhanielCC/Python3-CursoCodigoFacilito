"""
Atributos privados - estos seran modificados solo por la clase y no por la instancia
"""
class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password) #__password  atributo privado
        self.email = email      
    def __generar_password(self, password): #Método privado
        return password.upper()
    def get_password(self): #Accediendo a los atributos privados solo por la clase y no por la instancia
        return self.__password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,valor):
        self.__password = self.__generar_password(valor)
    

jhaniel = Usuario('Jhaniel','pass123','jhaart3@gmail.com')

print("Nuevo Usuario: ",jhaniel.username, " Pass: ",jhaniel.get_password()," Email: ",jhaniel.email)

"""
v36 Properties  -  Trabajar con los atributos privados de una clase
@property #Decorador
    def password(self):
"""
print(jhaniel.password) #No es posible editar el atributo ya que solo esta disponible para visualizar
jhaniel.password="Nuevo password"
print(jhaniel.password) 
