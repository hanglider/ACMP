r, n, q, x, y, a, b = map(int, open(0).read().split())
s = __import__('math').isqrt((r + q)**2 * (a * a + b * b))
w = 1000 * b
t = 0
for i in range(n):
    k = 1000 * (x * b + (i - y) * a)
    l = max(-i, -((s - k) // w))
    h = min(i, (k + s) // w)
    t += max(0, (h - i) // 2 + (i - l) // 2 + 1)
print(t)
