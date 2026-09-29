n, *a = map(int, open(0).read().split())
p = sorted(zip(a[::2], a[1::2]))
s = 0
for l in p, p[::-1]:
    h = []
    for q in l:
        while len(h) > 1 and (h[-1][0] - h[-2][0]) * (q[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (q[0] - h[-2][0]) <= 0:
            h.pop()
        h += [q]
    s += sum(abs(complex(*x) - complex(*y)) for x, y in zip(h, h[1:]))
print("%.1f" % s)
