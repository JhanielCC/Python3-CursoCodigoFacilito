"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Parte 1 Funciones 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
#Factorial de un número
numero = 5
factorial = 1
while numero > 0:
    factorial = factorial * numero
    numero-=1
print("Factorial: ",factorial)

#Para establecer una función def
def factorial_numero():
    #pass
    numero = 6
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero-=1
    print("Factorial creado con funcion: ",factorial)

factorial_numero()

#Recepción de argumentos
def factorial_arg(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero-=1
    print("Factorial creado con funcion recibiendo argumentos: ",factorial)

factorial_arg(8)

#Retorno de valores
def factorial_arg_ret(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero-=1
    return factorial

resultado = factorial_arg_ret(9)
print("Factorial creado con Retorno de valores: ",resultado)


"""
Funciones Argumentos
"""
#La funcion esta preparada solo para dos arguemntos
def suma(valor_uno,valor_dos):
    return valor_uno+valor_dos

resultadosuma= suma(33,77)
print("Suma: ",resultadosuma)

#  *  puede recibir n cantidad de argumentos *args "La mayoria utiliza args para definir los argumentos"
def suma_dos(*argum):
    """
    print(argum)    #Los imprime como tupla
    print(type(argum)) #Para saber el tipo de un valor
    """
    resulta = 0
    for valor in argum:
        resulta = resulta + valor
    return resulta

ressum= suma_dos(33,77,12,33,1,86)
print("Suma Varios argumentos: ",ressum)

# **kwargs argumentos con keys
def sum_key(**kwargs):
    valor=kwargs.get('kvalor', 'No contiene valor') #Obtener el valor con la llave kvalor y si no lo contiene regresar 'No contiene el valor'
    print(valor)

sum_key(x=12,y=44,z=86,a=True)

# * -> n valores -> tuplas
# ** -> n valores -> diccionarios

"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Parte 2 Funciones 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
#Pasar los valores de forma desordenada pero indicando la variable

def division(v_uno,v_dos):
    return v_uno / v_dos
res_div = division(v_dos=10, v_uno=1000 ) # == division(1000,10) 
print("División :",res_div)

#Asignación por default
def multiplicacion(v_uno,v_dos=10): #v_dos va tomar el valor de 10 si este argumento no es enviado
    return v_uno * v_dos
res_mul = multiplicacion(6,8)
res_mul2 = multiplicacion(7) 
print("Multiplicación dos argumentos:",res_mul)
print("Multiplicación un argumento:",res_mul2)

#Regresar multiples valores en tupla
def multiples_valores():
    return "String",8,True,22.54

res_mv = multiples_valores()
print("Multiples valores:",res_mv)
#Separar los valores
"""
stri = res_mv[0]
entero = res_mv[1]
bole = res_mv[2]
flotan = res_mv[3]
#  ==
"""
stri,entero,bole,flotan = multiples_valores() 
print("Multiples valores separados:",stri," ",entero," ",bole," ",flotan)

#Ejecución de función mediante variable
mi_var = multiplicacion
re_var = mi_var(12,8)
print("Resultado de multiplicación mediante variable:  ",re_var)

#Funciones dentro de funciones
def mostrar_resultado( funcion ):
    print("Ejecución de la función dentro de otra función:",funcion(6,8))

mostrar_resultado(mi_var)