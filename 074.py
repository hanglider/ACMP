n, m = map(int, input().split())
k = n
while m % 2 * m > 1:
    k -= k // 2
    m = m // 2 + 1
print(n - k + m // 2 or n)
