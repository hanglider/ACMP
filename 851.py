m, n = map(int, input().split())
k = min(m, n // 2)
print("BGG" * k + "B" * (m > k) + "G" * (n - 2 * k) + "B" * (m - k - 1))
