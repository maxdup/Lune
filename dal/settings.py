# -*- coding: utf-8 -*-

import json
import os


class Settings():
    '''
    settings are saved as json.
    the json object should look something like:
    {
        'libpaths':['library path 1', 'library path 2']
    }
    (plz update this schema as things move forward)
    '''

    def __init__(self):
        self.settings = {
            'libpaths': []
        }
        if os.path.isfile('settings.json'):
            with open('settings.json', 'r') as input_file:
                self.settings = json.load(input_file)

    def get_paths(self):
        return self.settings['libpaths']

    def add_path(self, path):
        # validate path?
        self.settings['libpaths'].append(path)
        self.save()

    def del_path(self, path):
        if path in self.settings['libpaths']:
            self.settings['libpaths'].remove(path)
            self.save()

    def save(self):
        with open('settings.json', 'w') as outfile:
            json.dump(self.settings, outfile)
