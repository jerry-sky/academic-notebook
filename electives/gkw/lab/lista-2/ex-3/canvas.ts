import { ListOfPoint3D } from '../types';
import { vertexShaderRaw, fragmentShaderRaw } from './shaders'

export type Colour = number[];

export interface Shape {
    points: ListOfPoint3D
    drawType: number
    colour: Colour
}

export class MyCanvas {

    /**
     * WebGL context.
     */
    private gl: WebGLRenderingContext

    private program: WebGLProgram

    /**
     * List of all shapes the user wants to draw.
     */
    private _shapes: Shape[] = []
    public addShape(newShape: Shape) {
        return this._shapes.push(newShape)
    }
    public get shapes() {
        return this._shapes
    }
    public resetShapes() {
        this._shapes = []
    }

    public readonly DrawTypes: {
        POINTS: number,
        LINES: number,
        LINE_STRIP: number,
        LINE_LOOP: number,
        TRIANGLES: number,
        TRIANGLE_STRIP: number,
        TRIANGLE_FAN: number,
    }

    constructor(private canvas: HTMLCanvasElement) {
        this.gl = this.canvas.getContext('webgl')

        if (!this.gl) {
            this.gl = this.canvas.getContext('experimental-webgl') as WebGLRenderingContext
        }

        if (!this.gl) {
            throw new Error('WebGL not supported')
        }

        // initialize pseudo-enum containing types of primitive shapes
        this.DrawTypes = {
            POINTS: this.gl.POINTS,
            LINES: this.gl.LINES,
            LINE_STRIP: this.gl.LINE_STRIP,
            LINE_LOOP: this.gl.LINE_LOOP,
            TRIANGLES: this.gl.TRIANGLES,
            TRIANGLE_STRIP: this.gl.TRIANGLE_STRIP,
            TRIANGLE_FAN: this.gl.TRIANGLE_FAN,
        }

        this.clearScreen()
        this.prepare()

        this.gl.lineWidth(5)

        // enable depth
        this.gl.enable(this.gl.DEPTH_TEST)
    }

    private prepare() {
        const gl = this.gl;
        const vertexShader = this.prepareShader(vertexShaderRaw.source, gl.VERTEX_SHADER)
        const fragmentShader = this.prepareShader(fragmentShaderRaw.source, gl.FRAGMENT_SHADER)

        this.program = this.prepareProgram([vertexShader, fragmentShader])
    }

    /**
     * Wipe the whole screen clean.
     */
    private clearScreen() {
        this.gl.clearColor(0, 0, 0, 1)
        this.gl.clear(this.gl.COLOR_BUFFER_BIT | this.gl.DEPTH_BUFFER_BIT)
    }

    private prepareShader(source: string, shaderType: number) {
        const gl = this.gl

        const shader = gl.createShader(shaderType)

        gl.shaderSource(shader, source)
        gl.compileShader(shader)

        if (!this.gl.getShaderParameter(shader, this.gl.COMPILE_STATUS)) {
            throw new Error('Shader compilation error: ' + this.gl.getShaderInfoLog(shader))
        }

        return shader;
    }

    private prepareProgram(shaders: WebGLShader[]) {
        const gl = this.gl;

        const program = gl.createProgram()
        shaders.forEach((shader) => {
            gl.attachShader(program, shader)
        });

        gl.linkProgram(program)
        if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
            throw new Error('Program linking error: ' + this.gl.getProgramInfoLog(program))
        }

        gl.validateProgram(program)
        if (!gl.getProgramParameter(program, gl.VALIDATE_STATUS)) {
            throw new Error('Program validating error: ' + gl.getProgramInfoLog(program))
        }

        return program;
    }

    public startAnimationLoop() {

        this.clearScreen()

        this._shapes.forEach((shape) => {
            this.draw3DUniformColor(shape.points, shape.drawType, shape.colour)
        })

        window.requestAnimationFrame(this.startAnimationLoop.bind(this))
    }

    private draw3DUniformColor(vertices: ListOfPoint3D, drawType: number, colour: Colour) {
        const gl = this.gl

        const vertexBuffer = gl.createBuffer()
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer)
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices.flatList), gl.STATIC_DRAW)

        const positionAttribLocation = gl.getAttribLocation(this.program, vertexShaderRaw.attributes.vertPosition)

        gl.enableVertexAttribArray(positionAttribLocation)
        gl.vertexAttribPointer(
            positionAttribLocation, // the vertex position attrib
            3, // 3D
            gl.FLOAT,
            false,
            3 * Float32Array.BYTES_PER_ELEMENT,
            0 // offset equal to zero, because we’re not expecting any additional information in the given array
        )

        gl.useProgram(this.program)
        const colourUniformLocation = gl.getUniformLocation(this.program, fragmentShaderRaw.uniforms.colour)
        gl.uniform3fv(colourUniformLocation, new Float32Array(colour))

        gl.drawArrays(drawType, 0, vertices.length)
    }

}
