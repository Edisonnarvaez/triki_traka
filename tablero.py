# tablero.py
def dibujar_tablero(tablero):
    """Función para dibujar el tablero"""
    print("  1 2 3")
    for i, fila in enumerate(tablero):
        print(f"{i + 1} {' '.join(fila)}")

def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    """Actualiza el tablero con la acción del jugador actual"""
    tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual

def tablero_completo(tablero_actual):
    """Comprueba si el tablero está completo, devuelve True o False"""
    return all(celda != '-' for fila in tablero_actual for celda in fila)

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
