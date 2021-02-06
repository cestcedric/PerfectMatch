class Solver:
    def __init__(self, matches = 10):
        self.base = [ x for x in range(matches) ]

    def predict(self):
        raise NotImplementedError

    def check(self):
        return False

    def checkIndex(self):
        raise NotImplementedError

    def updateScore(self, score):
        return None
    
    def updateCheck(self, check):
        return None