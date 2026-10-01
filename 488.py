from fractions import Fraction as F
r, k, *a = map(F, open(0).read().split())
l = [a[i:i + 4] for i in range(0, len(a), 4)]
s = k + 1
for i in range(len(l)):
    for j in range(i):
        p, q, u, v = l[i]
        c, d, e, f = l[j]
        t = ((c - p) * (f - d) - (d - q) * (e - c)) / ((u - p) * (f - d) - (v - q) * (e - c))
        s += (p + t * (u - p))**2 + (q + t * (v - q))**2 < r * r
print(s)
