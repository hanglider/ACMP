n, *a = map(int, open(0).read().split())
a.sort()
x, y = 0, 1e9
for p, q in zip(a, a[1:]):
    x, y = y, min(x, y) + q - p
print(y)
