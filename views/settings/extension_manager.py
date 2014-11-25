from PySide import QtGui, QtCore

class ExtensionManager(QtGui.QWidget):

    FORMATS = ['mp3', 'flac', 'aac', 'opus', 'ogg', 'oga', 'ape', 'mpc', 'wav', 'pcm', 'aiff', 'm4a']

    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.user_settings = user_settings

        layout.addWidget(QtGui.QLabel('include these formats in my library:'))

        for ext in self.FORMATS:
            layout.addWidget(QtGui.QCheckBox(ext))

        self.setLayout(layout)
