n, k = map(int, input().split())
print(n**n - k * (n - 1) + 4 * (n < 3))
