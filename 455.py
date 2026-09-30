from fractions import Fraction as F
s = input()
a, b = (s + '.').split('.')[:2]
b, c = (b + '(').split('(')[:2]
c = c.strip(')')
x = (F(int(a + b), 10**len(b)) + F(int(c or 0), (10**len(c) - 1 or 1) * 10**len(b))) * int(input())
p, q = x.numerator, x.denominator
u = q
for d in 2, 5:
    while u % d < 1:
        u //= d
k = 0
while 10**k % (q // u):
    k += 1
l = u > 1
while (10**l - 1) % u:
    l += 1
d = str(p % q * 10**(k + l) // q).zfill(k + l)
r = str(p // q)
if k + l:
    r += '.' + d[:k]
if l:
    r += '(' + d[k:] + ')'
print(r)
