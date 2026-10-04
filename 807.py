from math import comb
n = int(input())
a = [1]
for m in range(1, n + 1):
    a += [sum((-1)**(k + 1) * comb(m, k) * 2**(k * (m - k)) * a[m - k] for k in range(1, m + 1))]
print(a[n])
