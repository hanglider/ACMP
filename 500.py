n, *a = map(int, open(0).read().split())
c = [r for _, r in sorted(zip(a[::2], a[1::2]))]
x, y = 9e9, c[1]
for r in c[2:]:
    x, y = y, r + min(x, y)
print(y)
