# -*- coding: utf-8 -*-

import json
import os

def read(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as input_file:
            return json.load(input_file)
    else:
        #default setting
        return { 'libpaths': [],
                 'extensions': ['mp3', 'flac', 'm4a', 'wav'] }

def save(user_settings):
    with open(user_settings.filename, 'w') as outfile:
        json_out = { 'libpaths': user_settings.path_list,
                     'extensions': user_settings.extension_list }
        json.dump(json_out, outfile)

