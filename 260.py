from heapq import *
n, m, k, c, *a = map(int, open(0).read().split())
g = [[] for _ in range(n + 1)]
for i in range(k, k + 3 * m, 3):
    s, e, t = a[i:i + 3]
    g[s] += (t, e),
    g[e] += (t, s),
d = [1e9] * (n + 1)
d[c] = 0
q = [(0, c)]
while q:
    w, u = heappop(q)
    if w == d[u]:
        for t, v in g[u]:
            if w + t < d[v]:
                d[v] = w + t
                heappush(q, (w + t, v))
for w, u in sorted((d[u], u) for u in a[:k]):
    print(u, w)
