from math import comb, factorial as F
n, k = map(int, input().split())
m = n - k
D = [1, 0]
for i in range(2, m + 1):
    D.append((i - 1) * (D[i - 1] + D[i - 2]))
print(comb(n, k) * D[m])
