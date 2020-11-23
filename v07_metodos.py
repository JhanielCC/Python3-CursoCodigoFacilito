"""METODOS DE CADENAS"""
course = "Curso"
my_string = "Código Facilito Python 3"
#METODOS DE FORMATOS
print('<<<<< METODOS DE FORMATOS >>>>>')
resultA = "{} de {}".format(course,my_string)
print("Formato de '{ }':  ", resultA)
result = "{a} de {b}".format(b=course, a=my_string)
print("Formato de '{ a }':  ", result)
result = resultA.lower()	#estandarizar todo el string en minúsculas
print("Formato usando lower():  ",result)
result = resultA.upper()	#estandarizar todo el string en mayusculas
print("Formato usando upper():  ",result)
result = resultA.title()	#poner el string como un titulo
print("Formato usando title():  ",result)

#METODOS DE BUSQUEDA
print('<<<<< METODOS DE BUSQUEDA >>>>>')
pos = resultA.find('Código') #Buscar
print("Busqueda de posición 'Código':  ",pos)
cou = resultA.count('c')	#Contar 
print("Cuenta de 'c':  ",cou)
new_string = resultA.replace('c','x') #remplazar caracteres
print("Reemplazo de 'c' por 'x':  ",new_string)
new_string_sec = resultA.split(' ') #secciona string en pequeños bloques  cada espacio
print("Seccionando string en pequeños bloques cada espacio: ",new_string_sec)
