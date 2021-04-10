import { Cuboid, Point3D } from '../types'
import { MyCanvas } from './my-canvas'

const canvas = document.getElementById('canvas') as HTMLCanvasElement

const myCanvas = new MyCanvas(canvas)

function getRandomInt(max: number) {
    return Math.floor(Math.random() * max)
}

// generate the cuboids
const cuboidCount = 30
const z = -150
const width = 50
const height = 50
const depth = 25
for (let i = 0; i < cuboidCount; i++) {

    const x = getRandomInt(myCanvas.width) - myCanvas.width / 2
    const y = getRandomInt(myCanvas.height) - myCanvas.height / 2

    const cuboid = new Cuboid(
        x, y, z,
        width, height, depth
    )

    myCanvas.cuboids.push(cuboid)

}

myCanvas.resetPlayer(new Point3D(
    0,
    -myCanvas.height/2,
    z
))

myCanvas.targetCuboid = new Cuboid(
    0, myCanvas.height/2, z,
    width, height, depth * .3
)

document.addEventListener('keydown', (event: KeyboardEvent) => {

    switch(event.key) {
        case 'ArrowUp':
            myCanvas.movePlayer(0, 10)
            break
        case 'ArrowDown':
            myCanvas.movePlayer(0, -10)
            break
        case 'ArrowLeft':
            myCanvas.movePlayer(10, 0)
            break
        case 'ArrowRight':
            myCanvas.movePlayer(-10, 0)
            break
    }

    myCanvas.redraw()

    if(myCanvas.checkIfPlayerWon()) {
        alert('You’ve won!')
        location.reload()
    }

})

myCanvas.redraw()
