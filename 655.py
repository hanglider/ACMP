from math import gcd
c = int(input())
k = int(input())
p = 10**k + 1
for m in range(1, 19):
    q = 10**m + 1
    g = gcd(p, q)
    s = p // g
    l = max(10**(k - 1), -(((10**m - 1) * p - c) // q))
    a = l + (c // g * pow(q // g, -1, s) - l) % s
    if c % g == 0 and a <= min(10**k - 1, c // q):
        print(a * 10**m + (c - a * q) // p)
        break
