# logica_juego.py
import random

def inicializar_juego():
    """Función que inicializa los valores del juego"""
    jugadores = [["Jugador 1", "X"], ["Jugador 2", "O"]]
    jugador_actual = random.randint(0, 1)
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    return jugadores, jugador_actual, tablero

def jugar_turno(jugadores, jugador_actual, tablero, coordenada_fila, coordenada_columna):
    """Realiza el turno del jugador actual y devuelve el estado actualizado"""
    tablero[coordenada_fila - 1][coordenada_columna - 1] = jugadores[jugador_actual][1]
    ganador = comprobar_ganador(jugadores[jugador_actual], tablero)
    if not ganador:
        jugador_actual = 1 - jugador_actual
    return tablero, ganador

def comprobar_ganador(jugador, tablero_actual):
    """Comprueba si ha ganado el jugador actual, devuelve True o False"""
    simbolo = jugador[1]
    # Comprobar filas y columnas
    for i in range(3):
        if all(tablero_actual[i][j] == simbolo for j in range(3)) or \
            all(tablero_actual[j][i] == simbolo for j in range(3)):
            return True
    # Comprobar diagonales
    if all(tablero_actual[i][i] == simbolo for i in range(3)) or \
        all(tablero_actual[i][2 - i] == simbolo for i in range(3)):
        return True
    return False
