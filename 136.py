from itertools import *
from operator import *
n, *a = map(int, open(0).read().split())
a = [x % 10**9 for x in a]
d = [a[i * n:i * n + n] for i in range(n)]
for k in range(n):
    for i in range(n):
        d[i] = [*map(min, d[i], map(add, d[k], repeat(d[i][k])))]
print(max(x for r in d for x in r if x < 10**6))
