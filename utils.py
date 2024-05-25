# utils.py
import os

def pedir_coordenadas():
    """Pide al jugador que ingrese coordenadas válidas"""
    while True:
        try:
            coordenada_fila, coordenada_columna = map(int, input("Elige coordenadas (fila columna): ").split())
            if 1 <= coordenada_fila <= 3 and 1 <= coordenada_columna <= 3:
                return coordenada_fila, coordenada_columna
            else:
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa números separados por un espacio.")

def limpiar_pantalla():
    """Función para limpiar la pantalla"""
    os.system("cls" if os.name == "nt" else "clear")
