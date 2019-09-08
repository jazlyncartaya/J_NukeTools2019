# J_AttachNodes Tool v.2.0.1
# Jazlyn Cartaya, 2019
# Add to menu.py

#nuke.menu('Nuke').addCommand('J_Tools/Attach Nodes',
                            # 'show_attach_nodes()',
                            # 'ctrl+alt+a')

import nuke
import sys
import PySide2
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class AttachNodes(QWidget):
    """Panel 1: Attaches created nodes to selected
    nodes in the artist's node graph."""

    def __init__(self):
        """This function creates a panel that asks the artist to
        type in the node they want to create and attach to
        selected nodes in the node graph."""

        # Inherits QWidget parent class:
        super(AttachNodes, self).__init__()

        # Panel 1 widget:
        self.panel_name = self.setWindowTitle('Attach Nodes')
        self.resize = self.resize(250, 150)
        self.label = QLabel("""Select node(s) in your node graph
to attach created nodes to:""")

        # Create widgets:

        # Line widget:
        self.attached_node = QLineEdit()
        self.attached_node.setToolTip('Type in the name of node you would '
                                      'like to create and attach. i.e. Grade')
        self.attached_node.setPlaceholderText('node name')
        self.completer = QCompleter(['Grade', 'Blur', 'Transform',
                                     'TransformMasked', 'Defocus',
                                     'Roto', 'RotoPaint', 'Premult'])
        self.attached_node.setCompleter(self.completer)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Checkbox widget:
        self.clone_node = QCheckBox('clone node')
        self.clone_node.setToolTip('Do you want to create clones of the node?')
        self.clone_node.setChecked(False)

        # Button widget:
        self.execute = QPushButton('execute')
        self.execute.setToolTip('Execute the data.')
        self.execute.clicked.connect(self.execute_button)
        self.cancel = QPushButton('cancel')
        self.cancel.clicked.connect(self.close)

        # Add widgets:
        self.master_layout = QGridLayout()
        self.master_layout.addWidget(self.label, 0, 0)
        self.master_layout.addWidget(self.attached_node, 1, 0)
        self.master_layout.addWidget(self.clone_node, 2, 0)
        self.master_layout.addWidget(self.execute, 3, 0)
        self.master_layout.addWidget(self.cancel, 3, 1)
        self.setLayout(self.master_layout)

        # Define variables:
        self.selected = nuke.selectedNodes()
        self.panel_two = None

        # List:
        self.created_nodes = []

    def execute_button(self):
        """The function that runs if the artist
        clicks the execute button."""

        self.attach_nodes()
        self.close()

    def attach_nodes(self):
        """This function takes the data from the panel and attaches
        created nodes to selected nodes, with the option to clone."""

        # Define variables:
        attached_node = self.attached_node.text()
        clone_node = self.clone_node.isChecked()

        # Attach node(s):
        for node in self.selected:
            node.setSelected(False)

        try:
            if clone_node is False:
                for node in self.selected:
                    node.setSelected(True)
                    created_node = nuke.createNode(attached_node.title())
                    self.created_nodes.append(created_node)  # add to list
                    node.setSelected(False)
                    created_node.setSelected(False)

            # Clone node:
            if clone_node is True:
                if self.selected[0]:
                    self.selected[0].setSelected(True)
                    created_node = nuke.createNode(attached_node.title())
                    self.created_nodes.append(created_node)  # add to list
                    created_node.setSelected(False)

                del self.selected[0]

                for node in self.selected:
                    node.setSelected(True)
                    nuke.clone(created_node)
                    node.setSelected(False)
                    created_node.setSelected(False)

            self.created_nodes[0].setSelected(True)

        except RuntimeError:
            nuke.message('The name you entered was not a node name.'
                         ' Please enter a node name.')

        # Show Panel 2 if Panel 1 is successful:
        if self.created_nodes:
            self.panel_two = ANSetKnobs()
            self.panel_two.show()


class ANSetKnobs(QWidget):
    """Panel 2: Artist can change one of the
    knob values in all created nodes."""

    def __init__(self):
        """This function creates a panel that asks for
        the artist to select the knob value they want to
        change in the created nodes."""

        # Inherits QWidget parent class:
        super(ANSetKnobs, self).__init__()

        # Panel 2 widget:
        self.panel_name = self.setWindowTitle('Attach Nodes')
        self.resize = self.resize(250, 150)
        self.label = QLabel("""Select a knob value to
change in all created nodes:""")

        # Create widgets:
        self.knobs = nuke.selectedNode().knobs().keys()  # List of knobs.

        # Combo widget:
        self.knob_name = QComboBox()
        self.knob_name.setToolTip('Select the knob you would like to change.')
        self.knob_name.addItems(self.knobs)

        # Line widget:
        self.optional_value = QLineEdit()
        self.optional_value.setToolTip('Type in the value you would like to '
                                        'set the knob to in all created nodes.')
        self.optional_value.setPlaceholderText('number value')

        # Button widget:
        self.execute = QPushButton('execute')
        self.execute.setToolTip('Execute the data.')
        self.execute.clicked.connect(self.execute_button)
        self.cancel = QPushButton('cancel')
        self.cancel.clicked.connect(self.close)

        # Add widgets:
        self.master_layout = QGridLayout()
        self.master_layout.addWidget(self.label, 0, 0)
        self.master_layout.addWidget(self.knob_name, 1, 0)
        self.master_layout.addWidget(self.optional_value, 2, 0)
        self.master_layout.addWidget(self.execute, 3, 0)
        self.master_layout.addWidget(self.cancel, 3, 1)
        self.setLayout(self.master_layout)

    def execute_button(self):
        """The function that runs if the artist
        clicks the execute button."""

        self.set_knobs()
        self.close()

    def set_knobs(self):
        """This function takes the data from the panel and
        sets the knob value in all created nodes."""

        # Define variables:
        knob_name = self.knob_name.currentText()
        optional_value = self.optional_value.text()

        # Change the knob of x attached node(s) to y input value:
        try:
            for node in show_an_panel.created_nodes_list:
                node.knob(str(knob_name)).setValue(int(optional_value))

        except ValueError:
            nuke.message('The value you entered was not a number.'
                         ' Please enter a number value.')

        except TypeError:
            nuke.message('The knob you selected does not take a number value.'
                         ' Please select a knob that takes a number value.')


def show_an_panel():  # show panels
    """This function shows the panels."""

    show_an_panel.panel_one = AttachNodes()
    show_an_panel.panel_one.show()

    show_an_panel.created_nodes_list = show_an_panel.panel_one.created_nodes
    
