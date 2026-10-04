from functools import lru_cache
from math import gcd
n, k = map(int, input().split())
d = [i for i in range(1, int(n**0.5) + 1) if n % i == 0]
d = sorted(set(d + [n // i for i in d]))
g = [[t for t in range(i + 1, len(d)) if gcd(d[i], d[t]) == 1] for i in range(len(d))]
@lru_cache(None)
def f(i, r, j):
    s = 0
    for t in g[i]:
        if d[t]**j > r:
            break
        s += j < 2 or f(t, r // d[t], j - 1)
    return s
print(sum(f(t, n // d[t], k - 1) for t in range(len(d))))
