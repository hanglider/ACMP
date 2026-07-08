from itertools import combinations_with_replacement as C
from collections import Counter
from math import factorial as F

N = int(input())
t = 0
b = None
for c in C(range(10), N):
    s = sum(c)
    p = 1
    for d in c:
        p *= d
    if s == p:
        k = Counter(c)
        dn = 1
        for v in k.values():
            dn *= F(v)
        tp = F(N) // dn
        if N == 1:
            v = tp
        else:
            if k[0] > 0:
                k2 = k.copy()
                k2[0] -= 1
                d2 = 1
                for x in k2.values():
                    if x > 0:
                        d2 *= F(x)
                lz = F(N - 1) // d2
                v = tp - lz
            else:
                v = tp
        if v > 0:
            t += v
            g = list(c)
            if N == 1:
                cd = g[0]
            else:
                nz = [x for x in g if x != 0]
                f = min(nz)
                r = g.copy()
                r.remove(f)
                r.sort()
                cd = int(str(f) + ''.join(map(str, r)))
            if b is None or cd < b:
                b = cd
print(t, b)
