k, n = map(int, input().split())
a = b = 0
c = k
for _ in range(n - 1):
    m = a + b + c
    a, b, c = b, c, max(5 * i + (m - 3 * i) // 5 * 9 for i in range(5) if 3 * i <= m)
print(a + b + c)
