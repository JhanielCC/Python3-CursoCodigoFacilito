"""
Documentar código
"""

def generador(*args):
    """Recibe n cantidad de números y regresa el número además de regresar
True o false si el número es mayor a 5 -Siempre crear la documentacion en la primer linea de la función
    """
    for valor in args:
        yield valor, True if valor > 5 else False

nombre= generador.__name__
documentacion = generador.__doc__

print(nombre," : ")
print(documentacion)


#Interprete de python
"""
->python3 
->from v23_docstring import generador
->help(generador)
...
"""