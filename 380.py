n, *t = map(int, open(0).read().split())
r = []
for i in range(n):
    a, b, c, d = t[4 * i:4 * i + 4]
    r += [sorted((a, c)) + sorted((b + 10**4, d + 10**4))]
x = sorted({*t[::2]})
s = 0
for p, q in zip(x, x[1:]):
    m = 0
    for a, c, b, d in r:
        if a <= p and q <= c:
            m |= (1 << d) - (1 << b)
    s += (q - p) * bin(m).count("1")
print(s)
