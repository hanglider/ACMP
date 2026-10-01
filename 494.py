x, y, u, v = map(int, input().split())
a = x * x + y * y
b = u * u + v * v
p = x * (x - u) + y * (y - v)
q = (u - x)**2 + (v - y)**2
n, q = (a * q - p * p, q) if 0 < p < q else (min(a, b), 1)
print(sum((n <= r * r * q) * (r * r <= a) + (n < r * r * q) * (r * r <= b) for r in range(1, 1500)))
