t = open(0).read().lower().split()
n, k, m = int(t[0]), int(t[2]), int(t[3])
d = float(t[1])
a = t[4:]
o = {a[2 * i]: float(a[2 * i + 1]) for i in range(n, n + k)}
w = {a[2 * i]: float(a[2 * i + 1]) for i in range(n + k, n + k + m)}
r = [0] * n
for i in sorted(range(n), key=lambda i: w.get(a[2 * i], 1e18) / o[a[2 * i]]):
    p = o[a[2 * i]]
    if w.get(a[2 * i], p) < p:
        r[i] = min(float(a[2 * i + 1]), d / p)
        d -= r[i] * p
for x in r:
    print('%.4f' % x)
