from PySide import QtGui
from PySide.QtGui import QListView, QStandardItemModel, QSortFilterProxyModel


class LibraryListView(QListView):
    def __init__(self, strategy):
        QListView.__init__(self)

        self.item_strat = strategy

        self.itemmodel = QStandardItemModel()
        self.proxymodel = QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.itemmodel)
        self.proxymodel.setDynamicSortFilter(True)
        self.setModel(self.proxymodel)
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    def add(self, obj):
        item = self.item_strat.get_item(obj)
        self.itemmodel.appendRow(item)
        return item

    def filter(self, field, value):
        self.proxymodel.setFilterRole(field)
        self.proxymodel.setFilterFixedString(value)
        


        
    
