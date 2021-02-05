from   args import my_args
import glob
import importlib
import numpy as np
import os
import PerfectMatch
import solvers
import utils

args = None
outputpath = None
solver = None

def play(rounds):
    fill = len(str(rounds))
    tries = []
    for i in range(0, rounds + 1):
        print('Round ' + str(i).zfill(fill) + '/' + str(rounds) + ': ', end='')
        match = PerfectMatch.PerfectMatch(
            outputpath = os.path.join(outputpath, str(i).zfill(fill)), 
            solver = solver, 
            limit = args.limit)
        tries.append(match.playMatch())
    print('Mean number of tries to guess match:', np.average(tries))
    print('Median number of tries to guess match:', np.median(tries))
    utils.plotHistogram(
        outputpath = os.path.join(outputpath, 'hist'), 
        data = tries,
        range = [0, args.limit],
        bins = 10)


if __name__ == '__main__':

    args = my_args

    # Set parameters here for debugging
    args.limit = 100
    args.rounds = 1000
    args.id = 'test'

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