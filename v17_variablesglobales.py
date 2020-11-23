"""
Variable Local :
Son solo las que se crean o utilizan dentro de una función, 
una vez terminada no podran ser accedidas o dificadas
Variable Global :
La vamos a poder utilizar a lo largo de nuestro proyecto


def palindromo(frase):
    #Eliminar los espacios vacios dentro de la cadena
    frase = frase.replace(' ','')#variable local
    print(frase)
    return frase==frase[::-1]   #Nos retornara True o False dependiendo si o no es similar

frase = 'anita lava la tina'    #variable global
print(frase)
resultado = palindromo(frase)
print(resultado)
"""
#La Variable Gobal ahora esta siendo accedidad por la función 
#La variable global puede estar antes o despues de la declaración de la función
#Lo que si afectaria es llamar la función antes de ser declarada
def palindromo():
    n_valor = frase.replace(' ','')
    return n_valor==n_valor[::-1]   

frase = 'anita lava la tina'   
resultado = palindromo()
print(resultado)

#Modificación de variables globales
def valor_global():
    global var_glob # global para modificar la varibale global 
    var_glob = 'Cambiar valor'

var_glob = 'Esto es una variable global'

print(var_glob)
valor_global()
print(var_glob)


#Creaciónde una variable global dentro de una función
def crear_global():
    global nueva_var_glob
    nueva_var_glob = 'Esto es una variable global creada en una función'

crear_global()
print(nueva_var_glob)
