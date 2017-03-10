import os
import json


class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()
    def __str__(self):
        return ('key "{0}" not found.  Available keys: '
                '({1})'.format(self.key, ', '.join(self.keys)))

class ConfigDict(dict):

    config_directory = 'E:/FTW-Engineering/Welch/OOPlearning/assignments/ass5'

    def __init__(self, filename):
        self._filename = os.path.join(ConfigDict.config_directory, filename + '.json')

        if not os.path.isfile(self._filename):
            with open(self._filename, 'w') as f:
                json.dump({}, f)

        with open(self._filename) as f:
            conf = json.load(f)
            self.update(conf)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as f:
            json.dump(self, f)
