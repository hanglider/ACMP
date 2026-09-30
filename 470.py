from itertools import *
f = open(0)
h, w, n = map(int, next(f).split())
q = [[0] * (w + 1)]
for _ in range(h):
    q += [x + y for x, y in zip(q[-1], [0, *accumulate(map(int, next(f).split()))])],
while s := list(islice(f, 9999)):
    x = map(int, ' '.join(s).split())
    print('\n'.join(str(q[c][d] - q[a - 1][d] - q[c][b - 1] + q[a - 1][b - 1]) for a, b, c, d in zip(x, x, x, x)))
