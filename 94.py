n, m, k = map(int, input().split())
print(1 if m <= n else 'NO' if n <= k else 1 - (n - m) // (n - k))