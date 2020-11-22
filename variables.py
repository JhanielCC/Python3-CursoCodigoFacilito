"""
Espacio en la memoria RAM que va a almacenar ciertos tipos de datos
Caracteres, cadenas de caracteres, números, números reales, booleanos.
Las variables no puedes iniciar con mayúsculas
"""
curso_codigo_facilito = "python 3" 
curso_numero = 11
curso_confirmacion = True
print("Imprimiendo la variable:  ", curso_codigo_facilito, "\n No de Curso: ",curso_numero,"\n Curso confirmación: ", curso_confirmacion)

#La variable puede cambiar de tipo sin ningun problema de string a número a boolean
curso_codigo_facilito = "Curso Python 3"
print("La variable curso_codigo_facilito es:  ", curso_codigo_facilito)
curso_codigo_facilito = 15
print("La variable curso_codigo_facilito es:  ", curso_codigo_facilito)
curso_codigo_facilito = False
print("La variable curso_codigo_facilito es:  ", curso_codigo_facilito)