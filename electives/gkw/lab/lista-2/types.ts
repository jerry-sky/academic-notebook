
export class Point3D {

    constructor(
        public x: number,
        public y: number,
        public z: number
    ) { }

    public translate(vector: Point3D) {
        this.x += vector.x
        this.y += vector.y
        this.z += vector.z
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

    public translate(vector: Point3D) {
        this.forEach((vertex) => {
            vertex.translate(vector)
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
