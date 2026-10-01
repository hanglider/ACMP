m, n, x, y = map(int, input().split())
if (m + n + x + y) % 2 or (m, n) == (x, y):
    print(0)
elif abs(m - x) == abs(n - y):
    print(1)
else:
    a = (m - n + x + y) // 2
    b = x + y - a
    if not 0 < a < 9 > b > 0:
        a = (m + n + x - y) // 2
        b = m + n - a
    print(2)
    print(a, b)
