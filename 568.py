n, m, *e = map(int, open(0).read().split())
g = [[] for _ in range(n + 1)]
for a, b in zip(e[::2], e[1::2]):
    g[a].append(b)
    g[b].append(a)
s = [1]
r = []
while s:
    v = s[-1]
    if g[v]:
        s.append(g[v].pop())
    else:
        r.append(s.pop())
print(2 * m)
print(*r)
