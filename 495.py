n, *a = map(int, open(0).read().split())
z = [p + q * 1j for p, q in zip(a[:-1:2], a[1::2])]
for _ in range(a[-1]):
    z = [(z[i] + z[i - 1]) / 2 for i in range(n)]
print(sum(abs(z[i] - z[i - 1]) for i in range(n)))
