n, *t = map(float, open(0).read().split())
r = 100
d = e = 0
for a, b in zip(t[::2], t[1::2]):
    r = max(r, d * a, e * b)
    d, e = r / a, r / b
print("%.2f" % r)
