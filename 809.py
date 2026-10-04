from collections import Counter
r = open(0).read().split()
n = int(r[0])
a = list(map(int, r[1:]))
g = {}
for i in range(2 * n):
    (x, y), (u, v) = sorted([a[4 * i:4 * i + 2], a[4 * i + 2:4 * i + 4]])
    g.setdefault((u - x, v - y), ([], []))[i >= n].append(x * 10**5 + y)
h = [(p, [[b for b in q if b % 17 == s] for s in range(17)]) for p, q in g.values()]
m = 0
for s in range(17):
    c = Counter()
    for p, q in h:
        for x in p:
            c.update(b - x for b in q[(x + s) % 17])
    m = max(m, *c.values(), 0)
print(n - m)
