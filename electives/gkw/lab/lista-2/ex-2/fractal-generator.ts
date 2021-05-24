import { ListOfPoint3D, Point3D } from '../types'

function kochEdge(level: number, z: number): ListOfPoint3D {
    if (level === 1) {
        return new ListOfPoint3D([
            new Point3D(-1, 0, z),
            new Point3D(-1 / 3, 0, z),
            new Point3D(0, Math.sqrt(3) / 3, z),
            new Point3D(1 / 3, 0, z),
            new Point3D(1, 0, z),
        ])
    } else {
        const first = kochEdge(level - 1, z)
        first.scale(1 / 3)
        first.translate(new Point3D(-2 / 3, 0, 0))
        const second = kochEdge(level - 1, z)
        second.translate(new Point3D(1, 0, 0))
        second.rotateXY(60)
        second.translate(new Point3D(-1, 0, 0))
        second.scale(1 / 3)
        const third = kochEdge(level - 1, z)
        third.translate(new Point3D(1, 0, 0))
        third.rotateXY(-60)
        third.translate(new Point3D(0, Math.sqrt(3), 0))
        third.scale(1 / 3)
        // third.rotateXY(-60)
        const fourth = kochEdge(level - 1, z)
        fourth.translate(new Point3D(2, 0, 0))
        fourth.scale(1 / 3)
        return ListOfPoint3D.concatenate(
            first,
            second,
            third,
            fourth
        )
    }
}


export function GenerateKoch(level: number, z: number) {

    const one = kochEdge(level, z)
    one.translate(new Point3D(0, 1, 0))
    const two = kochEdge(level, z)
    two.translate(new Point3D(1, 0, 0))
    two.rotateXY(-120)
    two.translate(new Point3D(1, 1, 0))
    const three = kochEdge(level, z)
    three.translate(new Point3D(1, 0, 0))
    three.rotateXY(120)
    three.translate(new Point3D(0, Math.sqrt(3) * -5 / 12, 0))

    const koch = ListOfPoint3D.concatenate(one, two, three)

    return koch

}

export function GenerateSierpiński(level: number, z: number) {

    if (level === 1) {
        return new ListOfPoint3D([
            new Point3D(-1, -1, z),
            new Point3D(0, Math.sqrt(3) - 1, z),
            new Point3D(1, -1, z),
        ])
    } else {
        const one = GenerateSierpiński(level - 1, z)
        one.translate(new Point3D(-1, -1, 0))
        one.scale(0.5)
        const two = GenerateSierpiński(level - 1, z)
        two.translate(new Point3D(1, 1, 0))
        two.scale(0.5)
        two.translate(new Point3D(
            -0.5,
            -1 + 0.5 * Math.sqrt(3),
            0
        ))
        const three = GenerateSierpiński(level - 1, z)
        three.translate(new Point3D(1, 1, 0))
        three.scale(0.5)
        three.translate(new Point3D(
            0,
            -1,
            0
        ))

        const vertices = ListOfPoint3D.concatenate(one, two, three)

        return vertices
    }

}
