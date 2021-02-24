import glob
import importlib
import numpy as np
import os
import PerfectMatch
import solvers
import sys
from   util import logger, utils
from   util.args import my_args

def play(limit, matches, outputpath, rounds, solver, verbose = False):
    try:
        solver = solvers.__dict__[solver](matches = matches)
    except:
        print('Solver not found:', args.solver)
        print('Import and register solver in solvers.__init__.py')
        exit(1)

    fill = len(str(rounds))
    tries = []
    performance = []
    for i in range(1, rounds + 1):
        print('Round ' + str(i).zfill(fill) + '/' + str(rounds) + ': ', end='')
        match = PerfectMatch.PerfectMatch(
            solver = solver,
            matches = matches,
            limit = limit)
        t, p = match.playMatch()
        tries.append(t)
        performance.append(p)
        if verbose:
            utils.plotScores(
                outputpath = os.path.join(outputpath, str(i).zfill(fill)),
                data = p
            )

    print('Mean number of tries to guess match:', np.average(tries))
    print('Median number of tries to guess match:', np.median(tries))
    print('Minimum number of tries to guess match:', np.min(tries))
    print('Maximum number of tries to guess match:', np.max(tries))
    utils.plotScoreSummary(
        outputpath = os.path.join(outputpath, 'summary'),
        data = performance,
        rounds = rounds
    )
    utils.plotHistogram(
        outputpath = os.path.join(outputpath, 'hist'), 
        data = tries,
        range = [0, np.array(tries).max()],
        bins = 10)
    auc_roc = utils.plotAUCROC(
        outputpath = os.path.join(outputpath, 'auc-roc'),
        data = performance,
        limit = limit,
        maxScore = matches
    )
    print('Mean AUC-ROC: {:.2f}'.format(auc_roc))
    return np.average(tries)


def complexityAnalysis(limit, matches, outputpath, rounds, solver, verbose = False):
    numMatches = []
    tries = []
    assert matches > 2
    for N in range(2, matches + 1):
        numMatches.append(N)
        with logger.suppress_stdout():
            t = play(limit = N**2, 
                matches = N, 
                outputpath = outputpath, 
                rounds = args.rounds, 
                solver = args.solver, 
                verbose = False)
        tries.append(t)
        print('N:', N)
        print(t, 'tries')
    utils.plotComplexity(
        outputpath = os.path.join(outputpath, 'complexity'), 
        x = numMatches, 
        y = tries
    )



if __name__ == '__main__':

    args = my_args

    np.random.seed(args.seed)
    outputpath = os.path.join(args.output, args.id)

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

    if args.complexity:
        complexityAnalysis(limit = args.limit, 
            matches = args.matches, 
            outputpath = outputpath, 
            rounds = args.rounds, 
            solver = args.solver, 
            verbose = args.verbose)
    else:
        play(limit = args.limit, 
            matches = args.matches, 
            outputpath = outputpath, 
            rounds = args.rounds, 
            solver = args.solver, 
            verbose = args.verbose)

    print('='*50)

    exit(0)