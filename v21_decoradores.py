"""
Un Decorador:
Nos va a permitir agregar mayor funcionalidad a una funcion en concreta
"una función que crea funciones"
"""
#A, B, C son funciones
#A recibe como parametro B para poder crear C
def decorador(is_valid):
    
    def _decorador(func): #A (B)
        def before_action():
            print("Vamos a ejecutar la función")
        def after_action():
            print("Se ejecuto la función")

        def nueva_funcion(*args,**kwargs): #De esta forma mi decorador es flexible para recibir o no argumentos 
            if is_valid:
                before_action()
            resultado = func(*args,**kwargs)
            after_action()
            return resultado
        return nueva_funcion #C
    return _decorador

@decorador(is_valid=True)
def saluda():
    print("Hola Mundo")

@decorador(is_valid=False)
def suma(n_uno,n_dos):
    return n_uno + n_dos

#Al ser el decorador flexible con los argumentos puede o no recibirlos
saluda()
res = suma(87,17)
print(res)