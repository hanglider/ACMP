t = open(0).read().split()
n, d = int(t[0]), int(t[1])
h = d // 2
g = [[] for _ in range(n + 1)]
for i in range(2, 2 * n, 2):
    a, b = int(t[i]), int(t[i + 1])
    g[a].append(b)
    g[b].append(a)
p = [0] * (n + 1)
q = [1]
for u in q:
    for v in g[u]:
        if v != p[u]:
            p[v] = u
            q.append(v)
H = [0] * (n + 1)
for u in q[:0:-1]:
    H[p[u]] = max(H[p[u]], H[u] + 1)
F = [0] * (n + 1)
W = [0] * (n + 1)
r = 0
for v in q[::-1]:
    c = [u for u in g[v] if u != p[v]]
    f = []
    w = []
    m = 0
    if c:
        m = max(c, key=H.__getitem__)
        f = F[m]
        w = W[m]
    f.append(1)
    w.append(0)
    L = len(f)
    e = f[-1 - h] if h < L else 0
    r += w[-1 - h] if h < L else 0
    o = 0
    for u in c:
        if u != m:
            a = F[u]
            b = W[u]
            k = len(a)
            x = a[-h] if h <= k else 0
            r += o * x
            o += e * x
            e += x
            for s in range(max(0, h - L), min(k, h)):
                j = h - s
                r += a[-1 - s] * w[-j] + b[-1 - s] * f[-j]
            for s in range(k):
                f[-2 - s] += a[-1 - s]
                w[-2 - s] += b[-1 - s]
    w[-1] += o
    F[v] = f
    W[v] = w
print(r * (d % 2 < 1))