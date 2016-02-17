#version 420

//vertex attribs
in vec4 model_postion;
in vec2 tex_coord_in;
in vec4 color_in;

//uniform variables
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;

//vs output
out vec2 tex_coord;
out vec4 colorInstance;
out int  instanceID;
out int  vertexID;

void main(void) 
{
    vec4 eye_coord, clip_coord;
    eye_coord = modelViewMatrix * model_postion;
    clip_coord = projectionMatrix * eye_coord;

    if (gl_InstanceID == 1)
    {
        clip_coord.x += 30.0;
        clip_coord.y -= 20;
    }

    if (gl_VertexID > 0)
    {
        tex_coord = tex_coord_in;
    }

    colorInstance = color_in;
    //tex_coord = tex_coord_in;
    instanceID = gl_InstanceID;
    vertexID = gl_VertexID;
    gl_Position = clip_coord;
}
