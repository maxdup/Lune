# -*- coding: utf-8 -*-

import json
import os


class Settings():

    '''
    settings are saved as json.
    the json object should look something like:
    {
        'libpaths':['library path 1', library path 2]
    }
    (plz update this schema as things move forward)
    '''

    def __init__(self):
        self.settings = {
            'libpaths': []
            }
        if os.path.isfile('settings.txt'):
            with open('settings.txt', 'r') as inputfile:
                self.settings = json.load(inputfile)

    def getPaths(self):
        return self.settings['libpaths']

    def addPath(self, path):
        #validate path?
        self.settings['libpaths'].append(path)

    def writePath(self, path):
        self.settings['libpaths'].append(path)
        self.save()

    def delPath(self, path):
        if path in self.settings['libpaths']:
            self.settings['libpaths'].remove(path)
            self.save()

    def save(self):
        with open('settings.txt', 'w') as outfile:
            json.dump(self.settings, outfile)
