from math import comb
n, a, b = map(int, input().split())
print(comb(a + n, n) * comb(b + n, n))
