from math import *
from bisect import *
from itertools import accumulate as u
from array import array as A
n = int(input())
g = A('d')
h = A('d')
for _ in range(n):
    f, t = map(float, input().split())
    h.append(f)
    g.append(t % 360)
o = sorted(range(n), key=g.__getitem__)
d = A('d', (g[k] for k in o))
d += A('d', (t + 360 for t in d))
x = A('d', [0]) + A('d', u(h[o[k % n]] * cos(radians(d[k])) for k in range(2 * n)))
y = A('d', [0]) + A('d', u(h[o[k % n]] * sin(radians(d[k])) for k in range(2 * n)))
c = sorted({t % 180 for t in g})
b = -1
for i in range(len(c)):
    for k in 0, 180:
        l = ((c[i] + c[i - 1] + 180 * (i < 1)) / 2 + k) % 360
        p = bisect(d, l)
        q = bisect_left(d, l + 180)
        v = (x[q] - x[p])**2 + (y[q] - y[p])**2
        if v > b:
            b, w = v, (p, q)
p, q = w
r = [o[k % n] + 1 for k in range(p, q)] or [1]
print(len(r))
print(*r)
