#version 420

// ps input
in vec2 tex_coord;
in vec4 colorInstance;

// uniform variables
uniform sampler2D tex;

// ps output
out vec4 color;

void main(void) 
{
    //color = texture(tex, tex_coord);
    //color = color * 0.5 + colorInstance * 0.5;
    color = colorInstance;
}
