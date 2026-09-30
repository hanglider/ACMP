a = list(map(int, open(0).read().split()))
p = list(zip(a[::2], a[1::2]))
print(sum(any((x - 25 * c)**2 + y * y <= 100 for x, y in p) for c in range(5)))
