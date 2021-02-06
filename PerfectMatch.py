import utils

class PerfectMatch:
    def __init__(self,
                outputpath,
                solver,
                limit):
        self.limit = limit
        self.match = utils.createMatch()
        self.outputpath = outputpath
        self.solver = solver

    def playMatch(self):
        solved = False
        scores = []
        i = 0
        while True:
            prediction = self.solver.predict()
            score = utils.score(match = self.match, prediction = prediction)
            self.solver.updateScore(score)
            if self.solver.check():
                self.solver.updateCheck(self.solver.checkIndex())

            scores.append(score)

            solved = self.match == prediction
            i += 1
            if solved or i >= self.limit:
                break
        
        if solved:
            print('Perfect match found after', i, 'tries!')
        else:
            print('Perfect match not found!')
        
        utils.plotScores(
            outputpath = self.outputpath,
            data = scores
        )
        return i