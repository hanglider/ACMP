n = int(input())
print(max(k for k in range(1, 45000) if k * (k + 1) // 2 <= n and (n - k * (k - 1) // 2) % k < 1))
