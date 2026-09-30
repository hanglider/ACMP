from math import *
from cmath import phase
a, b, c, d, x, y, r = map(float, open(0).read().split())
p = complex(a - x, b - y)
q = complex(c - x, d - y)
u = abs(p)
v = abs(q)
t = abs(phase(q / p)) - acos(min(r / u, 1)) - acos(min(r / v, 1))
print(t > 0 and sqrt(abs(u * u - r * r)) + sqrt(abs(v * v - r * r)) + r * t or abs(p - q))
