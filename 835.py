from bisect import *
from itertools import *
n, W, *a = map(int, open(0).read().split())
T = [[(0, 0)], [(0, n << 20)]]
for i in range(n):
    d = (a[2 * i + 1] << 40) - (1 << 20) + (1 << n - 1 - i)
    T[i < n // 2] += [(x + a[2 * i], y + d) for x, y in T[i < n // 2]]
R, L = T
R.sort()
u = [x for x, y in R]
v = list(accumulate([y for x, y in R], max))
b = max(y + v[bisect(u, W - x) - 1] for x, y in L if x <= W)
s = [i + 1 for i in range(n) if b >> n - 1 - i & 1]
print(len(s), b >> 40)
print(*s)
