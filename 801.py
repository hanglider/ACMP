from random import shuffle
from operator import mul
def p(a, b):
    return sum(map(mul, a, b))
def f(A, o, E):
    d = len(E)
    c = [e[2] for e in E]
    if d < 2:
        l, h = -1e10, 1e10
        for g in A:
            q = p(g, E[0])
            r = (g[3] - p(g, o)) / (q or 1)
            if q > 1e-12:
                h = min(h, r)
            if q < -1e-12:
                l = max(l, r)
        u = l if c[0] > 1e-12 else h if c[0] < -1e-12 else min(max(0, l), h)
        return [x + u * y for x, y in zip(o, E[0])]
    v = [0 if abs(q) < 1e-12 else -1e10 if q > 0 else 1e10 for q in c]
    z = [o[j] + p(v, [e[j] for e in E]) for j in range(3)]
    for i in range(len(A)):
        g = A[i]
        if p(g, z) > g[3] + 1e-9:
            a = [p(g, e) for e in E]
            b = (g[3] - p(g, o)) / p(a, a)
            F = []
            for k in range(d):
                e = [1.0 * (j == k) for j in range(d)]
                for w in [a] + F:
                    s = p(e, w) / p(w, w)
                    e = [x - s * y for x, y in zip(e, w)]
                m = p(e, e)
                if m > 1e-6 and len(F) < d - 1:
                    F.append([x / m**.5 for x in e])
            z = f(A[:i], [o[j] + b * p(a, [e[j] for e in E]) for j in range(3)], [[p(w, [e[j] for e in E]) for j in range(3)] for w in F])
    return z
C = [(1, 0, 0, 1e9), (-1, 0, 0, 1e9), (0, 1, 0, 1e9), (0, -1, 0, 1e9), (0, 0, 1, 1e9), (0, 0, -1, 1e9)]
D = []
for i in range(int(input())):
    x, y, X, Y = map(int, input().split())
    a = Y - y
    b = x - X
    m = (a * a + b * b)**.5
    c = (a * x + b * y) / m
    a /= m
    b /= m
    D += [(a, b, -1, c), (-a, -b, -1, -c)]
shuffle(D)
print(*f(C + D, [0, 0, 0], [[1, 0, 0], [0, 1, 0], [0, 0, 1]])[:2])
