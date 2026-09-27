from fractions import Fraction as F
n, c, *a = open(0).read().split()
n = int(n)
v = [set() for _ in range(1 << n)]
for i in range(n):
    v[1 << i] = {F(a[i])}
for m in range(1 << n):
    for s in range(1, m):
        if s & m == s:
            v[m] |= {f for x in v[s] for y in v[m ^ s] for f in (x + y, x * y / (x + y))}
print("YNEOS"[all(abs(x - F(c)) > F(1, 100) for w in v for x in w)::2])
