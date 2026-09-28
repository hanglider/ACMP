a = int(input())
r = 1
m = a
p = 2
while p * p <= m:
    if m % p < 1:
        r *= p
        while m % p < 1:
            m //= p
    p += 1
r *= m
n = r
while pow(n, n, a):
    n += r
print(n)
