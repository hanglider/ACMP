from decimal import *
getcontext().prec = 60
def g(a, m, l, r):
    if l < 1:
        return 0
    a %= m
    k = -(-l // a)
    if a * k <= r:
        return k
    return -(-(m * g(m, a, -r % a, -l % a) + l) // a)
n = int(input())
M = 10**40
f = lambda x: int(Decimal(x).log10() * M) % M
A = f(2)
k = (10**(len(str(n)) - 1)).bit_length()
c = A * k % M
l = max(f(n) - 99, 0)
r = (f(n + 1) - 99) % M
print(k + (not l <= c <= r and g(A, M, (l - c) % M, (r - c) % M)))
