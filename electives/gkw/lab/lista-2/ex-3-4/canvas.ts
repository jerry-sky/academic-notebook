import { ListOfPoint3D, Point3D } from '../types';
import { vertexShaderRaw, fragmentShaderRaw, vertexTextureShaderRaw, fragmentTextureShaderRaw } from './shaders'

export type Colour = number[];

export interface Shape {
    points: ListOfPoint3D
    drawType: number
    colour: Colour
}

export interface TextureSquare {
    origin: Point3D
    size: number
    texture: HTMLImageElement
}

export class MyCanvas {

    /**
     * WebGL context.
     */
    private gl: WebGLRenderingContext

    private program: WebGLProgram
    private programTex: WebGLProgram

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

    private _textureSquares: TextureSquare[] = []
    public addTextureSquare(newSquare: TextureSquare) {
        return this._textureSquares.push(newSquare)
    }
    public get textureSquares() {
        return this._textureSquares
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
        // this.gl.enable(this.gl.CULL_FACE)
        // this.gl.frontFace(this.gl.CCW)
        this.gl.cullFace(this.gl.BACK)
    }

    private prepare() {
        const gl = this.gl;

        const vertexShader = this.prepareShader(vertexShaderRaw.source, gl.VERTEX_SHADER)
        const fragmentShader = this.prepareShader(fragmentShaderRaw.source, gl.FRAGMENT_SHADER)
        this.program = this.prepareProgram([vertexShader, fragmentShader])

        const vertexTextureShader = this.prepareShader(vertexTextureShaderRaw.source, gl.VERTEX_SHADER)
        const fragmentTextureShader = this.prepareShader(fragmentTextureShaderRaw.source, gl.FRAGMENT_SHADER)
        this.programTex = this.prepareProgram([vertexTextureShader, fragmentTextureShader])
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

        this._textureSquares.forEach((square) => {
            this.drawTexturedSquare(square.origin, square.size, square.texture)
        })

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

    private drawTexturedSquare(origin: Point3D, size: number, textureSource: HTMLImageElement) {
        const gl = this.gl

        const ox = origin.x
        const oy = origin.y
        const oz = origin.z
        // generate a square anchored in the `origin` point
        const vertices = [
            // X, Y, Z, U, V
            ox, oy, oz, 0, 1,
            ox, oy + size, oz, 0, 0,
            ox + size, oy + size, oz, 1, 0,
            ox + size, oy, oz, 1, 1
        ]

        const vertexBuffer = gl.createBuffer()
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer)
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW)

        const positionAttribLocation =
            gl.getAttribLocation(this.programTex, vertexTextureShaderRaw.attributes.vertPosition)
        const textureCoordinateAttribLocation
            = gl.getAttribLocation(this.programTex, vertexTextureShaderRaw.attributes.vertTextureCoordinate)

        gl.vertexAttribPointer(
            positionAttribLocation, // the vertex position attrib
            3, // 3D
            gl.FLOAT,
            false,
            5 * Float32Array.BYTES_PER_ELEMENT,
            0
        )
        gl.vertexAttribPointer(
            textureCoordinateAttribLocation,
            2,
            gl.FLOAT,
            false,
            5 * Float32Array.BYTES_PER_ELEMENT,
            3 * Float32Array.BYTES_PER_ELEMENT // to get the UV coordinates we skip the XYZ coordinates
        )
        gl.enableVertexAttribArray(positionAttribLocation)
        gl.enableVertexAttribArray(textureCoordinateAttribLocation)

        const texture = gl.createTexture()
        gl.bindTexture(gl.TEXTURE_2D, texture)
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texImage2D(
            gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA,
            gl.UNSIGNED_BYTE,
            textureSource
        )

        gl.useProgram(this.programTex)

        gl.activeTexture(gl.TEXTURE0)

        gl.drawArrays(gl.TRIANGLE_FAN, 0, vertices.length/5)
    }

}
