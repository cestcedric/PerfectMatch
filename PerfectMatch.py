import tools

class PerfectMatch:
    def __init__(self,
                outputpath,
                solver,
                limit):
        self.limit = limit
        self.match = tools.createMatch()
        self.solver = solver

    def playMatch(self):
        solved = False
        scores = []
        i = 0
        while True:
            prediction = self.solver.predict()
            score = tools.score(match = self.match, prediction = prediction)
            self.solver.learn(score)

            scores.append(score)

            solved = self.match == prediction
            i += 1
            if solved or i >= self.limit:
                break
        
        if solved:
            print('Perfect match found after', i, 'tries!')
        else:
            print('Perfect match not found!')
        
        #TODO: make graph
        return i