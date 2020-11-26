"""
Paquetes
PyPI Python
->easy install nombre_del_paquete
->pip install nombre_del_paquete
pip install virtualenv
"""
#from animals.gato import Gato
from animals import Gato #Cuando ya esta importado en el init
#from animals import creador_gatos
#from animals import CONSTANTES

gato = Gato('Nuevo gato por paquete')
print(gato.nombre)

#gato_init = Gato('Nuevo gato creado en init')
#print(gato_init.nombre)

#print(CONSTANTES)

"""
Sub paquetes
"""
print(gato.comer())