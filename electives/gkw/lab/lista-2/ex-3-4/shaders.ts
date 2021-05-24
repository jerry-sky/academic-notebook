
export const vertexShaderRaw = {
    source: `
precision mediump float;

attribute vec3 vertPosition;

void main()
{
    gl_Position = vec4(vertPosition, 1.0);
    gl_PointSize = 10.0;
}
`,
    attributes: {
        vertPosition: 'vertPosition',
    },
}

export const fragmentShaderRaw = {
    source: `
precision mediump float;

uniform vec3 fragColour;

void main()
{
    gl_FragColor = vec4(fragColour, 1.0);
}
`,
    attributes: {},
    uniforms: {
        colour: 'fragColour',
    },
}

export const vertexTextureShaderRaw = {
    source: `
precision mediump float;

attribute vec3 vertPosition;
attribute vec2 vertTextureCoordinate;

varying vec2 fragmentTextureCoordinate;

void main()
{
    gl_Position = vec4(vertPosition, 1.0);
    fragmentTextureCoordinate = vertTextureCoordinate;
}
`,
    attributes: {
        vertPosition: 'vertPosition',
        vertTextureCoordinate: 'vertTextureCoordinate'
    },
}

export const fragmentTextureShaderRaw = {
    source: `
precision mediump float;

uniform sampler2D sampler;

varying vec2 fragmentTextureCoordinate;

void main()
{
    gl_FragColor = texture2D(sampler, fragmentTextureCoordinate);
}
`,
    attributes: {},
    uniforms: {
        colour: 'sampler',
    },
}
