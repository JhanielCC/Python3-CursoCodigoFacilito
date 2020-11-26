"""
v44 Init
"""
#des pues del . se busca lo que este al mismo nivel que el archivo init
"""
from .gato import Gato  

CONSTANTES = "Esto es una constante"

def creador_gatos(nombre):
    return Gato(nombre)
"""
"""
Patrón Singleto
"""
#Sub paquetes
from .felinos import Gato
from .felinos import Leon