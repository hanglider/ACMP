from itertools import *
n, m, p, *t = map(int, open(0).read().split())
g = [[0] * m for _ in range(n)]
for a, e in zip(t[::2], t[1::2]):
    g[a - 1][m - e] = 1
c = [0] * m
s = 0
for r in g:
    s += sum(x * y for x, y in zip(r, accumulate([0] + c)))
    c = [x + y for x, y in zip(c, r)]
print(s)
