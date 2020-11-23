"""
CONDICIONAL IF
"""
print("Fruta=")
fruta = 'kiwi'
if fruta == 'kiwi':
    print("El valor es kiwi")
else:
   print("No son iguales")

#---------------------------------
mensaje='El valor es kiwi x2' if fruta == 'kiwi' else 'No son iguales' #si es mas de un valor se usa la ant
mensaje=99 if fruta == 'kiwi' else False
print(mensaje)

#---------------------------------
#	>	<	>=	<=	!=	==
if fruta == 'kiwi':
    print("El valor es kiwi")
elif fruta == 'manzana':
    print('El valor es una manzana')
elif fruta == 'limon':
    pass 	 #Necesitaremos la condiciona pero aun no sabemos que acciones hacer la pasamos
else:
   print("No son iguales")

#---------------------------------
#True = 1  , False = 0
if True:  #if 1:
    print("Es verdad")
#Todas las variables van a ser boleanas
#[] , (), {}, 0 ,’’, None  son vacíos son falsos 
if 0:   # if []: nos regresara false, todas las variables vacias o nulas son tomadas como falsas
    print("Es verdad")
else:
    print("No es verdad")

#---------------------------------
valor = 1 # 	valor = None
valor_dos = 21
if valor and valor_dos > 20:  	# If valor or valor_dos > 20:  
    print("Es verdad usando and")
else:
    print("No es verdad")
