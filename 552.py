_, *a = map(int, open(0).read().split())
x = y = z = 0
for v in a:
    z += y * v
    y += x * v
    x += v
print(z)
