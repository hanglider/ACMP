from heapq import *
d = open(0).read().split()
m, n, k = int(d[0]), int(d[1]), int(d[2])
a = list(map(int, d[3:]))
N = m * n
L = []
for i in range(m):
    for j in range(n):
        u = i * n + j
        if (i + j) % 2 < 1:
            for v in [u - n] * (i > 0) + [u + n] * (i < m - 1) + [u - 1] * (j > 0) + [u + 1] * (j < n - 1):
                L.append((-a[u] * a[v], u, v))
L.sort()
I = 10**18
g = [[] for _ in range(N)]
Z = [I] * N
for w, u, v in L[:7 * k - 6]:
    g[u].append((v, w))
    g[v].append((u, w))
    Z[u] = 0
W = [v for v in range(N) if g[v] and Z[v]]
M = [-1] * N
h = [0] * N
B = [(I, -1)] * N
def b(v):
    B[v] = min([(w, u) for u, w in g[v] if Z[u] < 1] + [(I, -1)])
for v in W:
    b(v)
    h[v] = B[v][0]
H = min(h)
r = 0
for _ in range(k):
    D = Z[:]
    P = {}
    q = []
    for v in W:
        x = B[v][0]
        if x < I:
            x -= h[v]
            D[v] = x
            P[v] = B[v][1]
            q.append((x + h[v] - H << 12 | v + 2048) if M[v] < 0 else x << 12 | v)
    heapify(q)
    while q:
        x, v = divmod(heappop(q), 4096)
        if v > 2047:
            v -= 2048
            break
        if x > D[v]:
            continue
        u = M[v]
        x += h[v] + a[u] * a[v] - h[u]
        D[u] = x
        x += h[u]
        for y, w in g[u]:
            z = x + w - h[y]
            if z < D[y] and y != v:
                D[y] = z
                P[y] = u
                heappush(q, (z + h[y] - H << 12 | y + 2048) if M[y] < 0 else z << 12 | y)
    h = [i + min(j, x) for i, j in zip(h, D)]
    H += x
    while 1:
        u = P[v]
        r += a[u] * a[v]
        y = M[u]
        M[u] = v
        M[v] = u
        if y < 0:
            break
        r -= a[u] * a[y]
        v = y
    Z[u] = I
    for v, w in g[u]:
        b(v)
print(r)
