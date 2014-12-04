# -*- coding: utf-8 -*-

import json
import os


class SettingsDAO():
    '''
    settings are saved as json.
    the json object should look something like:
    {
        'libpaths': ['library path 1', 'library path 2'],
        'extensions': ['mp3', 'flac']
    }
    (plz update this schema as things move forward)
    '''

    def __init__(self):
        self.settings = {
            'libpaths': [],
            'extensions': []
        }
        if os.path.isfile('settings.json'):
            with open('settings.json', 'r') as input_file:
                self.settings = json.load(input_file)
        else:
            #default setting
            self.settings['extensions'] = ['mp3', 'flac', 'm4a', 'wav']

    def save(self):
        with open('settings.json', 'w') as outfile:
            json.dump(self.settings, outfile)

    def get_paths(self):
        return self.settings['libpaths']

    def add_path(self, path):
        self.settings['libpaths'].append(path)
        self.save()

    def del_path(self, path):
        if path in self.settings['libpaths']:
            self.settings['libpaths'].remove(path)
            self.save()

    def get_exts(self):
        return self.settings['extensions']

    def add_ext(self, ext):
        if ext not in self.settings['extensions']:
            self.settings['extensions'].append(ext)
            self.save()

    def del_ext(self, ext):
        if ext in self.settings['extensions']:
            self.settings['extensions'].remove(ext)
            self.save()
