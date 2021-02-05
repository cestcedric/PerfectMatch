import matplotlib as pl
import numpy as np
import os

def createMatch():
    return [ x for x in np.random.permutation(range(10)) ]
    
def score(match, prediction):
    return np.sum(np.array(match) == np.array(prediction))

def checkBox(match, prediction, index):
    return match[index] == prediction[index]

def plotPerformance(output, scores):
    return None

