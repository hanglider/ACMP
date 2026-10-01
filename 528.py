n, k = map(int, input().split())
k += 1
print(((n - 2) * k * k - (n - 4) * k) // 2)
