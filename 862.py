n, m = map(int, input().split())
k = min(n, m)
a = n // m * m * (m - 1) // 2 + n % m * (n % m + 1) // 2 + n * m
i = 1
while i <= k:
    q = m // i
    j = min(k, m // q)
    a -= q * (i + j) * (j - i + 1) // 2
    i = j + 1
print(a)
