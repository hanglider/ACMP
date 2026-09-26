from itertools import *
from bisect import bisect_left as B
from operator import sub
t = [*map(int, open('input.txt').read().split())]
z = [complex(t[i], t[i + 1]) for i in range(4, len(t), 2)]
T = []
for L, x, y in {*permutations(t[1:4])}:
    u = (L * L + x * x - y * y) / 2 / L
    H = (x * x - u * u)**.5
    T.append((L, u / H, (L - u) / H))
r = 1
for i in z:
    for j in z:
        D = abs(j - i)
        if D and r < len(z):
            Q = [(p - i) * D / (j - i) for p in z]
            Q = [(q.real, q.imag) for q in Q if q.imag > -1e-7]
            for L, f, g in T:
                if D < L + 1e-7:
                    a, b = zip(*[(s - L + d * g, s - d * f + 1e-7) for s, d in Q if d * (f + g) < L + 1e-7])
                    r = max(r, *map(sub, count(1), map(B, repeat(sorted(b)), sorted(a))))
print(r)