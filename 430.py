from math import *
r, *p = map(float, open(0).read().split())
a, b, c, d = map(radians, p)
h = sin((c - a) / 2)**2 + cos(a) * cos(c) * sin((d - b) / 2)**2
print('%.2f' % (2 * r * asin(min(1, sqrt(h)))))
