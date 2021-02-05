import random

class Random:

    def __init__(self, matches = 10):
        self.matches = matches
        self.base = [ x for x in range(self.matches) ]
        print('Random solver initialized!')

    def predict(self):
        return random.sample(self.base, self.matches)

    def learn(self, score):
        return None
