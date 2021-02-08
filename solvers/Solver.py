class Solver:
    def __init__(self, matches = 10):
        pass

    def predict(self):
        raise NotImplementedError

    def performCheck(self):
        return False

    def checkIndex(self):
        raise NotImplementedError

    def updateScore(self, score):
        pass
    
    def updateCheck(self, check):
        pass

    def reset(self):
        return self