k, n, m, *a = map(int, open(0).read().split())
g = {r + c * 1j: a[r * m + c] for r in range(n) for c in range(m)}
s = [(p, d, 0) for p in g for d in (1, -1, 1j, -1j) if g[p] == 2]
v = set(s)
t = 0
while s:
    if any(g[p] == 3 for p, d, r in s):
        break
    q = []
    for p, d, r in s:
        for e, x in (d, 0), (d * 1j, 0), (d * -1j, 1):
            y = (p + e, e, r + x)
            if g.get(p + e, 1) != 1 and r + x <= k and y not in v:
                v.add(y)
                q.append(y)
    s = q
    t += 1
print(t if s else -1)
