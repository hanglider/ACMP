r = open(0).read().split()
a = j = 0
p = [(0, 0)]
e = []
for d in r[1:]:
    x = (d in "12") - (d in "45")
    y = (d in "56") - (d in "23")
    if y:
        e += [(min(j, j + y), a + a + x)]
    a += x
    j += y
    p += [(a, j)]
m = min(p)[0]
h = min(y for x, y in p)
W = max(p)[0] - m + 2
U = D = 0
e.sort()
for (i, x), (k, y) in zip(e[::2], e[1::2]):
    x -= 2 * m
    y -= 2 * m
    k = (i - h) * W
    U |= (1 << (y + 1) // 2) - (1 << (x + 1) // 2) << k
    D |= (1 << y // 2) - (1 << x // 2) << k
V = U & D << W
E = D & U >> W
s = 0
t = U
while t:
    s += t.bit_count()
    t = V & (t & t >> 1) << W
t = D
while t:
    s += t.bit_count()
    t = E & (t & t << 1) >> W
print(s)
