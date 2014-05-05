from PySide import QtGui


class SettingsView(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        label = QtGui.QLabel('settings')
        layout.addWidget(label)
        self.setLayout(layout)
