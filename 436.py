n, k = map(int, input().split())
m = max(k, 1)
b = 0, -m - 1
for d in [d for d in [*range(m + 1, int(n**.5) + 2), n - k, n // m - 1, k + 1] if d > m and n % d == k]:
    x = n
    l = 0
    while x and x % d == k:
        x //= d
        l += 1
    b = max(b, (l, -d))
print(-b[1], b[0])
