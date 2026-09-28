n, *m = open(0).read().split()
b = {(c, r): 'wb'[r > 3] for c in range(8) for r in range(8) if (c + r) % 2 < 1 and r - 3 & 6}
for s in m:
    p = [(ord(x) - 97, int(y) - 1) for x, y in zip(s[::3], s[1::3])]
    for (x, y), (u, v) in zip(p, p[1:]):
        k = b.pop((x, y))
        for t in range(1, abs(u - x)):
            b.pop((x + t * (u > x or -1), y + t * (v > y or -1)), 0)
        b[u, v] = k.upper() if v == 7 * (k in 'wW') else k
for r in range(7, -1, -1):
    print(''.join(b.get((c, r), '-.'[(c + r) % 2]) for c in range(8)))
