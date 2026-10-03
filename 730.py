from itertools import product
n, m, *a = map(int, open(0).read().split())
e = [[] for _ in range(n + 1)]
for i in range(m):
    e[a[3 * i + 1]] += [i]
r = []
for p in product(*e[2:]):
    s = {1}
    for _ in p:
        s |= {a[3 * i + 1] for i in p if a[3 * i] in s}
    if len(s) == n:
        r += [(sum(a[3 * i + 2] for i in p), sorted(i + 1 for i in p))]
c, p = min(r)
print(c, len(p))
print(*p)
