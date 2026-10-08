from fractions import Fraction as F
n, m, *a = map(int, open(0).read().split())
l = a[1::3]
h = a[2::3]
print(min({m} | {s for s in l if s < m}, key=lambda s: (F(sum(a[::3]), s) + sum(y for x, y in zip(l, h) if x < s), -s)))
