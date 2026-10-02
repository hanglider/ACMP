import re
d = {'m': 1, 'km': 1000, 'mile': 1609, 'uin': 33, 'kairi': 1852, 'zhang': 3, 'sen': 38}
l = sorted((int(a) * d[b], i) for i, (a, b) in enumerate(re.findall(r'(\d+)\s*([a-z]+)', open(0).read()), 1))
p, *t = max(((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c), i, j, k) for (a, i), (b, j), (c, k) in zip(l, l[1:], l[2:]))
print(p**.5 / 16)
print(*t)
