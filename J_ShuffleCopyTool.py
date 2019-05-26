# J_ShuffleCopyTool v.1.0.0
# Copyright (c) 2019 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

    # SHUFFLE COPY TOOL
def shuffleCopyTool():

    # Global variables/lists:

    selected_nodes = nuke.selectedNodes()
    exr_nodes = []
    organized_nodes = []
    shuffle_copy_nodes = []
    names = []
    shuffle_copy_node_x_positions = []
    shuffle_copy_node_y_positions = []
    exr_x_positions = []
    exr_y_positions = []

    # Deselect nodes:

    for node in selected_nodes:
        node.setSelected(False)
        organized_nodes.append(node)

    # Put all selected exr nodes into a list:

    for node in selected_nodes:
        exr_nodes.append(node)

    # Put the names of all selected exr nodes into a list:

    for node in exr_nodes:
        file = node.knob('file').value()
        string = file.split('/')
        new_string = os.path.join(
           string[11]
           )

        names.append(new_string)

    # Create a ShuffleCopy for each selected exr node:

    for node in selected_nodes:
        shuffle_copy = nuke.createNode('ShuffleCopy')
        organized_nodes.append(shuffle_copy)
        shuffle_copy_nodes.append(shuffle_copy)
        shuffle_copy.setInput(1,node)
        node.setSelected(True)
        shuffle_copy.setSelected(False)
        node.setSelected(False)
        shuffle_copy.setSelected(False)

        # Check the alpha box in the 'out' rgba:
        shuffle_copy.knob('alpha').setValue('alpha2')

    # Create new layer, with red, green, blue, and alpha checked:
    for i,node in enumerate(shuffle_copy_nodes):
        name = names[i]
        nuke.Layer(name,['red','green','blue','alpha'])
        node.knob('out2').setValue(name)
        node.knob('black').setValue('red')
        node.knob('white').setValue('green')
        node.knob('red2').setValue('blue')
        node.knob('green2').setValue('alpha')

    # Organize nodes:

    for node in organized_nodes:
        node.setSelected(True)
        nuke.autoplace(node)

    # Aesthetic:

    for node in shuffle_copy_nodes:
    # Assign a variable to x and y positions:
        shuffle_copy_x_position = nuke.Node.xpos(node)
        shuffle_copy_y_position = nuke.Node.ypos(node)
        shuffle_copy_node_x_positions.append(shuffle_copy_x_position)
        shuffle_copy_node_y_positions.append(shuffle_copy_y_position)

    for node in exr_nodes:
    # Assign a variable to x and y positions:
        exr_x_position = nuke.Node.xpos(node)
        exr_y_position = nuke.Node.ypos(node)
        exr_x_positions.append(exr_x_position)
        exr_y_positions.append(exr_y_position)

    # Create lists for new node positions:

    new_shuffle_y_positions = []
    new_exr_y_positions = []

    # Alter y positions on ShuffleCopy and exr nodes:

    try:
        numbers = range(0,100)
        for i,digit in enumerate(shuffle_copy_node_y_positions):
            number = numbers[i]
            new_number = digit + 144*number
            new_shuffle_y_positions.append(new_number)
    except IndexError:
        pass

    try:
        numbers = range(0,100)
        for i,digit in enumerate(exr_y_positions):
            number = numbers[i]
            new_number = digit + 144*number
            new_exr_y_positions.append(new_number)
    except IndexError:
        pass

    # Offset ShuffleCopy x and y positions:
    try:
        for i,node in enumerate(shuffle_copy_nodes):
            shuffle_copy_node_x_position = shuffle_copy_node_x_positions[i:i+1]
            node.setXpos(shuffle_copy_node_x_positions[0])
    except IndexError:
        pass

    try:
        for i,node in enumerate(shuffle_copy_nodes):
            new_shuffle_y_position = new_shuffle_y_positions[i]
            print new_shuffle_y_position
            node.setYpos(int(new_shuffle_y_position))
    except IndexError:
        pass

    # Connect '2' pipe to each preceding ShuffleCopy node:
    try:
        for i,node in enumerate(shuffle_copy_nodes):
            shuffle_copy_node = shuffle_copy_nodes[i+1]
            shuffle_copy_node.setInput(0,node)
    except IndexError:
        pass

    # Offset exr x and y positions:
    try:
        for i,node in enumerate(shuffle_copy_nodes):
            exr_x_position = exr_x_positions[i:i+1]
            node.setXpos(exr_x_positions[0])
    except IndexError:
        pass

    try:
        for i,node in enumerate(exr_nodes):
            exr_x_position = exr_x_positions[i:i+1]
            node.setXpos(exr_x_positions[1])
    except IndexError:
        pass

    try:
        for i,node in enumerate(exr_nodes):
            new_exr_y_position = new_exr_y_positions[i]
            node.setYpos(new_exr_y_position)
    except IndexError:
        pass

    # Deselect all nodes:

    for node in selected_nodes:
        node.setSelected(False)

    for node in exr_nodes:
        node.setSelected(False)

    for node in shuffle_copy_nodes:
        node.setSelected(False)

    # Create Write node:

    write_node = nuke.createNode('Write')
    write_node.knob('channels').setValue('all')
    write_node.knob('file_type').setValue('exr')

    # Connect Write node to final ShuffleCopy node, and place in tree:

    write_node.setInput(0,shuffle_copy_nodes[-1])
    nuke.autoplace(write_node)