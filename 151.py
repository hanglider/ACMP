n, m, *a = map(int, open(0).read().split())
p = [*zip(a[::2], a[1::2])]
c = {}
for s in range(1, n + 1):
    q = [s] * (s not in c)
    c[s] = c.get(s, 0)
    for u in q:
        for x, y in p:
            v = x + y - u
            if u in (x, y) and v not in c:
                c[v] = 1 - c[u]
                q += [v]
print("YNEOS"[any(c[x] == c[y] for x, y in p)::2])
