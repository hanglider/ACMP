n, p, q, r = map(int, open(0).read().split())
k = p + q + r - n
b = max(0, k - r)
c = max(0, k - p)
a = k - b - c
if a < max(0, k - q):
    print('NO')
else:
    print('YES')
    print(a, p - a - b, b, q - b - c, c, r - a - c)
