import { Cuboid, Point3D, Projector } from '../types';

export class MyCanvas {

    /**
     * Player’s current position.
     */
    private _currentPos: Point3D;

    private _width: number;
    private _height: number;

    private context: CanvasRenderingContext2D;

    public cuboids: Cuboid[] = [];

    public targetCuboid: Cuboid

    constructor(
        canvasElement: HTMLCanvasElement
    ) {
        this._width = canvasElement.width
        this._height = canvasElement.height

        this.context = canvasElement.getContext('2d')!;

        this.reset()

        this.context.lineWidth = 5;
    }

    public get width() {
        return this._width
    }

    public get height() {
        return this._height
    }

    /**
     * Set stroke colour to the primary colour.
     */
    private setToPrimaryColour() {
        this.context.strokeStyle = "#000000";
    }

    /**
     * Set stroke colour to the secondary colour.
     */
    private setToSecondaryColour() {
        this.context.strokeStyle = "#ff00ff";
    }

    public redraw() {

        const c = this.context;

        // clear the canvas
        c.clearRect(0, 0, this._width, this._height);

        // draw all the cuboids
        this.setToPrimaryColour();
        this.cuboids.forEach((cuboid) => {
            cuboid.lines.forEach((line) => {
                const begin = Projector.Project3DInto2D(line.begin, this._width, this._height)
                const end = Projector.Project3DInto2D(line.end, this._width, this._height)
                c.beginPath()
                c.moveTo(begin.x, begin.y)
                c.lineTo(end.x, end.y)
                c.closePath()
                c.stroke();
            })
        })

        if (this.targetCuboid) {
            // draw the target cuboid
            this.setToSecondaryColour()
            this.targetCuboid.lines.forEach((line) => {
                const begin = Projector.Project3DInto2D(line.begin, this._width, this._height)
                const end = Projector.Project3DInto2D(line.end, this._width, this._height)
                c.beginPath()
                c.moveTo(begin.x, begin.y)
                c.lineTo(end.x, end.y)
                c.closePath()
                c.stroke();
            })
        }

        // draw the player
        const cur = Projector.Project3DInto2D(this._currentPos, this._width, this._height)
        this.setToSecondaryColour()
        c.beginPath()
        this.context.arc(
            cur.x, cur.y,
            10,
            0, 2 * Math.PI
        )
        c.stroke()
        c.closePath()

    }

    public get currentPos() {
        return this._currentPos;
    }

    public reset() {
        this._currentPos = new Point3D(0, 0, 0)
        this.cuboids = []
        this.redraw()
    }

    public resetPlayer(point: Point3D) {
        this._currentPos = point
    }

    public checkIfPlayerWon() {

        if(this.targetCuboid && this.targetCuboid.isInside(this._currentPos)) {
            return true
        }
        return false

    }

    public movePlayer(x: number, y: number) {
        this._currentPos.x += x
        this._currentPos.y += y
        // check if the player hit a wall
        for (let i = 0; i < this.cuboids.length; i++) {
            const cuboid = this.cuboids[i]
            if (cuboid.isInside(this._currentPos)) {
                // player has hit the wall
                this._currentPos.x -= x
                this._currentPos.y -= y
                return
            }
        }
    }

}
