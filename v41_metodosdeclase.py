"""
Factory metod
"""
class Animal:
    volador = True

class Cocodrilo(Animal):
    def __init__(self,nombre):
        self.nombre= nombre
    """
    Los métodos de clase pueden acceder a los atributos o a los métodos de las clases que se estan heredando
    """
    @classmethod   #para hacerlo método de clase
    def new(cls,nombre): #(self,nombre) Método de instancia - solo puede ser ejecutado por un objeto
        cls.volador=False #accediendo a volador de herencia animal
        return Cocodrilo(nombre)

coco=Cocodrilo.new('Coco')
print("Nombre de cocodrilo: ",coco.nombre)
print("Cocodrilo volador?: ",coco.volador)