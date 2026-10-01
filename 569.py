n, d, *a = (int(x) for l in open(0) for x in l.split())
r = [0] * n
u = (i for i in range(n) if a[i] > d)
j = next(u, 0)
for i in range(n):
    g = d - a[i]
    while g > 0:
        r[i] = (j + 1 << 30) + g
        a[j] -= g
        g = d - a[j]
        if g >= 0:
            a[j] = d
            i = j
            j = next(u, 0)
for x in r:
    print(*divmod(x, 1 << 30))
