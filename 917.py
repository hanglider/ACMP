from math import *
n, *l = map(int, open(0).read().split())
m = max(l)
l.remove(m)
f = lambda r, s: sum(asin(x / 2 / r) for x in l) + s * asin(m / 2 / r)
s = 1 - 2 * (f(m / 2, 1) < pi)
a = m / 2
b = 1e7
for i in range(200):
    r = (a + b) / 2
    if (f(r, s) > pi * (s > 0)) == (s > 0):
        a = r
    else:
        b = r
print("%.2f" % (sum(r * r * sin(2 * asin(x / 2 / r)) for x in l) / 2 + s * r * r * sin(2 * asin(m / 2 / r)) / 2))
