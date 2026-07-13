from itertools import combinations
d = list(map(int, open(0).read().split()))
n = d[0]
p = [(d[1 + 2 * i], d[2 + 2 * i]) for i in range(n)]
e = []
for i in range(n):
    a, b = p[i]
    c, f = p[(i + 1) % n]
    u = c - a
    v = f - b
    l = (u * u + v * v)**0.5
    e.append((-v / l, u / l, (u * b - v * a) / l))
D = lambda a, b, c: a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0])
w = 0
for i, j, k in combinations(range(n), 3):
    q = [e[i], e[j], e[k]]
    m = D(*[(t[0], t[1], -1) for t in q])
    if abs(m) < 1e-9:
        continue
    x = D(*[(t[2], t[1], -1) for t in q]) / m
    y = D(*[(t[0], t[2], -1) for t in q]) / m
    r = D(*q) / m
    if r > 1e-9 and all(abs(t[0] * x + t[1] * y - t[2] - r) < 1e-6 for t in e):
        w = 1
        break
if w:
    print("YES")
    print("%.3f %.3f %.3f" % (x, y, r))
else:
    print("NO")
