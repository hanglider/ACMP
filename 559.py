from math import acos, pi
d, r, n = map(float, open(0).read().split())
l = d + 2 * r
g = lambda x: r * r * acos(1 - x / r) - (r - x) * (2 * r * x - x * x)**0.5
f = lambda x: g(x) if x < r else pi * r * r / 2 + 2 * r * (x - r) if x < r + d else pi * r * r + 2 * r * d - g(l - x)
for i in range(1, int(n)):
    t = (pi * r * r + 2 * r * d) * i / n
    a = 0
    b = l
    for _ in range(60):
        m = (a + b) / 2
        if f(m) < t:
            a = m
        else:
            b = m
    print("%.6f" % a)
