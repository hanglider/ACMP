from math import gcd
n, *a = map(int, open(0).read().split())
print(len({(x // gcd(x, y), y // gcd(x, y)) for x, y in zip(a[::2], a[1::2]) if x or y}))
