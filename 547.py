from math import gcd
n = int(input())
k = 0
while gcd(n, 10) > 1:
    n //= gcd(n, 10)
    k += 1
p = 1
r = 10 % n
while r > 1:
    r = r * 10 % n
    p += 1
print(k, p)
