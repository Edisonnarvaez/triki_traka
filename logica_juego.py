# logica_juego.py
import random
from tablero import actualizar_tablero, tablero_completo, comprobar_ganador

def inicializar_juego():
    """Función que inicializa los valores del juego"""
    juego_en_curso = True
    jugadores = [["Jugador 1", "X"], ["Jugador 2", "O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    return juego_en_curso, jugadores, jugador_actual, tablero

def jugar_turno(jugadores, jugador_actual, tablero, coordenada_fila, coordenada_columna):
    """Realiza el turno del jugador actual y devuelve el estado actualizado"""
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero)
    ganador = comprobar_ganador(jugadores[jugador_actual], tablero)
    if not ganador:
        jugador_actual = 1 - jugador_actual
    return tablero, jugador_actual, ganador
