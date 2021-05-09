import { Point3D } from '../types'
import { MyCanvas, Shape } from './canvas'
import { GenerateKoch, GenerateSierpiński } from './fractal-generator'

const canvasElement: HTMLCanvasElement = document.querySelector('canvas')
const formElement: HTMLFormElement = document.querySelector('form')
const fractalSelectElement: HTMLSelectElement = document.querySelector('select')
const colourInputElement: HTMLInputElement = document.querySelector('#colour-input')
const fractalLevelInputElement: HTMLInputElement = document.querySelector('#level-input')

const myCanvas = new MyCanvas(canvasElement)

myCanvas.startAnimationLoop()

formElement.onsubmit = (event) => {

    event.preventDefault()

    const chosenFractal = fractalSelectElement.value
    const fractalLevel = parseInt(fractalLevelInputElement.value)
    const colour = colourInputElement.value
        .replace(/\s+/g, '')
        .split(',')
        .map((raw) => parseFloat(raw))

    if (colour.length !== 3) {
        alert('please provide a valid RGB colour tuple')
        return
    }

    for (const c of colour) {
        if (isNaN(c)) {
            alert('please provide a valid RGB colour tuple')
            return
        }
    }

    if (isNaN(fractalLevel) || fractalLevel < 1) {
        alert('please provide fractal level that is an integer number greater than 0')
        return
    }

    let fractal: Shape
    if (chosenFractal === 'Koch') {
        fractal = {
            colour,
            drawType: myCanvas.DrawTypes.LINE_LOOP,
            points: GenerateKoch(fractalLevel, 0)
        }
    } else {
        fractal = {
            colour,
            drawType: myCanvas.DrawTypes.TRIANGLES,
            points: GenerateSierpiński(fractalLevel, 0)
        }
    }

    fractal.points.scale(0.5)

    myCanvas.addShape(fractal)

}

window.addEventListener('keydown', (event) => {

    const shape = myCanvas.lastAddedShape

    if (!shape) return

    switch (event.key) {
        case 'J':
            shape.points.translate(new Point3D(
                0,
                0,
                -0.1
            ))
            break
        case 'j':
            shape.points.translate(new Point3D(
                0,
                -0.1,
                0
            ))
            break
        case 'K':
            shape.points.translate(new Point3D(
                0,
                0,
                0.1
            ))
            break
        case 'k':
            shape.points.translate(new Point3D(
                0,
                0.1,
                0
            ))
            break
        case 'h':
            shape.points.translate(new Point3D(
                -0.1,
                0,
                0
            ))
            break
        case 'l':
            shape.points.translate(new Point3D(
                0.1,
                0,
                0
            ))
            break
    }

})
