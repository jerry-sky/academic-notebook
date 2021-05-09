
export class Point3D {

    constructor(
        public x: number,
        public y: number,
        public z: number
    ) { }

    public static from(p: Point3D): Point3D {
        return new Point3D(p.x, p.y, p.z)
    }

    public reset(p?: Point3D) {
        this.x = p?.x || 0
        this.y = p?.y || 0
        this.z = p?.z || 0
    }

    public negate() {
        this.x = -this.x
        this.y = -this.y
        this.z = -this.z
    }

    public translate(vector: Point3D) {
        this.x += vector.x
        this.y += vector.y
        this.z += vector.z
    }

    public translateY(value: number) {
        this.y += value
    }

    public scale(factor: number) {
        this.x *= factor
        this.y *= factor
        this.z *= factor
    }

    /**
     * Rotate the point around (0,0,0)
     * looking top-down on the XY plane.
     *
     * The unit of the `angle` argument is degrees.
     */
    public rotateXY(angle: number) {
        const sin = Math.sin(angle / 180 * Math.PI)
        const cos = Math.cos(angle / 180 * Math.PI)
        const newX = this.x * cos - this.y * sin
        const newY = this.x * sin + this.y * cos
        this.x = newX
        this.y = newY
    }

}

export class ListOfPoint3D extends Array<Point3D> {

    constructor(points?: Point3D[]) {
        if (points)
            super(...points)
        else
            super(0)
    }

    public static concatenate(...list: ListOfPoint3D[]) {
        return new ListOfPoint3D([].concat(...list))
    }

    public get flatList() {

        const flat = new Array<number>()

        this.forEach((vertex) => {
            flat.push(vertex.x)
            flat.push(vertex.y)
            flat.push(vertex.z)
        });

        return flat

    }

    public reset(p?: Point3D) {
        const origin = Point3D.from(this[0])
        origin.negate()
        origin.translate(p)
        this.forEach((vertex) => {
            vertex.translate(origin)
        })
    }

    public translate(vector: Point3D) {
        this.forEach((vertex) => {
            vertex.translate(vector)
        })
    }

    public translateY(value: number) {
        this.forEach((vertex) => {
            vertex.translateY(value)
        })
    }

    public scale(factor: number) {
        this.forEach((vertex) => {
            vertex.scale(factor)
        })
    }

    /**
     * Rotate by some amount given in degrees.
     */
    public rotateXY(angle: number) {
        this.forEach((vertex) => {
            vertex.rotateXY(angle)
        })
    }
}
