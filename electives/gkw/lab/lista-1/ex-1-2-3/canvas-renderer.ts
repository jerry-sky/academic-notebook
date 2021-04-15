import { Point2D } from '../types';

export interface CanvasRenderer {

    currentPos: Point2D;

    redraw(): void;

    move(value: number): void;

    rotate(value: number): void;

    reset(): void;

}
