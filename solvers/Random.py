import random
from   solvers import Solver

'''
The Random solver just produces random permutations and ignores feedback.
'''

class Random(Solver):

    def __init__(self, matches = 10):
        Solver.__init__(self, matches)
        self.matches = matches
        self.base = [ x for x in range(self.matches) ]
        print('Random solver initialized!')

    def predict(self):
        return random.sample(self.base, self.matches)