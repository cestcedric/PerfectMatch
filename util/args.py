import argparse
from   datetime import datetime
import math

ap = argparse.ArgumentParser()
ap.add_argument('--id', type = str, default = None, help = 'ID for solver run')
ap.add_argument('--matches', type = int, default = 10, help = 'Matches in a game (default: 10)')
ap.add_argument('--limit', type = int, default = None, help = 'Limit number of tries (default: matches!)')
ap.add_argument('--output', type = str, default = 'output', help = 'Output directory for graphs (default: output)')
ap.add_argument('--rounds', type = int, default = 2, help = 'Seasons of PerfectMatch played (default: 1)')
ap.add_argument('--seed', type = int, default = 69420, help = 'Seed for match generation (default: 69420)')
ap.add_argument('--solver', type = str, default = 'Random', help = 'Solver to guess matching (default: Random)')
ap.add_argument('--verbose', action = 'store_true', help = 'Plot scores for all rounds (default: False, just plot 5 rounds)')
ap.set_defaults(verbose = False)
ap.add_argument('--complexity', action = 'store_true', help = 'Perform complexity analysis: compute average duration for 1 - matches pairs (default: False, just plot 5 rounds)')
ap.set_defaults(complexity = False)


my_args = ap.parse_args()

if my_args.id == None:
    now = datetime.now()
    my_args.id = str(now.year).zfill(4) \
        + str(now.month).zfill(2) \
        + str(now.day).zfill(2) \
        + str(now.hour).zfill(2) \
        + str(now.minute).zfill(2) \
        + str(now.second).zfill(2)

if my_args.limit == None:
    my_args.limit = math.factorial(my_args.matches)
