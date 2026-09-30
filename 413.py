p = c = 0
for r in open(0).read().split()[2:]:
    x = int(r.translate({46: 48, 35: 49}), 2)
    c += bin(x & ~(p | x >> 1)).count('1')
    p = x
print(c)
