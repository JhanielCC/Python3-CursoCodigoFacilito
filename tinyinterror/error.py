class TinyIntError(Exception):
    def __init__(self):
        self.mensaje='El número no cuenta con las caracteristicas de un número tiny_int'
    def __str__(self):
        return self.mensaje