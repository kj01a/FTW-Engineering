#my solution to assignment 3

import os


class ConfigDict(dict):
    def __init__(self, filename):
        self.filename = open(filename, 'r+')

        if os.path.isfile(filename):
            for i in self.filename.readlines():
                filename.strip()
                config_val = i
                key, val = config_val.split('=', 1)
                dict.__setitem__(self, key, val)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        self.filename.write(key + "=" + val)
