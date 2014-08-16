from PySide import QtGui

class TopBar(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setObjectName('topbar')
        layout = QtGui.QHBoxLayout()
        self.setLayout(layout)

        shutdown = QtGui.QPushButton(';')
        maximise = QtGui.QPushButton('^')
        minimise = QtGui.QPushButton('_')
        settings = QtGui.QPushButton('?')

        layout.addWidget(shutdown)
        layout.addWidget(maximise)
        layout.addWidget(minimise)
        layout.addWidget(settings)

        #todo, bind buttons
        
