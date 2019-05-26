# J_ParentedNodes v.1.0.0
# Copyright (c) 2019 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke
	
    # Grade Node:
	
def grade_parented_node():
    """This function creates a parented Grade node."""

    this_node = nuke.thisNode()

    # Create node-to-be-parented:
    this_node.setSelected(False)
    created_node = nuke.createNode('Grade')

    # Parent BlackPoint:
    created_node.knob('blackpoint').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.blackpoint')
	
    # Parent WhitePoint:
    created_node.knob('whitepoint').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.whitepoint')
	
    # Parent Black (Lift):
    created_node.knob('black').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.black')
	
    # Parent White (Gain):
    created_node.knob('white').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.white')
	
    # Parent Multiply:
    created_node.knob('multiply').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.multiply')
	
    # Parent Add (Offset):
    created_node.knob('add').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.add')
	
    # Parent Gamma:
    created_node.knob('gamma').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.gamma')
	
def grade_parented_node_button():
    """This function creates a button in the Grade node
    which executes the grade_parented_node function."""
	
    node = nuke.thisNode()

    tab = nuke.Tab_Knob('J_Buttons')
    node.addKnob(tab)

    pyknob = nuke.PyScript_Knob('parented_grade',
                                'create parented node',
                                'grade_parented_node()')
    node.addKnob(pyknob)
    pyknob.setTooltip('Click this button to create a Grade node that is parented to this Grade node.')

nuke.addOnCreate(lambda: grade_parented_node_button(), nodeClass='Grade')

    # Blur Node:
	
def blur_parented_node():
    """This function creates a parented Blur node."""

    this_node = nuke.thisNode()

    # Create node-to-be-parented:
    this_node.setSelected(False)
    created_node = nuke.createNode('Blur')

    # Parent Size:
    created_node.knob('size').setExpression('parent.' 
        + str(this_node.knob('name').value()) 
        + '.size')

def blur_parented_node_button():
    """This function creates a button in the Blur node
    which executes the blur_parented_node function."""

    node = nuke.thisNode()

    tab = nuke.Tab_Knob('J_Buttons')
    node.addKnob(tab)

    pyknob = nuke.PyScript_Knob('blur_parented_node',
                                'create parented node',
                                'blur_parented_node()')
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: blur_parented_node_button(), nodeClass='Blur')

    # Transform Node:
	
def transform_parented_node():
    """This function creates a parented Transform node."""

    this_node = nuke.thisNode()

    # Create node-to-be-parented:
    this_node.setSelected(False)
    created_node = nuke.createNode('Transform')

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
	
def transform_parented_node_button():
    """This function creates a button in the Transform node
    which executes the transform_parented_node function."""
	
    node = nuke.thisNode()

    tab = nuke.Tab_Knob('J_Buttons')
    node.addKnob(tab)

    pyknob = nuke.PyScript_Knob('transform_parented_node',
                                'create parented node',
                                'transform_parented_node()')
    node.addKnob(pyknob)

nuke.addOnCreate(
    lambda: transform_parented_node_button(), 
    nodeClass='Transform'
    )