from math import gcd
from random import randrange as R
n = int(input())
c = {}


def q(x):
    t = ((x - 1) & (1 - x)).bit_length() - 1
    for a in 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37:
        y = pow(a, x - 1 >> t, x)
        if y != 1 and all(pow(y, 2**i, x) != x - 1 for i in range(t)):
            return 0
    return 1


def r(x):
    while 1:
        k = R(1, x)
        a = b = R(2, x)
        d = 1
        while d == 1:
            a = (a * a + k) % x
            b = (b * b + k) % x
            b = (b * b + k) % x
            d = gcd(a - b, x)
        if d < x:
            return d


for p in range(2, 10**4):
    while n % p < 1:
        n //= p
        c[p] = c.get(p, 0) + 1
s = [n]
while s:
    x = s.pop()
    if x > 1:
        if q(x):
            c[x] = c.get(x, 0) + 1
        else:
            d = r(x)
            s += [d, x // d]
a = 1
for p in c:
    a *= p**(c[p] - 1) * ((c[p] + 1) * p - c[p])
print(a)
