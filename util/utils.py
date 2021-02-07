import matplotlib.pyplot as plt
import numpy as np
import os
import random

def createMatch(matches):
    return [ x for x in np.random.permutation(range(matches)) ]
    

def score(match, prediction):
    assert validPrediction(prediction)
    return np.sum(np.array(match) == np.array(prediction))


def validPrediction(prediction):
    for i in range(len(prediction)):
        if not i in prediction:
            return False
    return True


def checkPair(match, prediction, index):
    return match[index] == prediction[index]


def cumulative(data):
    maxScore = -1
    out = []
    for d in data:
        if d > maxScore:
            maxScore = d
        out.append(maxScore)
    return out


def padded(data, length = 0):
    if len(data) < length:
        pad = [data[-1]]*(length - len(data))
        return data + pad
    return data


def plotScores(outputpath, data):
    fig, ax = plt.subplots()
    ax.scatter(x = range(len(data)), y = data)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Score')
    fig.savefig(outputpath + '.pdf', format = 'pdf', bbox_inches = 'tight')
    plt.close(fig)


def plotScoreSummary(outputpath, data):
    markers = ['o', '*', '+', 'x', 'v']
    samples = random.sample(data, 5)

    fig, ax = plt.subplots()
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Score')
    for m, s in zip(markers, samples):
        ax.scatter(x = range(len(s)), y = s, marker = m)
    fig.savefig(outputpath + '.pdf', format = 'pdf', bbox_inches = 'tight')
    plt.close(fig)


def plotHistogram(outputpath, data, range = [0, 10e6], bins = 100):
    fig, ax = plt.subplots()
    ax.hist(data, range = range, bins = bins)
    ax.set_xlabel('# Tries')
    ax.set_ylabel('# Runs')
    fig.savefig(outputpath + '.pdf', format = 'pdf', bbox_inches = 'tight')
    plt.close(fig)


def plotAUCROC(outputpath, data, limit, maxScore):
    # compute AUC-ROC equivalent
    list_cumulative = [ padded(cumulative(d), limit) for d in data ]
    list_average = [0] + [ sum(x)/len(x) for x in zip(*list_cumulative) ]
    list_ratio = [ x/maxScore for x in list_average ]
    auc_roc = np.sum(list_average) / (limit*maxScore)
    # plot
    fig, ax = plt.subplots()
    ax.plot(list_ratio)
    ax.plot([0, limit], [0, 1], color = 'red', linestyle = '--', linewidth = 1)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Share of correct matches')
    ax.set_ylim(0, 1)
    ax.set_xlim(0, limit)
    ax.text(0.05, 0.95, 
            'Mean AUC-ROC: {:.2f}'.format(auc_roc), 
            transform=ax.transAxes, 
            fontsize=14,
            verticalalignment='top', 
            bbox = {'boxstyle':'round', 'facecolor':'white'})
    fig.savefig(outputpath + '.pdf', format = 'pdf', bbox_inches = 'tight')
    plt.close(fig)
    return auc_roc
