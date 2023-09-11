import tkinter as tk
from tkinter import ttk
from musico import Musico
from instrumento import Instrumento
from random import choice, randint
from banda import Banda

class BandaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banda Musical")
        
        self.nombre_banda_label = ttk.Label(root, text="Nombre de la banda:")
        self.nombre_banda_label.pack()
        self.nombre_banda_entry = ttk.Entry(root)
        self.nombre_banda_entry.pack()
        
        self.crear_banda_button = ttk.Button(root, text="Crear Banda", command=self.crear_banda)
        self.crear_banda_button.pack()
        
  # Carpeta donde se encuentran las imágenes de los instrumentos
        
        self.instruments_images = {
            "Piano": tk.PhotoImage("piano.png"),
            "Flauta": tk.PhotoImage("flauta.png"),
            "Guitarra": tk.PhotoImage( "guitarra.png"),
            "Saxofon": tk.PhotoImage("saxofon.png"),
            "Bajo": tk.PhotoImage("bajo.png"),
        }
        
        self.instrumentos_label = ttk.Label(root, text="Instrumentos:")
        self.instrumentos_label.pack()
        
        self.instrumentos_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.instrumentos_listbox.pack()
        for instrument in self.instruments_images.keys():
            self.instrumentos_listbox.insert(tk.END, instrument)
        
        self.cargar_imagenes_button = ttk.Button(root, text="Cargar Imágenes", command=self.cargar_imagenes)
        self.cargar_imagenes_button.pack()
        
        self.musico_label = ttk.Label(root, text="Músicos:")
        self.musico_label.pack()
        self.musico_text = tk.Text(root, height=10, width=40)
        self.musico_text.pack()
        
    def crear_banda(self):
        nombre_banda = self.nombre_banda_entry.get()
        selected_instruments = [self.instrumentos_listbox.get(i) for i in self.instrumentos_listbox.curselection()]
        
        self.banda = Banda(nombre_banda, selected_instruments)
        
        self.cargar_imagenes()
        self.actualizar_musico_text()
    
    def cargar_imagenes(self):
        for musico in self.banda.integrantes:
            instrument = musico.instrumento_toca.nombre
            if instrument in self.instruments_images:
                self.musico_text.image_create(tk.END, image=self.instruments_images[instrument])
                self.musico_text.insert(tk.END, f"\n{musico.nombre} - {instrument}\n")
    
    def actualizar_musico_text(self):
        self.musico_text.delete(1.0, tk.END)
        if hasattr(self, 'banda'):
            for musico in self.banda.integrantes:
                self.musico_text.insert(tk.END, f"{musico.nombre} - {musico.instrumento_toca.nombre}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BandaApp(root)
    root.mainloop()
