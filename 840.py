from fractions import Fraction as F
from itertools import product, chain
t = open(0).read().split()
d = 10**max(len(s) - s.find(".") - 1 if "." in s else 0 for s in t)
t = [int(F(s) * d) for s in t]
b = [t[:4]] + [t[i:i + 4] for i in range(5, len(t), 4)]
c = lambda x, y, z, r: [range((v - r) >> k, ((v + r) >> k) + 1) for v in (x, y, z)]
n = lambda u: min(len(u[0]) * len(u[1]) * len(u[2]), 513)
k = (9 * 10**4 * d).bit_length()
while k and sum(n(c(*a)) for a in b) < 5 * 10**4:
    k -= 1
k += 1
g = {}
o = []
s = set()
for i, (x, y, z, r) in enumerate(b):
    h = set()
    u = c(x, y, z, r)
    m = n(u) > 512
    u = [] if m else list(product(*u))
    for j in range(i) if m else set(chain(o, *filter(None, map(g.get, u)))):
        p, q, w, e = b[j]
        if (x - p)**2 + (y - q)**2 + (z - w)**2 < (r + e)**2:
            h.add(j)
    if h:
        s -= h
    else:
        s.add(i)
    if i and not s:
        print(i)
        exit()
    o += [i] * m
    for a in u:
        g.setdefault(a, []).append(i)
print(0)
