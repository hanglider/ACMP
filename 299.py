from math import comb
a, b = sorted(map(int, input().split(':')))
print(comb(24 + a, a) if a < 24 else comb(48, 24) * 2**(a - 24))
