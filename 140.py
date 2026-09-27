from itertools import *
from operator import *
n, *a = map(int, open(0).read().split())
d = [[x if x < 10**5 else 1e300 for x in a[i * n:i * n + n]] for i in range(n)]
for k in range(n):
    for i in range(n):
        d[i] = [*map(min, d[i], map(add, d[k], repeat(d[i][k])))]
print("YNEOS"[min(d[i][i] for i in range(n)) >= 0::2])
