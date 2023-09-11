from musico import Musico
from instrumento import Instrumento
from random import choice, randint

class Banda:
    def __init__(self, nombre, instrumentos):
        self.nombre = nombre
        self.integrantes = []
        self.instrumentos = instrumentos
    def tocar(self):
        pass
    def crear(self):
        for i in range(0, randint(1, 5)):
            instrumento_random = choice(self.instrumentos)
            musico = Musico("Musico"+str(i+1), instrumento_random)
            self.integrantes.append(musico)

    def afinar_instrumentos(self):
        for musico in self.integrantes:
            musico.afinar_instrumento()

    def mostrar_instrumento(self):
        for Instrumento in self.instrumentos:
            Instrumento.mostrar_imagen()


    def consultar(self):
        print("Nombre de la banda: ", self.nombre)
        print("Instrumentos en la banda: ", [instrumento.nombre for instrumento in self.instrumentos])
        print("Integrantes de la banda: ", [(musico.nombre, musico.instrumento_toca.nombre) for musico in self.integrantes])
