import { Point2D, Point3D, Projector } from '../types';

export class MyCanvas {

    /**
     * Coordinates of the turtle’s current position.
     */
    private _currentPos: Point3D;
    /**
     * The angle of the turtle.
     */
    private currentOrientationXY: number;
    private currentOrientationYZ: number;

    private maxX: number;
    private minX: number;
    private maxY: number;
    private minY: number;
    private rangeX: number;
    private rangeY: number;

    private context: CanvasRenderingContext2D;

    private points: Point3D[] = [];

    constructor(
        canvasElement: HTMLCanvasElement
    ) {
        this.maxX = canvasElement.width;
        this.minX = 0;
        this.maxY = canvasElement.height;
        this.minY = 0;
        this.rangeX = this.maxX - this.minX;
        this.rangeY = this.maxY - this.minY;

        this.context = canvasElement.getContext('2d')!;

        this.reset()

        this.setToPrimaryColour()

        this.context.lineWidth = 5;
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

    public rotateX(degrees: number) {

        const radian = degrees / 180 * Math.PI

        this.currentOrientationYZ += radian

        const cos = Math.cos(radian)
        const sin = Math.sin(radian)

        const points = [...this.points, this._currentPos]

        const middle = new Point3D(0, 0, 0)
        points.forEach((p) => {
            const y = (p.y - middle.y) * cos - (p.z - middle.z) * sin
            const z = (p.y - middle.y) * sin + (p.z - middle.z) * cos

            p.y = y + middle.y
            p.z = z + middle.z
        })

    }

    public rotateY(degrees: number) {

        const radian = degrees / 180 * Math.PI

        this.currentOrientationXY += radian

        const cos = Math.cos(radian)
        const sin = Math.sin(radian)

        const points = [...this.points, this._currentPos]

        const middle = new Point3D(0, 0, 0)
        points.forEach((p) => {
            const x = (p.z - middle.z) * sin - (p.x - middle.x) * cos
            const z = (p.z - middle.z) * cos + (p.x - middle.x) * sin

            p.x = x + middle.x
            p.z = z + middle.z
        })
    }


    public async redraw() {

        const c = this.context;

        c.clearRect(this.minX, this.minY, this.rangeX, this.rangeY)

        // draw all the lines
        this.setToPrimaryColour()
        c.moveTo(this.rangeX / 2, this.rangeY / 2)
        c.beginPath()
        for (let i = 0; i < this.points.length; i++) {
            const point = Projector.Project3DInto2D(this.points[i], this.rangeX, this.rangeY)
            // draw the line
            c.lineTo(point.x, point.y)
        }
        c.stroke()
        c.closePath()

        console.log(this.points)

        // mark the current position
        const cur = Projector.Project3DInto2D(this._currentPos, this.rangeX, this.rangeY)
        c.moveTo(cur.x, cur.y)
        c.beginPath()
        c.arc(
            cur.x, cur.y,
            10,
            -.75 * Math.PI - this.currentOrientationXY,
            -0.25 * Math.PI - this.currentOrientationXY
        )
        this.setToSecondaryColour()
        c.stroke()
        c.closePath()

    }

    /**
     * Move by some given value on the canvas.
     */
    public move(value: number): void {
        // calc the new position
        const x = Math.sin(this.currentOrientationXY) * value
        this._currentPos.x += x
        const y = Math.cos(this.currentOrientationXY) * value
        this._currentPos.y += y
        const z = Math.sin(this.currentOrientationYZ) * value
        this._currentPos.z += z

        // the new position
        const newX = this.currentPos.x
        const newY = this.currentPos.y
        const newZ = this.currentPos.z

        // save as a new line
        this.points.push(
            new Point3D(newX, newY, newZ),
        );
    }

    /**
     * Alter the current orientation.
     */
    public rotateXY(value: number): void {
        this.currentOrientationXY += value / 180 * Math.PI;
    }

    public rotateYZ(value: number): void {
        this.currentOrientationYZ += value / 180 * Math.PI;
    }

    public get currentPos() {
        return this._currentPos;
    }

    public reset() {
        this._currentPos = new Point3D(
            0,
            0,
            -200
        )

        this.currentOrientationXY = 0
        this.currentOrientationYZ = 0

        this.points = []
        this.points.push(new Point3D(
            0,
            0,
            -200
        ))

        this.redraw()
    }

}
