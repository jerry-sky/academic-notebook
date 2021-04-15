import { MyCanvas } from "./my-canvas";
import { LogoInterpreter } from './interpreter';
import { CanvasRenderer } from './canvas-renderer';
import { SVGCanvas } from './svg-canvas';

// get all the necessary elements
const form = document.getElementById('execution-form')
const input = document.getElementById('command-input') as HTMLInputElement
const canvas = document.getElementById('canvas') as HTMLCanvasElement
const svgCanvas = document.getElementsByTagName('svg')[0] as unknown as SVGElement
const clearButton = document.getElementById('clear-button') as HTMLButtonElement
const switchCanvasButton = document.getElementById('switch-canvas') as HTMLButtonElement

const exampleButtons = document.getElementsByClassName('example-button') as HTMLCollectionOf<HTMLButtonElement>

if (form !== null && input !== null && canvas !== null && svgCanvas !== null && clearButton !== null) {

    // by default hide the SVG canvas
    svgCanvas.style.display = 'none'

    let myCanvas: CanvasRenderer = new MyCanvas(canvas)

    myCanvas.redraw()

    switchCanvasButton.onclick = (event: Event) => {
        if (myCanvas instanceof MyCanvas) {
            canvas.style.display = 'none'
            svgCanvas.style.display = 'initial'
            switchCanvasButton.innerText = 'Switch canvas mode, current: SVG'
            myCanvas = new SVGCanvas(svgCanvas)
        } else {
            svgCanvas.style.display = 'none'
            canvas.style.display = 'initial'
            switchCanvasButton.innerText = 'Switch canvas mode, current: CANVAS'
            myCanvas = new MyCanvas(canvas)
        }
        myCanvas.redraw()
    }

    form.onsubmit = (event: Event) => {

        // prevent refreshing the page
        event.preventDefault()

        setTimeout(async () => {

            // get the value
            const tokens = input.value

            const interpreter = new LogoInterpreter(myCanvas)

            await interpreter.ExecuteCommandStack(tokens)

            await myCanvas.redraw()

        }, 50)
    }

    clearButton.onclick = (event: Event) => {

        event.preventDefault()

        myCanvas.reset()

    }

    const examples = [
        `
F 100
R 90
F 100
R 90
F 100
R 90
F 100
        `,
        `
RE 5 [F 100 R 72]
        `,
        `
RE 9 [F 100 R 40]
        `,
        `
BE koch 2 :st :a
    IF :st = 0 [ F :a TE ]
    koch CA :st - 1 CA :a / 3 R 60
    koch CA :st - 1 CA :a / 3 L 120
    koch CA :st - 1 CA :a / 3 R 60
    koch CA :st - 1 CA :a / 3
EN


BE star 2 :st :a
    RE 3 [ koch :st :a L 120]
EN

star 5 300
        `,
        `
BE troj 1 :a
    RE 3 [F :a R 120]
EN

BE sierp 2 :n :a
    IF :n = 0 [troj :a TE]
    troj :a

    sierp CA :n - 1 CA :a / 2
    F CA :a / 2
    sierp CA :n - 1 CA :a / 2
    R 60
    F CA :a / 2 R 60

    sierp CA :n - 1 CA :a / 2
    L 60 B CA :a / 2
    L 60 B CA :a / 2
EN

BE sierpinski 2 :n :a
    R 30
    sierp :n :a
EN

sierpinski 5 300

        `
    ]

    for (let i = 0; i < exampleButtons.length; i++) {
        const button = exampleButtons[i]
        const example = examples[i]

        button.onclick = (event: Event) => {
            input.value = example
        }
    }

}
