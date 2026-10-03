from math import *
n, a, *v = map(int, open(0).read().split())
t = tan(radians(a))
p = {(v[i + j], v[i + k], v[i + 4] * t) for i in range(0, 5 * n, 5) for j in (0, 2) for k in (1, 3)}
q = (sqrt(5) - 1) / 2
e = lambda x, y: max([c + hypot(x - a, y - b) for a, b, c in p])
def g(f, l, r):
    c = r - q * (r - l)
    d = l + q * (r - l)
    u = f(c)
    w = f(d)
    for _ in range(36):
        if u < w:
            r, d, w = d, c, u
            c = r - q * (r - l)
            u = f(c)
        else:
            l, c, u = c, d, w
            d = l + q * (r - l)
            w = f(d)
    return min((u, c), (w, d))
x = g(lambda x: g(lambda y: e(x, y), 0, 1000)[0], 0, 1000)[1]
y = g(lambda y: e(x, y), 0, 1000)[1]
s = 1e9
for i in range(0, 5 * n, 5):
    a, b, c, d, h = v[i:i + 5]
    r = min(g(lambda z: e(z, b), a, c), g(lambda z: e(z, d), a, c), g(lambda z: e(a, z), b, d), g(lambda z: e(c, z), b, d))[0]
    if a <= x <= c and b <= y <= d:
        r = min(r, e(x, y))
    s = min(s, r / t - h)
print(s)
