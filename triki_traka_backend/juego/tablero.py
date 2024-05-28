def dibujar_tablero(tablero):
    print("  1 2 3")
    for i, fila in enumerate(tablero):
        print(f"{i + 1} {' '.join(fila)}")


def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
    tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual


def tablero_completo(tablero_actual):
    return all(celda != '-' for fila in tablero_actual for celda in fila)


def comprobar_ganador(jugador, tablero_actual):
    simbolo = jugador[1]
    # Comprobar filas y columnas
    for i in range(3):
        if all(tablero_actual[i][j] == simbolo for j in range(3)) or all(tablero_actual[j][i] == simbolo for j in range(3)):
            return True
    # Comprobar diagonales
    if all(tablero_actual[i][i] == simbolo for i in range(3)) or all(tablero_actual[i][2 - i] == simbolo for i in range(3)):
        return True
    return False
