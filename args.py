import argparse
from   datetime import datetime

ap = argparse.ArgumentParser()
ap.add_argument('--id', type = str, default = None, help = 'ID for solver run')
ap.add_argument('--limit', type = int, default = 4*10e5, help = 'Limit number of tries')
ap.add_argument('--output', type = str, default = 'output', help = 'Output directory for graphs (default: output)')
ap.add_argument('--rounds', type = int, default = 2, help = 'Seasons of PerfectMatch played (default: 1)')
ap.add_argument('--seed', type = int, default = 69420, help = 'Seed for match generation (default: 69420)')
ap.add_argument('--solver', type = str, default = 'Random', help = 'Solver to guess matching (default: Random)')


my_args = ap.parse_args()

if my_args.id == None:
    now = datetime.now()
    my_args.id = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
