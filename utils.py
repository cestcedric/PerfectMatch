import matplotlib.pyplot as plt
import numpy as np
import os

def createMatch():
    return [ x for x in np.random.permutation(range(10)) ]
    
def score(match, prediction):
    return np.sum(np.array(match) == np.array(prediction))

def checkBox(match, prediction, index):
    return match[index] == prediction[index]

def plotScores(outputpath, data):
    fig, ax = plt.subplots()
    ax.scatter(x = range(len(data)), y = data)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Score')
    fig.savefig(outputpath + '.pdf', format = 'pdf', bbox_inches = 'tight')
    plt.close(fig)

def plotHistogram(outputpath, data, range = [0, 10e6], bins = 100):
    fig, ax = plt.subplots()
    ax.hist(data, range = range, bins = bins)
    ax.set_xlabel('Tries')
    ax.set_ylabel('#Runs')
    fig.savefig(outputpath + '.pdf', format = 'pdf', bbox_inches = 'tight')
    plt.close(fig)