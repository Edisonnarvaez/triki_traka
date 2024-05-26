// static/js/scripts.js
document.addEventListener("DOMContentLoaded", () => {
    const board = document.getElementById('game-board');

    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('div');
        cell.addEventListener('click', () => {
            if (cell.textContent === '') {
                cell.textContent = 'X'; // O 'O', según el turno
            }
        });
        board.appendChild(cell);
    }
});
