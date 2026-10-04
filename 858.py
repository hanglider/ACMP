a, b, c, d, e, f, g, h, i = map(int, open(0).read().split())
x = d * h - e * g
y = g * b - h * a
z = a * e - b * d
n = 1000 * (c * x + f * y + i * z)**2 // abs(2 * x * y * z)
print(f'{n // 1000}.{n % 1000:03}')
