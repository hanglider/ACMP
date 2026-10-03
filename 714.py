from fractions import Fraction as F
p = list(zip(*[iter(map(int, open(0).read().split()))] * 2))
l = lambda i, j: (2 * (p[j][0] - p[i][0]), 2 * (p[j][1] - p[i][1]), p[j][0]**2 + p[j][1]**2 - p[i][0]**2 - p[i][1]**2)
g = lambda c, i: (c[0] - p[i][0])**2 + (c[1] - p[i][1])**2
n = 0
z = 0
m = (1e9,)
for a, b, c, d, v in (1, 2, 1, 3, 0), (0, 2, 0, 3, 1), (0, 1, 0, 3, 2), (0, 1, 0, 2, 3), (0, 1, 2, 3, 2), (0, 2, 1, 3, 1), (0, 3, 1, 2, 1):
    e, f, h = l(a, b)
    q, r, s = l(c, d)
    k = e * r - q * f
    if k:
        o = (F(h * r - s * f, k), F(e * s - q * h, k))
        if g(o, a) == g(o, v):
            z = 1
            m = 0, *map(float, o)
        else:
            n += 1
            m = min(m, ((g(o, a)**0.5 + g(o, v)**0.5) / 2, *map(float, o)))
    elif e * s == q * h and f * s == r * h:
        z = 1
        w = max((g(p[a], i), i) for i in (c, d))[1]
        u = e * p[a][0] + f * p[a][1] - h
        t = u / (u - e * p[w][0] - f * p[w][1] + h)
        o = (p[a][0] + (p[w][0] - p[a][0]) * t, p[a][1] + (p[w][1] - p[a][1]) * t)
        m = min(m, (g(p[a], w)**0.5 / 2, *o))
print(z and 'Infinity' or n)
print(*m[1:], m[0])
