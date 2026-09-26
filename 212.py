t = [*map(int, open('input.txt').read().split())]
n, p = t[0], t[1]
g = [[] for _ in range(n + 1)]
for i in range(2, len(t) - 1, 2):
    g[t[i]].append(t[i + 1])
    g[t[i + 1]].append(t[i])
q = [1]
for u in q:
    for v in g[u]:
        g[v].remove(u)
        q.append(v)
I = 999
d = {}
r = I
for u in q[::-1]:
    a = [I, 0]
    for v in g[u]:
        c = [I] * (len(a) + len(d[v]))
        for i, x in enumerate(a):
            c[i] = min(c[i], x + 1)
            for j, y in enumerate(d[v]):
                c[i + j] = min(c[i + j], x + y)
        a = c
    d[u] = a
    if p < len(a):
        r = min(r, a[p] + (u > 1))
print(r)