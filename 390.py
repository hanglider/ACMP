a, b, c, d, e, f, x, y = map(int, open(0).read().split())
p = [a + b * 1j, c + d * 1j, e + f * 1j]
print(min(abs(((x + y * 1j - u) / (v - u)).imag * abs(v - u)) for u, v in zip(p, p[1:] + p)))
