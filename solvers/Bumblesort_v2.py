from   solvers import Solver

'''
BSv2 is an improved Bumblesort variant with improved efficiency when updating indices.
'''

class BSv2(Solver):
    def __init__(self, matches = 10):
        Solver.__init__(self, matches)
        self.matches = matches
        self.reset()
        print('BSv2 solver initialized!')


    def reset(self):
        self.base = [ x for x in range(self.matches) ]
        self.matched = [ None for b in self.base ]

        self.index = 0
        self.testIndex = 0
        self.swapIndex = 0

        self.baseScore = None
        self.setBaseScore = True
        self.check = False
        self.prediction = None
        self.solved = False

        return self


    def predict(self):
        self.prediction = BSv2.swapEntries(self.base.copy(), self.index, self.swapIndex)
        return self.prediction


    def performCheck(self):
        return self.check


    def checkIndex(self):
        return self.testIndex


    def updateScore(self, score):
        #TODO:
        pass


    def updateCheck(self, check):
        #TODO:
        pass


    def updateIndex(self):
        self.index = 0
        self.swapIndex = 0
        while self.matched[self.index] != None:
            self.index += 1
            if self.index == len(self.base):
                raise ValueError('Unable to find matching value for pair ' + str(self.index))
        self.updateSwapIndex()
        self.baseScore = None
        self.setBaseScore = True
        self.check = False


    def updateSwapIndex(self):
        tmp = self.swapIndex
        self.swapIndex = (self.swapIndex + 1) % len(self.base)
        while self.matched[self.swapIndex] != None:
            self.swapIndex = (self.swapIndex + 1) % len(self.base)
            if self.swapIndex == tmp:
                raise ValueError('Unable to find matching value for pair ' + str(self.swapIndex))


    @staticmethod
    def swapEntries(array, a, b):
        array[a], array[b] = array[b], array[a]
        return array
