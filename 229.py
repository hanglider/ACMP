from fractions import Fraction as F
from bisect import bisect
r = open(0).read().split()
a = [(F(r[i]), F(r[i + 1])) for i in range(1, len(r), 2)]
X = max(x for x, y in a)
L = max(y for x, y in a) / 100 or 1e-9
R = X and 100 / X or 1e9
d = {}
for x, y in a:
    d[x] = max(d.get(x, y), y)
h = []
for p in sorted(d.items()):
    while len(h) > 1 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) >= (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]):
        h.pop()
    h += [p]
b = [-1e9] + [(u[1] - v[1]) / (v[0] - u[0]) for u, v in zip(h, h[1:])] + [1e9]
s = [x for x, y in h] + [1e9]
w = []
for k, (x, y) in enumerate(a):
    i = bisect(s, x) - 1
    u, v = h[i], (h + [(0, 0)])[i + 1]
    c = (x, y) == u
    if (c or (v[0] - u[0]) * (y - u[1]) == (v[1] - u[1]) * (x - u[0]) and x < v[0]) and b[i + 1 - c] <= R and b[i + 1] >= L:
        w += [k + 1]
print(len(w))
print(*w)
