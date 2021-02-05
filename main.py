from   args import my_args
import importlib
import numpy as np
import os
import PerfectMatch
import solvers
import tools

args = None
outputpath = None
solver = None

def play(rounds):
    tries = []
    for _ in range(rounds):
        match = PerfectMatch.PerfectMatch(outputpath = outputpath, solver = solver, limit = args.limit)
        tries.append(match.playMatch())
    print('Average number of tries to guess match:', np.average(tries))


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

    args.limit = 1000

    print('Run ID:', args.id)
    print('Output directory:', args.output)
    print('Solver:', args.solver)
    print('Maximum tries:', args.limit)

    play(rounds = args.rounds)

    exit(0)