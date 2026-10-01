n, a, b, c, d, *t = map(int, open(0).read().split())
c -= a
d -= b
s = [k for k, (x, y, r) in enumerate(zip(*[iter(t)] * 3), 1) if (c * (y - b) - d * (x - a))**2 <= r * r * (c * c + d * d)]
print(len(s))
print(*s)
