class Musico:
    def __init__(self, nombre, instrumento_toca):
        self.nombre = nombre
        self.instrumento_toca = instrumento_toca

    def tocar(self):
        self.instrumento_toca.tocar()

    def afinar_instrumento(self):
        self.instrumento_toca.afinar()
