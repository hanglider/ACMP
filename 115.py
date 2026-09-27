from itertools import *
from operator import *
n, m, *a = map(int, open(0).read().split())
r = -999
for i in range(n):
    c = [0] * m
    for j in range(i, n):
        c = [*map(add, c, a[j * m:j * m + m])]
        p = [0, *accumulate(c)]
        r = max(r, *map(sub, p[1:], accumulate(p, min)))
print(r)
