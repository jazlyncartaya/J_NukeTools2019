# J_TrackToRotoPaint v.1.0.0
# Copyright (c) 2019 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

def track_to_rotopaint():

    # Create RotoPaint node-to-be-parented:
    this_node = nuke.thisNode()
    created_node = nuke.createNode('RotoPaint')

    # Parent Translate:
    created_node.knob('translate').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.translate')

    # Parent Rotate:
    created_node.knob('rotate').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.rotate')

    # Parent Scale:
    created_node.knob('scale').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.scale')

    # Parent Skew X:
    created_node.knob('skewX').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.skewX')

    # Parent Skew Y:
    created_node.knob('skewY').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.skewY')

    # Parent Center:
    created_node.knob('center').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.center')

    # Label Node:
    created_node.knob('label').setValue(
        str(this_node.knob('name').value())
        + '\nref ' 
        + str(int(this_node.knob('reference_frame').value()))
        )

def track_to_rotopaint_tab():

    node = nuke.thisNode()

    tab = nuke.Tab_Knob('Track to RotoPaint')
    node.addKnob(tab)

    pyknob = nuke.PyScript_Knob('track_to_rotopaint',
                                'create parented rotopaint',
                                'track_to_rotopaint()')
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: track_to_rotopaint_tab(), nodeClass='Tracker4')