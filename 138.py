from itertools import *
from operator import *
n, m, *a = map(int, open(0).read().split())
f = float("inf")
w = [[f] * n for _ in range(n)]
for i in range(0, 3 * m, 3):
    u, v, c = a[i:i + 3]
    w[u - 1][v - 1] = min(w[u - 1][v - 1], c)
d = [0] + [f] * (n - 1)
for _ in range(n):
    for u in range(n):
        d = [*map(min, d, map(add, w[u], repeat(d[u])))]
print(*[x if x < f else 30000 for x in d])
