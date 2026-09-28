from math import *
n, *a = [round(float(x) * 100) for x in open(0).read().split()]
c = [a[i:i + 3] for i in range(0, len(a), 3)]
t = 2 * pi
r = 'YES'
for x, y, p in c:
    e = [(t, 0)]
    s = 0
    for u, v, q in c:
        d = (u - x)**2 + (v - y)**2
        if d:
            f = atan2(v - y, u - x)
            for z, k in (p - q, 1), (p + q, 1000):
                w = atan2(sqrt(d - z * z), z)
                g = (f - w) % t
                h = g + 2 * w
                b = h > t
                s += k * b
                e += (g, k), (h - b * t, -k)
    o = 0
    for g, k in sorted(e):
        if g - o > 1e-13 and s % 1000 == s // 1000 > 0:
            r = 'NO'
        s += k
        o = g
print(r)
