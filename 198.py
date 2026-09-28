n, *d = map(int, open(0).read().split())
a = [d[i * (n + 1):(i + 1) * (n + 1)] for i in range(n)]
for i in range(n):
    a[i:] = sorted(a[i:], key=lambda r: -abs(r[i]))
    p = [x / a[i][i] for x in a[i]]
    a = [[x - r[i] * y for x, y in zip(r, p)] if j - i else p for j, r in enumerate(a)]
print(*[round(r[n]) for r in a])
