""" v28_30 """
import random
import datetime
import sys
import time

valor = random.randint(0,10)    #(inicio,termina)
print("Valor Random generado entr 0 y 10 :  ",valor)

lista = [True,"String", 23,False]
valor = random.choice(lista)
print("Valor Random tomado de una lista :  ",valor)

print("Lista normal:  ",lista)
random.shuffle(lista)
print("Lista desordenada:  ",lista)

print("Hora actual:  ",datetime.datetime.now())

""" Excepciones """
try:
    print(2/0)
except ZeroDivisionError as ex:
    print(ex)
    print("No es posible dividir por 0") #Mo utilizar aquí pass

try: #Si o si
    lista = [1,2]
    print(lista[9])
except Exception as ex: #Exception cuando no conoces el tipo de error
    print(ex)
    print("Ah ocurrido un error!")
finally: #si o si
    print("Este bloque siempre se va a ejecutar")
"""
except IndexError as ex:
    print(ex)
    print("No es posible obtener el valor en [9]")
except ZeroDivisionError as ex:
    print(ex)
    print("No es posible dividir por 0") 
"""


for i in range(11):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.flush()

