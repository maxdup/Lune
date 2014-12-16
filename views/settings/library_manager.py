from PySide import QtGui, QtCore

class LibraryManager(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(QtGui.QLabel('Update your library:'))
        layout.addWidget(QtGui.QPushButton('Update'))
        layout.addWidget(QtGui.QLabel('Clean your library:'))
        layout.addWidget(QtGui.QPushButton('Clean'))
        layout.addStretch()
        self.setLayout(layout)
