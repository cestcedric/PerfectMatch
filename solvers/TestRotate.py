from   solvers import Solver

'''
The TestRotate solver works through the matches from front to back.
At every index it tries all not yet used pairings.
The score is ignored, every combination is only judged based on the individual check.
'''

class TestRotate(Solver):
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

        return self


    def predict(self):
        prediction = self.matched.copy()
        prediction[self.index] = self.base[self.testIndex]
        prediction = self.fill(prediction)
        return prediction


    def performCheck(self):
        return True


    def checkIndex(self):
        return self.index

    
    def updateCheck(self, check):
        if check:
            self.matched[self.index] = self.base[self.testIndex]
            self.index += 1
            self.resetTestIndex()
        else:
            self.updateTestIndex()


    def resetTestIndex(self):
        self.testIndex = 0
        while self.base[self.testIndex] in self.matched:
            self.testIndex += 1
            if self.testIndex == len(self.base):
                raise ValueError('Unable to find matching value for pair ' + str(self.index))

    
    def updateTestIndex(self):
        self.testIndex += 1
        while self.base[self.testIndex] in self.matched:
            self.testIndex += 1
            if self.testIndex == len(self.base):
                raise ValueError('Unable to find matching value for pair ' + str(self.index))


    def fill(self, data):
        availableEntries = [ b for b in self.base if b not in data ]
        availableIndices = [ i for i in range(len(data)) if data[i] == None ]

        for e,i in zip(availableEntries, availableIndices):
            data[i] = e

        return data

