# J_ShuffleNodeTool v.1.0.0
# Copyright (c) 2019 Jazlyn Cartaya. All Rights Reserved.
# Add to menu.py
#import nuke

    # SHUFFLE NODE TOOL

def shuffle_node_tool():

    # Define variables:

    selected = nuke.selectedNode()
    selected.setSelected(False)

    exr_x_position = nuke.Node.xpos(selected)
    exr_y_position = nuke.Node.ypos(selected)

    shuffle_layers = nuke.layers(selected)

    # Create a list for newly created Shuffle and Dot nodes:

    shuffle_nodes = []
    dot_nodes = []
    backdrop_nodes = []

    # Create a Dot and corresponding Shuffle node:

    for shuffle_layer in shuffle_layers:
        dot_node = nuke.createNode('Dot')
        shuffle_node = nuke.createNode('Shuffle')
        dot_nodes.append(dot_node)
        shuffle_nodes.append(shuffle_node)
        shuffle_node.knob('in').setValue(str(shuffle_layer))

    for shuffle_node in shuffle_nodes:
        shuffle_node.setSelected(False)

    # Set x and y pos of each Dot node:

    for dot_node in dot_nodes:
        dot_node.setSelected(True)

    dot_positionX = 164
    for dot_node in dot_nodes:
        dot_node.setInput(0, None)
        dot_x_position = nuke.Node.xpos(dot_node)
        dot_y_position = nuke.Node.ypos(dot_node)
        dot_node.setYpos(exr_y_position + 210)
        dot_node.setXpos(exr_x_position + dot_positionX - 130)
        dot_positionX += 164

    for dot_node in dot_nodes:
        dot_node.setSelected(False)

    # Set x and y pos of each Shuffle node:

    for shuffle_node in shuffle_nodes:
        shuffle_node.setSelected(True)

    shuffle_positionX = 164
    for shuffle_node in shuffle_nodes:
        shuffle_x_position = nuke.Node.xpos(shuffle_node)
        shuffle_y_position = nuke.Node.ypos(dot_node)
        shuffle_node.setYpos(exr_y_position + 500)
        shuffle_positionX += 164

    # Set Input:

    dot_nodes[0].setInput(0, selected)

    for i, dot_node in enumerate(dot_nodes[1:]):
        next_dot = dot_nodes[i]
        dot_node.setInput(0, next_dot)

    # Create BackDrop Node for each Shuffle node:

    for shuffle_node in shuffle_nodes:
        shuffle_node.setSelected(True)
        backdrop_node = nuke.createNode('BackdropNode')
        backdrop_node.knob('bdwidth').setValue(164)
        backdrop_node.knob('bdheight').setValue(358)
        backdrop_nodes.append(backdrop_node)

    # Label BackDrop Nodes:

    for i, backdrop_node in enumerate(backdrop_nodes):
        shuffle_layer = shuffle_layers[i]
        backdrop_node.knob('label').setValue(shuffle_layer)
        backdrop_node.knob('note_font_size').setValue(30)

    # Set Odd BackDrop Nodes' Light Purple Color:

    light_purple = int('%02x%02x%02x%02x' % (0.452*255, 0.409*255, 0.625*255, 255), 16)
    for backdrop_node in backdrop_nodes[::2]:
        backdrop_node.knob('tile_color').setValue(light_purple)

    # Set Even BackDrop Nodes' Dark Purple Color:

    dark_purple = int('%02x%02x%02x%02x' % (0.318*255, 0.204*255, 0.592*255, 255), 16)
    for backdrop_node in backdrop_nodes[1::2]:
        backdrop_node.knob('tile_color').setValue(dark_purple)

    # Set Position of BackDrop Nodes:

    backdrop_positionX = 164
    for backdrop_node in backdrop_nodes:
        backdrop_x_position = nuke.Node.xpos(backdrop_node)
        backdrop_y_position = nuke.Node.ypos(backdrop_node)
        backdrop_node.setXpos(shuffle_x_position + backdrop_positionX -540)
        backdrop_node.setYpos(shuffle_y_position + 34)
        backdrop_positionX += 164