from itertools import product
a = open(0).read().split()
n = int(a[0])
m = n - 1
t = range(n)
s = set(product(t, t, t))
R = [(a[1 + 6 * r + v][c], [[(c, k, r), (k, m - c, r), (m - c, m - k, r), (m - k, c, r), (c, m - r, k), (c, r, m - k)][v] for k in t]) for v in range(6) for r in t for c in t]
for h, l in R:
    if h == '.':
        s -= set(l)
w = 1
while w:
    w = 0
    d = {}
    for h, l in R:
        q = next((q for q in l if q in s), 0)
        if q and d.setdefault(q, h) != h:
            s -= {q}
            w = 1
print(len(s))
