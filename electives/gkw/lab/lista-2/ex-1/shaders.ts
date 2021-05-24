
export const vertexShaderRaw = {
    source: `
precision mediump float;

attribute vec2 vertPosition;
// attribute vec3 vertColor;
// uniform vec3 fragColor;

void main()
{
    // fragColor = vertColor;
    gl_Position = vec4(vertPosition, 0.0, 1.0);
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

uniform vec3 fragColor;

void main()
{
    gl_FragColor = vec4(fragColor, 1.0);
}
`,
    attributes: {},
    uniforms: {
        colour: 'fragColor',
    },
}
