import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
class Instrumento:
    def __init__(self, nombre, puede_afinar=False):
        self.nombre = nombre
        self.puede_afinar = puede_afinar
        self.label = tk.Label()
        canvas = Canvas()

    def afinar(self):
        if self.puede_afinar:
            print(f"Afinando {self.nombre}")
        else:
            print(f"{self.nombre} no se puede afinar")
    def tocar(self):
        pass
    def consultar(self):
        print("Soy: ", self.nombre)

class Piano(Instrumento):
    def __init__(self):
        super().__init__("Piano")
    def tocar(self):
        print("Tocando piano: ¡plink plink!")
    def mostrar_imagen(self):
        self.label.image_create(tk.END, image=tk.PhotoImage("Piano.png"))

class Flauta(Instrumento):
    def __init__(self):
        super().__init__("Flauta")
    def tocar(self):
        print("Tocando flauta: ¡flauta flauta!")
    def mostrar_imagen(self):
        self.label.image_create(tk.END, image=tk.PhotoImage("Flauta.png"))
class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando guitarra: ¡strum strum!")
    def mostrar_imagen(self):
        self.label.image_create(tk.END, image=tk.PhotoImage("Guitarra.png"))
class Saxofon(Instrumento):
    def __init__(self):
        super().__init__("Saxofon")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando saxofon: ¡jazz jazz!")   
    def mostrar_imagen(self):
        self.label.image_create(tk.END, image=tk.PhotoImage("Saxofon.png")) 
class Bajo(Instrumento):
    def __init__(self):
        super().__init__("Bajo")
        self.puede_afinar = True
    def tocar(self):
        print("Tocando bajo: ¡dum dum!")
    def mostrar_imagen(self):
        self.label.image_create(tk.END, image=tk.PhotoImage("Bajo.png"))
if __name__ == "__main__":
    a = Piano()
    a.consultar()
