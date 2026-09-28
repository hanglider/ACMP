n, *a = map(int, open(0).read().split())
a.sort()
d = [0, 2e9]
for i in range(2, n + 1):
    d += [min(max(d[i - k], a[i - 1] - a[i - k]) for k in (2, 3) if k <= i)]
print(d[n])
