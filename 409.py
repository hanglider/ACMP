n, *a = map(int, open(0).read().split())
print((sum(a) * 2 - a[0] - a[-1]) / (2 * n - 2))
