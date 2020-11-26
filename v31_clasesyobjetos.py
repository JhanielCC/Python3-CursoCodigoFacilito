"""
v31
"En python todo es un objeto"

"""
class Lapiz:
    """
    v33 Init - Inicializar todos los atributos
    """
    def __init__(self, color='Amarillo', contiene_borrador=True, usa_grafito=True):
        #Atributos
        self.color=color            
        self.contiene_borrador = contiene_borrador   
        self.usa_grafito = usa_grafito           

    #Métodos
    def dibujar(self):
        print("El lapiz esta dibujando...")
    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lapiz esta borrando...")
        else:
            print("No es posible borrar...")    
    def es_valido_para_borrar(self):
        return self.contiene_borrador



"""
v32
Atributos y métodos
"""
#Esto es un objeto 
lapiz_generico = Lapiz("Amarillo",True,True)
print(lapiz_generico.color)
print(lapiz_generico.dibujar())
print(lapiz_generico.borrar())

lapiz_dibujo = Lapiz("Verde",False,True)
print(lapiz_dibujo.color)
print(lapiz_dibujo.dibujar())
print(lapiz_dibujo.borrar())
lapiz_dibujo = Lapiz(contiene_borrador=True)
print(lapiz_dibujo.borrar())

lapiz_nuevo = Lapiz()
print(lapiz_nuevo.color)
print(lapiz_nuevo.dibujar())
print(lapiz_nuevo.borrar())
