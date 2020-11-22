"""DICCIONARIOS
Son una estructura de datos que al igual que las listas y las tuplas nos permiten almacenar diferentes tipos de datos, aquí podemos almacenar enteros, strins, listas, tuplas, el diccionario no se rige por un índice, no podemos modificar los valores dentro mediante índices, para poder hacerlo necesitamos
Calve : valor
"""
diccionario={'a':55,'e':True,4:"Esto es un string",(1,2):False,'a':False,'a':100} #Las claves/llaves deben ser inmutables
#Si existen dos llaves iguales, toma el valo de la ultima llave a la derecha
print("<<<<< DICCIONARIOS >>>>>")
print("Diccionario:  ",diccionario)
#Los diccionarios pueden crecer o decrecer
diccionario['c']= "Nuevo String" #Creamos clave/valor
print("Creación de la llave[c]:  ",diccionario)
diccionario['a']= "Ahora String" #Modificar, si la llave/clave se encuentra actualiza, sino crea
print("Modificar llave[a] y si no existe se crea:  ",diccionario)
valor = diccionario['a'] #obtener los valores
print("Obtener el valor de una llave [a]:  ",valor)
print(diccionario)

#GET
#valor = diccionario['z'] # Si la calve no existe marcara error
valor = diccionario.get('z', False)  #Buscara la clave que se le da y si esta no existe nos regresa false
valor = diccionario.get('z', "Esa clave no existe") #Se puede regresar todo 

#ELIMINAR
print("Eliminar la llave [a]")
del diccionario['a']  #del elimina
print(diccionario)

llaves = diccionario.keys() #Objeto iterable
print("Llaves del Diccionario:  ",llaves)
llaves = list(diccionario.keys()) #Convertirla en una lista
print("Llaves en lista:  ",llaves)
llaves = tuple(diccionario.keys()) #Convertirla en una tupla
print("Llaves en tupla:  ",llaves)
valores = diccionario.values() #Valores
print("Valores del Diccionario:  ",valores) 
valores = list(diccionario.values()) #Valores como listas
print("Valores en lista:  ",valores)
valores = tuple(diccionario.values()) #Valores como tuplas
print("Valores en tupla:  ",valores)


#EXTENDER DICCIONARIO
diccionario_dos = {'z':12,'w':88}
print("Diccionario:  ",diccionario,"  Diccionario2:  ",diccionario_dos)
diccionario['z'] = diccionario_dos['z'] #el elemento z
diccionario['w'] = diccionario_dos['w'] #el elemento w
diccionario.update(diccionario_dos) #todo el diccionario dos
print("Diccionarios unidos:  ",diccionario)
