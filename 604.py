n, *e = map(int, open(0).read().split())
g = [[] for _ in range(n + 1)]
for i in range(0, len(e), 2):
    g[e[i]].append(e[i + 1])
    g[e[i + 1]].append(e[i])
o = [1]
p = [0] * (n + 1)
for v in o:
    for u in g[v]:
        if u != p[v]:
            p[u] = v
            o.append(u)
r = [0] * (n + 1)
for v in o[::-1]:
    a, b, c, d = 1, 0, 0, 0
    for u in g[v]:
        if u != p[v]:
            x, y, z = r[u]
            a, b, c, d = a * x, b * x + a * y, c * x + a * z, d * x + (b + c) * (y + z)
    r[v] = a + c + d, a, b + c
print(r[1][0])
