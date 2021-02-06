from solvers import Solver

class Tryhard:

    def __init__(self):
        Solver.__init__(self)
        print('Tryhard solver initialized!')

    def predict(self):
        raise NotImplementedError

    def updateScore(self, score):
        raise NotImplementedError