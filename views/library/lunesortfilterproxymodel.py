from PySide.QtGui import QSortFilterProxyModel
from PySide import QtCore
class LuneSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)
        self.sort_order = QtCore.Qt.AscendingOrder

    def sortOrder(self):
        return self.sort_order

    def setSortOrder(self, sort_order):
        self.sort_order = sort_order

    def lessThan(self, left, right):
        ordered = left.data(QSortFilterProxyModel.sortRole(self)) < right.data(QSortFilterProxyModel.sortRole(self))
        if self.sortOrder() == QtCore.Qt.AscendingOrder:
            return ordered
        else:
            return not ordered
    
        
