n, k, *a = map(int, open(0).read().split())
b = a[:n]
c = a[n:2 * n - 1]
d = sum(map(abs, b)) - sum(map(abs, c))
print([d, -d][(b.count(-d) + c.count(-d) + a[2 * n - 1:].count(d)) % 2])
