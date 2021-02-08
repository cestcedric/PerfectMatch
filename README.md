# PerfectMatch

----

## Task

A perfect match is a bijective mapping between 2xN points.
Solving this matching is supported by two ways to gain information: a score signaling the overall number of correctly matched points (without revealing which are the correct pairs) and the possibility to directly investigate whether or not a single pairing is part of the perfect match.

This is a round based game, where both the total score as well as one pairing can be checked per iteration.

A questionable adaption of this problem with 2x10 participants is implemented in the RTL2 show "Are you the One", which is not necessarily endorsed by everyone.

----

## Leaderboard

Entries on the leaderboard are playing 1000 rounds with 10 pairings.

| Algorithm | Mean tries | Median tries | AUC-ROC |
|-----------|------------|--------------|---------|
| TestRotate | 30.654 | 31 | 1.00 |
