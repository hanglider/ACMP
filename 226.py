n, e, *t = open(0).read().split()
n = int(n)
g = [[] for _ in range(n + 1)]
q = []
for i in range(0, len(t), 3):
    a, b = int(t[i]), int(t[i + 1])
    c = round(float(t[i + 2]) * 1000) * (1 - 2 * (b < a))
    g[a] += [(b, c)]
    g[b] += [(a, -c)]
    q += [(a, b, c)]
p = [None] * (n + 1)
p[1] = 0
s = [1]
for a in s:
    for b, c in g[a]:
        if p[b] is None:
            p[b] = p[a] + c
            s += [b]
if None in p[1:] or any(p[b] - p[a] != c for a, b, c in q) or any(p[i] > p[i + 1] for i in range(1, n)):
    print("NO")
else:
    print("YES")
    print(*["%.3f" % ((p[i + 1] - p[i]) / 1000) for i in range(1, n)])
