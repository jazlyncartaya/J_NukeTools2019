# J_SetRemoveAllCornerPin2DKeys Button v.1.0.0
# Copyright (c) 2019 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

    # Creates button that sets keys in all 'to' knobs in "CornerPin2D":
	
def set_all_to_cornerpin_keys():
    """This function sets all of the keys in all of the 'to' knobs
    in the CornerPin2D node."""

    this_node = nuke.thisNode()

    # "CornerPin2D" Knob: to1

    to_one_knob = this_node['to1']
    to_one_knob.splitView('right')

    input_amount_to_one = this_node.knob('to1').value()
    print input_amount_to_one

    to_one_knob.setAnimated(view='right')
    to_one_knob.setValue(input_amount_to_one)

    # "CornerPin2D" Knob: to2

    to_two_knob = this_node['to2']
    to_two_knob.splitView('right')

    input_amount_to_two = this_node.knob('to2').value()
    print input_amount_to_two

    to_two_knob.setAnimated(view='right')
    to_two_knob.setValue(input_amount_to_two)

    # "CornerPin2D" Knob: to3

    to_three_knob = this_node['to3']
    to_three_knob.splitView('right')

    input_amount_to_three = this_node.knob('to3').value()
    print input_amount_to_three

    to_three_knob.setAnimated(view='right')
    to_three_knob.setValue(input_amount_to_three)

    # "CornerPin2D" Knob: to4

    to_four_knob = this_node['to4']
    to_four_knob.splitView('right')

    input_amount_to_four = this_node.knob('to4').value()
    print input_amount_to_four

    to_four_knob.setAnimated(view='right')
    to_four_knob.setValue(input_amount_to_four)

    # Creates button that sets keys in all 'from' knobs in "CornerPin2D":
	
def set_all_from_cornerpin_keys():
    """This function sets all of the keys in all of the 'from' knobs
    in the CornerPin2D node."""

    this_node = nuke.thisNode()

    # "CornerPin2D" Knob: from1

    to_one_knob = this_node['from1']
    to_one_knob.splitView('right')

    input_amount_to_one = this_node.knob('from1').value()
    print input_amount_to_one

    to_one_knob.setAnimated(view='right')
    to_one_knob.setValue(input_amount_to_one)

    # "CornerPin2D" Knob: from2

    to_two_knob = this_node['from2']
    to_two_knob.splitView('right')

    input_amount_to_two = this_node.knob('from2').value()
    print input_amount_to_two

    to_two_knob.setAnimated(view='right')
    to_two_knob.setValue(input_amount_to_two)

    # "CornerPin2D" Knob: from3

    to_three_knob = this_node['from3']
    to_three_knob.splitView('right')

    input_amount_to_three = this_node.knob('from3').value()
    print input_amount_to_three

    to_three_knob.setAnimated(view='right')
    to_three_knob.setValue(input_amount_to_three)

    # "CornerPin2D" Knob: from4

    to_four_knob = this_node['from4']
    to_four_knob.splitView('right')

    input_amount_to_four = this_node.knob('from4').value()
    print input_amount_to_four

    to_four_knob.setAnimated(view='right')
    to_four_knob.setValue(input_amount_to_four)

    # Creates button that removes keys in all 'to' knobs in "CornerPin2D":

def remove_all_to_cornerpin_keys():
    """This function removes all of the keys in all 'to' knobs
    in the CornerPin2D node. """

    this_node = nuke.thisNode()

    # "CornerPin2D" Knob: to1

    frame = nuke.frame()
    to_one_knob = this_node['to1']
    to_one_knob.removeKeyAt(frame)

    # "CornerPin2D" Knob: to2

    frame = nuke.frame()
    to_two_knob = this_node['to2']
    to_two_knob.removeKeyAt(frame)

    # "CornerPin2D" Knob: to3

    frame = nuke.frame()
    to_three_knob = this_node['to3']
    to_three_knob.removeKeyAt(frame)

    # "CornerPin2D" Knob: to4

    frame = nuke.frame()
    to_four_knob = this_node['to4']
    to_four_knob.removeKeyAt(frame)

    # Creates button that removes keys in all 'from' knobs in "CornerPin2D":

def remove_all_from_cornerpin_keys():
    """This function removes all of the keys in all 'from' knobs
    in the CornerPin2D node. """

    this_node = nuke.thisNode()

    # "CornerPin2D" Knob: from1

    frame = nuke.frame()
    to_one_knob = this_node['from1']
    to_one_knob.removeKeyAt(frame)

    # "CornerPin2D" Knob: from2

    frame = nuke.frame()
    to_two_knob = this_node['from2']
    to_two_knob.removeKeyAt(frame)

    # "CornerPin2D" Knob: from3

    frame = nuke.frame()
    to_three_knob = this_node['from3']
    to_three_knob.removeKeyAt(frame)

    # "CornerPin2D" Knob: from4

    frame = nuke.frame()
    to_four_knob = this_node['from4']
    to_four_knob.removeKeyAt(frame)

def cornerpin_tab():
    """This function creates a button in CornerPin2D node
    which executes the set_all_to_cornerpin_keys() function."""
	
    node = nuke.thisNode()

    tab = nuke.Tab_Knob('Set/Remove Keys')
    node.addKnob(tab)

    pyknob = nuke.PyScript_Knob('set_all_to_cornerpin_keys',
                                'set all \'to\' keys',
                                'set_all_to_cornerpin_keys()')
    node.addKnob(pyknob)

    pyknob = nuke.PyScript_Knob('remove_all_to_cornerpin_keys',
                                'remove all \'to\' keys',
                                'remove_all_to_cornerpin_keys()')
    node.addKnob(pyknob)

    divider = nuke.Text_Knob('divider', '')
    node.addKnob(divider)

    pyknob = nuke.PyScript_Knob('set_all_from_cornerpin_keys',
                                'set all \'from\' keys',
                                'set_all_from_cornerpin_keys()')
    node.addKnob(pyknob)

    pyknob = nuke.PyScript_Knob('remove_all_from_cornerpin_keys',
                                'remove all \'from\' keys',
                                'remove_all_from_cornerpin_keys()')
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: cornerpin_tab(), nodeClass='CornerPin2D')