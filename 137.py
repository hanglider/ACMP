from itertools import *
from operator import *
n, *a = map(int, open(0).read().split())
f = float("inf")
d = [[a[i * n + j] or f for j in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = min(d[i][i], 0)
for k in range(n):
    for i in range(n):
        d[i] = [*map(min, d[i], map(add, d[k], repeat(d[i][k])))]
for i in range(n):
    b = {j for k in range(n) if d[i][k] < f > -d[k][k] > 0 for j in range(n) if d[k][j] < f}
    print(*[(d[i][j] < f) + (j in b) for j in range(n)])
