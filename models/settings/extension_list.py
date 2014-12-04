class ExtensionList(list):

    FORMATS = ['mp3', 'flac', 'aac', 'opus', 'ogg', 'oga',
               'ape', 'mpc', 'wav', 'pcm', 'aiff', 'm4a']

    def __init__(self, user_settings, *args):
        list.__init__(self, *args)
        self.user_settings = user_settings

    def append(self, ext):
        list.append(self, ext)
        self.user_settings.notify()

    def remove(self, ext):
        list.remove(self, ext)
        self.user_settings.notify()
        
    
