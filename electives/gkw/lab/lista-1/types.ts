
/**
 * Simple class that holds two values: `x` and `y`.
 */
export class Point2D {

    constructor(
        public x: number,
        public y: number
    ) { }

}

export class Point3D extends Point2D {

    constructor(
        public x: number,
        public y: number,
        public z: number
    ) {
        super(x, y)
    }

}

export class Line3D {

    constructor(
        public begin: Point3D,
        public end: Point3D
    ) { }

}

export class Cuboid {

    private _lines: Line3D[]
    private _vertices: Point3D[]

    private middle: Point3D

    private maxPoints: Point3D[]

    constructor(
        x: number,
        y: number,
        z: number,
        width: number,
        height: number,
        depth: number
    ) {
        this.middle = new Point3D(x, y, z)
        // prepare all the cuboid vertices
        const v = [
            new Point3D(x - width / 2, y - height / 2, z - depth / 2),
            new Point3D(x - width / 2, y + height / 2, z - depth / 2),
            new Point3D(x + width / 2, y + height / 2, z - depth / 2),
            new Point3D(x + width / 2, y - height / 2, z - depth / 2),
            new Point3D(x - width / 2, y - height / 2, z + depth / 2),
            new Point3D(x - width / 2, y + height / 2, z + depth / 2),
            new Point3D(x + width / 2, y + height / 2, z + depth / 2),
            new Point3D(x + width / 2, y - height / 2, z + depth / 2),
        ]
        this._lines = [
            // “lower” rectangle
            new Line3D(v[0], v[1]),
            new Line3D(v[1], v[2]),
            new Line3D(v[2], v[3]),
            new Line3D(v[3], v[0]),
            // “connecting” lines between the “lower” and “upper” rectangles
            new Line3D(v[0], v[4]),
            new Line3D(v[1], v[5]),
            new Line3D(v[2], v[6]),
            new Line3D(v[3], v[7]),
            // “upper” rectangle
            new Line3D(v[4], v[5]),
            new Line3D(v[5], v[6]),
            new Line3D(v[6], v[7]),
            new Line3D(v[7], v[4])
        ]
        this._vertices = v
        // save the vertices that help in determining if given point is inside the cuboid
        this.maxPoints = [
            v[0],
            v[6]
        ]
    }

    public get lines() {
        return this._lines
    }

    public get vertices() {
        return this._vertices
    }

    public isInside(point: Point3D) {
        const x = point.x
        const y = point.y
        const z = point.z
        const one = this.maxPoints[0]
        const two = this.maxPoints[1]
        if (
            x >= one.x && x <= two.x
            && y >= one.y && y <= two.y
            && z >= one.z && z <= two.z
        ) {
            return true
        }
        return false
    }

    public rotateX(radian: number) {

        const cos = Math.cos(radian)
        const sin = Math.sin(radian)

        this.vertices.forEach((p) => {
            const y = (p.y - this.middle.y) * cos - (p.z - this.middle.z) * sin
            const z = (p.y - this.middle.y) * sin + (p.z - this.middle.z) * cos

            p.y = y + this.middle.y
            p.z = z + this.middle.z
        })
    }

    public rotateY(radian: number) {

        const cos = Math.cos(radian)
        const sin = Math.sin(radian)

        this.vertices.forEach((p) => {
            const x = (p.z - this.middle.z) * sin - (p.x - this.middle.x) * cos
            const z = (p.z - this.middle.z) * cos + (p.x - this.middle.x) * sin

            p.x = x + this.middle.x
            p.z = z + this.middle.z
        })
    }

}

export class Projector {

    public static FocalLength = 100

    public static Project3DInto2D(point: Point3D, width: number, height: number): Point2D {
        const x = point.x * (Projector.FocalLength / point.z) + 0.5 * width;
        const y = point.y * (Projector.FocalLength / point.z) + 0.5 * height;

        return new Point2D(x, y)
    }

}

