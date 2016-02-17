# Ciao-Marika
HelloWorld

InstancedDraw
Using transformfeedback to verify gl_VertexID/gl_InstanceID with instanced attribs and different draw command
Following theory based on test results on Nvidia GTX860M(OGL4.5)/Intel HD4600(OGL4.3)

KEY 1 : glDrawArrays( mode, first, count);
'first' affect gl_VertexID, so gl_VertexID range from first~first+count-1

KEY 2 : glDrawArraysInstancedBaseInstance( mode, first, count, instancecount, baseinstance);
'first' affect gl_VertexID, so gl_VertexID range from first~first+count-1
'baseInstance' doesn't affect gl_InstanceID, so gl_VertexID range from 0~instanceCounts-1,
but for each instanced attrib, the first baseinstance items will be skiped, then start fetching.

KEY 3 : glDrawElements( mode, count, type, indices);
'indices' affect gl_VertexID, so gl_VertexID range from indice[0]~indice[count-1]

KEY 4 : glDrawElementsInstancedBaseVertexBaseInstance( mode, count, type, indices, instancecount, basevertex, baseinstance);
'indices' and 'BaseVertex' affect gl_VertexID, so gl_VertexID range from indice[0]+BaseVertex~indice[count-1]+BaseVertex
'baseInstance' doesn't affect gl_InstanceID, so gl_VertexID range from 0~instanceCounts-1,
but for each instanced attrib, the first baseinstance items will be skiped, then start fetching.