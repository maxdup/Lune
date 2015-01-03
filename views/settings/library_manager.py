from PySide import QtGui, QtCore
from models.gui_operation_queue import collect_worker, clean_worker

import multiprocessing

class LibraryManager(QtGui.QWidget):

    def __init__(self, user_settings):
        QtGui.QWidget.__init__(self)

        self.user_settings = user_settings

        layout = QtGui.QVBoxLayout()

        layout.addWidget(QtGui.QLabel('Update your library:'))
        update = QtGui.QPushButton('Update')
        update.clicked.connect(self.update_lib)
        layout.addWidget(update)

        layout.addWidget(QtGui.QLabel('Clean your library:'))
        clean = QtGui.QPushButton('Clean')
        clean.clicked.connect(self.clean_lib)
        layout.addWidget(clean)

        layout.addStretch()
        self.setLayout(layout)

    def update_lib(self):
        p = multiprocessing.Process(target=collect_worker,
                    args=(self.user_settings.operation_queue.multi_queue,
                          self.user_settings.path_list,
                          self.user_settings.extension_list,))
        p.start()
        return

    def clean_lib(self):
        return
