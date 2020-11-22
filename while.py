"""
#Estructura
while condición:
    código
else:
    código
"""
contador = 0
while contador <= 10: # < > <= >= == !=
    print(contador)
    contador +=1  #contador = contador + 1
    if contador== 5:
        print("Estamos en el número 5")
        continue #continuar el ciclo
    if contador==8:
        break   #romper el ciclo
else:
    print('El while a terminado incrementando de 0 a 10')

print('Contador con badera')
contador_dos = 0
bandera = True
while bandera: # < > <= >= == !=
    print(contador_dos)
    contador_dos +=1  #contador = contador + 1
    if contador_dos==8:
        bandera = False
else:
    print('El while a terminado')

