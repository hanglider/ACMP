n, *d = map(int, open(0).read().split())
z = 1e-9 + 1e-9j + sum(s * 1j**((3 - k) / 2) for k, s in zip(d[::2], d[1::2]))
print('%.3f %.3f' % (z.real, z.imag))
