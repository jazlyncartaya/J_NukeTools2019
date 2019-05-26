# J_ChangeSelectedNodeKnobs v.1.0.0
# Copyright (c) 2018 Jazlyn Cartaya.  All Rights Reserved.
# Add to menu.py
#import nuke

def changeSelectedNodeKnobs():

    selected_nodes = nuke.selectedNodes()
    selected_knob = None
    knobs = nuke.selectedNode().knobs().keys()
    knobs.sort(key=str.lower) # Sort knobs into alphabetical order.

    panel = nuke.Panel('Knob Input')
    panel.addEnumerationPulldown('Knob (optional):', ' '.join(knobs))
    panel.addSingleLineInput('Input (optional):', 0)
    ret = panel.show()

    selected_knob = panel.value('Knob (optional):')
    print selected_knob

    input_amount = panel.value('Input (optional):')
    print input_amount

    # Set x node(s), at y value.
    try:
        for node in selected_nodes:
            node.knob(selected_knob).setValue(int(input_amount))

    except TypeError:
        nuke.message(
            ' The knob you selected does not take a number value.'
            ' Please select a knob that takes a number value.'
            )

    except ValueError:
        nuke.message(
            ' You must type a number value'
            ' into the Input section.'
            )