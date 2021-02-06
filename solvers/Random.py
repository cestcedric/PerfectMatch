import random
from   solvers import Solver

class Random(Solver):

    def __init__(self, matches = 10):
        Solver.__init__(self)
        self.matches = matches
        self.base = [ x for x in range(self.matches) ]
        print('Random solver initialized!')

    def predict(self):
        return random.sample(self.base, self.matches)