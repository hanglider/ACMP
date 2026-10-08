a = [*map(int, open(0).read().split())]
v = [a[i:i + 3] for i in range(0, 24, 3)]
d = lambda u, w: sum(map(int.__mul__, u, w))
f = lambda k, x: [d(v[k], x) + sum(g(0, d(w, x)) for w in v[k + 1:k + 4]) for g in (min, max)]
s = 0
for u in v[1:4] + v[5:]:
    for w in v[1:4] + v[5:]:
        x = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
        p, q = f(0, x)
        r, t = f(4, x)
        s |= q < r or t < p
print("YNEOS"[s::2])
