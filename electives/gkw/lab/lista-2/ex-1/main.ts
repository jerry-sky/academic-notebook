import { MyCanvas } from './canvas'

const canvasElement: HTMLCanvasElement = document.querySelector('canvas')
const inputElement: HTMLTextAreaElement = document.querySelector('textarea')
const selectElement: HTMLSelectElement = document.querySelector('select')
const formElement: HTMLFormElement = document.querySelector('form')

const vertexGenericLocationIndex = 10

console.log('Initializing a new canvas. Setting the attrib location to', vertexGenericLocationIndex)
const myCanvas = new MyCanvas(canvasElement, vertexGenericLocationIndex)
console.log('Initialized. Attrib location:')
myCanvas.printAttribLocation()

console.log('All active attributes:')
myCanvas.printAllActiveAttributes()
console.log('All active uniforms:')
myCanvas.printAllActiveUniforms()

formElement.onsubmit = (event) => {

    event.preventDefault()

    const drawType = myCanvas.DrawTypes[selectElement.value] as number

    const verticesRaw = inputElement.value.replace(/\s+/g, '')
    const vertices: number[] = []
    verticesRaw.split(',').forEach((vertexRaw) => {
        const parsed = parseFloat(vertexRaw)
        if (!isNaN(parsed)) {
            vertices.push(parsed)
        }
    })

    myCanvas.draw2DUniformColor(vertices, drawType, [1, 0, 1])

}
