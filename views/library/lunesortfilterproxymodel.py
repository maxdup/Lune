from PySide.QtGui import QSortFilterProxyModel
from PySide import QtCore

from views.library.librarysort import LibrarySort


class LuneSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)
        self.library_sort = LibrarySort()

    def set_library_sort(self, lib_sort):
        self.library_sort = lib_sort
        self.setSortRole(self.library_sort.role)
        self.resort()

    def resort(self):
        # big hack, oh yeah!
        self.setDynamicSortFilter(True)
        self.setDynamicSortFilter(False)

    def lessThan(self, left, right):
        sort = self.library_sort
        while left.data(sort.role) == right.data(sort.role) and sort.fallback:
            sort = sort.fallback

        try:
            ordered = left.data(sort.role) < right.data(sort.role)
        except Exception as e:
            ordered = not bool(left.data(sort.role))
        if self.library_sort.order == QtCore.Qt.AscendingOrder:
            return ordered
        else:
            return not ordered
    
        
