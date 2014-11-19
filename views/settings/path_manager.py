from PySide import QtGui, QtCore

class PathManager(QtGui.QWidget):

    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.user_settings = user_settings
        self.library_list = QtGui.QListWidget()

        def add_path_dialog():
            path = QtGui.QFileDialog.getExistingDirectory()
            if path:
                path_obj = self.user_settings.add_path(path)
                self.add_path(path_obj)

        btn_add_paths = QtGui.QPushButton('add paths')
        btn_add_paths.clicked.connect(add_path_dialog)

        for path_obj in self.user_settings.path_list:
            self.add_path(path_obj)

        layout.addWidget(self.library_list)
        layout.addWidget(btn_add_paths)
        self.setLayout(layout)

    def add_path(self, path_obj):
        size = QtCore.QSize(25, 25)
        item = QtGui.QListWidgetItem(self.library_list)
        item.setSizeHint(size)
        item_widget = PathItem(path_obj, item, self)
        self.library_list.setItemWidget(item, item_widget)

class PathItem(QtGui.QWidget):
    def __init__(self, path_obj, item, path_manager):
        self.path_obj = path_obj
        self.item = item
        self.path_manager = path_manager

        QtGui.QWidget.__init__(self)
        layout = QtGui.QHBoxLayout()

        label = QtGui.QLabel(path_obj.path)
        remove = QtGui.QPushButton('x')
        remove.setObjectName('smallX')
        remove.clicked.connect(self.remove)

        layout.setContentsMargins(5,0,5,0)

        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(remove)
        self.setLayout(layout)

    def remove(self):
        self.path_obj.remove()
        index = self.item.listWidget().row(self.item)
        self.path_manager.library_list.takeItem(index)
