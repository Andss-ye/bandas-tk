from banda import *
from instrumento import *

if __name__ == "__main__":
    # Crear una banda con algunos instrumentos
    b = Banda("Los Rítmicos", [Piano(), Guitarra(), Saxofon(), Bajo(), Flauta()])
    
    # Crear músicos aleatorios
    b.crear()
    
    # Consultar la información inicial de la banda
    b.consultar()
    
    # Dar la opción de afinar los instrumentos
    opcion = input("¿Deseas afinar los instrumentos de la banda? (S/N): ").strip().lower()
    b.consultar()
    print ("\nTocando sonidos de la banda:\n")
    if opcion == 's':
        b.afinar_instrumentos()  # Llama al método para afinar los instrumentos
    for Musico in b.integrantes:
        Musico.tocar()    # Consultar la información actualizada de la banda
    for instrumento in list(b.mostrar_instrumento()):
        Instrumento.mostrar_imagen()
