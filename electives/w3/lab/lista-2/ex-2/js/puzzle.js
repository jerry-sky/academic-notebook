
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

const Direction = {
    UP: 'up',
    DOWN: 'down',
    LEFT: 'left',
    RIGHT: 'right'
}

class Puzzle {
    constructor(columns, rows, onDone) {
        this.columns = columns;
        this.rows = rows;

        this.onDone = onDone;

        // create an array representing the grid
        this.grid = [];
        for (let y = 0; y < rows; y++) {
            for (let x = 0; x < columns; x++) {
                if(x === 0 && y === 0) {
                    // add an empty tile
                    this.grid.push(null);
                } else {
                    this.grid.push(new Point(x, y));
                }
            }
        }

        this.gridOriginal = JSON.stringify(this.grid);
    }

    /**
     * Get the value at (x, y).
     *
     * @param {Point} p
     */
    getCell(p) {
        return this.grid[this.pointToRawLocation(p)];
    }

    setCell(p, value) {
        this.grid[this.pointToRawLocation(p)] = value;
    }

    getNeighbours(p) {
        return [
            this.getCell(new Point(p.x + 1, p.y)),
            this.getCell(new Point(p.x - 1, p.y)),
            this.getCell(new Point(p.x, p.y + 1)),
            this.getCell(new Point(p.x, p.y - 1))
        ];
    }

    get currentLocation() {
        const rawValue = this.currentLocationRaw;
        const offset = Math.floor(rawValue / this.columns);
        return new Point(rawValue - offset * this.columns, offset);
    }

    get currentLocationRaw() {
        return this.grid.indexOf(null);
    }

    pointToRawLocation(p) {
        return this.columns * p.y + p.x;
    }

    get isDone() {
        if(JSON.stringify(this.grid) === this.gridOriginal) {
            return true;
        }
        return false;
    }

    shuffle(steps) {
        let i = 0;
        while (i < steps) {
            let dir = Math.floor(Math.random() * 4)
            if (dir === 4) dir = 3;

            if (this._move(Direction[Object.keys(Direction)[dir]])) {
                i++;
            }
        }
    }

    /**
     * Try to move the empty cell.
     *
     * @param {string} dir
     */
    _move(dir) {
        const cur = this.currentLocation;

        switch (dir) {
            case Direction.UP:
                if (cur.y > 0) {
                    const newLoc = new Point(cur.x, cur.y - 1);
                    this.setCell(cur, this.getCell(newLoc));
                    this.setCell(newLoc, null);
                    return true;
                }
                break;

            case Direction.DOWN:
                if (cur.y < this.rows - 1) {
                    const newLoc = new Point(cur.x, cur.y + 1);
                    this.setCell(cur, this.getCell(newLoc));
                    this.setCell(newLoc, null);
                    return true;
                }
                break;

            case Direction.LEFT:
                if (cur.x > 0) {
                    const newLoc = new Point(cur.x - 1, cur.y);
                    this.setCell(cur, this.getCell(newLoc));
                    this.setCell(newLoc, null);
                    return true;
                }
                break;

            case Direction.RIGHT:
                if (cur.x < this.columns - 1) {
                    const newLoc = new Point(cur.x + 1, cur.y);
                    this.setCell(cur, this.getCell(newLoc));
                    this.setCell(newLoc, null);
                    return true;
                }
                break;
        }

        return false;
    }

    move(dir) {
        this._move(dir);
        if(this.isDone) {
            this.onDone();
            return true;
        }
        return false;
    }
}
