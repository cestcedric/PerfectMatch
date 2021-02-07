from   args import my_args
import glob
import importlib
import numpy as np
import os
import PerfectMatch
import solvers
import sys
from   util import logger, utils

args = None
outputpath = None
solver = None

def play(rounds):
    fill = len(str(rounds))
    tries = []
    performance = []
    for i in range(1, rounds + 1):
        print('Round ' + str(i).zfill(fill) + '/' + str(rounds) + ': ', end='')
        match = PerfectMatch.PerfectMatch(
            solver = solver,
            matches = args.matches,
            limit = args.limit)
        t, p = match.playMatch()
        tries.append(t)
        performance.append(p)
        if args.verbose:
            utils.plotScores(
                outputpath = os.path.join(outputpath, str(i).zfill(fill)),
                data = p
            )

    print('Mean number of tries to guess match:', np.average(tries))
    print('Median number of tries to guess match:', np.median(tries))
    utils.plotScoreSummary(
        outputpath = os.path.join(outputpath, 'summary'),
        data = performance
    )
    utils.plotHistogram(
        outputpath = os.path.join(outputpath, 'hist'), 
        data = tries,
        range = [0, args.limit],
        bins = 10)
    auc_roc = utils.plotAUCROC(
        outputpath = os.path.join(outputpath, 'auc-roc'),
        data = performance,
        limit = args.limit,
        maxScore = args.matches
    )
    print('Mean AUC-ROC: {:.2f}'.format(auc_roc))


if __name__ == '__main__':

    args = my_args

    np.random.seed(args.seed)
    outputpath = os.path.join(args.output, args.id)

    try:
        solver = solvers.__dict__[args.solver](matches = 10)
    except:
        print('Solver not found:', args.solver)
        print('Import and register solver in solvers.__init__.py')
        exit(1)

    if not os.path.exists(args.output):
        os.mkdir(args.output)

    if not os.path.exists(outputpath):
        os.mkdir(outputpath)

    files = glob.glob(os.path.join(outputpath,'*'))
    for f in files:
        os.remove(f)
    sys.stdout = logger.Logger(os.path.join(outputpath, 'out.log'))

    print('-'*50)
    print('Run ID:', args.id)
    print('Output directory:', os.path.join(args.output, args.id))
    print('Solver:', args.solver)
    print('Rounds:', args.rounds)
    print('Maximum tries:', args.limit)
    print('-'*50)

    play(rounds = args.rounds)

    print('='*50)

    exit(0)