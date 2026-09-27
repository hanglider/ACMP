from math import comb
x, k = map(int, input().split())
print(comb(x // 5 + k, k))
