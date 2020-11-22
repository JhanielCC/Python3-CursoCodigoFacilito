"""
Objetos iterables
"""
lista =[1,2,3,4,5,6,7,8,9,10]
tupla =(1,2,3,4,5,6,7,8,9,10)
print("Lista ...")
for valor in lista:
    print(valor)


nuevo_rango = range(0,10) #Range genera un objeto iterable con (n) numeros
#range(0,20) asi genera un OI (Desde donde inicia, hasta donde termina)
#range(20) asi solo genera un OI hasta el 19
#range(0,20,2) asi genera un OI con algunos saltos (de 2 en 2)
print("Rango ...")
for valor in nuevo_rango:
    print(valor)
"""
#for valor=0; valor<20; valor +4
for valor in range(0,20,4)
    print(valor)
"""
print("Creando un indice....indice=0")
indice = 0
for valor in lista:
    print(valor," tiene el indice: ", indice)
    indice +=1

print("Utilizando enumerate.....")
for indi,val in enumerate(lista):
    print(val," tiene el indice: ", indi)

print("Usando la cantidad de los items alojados en una lista usando len(): ")
for valor in range(0,len(lista)):
    print(valor)

print("Recorrer String")
for valor in 'Curso de código facilito':
    print(valor)

diccionario = {'a':10,'b':300,'c':750}
for valor in diccionario.items(): #diccionario.keys()  diccionario.values()
    print(valor)

