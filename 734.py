n, k = map(int, input().split())
m = n // 2
print(sum(k**i for i in range(m + 1, n + 1)))
print(k**m + 1 if n % 2 < 1 else 1)
