from heapq import *
n, *a = map(int, open(0).read().split())
P = list(map(complex, a[::2], a[1::2]))
e = []
for i in range(n):
    d = list(map(abs, map(P[i].__sub__, P)))
    e += [(d[j], i, j) for j in nsmallest(19, range(n), key=d.__getitem__)[1:]]
k = list(range(n))
g = [[i] for i in k]
c = [1] * n
for r, u, v in sorted(e):
    if k[u] == k[v]:
        if c[u] == c[v]:
            break
        continue
    t = c[u] == c[v]
    if len(g[k[u]]) < len(g[k[v]]):
        u, v = v, u
    b = g[k[v]]
    for x in b:
        k[x] = k[u]
        c[x] ^= t * 3
    g[k[u]] += b
print(r / 2)
print(*c)
