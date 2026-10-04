from itertools import *
g = lambda l: l == [24] if len(l) < 2 else any(g([v, *p[2:]]) for p in permutations(l) for v in (p[0] + p[1], p[0] - p[1], p[0] * p[1]))
print('YNEOS'[g(list(map(int, open(0).read().split()))) < 1::2])
