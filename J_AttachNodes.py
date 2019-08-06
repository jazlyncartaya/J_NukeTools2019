# J_AttachNodes Tool v.1.1.1
# Jazlyn Cartaya, 2019
# Add to menu.py
# import nuke
# J_AttachNodes Menu
# nuke.menu('Nuke').addCommand('J_AttachNodes/Attach Nodes',
                             # 'attach_nodes()',
                             # 'ctrl+alt+a')


class AttachNodes(nukescripts.PythonPanel):
    def __init__(self):
        """This function creates a panel that lets the artist attach any node, 
        of the same node, to all selected nodes. And adjust one of the
        knobs in the created nodes."""

        # Panel 1: Asks for the name of the node that the artist
        # would like to attach to selected nodes. Gives option to clone.
        nukescripts.PythonPanel.__init__(self, 'Attach Nodes')

        # Create knobs:
        self.attached_node = nuke.String_Knob('attached_node',
                                              'node to attach:',
                                              ''
                                              )
        self.clone_node = nuke.Boolean_Knob('clone_node', 'clone node', False)
        self.clone_node.setFlag(nuke.STARTLINE)

        # Add knobs:
        for knob in (self.attached_node, self.clone_node):
            self.addKnob(knob)

    def attach_nodes(self):
        """This function takes the information from the panel and attaches
        created nodes to selected nodes in the node graph."""

        # List of created node(s):
        desired_nodes = []

        # Define variables:
        selected = nuke.selectedNodes()
        attached_node = self.attached_node.value()
        clone_node = self.clone_node.value()

        # Attach node(s):
        for node in selected:
            node.setSelected(False)

        try:
            if clone_node is False:
                for node in selected:
                    node.setSelected(True)
                    desired_node = nuke.createNode(attached_node.title())
                    desired_nodes.append(desired_node)  # add to list
                    node.setSelected(False)
                    desired_node.setSelected(False)

            # Clone node:
            if clone_node is True:
                if selected[0]:
                    selected[0].setSelected(True)
                    desired_node = nuke.createNode(attached_node.title())
                    desired_nodes.append(desired_node)  # add to list
                    desired_node.setSelected(False)

                del selected[0]

                for node in selected:
                    node.setSelected(True)
                    nuke.clone(desired_node)
                    node.setSelected(False)
                    desired_node.setSelected(False)

            desired_nodes[0].setSelected(True)

        except RuntimeError:
            nuke.message('The name you entered was not a node name.'
                         ' Please enter a node name.')

        return desired_nodes  # List of created nodes.


class ANSetKnobs(nukescripts.PythonPanel):
    def __init__(self):
        """This function creates a panel that lets the artist select
        a knob and change the value of the knob in all created nodes."""

        # Panel 2: Asks for the knob name and
        # the number value the artist would like to set.
        nukescripts.PythonPanel.__init__(self, 'Knob Input')

        # Create knobs:
        knobs = nuke.selectedNode().knobs().keys()  # Generate list of knobs.

        try:
            self.knob_name = nuke.Enumeration_Knob('optional_knob',
                                                   'knob:',
                                                   knobs
                                                   )
            self.optional_value = nuke.String_Knob('optional_value',
                                                   'value:',
                                                   ''
                                                   )

        # Add knobs:
            for knob in (self.knob_name, self.optional_value):
                self.addKnob(knob)
        except UnboundLocalError:
            pass

    def set_knobs(self, attach_nodes):
        """This function takes the information from the panel and
        sets the knob value in all created nodes."""

        # Define variables:
        knob_name = self.knob_name.value()
        optional_value = self.optional_value.value()

        # Change the knob(s) of x attached node(s) to y input value:
        try:
            for node in attach_nodes:
                node.knob(str(knob_name)).setValue(int(optional_value))

        except ValueError:
            nuke.message('The value you entered was not a number.'
                         ' Please enter a number value.')

        except TypeError:
            nuke.message('The knob you selected does not take a number value.'
                         ' Please select a knob that takes a number value.')


def show_attach_nodes():
    """This function creates instances of each class and
    shows the panels."""

    panel_one = AttachNodes()
    panel_one.showModalDialog()
    attach_nodes = panel_one.attach_nodes()

    if attach_nodes:
        panel_two = ANSetKnobs()
        panel_two.showModalDialog()
        panel_two.set_knobs(attach_nodes)
