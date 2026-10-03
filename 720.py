from math import *
from fractions import *
r, l = input().split()
q = int(Fraction(r)**2 / int(l)**2)
print(4 * sum(isqrt(q - i * i) for i in range(1, isqrt(q) + 1)))
