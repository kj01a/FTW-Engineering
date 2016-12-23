import abc
import datetime

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

class LogFile(WriteFile):

    def __init__(self, log):
        self.log = open(log, 'w')
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def write(self, str):
        self.log.write(self.dt + " " + str + "\n")

class DelimFile(WriteFile):

    def __init__(self, csv, delim):
        self.csv = open(csv, 'w')
        self.delim = delim

    def write(self, str):
        for i in str: self.csv.write("%s" % i + self.delim)
        self.csv.write("\n")
