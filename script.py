import bpy


def lm2w(lumens, color): 
    r, g, b = color[0], color[1], color[2]

    efficacy = .2126*r + .7152*g + .0722*b
    
    if efficacy == 0:
        return 0

    return lumens / (683 * efficacy)


for x in bpy.context.selected_objects:
    x.data.energy = lm2w(x.data["Lumens"], x.data.color)
