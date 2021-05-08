import { Point3D } from '../types'
import { MyCanvas, Shape } from './canvas'
import { GenerateKoch, GenerateSierpiński } from './fractal-generator'

const canvasElement: HTMLCanvasElement = document.querySelector('canvas')
const formElement: HTMLFormElement = document.querySelector('form')
const fractalSelectElement: HTMLSelectElement = document.querySelector('select')
const colourInputElement: HTMLInputElement = document.querySelector('#colour-input')

const myCanvas = new MyCanvas(canvasElement)

myCanvas.startAnimationLoop()

formElement.onsubmit = (event) => {

    event.preventDefault()

    const chosenFractal = fractalSelectElement.value
    const colour = colourInputElement.value
        .replace(/\s+/g, '')
        .split(',')
        .map((raw) => parseFloat(raw))

    if (colour.length !== 3) {
        alert('please provide a valid RGB colour value')
        return
    }

    let fractal: Shape
    if (chosenFractal === 'Koch') {
        fractal = {
            colour,
            drawType: myCanvas.DrawTypes.LINE_LOOP,
            points: GenerateKoch(5, 0.5, 0)
        }
    } else {
        fractal = {
            colour,
            drawType: myCanvas.DrawTypes.TRIANGLES,
            points: GenerateSierpiński(5, 0.5, 0)
        }
    }

    myCanvas.addShape(fractal)

}

window.addEventListener('keydown', (event) => {

    const shape = myCanvas.lastAddedShape

    if (event.key === 'ArrowDown') {
        shape.points.translate(new Point3D(
            0,
            0,
            -0.1
        ))
    } else if (event.key === 'ArrowUp') {
        shape.points.translate(new Point3D(
            0,
            0,
            0.1
        ))
    }

})
