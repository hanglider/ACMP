from math import *
a, b, x, y, r = map(float, open(0).read().split())
d = max(hypot(a - x, b - y), r, 1e-9)
print(pi * r * r + r * sqrt(d * d - r * r) - r * r * acos(r / d))
