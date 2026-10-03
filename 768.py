from itertools import *
from collections import *
n, *a = map(int, open(0).read().split())
c = Counter((x + u, y + v, (x - u)**2 + (y - v)**2) for (x, y), (u, v) in combinations(zip(a[::2], a[1::2]), 2))
print(sum(k * k - k for k in c.values()) // 2)
