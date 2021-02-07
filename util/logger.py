import sys

class Logger(object):

    def __init__(self, outputpath):
        self.terminal = sys.stdout
        self.log = outputpath

    def write(self, message):
        self.terminal.write(message)
        log = open(self.log, 'a')
        log.write(message)
        log.close()

    def flush(self):
        pass    