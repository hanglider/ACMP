from math import atan2
from bisect import *
n, *d = map(int, open(0).read().split())
p = sorted(zip(d[::2], d[1::2]))
r = sum(1 << 10 * k for k in range(n))
f = []
v = []
for x, y in p:
    g = [atan2(b - y, a - x) for a, b in p]
    l = []
    q = [0] * n
    for b in range(len(f) + 1, n):
        q[b] = bisect(l, g[b])
        insort(l, g[b])
    f += [sum(q[k] << 10 * k for k in range(n))]
    v += [(q, g)]
c = 0
for i in range(n):
    q, g = v[i]
    o = sorted(range(i + 1, n), key=g.__getitem__)
    s = [0] * (n + 1)
    for t in range(len(o) - 1, -1, -1):
        s[t] = s[t + 1] + (1 << 10 * o[t])
    for t in range(len(o)):
        j = o[t]
        z = (f[i] - f[j] - s[t + 1] + (256 - q[j]) * r ^ 256 * r) + 511 * r & 512 * r
        c += n - 1 - j - (z >> 10 * j + 10).bit_count()
print(c)
