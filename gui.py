# gui.py
import tkinter as tk
from tkinter import messagebox
from logica_juego import inicializar_juego, jugar_turno

class TresEnRayaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")

        self.jugadores = [["Jugador 1", "X"], ["Jugador 2", "O"]]
        self.juego_en_curso = False
        self.crear_widgets()

    def crear_widgets(self):
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack()

        self.nueva_partida_button = tk.Button(self.frame_botones, text="Nueva Partida", command=self.nueva_partida)
        self.nueva_partida_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.reiniciar_button = tk.Button(self.frame_botones, text="Reiniciar", command=self.reiniciar_partida, state=tk.DISABLED)
        self.reiniciar_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.salir_button = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.salir_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.frame_tablero = tk.Frame(self.root)
        self.frame_tablero.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame_tablero, text='', width=10, height=3,
                                    command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.label = tk.Label(self.root, text="Haz click en 'Nueva Partida' para comenzar", fg="blue")
        self.label.pack()

    def on_button_click(self, i, j):
        if self.juego_en_curso:
            if self.tablero[i][j] == '-':
                self.tablero, ganador = jugar_turno(self.jugadores, self.jugador_actual, self.tablero, i + 1, j + 1)
                self.update_buttons()
                if ganador:
                    self.mostrar_ganador()
                elif all(celda != '-' for fila in self.tablero for celda in fila):
                    self.label.config(text="Fin del juego, no hay ganador")
                    self.disable_buttons()
                else:
                    self.jugador_actual = 1 - self.jugador_actual
                    self.label.config(text=f"Turno de: {self.jugadores[self.jugador_actual][0]}")
        else:
            messagebox.showinfo("Atención", "Haz click en 'Nueva Partida' para comenzar")

    def nueva_partida(self):
        self.juego_en_curso = True
        self.jugador_actual = 0
        self.tablero = [['-' for _ in range(3)] for _ in range(3)]
        self.update_buttons()
        self.label.config(text=f"Turno de: {self.jugadores[self.jugador_actual][0]}")
        self.reiniciar_button.config(state=tk.NORMAL)
        self.enable_buttons()

    def reiniciar_partida(self):
        self.nueva_partida()

    def mostrar_ganador(self):
        ganador = self.jugadores[self.jugador_actual][0]
        messagebox.showinfo("¡Ganador!", f"{ganador} ha ganado la partida.")
        self.disable_buttons()
        self.reiniciar_button.config(state=tk.NORMAL)

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

    def enable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='normal')

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.tablero[i][j])

def main():
    root = tk.Tk()
    app = TresEnRayaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
