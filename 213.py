n, *a = map(int, open(0).read().split())
p = a[:n]
r = 0
for i in range(a[n + 1]):
    t = a[n + 2 + i * n:n + 2 + i * n + n]
    r = max(r, sum(x * y for x, y in zip(p, t)) + a[n] * all(t) - 2 * i)
    print(r)
