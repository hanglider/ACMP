s = [*map(int, open(0).read().split())]
p = sorted(set(zip(s[1::2], s[2::2])))
h = []
for r in p, p[::-1]:
    t = []
    for x, y in r:
        while len(t) > 1 and (t[-1][0] - t[-2][0]) * (y - t[-2][1]) <= (t[-1][1] - t[-2][1]) * (x - t[-2][0]):
            t.pop()
        t += [(x, y)]
    h += t
print((sum(a * d - b * c for (a, b), (c, d) in zip(h, h[1:])) + 1) // 2)
