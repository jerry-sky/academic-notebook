const canvas = document.querySelector('canvas');

let puzzle, myCanvas;
let image = document.querySelector('img');
let cols = 4;
let rows = 4;

function makeNewGame() {

    const values = getGameSize();
    if (values !== null) {
        cols = values[0];
        rows = values[1];
        if (!(cols > 1 && rows > 1)) {
            alert('Both provided numbers should be greater than one.');
            return;
        }
    } else {
        alert('Please provide valid game size parameters below.');
        return;
    }

    if (puzzle && myCanvas) {
        myCanvas.removeEventListeners();
        delete puzzle;
        delete myCanvas;
    }

    puzzle = new Puzzle(cols, rows, () => {
        alert('You’ve completed the puzzle.');
        makeNewGame();
    });
    while (puzzle.isDone) {
        puzzle.shuffle(cols * rows * 5);
    }

    myCanvas = new MyCanvas(canvas, puzzle, image);

    canvas.scrollIntoView();

    // console.log(puzzle.grid);
    // setTimeout(() => {
    //     myCanvas.redraw();
    // }, 1000);

}

function getGameSize() {
    /**
     * @type HTMLInputElement
     */
    const colsInput = document.getElementById('columns-input');
    /**
     * @type HTMLInputElement
     */
    const rowsInput = document.getElementById('rows-input');

    const cols = Number(colsInput.value);
    const rows = Number(rowsInput.value);

    if (isNaN(cols) || isNaN(rows)) {
        return null;
    } else {
        return [cols, rows];
    }
}

images.forEach((img) => {
    img.addEventListener('click', () => {
        image = img;
        makeNewGame();
    })
});
