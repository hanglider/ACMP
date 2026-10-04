a = list(map(int, open(0).read().split()))
p = [complex(a[i], a[i + 1]) for i in range(0, 12, 2)]
c = lambda a, b: (a.conjugate() * b).imag
r = []
for i, j, k, g in (0, 2, 3, 1), (1, 2, 3, 1), (2, 0, 1, -1), (3, 0, 1, -1):
    d = g * (p[4] - p[5])
    w = p[j] - p[i]
    e = p[k] - p[j]
    D = c(d, e)
    if D:
        t = c(w, e) / D
        s = c(w, d) / D
        if t >= 0 <= s <= 1:
            r += [t]
    elif d and c(w, d) == 0:
        r += [t for t in ((w / d).real, ((w + e) / d).real) if t >= 0]
print(min(r) if r else -1)
