from itertools import *
n, k, *a = map(int, open(0).read().split())
c, p = max((-sum(a[n * n + i] for i in p) - sum(a[i * n + j] for i, j in zip(p, p[1:])), p) for p in permutations(range(n), k))
print(-c)
print(*[i + 1 for i in p])
