n, *a = map(int, open(0).read().split())
g = [[]]
for x in a:
    if x:
        g[-1].append(x)
    else:
        g.append([])
q = [1]
for v in q:
    q += g[v - 1]
c = [0] * (n + 1)
for v in q[::-1]:
    g[v - 1].sort(key=lambda u: c[u])
    g[v - 1] = g[v - 1][:len(g[v - 1]) + 1 >> 1]
    c[v] = 1 + sum(c[u] for u in g[v - 1])
q = [1]
for v in q:
    q += g[v - 1]
print(len(q))
print(*q[::-1], sep='\n')
