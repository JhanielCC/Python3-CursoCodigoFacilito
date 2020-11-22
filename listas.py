"""
LISTAS
Son un tipo de dato en python que pueden almacenar diferentes tipos de datos y pueden modificar su tamaño
"""
print("<<<<<  LISTAS  >>>>>")
my_list = ["String",15,15.6,True,"SS"]
print("Lista:  ",my_list)
my_list.append(6)	#Almacenar el valor 6, en la ultima posición 
print("Almacenamos 6:  ",my_list)
my_list.insert(1,"insert")	#Almacenar "insert" en la posición que se le indique 1 
print("Insertamos 'insert'[1]:  ",my_list)
my_list.remove(15)	#Indicamos que dato dentro de la lista se va a eliminar 
print("Removemos 15:  ",my_list)
print("Lista posición [1]:  ",my_list[1])


#Las podemos trabajar como si fueran pilas
last_value = my_list.pop() #Pop removemos el ultimo elemento de la lista
print("Hacemos Pop a la lista:  ",last_value,"\n",my_list)

my_list= [1,9,22,6,8,65,14,99]
my_list_two= [66,99]
print("Nueva Lista:  ",my_list,"\n Nueva Lista 2:  ",my_list_two)
my_list.sort()
print("Ordenar Ascendente:  ",my_list) #ordenar de forma ascendente
my_list.sort(reverse = True) #ordenar de forma descendente
print("Ordenar Descendente:  ",my_list)
my_list.extend(my_list_two) #unir dos listas
print("Unir ambas listas:  ",my_list)
my_list.append(my_list_two) #despues de los numeros nos almaceno la lista en un espacio
print("Almacenar la segunda lista en un solo espacio:  ",my_list)