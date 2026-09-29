from math import comb
n, m = map(int, input().split())
print(sum(comb(n, k) for k in range(m, n + 1)))
