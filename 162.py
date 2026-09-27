n, m = map(int, input().split())
p = [(x, 0) for x in range(1, m)] + [(m, y) for y in range(1, n)] + [(x, n) for x in range(m - 1, 0, -1)] + [(0, y) for y in range(n - 1, 0, -1)]
g = [abs(a - c) + abs(b - d) for (a, b), (c, d) in zip(p, p[1:] + p[:1])]
print((n + 1) * m + (m + 1) * n + min(sum(g[::2]), sum(g[1::2])))
