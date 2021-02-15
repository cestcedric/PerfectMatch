from   solvers import Solver

'''
The Bumblesort launcher works through the matches from front to back.
Every prediction is generated by swapping two entries from the currently best performing prediction.
The score can then change as follows:
    +2 =>   both new matches are correct, save and go to next index
    -2 =>   two correct matches were destroyed, save reversed swap and go to next index
    +1 =>   one of the new pairs is a match, use the check tool to test which one; 
            continue to find match for current index or go to next one, depending on which one was correct
    else => just try swapping with the next free entry
'''

class Bumblesort(Solver):
    def __init__(self, matches = 10):
        Solver.__init__(self, matches)
        self.matches = matches
        self.reset()
        print('Bumblesort solver initialized!')


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
        self.prediction = Bumblesort.swapEntries(self.base.copy(), self.index, self.swapIndex)
        return self.prediction


    def performCheck(self):
        return self.check


    def checkIndex(self):
        return self.testIndex


    def updateScore(self, score):
        if score == len(self.base):
            self.solved = True
        elif self.baseScore == None:
            self.baseScore = score
            self.testIndex = self.index
            self.check = True
            self.setBaseScore = True
        else:
            if self.baseScore + 2 == score:
                # Swapping created two correct matches
                self.matched[self.index] = self.prediction[self.index]
                self.matched[self.swapIndex] = self.prediction[self.swapIndex]
                self.base = self.prediction.copy()
                self.updateIndex()
            elif self.baseScore - 2 == score:
                # Swapping destroyed two correct matches
                self.matched[self.index] = self.prediction[self.swapIndex]
                self.matched[self.swapIndex] = self.prediction[self.index]
                self.base = Bumblesort.swapEntries(self.prediction.copy(), self.index, self.swapIndex)
                self.updateIndex()
            elif self.baseScore + 1 == score:
                # One of the new pairs is correct
                self.base = self.prediction.copy()
                self.baseScore = score
                self.testIndex = self.index
                self.check = True
            else:
                # score stays the same or reduced by 1
                self.check = False
                self.updateSwapIndex()


    def updateCheck(self, check):
        if self.solved:
            pass
        elif check:
            self.matched[self.testIndex] = self.prediction[self.testIndex]
            self.base = self.prediction.copy()
            self.updateIndex()
        elif self.setBaseScore:
            self.setBaseScore = False
            self.updateSwapIndex()
        else:
            self.matched[self.swapIndex] = self.prediction[self.swapIndex]
            self.updateSwapIndex()


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