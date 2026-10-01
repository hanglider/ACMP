from math import isqrt
a, b, c, d, x, y, r = map(int, open(0).read().split())
s = 0
for i in range(max(a, x - r), min(c, x + r) + 1):
    k = isqrt(r * r - (i - x)**2)
    s += max(0, min(d, y + k) - max(b, y - k) + 1)
print(s)
