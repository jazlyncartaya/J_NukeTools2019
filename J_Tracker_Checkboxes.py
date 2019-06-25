# J_Tracker_Checkboxes v.1.0.0
# Jazlyn Cartaya, 2019
# Add to menu.py
# import nuke


def tracker_checkboxes_tab():
    """This function creates a tab in the Tracker node that lets
    the artist quickly select the amount of T, R, S Tracker
    checkboxes they want to check."""

    # Define Variables:
    node = nuke.thisNode()

    # Create knobs:
    tab = nuke.Tab_Knob('Check Boxes')
    number_of_trackers = nuke.String_Knob('number_of_trackers',
                                          'number of trackers:',
                                          'All'
                                          )
    number_of_trackers.setFlag(nuke.STARTLINE)
    t_boolean_knob = nuke.Boolean_Knob('translate_box', 'translate', True)
    r_boolean_knob = nuke.Boolean_Knob('rotate_box', 'rotate', True)
    s_boolean_knob = nuke.Boolean_Knob('scale_box', 'scale', True)
    pyknob = nuke.PyScript_Knob('check_tracker_boxes',
                                'execute',
                                'tracker_checkboxes()'
                                )
    pyknob.setFlag(nuke.STARTLINE)

    # Add knobs:
    node.addKnob(tab)
    node.addKnob(number_of_trackers)
    node.addKnob(t_boolean_knob)
    node.addKnob(r_boolean_knob)
    node.addKnob(s_boolean_knob)
    node.addKnob(pyknob)

nuke.addOnCreate(lambda: tracker_checkboxes_tab(), nodeClass='Tracker4')

# Check boxes in 'Tracker' node:


def tracker_checkboxes():
    """This function checks all or x amount of T, R, and S
    checkboxes in the Tracker node."""

    # Define variables:

    selected_node = nuke.selectedNode()
    knob = selected_node['tracks']
    num_columns = 31
    col_translate = 6
    col_rotate = 7
    col_scale = 8
    count = 0
    trackers_knobvalue = selected_node.knob('number_of_trackers').value()
    translate_knobvalue = selected_node.knob('translate_box').value()
    rotate_knobvalue = selected_node.knob('rotate_box').value()
    scale_knobvalue = selected_node.knob('scale_box').value()

    # Put toScript in list:

    trackers = []
    script = selected_node['tracks'].toScript()
    trackers.append(script)

    # Get number of tracks from list:

    for item in trackers:
        total_tracks = item.count('\"track ')

    # Check ALL boxes:

    # Math = (True (1) or False (0), 31 columns * track number (0 to infinity)
    # + Translate (6), Rotate (7), or Scale (8))

    if trackers_knobvalue == 'All':
        while count <= int(total_tracks)-1:

            if all([translate_knobvalue, rotate_knobvalue, scale_knobvalue]):
                knob.setValue(1, num_columns * count + col_translate)
                knob.setValue(1, num_columns * count + col_rotate)
                knob.setValue(1, num_columns * count + col_scale)
            elif not any([translate_knobvalue,
                          rotate_knobvalue,
                          scale_knobvalue]):
                knob.setValue(0, num_columns * count + col_translate)
                knob.setValue(0, num_columns * count + col_rotate)
                knob.setValue(0, num_columns * count + col_scale)

            if translate_knobvalue is True:
                knob.setValue(1, num_columns * count + col_translate)
            elif translate_knobvalue is False:
                knob.setValue(0, num_columns * count + col_translate)

            if rotate_knobvalue is True:
                knob.setValue(1, num_columns * count + col_rotate)
            elif rotate_knobvalue is False:
                knob.setValue(0, num_columns * count + col_rotate)

            if scale_knobvalue is True:
                knob.setValue(1, num_columns * count + col_scale)
            if scale_knobvalue is False:
                knob.setValue(0, num_columns * count + col_scale)
            count += 1

    # Check x number of boxes:

    if trackers_knobvalue != 'All':
        while count <= int(trackers_knobvalue)-1:

            if translate_knobvalue is True:
                knob.setValue(1, num_columns * count + col_translate)
            elif translate_knobvalue is False:
                knob.setValue(0, num_columns * count + col_translate)

            if rotate_knobvalue is True:
                knob.setValue(1, num_columns * count + col_rotate)
            elif rotate_knobvalue is False:
                knob.setValue(0, num_columns * count + col_rotate)

            if scale_knobvalue is True:
                knob.setValue(1, num_columns * count + col_scale)
            elif scale_knobvalue is False:
                knob.setValue(0, num_columns * count + col_scale)
            count += 1
