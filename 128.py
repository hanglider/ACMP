n, a, b, c, d = map(int, open(0).read().split())
s = {a + b * 1j}
k = 0
while c + d * 1j not in s:
    s |= {w for z in s for v in (1 + 2j, 2 + 1j, 1 - 2j, 2 - 1j) for w in (z + v, z - v) if 0 < w.real <= n and 0 < w.imag <= n}
    k += 1
print(k)
