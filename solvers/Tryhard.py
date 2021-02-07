import itertools
from   solvers import Solver

class Tryhard:

    def __init__(self, matches = 10):
        Solver.__init__(self, matches)
        self.base = [ x for x in range(matches) ]
        self.generator = itertools.permutations(self.base)
        print('Tryhard solver initialized!')

    def predict(self):
        return next(self.generator)

    def check(self):
        return False

    def checkIndex(self):
        raise NotImplementedError

    def updateScore(self, score):
        pass
    
    def updateCheck(self, check):
        pass