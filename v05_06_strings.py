"""
STRINGS
Un string es una lista de caracteres y la unión de ellos, también es un objeto 
"""
my_string = "Hola Mundo"	#'Hola Mundo' Puede ser también 
my_string = "Hola mundo, 'Comillas simples dentro de las dobles'"
my_string = 'Hola mundo, "Comillas dobles dentro de las simples"' 
my_string = """ Para trabar con
strings con saltos de línea
necesito 3 veces comillasdobles  """
my_string = ''' O tambien puedo hacerlo
con tres veces comillas simples 
y así poder trabajar '''
my_string = """	y si no se quiere trabajar con esa forma\n podermos usar\n esta tambien"""
course = "Python 3"
code = "Py001"
user= 'Jhaart'
final_message = "Nuevo curso de  "+ course + " por " + user + " , código: " + code	#1 
final_message = "Nuevo curso de  %s por %s , código: %s" %(course,user,code)		#2
final_message = 'Nuevo curso de  {} por {} , código: {}' .format(course,user,code)		#3
print(final_message) 


"""
STRING COMO LISTAS
"""
my_string = "Curso de CF Python 3"
print(my_string)
print("Posción [0]:     ",my_string[0])
#Indico que inicio desde el lado derecho
print("Inicio desde el lado derecho:     ",my_string[-1]) 	 
#Primer y ultimo caracter
print("Primer y ultimo caracter:     ",my_string[0], my_string[-1]) 	
#sub lista dentro del string
print("Sub lista dentro del string:     ",my_string[0:10])	
#sub lista dentro del string invertida 
print("Sub lista dentro del string invertida:     ",my_string[-12:-1])	
#saltos progresivos de la posición 0 a la 10 de 2 en 2 caracteres
print("Saltos progresivos:     ",my_string[0:10:2])
#String leido de derecha a izquierda  Reverse 
print("String leido de Izq a Der reverse:     ",my_string[::-1])	
