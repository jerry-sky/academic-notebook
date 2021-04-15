import { Point2D } from '../types';
import { CanvasRenderer } from './canvas-renderer'

export class MyCanvas implements CanvasRenderer {

    /**
     * Coordinates of the turtle’s current position.
     */
    private _currentPos: Point2D;
    /**
     * The angle of the turtle.
     */
    private _currentOrientation: number;

    private maxX: number;
    private minX: number;
    private maxY: number;
    private minY: number;
    private rangeX: number;
    private rangeY: number;

    private context: CanvasRenderingContext2D;

    private points: Point2D[] = [];

    constructor(
        canvasElement: HTMLCanvasElement
    ) {
        this.maxX = canvasElement.width;
        this.minX = 0;
        this.maxY = canvasElement.height;
        this.minY = 0;
        this.rangeX = this.maxX - this.minX;
        this.rangeY = this.maxY - this.minY;

        this._currentPos = new Point2D(this.rangeX / 2, this.rangeY / 2);
        this._currentOrientation = 0;
        this.points.push(new Point2D(this.rangeX / 2, this.rangeY / 2))

        this.context = canvasElement.getContext('2d')!;

        this.context.lineWidth = 5;
        this.context.strokeStyle = "#000000";
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

    public async redraw() {

        const c = this.context;

        c.clearRect(this.minX, this.minY, this.rangeX, this.rangeY);

        // draw all the lines
        this.setToPrimaryColour();
        c.moveTo(this.rangeX / 2, this.rangeY / 2)
        c.beginPath();
        for (let i = 0; i < this.points.length; i++) {
            const point = this.points[i]
            // draw the line
            c.lineTo(point.x, point.y);
        }
        c.stroke();
        c.closePath();

        // mark the current position
        const cur = this._currentPos;
        c.moveTo(cur.x, cur.y);
        c.beginPath();
        c.arc(
            cur.x, cur.y,
            10,
            -.75 * Math.PI - this._currentOrientation,
            -0.25 * Math.PI - this._currentOrientation
        );
        this.setToSecondaryColour();
        c.stroke();
        c.closePath();

    }

    /**
     * Move by some given value on the canvas.
     */
    public move(value: number): void {
        // calc the new position
        const x = Math.sin(this._currentOrientation) * value;
        this._currentPos.x += x;
        const y = Math.cos(this._currentOrientation) * value;
        this._currentPos.y += y;

        // the new position
        const newX = this.currentPos.x;
        const newY = this.currentPos.y;

        // save as a new line
        this.points.push(
            new Point2D(newX, newY),
        );
    }

    /**
     * Alter the current orientation.
     */
    public rotate(value: number): void {
        this._currentOrientation += value / 180 * Math.PI;
    }

    public get currentPos() {
        return this._currentPos;
    }

    public reset() {
        this._currentPos = new Point2D(this.rangeX / 2, this.rangeY / 2)
        this._currentOrientation = 0
        this.context.clearRect(this.minX, this.minY, this.rangeX, this.rangeY);
        this.points = []
        this.points.push(new Point2D(this.rangeX / 2, this.rangeY / 2))
        this.redraw()
    }

}
