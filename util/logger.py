import sys

class Logger(object):
    def __init__(self, outputpath):
        self.terminal = sys.stdout
        self.log = open(outputpath, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        pass    