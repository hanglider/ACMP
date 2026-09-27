from heapq import *
n, *s = map(int, open(0).read().split())
g = [[] for _ in s]
for a, b in zip(s[n + 1::2], s[n + 2::2]):
    g[a] += [b]
    g[b] += [a]
h = [(0, 1)]
d = {}
while h:
    w, u = heappop(h)
    if u not in d:
        d[u] = w
        for v in g[u]:
            heappush(h, (w + s[u - 1], v))
print(d.get(n, -1))
