from heapq import *
n, m, *a = map(int, open(0).read().split())
d = {0: a[0]}
h = [(a[0], 0)]
while h:
    c, v = heappop(h)
    if c > d[v]:
        continue
    for u in v - m, v + m, v - 1 if v % m else -1, v + 1 if (v + 1) % m else -1:
        if 0 <= u < n * m and c + a[u] < d.get(u, 1e9):
            d[u] = c + a[u]
            heappush(h, (d[u], u))
print(d[n * m - 1])
