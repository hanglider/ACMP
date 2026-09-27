from math import *
a, b, c, d, r, s = map(int, open(0).read().split())
h = min(hypot(a - c, b - d), 2 * r)
print(['NO', 'YES'][2 * pi * r * r - 2 * r * r * acos(h / 2 / r) + h * sqrt(4 * r * r - h * h) / 2 > s])