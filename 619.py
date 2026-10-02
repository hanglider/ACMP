from math import comb
n, q = map(int, input().split())
print(sum((-1)**k * comb(n, k) * comb(q - 6 * k - 1, n - 1) for k in range((q - n) // 6 + 1)) / 6**n)
