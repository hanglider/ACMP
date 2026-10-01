a, b, c = map(float, input().split())
m = 0
for a, b, c in (a, b, c), (b, c, a), (c, a, b):
    p = (b * b + c * c - a * a) / 2 / c
    h = abs(b * b - p * p)**.5
    k = max(p, c - p)
    m = max(m, min(k, c * c / k) * h / 2, c * c / 4 * (k <= h))
print(m)
