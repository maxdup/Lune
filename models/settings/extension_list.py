
class ExtensionList(list):
    def __init__(self, settings_dao, *args):
        list.__init__(self, *args)
        self._settings_dao = settings_dao
        for ext in self._settings_dao.get_exts():
            list.append(self, ext)

    def append(self, ext):
        list.append(self, ext)
        self._settings_dao.add_ext(ext)

    def remove(self, ext):
        list.remove(self, ext)
        self._settings_dao.del_ext(ext)
        
        
    
