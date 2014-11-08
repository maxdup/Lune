from PySide import QtGui, QtCore
from PySide.QtGui import QSortFilterProxyModel
from models.album import Album


class SortFilterProxy:

    def __init__(self, qlist, strategy):        
        self.qlist = qlist
        self.item_strat = strategy

        self.model = QtGui.QStandardItemModel(self.qlist)

        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setDynamicSortFilter(True)
        self.qlist.setModel(self.proxymodel)

        self.icon = QtGui.QIcon(':img/placeholder.jpg')

    def add(self, obj):
        item = self.item_strat.get_item(obj)
        if type(obj) == Album:
            item.setIcon(self.icon)
        self.model.appendRow(item)

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
