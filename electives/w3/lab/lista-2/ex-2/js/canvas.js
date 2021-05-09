class MyCanvas {
    /**
     * @param {HTMLCanvasElement} canvas
     * @param {Puzzle} puzzle
     * @param {HTMLImageElement} imageElement
     */
    constructor(canvas, puzzle, imageElement) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.puzzle = puzzle;
        this.image = imageElement;

        /**
         * The current position of the mouse (while hovering).
         */
        this.currentHover = null;

        this.updateCanvasSize();

        this.setupEventListeners();

        this.redraw();

    }

    onMouseMove(event) {
        this.currentHover = new Point(event.offsetX, event.offsetY);
        this.redraw();
    }
    onMouseOut() {
        this.currentHover = null;
        this.redraw();
    }
    onMouseDown(event) {
        const x = event.offsetX;
        const y = event.offsetY;
        this.click(
            Math.floor(x / this.width * this.puzzle.columns),
            Math.floor(y / this.height * this.puzzle.rows)
        );
    }
    onWindowResize() {
        this.updateCanvasSize();
    }

    setupEventListeners() {
        this.listener1 = this.onMouseMove.bind(this);
        canvas.addEventListener('mousemove', this.listener1, true);
        this.listener2 = this.onMouseOut.bind(this);
        canvas.addEventListener('mouseout', this.listener2, true);
        this.listener3 = this.onMouseDown.bind(this)
        canvas.addEventListener('mousedown', this.listener3, true);
        this.listener4 = this.onWindowResize.bind(this)
        window.addEventListener('resize', this.listener4, true);
    }

    removeEventListeners() {
        canvas.removeEventListener('mousemove', this.listener1, true);
        canvas.removeEventListener('mouseout', this.listener2, true);
        canvas.removeEventListener('mousedown', this.listener3, true);
        window.removeEventListener('resize', this.listener4, true);
    }

    updateCanvasSize() {
        let newWidth = document.body.clientWidth;
        if (newWidth > 600) {
            newWidth = 600;
        }
        this.setCanvasSize(newWidth);
        this.redraw();
    }

    setCanvasSize(size) {
        this.canvas.width = size;
        this.canvas.height = size;
        this.width = size;
        this.height = size;
    }

    click(x, y) {
        const p = this.puzzle;
        let result = false;
        if (p.getCell(new Point(x - 1, y)) === null) {
            result = p.move(Direction.RIGHT);
        } else if (p.getCell(new Point(x + 1, y)) === null) {
            result = p.move(Direction.LEFT);
        } else if (p.getCell(new Point(x, y - 1)) === null) {
            result = p.move(Direction.DOWN);
        } else if (p.getCell(new Point(x, y + 1)) === null) {
            result = p.move(Direction.UP);
        }
        if (!result) {
            this.redraw();
        }
    }

    redraw() {
        const c = this.ctx;
        c.clearRect(0, 0, this.width, this.height);

        const cols = this.puzzle.columns;
        const rows = this.puzzle.rows;
        for (let y = 0; y < rows; y++) {
            for (let x = 0; x < cols; x++) {
                const cell = this.puzzle.getCell(new Point(x, y));

                const sliceX = x * this.width / cols;
                const sliceY = y * this.height / rows;
                const sliceWidth = this.width / cols;
                const sliceHeight = this.height / rows

                // draw the cell itself
                if (cell !== null) {
                    c.drawImage(
                        // image to draw
                        this.image,
                        // the (local to the image itself) position of the slice
                        cell.x * this.image.naturalWidth / cols,
                        cell.y * this.image.naturalHeight / rows,
                        // the size of the slice
                        this.image.naturalWidth / cols,
                        this.image.naturalHeight / rows,
                        // the position of the slice on the canvas
                        sliceX,
                        sliceY,
                        // the size of the slice on the canvas is the same as
                        // the slice’s size itself
                        sliceWidth,
                        sliceHeight
                    );
                } else {
                    c.fillStyle = "red";
                    c.fillRect(
                        sliceX,
                        sliceY,
                        sliceWidth,
                        sliceHeight
                    );
                }

                if (
                    this.currentHover !== null
                    // if the cell is currently under the mouse cursor
                    && this.currentHover.x >= x * sliceWidth
                    && this.currentHover.x <= (x + 1) * sliceWidth
                    && this.currentHover.y >= y * sliceHeight
                    && this.currentHover.y <= (y + 1) * sliceHeight
                    // and it’s a neighbour of the `null` cell
                    && this.puzzle.getNeighbours(new Point(x, y)).indexOf(null) !== -1
                ) {
                    c.fillStyle = "#ffffff44";
                    c.fillRect(
                        sliceX,
                        sliceY,
                        sliceWidth,
                        sliceHeight
                    );
                }
            }
        }
    }
}
