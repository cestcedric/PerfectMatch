import itertools
from   solvers import Solver

'''
The Tryhard solver iterates over all possible permutations and completely ignores feedback.
'''

class Tryhard(Solver):

    def __init__(self, matches = 10):
        Solver.__init__(self, matches)
        self.base = [ x for x in range(matches) ]
        self.generator = itertools.permutations(self.base)
        print('Tryhard solver initialized!')

    def predict(self):
        return next(self.generator)