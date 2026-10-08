from math import atan2, degrees
from bisect import bisect_left, bisect_right
n, a, x, y, *p = map(int, open(0).read().split())
e = 1e-9
b = sorted(degrees(atan2(p[i + 1] - y, p[i] - x)) for i in range(0, 2 * n, 2))
b += [v + 360 for v in b]
t = [bisect_right(b, v + a + e) for v in b]
i = min(range(n, 2 * n), key=lambda i: i - bisect_left(b, b[i] - a - e))
r = n
for s in range(bisect_left(b, b[i] - a - e), i + 1):
    s %= n
    j = s
    c = 0
    while j < s + n:
        j = t[j]
        c += 1
    r = min(r, c)
print(r)
