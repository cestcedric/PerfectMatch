from   contextlib import contextmanager
import os
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

@contextmanager
def suppress_stdout():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout