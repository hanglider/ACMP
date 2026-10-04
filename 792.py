a, p, b, q = map(int, open(0).read().split())
s = t = 0
while a:
    s += a % p
    a //= p
while b:
    t += b % q
    b //= q
print(s * (s == t))
