p, q, r, s = zip(*[map(int, open(0).read().split())] * 2)
f = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
print("YNeos"[not(f(p, q, r) * f(p, q, s) <= 0 >= f(r, s, p) * f(r, s, q) and min(p, q) <= max(r, s) and min(r, s) <= max(p, q))::2])
