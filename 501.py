n, *a = map(int, open(0).read().split())
r = [(min(a[i], a[i + 2]), min(a[i + 1], a[i + 3]), max(a[i], a[i + 2]), max(a[i + 1], a[i + 3])) for i in range(0, len(a), 4)]
x, y, u, v = r.pop()
print(sum(max(0, min(c, u) - max(a, x)) * max(0, min(d, v) - max(b, y)) for a, b, c, d in r))
