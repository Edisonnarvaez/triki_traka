import tkinter as tk
from logica_juego import inicializar_juego, jugar_turno
from tablero import dibujar_tablero

class TresEnRayaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triki traka")

        self.juego_en_curso, self.jugadores, self.jugador_actual, self.tablero = inicializar_juego()
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', width=10, height=3, 
                                command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.label = tk.Label(self.root, text=f"Turno de: {self.jugadores[self.jugador_actual][0]}")
        self.label.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, i, j):
        if self.tablero[i][j] == '-':
            self.tablero, self.jugador_actual, ganador = jugar_turno(self.jugadores, self.jugador_actual, self.tablero, i + 1, j + 1)
            self.update_buttons()
            if ganador:
                self.label.config(text=f"Ganador: {self.jugadores[self.jugador_actual][0]}")
                self.disable_buttons()
            elif all(celda != '-' for fila in self.tablero for celda in fila):
                self.label.config(text="Fin del juego, no hay ganador")
                self.disable_buttons()
            else:
                self.label.config(text=f"Turno de: {self.jugadores[self.jugador_actual][0]}")
        else:
            self.label.config(text="Casilla ya ocupada. Elige otra casilla.")

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.tablero[i][j])

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

def main():
    root = tk.Tk()
    app = TresEnRayaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
