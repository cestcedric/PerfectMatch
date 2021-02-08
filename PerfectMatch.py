from util import utils

class PerfectMatch:
    def __init__(self,
                solver,
                matches,
                limit):
        self.limit = limit
        self.matches = matches
        self.match = utils.createMatch(self.matches)
        self.solver = solver.reset()

    def playMatch(self):
        solved = False
        scores = []
        i = 0
        
        while True:
            prediction = self.solver.predict()
            score = utils.score(match = self.match, prediction = prediction)
            self.solver.updateScore(score)
            if self.solver.performCheck():
                check = utils.checkPair(
                    match = self.match, 
                    prediction = prediction, 
                    index = self.solver.checkIndex())
                self.solver.updateCheck(check)

            scores.append(score)

            solved = self.match == prediction
            i += 1
            if solved or i >= self.limit:
                break
        
        if solved:
            print('Perfect match found after', i, 'tries!')
        else:
            print('Perfect match not found!')
        
        return i, scores