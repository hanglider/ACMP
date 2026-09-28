from math import *
g = (float(w) for l in open(0) for w in l.split())
n, x, y = next(g), next(g), next(g)
e = []
for u, v, r in zip(g, g, g):
    d = asin(r / hypot(u - x, v - y))
    a = (atan2(v - y, u - x) - d) % tau
    b = a + 2 * d
    e += [(a, min(b, tau))]
    if b > tau:
        e += [(0, b - tau)]
c = 0
for a, b in sorted(e):
    if a > c + 1e-9:
        break
    c = max(c, b)
print(['NO', 'YES'][c > tau - 1e-9])
