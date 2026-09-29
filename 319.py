from math import gcd
a, b, c, d = map(int, open(0).read().split())
print(gcd(a - c, b - d) + 1)
