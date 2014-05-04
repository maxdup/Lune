import json


class UserSettings():

    '''
    settings are saved as json.
    the json object should look something like:
    {
        'libPath':['library path 1', library path 2]
    }
    (plz update this schema as things move forward)
    '''

    def __init__(self):
        self.uSettings = {}
        with open('settings.txt', 'r') as inputfile:
            self.uSettings = json.load(inputfile)

    def getPaths(self):
        return self.uSettings['libPaths']

    def addPath(self, path):
        #validate path?
        self.uSettings['libPaths'].append(path)
        self.save()

    def removePath(self, path):
        if path in self.uSettings['libPaths']:
            self.uSettings['libPaths'].remove(path)
            self.save()

    def save(self):
        with open('settings.txt', 'w') as outfile:
            json.dump(self.uSettings, outfile)