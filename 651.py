from math import gcd
n, m = map(int, input().split())
g = gcd(n, m)
c = 0
for x in n // g, m // g:
    d = 2
    while d * d <= x:
        while x % d < 1:
            x //= d
            c += 1
        d += 1
    c += x > 1
print(c)
