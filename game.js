function renderBoard(board) {
    const boardDiv = document.getElementById('game-board');
    boardDiv.innerHTML = ''; // Clear the board
    board.forEach((row, rowIndex) => {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';
        row.forEach((cell, cellIndex) => {  
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell';
            if (cell) {
                const [player, piece] = cell.split('-');
                if (player === 'A') {
                    cellDiv.classList.add('player-a');
                } else if (player === 'B') {
                    cellDiv.classList.add('player-b');
                }
                cellDiv.innerText = piece;
            } else {
                cellDiv.classList.add('empty');
            }
            rowDiv.appendChild(cellDiv);
        });
        boardDiv.appendChild(rowDiv);
    });
}
