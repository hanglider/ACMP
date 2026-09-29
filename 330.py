a, b, c, d = map(int, open(0).read().split())
x = abs(a - c)
y = abs(b - d)
print((x + y + 1) % 2 * (1 + (x != y)))
