from math import gcd
a, b, c, d, e, f = map(int, open(0).read().split())
g = [gcd(c - a, d - b), gcd(e - c, f - d), gcd(a - e, b - f)]
print(sum(g) if (c - a) * (f - b) - (d - b) * (e - a) else max(g) + 1)
