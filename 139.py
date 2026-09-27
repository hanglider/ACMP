n, m, *a = map(int, open(0).read().split())
g = [[] for _ in range(n + 1)]
r = [[] for _ in range(n + 1)]
for i in range(0, 3 * m, 3):
    u, v, w = a[i:i + 3]
    g[u] += [(v, w)]
    r[v] += [(u, w)]
def f(s, g):
    q = [s]
    t = {s}
    for u in q:
        for v, w in g[u]:
            if v not in t:
                t.add(v)
                q += [v]
    return t
s = f(1, g) & f(n, r)
d = {1: 0}
e = {}
p = {1}
q = [1] * (n in s)
k = 0
for u in q:
    p.discard(u)
    for v, w in g[u]:
        if v in s and d[u] + w > d.get(v, -1e18):
            d[v] = d[u] + w
            e[v] = u
            k += 1
            if k % len(s) < 1:
                t = {}
                for x in e:
                    y = x
                    while y in e and y not in t:
                        t[y] = x
                        y = e[y]
                    if t.get(y) == x:
                        exit(print(":)"))
            if v not in p:
                p.add(v)
                q += [v]
print(d.get(n, ":("))
