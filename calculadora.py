#!/usr/bin/python3
"""
v24_25_26_27_modulos_calculadora 
Aquí colocamos todo lo que hace el modulo a que contexto le corresponde.
"""
#Estructura que tiene que tener un modulo  /  Metadatos
__author__ ="Jhaniel CC"
__copyright__ ="Copyright 2020, ..."
__credits__ ="Curso Código Facilito Python 3"

__license__ ="GPL"
__version__ ="1.0.1"
__maintainer__ ="Jhaniel CC"
__email__ ="jhaart3@gmail.com"
__status__ ="Developer"

def suma(n_uno,n_dos):
    """Regresa un número entero el cual es el resultado de una suma"""
    return n_uno + n_dos

def resta(n_uno,n_dos):
    """Regresa un número entero el cual es el resultado de una resta"""
    return n_uno - n_dos

def multiplicacion(n_uno,n_dos):
    """Regresa un número entero el cual es el resultado de una multiplicación"""
    return n_uno * n_dos

def division(n_uno,n_dos):
    """Regresa un número real el cual es el resultado de una división"""
    return n_uno / n_dos

def saluda():
    print(__name__)
    print("Saludo desde calculadora")

if __name__ ==  '__main__':
    saluda()

"""
Para revisar este modulo
->python3
->import v24_25_26_modulos_calculadora 
->help(v24_25_26_modulos_calculadora)
...
->dir(v24_25_26_modulos_calculadora)
"""