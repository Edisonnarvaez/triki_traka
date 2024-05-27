
/*scripts.js*/
document.addEventListener("DOMContentLoaded", function() {
    const gameBoard = document.getElementById('game-board');
    const turnoJugador = document.getElementById('turno-jugador');
    const reiniciarBtn = document.getElementById('reiniciar-btn');
    let jugadores = [["Jugador 1", "X"], ["Jugador 2", "O"]];
    let jugadorActual = 0;
    let tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]];

    function dibujarTablero() {
        gameBoard.innerHTML = '';
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const cell = document.createElement('div');
                cell.className = 'cell';
                cell.textContent = tablero[i][j];
                //cell.innerHTML = tablero[i][j];
                cell.dataset.fila = i;
                cell.dataset.columna = j;
                cell.addEventListener('click', manejarClick);
                gameBoard.appendChild(cell);
            }
        }
        turnoJugador.textContent = jugadores[jugadorActual][0];
    }

    function manejarClick(event) {
        const fila = event.target.dataset.fila;
        const columna = event.target.dataset.columna;

        if (tablero[fila][columna] === '-') {
            tablero[fila][columna] = jugadores[jugadorActual][1];
            if (comprobarGanador()) {
                alert(jugadores[jugadorActual][0] + ' ha ganado!');
            } else if (tableroCompleto()) {
                alert('Empate!');
            } else {
                jugadorActual = 1 - jugadorActual;
                turnoJugador.textContent = jugadores[jugadorActual][0];
            }
            dibujarTablero();
        }
    }

    function reiniciarJuego() {
        tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]];
        jugadorActual = 0;
        dibujarTablero();
    }

    function comprobarGanador() {
        // Lógica para comprobar el ganador
    }

    function tableroCompleto() {
        return tablero.flat().every(cell => cell !== '-');
    }

    reiniciarBtn.addEventListener('click', reiniciarJuego);

    dibujarTablero();
});
