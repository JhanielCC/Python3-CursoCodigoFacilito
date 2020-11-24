"""
Generadores:
Nos vana servir para poder crear objetos sin necesidad de almacenarlos en la RAM
range es uno
"""

def generador(*args):
    for valor in args:
        yield valor*10, True #return valor*10  en el 1 termina todo, para poder utilizar el generador hacemos uso de yield
        #yield no esta restringido a solo regresarnos un valor

for valor_uno, valor_dos in generador(1,2,3,4,5,6,7,8,9):  #for valor in  1valor
    print(valor_uno,valor_dos) #print(valor)   1valor
    