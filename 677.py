from fractions import Fraction as F
k, n, m, d = map(int, input().split())
s = 1 - F(1, k) - F(1, n) - F(1, m)
x = d / s if s > 0 else F(1, 2)
print(x if x.denominator == 1 and x % k == x % n == x % m == 0 else -1)
