#Raise para ejecutar una excepción 
"""
class TinyIntError(Exception):
    def __init__(self):
        self.mensaje='El número no cuenta con las caracteristicas de un número tiny_int'
    def __str__(self):
        return self.mensaje
"""
"""
def validate_tiny_int(val):
    return val >= 0 and val <= 255

def validate_val(val): #"60"
    try:
        return isinstance(int(val),int) #retorna T/F siel valor es una instancia de int
    except ValueError as error:
        return False
"""
"""
def tiny_int(val, call_back = None):
    try:
        if validate_val(val) and validate_tiny_int(val):
            return True
        else:
            raise TinyIntError()
    except TinyIntError as error:
        if call_back is not None:
            call_back()
        else:
            print(error)     

def call_back_function():
    print("Esto se ejecuta cuando existe un erro")
"""
from tinyinterror import tiny_int
from tinyinterror import call_back_function

print(tiny_int(50, call_back_function))
#print(tiny_int(400, None))
"""
https://pypi.org/
https://choosealicense.com/
"""