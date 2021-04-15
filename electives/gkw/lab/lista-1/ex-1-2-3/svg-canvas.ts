import { Point2D } from '../types';
import { CanvasRenderer } from './canvas-renderer';

export class SVGCanvas implements CanvasRenderer {

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

    private points: Point2D[] = []

    constructor(
        private svgCanvas: SVGElement
    ) {
        this.minX = 0
        this.minY = 0
        this.maxX = this.svgCanvas.clientWidth
        this.maxY = this.svgCanvas.clientHeight
        this.rangeX = this.maxX - this.minX;
        this.rangeY = this.maxY - this.minY;

        this._currentPos = new Point2D(this.rangeX / 2, this.rangeY / 2);
        this._currentOrientation = 0;
        this.points.push(new Point2D(this.rangeX / 2, this.rangeY / 2))

    }

    public get currentPos() {
        return this._currentPos
    }

    redraw(): void {

        const c = this.svgCanvas

        // clear
        c.innerHTML = ''

        // draw all the lines
        let stroke = '<polyline points="'
        for (let i = 0; i < this.points.length; i++) {
            const point = this.points[i]
            // draw the line
            stroke += point.x.toString()
            stroke += ','
            stroke += point.y.toString()
            stroke += ' '
        }
        stroke += '" style="fill: none; stroke: black;stroke-width:3;" />'

        c.innerHTML += stroke

        // mark the current position
        const cur = this._currentPos;
        let marker = '<polygon points="0,-10 -10,10 10,10" transform="translate('
        marker += cur.x.toString()
        marker += ', '
        marker += cur.y.toString()
        marker += ') rotate('
        marker += (this._currentOrientation / Math.PI * 180).toString()
        marker += ')" style="fill: none; stroke: #ff00ff;stroke-width:5" />'

        c.innerHTML += marker

    }

    move(value: number): void {
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

    rotate(value: number): void {
        this._currentOrientation += value / 180 * Math.PI;
    }

    public reset() {
        this._currentPos = new Point2D(this.rangeX / 2, this.rangeY / 2)
        this._currentOrientation = 0
        this.points = []
        this.points.push(new Point2D(this.rangeX / 2, this.rangeY / 2))
        this.redraw()
    }

}
