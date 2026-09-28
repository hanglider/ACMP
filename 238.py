n, m, a, b, *d = map(int, open(0).read().split())
k = n * m
g = {(i // m + 1, i % m + 1) for i in range(k) if d[i] < 1}
h = k + 1 + 4 * d[k]
t = {(x, y): (u, v) for x, y, u, v in zip(*[iter(d[k + 1:h])] * 4)}
e = d[h + 1:]
e = set(zip(e[::2], e[1::2]))
q = [(a, b)]
r = {(a, b): 1}
for p in q:
    if p in e:
        print(r[p])
        exit()
    x, y = p
    for c in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), t.get(p):
        if c in g and c not in r:
            r[c] = r[p] + 1
            q.append(c)
print("Impossible")
