from PySide import QtGui, QtCore

class ExtensionManager(QtGui.QWidget):

    FORMATS = ['mp3', 'flac', 'aac', 'opus', 'ogg', 'oga', 'ape', 'mpc', 'wav', 'pcm', 'aiff', 'm4a']

    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.user_settings = user_settings

        layout.addWidget(QtGui.QLabel('include these formats in my library:'))

        self.boxes = QtGui.QButtonGroup()
        self.boxes.setExclusive(False)
        for i, ext in enumerate(self.FORMATS):
            ext_checkbox = QtGui.QCheckBox(ext)
            self.boxes.addButton(ext_checkbox)
            layout.addWidget(ext_checkbox, i)

        self.boxes.buttonReleased.connect(self.value_changed)

        self.setLayout(layout)

    def value_changed(self, cb):
        if cb.isChecked():
            self.user_settings.extension_list.append(cb.text())
        else:
            self.user_settings.extension_list.remove(cb.text())
