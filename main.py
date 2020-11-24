""" v24_25_26_27_modulos_calculadora """
#import v24_25_modulos_calculadora
#from v24_25_modulos_calculadora import *    No es tan convencional dependiendo de la complegidad
from calculadora import suma,resta,multiplicacion #Solo importar la funcionalidad
from calculadora import division as d1 #Renombramos division como d1
from calculadora import __name__ as __name__calculadora

#resultado = calculadora.suma(30, 46)
resultado = suma(30, 46)
resultado2 = resta(125, 35)
resultado3 = d1(280, 22)

print("Suma importada:  ",resultado)
print("Resta importada:  ",resultado2)
print("División importada[d1]:  ",resultado3)

print(__name__) #simpre sera main cuando el archivo sea el principal
print(__name__calculadora)

#if __name__ == '__main__': #Es este el script principal?
