from math import gcd
a, b, c, d, e, f = map(int, input().split())
r = []
for a, b, c in (a, b, c), (d, e, f):
    g = gcd(a, c)
    m = c // g
    r += [b % g < 1, b // g * pow(a // g, -1, m) % m, m]
print(["NO", "YES"][r[0] and r[3] and (r[1] - r[4]) % gcd(r[2], r[5]) < 1])
