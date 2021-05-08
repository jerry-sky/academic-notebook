import { vertexShaderRaw, fragmentShaderRaw } from './shaders'

export type Colour = number[];

export class MyCanvas {

    /**
     * WebGL context.
     */
    private gl: WebGLRenderingContext

    private program: WebGLProgram

    public readonly DrawTypes: {
        POINTS: number,
        LINES: number,
        LINE_STRIP: number,
        LINE_LOOP: number,
        TRIANGLES: number,
        TRIANGLE_STRIP: number,
        TRIANGLE_FAN: number,
    }

    constructor(private canvas: HTMLCanvasElement, private vertexGenericLocationIndex = 3) {
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

        gl.bindAttribLocation(program, this.vertexGenericLocationIndex, vertexShaderRaw.attributes.vertPosition)

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

    public printAllActiveAttributes() {
        const gl = this.gl
        const numAttribs = gl.getProgramParameter(this.program, gl.ACTIVE_ATTRIBUTES);
        for (let i = 0; i < numAttribs; ++i) {
            const info = gl.getActiveAttrib(this.program, i);
            console.log('name:', info.name, 'type:', info.type, 'size:', info.size);
        }
    }

    public printAllActiveUniforms() {
        const gl = this.gl
        const numUniforms = gl.getProgramParameter(this.program, gl.ACTIVE_UNIFORMS);
        for (let i = 0; i < numUniforms; ++i) {
            const info = gl.getActiveUniform(this.program, i);
            console.log('name:', info.name, 'type:', info.type, 'size:', info.size);
        }
    }

    public printAttribLocation() {
        console.log(
            this.gl.getAttribLocation(
                this.program,
                vertexShaderRaw.attributes.vertPosition
            )
        )
    }

    public draw2DUniformColor(vertices: number[], drawType: number, colour: Colour) {
        const gl = this.gl

        this.clearScreen()

        const verticesCount = vertices.length / 2;

        // the array must be dividable by five
        // every vertex is expected to have two coordinate parameters
        // and three colour parameters
        if (verticesCount !== Math.floor(vertices.length / 2)) {
            throw new Error('Invalid number of vertices’ parameters')
        }

        const vertexBuffer = gl.createBuffer()
        gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer)
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW)

        const positionAttribLocation = gl.getAttribLocation(this.program, vertexShaderRaw.attributes.vertPosition)

        gl.vertexAttribPointer(
            positionAttribLocation, // the vertex position attrib
            2, // 2D
            gl.FLOAT,
            false,
            2 * Float32Array.BYTES_PER_ELEMENT,
            0 // offset equal to zero, because we’re not expecting any additional information in the given array
        )
        gl.enableVertexAttribArray(positionAttribLocation)

        gl.useProgram(this.program)
        const colourUniformLocation = gl.getUniformLocation(this.program, fragmentShaderRaw.uniforms.colour)
        gl.uniform3fv(colourUniformLocation, new Float32Array(colour))

        gl.drawArrays(drawType, 0, verticesCount)
    }

}
