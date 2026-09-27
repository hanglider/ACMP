from heapq import *
n, a, z, r, *s = map(int, open(0).read().split())
g = [[] for _ in range(n + 1)]
for i in range(0, 4 * r, 4):
    g[s[i]] += [s[i + 1:i + 4]]
d = {a: 0}
h = [(0, a)]
while h:
    w, u = heappop(h)
    if w == d[u]:
        for t, b, e in g[u]:
            if t >= w and e < d.get(b, 1e9):
                d[b] = e
                heappush(h, (e, b))
print(d.get(z, -1))
