from math import hypot as h
n, *a = map(int, open(0).read().split())
x = a[::2]
y = a[1::2]
l, r = sorted(x[:2])
for i in [0] * 30:
    m = (l + r) / 2
    if sum((m - u) / (h(m - u, v) or 1) for u, v in zip(x, y)) < 0:
        l = m
    else:
        r = m
print(l)
