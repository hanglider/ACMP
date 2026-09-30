from math import comb
from collections import defaultdict
n, k = map(int, input().split())
l = n * k
M = [(2 << 2 * r) - 1 << l - r for r in range(l + 1)]
C = [[comb(a, i) for i in range(a + 1)] for a in range(n + 1)]
d = {(0, 1 << l): 1}
for c in range(k, 2, -1):
    e = defaultdict(int)
    for (m, b), w in d.items():
        f = n - m
        for x, y in zip(C[f], M[f * (c - 1)::1 - c]):
            t = b & y
            if t:
                e[m, t] += w * x
            b = b << c | b >> c
            m += 1
    d = e
q = int('0001' * l, 2)
p = defaultdict(int)
h = defaultdict(int)
for (m, b), w in d.items():
    u = b >> l
    p[n - m, (u & -u).bit_length()] += w
    h[n - m, (u & q & -(u & q) or 4 << l).bit_length(), (u & q * 4 & -(u & q * 4) or 4 << l).bit_length()] += w
r = range(n + 1 if k > 1 else 1)
s = sum(w * C[f][a] * C[f - a][b] for (f, z), w in p.items() for a in r for b in range(1, f - a + 1) if b % 2 != z % 2 and z <= 2 * a + b + 1)
s += sum(w * C[f][a] for (f, y, v), w in h.items() for a in r if a <= f and (v if a % 2 else y) <= 2 * a + 1)
print((k + 1)**n - s)
