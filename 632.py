w, h, n, *a = map(int, open(0).read().split())
a = [min(max(v, 0), [w, h][i % 2]) for i, v in enumerate(a)]
x = sorted({0, w, *a[::2]})
y = sorted({0, h, *a[1::2]})
X = len(x) - 1
Y = len(y) - 1
B = set()
for p, q, r, t in zip(*[iter(a)] * 4):
    if p == r:
        B |= {(x.index(p), j, 0) for j in range(Y) if min(q, t) <= y[j] and y[j + 1] <= max(q, t)}
    if q == t:
        B |= {(i, y.index(q), 1) for i in range(X) if min(p, r) <= x[i] and x[i + 1] <= max(p, r)}
u = set()
o = []
for i in range(X):
    for j in range(Y):
        if (i, j) in u:
            continue
        u.add((i, j))
        k = [(i, j)]
        s = 0
        while k:
            c, d = k.pop()
            s += (x[c + 1] - x[c]) * (y[d + 1] - y[d])
            for e, f, g in (c - 1, d, (c, d, 0)), (c + 1, d, (c + 1, d, 0)), (c, d - 1, (c, d, 1)), (c, d + 1, (c, d + 1, 1)):
                if -1 < e < X and -1 < f < Y and g not in B and (e, f) not in u:
                    u.add((e, f))
                    k.append((e, f))
        o.append(s)
print(*sorted(o)[::-1], sep="\n")
