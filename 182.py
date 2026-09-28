a = [*map(int, input().split())]
p = [complex(*a[i:i + 2]) for i in (0, 2, 4)]
for i in range(3):
    x, y, z = p[i:] + p[:i]
    if ((y - x) * (z - x).conjugate()).real == 0:
        d = y + z - x
print(int(d.real), int(d.imag))
