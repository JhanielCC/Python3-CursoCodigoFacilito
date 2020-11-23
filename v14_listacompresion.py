"""
lista = []
for valor in range(0,101):
    lista.append(valor)

print(lista)
"""
#1- Valor a agregar a la lista 
#2- Un ciclo, for 
print("Lista: ")
lista = [ valor for valor in range(0,101)]
print(lista)

print("Lista Pares: ")
lista_pares = [ val for val in range(0,101) if val % 2 == 0 ]  
print(lista_pares)

print("Tupla Inpar: ")
tupla = tuple((valo for valo in range(0,101) if valo % 2 != 0)) 
print(tupla)

print("Diccionario: ")
diccionario = { indice:dval for indice,dval in enumerate(lista) if indice < 50}
print(diccionario)

