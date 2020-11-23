#Función anónima
#Deben de ser acciones muy concretas, no ciclos, no condicionales
mi_funcion = lambda v_uno, v_dos: v_uno + v_dos 
formato = lambda sentencia : '¡¿{}?!'.format(sentencia)

resultado = mi_funcion(10,20)
print(resultado)

resultado2 = formato('Crea una pregunta')
print(resultado2)

