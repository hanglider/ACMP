n, m, *g = open(0).read().split()
S = [(a, b) for a in range(3) for b in range(3) if g[a][b] > '.']


def f(m, n, v):
    if v % 2:
        m, n = n, m
    P = sorted(((a, 2 - a)[v >> 1 & 1], (b, 2 - b)[v >> 2])[::1 - v % 2 * 2] for a, b in S)
    x, y = P[0]
    d = {0: 0}
    t = 0
    for i in range(-2, m):
        for j in range(-2, n):
            p = 0
            for a, b in P:
                if -1 < i + a < m and -1 < j + b < n:
                    p |= 1 << (i + a) * n + j + b
            e = dict(d)
            for s in d:
                k = s | p
                if e.get(k, 99) > d[s] + 1:
                    e[k] = d[s] + 1
            d = e
            t += len(d)
            if -1 < i + x < m and -1 < j + y < n:
                k = 1 << (i + x) * n + j + y
                d = {s ^ k: d[s] for s in d if s & k}
    return t, d[0]


print(f(int(m), int(n), min(range(8), key=lambda v: f(6, 6, v)))[1])
