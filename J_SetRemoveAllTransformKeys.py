# J_SetRemoveAllTransformKeys v.1.0.1
# Jazlyn Cartaya, 2019
# Add to menu.py
# import nuke


class TransformKeys():
    def __init__(self):
        """This function initializes the class."""

        self.this_node = nuke.thisNode()

    def set_all_keys(self):
        """This function sets all of the keys in all of the knobs
        in the Transform node."""

        # Define variables:
        this_node = self.this_node
        frame_number = nuke.frame()

        # "Transform" knob: Translate
        translate_knob = this_node.knob('translate')
        translate_knob.splitView('right')

        input_amount_translate = translate_knob.value()

        translate_knob.setAnimated(view='right')
        translate_knob.setValue(input_amount_translate)

        # "Transform" knob: Rotate
        rotate_knob = this_node.knob('rotate')

        input_amount_rotate = rotate_knob.value()

        rotate_knob.setAnimated(0)
        rotate_knob_an = rotate_knob.animations()[0]
        rotate_knob_an.setKey(int(frame_number), float(input_amount_rotate))

        # "Transform" knob: Scale
        scale_knob = this_node.knob('scale')
        scale_knob.splitView('right')

        input_amount_scale = scale_knob.value()

        scale_knob.setAnimated(view='right')
        scale_knob.setValue(input_amount_scale)

        # "Transform" knob: Skew X
        skew_x_knob = this_node.knob('skewX')

        input_amount_skew_x = skew_x_knob.value()

        skew_x_knob.setAnimated(0)
        skew_x_knob_an = skew_x_knob.animations()[0]
        skew_x_knob_an.setKey(int(frame_number), float(input_amount_skew_x))

        # "Transform" knob: Skew Y
        skew_y_knob = this_node.knob('skewY')

        input_amount_skew_y = skew_y_knob.value()

        skew_y_knob.setAnimated(0)
        skew_y_knob_an = skew_y_knob.animations()[0]
        skew_y_knob_an.setKey(int(frame_number), float(input_amount_skew_y))

        # "Transform" knob: Center
        center_knob = this_node.knob('center')
        center_knob.splitView('right')

        input_amount_center = center_knob.value()

        center_knob.setAnimated(view='right')
        center_knob.setValue(input_amount_center)

    def remove_all_keys(self):
        """This function removes all of the keys in all knobs
        in the Transform node."""

        # Define variables:
        this_node = self.this_node
        frame_number = nuke.frame()

        # "Transform" knob: Translate
        translate_knob = this_node.knob('translate')
        translate_knob.removeKeyAt(frame_number)

        # "Transform" knob: Rotate
        rotate_knob = this_node.knob('rotate')
        rotate_knob.removeKeyAt(frame_number)

        # "Transform" knob: Scale
        scale_knob = this_node.knob('scale')
        scale_knob.removeKeyAt(frame_number)

        # "Transform" knob: Skew X
        skew_x_knob = this_node.knob('skewX')
        skew_x_knob.removeKeyAt(frame_number)

        # "Transform" knob: Skew Y
        skew_y_knob = this_node.knob('skewY')
        skew_y_knob.removeKeyAt(frame_number)

        # "Transform" knob: Center
        center_knob = this_node.knob('center')
        center_knob.removeKeyAt(frame_number)


def add_transform_tab():
    """This function creates a tab and button in the
    Transform node that sets and removes keys."""

    # Define variables:
    this_node = nuke.thisNode()

    # Create Knobs
    tab = nuke.Tab_Knob('Set/Remove Keys')
    this_node.addKnob(tab)

    set_button = nuke.PyScript_Knob('set_all_transform_keys',
                                    'set all keys',
                                    'TransformKeys().set_all_keys()'
                                    )
    this_node.addKnob(set_button)

    remove_button = nuke.PyScript_Knob('remove_all_transform_keys',
                                       'remove all keys',
                                       'TransformKeys().remove_all_keys()'
                                       )
    this_node.addKnob(remove_button)

nuke.addOnCreate(add_transform_tab, nodeClass='Transform')
