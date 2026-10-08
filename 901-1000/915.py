n, m, *a = map(int, open(0).read().split())
d = [(0, 0, 0)] + [(-10**9,) * 3] * m
for i in range(n * m):
    j = i % m
    x = a[i]
    u, v, w = map(max, d[j], d[j - 1])
    d[j] = (max(6 * x, x) + max(v, w), max(5 * x, 2 * x) + max(u, w), max(4 * x, 3 * x) + max(u, v))
print(max(d[m - 1]))
