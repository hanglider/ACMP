n, m, *a = map(int, open(0).read().split())
g = [a[i:i + m] for i in range(0, n * m, m)]
l = sum(x != y for r in g + [*zip(*g)] for x, y in zip(r, r[1:]))
v = sum(len({*r[j:j + 2], *s[j:j + 2]}) > 1 for r, s in zip(g, g[1:]) for j in range(m - 1))
print((48 * l + 12 * v) / 100)
