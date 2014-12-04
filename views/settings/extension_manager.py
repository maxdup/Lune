from PySide import QtGui, QtCore
from models.settings.extension_list import ExtensionList


class ExtensionManager(QtGui.QWidget):

    def __init__(self, extension_list):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        self._ext_list = extension_list

        layout.addWidget(QtGui.QLabel('include these formats in my library:'))

        self.boxes = QtGui.QButtonGroup()
        self.boxes.setExclusive(False)
        for i, ext in enumerate(ExtensionList.FORMATS):
            ext_checkbox = QtGui.QCheckBox(ext)
            self.boxes.addButton(ext_checkbox)
            layout.addWidget(ext_checkbox, i)
            if ext in self._ext_list:
                ext_checkbox.setCheckState(QtCore.Qt.CheckState.Checked)

        self.boxes.buttonReleased.connect(self.value_changed)

        self.setLayout(layout)

    def value_changed(self, checkbox):
        if checkbox.isChecked():
            self._ext_list.append(checkbox.text())
        else:
            self._ext_list.remove(checkbox.text())
