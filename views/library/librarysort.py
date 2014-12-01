from PySide import QtCore

class LibrarySort:
    def __init__(self, text, role=0, order=True):
        self.text = text
        self.role = role
        if order:
            self.order = QtCore.Qt.AscendingOrder
        else:
            self.order = QtCore.Qt.DescendingOrder
