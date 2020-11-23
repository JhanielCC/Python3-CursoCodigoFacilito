"""
FUNCIONES ANIDADAS

def validacion (n_uno, n_dos):
    return n_uno > 0 and n_dos > 0

def division(n_uno,n_dos):
    if validacion(n_uno, n_dos):  #Llamado de fuciones
        return n_uno / n_dos

resultado = division(10,2)
print(resultado)
"""

def division(n_uno,n_dos):
    #Cuando la función de validacion sea unica y exclusiva de división
    def validacion ():  #Las funciones anidadas pueden o no recibir parametros
        return n_uno > 0 and n_dos > 0
    if validacion():  #Llamado de fuciones
        return n_uno / n_dos

resultado = division(10,2)
print(resultado)

#Closure - funcies que crea funciones
def crear_funcion(n_uno, n_dos):
    def vali():
        print("Se ejeecuta validación")
        return n_uno > 0 and n_dos > 0
    return vali

nueva_funcion = crear_funcion(10,2)
print(nueva_funcion())


#Recibir función como parametro
print("Ejecución de función pasada como parametro")
def aplicar_funcion(func):
    res = func()
    print(res)

aplicar_funcion(nueva_funcion)